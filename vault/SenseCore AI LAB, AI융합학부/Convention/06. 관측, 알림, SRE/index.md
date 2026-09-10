---
title: "06. 관측, 알림, SRE"
---
# 06. 관측, 알림, SRE

관측·알림·장애 대응의 공통 규칙이다. 솔루션 상세와 서비스별 조치는 [Guide 03. 관측과 SRE](../../Guide/03. 관측과 SRE/index.md).

## severity

- 알림 심각도는 **critical / major / warning / minor** 4단계만 쓴다. PrometheusRule과 Alerta가 같은 값을 공유한다.

## 알림 경로

- 메트릭(Prometheus/Alertmanager)·로그(Loki ruler)·배포(ArgoCD Notifications)는 모두 **Alerta로 모이고 Discord로** 전송된다.
- 인프라 지표로 안 잡히는 **앱 레벨 기능 실패(예: 챗봇 발화 실패)는 앱이 Alerta로 직접** 보낸다.

## 알림 규칙 라벨

- 모든 규칙은 `severity / environment / service / instance / group` 라벨 스키마를 공유한다. 새 규칙도 같은 스키마를 따른다(별도 라우팅 불필요).

## SLO

- 기본 목표(제안): API 가용성 **99.9%**, 멀티윈도 번레이트(fast 1h&5m / slow 6h&30m)로 감시. 서비스별 목표는 확정해 명시한다.
- 자세한 기준은 [Guide 03 / SLO·SLI와 에러 버짓 가이드](../../Guide/03. 관측과 SRE/08. SLO·SLI와 에러 버짓 가이드/index.md).

## 인시던트

- 알림은 Alerta에서 상태(open/ack/closed)를 관리한다.
- 마무리 시 **원인 1줄·조치 1줄·재발 방지 1줄**을 남긴다. 판단 기준은 [장애 대응 의사결정 가이드](../../Guide/03. 관측과 SRE/10. 장애 대응 의사결정 가이드/index.md).

---

> **온보딩 트랙 — 4부 운영 변경과 컨벤션**
> 이전: [시크릿과 보안](../05. 시크릿과 보안/index.md) · 다음: [코드 규칙](../07. 코드 규칙/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../시작하기/index.md)
