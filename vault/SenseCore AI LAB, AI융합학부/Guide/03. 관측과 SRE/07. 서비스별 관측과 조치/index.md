---
title: "07. 서비스별 관측과 조치"
---
# 07. 서비스별 관측과 조치

서비스마다 **어디서(대시보드 URL) / 무슨 메트릭·로그를 보고 / 어떤 알림이 걸려 있고 / 무엇을 조치하는지**를 한 장씩 정리한다. 검수·온콜 시 그 서비스 페이지만 펴면 된다.

## 한눈 매트릭스

| 서비스 | 네임스페이스 | Grafana 대시보드 | Loki 쿼리 | 대표 알림 |
| --- | --- | --- | --- | --- |
| [do4i](do4i 관측과 조치/index.md) | `do4i` | `do4i-api-operations`, `platform-api-apm`(do4i-api) | `kubernetes.namespace:do4i` | 배포가용성·5xx·APM·MySQL |
| [passv](passv 관측과 조치/index.md) | `passv`(이전 중) | `platform-api-apm`(passv-api) | `kubernetes.namespace:passv` | 발화 실패(앱 Alerta)·5xx·APM |
| [palcar](palcar 관측과 조치/index.md) | `palcar` | `platform-api-apm`(palcar-api) | `kubernetes.namespace:palcar` | 배포가용성·5xx·APM |
| [papersens](papersens 관측과 조치/index.md) | `papersens` | `papersens-operations` | `kubernetes.namespace:papersens` | 5xx·OOM(메모리)·LLM 실패 |
| [wiki](wiki 관측과 조치/index.md) | `atlas` | (blackbox 합성) | `kubernetes.namespace:atlas` | EndpointDown·콘텐츠 동기화 |

## 공통 접속
- 메트릭/대시보드: `grafana.do4ai.com` (NodePort 30300) — 좌측 Dashboards에서 위 이름 검색.
- 로그: Grafana Explore(데이터소스 Loki) — `{namespace="<ns>"}` + 시간범위.
- 트레이스: Grafana → Explore → Tempo 데이터소스(서비스/지연으로 검색).
- 알림 상태: `alerta.do4ai.com`.
- 솔루션 상세는 [02. 메트릭](../02. 메트릭 - Prometheus와 Grafana/index.md)·[04. 로그](../04. 로그 - Loki와 Alloy/index.md)·[05. 트레이싱](../05. 트레이싱 - OpenTelemetry와 Tempo/index.md).

## Page Tree

- [do4i 관측과 조치](do4i 관측과 조치/index.md)
- [passv 관측과 조치](passv 관측과 조치/index.md)
- [palcar 관측과 조치](palcar 관측과 조치/index.md)
- [papersens 관측과 조치](papersens 관측과 조치/index.md)
- [wiki 관측과 조치](wiki 관측과 조치/index.md)

---

> **온보딩 트랙 — 3부 관측과 SRE**
> 이전: [모니터링·알림 아키텍처 가이드](../06. 모니터링·알림 아키텍처 가이드/index.md) · 다음: [do4i 관측과 조치](do4i 관측과 조치/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../../시작하기/index.md)
