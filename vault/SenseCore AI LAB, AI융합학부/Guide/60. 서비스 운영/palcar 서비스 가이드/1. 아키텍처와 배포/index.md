---
title: "1. 아키텍처와 배포"
---
# palcar — 아키텍처와 배포

## 아키텍처 구조

```
딜러/셀러 ─ palcar.do4ai.com /api ─┐
운영자   ─ admin.palcar...  /api ─┤
                                  ▼
                          ingress-nginx
                                  ▼
                          api (:8000) ── MySQL (StatefulSet)
```

- **API**: Deployment `api`(라벨 `app: palcar-api`), 포트 8000, 헬스 `/health`.
- **DB**: MySQL 8.0 StatefulSet.
- **이미지**: `harbor.do4i.com/do4ai/palcar-api`.

## 배포 구조

- **네임스페이스**: `palcar` (prod·dev).
- **GitOps 경로**: `gitops/k8s/apps/palcar` (base + overlays/prod·dev), ArgoCD Application `palcar`.
- **시크릿**: Infisical → `InfisicalSecret`(api/mysql/harbor).
- **prod 규모**: 신규 HPA(min 2 / max 6) + PDB minAvailable 1.
- **도메인**: prod `palcar.do4ai.com`, `admin.palcar.do4ai.com` / dev `palcar.dev.do4ai.com` 등.

> 배포/롤백 손절차는 [Manual/70 palcar 배포 이상 대응 절차](../../../../Manual/70. 서비스별 운영 작업/palcar 배포 이상 대응 절차/index.md).
