---
title: "1. 아키텍처와 배포"
---
# passv 아키텍처와 배포

## 아키텍처 구조

```
landing/platform/admin (React, S3+CloudFront)
            │  /api*  (CloudFront → origin)
            ▼
       ingress-nginx
            ▼
     api (FastAPI, :8000) ── MySQL (StatefulSet)
        │                 └─ 런타임 스토리지(Chroma/업로드)
        └─ (아바타/음성: LiveKit+Simli, Minimax TTS)
```

- **API**: Python 3.12 FastAPI 모놀리스(DDD 컨텍스트: auth/user/organizations/products/sellers/payments/chatbot/avatar/voice 등). 포트 8000, 헬스 `/api/health`.
- **프론트 4종**: landing/platform/admin/mobile(React+Vite). **S3+CloudFront 정적 호스팅**: K8s 대상이 아니다.
- **DB**: MySQL 8.0, DB명 `passv`.
- **외부 의존성**: OpenAI, LiveKit/Simli(아바타), Minimax(TTS), Toss(결제), Google/Kakao OAuth, KMC/Work24(본인확인).

## 배포 구조 (이전 중)

> 자세한 경계·절차는 `gitops/k8s/apps/passv/README.md`와 [Manual/04 컷오버 점검](../../../../Manual/04. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md).

- **현재 prod 정본**: EC2 docker-compose(API) + S3/CloudFront(프론트). 이미지 ECR `passv-api`.
- **목표(중앙 gitops)**: `gitops/k8s/apps/passv` (base + overlays/prod·dev), ArgoCD Application `passv`, 네임스페이스 `passv`.
  - **dev**: 본 매니페스트로 K8s 배포(자동 동기화 on).
  - **prod**: K8s 컷오버는 MySQL 데이터 이관 + DNS 전환 + 점검창 필요한 **게이팅 작업**(자동 동기화 off).
- **시크릿**: Infisical `/apps/passv-api`, `/apps/passv-mysql`로 이관 예정(TODO(확정 필요)).
- **도메인**: prod `app/api/admin.passv.co.kr`, `kon.ai.kr` / dev `dev.passv.co.kr`, `app.dev.passv.co.kr`.

---

> **온보딩 트랙 2부. 서비스 운영**
> 이전: [passv 서비스 가이드](../index.md) · 다음: [passv 모니터링·알람·SRE](../2. 모니터링·알람·SRE/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../../시작하기/index.md)
