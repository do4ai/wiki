---
title: "2. 환경 분리와 GitOps, 런타임 연결"
source_kind: page
source_path: manual-local/lecture/fullstack-study/10-deploy-ops-scale/02-env-gitops-runtime
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 2. 환경 분리와 GitOps, 런타임 연결
이전 페이지에서는 `storefront`, `admin`, `server`를 배포 가능한 아티팩트로 나눴습니다. 이번 페이지에서는 그 아티팩트를 어떤 환경에, 어떤 설정으로, 어떤 GitOps 흐름을 통해 올릴지 정리합니다. 배포 아티팩트가 만들어졌다고 해서 곧바로 운영 서비스가 되는 것은 아닙니다. 이미지, 환경 변수, secret, 도메인, DB, ingress, 동기화 정책이 런타임에서 정확히 만나야 합니다.

실전 서비스에서 환경 분리는 단순히 `.env.dev`, `.env.prod`를 나누는 일이 아닙니다. 개발 환경은 빠른 실험을 위한 곳이고, 스테이징은 운영과 최대한 비슷하게 검증하는 곳이며, 운영은 사용자 데이터와 결제가 걸린 실제 환경입니다. 각 환경은 같은 이미지를 쓰되 다른 설정과 다른 데이터, 다른 접근 권한을 가져야 합니다.

즉 이번 페이지는 "이미지를 만들었다" 다음에 반드시 필요한, 환경별 실행 계약과 GitOps 배포 경로를 정하는 단계입니다.

# 왜 환경 분리가 중요한가
환경 분리가 불명확하면 개발 중에는 동작하던 기능이 운영에서 깨지거나, 더 위험하게는 개발 설정이 운영에 섞일 수 있습니다.

- 운영 DB를 로컬에서 실수로 바라볼 수 있다
- staging에서 검증하지 않은 이미지가 prod에 바로 올라갈 수 있다
- 프론트가 운영 API 대신 dev API를 호출할 수 있다
- LLM key나 결제 secret이 잘못된 환경에 주입될 수 있다
- rollback할 때 어떤 manifest를 되돌려야 하는지 모를 수 있다

환경 분리는 실수의 폭을 줄이는 구조입니다.

# 이 페이지에서 정할 것
이 페이지를 읽고 나면 아래 항목이 정리되어 있어야 합니다.

- dev, staging, prod는 무엇이 다른가
- 같은 이미지와 다른 설정을 어떻게 조합하는가
- GitOps repository에는 무엇이 들어가는가
- 애플리케이션 repo와 GitOps repo는 어떤 책임을 나누는가
- secret은 어디서 주입하고 어디에 기록하지 않는가
- 배포가 실제 런타임에 반영됐는지 어떻게 확인하는가

# 1. 환경은 세 단계로 나눈다
실전 교재에서는 환경을 최소 세 단계로 설명하는 것이 좋습니다.

- dev: 개발자가 빠르게 실행하고 확인하는 환경
- staging: 운영과 비슷한 조건에서 릴리스 후보를 검증하는 환경
- prod: 실제 사용자가 접근하는 운영 환경

작은 프로젝트에서는 dev와 prod만 있어도 시작할 수 있습니다. 하지만 교재에서는 staging 개념을 반드시 설명해야 합니다. staging이 있어야 배포 전 마지막 검증과 rollback 연습이 가능합니다.

# 2. 환경별로 달라지는 것
환경별로 달라지는 것은 코드가 아니라 설정입니다.

대표 차이는 아래입니다.

- API base URL
- database URL
- allowed origin
- log level
- secret key
- LLM provider key
- RAG index path
- payment provider mode
- domain과 ingress
- replica 수와 resource limit

같은 이미지라도 이 값이 다르면 완전히 다른 런타임으로 동작합니다.

# 3. 환경별로 같아야 하는 것
반대로 환경이 달라도 같아야 하는 것이 있습니다.

- 이미지 안의 애플리케이션 코드
- API 계약
- migration 순서
- health check endpoint
- 로그 포맷
- 권한 모델
- 핵심 E2E 시나리오

환경마다 코드가 달라지기 시작하면 staging 검증이 prod를 보장하지 못합니다. 가능하면 같은 이미지 태그를 staging에서 검증한 뒤 prod로 승격하는 방식이 좋습니다.

# 4. 애플리케이션 repo와 GitOps repo의 책임
애플리케이션 repo에는 앱 코드와 빌드 정의가 있습니다.

애플리케이션 repo의 책임은 아래입니다.

- 소스 코드
- 테스트
- Dockerfile
- build script
- image tag 생성
- `.env.example`
- 애플리케이션 문서

GitOps repo의 책임은 런타임 선언입니다.

- Kubernetes manifest
- Helm values 또는 Kustomize overlay
- image tag pinning
- ingress
- service
- configmap
- secret reference
- resource request/limit
- environment별 overlay

이 둘을 나누면 코드 변경과 런타임 변경을 분리해서 검토할 수 있습니다.

# 5. GitOps 배포 흐름
기본 흐름은 아래처럼 잡습니다.

1. 애플리케이션 repo에서 테스트와 빌드를 통과한다
2. 컨테이너 이미지를 registry에 push한다
3. GitOps repo의 환경별 manifest에서 image tag를 갱신한다
4. GitOps repo 변경을 리뷰하고 merge한다
5. ArgoCD 같은 GitOps controller가 변경을 감지한다
6. cluster에 manifest가 반영된다
7. health check와 smoke test로 live 상태를 확인한다

핵심은 cluster를 직접 수정하지 않고 Git의 선언 상태를 바꾸는 것입니다.

# 6. manifest는 어떻게 나누는가
Kubernetes 기준으로는 base와 overlay 구조가 자연스럽습니다.

예시는 아래와 같습니다.

- `base/server`
- `base/storefront`
- `base/admin`
- `overlays/dev`
- `overlays/staging`
- `overlays/prod`

base에는 공통 구조를 두고, overlay에는 환경별 차이를 둡니다. 예를 들어 prod에서는 replica 수와 도메인, resource limit이 다를 수 있습니다.

# 7. ConfigMap과 Secret을 구분한다
환경 설정은 ConfigMap과 Secret으로 나눕니다.

ConfigMap에 들어갈 수 있는 값은 아래입니다.

- `LOG_LEVEL`
- `CORS_ORIGINS`
- `APP_ENV`
- `RAG_INDEX_PATH`
- public runtime config

Secret에 들어가야 하는 값은 아래입니다.

- `DATABASE_URL`
- `SECRET_KEY`
- `LLM_API_KEY`
- 결제 provider secret
- 외부 서비스 token

secret 값은 Git에 평문으로 커밋하지 않습니다. GitOps에서는 sealed secret, external secret, cloud secret manager 같은 방식을 사용합니다.

# 8. 프론트 런타임 설정은 어떻게 연결하는가
프론트 앱은 빌드 시점 설정과 런타임 설정을 구분해야 합니다.

초기 구조에서는 build time 환경 변수로 시작할 수 있습니다.

- `VITE_API_BASE_URL`
- `VITE_APP_ENV`
- `VITE_CHAT_ENABLED`

하지만 운영 환경이 늘어나면 같은 이미지로 여러 환경을 돌리기 어렵습니다. 그때는 컨테이너 시작 시 `runtime-config.json`을 주입하거나, Nginx template으로 public config를 생성하는 방식이 유용합니다.

중요한 원칙은 하나입니다. 프론트 런타임 설정에는 secret을 넣지 않습니다.

# 9. 백엔드 런타임 설정은 어떻게 연결하는가
백엔드는 시작 시 환경 변수를 읽고 설정 객체를 구성합니다.

필수 설정은 아래처럼 명확히 검증해야 합니다.

- `DATABASE_URL`이 없으면 서버 시작 실패
- `SECRET_KEY`가 없으면 서버 시작 실패
- prod에서 debug mode가 켜져 있으면 서버 시작 실패
- `CORS_ORIGINS`가 비어 있으면 prod 시작 실패
- LLM 기능이 켜져 있는데 `LLM_API_KEY`가 없으면 시작 실패 또는 기능 비활성화

런타임 설정 검증은 장애를 빨리 드러내는 장치입니다. 조용히 잘못된 기본값으로 실행되는 서버가 더 위험합니다.

# 10. DB migration은 언제 실행하는가
배포에서 DB migration은 가장 조심해야 하는 단계입니다.

초기 교재에서는 아래 원칙으로 시작합니다.

- migration은 이미지 빌드가 아니라 배포 절차에서 실행한다
- staging에서 먼저 실행하고 검증한다
- prod에서는 백업 또는 rollback 계획을 확인한다
- 애플리케이션 코드와 schema 변경 순서를 맞춘다
- destructive migration은 별도 검토한다

MVP에서는 SQLite에서 시작할 수 있지만, 운영 배포를 설명할 때는 PostgreSQL 같은 실제 DB와 migration 도구를 기준으로 확장해야 합니다.

# 11. ingress와 도메인 연결
런타임에는 외부 요청이 어떤 앱으로 들어오는지 정해야 합니다.

예시는 아래와 같습니다.

- `shop.example.com`: storefront
- `admin.example.com`: admin
- `api.example.com`: server

또는 한 도메인 아래 path로 나눌 수도 있습니다.

- `/`: storefront
- `/admin`: admin
- `/api`: server

도메인 전략은 인증, CORS, cookie, 보안 헤더에 영향을 주므로 초기에 명확히 정해야 합니다.

# 12. CORS와 cookie 설정
프론트와 백엔드 도메인이 분리되면 CORS와 cookie 설정이 중요해집니다.

확인할 항목은 아래입니다.

- storefront origin 허용
- admin origin 허용
- 불필요한 wildcard origin 제거
- credential 사용 여부 명확화
- prod cookie secure 설정
- SameSite 정책 확인

인증이 토큰 기반인지 cookie 기반인지에 따라 설정이 달라집니다. 어떤 방식을 택하든 prod에서 느슨한 CORS를 쓰면 안 됩니다.

# 13. 배포 반영은 어떻게 확인하는가
GitOps controller가 sync했다고 끝이 아닙니다. 실제 서비스 상태를 확인해야 합니다.

확인 순서는 아래입니다.

1. GitOps app sync 상태 확인
2. pod rollout 상태 확인
3. image tag가 기대한 커밋인지 확인
4. health endpoint 확인
5. storefront와 admin 접속 확인
6. server API smoke test 실행
7. 로그에 startup error가 없는지 확인

배포는 manifest 반영이 아니라 사용자 흐름이 살아 있는 상태까지 확인해야 합니다.

# 14. 환경별 smoke test
각 환경에는 최소 smoke test가 있어야 합니다.

dev에서는 아래 정도면 충분합니다.

- server health
- storefront 첫 화면
- admin 첫 화면

staging에서는 아래까지 확인합니다.

- 로그인
- 상품 목록
- 장바구니
- 주문 생성
- admin 주문 확인

prod에서는 조심스럽게 확인합니다.

- health
- 상품 목록
- 로그인 또는 read-only smoke
- admin 접근
- 오류율 확인

prod smoke는 실제 사용자 데이터와 결제가 있으므로 테스트 계정과 테스트 상품을 분리하는 편이 좋습니다.

# 15. 이번 장의 구현 완료 기준은 무엇인가
이번 장에서 완료라고 볼 수 있는 상태는 아래 정도입니다.

- dev, staging, prod 차이가 문서화되어 있다
- app repo와 GitOps repo 책임이 분리되어 있다
- 환경별 manifest 또는 overlay 구조가 있다
- ConfigMap과 Secret 기준이 정해져 있다
- 프론트와 백엔드 런타임 설정 방식이 정해져 있다
- migration 실행 기준이 있다
- 배포 반영 확인 절차가 있다
- 환경별 smoke test가 있다

즉 이미지를 만들고 끝나는 것이 아니라, 실제 환경에서 올바른 설정으로 실행되는지 확인할 수 있어야 합니다.

# 16. 이번 페이지를 실제 구현 산출물로 바꾸면 무엇이 나와야 하나
이번 페이지를 코드와 실행 결과로 옮기면 최소한 아래 산출물이 있어야 합니다.

- GitOps manifest 구조
- dev/staging/prod overlay
- ConfigMap template
- Secret reference
- ingress 설정
- image tag update 절차
- migration 실행 절차
- 환경별 smoke test script
- ArgoCD 또는 GitOps sync 확인 절차

이 산출물이 있어야 다음 페이지에서 롤백, 운영 런북, 장애 대응을 실제 배포 환경 기준으로 다룰 수 있습니다.

# 17. 자주 하는 실수
- dev 설정을 prod에 그대로 사용한다
- 운영 secret을 Git에 평문으로 커밋한다
- cluster에 직접 hotfix하고 GitOps repo를 갱신하지 않는다
- staging에서 검증하지 않은 이미지를 prod에 올린다
- CORS를 wildcard로 열어 둔다
- image tag를 `latest`로만 관리한다
- GitOps sync 성공을 서비스 정상으로 착각한다

이 일곱 가지 실수는 배포 사고와 운영 drift의 대표 원인입니다.

# 정리
이번 페이지에서는 배포 아티팩트를 dev, staging, prod 환경에 연결하는 방법을 정리했습니다. 핵심은 같은 이미지를 환경별 설정과 GitOps manifest로 실행하고, secret과 config를 분리하며, sync 이후 실제 런타임 상태를 smoke test로 확인하는 것입니다.

# 다음으로 이어지는 것
다음 페이지에서는 롤백과 운영 런북과 장애 대응을 정리합니다.
