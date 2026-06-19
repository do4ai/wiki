---
title: "07. 코드 규칙"
---
# 07. 코드 규칙

서비스 레포의 코드 작성·품질 규칙이다. 모든 서비스는 **모노레포**(백엔드 `server/` + 프론트 `client/*` 또는 `web-app/`)이고, 백엔드는 Python·FastAPI, 프론트는 React·Vite·TypeScript다. 각 레포의 상세 정본은 그 레포의 `AGENTS.md`와 `sdd/99_toolchain/02_policies/`다. 이 문서는 조직 공통 기준과 현재 상태를 정리한다.

## 공통 원칙

- 신규/변경 코드는 **타입을 명시**한다(Python type hints, TS strict).
- 네이밍: Python `snake_case`, React 컴포넌트 `PascalCase`, TS 변수·함수 `camelCase`.
- 목업·placeholder 금지(실기능 구현). 미사용 import/변수는 제거한다.
- 문서·계획·검증 산출물은 `sdd/` 하위에만 둔다(top-level `docs/` 금지) — do4i·palcar·passv 공통 거버넌스.

## 백엔드 (Python · FastAPI)

- **버전**: Python 3.12 기준. 패키징은 **uv(`uv.lock`)** 를 표준으로 한다.
- **스타일**: 4-space 들여쓰기, type hints 필수, `snake_case`.
- **린트·포맷**: **ruff**(린트+포맷)를 표준으로 한다.
- **타입체크**: **mypy**(palcar의 `[tool.mypy]` 설정이 기준). 신규 코드에 적용.
- **테스트**: **pytest**(+ `pytest-asyncio`, `asyncio_mode=auto`). 위치 `server/tests/{unit,integration,e2e}`, 규칙 `test_*.py` / `Test*` / `test_*`. **API 변경 시 integration 테스트 1개 이상**을 동반한다.

## 프론트엔드 (React · Vite · TypeScript)

- **버전**: 신규는 React 19 + Vite 7 기준. TS `strict: true`는 모든 앱 필수. **Node 24.14.1 고정**(`.nvmrc`/`.node-version`).
- **린트**: **ESLint flat config**(`eslint.config.js`). `files`에 `ts,tsx`를 포함하고 `@typescript-eslint/parser`를 쓴다(JS 전용 패턴 금지).
- **포맷**: **Prettier**를 표준으로 한다.
- **타입체크**: 빌드에 `tsc`를 포함한다(`tsc -b && vite build`). `vite build`만 두지 않는다.
- **테스트**: **Vitest + Testing Library**(papersens `web-app` 선례). E2E는 CI 워크플로로 운영.

## CI 게이트

- PR(`main` 대상)에서 빌드 + 테스트를 돌린다. palcar는 `server/**` 변경 시 mypy를 강제한다(`server-mypy.yml`).
- 품질 게이트의 실제 위치는 각 레포 `.github/workflows/`다.

## 현재 상태 (레포별 실측)

| 레포 | Python 린트/포맷 | Python 타입 | Python 테스트 | 프론트 린트 | 프론트 테스트 |
| --- | --- | --- | --- | --- | --- |
| passv | 없음 | 없음 | pytest | platform·admin만 ESLint | 없음(E2E는 CI) |
| do4i | 없음 | 없음 | pytest | agents·admin만 ESLint | 없음 |
| palcar | ruff 선언(미사용) | **mypy 구성·CI 강제** | pytest(+JUnit) | 없음 | 없음 |
| papersens | 없음 | 없음 | 없음 | 없음 | Vitest(web-app) |

공통: **Prettier·pre-commit은 전 레포 부재**. 프론트 포매터 없음.

## 통일 과제 (TODO)

- ⚠️ **Python 린트/포맷/타입 미구성**(passv·do4i·papersens): ruff + mypy 도입 필요. palcar 설정을 기준으로 통일.
- ⚠️ **Prettier 전 레포 도입** + pre-commit 훅(ruff/prettier/tsc) 정비.
- ⚠️ **프론트 버전·ESLint·패키지매니저 불일치**: React/Vite/TS 버전, ESLint 적용 범위(ts/tsx), npm/pnpm 표기 통일.
- ⚠️ **빌드 타입체크 누락**(passv·do4i platform/admin): build에 `tsc` 통합.
- ⚠️ **papersens**: `pyproject.toml` 부재(requirements.txt 이원화), `web-app/Dockerfile`이 없는 `pnpm-lock.yaml`을 COPY → 빌드 실패 가능. 패키지매니저(pnpm 선언 vs npm 실사용) 정합 필요.

> 위 TODO는 레포별 설정 변경이 필요한 항목이다. 이 문서는 기준과 현황만 정의하고, 실제 설정 변경은 각 레포에서 PR로 진행한다.
