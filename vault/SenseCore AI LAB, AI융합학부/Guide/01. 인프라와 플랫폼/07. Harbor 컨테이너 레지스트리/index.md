---
title: "07. Harbor 컨테이너 레지스트리"
---
# 07. Harbor 컨테이너 레지스트리

서비스 컨테이너 이미지를 보관·배포하는 사설 레지스트리다. 배포 이미지의 출처이자 `ImagePullBackOff` 진단의 핵심.

## 실제 구성
- **Helm chart 1.18.3**, **prod 클러스터에만** 배포.
- **접속**: `harbor.do4i.com` (⚠️ `.do4i.com` 도메인, 현재 HTTP/ingress 노출).
- **프로젝트**: `do4ai`, 이미지 경로 예 `harbor.do4i.com/do4ai/do4i-api`, `.../palcar-api`, `.../passv-api`.
- **스토리지**: `local-path`(registry 20Gi, db 5Gi, redis 2Gi, jobLog 2Gi, trivy 5Gi).
- **자격증명**: Infisical `/platform/harbor-credentials` → `harbor-credentials`(InfisicalSecret). 각 앱은 `harbor-credentials`(또는 `harbor-registry`) imagePullSecret으로 pull.
- 참고: papersens·passv(prod)는 일부 **AWS ECR**도 사용([papersens 서비스 가이드](../../02. 서비스 운영/papersens 서비스 가이드/index.md)·[passv 서비스 가이드](../../02. 서비스 운영/passv 서비스 가이드/index.md) 참고).

## 무엇을 위해 보나
- 배포가 `ImagePullBackOff`면: ① gitops overlay `images:` 태그/digest 확인 → ② Harbor UI에 그 태그가 실제 있는지 → ③ pull 권한(`harbor-credentials` 동기화) 확인.

## 연결
- 푸시: 각 서비스 CI가 빌드 후 harbor로 push + gitops 이미지 ref 갱신.
- 사용 절차는 [Manual 04. Harbor 사용법](../../../Manual/04. 서버와 배포 작업/Harbor 사용법/index.md).

---

> **온보딩 트랙 1부. 인프라와 플랫폼**
> 이전: [ingress-nginx](../06. ingress-nginx/index.md) · 다음: [Harbor 사용법 (Manual)](../../../Manual/04. 서버와 배포 작업/Harbor 사용법/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../시작하기/index.md)
