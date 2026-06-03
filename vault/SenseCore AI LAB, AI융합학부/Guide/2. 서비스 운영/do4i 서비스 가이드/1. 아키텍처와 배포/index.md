---
title: "1. 아키텍처와 배포"
---
# do4i — 아키텍처와 배포

## 아키텍처 구조

```
[프론트엔드] React + Vite, AWS S3 + CloudFront 정적 호스팅
  ├ agents (사용자)  agents.do4i.com
  ├ admin  (운영)    admin.do4i.com
  └ landing(소개)    do4i.com
        │  /api*  (CloudFront → ingress)
        ▼
   ingress-nginx
        ▼
   api (FastAPI, :8000) ── MySQL (StatefulSet, DB명 do4i)
      │                 └─ 런타임 스토리지 PVC (Chroma 벡터DB / 업로드)
      └─ avatar-livekit-worker (LiveKit + Simli, HPA)
```

### 프론트엔드 (3종, K8s 아님 — S3/CloudFront)
- `client/agents` — 사용자 앱(React 19 + Vite, LiveKit/Simli 클라이언트). `agents.do4i.com`
- `client/admin` — 운영 대시보드(React 19 + Vite + Tailwind). `admin.do4i.com`
- `client/landing` — 소개 페이지(React 18 + Vite). `do4i.com`
- 빌드 산출물(dist)을 **AWS S3 + CloudFront**로 배포. `/api*`만 CloudFront가 ingress(백엔드)로 포워딩.

### 백엔드
- **Python 3.12 + FastAPI**(Uvicorn) 모놀리스, DDD 컨텍스트(agents/auth/avatar/chatbot/payments/user/organizations/sellers/voice 등).
- 포트 8000, 헬스 `/api/health`, 모든 라우트 `/api/*` 프리픽스. HTTP + WebSocket(아바타/채팅/STT/음성).
- ORM **SQLModel(SQLAlchemy 2.0)** + 마이그레이션 **Alembic**.
- **아바타 워커**: `avatar-livekit-worker`(API와 동일 이미지, `avatar_agent` 실행) — LiveKit 실시간 영상 + Simli 렌더링, 메모리 기준 HPA(10~100).

### 데이터
- **MySQL 8.0** StatefulSet(DB명 `do4i`). 개발 폴백은 SQLite.
- **Chroma 벡터DB**(RAG) — `api-storage` PVC(`/app/runtime/storage`)에 로컬 저장. 업로드 파일 동거.

### 외부 의존성
- OpenAI(LLM, realtime/TTS), LiveKit + Simli(아바타), Google OAuth, **Twilio(전화 인증)**, **Toss(결제)**, **MinIO(S3 호환 파일 저장)**.

## 배포 구조

- **네임스페이스**: `do4i` (prod·dev 클러스터 공통 이름). *프론트는 K8s가 아니라 S3/CloudFront.*
- **GitOps 경로**: `gitops/k8s/apps/do4i` (base + overlays/prod·dev), ArgoCD Application `do4i`.
- **이미지**: `harbor.do4i.com/do4ai/do4i-api` (API·아바타 워커 공용, overlay에서 태그+digest 핀).
- **시크릿**: Infisical `do4ai` 프로젝트 `/apps/api`, `/apps/mysql` → `InfisicalSecret`로 주입.
- **prod 규모**: API replicas 2(HA, pod anti-affinity) + HPA(min 2 / max 6, CPU 70%·Mem 80%), PDB minAvailable 1.
- **부트스트랩**: `api-bootstrap` Job이 alembic 마이그레이션 수행(ArgoCD Sync hook).
- **도메인**: `agents.do4i.com`, `admin.do4i.com`, `do4i.com` (프론트는 CloudFront→S3, `/api*`는 CloudFront→ingress).

> 배포 이상 대응은 [3. 운영 절차](../3. 운영 절차/index.md). 도구는 [Manual/4 ArgoCD 사용법](../../../../Manual/4. 서버와 배포 작업/ArgoCD 사용법/index.md). 플랫폼 공통 배포 모델은 [GitOps 운영 모델 가이드](../../../1. 인프라와 플랫폼/GitOps 운영 모델 가이드/index.md).
