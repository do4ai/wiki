---
title: "palcar 관측과 조치"
---
# palcar — 관측과 조치

자동차 경매 워크플로 palcar(namespace `palcar`).

## 접속
- **메트릭**: `grafana.do4ai.com` → `platform-api-apm`(service `palcar-api`) + 공통(kubernetes-cluster·nginx-ingress).
- **로그**: Grafana Explore → `{namespace="palcar"}`.
- **트레이스**: Grafana Explore → Tempo, service `palcar-api`.
- **배포 상태**: `argocd.do4ai.com` → `palcar`.

## 볼 수 있는 메트릭·로그
- ingress `palcar` 5xx율, api/mysql 리소스·재시작, APM 요청율·에러율·p95. `/health`·`/api` 경로 응답.
- 로그: DB 연결 실패/환경변수·secret 누락/startup/외부 연동 + 액세스로그 5xx.

## 이 서비스에 걸린 알림 → 조치
| 알림 | 의미 | 조치 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable(palcar/api) | 가용 replica 부족 | 파드/이벤트 → 원인별 대응, 직전 배포면 롤백 |
| PlatformAppIngress5xxRatioHigh(palcar) | 5xx 급증 | `/health`·`/api` 분리 확인 → api·mysql 로그 |
| PlatformAppServerErrorRateHigh / LatencyP95High(palcar-api) | 에러율·지연 | APM·로그, DB 의존성 확인 |
| 런타임 공통(CrashLoop/OOM/throttle/MySQLNotReady) | 워크로드 이상 | 로그·리소스, DB Ready 확인 |

## 더 보기
- 서비스 구조: [palcar 서비스 가이드](../../../02. 서비스 운영/palcar 서비스 가이드/index.md)
- 손절차: [palcar 운영 절차](../../../02. 서비스 운영/palcar 서비스 가이드/3. 운영 절차/index.md)

---

> **온보딩 트랙 — 3부 관측과 SRE**
> 이전: [passv 관측과 조치](../passv 관측과 조치/index.md) · 다음: [papersens 관측과 조치](../papersens 관측과 조치/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../../../시작하기/index.md)
