---
title: "01. 인프라와 플랫폼"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981a0b738ed69daa8f3a0__01. 인프라와 플랫폼
notion_id: 330e313f58b981a0b738ed69daa8f3a0
notion_url: https://www.notion.so/330e313f58b981a0b738ed69daa8f3a0
parent_notion_id: 330e313f58b9802b9cedda8dcbc5d112
---
# 01. 인프라와 플랫폼

서비스가 돌아가는 **기반 플랫폼**을 다룬다. 클러스터, 배포(GitOps/ArgoCD), 트래픽 입구, 레지스트리, 시크릿, 대시보드가 대상이다. 각 문서는 개념과 **실제 우리 설정(버전·접속·연결)** 을 함께 적는다.

> 관측(메트릭·로그·트레이스)과 SRE(SLO·알림·장애 대응)는 따로 떼어 [03. 관측과 SRE](../03. 관측과 SRE/index.md)에서 다룬다.

## 전체 아키텍처 한눈에

```
Terraform → k3s 클러스터 2개 (do4ai-prod / do4ai-dev)
                  │
         ArgoCD (app-of-apps, GitOps)  ← 레포 변경을 클러스터 상태로 수렴
                  │
   ingress-nginx(입구) · Harbor(이미지) · Infisical(시크릿) · Headlamp(대시보드)
                  │
   서비스(do4i·passv·palcar·papersens·wiki)  → 관측은 03. 관측과 SRE
```

## 읽는 순서

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

---

> **온보딩 트랙 1부. 인프라와 플랫폼**
> 이전: [시작하기: 신입 온보딩](../../시작하기/index.md) · 다음: [Kubernetes 기본 구조 가이드](01. Kubernetes 기본 구조 가이드/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../시작하기/index.md)
