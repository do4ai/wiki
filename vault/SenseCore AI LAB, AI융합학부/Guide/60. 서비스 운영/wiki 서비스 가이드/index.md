---
title: "wiki 서비스 가이드"
---
# wiki 서비스 가이드

사내 위키 런타임 `wiki`(코드상 `atlas`, WikiJS)의 모든 문서를 한곳에 모은 입구다. 지금 보고 있는 이 위키가 바로 이 서비스다.

## 한 줄 개요

- **무엇인가**: WikiJS 런타임. GitHub `do4ai/wiki` 레포(=이 vault)를 주기적으로 동기화해 서빙.
- **누구를 위한 것인가**: 데이터센스 전 구성원(`wiki.do4ai.com`).
- **명칭**: 서비스명은 `wiki`로 통일. gitops 디렉터리·ArgoCD Application은 아직 `atlas`(`apps/atlas`). 코드상 `atlas` = 서비스 `wiki`.

## 이 서비스 문서 맵

| 문서 | 내용 |
| --- | --- |
| [1. 아키텍처와 배포](1. 아키텍처와 배포/index.md) | WikiJS·SQLite·콘텐츠 동기화, 네임스페이스·전략·도메인 |
| [2. 모니터링·알람·SRE](2. 모니터링·알람·SRE/index.md) | 프로브·합성 프로브, 알림, 데이터 복구, SRE |
| [3. 운영 절차](3. 운영 절차/index.md) | 페이지 미표시·콘텐츠 미갱신 대응, 복구 |

## 공통·도구 문서

- 서비스 공통: [서비스 공통 1차 대응 절차](../서비스 공통 1차 대응 절차/index.md)
- 도구 사용법: `Manual`(솔루션 사용법)
- 발행 미리보기: `python3 scripts/wiki_wikijs_sync.py sync --dry-run`

## Page Tree

- [1. 아키텍처와 배포](1. 아키텍처와 배포/index.md)
- [2. 모니터링·알람·SRE](2. 모니터링·알람·SRE/index.md)
- [3. 운영 절차](3. 운영 절차/index.md)
