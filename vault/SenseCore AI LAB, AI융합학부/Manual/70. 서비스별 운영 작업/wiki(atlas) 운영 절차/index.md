---
title: "wiki(atlas) 운영 절차"
---
# wiki(atlas) 운영 절차

## 문서 목적

이 문서는 사내 위키 런타임 `wiki`(코드상 `atlas`, WikiJS)의 1차 운영·점검 절차를 정리한다. `wiki.do4ai.com`이 안 뜨거나, 문서가 갱신되지 않을 때 본다.

## 먼저 확인할 운영 단위

- namespace: `atlas` (prod 전용)
- 핵심 workload: `wikijs` 컨테이너(:3000, `/healthz`), `content-sync` 사이드카, `repo-bootstrap` init
- ingress host: `wiki.do4ai.com`
- 콘텐츠 정본: GitHub `do4ai/wiki` 레포(= vault)

## 절차

### 1. 페이지가 아예 안 뜬다
```bash
sudo kubectl get pods,svc,ing -n atlas
sudo kubectl describe ingress -n atlas
curl -I https://wiki.do4ai.com/healthz
```
- `wikijs` 파드 상태와 `/healthz`, ingress host 확인. `Recreate` 전략이라 **배포 중 짧은 다운은 정상**.

### 2. 문서가 갱신되지 않는다 (가장 흔함)
콘텐츠는 `content-sync` 사이드카가 60초마다 `do4ai/wiki` `main`을 pull → 동기화 스크립트가 WikiJS에 반영한다.
```bash
sudo kubectl logs deploy/atlas -c content-sync -n atlas --tail=100
```
- 레포 pull 실패(토큰/네트워크), 동기화 스크립트 오류를 확인. 정본은 레포이므로 대부분 재동기화로 해결.

### 3. 런타임 데이터 이상
- WikiJS는 SQLite(`/wiki/data/db.sqlite`) 단일 인스턴스다. 손상 시 **레포 재동기화로 콘텐츠 복구**가 우선(DB는 캐시/런타임 성격).

## 검증 기준
- `wiki.do4ai.com/healthz` 200, 최근 vault 변경이 페이지에 반영, `content-sync` 에러 없음.

## Escalation 또는 롤백 기준
- `wikijs` 파드가 계속 비정상 / 콘텐츠 동기화가 반복 실패 / 데이터 손상 의심 → 공유 후 재배포·복구.

## 참고
- 발행 파이프라인·동기화 스크립트 개요는 [wiki 서비스 가이드](../../../Guide/60. 서비스 운영/wiki 서비스 가이드/index.md).
- 로컬에서 동기화 미리보기: `python3 scripts/wiki_wikijs_sync.py sync --dry-run`.
