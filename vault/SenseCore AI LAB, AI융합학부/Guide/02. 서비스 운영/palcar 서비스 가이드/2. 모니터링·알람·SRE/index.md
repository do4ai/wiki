---
title: "2. 모니터링·알람·SRE"
---
# palcar — 모니터링·알람·SRE

## 모니터링·관측

- 플랫폼 공통 스택 사용. 메트릭/로그/트레이스에서 `palcar` 네임스페이스·`palcar-api` 서비스로 필터.
- 보는 순서: Grafana(5xx·리소스) → Kibana(로그) → Tempo(`palcar-api` 스팬). 전체 흐름은 [모니터링·알림 아키텍처 가이드](../../../03. 관측과 SRE/06. 모니터링·알림 아키텍처 가이드/index.md).

## 장애 알람 (이 서비스에 걸린 규칙)

| 알림 | 조건 | 심각도 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable | `palcar/api` 가용 replica 부족 | critical |
| PlatformAppIngress5xxRatioHigh | `palcar` ingress 5xx > 5% | major |
| PlatformAppServerErrorRateHigh / LatencyP95High | `palcar-api` 에러율·지연 | major/warning |
| 런타임/용량/SLO 공통 규칙 | CrashLoop·OOM·throttle·MySQLNotReady·번레이트 | critical~warning |

## SRE·SLO

- **가용성/지연 SLO**: `TODO(확정 필요)` 제안값 99.9% / p95 < 1500ms.
- **확장**: 기존 1 replica → HPA로 prod 최소 2 replica(HA 개선). 개념은 [SLO·SLI와 에러 버짓 가이드](../../../03. 관측과 SRE/08. SLO·SLI와 에러 버짓 가이드/index.md).

## 1차 확인 포인트

1. ArgoCD `palcar` Sync/Health.
2. `palcar` 네임스페이스 파드(api/mysql), `/health`·`/api` 경로.
3. Grafana 5xx·리소스 → Kibana 로그.

상세 절차: [3. 운영 절차](../3. 운영 절차/index.md).
