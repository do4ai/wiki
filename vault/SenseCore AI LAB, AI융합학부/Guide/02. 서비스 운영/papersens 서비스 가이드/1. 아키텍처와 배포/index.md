---
title: "1. 아키텍처와 배포"
---
# papersens — 아키텍처와 배포

## 아키텍처 구조

```
사용자 ─ papersens.do4ai.com, *.ps.do4ai.com ─ ingress-nginx
        ▼
   papersens (단일 컨테이너, FastAPI :8082)
      ├ 프론트(React 빌드물)를 / 및 /assets 에서 서빙
      └ LLM/VLM 호출 → OpenRouter(gpt-4o-mini) / Ollama 폴백
   (영속 DB 없음 — 인메모리)
```

### 프론트엔드
- `web-app` — React 18 + Vite + TypeScript. **별도 배포가 아니라 백엔드 이미지에 빌드 산출물(dist)이 포함**되어, FastAPI(`web_ui.py`)가 `/`(HTML)·`/assets`에서 직접 서빙한다. 즉 **UI + API가 한 컨테이너**.

### 백엔드
- **Python 3.12 + FastAPI** 단일 파일(`web_ui.py`), 포트 8082.
- 헬스 `/health`(+`/ping`). 클라이언트의 `/api/*` 호출은 미들웨어가 루트 경로로 리라이트.
- 주요 엔드포인트: `/upload`(논문 업로드) · `/analyze`·`/analyze-stream`(분석, SSE) · `/paper/{alias}/...`(도표/데이터셋/초록 등) · `/models`.

### 데이터 (중요)
- **영속 DB가 없다.** 업로드·분석 결과를 **인메모리 딕셔너리(`papers = {}`)** 에만 보관한다 → **파드 재시작 시 전부 소실**. 벡터/임베딩 DB도 없음.
- 검수·운영 시 이 점을 전제로 본다(영속성·백업 대상 아님, 재기동 = 데이터 초기화).

### LLM/VLM
- 기본 **OpenRouter**(텍스트·비전 모두 `openai/gpt-4o-mini`).
- 폴백 **Ollama**(VLM `qwen3-vl:30b-a3b-instruct`), `PAPERSENS_OPENROUTER_FALLBACK_TO_OLLAMA=true`.
- 선택적으로 **Cloudflare AI Gateway** 경유 가능.

### 멀티테넌시
- `*.ps.do4ai.com` 와일드카드는 **ingress(인프라)만 준비**된 상태이고, **앱은 단일 테넌트**다(공유 `papers` dict, 테넌트별 격리 로직 없음). "테넌트별 분리"로 오해하지 말 것.

## 배포 구조

- **네임스페이스**: `papersens` (prod·dev).
- **GitOps 경로**: `gitops/k8s/apps/papersens` (base + overlays/prod·dev), ArgoCD Application `papersens`.
- **이미지**: ECR `741323757384.dkr.ecr.ap-northeast-2.amazonaws.com/do4ai/papersens` (UI+API 단일 이미지).
- **시크릿**: `InfisicalSecret`(api) + ECR registry secret.
- **prod 규모**: 신규 HPA(min 2 / max 4) + PDB minAvailable 1. `TODO(확정 필요)`: 무거운 워크로드라 min 2는 노드 용량 의존 — 단일/저용량 노드면 min 1. (인메모리 특성상 replica 간 데이터 공유 안 됨도 유의.)
- **도메인**: `papersens.do4ai.com`, 와일드카드 `*.ps.do4ai.com`.

> 배포 이상 대응은 [3. 운영 절차](../3. 운영 절차/index.md). 도구는 [Manual/04 ArgoCD 사용법](../../../../Manual/04. 서버와 배포 작업/ArgoCD 사용법/index.md).

---

> **온보딩 트랙 — 2부 서비스 운영**
> 이전: [papersens 서비스 가이드](../index.md) · 다음: [papersens — 모니터링·알람·SRE](../2. 모니터링·알람·SRE/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../../../시작하기/index.md)
