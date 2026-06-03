---
title: "do4i 관측과 조치"
---
# do4i — 관측과 조치

에이전트 플랫폼 do4i(namespace `do4i`)의 관측 진입점과 알림별 조치.

## 접속
- **메트릭**: `grafana.do4ai.com` → `do4i-api-operations`(가용 replica·재시작·5xx·CPU/메모리), `platform-api-apm`(서비스 변수 `do4i-api`: 요청율·에러율·p95).
- **로그**: `kibana.do4ai.com` → `kubernetes.namespace:do4i` (+ `error`/`exception` 키워드).
- **트레이스**: Grafana Explore → Tempo, service `do4i-api`.
- **배포 상태**: `argocd.do4ai.com` → `do4i`.

## 볼 수 있는 메트릭
- 가용 replica vs desired, 컨테이너 재시작, ingress `api-ingress` 5xx율, CPU/메모리(요청·제한 대비), APM 요청율·에러율·p95(아바타 워커 메모리 기반 HPA 10~100).

## 볼 수 있는 로그
- `do4i` 네임스페이스의 api·mysql·avatar-worker 로그. DB 연결 실패/마이그레이션/secret 누락/외부 API(OpenAI·LiveKit) 오류를 키워드로 좁힌다.

## 이 서비스에 걸린 알림 → 조치
| 알림 | 의미 | 조치 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable(do4i/api) | 가용 replica 부족 | 파드 상태·이벤트 확인 → ImagePull/CrashLoop 원인별 대응, 직전 배포면 롤백 |
| PlatformAppIngress5xxRatioHigh(api-ingress) | 5xx 급증 | api 로그·APM 에러율 → 직전 배포 의심 시 롤백 |
| PlatformAppServerErrorRateHigh / LatencyP95High(do4i-api) | 서버 에러율/지연 | APM에서 느린 스팬·외부 호출 확인 |
| PlatformMySQLNotReady(do4i) | DB Ready 0 | mysql StatefulSet·PVC·연결 확인(앱과 동시 점검) |
| PlatformPodCrashLooping / OOMKilled / CPUThrottling | 워크로드 이상 | 로그·리소스 limit 확인, OOM이면 메모리 상향 |
| PlatformAvailabilitySLO*Burn | 에러버짓 소진 | fast burn=즉시 롤백/핫픽스, slow burn=원인 조사 |

## 더 보기
- 서비스 구조: [do4i 서비스 가이드](../../../02. 서비스 운영/do4i 서비스 가이드/index.md)
- 손절차: [do4i 운영 절차](../../../02. 서비스 운영/do4i 서비스 가이드/3. 운영 절차/index.md) · 판단: [10. 장애 대응 의사결정](../../10. 장애 대응 의사결정 가이드/index.md)
