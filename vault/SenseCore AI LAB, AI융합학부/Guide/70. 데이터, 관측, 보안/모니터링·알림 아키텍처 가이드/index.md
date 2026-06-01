---
title: "모니터링·알림 아키텍처 가이드"
---
# 모니터링·알림 아키텍처 가이드

이 문서는 데이터센스 플랫폼의 모니터링과 장애 알림이 **어떤 컴포넌트로, 어떤 경로로** 흐르는지 전체 그림을 설명한다. 개별 도구 사용 절차는 `Manual`에서 다룬다.

## 전체 파이프라인

```
[메트릭]  앱/노드/ingress ─ Prometheus ─┬─ Grafana (대시보드)
                                         └─ Alertmanager ─┐
[로그]    파드 ─ Filebeat ─ Elasticsearch ─┬─ Kibana       │
                                            └─ ElastAlert ──┤
[트레이스] 앱 ─ OTel Collector ─ Tempo ─ Grafana            │
                                                            ▼
                                                    Alerta (인시던트 허브)
                                                            │
                                                            ▼
                                                    Discord (알림 채널)
```

세 가지 신호가 각각 다른 질문에 답한다.

| 신호 | 도구 | 답하는 질문 |
| --- | --- | --- |
| 메트릭 | Prometheus / Grafana | 얼마나 나빠졌는가(범위·추세) |
| 로그 | Filebeat / Elasticsearch / Kibana | 무슨 일이 있었는가(오류 메시지) |
| 트레이스 | OTel / Tempo | 어디서 느려지거나 끊겼는가(병목) |

## 알림이 만들어지고 전달되는 경로

1. **규칙 평가**: Prometheus가 `PrometheusRule`(아래 인벤토리)을 평가해 alert를 발생.
2. **로그 기반**: ElastAlert가 `filebeat-*` 인덱스에서 에러/5xx 버스트를 감지해 직접 Alerta로 전송.
3. **라우팅**: Alertmanager(`AlertmanagerConfig`)가 `severity=~warning|critical|major|minor` alert를 Alerta webhook으로 전달. 그룹핑 키 `alertname/service/instance`, repeat 2h.
4. **인시던트 허브**: Alerta가 알림을 모아 상태(open/ack/closed)를 관리하고 Discord 플러그인으로 채널에 게시.
5. **GitOps 알림**: ArgoCD Notifications가 sync/health 실패를 Alerta로 보낸다.

## 알림 규칙 인벤토리 (gitops `k8s/infra/monitoring/manifests`)

| 파일 | 내용 |
| --- | --- |
| `platform-alert-rules.yaml` | 배포 가용성, ingress 5xx, APM 에러율/지연(p95), Alerta/OTel/Tempo/Filebeat 상태 |
| `platform-runtime-alerts.yaml` | CrashLoopBackOff, OOMKilled, CPU throttling, MySQL Ready 0, PVC 잔여, 노드 Memory/Disk Pressure |
| `platform-slo-rules.yaml` | 가용성 SLO 레코딩 + 멀티윈도 번레이트(fast/slow) |
| `blackbox-exporter.yaml` | 공개 엔드포인트 합성 프로브 + TLS 인증서 만료 임박 |

모든 규칙은 `severity / environment / service / instance / group` 라벨 스키마를 공유한다. 신규 규칙도 같은 스키마를 쓰므로 별도 라우팅 없이 같은 파이프라인을 탄다.

## 접속 지점

- Grafana: `grafana.do4ai.com`(NodePort 30300) — 대시보드.
- Kibana: `kibana.do4ai.com` — 로그.
- Alerta: `monitoring` 네임스페이스 — 인시던트 허브.
- Discord: 운영 알림 채널(`TODO 확정 필요`: 온콜/에스컬레이션 채널 분리).

## 이 문서와 하위 문서의 경계

- 이 문서: 컴포넌트가 **왜·어떻게 연결되는가**.
- 도구별 1차 확인 절차: [Manual/6 Grafana, Kibana, Tempo 1차 장애 확인 절차](../../../Manual/6. 모니터링-로그 작업/Grafana, Kibana, Tempo 1차 장애 확인 절차/index.md).
- 장애 판단·SLO·에스컬레이션: [90. 장애 대응과 운영 판단](../../90. 장애 대응과 운영 판단/index.md).
- Discord 리포트 설계 배경: [k3s 운영 장애 Discord 리포트 설계](../k3s 운영 장애 Discord 리포트 설계/index.md).
