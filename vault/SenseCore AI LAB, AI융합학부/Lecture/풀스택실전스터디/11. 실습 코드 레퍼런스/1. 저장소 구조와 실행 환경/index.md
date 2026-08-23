---
title: "1. 저장소 구조와 실행 환경"
source_kind: page
source_path: manual-local/lecture/fullstack-study/11-practice-code/01-repo-and-runtime
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 1. 저장소 구조와 실행 환경
이 페이지는 실습 저장소의 겉모양을 담습니다. 04장에서 설계한 모노레포 구조와 로컬 실행 환경이 실제 파일로 어떻게 남았는지 확인하는 자리입니다.

저장소는 `client/`에 storefront와 admin 두 앱을 두고, `server/`에 FastAPI 백엔드를 두며, `scripts/dev/`에 로컬 실행 명령을 모아 둡니다. compose 파일 하나로 서버와 두 클라이언트를 같이 띄우고, CI는 최소한의 검증만 돌리는 초안 상태로 둡니다. 04장의 설명을 읽은 뒤 이 파일들을 대조하면 문서와 코드가 어긋나지 않았는지 바로 알 수 있습니다.

# 파일

## `README.md`

````markdown
# lecture

`lecture`는 `palcar`, `passv`, `do4i`의 공통 모노레포 구조를 참고해 만든
실전형 풀스택 스터디 강의 초안 저장소다.

현재 저장소는 이커머스 프로젝트를 주제로 한 실전형 참고 코드와 강의 진행용 문서를 포함한다.
의도는 다음 두 가지다.

1. 강의에서 바로 설명 가능한 최소 기능을 가진 전체 구조를 제공한다.
2. 이후 인증, DB, 결제, 배포, 테스트 범위를 단계적으로 확장할 수 있는 시작점을 만든다.

## 현재 범위

- `client/storefront`: 구매자용 React + Vite storefront
- `client/admin`: 운영자용 React + Vite admin
- `server`: FastAPI + SQLAlchemy 기반 API
- `scripts/dev`: 로컬 개발 보조 스크립트
- `sdd`: 강의 기획, 계획, 검증 초안

현재 구현은 인메모리 샘플을 넘어서 아래 흐름까지 포함한다.

- buyer 회원가입 / 로그인
- buyer 전용 cart 조회와 mutation
- 주문 생성
- mock payment confirmation
- admin 로그인과 protected dashboard
- SQLite 기반 persistence
- GitHub Actions CI

로컬 기본 DB는 SQLite이며, `DATABASE_URL`을 통해 MySQL-compatible 방향으로 확장할 수 있게 구성했다.

## 구조

```text
lecture/
├─ client/
│  ├─ admin/
│  └─ storefront/
├─ scripts/
│  └─ dev/
├─ sdd/
│  ├─ 01_planning/
│  ├─ 02_plan/
│  └─ 03_verify/
└─ server/
   ├─ api/
   ├─ contexts/
   ├─ shared/
   └─ tests/
```

## 실행

```bash
cp .env.example .env
cp server/.env.example server/.env
pnpm install
docker compose up --build
```

브라우저:

- storefront: `http://127.0.0.1:5173`
- admin: `http://127.0.0.1:5174`
- api health: `http://127.0.0.1:8000/health`

개별 실행:

```bash
pnpm --dir client/storefront dev
pnpm --dir client/admin dev
server/.venv/bin/uvicorn api.app:app --reload --app-dir server
```

백엔드 최초 준비:

```bash
python3 -m venv server/.venv
server/.venv/bin/pip install -e 'server[dev]'
```

## 기본 계정

- live admin: `admin@lecture.test` / `Admin1234!`
- buyer: storefront에서 직접 회원가입
- admin demo fallback: `ops@lecture.local` / `lecture-admin-demo`

## 강의 초안 구성

1. 모노레포 구조 이해
2. FastAPI + SQLAlchemy로 catalog, auth, cart, order, payment mock API 만들기
3. React storefront에서 buyer auth와 checkout 흐름 연결하기
4. Admin dashboard에서 protected route와 운영 read model 읽기
5. 테스트, lint, CI, 검증 문서 남기기
6. 다음 단계로 MySQL, migration, PG 연동, E2E 확대하기

## 검증

```bash
server/.venv/bin/pytest server/tests -q
server/.venv/bin/ruff check server
pnpm --dir client/storefront build
pnpm --dir client/admin build
```

## 다음 확장 후보

- migration 체계 도입
- MySQL 실런타임 검증
- 외부 결제 provider contract
- Playwright E2E
- GitHub Actions deploy workflow
````

## `AGENTS.md`

````markdown
# Repository Guidelines

## Project Structure & Module Organization

This repository is a lecture workspace for a practical fullstack commerce study.

- `client/storefront`: buyer-facing commerce sample app
- `client/admin`: operator-facing admin dashboard sample app
- `server`: FastAPI API with domain-oriented folders
- `scripts/dev`: local development helpers
- `sdd`: planning, plan, and verification records for the lecture flow

Keep the structure aligned with the sibling app repos: separate client apps, a single backend, and durable planning artifacts.

## Build, Test, and Development Commands

Common commands:

```bash
pnpm install
pnpm --dir client/storefront dev
pnpm --dir client/admin dev
pnpm --dir client/storefront build
pnpm --dir client/admin build
uv run --project server pytest
docker compose up --build
```

## Coding Style & Naming Conventions

- Prefer TypeScript for client code and Python 3.11+ for server code.
- Keep React code straightforward and route-oriented.
- Preserve domain names under `server/contexts` such as `catalog`, `cart`, `orders`, and `admin`.
- Keep docs concise and practical; this repo is meant to be taught from.

## Testing Guidelines

- Add backend tests under `server/tests`.
- Prefer API boundary tests for lecture increments.
- Record human-readable outcomes in `sdd/03_verify`.

## Commit & Pull Request Guidelines

- Use short imperative commit messages.
- Separate lecture outline changes from runtime code changes when practical.
- Mention whether a change affects `storefront`, `admin`, `server`, or `sdd`.

## GitOps Reference

- 인프라, GitOps, 배포, 승격, 롤백, 런타임 환경 작업은 루트 `gitops/` 서브모듈의 매니페스트와 운영 문서를 함께 참고한다.
````

## `.claude/CLAUDE.md`

```markdown
# CLAUDE.md

## Repo Guide

- 이 저장소는 실전형 풀스택 스터디 강의를 위한 이커머스 reference workspace다.
- `client/storefront`, `client/admin`, `server`의 세 영역을 한 번에 설명할 수 있는 예제 코드를 유지한다.
- 강의 전달 속도를 위해 현재 런타임 데이터는 인메모리 기반이며, 후속 단계에서 DB와 인증을 붙일 수 있게 구조만 먼저 정리한다.
- 계획, 범위, 검증 기록은 `sdd/` 아래에 남긴다.

## Working Rules

- 구조는 `palcar`, `passv`, `do4i`의 공통 패턴을 참고하되 구현은 더 가볍게 유지한다.
- UI는 storefront와 admin의 역할 차이가 명확히 보이도록 시각적 톤을 분리한다.
- 강의용 repo이므로 README와 SDD 문서도 코드만큼 중요하다.

## Sanity Commands

- `pnpm install`
- `pnpm --dir client/storefront build`
- `pnpm --dir client/admin build`
- `cd server && uv run --extra dev pytest -q`
```

## `pnpm-workspace.yaml`

```yaml
packages:
  - client/*
```

## `.gitignore`

```bash
# frontend
node_modules/
client/storefront/node_modules/
client/storefront/dist/
client/storefront/dist-debug/
client/storefront/*.tsbuildinfo
client/admin/node_modules/
client/admin/dist/
client/admin/dist-debug/
client/admin/*.tsbuildinfo

# python
server/.venv/
server/.pytest_cache/
server/.mypy_cache/
server/__pycache__/
server/**/__pycache__/
server/**/*.pyc

# local
.env
.env.local
server/.env
server/.env.local
.DS_Store
.pnpm-store/
.agentic-dev/generated/
sdd/99_toolchain/01_automation/github-project-kit/task-catalog.json
sdd/99_toolchain/01_automation/github-project-kit/task-sync-state.json

# generated verification artifacts
sdd/**/__pycache__/
sdd/**/*.pyc
sdd/03_verify/10_test/ui_parity/[0-9]*/
sdd/03_verify/10_test/ui_parity/reference/
sdd/03_verify/10_test/ui_parity/reference_pages/
sdd/03_verify/10_test/ui_parity/source_pages/
```

## `.dockerignore`

```bash
.git
.github
README.md
compose.yml
sdd
server
node_modules
**/node_modules
**/dist
**/dist-debug
**/.venv
**/__pycache__
**/.pytest_cache
**/*.tsbuildinfo
```

## `.gitmodules`

```ini
[submodule "gitops"]
	path = gitops
	url = https://github.com/do4ai/gitops.git
```

## `compose.yml`

```yaml
services:
  server:
    container_name: lecture-server
    build:
      context: ./server
      network: host
    env_file:
      - path: ./server/.env.local
        required: false
      - path: ./server/.env
        required: false
      - path: ./server/.env.example
        required: true
    environment:
      DATABASE_URL: ${LECTURE_DATABASE_URL:-sqlite:///./data/lecture.db}
      JWT_SECRET_KEY: ${LECTURE_JWT_SECRET_KEY:-lecture-dev-secret}
      JWT_ALGORITHM: ${LECTURE_JWT_ALGORITHM:-HS256}
      JWT_EXPIRE_MINUTES: ${LECTURE_JWT_EXPIRE_MINUTES:-720}
      BOOTSTRAP_ADMIN_EMAIL: ${LECTURE_ADMIN_EMAIL:-admin@lecture.test}
      BOOTSTRAP_ADMIN_PASSWORD: ${LECTURE_ADMIN_PASSWORD:-Admin1234!}
      BOOTSTRAP_ADMIN_NAME: ${LECTURE_ADMIN_NAME:-Lecture Admin}
      CORS_ORIGINS: '${DASHBOARD_CORS_ORIGINS:-["http://127.0.0.1:5173","http://localhost:5173","http://127.0.0.1:5174","http://localhost:5174"]}'
    ports:
      - "${LECTURE_API_PORT:-8000}:8000"
    volumes:
      - ./server:/app
    command: ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

  storefront:
    container_name: lecture-storefront
    build:
      context: .
      dockerfile: client/Dockerfile
      args:
        APP_DIR: client/storefront
    depends_on:
      server:
        condition: service_started
    environment:
      VITE_API_BASE_URL: ${LECTURE_API_BASE_URL:-http://127.0.0.1:8000/api/v1}
      CHOKIDAR_USEPOLLING: "true"
    ports:
      - "${LECTURE_STOREFRONT_PORT:-5173}:5173"
    volumes:
      - ./client/storefront:/workspace/client/storefront
      - lecture_workspace_node_modules:/workspace/node_modules
      - lecture_storefront_node_modules:/workspace/client/storefront/node_modules

  admin:
    container_name: lecture-admin
    build:
      context: .
      dockerfile: client/Dockerfile
      args:
        APP_DIR: client/admin
    depends_on:
      server:
        condition: service_started
      storefront:
        condition: service_started
    environment:
      VITE_API_BASE_URL: ${LECTURE_API_BASE_URL:-http://127.0.0.1:8000/api/v1}
      CHOKIDAR_USEPOLLING: "true"
    ports:
      - "${LECTURE_ADMIN_PORT:-5174}:5174"
    volumes:
      - ./client/admin:/workspace/client/admin
      - lecture_workspace_node_modules:/workspace/node_modules
      - lecture_admin_node_modules:/workspace/client/admin/node_modules

volumes:
  lecture_workspace_node_modules:
  lecture_storefront_node_modules:
  lecture_admin_node_modules:
```

## `.env.example`

```bash
LECTURE_API_PORT=8000
LECTURE_STOREFRONT_PORT=5173
LECTURE_ADMIN_PORT=5174

LECTURE_API_BASE_URL=http://127.0.0.1:8000/api/v1
LECTURE_DATABASE_URL=sqlite:///./data/lecture.db
LECTURE_JWT_SECRET_KEY=lecture-dev-secret
LECTURE_JWT_ALGORITHM=HS256
LECTURE_JWT_EXPIRE_MINUTES=720
LECTURE_ADMIN_EMAIL=admin@lecture.test
LECTURE_ADMIN_PASSWORD=Admin1234!
LECTURE_ADMIN_NAME=Lecture Admin
DASHBOARD_CORS_ORIGINS=["http://127.0.0.1:5173","http://localhost:5173","http://127.0.0.1:5174","http://localhost:5174"]
```

## `server/.env.example`

```bash
APP_NAME=Lecture Commerce API
API_PREFIX=/api/v1
DATABASE_URL=sqlite:///./data/lecture.db
JWT_SECRET_KEY=lecture-dev-secret
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=720
BOOTSTRAP_ADMIN_EMAIL=admin@lecture.test
BOOTSTRAP_ADMIN_PASSWORD=Admin1234!
BOOTSTRAP_ADMIN_NAME=Lecture Admin
CORS_ORIGINS=["http://127.0.0.1:5173","http://localhost:5173","http://127.0.0.1:5174","http://localhost:5174"]
```

## `client/Dockerfile`

```dockerfile
FROM node:20-bookworm-slim AS deps

ARG APP_DIR

WORKDIR /workspace

RUN corepack enable && corepack prepare pnpm@10.32.1 --activate

COPY pnpm-lock.yaml pnpm-workspace.yaml /workspace/
COPY ${APP_DIR}/package.json /workspace/${APP_DIR}/package.json

RUN pnpm install --dir "${APP_DIR}" --lockfile-dir /workspace --frozen-lockfile

FROM node:20-bookworm-slim

ARG APP_DIR
ENV APP_DIR=${APP_DIR}

WORKDIR /workspace

RUN corepack enable && corepack prepare pnpm@10.32.1 --activate

COPY --from=deps /workspace/pnpm-lock.yaml /workspace/pnpm-lock.yaml
COPY --from=deps /workspace/pnpm-workspace.yaml /workspace/pnpm-workspace.yaml
COPY --from=deps /workspace/node_modules /opt/bootstrap/node_modules
COPY --from=deps /workspace/${APP_DIR}/node_modules /opt/bootstrap/${APP_DIR}/node_modules

CMD ["sh", "-lc", "mkdir -p /workspace/node_modules \"$APP_DIR/node_modules\" && if [ -z \"$(ls -A /workspace/node_modules 2>/dev/null)\" ]; then cp -a /opt/bootstrap/node_modules/. /workspace/node_modules/; fi && if [ -z \"$(ls -A \"$APP_DIR/node_modules\" 2>/dev/null)\" ]; then cp -a \"/opt/bootstrap/$APP_DIR/node_modules/.\" \"$APP_DIR/node_modules/\"; fi && pnpm --dir \"$APP_DIR\" dev"]
```

## `server/Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml /app/pyproject.toml
COPY README.md /app/README.md
COPY api /app/api
COPY contexts /app/contexts
COPY shared /app/shared
COPY data /app/data
COPY config.py /app/config.py
COPY main.py /app/main.py

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## `server/Makefile`

```makefile
.PHONY: test-server test-backend lint run

JUNIT ?= 0
JUNIT_OUT ?= .reports/pytest-junit.xml
ifeq ($(JUNIT),1)
PYTEST_JUNIT := --junitxml $(JUNIT_OUT)
endif

test-server:
	@if [ "$(JUNIT)" = "1" ]; then mkdir -p "$(dir $(JUNIT_OUT))"; fi
	uv run --extra dev python -m pytest -q $(PYTEST_JUNIT)

test-backend: test-server

lint:
	uv run --extra dev ruff check .

run:
	uv run uvicorn api.app:app --reload
```

## `server/pyproject.toml`

```toml
[project]
name = "lecture-commerce-server"
version = "0.1.0"
description = "Lecture commerce reference API"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
  "fastapi==0.116.1",
  "PyJWT==2.9.0",
  "sqlalchemy==2.0.36",
  "uvicorn[standard]==0.35.0",
  "pydantic-settings==2.10.1"
]

[project.optional-dependencies]
dev = [
  "pytest==8.4.1",
  "httpx==0.28.1",
  "ruff==0.12.11"
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["api", "shared", "contexts"]

[tool.pytest.ini_options]
pythonpath = ["."]
```

## `server/README.md`

````markdown
# lecture server

FastAPI 기반 이커머스 강의용 reference API다.

## 현재 도메인

- `catalog`: 상품 조회
- `cart`: 장바구니 상태 변경
- `orders`: 주문 요약 조회
- `admin`: 운영 지표 조회

## 실행

```bash
cp .env.example .env
uv run uvicorn api.app:app --reload
```

## 테스트

```bash
uv run pytest
```
````

## `server/data/README.md`

```markdown
`data/` is the template-aligned runtime data root for Template server.

- `data/storage/`: local file uploads and runtime artifacts
- committed bootstrap datasets are not used by Template right now
```

## `scripts/dev/server_up.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

docker compose up -d --build
```

## `scripts/dev/server_down.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

docker compose down
```

## `scripts/dev/server_logs.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

docker compose logs -f server storefront admin
```

## `.github/workflows/ci.yml`

```yaml
name: Monorepo CI

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  test-and-build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 10.32.1

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: pnpm

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Setup uv
        uses: astral-sh/setup-uv@v5

      - name: Install frontend dependencies
        run: pnpm install --frozen-lockfile

      - name: Install backend dependencies
        run: uv sync --project server --extra dev

      - name: Run backend tests
        run: uv run --project server pytest

      - name: Build storefront
        run: pnpm --dir client/storefront build

      - name: Build admin
        run: pnpm --dir client/admin build
```
