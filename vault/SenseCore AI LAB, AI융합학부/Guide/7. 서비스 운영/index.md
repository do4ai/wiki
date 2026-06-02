---
title: "7. 서비스 운영"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/guide/330e313f58b9802b9cedda8dcbc5d112__Guide/children/330e313f58b981389e9ee483d5ff6d88__7. 서비스 운영
notion_id: 330e313f58b981389e9ee483d5ff6d88
notion_url: https://www.notion.so/330e313f58b981389e9ee483d5ff6d88
parent_notion_id: 330e313f58b9802b9cedda8dcbc5d112
---
# 7. 서비스 운영

이 섹션은 연구실이 실제로 운영하는 서비스와 솔루션을 서비스 관점에서 설명한다.

각 서비스가 누구를 위한 것인지, 어떤 인프라 위에서 돌아가는지, 운영 중 어떤 신호를 먼저 봐야 하는지 같은 서비스별 큰 그림을 정리한다.

즉 이 섹션은 서비스의 목적, 구성, 주요 의존성, 1차 확인 포인트를 설명하는 곳이다.

서비스별 배포·장애 1차 대응 절차는 각 서비스 폴더의 `3. 운영 절차`에서 다룬다. 도구(ArgoCD·Grafana·Infisical 등) 사용법은 `Manual`(솔루션 사용법)에서 다룬다.

## 서비스 카탈로그

데이터센스가 운영하는 서비스를 한눈에 본다. 자세한 내용은 각 서비스 가이드로 들어간다.

| 서비스 | 한 줄 정의 | 주 사용자 | 회사·브랜드 | prod 도메인 | 배포 위치 | 상태 |
| --- | --- | --- | --- | --- | --- | --- |
| do4i | 에이전트 플랫폼(생성·대화·아바타) | 에이전트 제작자·사용자 | do4i(원본 본체) | agents.do4i.com | `apps/do4i` | 운영 중 |
| passv | AI 대화형 커머스(에이전트 판매·구매) | 셀러·바이어·조직 | 별도 회사·브랜드 | app.passv.co.kr | `apps/passv`(dev), prod 이전 중 | 이전 중 |
| palcar | 자동차 경매 딜러·셀러 워크플로 | 딜러·셀러 | do4i 계열 | palcar.do4ai.com | `apps/palcar` | 운영 중 |
| papersens | 논문 검사 솔루션(LLM/VLM) | 논문 검사 사용자 | do4i 계열 | papersens.do4ai.com | `apps/papersens` | 운영 중 |
| wiki | 사내 위키·지식베이스 런타임 | 전 구성원 | do4i 계열 | wiki.do4ai.com | `apps/atlas` | 운영 중 |

- **passv ↔ do4i**: 두 서비스는 같은 코드베이스에서 비슷한 서비스로 시작했지만, 지금은 서로 다른 회사가 다른 브랜드로 운영하는 별개 서비스다. 그래서 네임스페이스·이미지·도메인을 모두 분리한다.
- **wiki**: 코드상 이름은 `atlas`지만 서비스 명칭은 `wiki`로 통일한다(지금 보고 있는 이 위키의 런타임).
- **namanva**: 폐기 예정이라 이 카탈로그에서 제외한다.

## 서비스별 가이드 (서비스마다 한 폴더, 같은 구조)

각 서비스는 **한 폴더로 묶여** 있고, 그 안의 문서 구조가 모두 같다. 그래서 어떤 서비스를 보든 같은 자리에서 같은 정보를 찾는다.

> **`<서비스> 서비스 가이드/`**
> ├─ `index` — 개요 + 이 서비스 문서 맵(입구)
> ├─ `1. 아키텍처와 배포` — 컴포넌트·데이터 흐름·의존성 + 네임스페이스·이미지·도메인
> └─ `2. 모니터링·알람·SRE` — 대시보드·로그·트레이스 + 이 서비스 알림 규칙 + SLO + 1차 확인

운영 손절차(배포 이상 대응 등)는 각 서비스 입구에서 `Manual`로 링크한다. k3s·GitOps·SLO 개념 같은 공통 토대는 중복하지 않고 `50/70/90`에서 링크한다.

| 가이드 | 무엇을 보는 서비스인가 |
| --- | --- |
| [do4i 서비스 가이드](do4i 서비스 가이드/index.md) | 에이전트 플랫폼 |
| [passv 서비스 가이드](passv 서비스 가이드/index.md) | AI 대화형 커머스 |
| [palcar 서비스 가이드](palcar 서비스 가이드/index.md) | 자동차 경매 워크플로 |
| [papersens 서비스 가이드](papersens 서비스 가이드/index.md) | 논문 검사 솔루션 |
| [wiki 서비스 가이드](wiki 서비스 가이드/index.md) | 사내 위키 런타임 |

처음 보는 사람은 위 카탈로그로 전체 그림을 잡은 뒤, 맡은 서비스 폴더에 들어가 `index → 1 → 2` 순서로 읽는 것을 권장한다.

## Page Tree

- [do4i 서비스 가이드](do4i 서비스 가이드/index.md)
- [passv 서비스 가이드](passv 서비스 가이드/index.md)
- [palcar 서비스 가이드](palcar 서비스 가이드/index.md)
- [papersens 서비스 가이드](papersens 서비스 가이드/index.md)
- [wiki 서비스 가이드](wiki 서비스 가이드/index.md)
