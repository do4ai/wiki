---
title: "2. 모니터링·알람·SRE"
---
# papersens — 모니터링·알람·SRE

## 모니터링·관측

- 플랫폼 공통 스택 사용. Grafana `papersens-operations`(가용 replica·재시작·5xx·리소스).
- LLM 외부 호출 실패는 로그(Kibana)·트레이스(Tempo `papersens-api`)에서 확인.

## 장애 알람 (이 서비스에 걸린 규칙)

| 알림 | 조건 | 심각도 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable | `papersens/papersens` 가용 replica 부족 | critical |
| PlatformAppIngress5xxRatioHigh | `papersens-ingress` 5xx > 5% | major |
| PlatformAppServerErrorRateHigh / LatencyP95High | `papersens-api` 에러율·지연 | major/warning |
| 런타임/용량/SLO 공통 규칙 | CrashLoop·OOM(메모리 주의)·throttle·번레이트 | critical~warning |

> papersens는 메모리 사용이 커서 **OOMKilled·CPU throttling 알림**을 특히 주시한다.

## SRE·SLO

- **가용성/지연 SLO**: `TODO(확정 필요)` 제안값 99.9% / 지연은 LLM 호출 특성상 별도 기준 검토(공통 1500ms는 과도할 수 있음).
- **확장**: HPA로 부하 대응하되, 병목이 외부 LLM 호출이면 단순 스케일아웃 효과가 제한적임을 유의.

## 1차 확인 포인트

1. ArgoCD `papersens` Sync/Health.
2. `papersens` 네임스페이스 파드, `/health`(:8082).
3. Grafana 리소스(메모리)·5xx → Kibana 로그(LLM/OpenRouter 오류).

상세 절차: [3. 운영 절차](../3. 운영 절차/index.md).
