---
title: "3. 운영 절차"
---
# wiki — 운영 절차

WikiJS 런타임(`wiki.do4ai.com`, 코드상 `atlas`)이 안 뜨거나 문서가 갱신되지 않을 때의 절차다.

## 먼저 확인할 운영 단위
- namespace `atlas`(prod 전용) / workload `wikijs`(:3000, `/healthz`), `content-sync` 사이드카, `repo-bootstrap` init / ingress host `wiki.do4ai.com` / 콘텐츠 정본 GitHub `do4ai/wiki` 레포(= vault).

## 절차

### 1. 페이지가 아예 안 뜬다
```bash
sudo kubectl get pods,svc,ing -n atlas
curl -I https://wiki.do4ai.com/healthz
```
- `wikijs` 파드 상태·`/healthz`·ingress host 확인. `Recreate` 전략이라 배포 중 짧은 다운은 정상.

### 2. 문서가 갱신되지 않는다 (가장 흔함)
```bash
sudo kubectl logs deploy/atlas -c content-sync -n atlas --tail=100
```
- `content-sync`가 60초마다 `do4ai/wiki` `main`을 pull → WikiJS 반영. 레포 pull 실패(토큰/네트워크)·동기화 스크립트 오류 확인. 정본은 레포이므로 대부분 재동기화로 해결.

### 3. 런타임 데이터 이상
- SQLite(`/wiki/data/db.sqlite`) 단일 인스턴스. 손상 시 레포 재동기화로 콘텐츠 복구 우선(DB는 캐시/런타임).

## 검증 기준
- `wiki.do4ai.com/healthz` 200, 최근 vault 변경이 페이지에 반영, `content-sync` 에러 없음.

## 참고
- 로컬 발행 미리보기: `python3 scripts/wiki_wikijs_sync.py sync --dry-run`.
- 발행 파이프라인 개요: [wiki 서비스 가이드 — 아키텍처와 배포](../1. 아키텍처와 배포/index.md).
