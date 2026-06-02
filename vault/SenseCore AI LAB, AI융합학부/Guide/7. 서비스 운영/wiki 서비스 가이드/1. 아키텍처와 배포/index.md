---
title: "1. 아키텍처와 배포"
---
# wiki — 아키텍처와 배포

## 아키텍처 구조

```
GitHub do4ai/wiki (vault 소스)
        │  (content-sync 사이드카, 60s 주기 git pull)
        ▼
   wikijs (requarks/wiki:2, :3000, SQLite) ── ingress ── wiki.do4ai.com
```

- **런타임**: `requarks/wiki:2`(WikiJS), 포트 3000, 헬스 `/healthz`. DB는 SQLite(`/wiki/data/db.sqlite`), `HA_ACTIVE=false`.
- **콘텐츠 동기화**: `repo-bootstrap` init이 레포 클론, `content-sync` 사이드카가 60초마다 `do4ai/wiki` `main` pull.
- **발행 파이프라인**: vault 마크다운 → `scripts/wiki_wikijs_sync.py`가 WikiJS GraphQL로 페이지 생성/갱신.

## 배포 구조

- **네임스페이스**: `atlas` (prod 전용 — dev 없음).
- **GitOps 경로**: `gitops/k8s/apps/atlas`, ArgoCD Application `atlas`(prod 트리).
- **전략**: replicas 1, `Recreate`(롤링 아님). SQLite 단일 파일이라 HA 불가 — 단일 인스턴스 운영.
- **도메인**: `wiki.do4ai.com`, 내부 `origin.wiki.do4ai.com`.

> 운영·복구 손절차는 [3. 운영 절차](../3. 운영 절차/index.md).
