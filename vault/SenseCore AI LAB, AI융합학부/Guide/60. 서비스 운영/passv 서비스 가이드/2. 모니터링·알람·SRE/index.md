---
title: "2. 모니터링·알람·SRE"
---
# passv — 모니터링·알람·SRE

## 모니터링·관측

- 플랫폼 공통 스택(Prometheus/Grafana, ElastAlert/ES/Kibana, OTel/Tempo) 사용.
- gitops 편입 후 `passv` 네임스페이스가 알림/대시보드 대상에 포함된다.
- 합성 모니터링: blackbox 프로브가 `app.passv.co.kr`, `api.passv.co.kr/api/health` 점검(`TODO` 대상 확정).

## 발화 실패 앱 레벨 알림 (Alerta 직접 전송)

챗봇 **발화 실패**는 인프라 지표(ingress 5xx·배포 가용성)로 안 잡힌다(200 응답에 오류 본문, 외부 LLM/아바타 실패, 저트래픽 단발 등). 그래서 passv 백엔드가 **Alerta REST API로 직접** 알림을 쏜다.

- 경로: `passv → https://alerta.do4ai.com/api/alert (Key 인증) → Alerta Discord 플러그인 → 디스코드`. **EC2/K8s 어디서든 동작**.
- 구현: `server/shared/infrastructure/alerta.py`의 `notify_chat_failure()`가 `chat_streaming.py` 발화 실패 경로에 연결. 알림 실패는 내부에서 삼켜 본 기능 비차단.
- 노이즈 제어: `(passv/chat, ChatGenerationFailed)` 단위 임계(`ALERTA_CHAT_FAILURE_THRESHOLD`, 제안 5분 3건) + 최소 재전송 간격, Alerta correlate/timeout로 중복 수렴.
- 켜기/키 발급/검증 손절차: [Manual/70 passv 배포 이상 대응 절차](../../../../Manual/70. 서비스별 운영 작업/passv 배포 이상 대응 절차/index.md)의 "발화 실패 앱 레벨 알림" 절.

## 장애 알람 (gitops 편입 후)

신규 런타임/용량/SLO 규칙은 이미 `passv` 네임스페이스를 대상에 포함(CrashLoop, OOM, CPU throttling, PVC, MySQLNotReady, 가용성 번레이트). 컷오버 후 ingress 기반 5xx/지연 알림도 자동 적용.

## SRE·SLO

- **가용성/지연 SLO**: `TODO(확정 필요)` 제안값 99.9% / p95 < 1500ms.
- **확장**: API HPA(min 2 / max 6) 정의 완료(prod overlay). 아바타/음성 워커 분리 배포는 컷오버 단계 결정.
- **데이터 보호**: prod MySQL이 EC2→K8s StatefulSet로 이관되므로 컷오버 런북의 백업·복구 단계가 핵심.

## 1차 확인 포인트

- 현재(EC2): passv 레포 CI(`deploy.yml`/`rollback.yml`)와 EC2 호스트 점검.
- gitops(dev/컷오버 후): ArgoCD `passv` → `passv` 네임스페이스 파드 → Grafana/Kibana.
- 상세: [Manual/70 passv 배포 이상 대응 절차](../../../../Manual/70. 서비스별 운영 작업/passv 배포 이상 대응 절차/index.md).
