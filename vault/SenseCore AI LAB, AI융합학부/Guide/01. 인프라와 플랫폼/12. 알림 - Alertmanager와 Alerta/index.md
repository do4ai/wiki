---
title: "12. 알림 - Alertmanager와 Alerta"
---
# 12. 알림 — Alertmanager와 Alerta

장애 신호를 모아 디스코드로 보내는 알림 파이프라인이다. 전체 그림은 [모니터링·알림 아키텍처 가이드](../../03. 데이터, 관측, 보안/모니터링·알림 아키텍처 가이드/index.md), 도구 사용법은 [Manual 06. Alerta 사용법](../../../Manual/06. 모니터링-로그 작업/Alerta 사용법/index.md).

```
Prometheus 규칙 ─ Alertmanager ─┐
ElastAlert(로그)  ───────────────┤
ArgoCD Notifications ────────────┤
                                 ▼
                            Alerta (인시던트 허브, PostgreSQL)
                                 │ Discord 플러그인
                                 ▼
                              디스코드
```

## Alertmanager (kube-prometheus-stack 내장)
- **라우팅**(`AlertmanagerConfig`): 수신자 `alerta`(webhook), groupBy `alertname/service/instance`, groupWait **30s**, groupInterval **5m**, repeat **2h**.
- **매칭**: `severity =~ warning|critical|major|minor`, `Watchdog`/`InfoInhibitor` 제외.
- **전송**: `http://alerta.monitoring.svc.cluster.local:8080/api/webhooks/prometheus` (Key 인증, `alerta-secrets`의 `ADMIN_KEY`). 스토리지 5Gi.

## Alerta (인시던트 허브)
- **이미지**: `alerta/alerta-web:9.1.0`, replicas 1. **DB**: `postgres:16-alpine`(StatefulSet, 10Gi).
- **접속**: `alerta.do4ai.com` (AUTH_REQUIRED). 시크릿은 Infisical `/platform/incident-alerting`(`alerta-secrets`)에서 주입(ADMIN/API key/DB/Discord webhook).
- **플러그인**: `blackout, heartbeat, discord`. Discord 플러그인이 severity 색상으로 채널에 게시.
- **들어오는 경로**: Alertmanager(메트릭), ElastAlert(로그 버스트), ArgoCD Notifications(sync/health). 앱이 직접 보내기도 함(passv 발화 실패 → `/api/alert`).

## blackbox-exporter (합성 모니터링)
- **이미지**: `prom/blackbox-exporter:v0.25.0`, 모듈 `http_2xx`, 60s.
- **대상**: `agents.do4i.com/api/health`, `wiki.do4ai.com/healthz`, `app.passv.co.kr`, `api.passv.co.kr/api/health`, `pc.do4ai.com/health`.

## 알림 규칙 인벤토리 (`monitoring/manifests`)
| 파일 | 그룹 / 주요 알림 |
| --- | --- |
| `platform-alert-rules.yaml` | app-health(배포 가용성·ingress 5xx), apm-health(에러율·p95), observability-runtime(Alerta/OTel/Tempo/Filebeat 상태) |
| `platform-runtime-alerts.yaml` | workload-health(CrashLoop·OOMKilled·CPU throttling·MySQL Ready0), capacity(PVC·노드 Memory/Disk Pressure) |
| `platform-slo-rules.yaml` | SLO 레코딩(5m/30m/1h/6h) + 번레이트(fast/slow, 목표 99.9%) |
| `blackbox-exporter.yaml` | EndpointDown, SSLCertExpiringSoon |

모든 규칙은 `severity/environment/service/instance/group` 라벨을 공유해 별도 설정 없이 같은 파이프라인을 탄다.

## 1차 확인 포인트
1. 디스코드 알림 → Alerta(`alerta.do4ai.com`)에서 같은 service/alertname 묶음 확인(진짜 영향 vs 노이즈).
2. 알림이 안 오면: Alertmanager→Alerta webhook, Alerta 파드/DB, Discord webhook 순으로 점검.
3. 판단·에스컬레이션은 [04. 장애 대응과 운영 판단](../../04. 장애 대응과 운영 판단/index.md).
