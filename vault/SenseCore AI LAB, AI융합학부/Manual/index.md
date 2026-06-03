---
title: "Manual"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual
notion_id: 330e313f58b98098b619f0e3ef2d0fa0
notion_url: https://www.notion.so/330e313f58b98098b619f0e3ef2d0fa0
parent_notion_id: 31ee313f58b980d68c5ad8ed9d5aeff8
---
# SCAI LAB Manual

`Manual`은 **운영에 쓰는 솔루션(도구)을 어떻게 쓰는가**를 정리한 곳이다. ArgoCD, kubectl/k3s, Grafana, Kibana, Tempo, Infisical, Harbor, Alerta 같은 도구의 사용·점검 절차를 도구 단위로 모은다.

> 서비스별(do4i·passv·palcar·papersens·wiki) 아키텍처와 그 서비스의 운영 절차는 `Guide`의 [02. 서비스 운영](../Guide/02. 서비스 운영/index.md)에서 서비스 폴더로 본다. **Manual = 도구 사용법, Guide = 서비스.**

## 솔루션별 사용법 (빠른 찾기)

| 솔루션 | 무엇에 쓰나 | 문서 |
| --- | --- | --- |
| ArgoCD | 배포 상태 확인·sync·롤백 | [ArgoCD 사용법](04. 서버와 배포 작업/ArgoCD 사용법/index.md) |
| kubectl · k3s | 클러스터 접속·GitOps 배포 점검 | [k3s 클러스터 접속과 GitOps 배포 점검](04. 서버와 배포 작업/k3s 클러스터 접속과 GitOps 배포 점검/index.md) |
| Harbor | 컨테이너 이미지 레지스트리 | [Harbor 사용법](04. 서버와 배포 작업/Harbor 사용법/index.md) |
| Grafana · Kibana · Tempo | 메트릭·로그·트레이스 확인 | [Grafana, Kibana, Tempo 1차 장애 확인 절차](06. 모니터링-로그 작업/Grafana, Kibana, Tempo 1차 장애 확인 절차/index.md) |
| Alerta | 알림 허브·앱 직접 알림 전송 | [Alerta 사용법](06. 모니터링-로그 작업/Alerta 사용법/index.md) |
| Infisical | 시크릿 반영·권한 변경 | [Infisical 시크릿 반영과 권한 변경 절차](07. 시크릿-권한 작업/Infisical 시크릿 반영과 권한 변경 절차/index.md) |
| Ingress/도메인/환경변수 | 운영 변경 작업 | [Ingress, 도메인, 이미지, 환경 변수 변경 절차](05. 운영 변경 작업/Ingress, 도메인, 이미지, 환경 변수 변경 절차/index.md) |

## 섹션

[01. SCAI LAB Manual 사용법](01. SCAI LAB Manual 사용법/index.md)
[02. 계정 발급과 회수](02. 계정 발급과 회수/index.md)
[03. 외부 로그인 설정](03. 외부 로그인 설정/index.md)
[04. 서버와 배포 작업](04. 서버와 배포 작업/index.md)
[05. 운영 변경 작업](05. 운영 변경 작업/index.md)
[06. 모니터링/로그 작업](06. 모니터링-로그 작업/index.md)
[07. 시크릿/권한 작업](07. 시크릿-권한 작업/index.md)

## Page Tree

- [01. SCAI LAB Manual 사용법](01. SCAI LAB Manual 사용법/index.md)
- [02. 계정 발급과 회수](02. 계정 발급과 회수/index.md)
- [03. 외부 로그인 설정](03. 외부 로그인 설정/index.md)
  - [구글로그인](03. 외부 로그인 설정/구글로그인/index.md)
  - [카카오로그인](03. 외부 로그인 설정/카카오로그인/index.md)
- [04. 서버와 배포 작업](04. 서버와 배포 작업/index.md)
  - [ArgoCD 사용법](04. 서버와 배포 작업/ArgoCD 사용법/index.md)
  - [k3s 클러스터 접속과 GitOps 배포 점검](04. 서버와 배포 작업/k3s 클러스터 접속과 GitOps 배포 점검/index.md)
  - [Harbor 사용법](04. 서버와 배포 작업/Harbor 사용법/index.md)
  - [passv gitops 이전·컷오버 점검](04. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md)
- [05. 운영 변경 작업](05. 운영 변경 작업/index.md)
  - [Ingress, 도메인, 이미지, 환경 변수 변경 절차](05. 운영 변경 작업/Ingress, 도메인, 이미지, 환경 변수 변경 절차/index.md)
- [06. 모니터링/로그 작업](06. 모니터링-로그 작업/index.md)
  - [Grafana, Kibana, Tempo 1차 장애 확인 절차](06. 모니터링-로그 작업/Grafana, Kibana, Tempo 1차 장애 확인 절차/index.md)
  - [Alerta 사용법](06. 모니터링-로그 작업/Alerta 사용법/index.md)
- [07. 시크릿/권한 작업](07. 시크릿-권한 작업/index.md)
  - [Infisical 시크릿 반영과 권한 변경 절차](07. 시크릿-권한 작업/Infisical 시크릿 반영과 권한 변경 절차/index.md)
