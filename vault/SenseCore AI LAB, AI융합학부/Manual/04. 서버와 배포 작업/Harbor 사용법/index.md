---
title: "Harbor 사용법"
---
# Harbor 사용법

컨테이너 이미지 레지스트리 Harbor(`harbor.do4i.com`) 사용법이다. do4i·palcar 등은 harbor 이미지를 쓰고, papersens·passv 일부는 ECR을 쓴다.

## 무엇을 위해 보나
- 배포 이미지의 태그/다이제스트가 실제로 레지스트리에 있는지 확인.
- `ImagePullBackOff`의 원인(태그 오타, 권한, 미푸시) 분리.

## 접속
- UI: `harbor.do4i.com` (프로젝트 `do4ai`). 기본 계정은 Infisical 관리(평문 로테이션 진행 예정).
- 이미지 경로 예: `harbor.do4i.com/do4ai/do4i-api`, `harbor.do4i.com/do4ai/palcar-api`.

## 자주 쓰는 흐름
1. 배포가 `ImagePullBackOff`면, gitops overlay의 `images:` 태그/digest를 확인.
2. UI에서 해당 repository에 그 태그가 실제 있는지 확인.
3. 권한 문제면 클러스터의 `harbor-credentials`(InfisicalSecret) 동기화 상태 확인.

## 이미지 푸시(참고)
- 각 서비스 CI가 빌드 후 harbor로 푸시하고 gitops kustomization의 이미지 ref를 갱신한다(서비스 레포의 워크플로 참고).

## 함께 보기
- [ArgoCD 사용법](../ArgoCD 사용법/index.md) · [Infisical 시크릿 반영과 권한 변경 절차](../../07. 시크릿-권한 작업/Infisical 시크릿 반영과 권한 변경 절차/index.md)
