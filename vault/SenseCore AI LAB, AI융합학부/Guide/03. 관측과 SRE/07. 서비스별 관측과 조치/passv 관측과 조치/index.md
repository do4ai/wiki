---
title: "passv 관측과 조치"
---
# passv — 관측과 조치

AI 대화형 커머스 passv의 관측. **현재 prod는 EC2, gitops(K8s `passv`)로 이전 중**이라 환경에 따라 보는 곳이 다르다.

## 접속
- **메트릭(K8s 편입 후)**: `grafana.do4ai.com` → `platform-api-apm`(service `passv-api`).
- **로그(K8s)**: `kibana.do4ai.com` → `kubernetes.namespace:passv`. **현재 prod(EC2)**: EC2 호스트 `docker logs passv-server`.
- **트레이스**: Grafana Explore → Tempo, service `passv-api`(편입 후).
- **알림 상태**: `alerta.do4ai.com`.

## 발화 실패는 별도 — 앱 레벨 Alerta 알림
챗봇 **발화 실패는 ingress 5xx로 안 잡힌다**(200+오류 본문, LLM/아바타 실패 등). passv 백엔드가 Alerta로 직접 알림(`ChatGenerationFailed`)을 보낸다.
- 켜기·키 발급·검증: [Manual 06. Alerta 사용법](../../../../Manual/06. 모니터링-로그 작업/Alerta 사용법/index.md), 구현 개요: [passv 서비스 가이드 2. 모니터링·알람·SRE](../../../02. 서비스 운영/passv 서비스 가이드/2. 모니터링·알람·SRE/index.md).

## 이 서비스에 걸린 알림 → 조치
| 알림 | 의미 | 조치 |
| --- | --- | --- |
| ChatGenerationFailed(앱→Alerta) | 발화 실패 임계 초과 | LLM/LiveKit/Simli 의존성·키, 최근 배포 확인 |
| PlatformAppIngress5xx / APM 에러·지연(편입 후) | API 오류·지연 | api 로그·APM, 직전 배포 롤백 검토 |
| 런타임 공통(CrashLoop/OOM/throttle/MySQLNotReady) | 워크로드 이상 | 로그·리소스, DB Ready 확인 |

## 더 보기
- 서비스 구조: [passv 서비스 가이드](../../../02. 서비스 운영/passv 서비스 가이드/index.md)
- 손절차: [passv 운영 절차](../../../02. 서비스 운영/passv 서비스 가이드/3. 운영 절차/index.md) · 컷오버: [Manual 04. passv gitops 이전·컷오버 점검](../../../../Manual/04. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md)
