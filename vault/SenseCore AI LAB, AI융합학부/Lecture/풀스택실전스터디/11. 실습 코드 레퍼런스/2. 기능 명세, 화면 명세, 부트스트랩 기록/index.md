---
title: "2. 기능 명세, 화면 명세, 부트스트랩 기록"
source_kind: page
source_path: manual-local/lecture/fullstack-study/11-practice-code/02-specs
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 2. 기능 명세, 화면 명세, 부트스트랩 기록
이 페이지는 저장소가 무엇을 만들기로 했는지를 적어 둔 명세 문서를 담습니다. 01장부터 03장까지의 기획과 화면 설계가 저장소 안에서 어떤 형태로 고정됐는지 보여줍니다.

기능 명세는 MVP 범위를 확정하고, 화면 명세는 storefront와 admin의 화면 목록과 라우트를 확정합니다. 부트스트랩 계획과 검증 기록은 이 저장소를 처음 세울 때 무엇을 하기로 했고 무엇을 확인했는지를 남깁니다. 기획 문서가 구현으로 넘어가는 접점이 어디인지 확인할 때 이 네 문서를 봅니다.

# 파일

## `sdd/01_planning/01_feature/ecommerce_lecture_feature_spec.md`

```markdown
# Ecommerce Lecture Feature Spec

## Scope

- 이 교재는 이커머스 서비스를 실전형 풀스택 프로젝트로 완성하는 것을 목표로 한다.
- `frontend`, `backend`, `infra`를 분리해서 셋업하고, 마지막에 하나의 제품으로 통합한다.
- 구매자 storefront, 운영자 admin, FastAPI + SQLAlchemy 서버, 인증, 장바구니, 주문, mock 결제, CI를 포함한다.

## Primary Actors

- Buyer
- Admin operator
- Instructor

## Core Use Cases

1. 사용자는 회원가입 후 로그인한다.
2. 사용자는 상품 목록을 조회하고 장바구니를 관리한다.
3. 사용자는 장바구니 기준으로 주문을 생성한다.
4. 사용자는 mock 결제를 완료해 주문 상태를 다음 단계로 전환한다.
5. 관리자는 인증 후 상품, 주문, 결제 시도, 운영 지표를 조회한다.
6. 강사는 프론트, 백엔드, 인프라, 문서, 검증의 경계를 하나의 교재 흐름으로 설명한다.

## Domain Rules

- 상품은 persistence에 저장되며 초기 seed가 제공된다.
- 장바구니는 사용자 단위로 분리된다.
- 주문 생성 시 cart snapshot을 기준으로 합계와 배송비를 계산한다.
- 결제는 `payment_attempt`로 먼저 기록되고 mock confirmation 이후 성공 또는 실패 상태가 된다.
- admin endpoint는 관리자 권한이 필요하다.
- local baseline은 SQLite를 사용하되 ORM 구조는 MySQL 전환을 염두에 둔다.

## Out Of Scope

- 외부 PG사 연동
- 배송사 연동
- refresh token, email verification, password reset
- 실서비스 수준 재고 경쟁 조건 처리

## Acceptance Criteria

- buyer register/login API가 동작한다.
- authenticated cart/order/payment flow가 동작한다.
- admin login 후 protected dashboard가 동작한다.
- backend tests, lint, frontend builds, CI가 동작한다.
- 계획/검증 문서가 현재 구현과 일치한다.
```

## `sdd/01_planning/02_screen/ecommerce_lecture_screen_spec.md`

```markdown
# Ecommerce Lecture Screen Spec

## Storefront

### Hero

- 브랜드 메시지와 강의 목표를 한 화면에서 설명한다.
- CTA는 상품 섹션과 장바구니 섹션으로 이동시킨다.

### Product Grid

- 상품 카드에는 이름, 카테고리, 가격, 태그, 재고 상태를 표시한다.
- 각 카드는 장바구니 추가 액션을 가진다.

### Cart Panel

- 장바구니 라인 아이템, 수량 조절, 합계, 배송비 정책을 표시한다.

### Operations Strip

- 주문 요약, 배송 단계, 최근 주문 흐름을 보조 정보로 표시한다.

## Admin

### Dashboard Header

- 운영 관점의 핵심 메시지와 현재 샘플 데이터 상태를 보여준다.

### Metrics

- 매출, 주문 수, 재고 부족 상품 수, 평균 객단가를 카드로 표시한다.

### Product Table

- 운영자가 상품 상태를 빠르게 훑을 수 있어야 한다.

### Order Table

- 최근 주문의 상태, 고객, 금액, 채널을 표시한다.

## UI Direction

- storefront는 따뜻하고 편집숍 같은 무드
- admin은 차갑고 정제된 운영 대시보드 무드
- 모바일에서도 한 컬럼으로 읽히도록 구성
```

## `sdd/02_plan/01_kickoff/lecture_repo_bootstrap_plan.md`

```markdown
# Lecture Repo Plan

## Scope

- 이커머스 교재용 monorepo 정본 구성
- backend, storefront, admin, infra baseline, CI, SDD 문서 정리
- 따라 하기만 해도 하나의 서비스가 완성되는 학습 구조 제공

## Assumptions

- local baseline은 SQLite와 docker compose로 충분하다.
- 백엔드는 DDD 관점으로 컨텍스트를 나누되 구현은 과도하게 무겁지 않게 유지한다.
- 프론트는 storefront와 admin을 분리해 역할 차이를 드러낸다.

## Acceptance Criteria

- [x] backend가 persistence와 auth를 가진다.
- [x] storefront가 로그인, cart, checkout, payment mock까지 연결된다.
- [x] admin이 인증 후 운영 데이터에 접근한다.
- [x] CI workflow가 backend tests와 frontend builds를 수행한다.
- [x] 검증 결과가 `sdd/03_verify`에 기록된다.

## Execution Checklist

- [x] feature spec을 정리한다.
- [x] backend schema, seed, auth, order/payment API를 구현한다.
- [x] storefront를 authenticated flow 기준으로 확장한다.
- [x] admin과 CI workflow를 구현한다.
- [x] 통합 테스트와 build를 실행한다.
- [x] verify 문서를 갱신한다.

## Current Notes

- `lecture`는 현재 이 교재의 단일 정본이다.
- 초기 인메모리 초안은 persistence/auth/order/admin flow를 가진 현재 구조로 승격됐다.
- backend 응답 shape와 storefront/admin 기대 shape 사이의 mismatch는 통합 단계에서 정리했다.
- 최종 검증 기준은 `pytest`, `ruff`, storefront build, admin build다.

## Validation

- `server/.venv/bin/pytest server/tests -q`
- `server/.venv/bin/ruff check server`
- `pnpm --dir client/storefront build`
- `pnpm --dir client/admin build`
```

## `sdd/03_verify/01_feature/lecture_repo_bootstrap_verify.md`

```markdown
# Lecture Repo Verify

## Executed Commands

- `server/.venv/bin/pytest server/tests -q`
- `server/.venv/bin/ruff check server`
- `pnpm --dir client/storefront build`
- `pnpm --dir client/admin build`

## Results

- backend tests: passed (`3 passed`)
- backend lint: passed
- storefront production build: passed
- admin production build: passed

## Coverage Notes

- register/login
- authenticated cart mutation
- order creation
- mock payment confirmation
- buyer order listing
- admin protected endpoints
- admin session bootstrap
- admin payment attempts listing

## Residual Risk

- SQLite baseline과 MySQL runtime parity는 아직 검증되지 않았다.
- migration system이 아직 없어 schema evolution 전략은 후속 과제다.
- payment flow는 mock이므로 외부 provider contract는 검증 대상이 아니다.
```
