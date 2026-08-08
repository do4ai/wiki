---
title: "03. 알림 - Alertmanager와 Alerta"
---
# 03. 알림 - Alertmanager와 Alerta

장애 신호를 모아 디스코드로 보내는 알림 파이프라인이다. 전체 그림은 [모니터링·알림 아키텍처 가이드](../06. 모니터링·알림 아키텍처 가이드/index.md), 도구 사용법은 [Manual 06. Alerta 사용법](../../../Manual/06. 모니터링-로그 작업/Alerta 사용법/index.md).

**디스코드 쪽 구성**(웹훅 키 다섯 종과 실제 채널 네 개, 운영·개발 채널 분리, 메시지 형태, 시크릿 위치)은 [13. 디스코드 알림 채널과 웹훅 구성](../13. 디스코드 알림 채널과 웹훅 구성/index.md)에 따로 정리했다.

```
Prometheus 규칙 ─ Alertmanager ─┐
Loki ruler(로그)  ──────────────┤
ArgoCD Notifications ────────────┤
                                 ▼
                            Alerta (인시던트 허브, PostgreSQL)
                                 │ Discord 플러그인
                                 ▼
                              디스코드
```

> **Grafana는 알림을 보내지 않는다.** Grafana Unified Alerting은 쓰지 않고(규칙 0개), 알림 판단은 Prometheus 규칙과 Loki ruler가 하고 전달은 Alertmanager → Alerta → Discord가 맡는다. Grafana는 알림을 받은 뒤 원인을 파고들 때 쓰는 조회 화면이다.

## Alertmanager (kube-prometheus-stack 내장)
- **라우팅**(`AlertmanagerConfig`): 수신자 `alerta`(webhook), groupBy `alertname/service/instance`, groupWait **30s**, groupInterval **5m**, repeat **2h**.
- **매칭**: `severity =~ warning|critical|major|minor`, `Watchdog`/`InfoInhibitor` 제외.
- **전송**: `http://alerta.monitoring.svc.cluster.local:8080/api/webhooks/prometheus` (Key 인증, `alerta-secrets`의 `ADMIN_KEY`). 스토리지 5Gi.

## Alerta (인시던트 허브)
- **이미지**: `alerta/alerta-web:9.1.0`, replicas 1. **DB**: `postgres:16-alpine`(StatefulSet, 10Gi).
- **접속**: `alerta.do4ai.com` (AUTH_REQUIRED). 시크릿은 Infisical `/platform/incident-alerting`(`alerta-secrets`)에서 주입(ADMIN/API key/DB/Discord webhook).
- **플러그인**: `blackout, heartbeat, discord`. Discord 플러그인이 severity 색상으로 채널에 게시.
- **들어오는 경로**: Alertmanager(메트릭·로그 버스트), ArgoCD Notifications(sync/health).
- ⚠️ **앱 → Alerta 직송 경로는 현재 죽어 있다.** 코드에는 `/api/alert` 헬퍼가 있으나 어느 파드에도 `ALERTA_API_KEY`가 주입되지 않아 전송이 no-op이다. 앱 런타임 오류는 대신 `platform_runtime`이 디스코드로 직접 보낸다([13. 디스코드 알림 채널과 웹훅 구성](../13. 디스코드 알림 채널과 웹훅 구성/index.md) 참고).

## blackbox-exporter (합성 모니터링)
- **이미지**: `prom/blackbox-exporter:v0.25.0`, 모듈 `http_2xx`, 60s.
- **대상**: `agents.do4i.com/api/health`, `wiki.do4ai.com/healthz`, `app.passv.co.kr`, `api.passv.co.kr/api/health`, `palcar.co.kr/health`.
- ✅ **수집 정상(2026-08-08 확인).** `probe_success` 시계열 8개(공개 5 + 컴포저블 3)가 전부 `1`이고 공개 프로브 5건은 모두 HTTP 200이다. 2026-08-01에 기록했던 라벨 불일치(`Probe` 에 `release: kube-prometheus-stack` 이 없어 `probeSelector` 와 물리지 않던 문제)는 해소됐다. 상세는 [13. 디스코드 알림 채널과 웹훅 구성 — 해소된 결함](../13. 디스코드 알림 채널과 웹훅 구성/index.md).
- 다섯 번째 대상은 원래 `pc.do4ai.com/health` 였다. 이 이름은 은퇴한 별칭이라 DNS에서 회수됐고(NXDOMAIN), 감시 공백이 생기지 않도록 살아 있는 palcar 운영 엣지 `palcar.co.kr/health` 로 교체했다. 이 경로는 CloudFront가 hidden origin으로 넘겨 k3s `api`가 응답하므로 엣지와 백엔드를 한 번에 검사한다.

## 알림 규칙 인벤토리 (`monitoring/manifests`)
| 파일 | 그룹 / 주요 알림 |
| --- | --- |
| `platform-alert-rules.yaml` | app-health(배포 가용성·ingress 5xx), apm-health(에러율·p95), observability-runtime(Alerta/OTel/Tempo 상태), cluster-hygiene(파드 CIDR 잔재), logging-stack(Loki/Alloy·적재 정지) |
| `platform-runtime-alerts.yaml` | workload-health(CrashLoop·OOMKilled·CPU throttling·MySQL Ready0), capacity(PVC·노드 Memory/Disk Pressure) |
| `platform-slo-rules.yaml` | SLO 레코딩(5m/30m/1h/6h) + 번레이트(fast/slow, 목표 99.9%) |
| `blackbox-exporter.yaml` | EndpointDown, SSLCertExpiringSoon |
| `loki.yaml`(loki-rules) | PlatformLogErrorBurst(오류 로그 급증), PlatformLogHttp5xxBurst(5xx 로그 급증). Loki ruler가 평가한다 |

모든 규칙은 `severity/environment/service/instance/group` 라벨을 공유해 별도 설정 없이 같은 파이프라인을 탄다.

## 1차 확인 포인트
1. 디스코드 알림 → Alerta(`alerta.do4ai.com`)에서 같은 service/alertname 묶음 확인(진짜 영향 vs 노이즈).
2. 알림이 안 오면: Alertmanager→Alerta webhook, Alerta 파드/DB, Discord webhook 순으로 점검.
3. 판단·에스컬레이션은 [09. 알림에서 인시던트, 에스컬레이션까지](../09. 알림에서 인시던트, 에스컬레이션까지/index.md).

---

> **온보딩 트랙 3부. 관측과 SRE**
> 이전: [메트릭 - Prometheus와 Grafana](../02. 메트릭 - Prometheus와 Grafana/index.md) · 다음: [로그 - Loki와 Alloy](../04. 로그 - Loki와 Alloy/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../시작하기/index.md)
