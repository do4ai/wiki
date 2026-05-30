---
title: "wiki 서비스 가이드"
---
# wiki 서비스 가이드

이 문서는 사내 위키 런타임 `wiki`(코드상 이름 `atlas`)를 서비스 관점에서 설명한다. 지금 보고 있는 이 위키가 바로 이 서비스다. 모든 서비스 가이드는 같은 7개 절 순서를 따른다.

## 1. 서비스 개요

- **무엇인가**: 사내 위키·지식베이스 런타임. WikiJS로 페이지를 서빙하고, GitHub의 `do4ai/wiki` 레포(=이 vault)를 주기적으로 동기화한다.
- **누구를 위한 것인가**: 데이터센스 전 구성원(`wiki.do4ai.com`).
- **명칭**: 서비스명은 `wiki`로 통일한다. gitops 디렉터리·ArgoCD Application 이름은 아직 `atlas`다(`apps/atlas`). 코드상 `atlas` = 서비스 `wiki`.

## 2. 아키텍처 구조

```
GitHub do4ai/wiki (vault 소스)
        │  (content-sync 사이드카, 60s 주기 git pull)
        ▼
   wikijs (requarks/wiki:2, :3000, SQLite) ── ingress ── wiki.do4ai.com
```

- **런타임**: `requarks/wiki:2`(WikiJS), 포트 3000, 헬스 `/healthz`. DB는 SQLite(`/wiki/data/db.sqlite`), `HA_ACTIVE=false`.
- **콘텐츠 동기화**: `repo-bootstrap` init 컨테이너가 레포 클론, `content-sync` 사이드카가 60초마다 `do4ai/wiki` `main`을 pull.
- **발행 파이프라인**: vault의 마크다운 → 동기화 스크립트(`scripts/wiki_wikijs_sync.py`)가 WikiJS GraphQL로 페이지 생성/갱신.

## 3. 배포 구조

- **네임스페이스**: `atlas` (prod 전용 — dev 없음).
- **GitOps 경로**: `gitops/k8s/apps/atlas`, ArgoCD Application `atlas`(prod 트리).
- **전략**: replicas 1, `Recreate`(롤링 아님). SQLite 단일 파일이라 HA 불가 — 단일 인스턴스로 운영.
- **도메인**: `wiki.do4ai.com`, 내부 `origin.wiki.do4ai.com`.

## 4. 모니터링·관측

- 프로브: liveness/readiness + **startup 프로브(신규)** `/healthz:3000`.
- 합성 모니터링: blackbox 프로브가 `wiki.do4ai.com/healthz` 점검.
- 로그/리소스는 플랫폼 공통 스택에서 `atlas` 네임스페이스로 확인.

## 5. 장애 알람

- 런타임 공통 규칙(CrashLoop/OOM/throttle)과 합성 프로브(PlatformEndpointDown: `wiki.do4ai.com`) 대상.
- `Recreate` 전략이라 배포 중 짧은 다운이 정상임을 유의(알림 노이즈 판단 기준).

## 6. SRE·SLO

- **가용성**: 단일 인스턴스 + SQLite라 SLO는 보수적으로 본다(`TODO 확정 필요`). 내부 문서 도구 특성상 사용자 영향도는 외부 서비스보다 낮음.
- **데이터**: 콘텐츠 정본은 GitHub `do4ai/wiki` 레포다. WikiJS SQLite는 캐시/런타임이므로, 복구는 레포 재동기화로 대부분 해결.
- **개선 여지**: SQLite→외부 DB 전환 시 HA 가능(향후 검토 `TODO`).

## 7. 1차 확인 포인트

1. `wiki.do4ai.com/healthz` 응답 확인(또는 blackbox 알림).
2. ArgoCD `atlas` Sync/Health, `atlas` 네임스페이스 파드(wikijs/content-sync).
3. 콘텐츠가 안 보이면 `content-sync` 로그(레포 pull 실패) 확인.
4. 문서 발행/동기화 절차는 [Manual/70 wiki(atlas) 운영 절차](../../../Manual/70. 서비스별 운영 작업/wiki(atlas) 운영 절차/index.md).
