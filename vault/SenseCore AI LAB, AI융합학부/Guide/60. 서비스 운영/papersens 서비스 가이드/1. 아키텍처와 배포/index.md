---
title: "1. 아키텍처와 배포"
---
# papersens — 아키텍처와 배포

## 아키텍처 구조

```
사용자 ─ papersens.do4ai.com, *.ps.do4ai.com ─ ingress-nginx ─ papersens (:8082)
                                                                  │
                                              OpenRouter(gpt-4o-mini) / Ollama (LLM·VLM)
```

- **앱**: Deployment `papersens`(라벨 `app: papersens`), 포트 8082, 헬스 `/health`. 리소스 req 1Gi / limit 4Gi(무거움).
- **LLM 백엔드**: OpenRouter(`openai/gpt-4o-mini`) 기본, Ollama 폴백(`PAPERSENS_OPENROUTER_FALLBACK_TO_OLLAMA`).
- **이미지**: ECR `741323757384.dkr.ecr.ap-northeast-2.amazonaws.com/do4ai/papersens`.

## 배포 구조

- **네임스페이스**: `papersens` (prod·dev).
- **GitOps 경로**: `gitops/k8s/apps/papersens` (base + overlays/prod·dev), ArgoCD Application `papersens`.
- **시크릿**: `InfisicalSecret`(api) + ECR registry secret.
- **prod 규모**: 신규 HPA(min 2 / max 4) + PDB minAvailable 1. `TODO(확정 필요)`: 무거운 워크로드라 min 2는 노드 용량 의존 — 단일/저용량 노드면 min 1.
- **도메인**: `papersens.do4ai.com`, 와일드카드 `*.ps.do4ai.com`(테넌트).

> 배포/롤백 손절차는 [Manual/70 papersens 배포 이상 대응 절차](../../../../Manual/70. 서비스별 운영 작업/papersens 배포 이상 대응 절차/index.md).
