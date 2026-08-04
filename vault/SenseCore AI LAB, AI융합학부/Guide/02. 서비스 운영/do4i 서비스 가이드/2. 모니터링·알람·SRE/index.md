---
title: "2. 모니터링·알람·SRE"
---
# do4i 모니터링·알람·SRE

## 모니터링·관측

- **대시보드**: Grafana `do4i-api-operations`(가용 replica·재시작·5xx·CPU·메모리), `platform-api-apm`(요청율·에러율·p95).
- **로그**: Alloy → Loki → Grafana Explore. 에러/5xx 버스트는 Loki ruler가 감지한다.
- **트레이스**: OTel → Tempo(`do4i-api` 스팬).
- **보는 순서**: 메트릭(범위) → 로그(원인) → 트레이스(병목). 전체 파이프라인은 [모니터링·알림 아키텍처 가이드](../../../03. 관측과 SRE/06. 모니터링·알림 아키텍처 가이드/index.md).

## 장애 알람 (이 서비스에 걸린 규칙)

모두 Alertmanager → Alerta → Discord.

| 알림 | 조건 | 심각도 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable | `do4i/api` 가용 replica < desired (5m) | critical |
| PlatformAppIngress5xxRatioHigh | `api-ingress` 5xx 비율 > 5% (5m) | major |
| PlatformAppServerErrorRateHigh | `do4i-api` 서버 에러율 > 10% (10m) | major |
| PlatformAppServerLatencyP95High | `do4i-api` p95 > 1500ms (10m) | warning |
| PlatformPodCrashLooping / OOMKilled / CPUThrottling | 워크로드 런타임 이상 | critical~warning |
| PlatformMySQLNotReady | `do4i/mysql` Ready 0 (5m) | critical |
| PlatformAvailabilitySLO*Burn | 가용성 에러버짓 소진 | critical/warning |

## SRE·SLO

- **가용성 SLO**: `TODO(확정 필요)` 제안값 99.9%(월 에러버짓 0.1%). 5xx 비율로 측정, 멀티윈도 번레이트로 감시.
- **지연 SLO**: `TODO(확정 필요)` 제안값 p95 < 1500ms.
- **확장**: API는 HPA로 트래픽 대응, 아바타 워커는 세션 부하에 따라 10~100 스케일.
- 개념·기준은 [SLO·SLI와 에러 버짓 가이드](../../../03. 관측과 SRE/08. SLO·SLI와 에러 버짓 가이드/index.md).

## 1차 확인 포인트

1. ArgoCD에서 `do4i` Application Sync/Health.
2. `do4i` 네임스페이스 파드(api/mysql/avatar-worker).
3. Grafana `do4i-api-operations` → 5xx·재시작·리소스.
4. Grafana Explore에서 `{namespace="do4i"}` 로그 에러.

상세 절차: [3. 운영 절차](../3. 운영 절차/index.md).

---

> **온보딩 트랙 2부. 서비스 운영**
> 이전: [do4i 아키텍처와 배포](../1. 아키텍처와 배포/index.md) · 다음: [do4i 운영 절차](../3. 운영 절차/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../../시작하기/index.md)
