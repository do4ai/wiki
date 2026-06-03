---
title: "01. 인프라와 플랫폼"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__01. 인프라와 플랫폼
notion_id: 330e313f58b981a0b738ed69daa8f3a0
notion_url: https://www.notion.so/330e313f58b981a0b738ed69daa8f3a0
parent_notion_id: 330e313f58b9802b9cedda8dcbc5d112
---
# 01. 인프라와 플랫폼

우리가 실제로 구축해 운영하는 서버·클러스터·배포·관측 **솔루션 전부**를 다룬다. 각 문서는 "무엇을 위한 솔루션인지 + 실제 우리 설정(버전·접속·연결)"을 함께 적어, 검수와 운영에 그대로 쓸 수 있게 한다.

## 전체 아키텍처 한눈에

```
                Terraform → k3s 클러스터 2개 (do4ai-prod / do4ai-dev)
                                  │
                         ArgoCD (app-of-apps, GitOps)
                                  │  레포 변경을 클러스터 상태로 수렴
        ┌─────────────────────────┼──────────────────────────────┐
        ▼                         ▼                               ▼
   ingress-nginx            플랫폼 서비스                      관측(Observability)
   (트래픽 입구)        Harbor(이미지)·Infisical(시크릿)      메트릭: Prometheus·Grafana
        │               Headlamp(대시보드)                   알림:  Alertmanager·Alerta→Discord
        ▼                         │                          로그:  Filebeat·ES·Kibana·ElastAlert
   서비스(do4i·passv·palcar·papersens·wiki)                  트레이스: OTel·Tempo
```

## 읽는 순서 (기반 → 배포 → 플랫폼 → 관측)

| # | 문서 | 무엇을 보나 |
| --- | --- | --- |
| 01 | `Kubernetes 기본 구조 가이드` | namespace/deployment/service/ingress 기본 추상화 |
| 02 | `k3s 운영 구조 가이드` | 왜 k3s를 쓰고 어떤 단위로 보는지 |
| 03 | `k3s GitOps 운영 클러스터 초보자 가이드` | 처음 접하는 사람의 진입점 |
| 04 | `GitOps 운영 모델 가이드` | 레포 변경이 어떻게 운영에 반영되는지 |
| 05 | `ArgoCD 운영 흐름 가이드` | Application·sync·health 읽는 법 |
| 06 | `ingress-nginx` | 트래픽 입구(리버스 프록시), 5xx 1차 지점 |
| 07 | `Harbor 컨테이너 레지스트리` | 이미지 보관·배포, ImagePullBackOff 진단 |
| 08 | `Infisical 시크릿 관리 가이드` | 시크릿 저장·주입(InfisicalSecret) |
| 09 | `Headlamp 클러스터 대시보드` | 브라우저로 리소스/로그 둘러보기(읽기 전용) |
| 10 | `Observability 운영 가이드` | 메트릭·로그·트레이스를 어떤 순서로 보는지(개요) |
| 11 | `메트릭 - Prometheus와 Grafana` | 수집·대시보드(kube-prometheus-stack 58.7.2) |
| 12 | `알림 - Alertmanager와 Alerta` | 알림 라우팅 → Alerta → Discord, 규칙 인벤토리 |
| 13 | `로그 - Elasticsearch, Kibana, Filebeat, ElastAlert` | ELK 로그 수집·검색·로그기반 알림 |
| 14 | `트레이싱 - OpenTelemetry와 Tempo` | 분산 트레이싱·APM(스팬 메트릭) |

## 이 섹션의 원칙
- 개념과 **실제 구축 설정**(버전·접속·연결)을 함께 설명한다.
- 도구를 직접 다루는 단계별 절차는 `Manual`(솔루션 사용법)에서 다룬다.
- 평문 시크릿(`Admin12!` 등)·SPOF(ES/Tempo/Alerta replica 1) 같은 개선 과제는 본문에 ⚠️로 표시한다.

## Page Tree

- [01. Kubernetes 기본 구조 가이드](01. Kubernetes 기본 구조 가이드/index.md)
- [02. k3s 운영 구조 가이드](02. k3s 운영 구조 가이드/index.md)
- [03. k3s GitOps 운영 클러스터 초보자 가이드](03. k3s GitOps 운영 클러스터 초보자 가이드/index.md)
- [04. GitOps 운영 모델 가이드](04. GitOps 운영 모델 가이드/index.md)
- [05. ArgoCD 운영 흐름 가이드](05. ArgoCD 운영 흐름 가이드/index.md)
- [06. ingress-nginx](06. ingress-nginx/index.md)
- [07. Harbor 컨테이너 레지스트리](07. Harbor 컨테이너 레지스트리/index.md)
- [08. Infisical 시크릿 관리 가이드](08. Infisical 시크릿 관리 가이드/index.md)
- [09. Headlamp 클러스터 대시보드](09. Headlamp 클러스터 대시보드/index.md)
- [10. Observability 운영 가이드](10. Observability 운영 가이드/index.md)
- [11. 메트릭 - Prometheus와 Grafana](11. 메트릭 - Prometheus와 Grafana/index.md)
- [12. 알림 - Alertmanager와 Alerta](12. 알림 - Alertmanager와 Alerta/index.md)
- [13. 로그 - Elasticsearch, Kibana, Filebeat, ElastAlert](13. 로그 - Elasticsearch, Kibana, Filebeat, ElastAlert/index.md)
- [14. 트레이싱 - OpenTelemetry와 Tempo](14. 트레이싱 - OpenTelemetry와 Tempo/index.md)
