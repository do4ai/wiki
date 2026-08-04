---
title: "Guide"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide
notion_id: 330e313f58b9802b9cedda8dcbc5d112
notion_url: https://www.notion.so/330e313f58b9802b9cedda8dcbc5d112
parent_notion_id: 31ee313f58b980d68c5ad8ed9d5aeff8
---
# SCAI LAB Guide

이 페이지는 SCAI LAB 연구실 운영 전반을 이해하고 활용하기 위한 가이드의 허브다. 실제로 운영 중인 영역만 유지하며, 필요한 문서가 생기면 그때 추가한다.

신입은 [시작하기: 신입 온보딩](../시작하기/index.md)의 온보딩 트랙을 따라 01 → 02 → 03 순서로 읽는다 (트랙 1~3부).

> 섹션 넘버링은 **1부터 연속·두 자리 zero-pad(01, 02, …)**, 같은 레벨은 모두 `NN. 제목/index.md` 폴더로 통일한다. 자세한 규칙은 [Manual 01. SCAI LAB Manual 사용법](../Manual/01. SCAI LAB Manual 사용법/index.md)의 "넘버링 규칙".

[01. 인프라와 플랫폼](01. 인프라와 플랫폼/index.md)
[02. 서비스 운영](02. 서비스 운영/index.md)
[03. 관측과 SRE](03. 관측과 SRE/index.md)

| 섹션 | 무엇을 보나 |
| --- | --- |
| 01. 인프라와 플랫폼 | 기반: 클러스터·GitOps·ArgoCD·ingress·Harbor·Infisical·Headlamp |
| 02. 서비스 운영 | 서비스별(do4i·passv·palcar·papersens·wiki) 아키텍처·운영 |
| 03. 관측과 SRE | **관측 솔루션·URL·메트릭/로그·서비스별 조치 + SLO·인시던트·의사결정** (가장 중요) |

## Page Tree

- [01. 인프라와 플랫폼](01. 인프라와 플랫폼/index.md)
  - [01. Kubernetes 기본 구조 가이드](01. 인프라와 플랫폼/01. Kubernetes 기본 구조 가이드/index.md)
  - [02. k3s 운영 구조 가이드](01. 인프라와 플랫폼/02. k3s 운영 구조 가이드/index.md)
  - [03. k3s GitOps 운영 클러스터 초보자 가이드](01. 인프라와 플랫폼/03. k3s GitOps 운영 클러스터 초보자 가이드/index.md)
  - [04. GitOps 운영 모델 가이드](01. 인프라와 플랫폼/04. GitOps 운영 모델 가이드/index.md)
  - [05. ArgoCD 운영 흐름 가이드](01. 인프라와 플랫폼/05. ArgoCD 운영 흐름 가이드/index.md)
  - [06. ingress-nginx](01. 인프라와 플랫폼/06. ingress-nginx/index.md)
  - [07. Harbor 컨테이너 레지스트리](01. 인프라와 플랫폼/07. Harbor 컨테이너 레지스트리/index.md)
  - [08. Infisical 시크릿 관리 가이드](01. 인프라와 플랫폼/08. Infisical 시크릿 관리 가이드/index.md)
  - [09. Headlamp 클러스터 대시보드](01. 인프라와 플랫폼/09. Headlamp 클러스터 대시보드/index.md)
- [02. 서비스 운영](02. 서비스 운영/index.md)
  - [서비스 공통 1차 대응 절차](02. 서비스 운영/서비스 공통 1차 대응 절차/index.md)
  - [do4i 서비스 가이드](02. 서비스 운영/do4i 서비스 가이드/index.md)
  - [passv 서비스 가이드](02. 서비스 운영/passv 서비스 가이드/index.md)
  - [palcar 서비스 가이드](02. 서비스 운영/palcar 서비스 가이드/index.md)
  - [papersens 서비스 가이드](02. 서비스 운영/papersens 서비스 가이드/index.md)
  - [wiki 서비스 가이드](02. 서비스 운영/wiki 서비스 가이드/index.md)
- [03. 관측과 SRE](03. 관측과 SRE/index.md)
  - [01. Observability 운영 가이드](03. 관측과 SRE/01. Observability 운영 가이드/index.md)
  - [02. 메트릭 - Prometheus와 Grafana](03. 관측과 SRE/02. 메트릭 - Prometheus와 Grafana/index.md)
  - [03. 알림 - Alertmanager와 Alerta](03. 관측과 SRE/03. 알림 - Alertmanager와 Alerta/index.md)
  - [04. 로그 - Loki와 Alloy](03. 관측과 SRE/04. 로그 - Loki와 Alloy/index.md)
  - [05. 트레이싱 - OpenTelemetry와 Tempo](03. 관측과 SRE/05. 트레이싱 - OpenTelemetry와 Tempo/index.md)
  - [06. 모니터링·알림 아키텍처 가이드](03. 관측과 SRE/06. 모니터링·알림 아키텍처 가이드/index.md)
  - [07. 서비스별 관측과 조치](03. 관측과 SRE/07. 서비스별 관측과 조치/index.md)
  - [08. SLO·SLI와 에러 버짓 가이드](03. 관측과 SRE/08. SLO·SLI와 에러 버짓 가이드/index.md)
  - [09. 알림에서 인시던트, 에스컬레이션까지](03. 관측과 SRE/09. 알림에서 인시던트, 에스컬레이션까지/index.md)
  - [10. 장애 대응 의사결정 가이드](03. 관측과 SRE/10. 장애 대응 의사결정 가이드/index.md)
  - [11. 운영 장애 Discord 리포트 솔루션 리서치](03. 관측과 SRE/11. 운영 장애 Discord 리포트 솔루션 리서치/index.md)
  - [12. k3s 운영 장애 Discord 리포트 설계](03. 관측과 SRE/12. k3s 운영 장애 Discord 리포트 설계/index.md)
