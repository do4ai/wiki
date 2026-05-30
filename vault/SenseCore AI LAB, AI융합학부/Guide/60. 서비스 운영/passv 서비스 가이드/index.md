---
title: "passv 서비스 가이드"
---
# passv 서비스 가이드

이 문서는 AI 대화형 커머스 플랫폼 `passv`(PassView)를 서비스 관점에서 설명한다. 모든 서비스 가이드는 같은 7개 절 순서를 따른다.

## 1. 서비스 개요

- **무엇인가**: 셀러가 AI 에이전트를 만들어 판매하고, 바이어가 구매·실행(텍스트·음성·아바타·모바일)하는 대화형 커머스 플랫폼.
- **누구를 위한 것인가**: 셀러, 바이어, 조직(organization), 운영 admin. 모바일은 "IN"/KON 브랜드.
- **회사·브랜드**: `do4i`와 같은 코드베이스에서 시작했지만 **지금은 다른 회사가 다른 브랜드(PassView/KON)로 운영**하는 독립 서비스다. 그래서 네임스페이스·이미지·도메인·시크릿을 모두 분리한다.

## 2. 아키텍처 구조

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
- **프론트엔드 4종**: landing/platform/admin/mobile(React+Vite). **S3+CloudFront 정적 호스팅** — K8s 배포 대상이 아니다.
- **DB**: MySQL 8.0, DB명 `passv`.
- **외부 의존성**: OpenAI, LiveKit/Simli(아바타), Minimax(TTS), Toss(결제), Google/Kakao OAuth, KMC/Work24(본인확인).

## 3. 배포 구조

> **이전(migration) 중인 서비스다.** 자세한 경계는 `gitops/k8s/apps/passv/README.md` 참고.

- **현재 prod 정본**: EC2 docker-compose(API) + S3/CloudFront(프론트). 이미지 ECR `passv-api`.
- **목표(중앙 gitops)**: `gitops/k8s/apps/passv` (base + overlays/prod·dev), ArgoCD Application `passv`, 네임스페이스 `passv`.
  - **dev**: 본 매니페스트로 K8s 배포(자동 동기화 on).
  - **prod**: K8s 컷오버는 MySQL 데이터 이관 + DNS 전환 + 점검창이 필요한 **게이팅 작업**(자동 동기화 off). 절차는 [Manual/30 passv gitops 이전·컷오버 점검](../../../Manual/30. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md).
- **시크릿**: Infisical `/apps/passv-api`, `/apps/passv-mysql`로 이관 예정(`TODO 확정 필요`).
- **도메인**: prod `app/api/admin.passv.co.kr`, `kon.ai.kr` / dev `pv.dev.do4ai.com`, `app.dev.passv.co.kr`.

## 4. 모니터링·관측

- 플랫폼 공통 스택(Prometheus/Grafana, ElastAlert/ES/Kibana, OTel/Tempo)을 그대로 사용.
- gitops 편입 후 `passv` 네임스페이스가 알림/대시보드 대상에 포함된다(아래 5절 알림 규칙에 `passv` 이미 포함).
- 합성 모니터링: blackbox 프로브가 `app.passv.co.kr`, `api.passv.co.kr/api/health`를 점검(`TODO` 대상 확정).

## 5. 장애 알람

신규 런타임/용량/SLO 규칙은 이미 `passv` 네임스페이스를 대상에 포함한다(CrashLoop, OOM, CPU throttling, PVC, MySQLNotReady, 가용성 번레이트). 컷오버 이후 ingress 기반 알림(5xx/지연)도 자동 적용된다.

## 6. SRE·SLO

- **가용성/지연 SLO**: `TODO(확정 필요)` 제안값 99.9% / p95 < 1500ms.
- **확장**: API HPA(min 2 / max 6) 정의 완료(prod overlay). 아바타/음성 워커 분리 배포는 컷오버 단계 결정(`TODO`).
- **데이터 보호**: prod MySQL이 EC2에서 K8s StatefulSet로 이관되므로, 컷오버 런북에 백업·복구 단계가 핵심.

## 7. 1차 확인 포인트

- **현재(EC2)**: 배포/롤백은 passv 레포 CI(`deploy.yml`, `rollback.yml`)와 EC2 호스트 점검.
- **gitops(dev/컷오버 후)**: ArgoCD `passv` Application → `passv` 네임스페이스 파드 → Grafana/Kibana.
- 서비스별 대응 절차는 [Manual/70 passv 배포 이상 대응 절차](../../../Manual/70. 서비스별 운영 작업/passv 배포 이상 대응 절차/index.md).
