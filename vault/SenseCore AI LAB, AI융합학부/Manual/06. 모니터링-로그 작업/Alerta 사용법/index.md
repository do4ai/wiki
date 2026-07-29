---
title: "Alerta 사용법"
---
# Alerta 사용법

Alerta(`alerta.do4ai.com`)는 모든 알림이 모이는 인시던트 허브다. Prometheus/Alertmanager·ElastAlert·ArgoCD 알림이 여기로 모이고, Discord 플러그인이 디스코드로 게시한다. 전체 파이프라인은 [모니터링·알림 아키텍처 가이드](../../../Guide/03. 관측과 SRE/06. 모니터링·알림 아키텍처 가이드/index.md).

## 무엇을 위해 보나
- 디스코드에 뜬 알림의 상태(open/ack/closed)를 관리하고, 같은 서비스/alertname 묶음을 본다.
- 알림이 진짜 영향인지 노이즈인지 1차 분류(triage).

## 앱이 직접 알림 보내기 (passv 발화 실패 등)
인프라 지표로 안 잡히는 기능 실패는 앱이 Alerta REST API로 직접 보낼 수 있다.

```bash
curl -XPOST https://alerta.do4ai.com/api/alert \
  -H "Authorization: Key <KEY>" -H 'Content-Type: application/json' \
  -d '{"environment":"Production","service":["passv"],"resource":"passv/chat",
       "event":"ChatGenerationFailed","severity":"major","text":"발화 실패"}'
```

### passv 발화 실패 알림 켜기
1. **전용 API 키 발급(ADMIN_KEY 재사용 금지)**: Alerta UI → API Keys에서 `scope=write` 키 생성. 또는
   `curl -XPOST https://alerta.do4ai.com/api/key -H "Authorization: Key <ADMIN_KEY>" -H 'Content-Type: application/json' -d '{"user":"passv","scopes":["write:alerts"],"text":"passv app alerts"}'`
2. 키를 Infisical `do4ai/prod/apps/passv-api`의 `ALERTA_API_KEY`로 저장(EC2면 `.env.production`).
3. passv 설정: `ALERTA_ENABLED=true`, `ALERTA_API_URL=https://alerta.do4ai.com/api` (임계 `ALERTA_CHAT_FAILURE_THRESHOLD`=3, window 300s는 제안값).
4. 검증: 위 curl 스모크 테스트로 디스코드 수신 확인. 구현은 passv `server/shared/infrastructure/alerta.py`.

## 노이즈 제어
- Alerta는 `(environment, resource, event)`로 중복을 묶는다. 앱은 `correlate`·`timeout`을 함께 보내고, 임계/최소 재전송 간격으로 도배를 막는다.

## 함께 보기
- [Grafana, Kibana, Tempo 1차 장애 확인 절차](../Grafana, Kibana, Tempo 1차 장애 확인 절차/index.md) · [Guide/03 09. 알림에서 인시던트, 에스컬레이션까지](../../../Guide/03. 관측과 SRE/09. 알림에서 인시던트, 에스컬레이션까지/index.md)

---

> **온보딩 트랙 — 3부 관측과 SRE**
> 이전: [Grafana, Kibana, Tempo 1차 장애 확인 절차 (Manual)](../Grafana, Kibana, Tempo 1차 장애 확인 절차/index.md) · 다음: [모니터링·알림 아키텍처 가이드](../../../Guide/03. 관측과 SRE/06. 모니터링·알림 아키텍처 가이드/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../../시작하기/index.md)
