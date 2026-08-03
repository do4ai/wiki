---
title: "03. 관측과 SRE"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b9810a9075d5d9e176d8fd__03. 관측과 SRE
notion_id: 330e313f58b9810a9075d5d9e176d8fd
notion_url: https://www.notion.so/330e313f58b9810a9075d5d9e176d8fd
parent_notion_id: 330e313f58b9802b9cedda8dcbc5d112
---
# 03. 관측과 SRE

운영에서 **가장 중요한 섹션**이다. "어떤 관측 솔루션이 있고 / 어디로 접속하며 / 무슨 메트릭·로그를 볼 수 있고 / 문제가 나면 어떻게 조치하는가"를 한곳에 모은다. 솔루션 사용 절차는 `Manual`, 서비스 자체 구조는 [02. 서비스 운영](../02. 서비스 운영/index.md).

## 관측 솔루션 · 접속 URL 일람

| 솔루션 | 접속 | 무엇을 보나 |
| --- | --- | --- |
| **Grafana** | `grafana.do4ai.com` (NodePort 30300) | 메트릭 대시보드(서비스 운영·APM), 트레이스 Explore |
| **Prometheus** | `prometheus.do4ai.com` (basic-auth) | 메트릭 원본 쿼리(PromQL)·스크레이프 타겟 |
| **Loki** | Grafana Explore | 로그 조회(`{namespace="<ns>"}`) |
| **Alerta** | `alerta.do4ai.com` | 인시던트 허브(알림 집계·상태) → Discord |
| **Tempo** | Grafana 내 데이터소스(Explore) | 분산 트레이스(요청 구간별 지연·오류) |
| **(ArgoCD)** | `argocd.do4ai.com` | 배포 상태(Sync/Health) — [01. 인프라](../01. 인프라와 플랫폼/05. ArgoCD 운영 흐름 가이드/index.md) |
| **(Headlamp)** | `headlamp.do4ai.com` | 리소스/이벤트/로그 빠른 점검 |

> ⚠️ 일부 기본 계정이 평문(`Admin12!`)이고 Loki/Tempo/Alerta는 replica 1(SPOF). 개선 과제는 각 문서에 ⚠️로 표시.

## 문서 맵 (읽는 순서)

| # | 문서 | 핵심 |
| --- | --- | --- |
| 01 | [Observability 운영 가이드](01. Observability 운영 가이드/index.md) | 메트릭·로그·트레이스를 보는 순서(개요) |
| 02 | [메트릭 - Prometheus와 Grafana](02. 메트릭 - Prometheus와 Grafana/index.md) | 수집·대시보드 |
| 03 | [알림 - Alertmanager와 Alerta](03. 알림 - Alertmanager와 Alerta/index.md) | 알림 → Alerta → Discord, 규칙 인벤토리 |
| 04 | [로그 - Loki와 Alloy](04. 로그 - Loki와 Alloy/index.md) | 로그 수집·조회·로그기반 알림 |
| 05 | [트레이싱 - OpenTelemetry와 Tempo](05. 트레이싱 - OpenTelemetry와 Tempo/index.md) | 분산 트레이싱·APM |
| 06 | [모니터링·알림 아키텍처 가이드](06. 모니터링·알림 아키텍처 가이드/index.md) | 전체 파이프라인 한눈에 |
| 07 | [서비스별 관측과 조치](07. 서비스별 관측과 조치/index.md) | **서비스마다 대시보드 URL·메트릭·로그·알림·조치** |
| 08 | [SLO·SLI와 에러 버짓 가이드](08. SLO·SLI와 에러 버짓 가이드/index.md) | 건강 기준·번레이트 |
| 09 | [알림에서 인시던트, 에스컬레이션까지](09. 알림에서 인시던트, 에스컬레이션까지/index.md) | severity·온콜·에스컬레이션 |
| 10 | [장애 대응 의사결정 가이드](10. 장애 대응 의사결정 가이드/index.md) | 롤백·핫픽스·대기 판단 |
| 11 | [운영 장애 Discord 리포트 솔루션 리서치](11. 운영 장애 Discord 리포트 솔루션 리서치/index.md) | 설계 배경(참고) |
| 12 | [k3s 운영 장애 Discord 리포트 설계](12. k3s 운영 장애 Discord 리포트 설계/index.md) | 설계 배경(참고) |
| 13 | [디스코드 알림 채널과 웹훅 구성](13. 디스코드 알림 채널과 웹훅 구성/index.md) | **웹훅 키 5종·실채널 4개·메시지 형태·시크릿 위치·알려진 결함** |

**검수/온콜 빠른 진입**: 특정 서비스가 궁금하면 → **07. 서비스별 관측과 조치**에서 그 서비스의 대시보드 URL·메트릭·로그·조치를 바로 본다.

## Page Tree

- [01. Observability 운영 가이드](01. Observability 운영 가이드/index.md)
- [02. 메트릭 - Prometheus와 Grafana](02. 메트릭 - Prometheus와 Grafana/index.md)
- [03. 알림 - Alertmanager와 Alerta](03. 알림 - Alertmanager와 Alerta/index.md)
- [04. 로그 - Loki와 Alloy](04. 로그 - Loki와 Alloy/index.md)
- [05. 트레이싱 - OpenTelemetry와 Tempo](05. 트레이싱 - OpenTelemetry와 Tempo/index.md)
- [06. 모니터링·알림 아키텍처 가이드](06. 모니터링·알림 아키텍처 가이드/index.md)
- [07. 서비스별 관측과 조치](07. 서비스별 관측과 조치/index.md)
- [08. SLO·SLI와 에러 버짓 가이드](08. SLO·SLI와 에러 버짓 가이드/index.md)
- [09. 알림에서 인시던트, 에스컬레이션까지](09. 알림에서 인시던트, 에스컬레이션까지/index.md)
- [10. 장애 대응 의사결정 가이드](10. 장애 대응 의사결정 가이드/index.md)
- [11. 운영 장애 Discord 리포트 솔루션 리서치](11. 운영 장애 Discord 리포트 솔루션 리서치/index.md)
- [12. k3s 운영 장애 Discord 리포트 설계](12. k3s 운영 장애 Discord 리포트 설계/index.md)
- [13. 디스코드 알림 채널과 웹훅 구성](13. 디스코드 알림 채널과 웹훅 구성/index.md)

---

> **온보딩 트랙 — 3부 관측과 SRE**
> 이전: [wiki — 운영 절차](../02. 서비스 운영/wiki 서비스 가이드/3. 운영 절차/index.md) · 다음: [Observability 운영 가이드](01. Observability 운영 가이드/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../시작하기/index.md)
