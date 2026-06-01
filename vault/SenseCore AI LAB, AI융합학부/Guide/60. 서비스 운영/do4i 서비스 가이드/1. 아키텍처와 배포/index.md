---
title: "1. 아키텍처와 배포"
---
# do4i — 아키텍처와 배포

## 아키텍처 구조

```
사용자 ─ agents.do4i.com /api ─┐
운영자 ─ admin.do4i.com  /api ─┤
                               ▼
                      ingress-nginx
                               ▼
                     api (FastAPI, :8000)  ── MySQL (StatefulSet)
                        │                  └─ 런타임 스토리지 PVC (Chroma/업로드)
                        └─ avatar-livekit-worker (LiveKit + Simli, HPA)
```

- **API**: Python 3.12 FastAPI 모놀리스. 컨테이너 포트 8000, 헬스 `/api/health`.
- **DB**: MySQL 8.0 StatefulSet(`mysql`), DB명 `do4i`.
- **아바타 워커**: `avatar-livekit-worker` — LiveKit 실시간 영상 + Simli 렌더링. 메모리 기준 HPA(10~100).
- **상태 저장**: `api-storage` PVC(`/app/runtime/storage`) — Chroma 벡터 DB, 업로드 파일.
- **외부 의존성**: OpenAI(LLM), LiveKit/Simli(아바타), Google OAuth.

## 배포 구조

- **네임스페이스**: `do4i` (prod·dev 클러스터 공통 이름).
- **GitOps 경로**: `gitops/k8s/apps/do4i` (base + overlays/prod·dev), ArgoCD Application `do4i`.
- **이미지**: `harbor.do4i.com/do4ai/do4i-api` (overlay에서 태그+digest 핀).
- **시크릿**: Infisical `do4ai` 프로젝트 `/apps/api`, `/apps/mysql` → `InfisicalSecret`로 주입.
- **prod 규모**: API replicas 2(HA, pod anti-affinity) + HPA(min 2 / max 6, CPU 70%·Mem 80%), PDB minAvailable 1.
- **부트스트랩**: `api-bootstrap` Job이 alembic 마이그레이션 수행(ArgoCD Sync hook).
- **도메인**: `agents.do4i.com`, `admin.do4i.com` (CloudFront `/api*` → ingress).

> 배포 이상 대응은 [3. 운영 절차](../3. 운영 절차/index.md). 도구는 [Manual/4 ArgoCD 사용법](../../../../Manual/4. 서버와 배포 작업/ArgoCD 사용법/index.md). 플랫폼 공통 배포 모델은 [GitOps 운영 모델 가이드](../../../50. 인프라와 플랫폼/GitOps 운영 모델 가이드/index.md).
