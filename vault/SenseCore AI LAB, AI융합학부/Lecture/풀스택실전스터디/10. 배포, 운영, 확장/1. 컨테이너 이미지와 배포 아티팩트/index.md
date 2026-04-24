---
title: "1. 컨테이너 이미지와 배포 아티팩트"
source_kind: page
source_path: manual-local/lecture/fullstack-study/10-deploy-ops-scale/01-images-artifacts
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 1. 컨테이너 이미지와 배포 아티팩트
이전 장에서는 통합 검증, 성능과 보안, 운영 점검표, 릴리스 체크리스트를 정리했습니다. 이제 마지막 장에서는 지금까지 만든 이커머스 서비스를 실제 배포 가능한 단위로 묶습니다. 이번 페이지의 목표는 코드를 "내 컴퓨터에서 실행되는 프로젝트"에서 "런타임에 올릴 수 있는 아티팩트"로 바꾸는 것입니다.

배포는 단순히 `docker build`를 하는 일이 아닙니다. 어떤 앱을 어떤 이미지로 만들지, 프론트 정적 파일을 어디에서 서빙할지, 서버 이미지는 어떤 환경 변수를 필요로 하는지, 이미지 태그는 어떤 기준으로 붙일지, 배포 전 어떤 검증을 통과해야 하는지 정해야 합니다.

즉 이번 페이지는 `storefront`, `admin`, `server`를 명확한 배포 단위로 나누고, 각 단위가 어떤 빌드 결과와 런타임 계약을 갖는지 정리하는 단계입니다.

# 왜 배포 아티팩트를 먼저 정해야 하는가
배포 아티팩트가 불명확하면 운영 환경에서 문제가 생겼을 때 원인을 좁히기 어렵습니다.

- 어떤 커밋이 배포됐는지 알 수 없다
- storefront와 admin이 서로 다른 API 계약을 보고 있을 수 있다
- 서버 이미지는 바뀌었는데 정적 자산은 예전 버전일 수 있다
- 환경 변수 누락이 빌드 문제인지 런타임 문제인지 구분하기 어렵다
- 롤백할 이미지 태그를 찾기 어렵다

따라서 배포 전에 먼저 "무엇을 만들어서 어디에 올릴 것인가"를 고정해야 합니다.

# 이 페이지에서 정할 것
이 페이지를 읽고 나면 아래 항목이 정리되어 있어야 합니다.

- 배포 단위는 몇 개인가
- 각 단위는 어떤 빌드 결과물을 갖는가
- 컨테이너 이미지는 어떻게 나누는가
- 이미지 태그는 어떤 규칙으로 붙이는가
- 환경 변수와 secret은 이미지에 들어가지 않는가
- 배포 전 아티팩트 검증은 무엇인가

# 1. 이 프로젝트의 배포 단위
이번 이커머스 프로젝트의 기본 배포 단위는 세 개입니다.

- `storefront`: 구매자 웹 앱
- `admin`: 운영자 웹 앱
- `server`: FastAPI 백엔드 API

여기에 선택적으로 `worker`나 `scheduler`가 붙을 수 있지만, MVP에서는 세 단위로 충분합니다. AI 상담 챗봇도 처음에는 `server` 안의 `support` 컨텍스트로 배포합니다.

# 2. storefront 배포 아티팩트
`storefront`는 React/Vite 앱입니다. 빌드 결과는 정적 파일입니다.

기본 산출물은 아래입니다.

- `index.html`
- JS bundle
- CSS bundle
- 이미지와 정적 asset
- build manifest

이 아티팩트는 Nginx, CDN, object storage, 또는 프론트 전용 컨테이너에서 서빙할 수 있습니다. 교재에서는 처음에 컨테이너로 감싸 배포 단위를 명확히 하고, 이후 CDN 확장을 설명하는 흐름이 좋습니다.

# 3. admin 배포 아티팩트
`admin`도 React/Vite 앱이지만 목적과 접근 권한이 다릅니다.

기본 산출물은 storefront와 비슷합니다.

- `index.html`
- JS bundle
- CSS bundle
- 운영자 화면 asset
- build manifest

하지만 배포 관점에서는 별도 앱으로 분리하는 편이 좋습니다. admin은 접근 제어, 도메인, 보안 헤더, 인증 실패 처리 기준이 storefront와 다를 수 있기 때문입니다.

# 4. server 배포 아티팩트
`server`는 FastAPI 앱입니다. 배포 아티팩트는 실행 가능한 컨테이너 이미지로 봅니다.

이미지에는 아래가 포함됩니다.

- 애플리케이션 코드
- Python dependency
- ASGI server 실행 설정
- migration 또는 seed 실행 도구
- health check endpoint

이미지에 포함하면 안 되는 것은 아래입니다.

- 실제 DB 비밀번호
- API secret
- LLM provider key
- 운영 환경별 설정값
- 사용자 데이터

이미지는 환경과 분리되어야 합니다. 같은 이미지를 dev, staging, prod에서 다른 환경 변수로 실행할 수 있어야 합니다.

# 5. 이미지 분리 전략
MVP에서는 아래 이미지 구성이 자연스럽습니다.

- `lecture-storefront`
- `lecture-admin`
- `lecture-server`

이미지를 하나로 합치면 처음에는 편해 보이지만, 배포와 롤백이 거칠어집니다. storefront만 바꿨는데 server까지 같이 교체해야 하고, admin만 롤백하기도 어려워집니다. 따라서 앱 경계와 배포 경계를 맞추는 편이 좋습니다.

# 6. Dockerfile은 어떤 기준으로 작성하는가
Dockerfile은 재현 가능해야 합니다.

프론트 이미지는 보통 아래 단계로 구성합니다.

1. dependency 설치
2. build 실행
3. 정적 파일을 서빙 이미지로 복사
4. health 또는 basic route 확인

백엔드 이미지는 아래 단계로 구성합니다.

1. Python runtime 선택
2. dependency 설치
3. 애플리케이션 코드 복사
4. non-root user 설정
5. ASGI server 실행
6. health check 연결

처음부터 극단적으로 최적화하기보다, 빌드가 재현되고 secret이 들어가지 않으며 실행 명령이 명확한 것이 우선입니다.

# 7. 이미지 태그 규칙
이미지 태그는 배포 추적의 핵심입니다.

권장 태그는 아래 조합입니다.

- git short SHA
- semantic version 또는 release version
- build timestamp
- environment tag

예를 들어 `lecture-server:9c222d4`처럼 커밋 기준 태그를 붙이면 어떤 코드가 배포되었는지 추적하기 쉽습니다. `latest`만 쓰는 방식은 롤백과 장애 분석을 어렵게 만듭니다.

# 8. 환경 변수는 어떻게 분리하는가
이미지와 환경 설정은 분리해야 합니다.

server가 필요로 하는 환경 변수 예시는 아래입니다.

- `DATABASE_URL`
- `SECRET_KEY`
- `CORS_ORIGINS`
- `LLM_API_KEY`
- `RAG_INDEX_PATH`
- `LOG_LEVEL`

프론트가 필요로 하는 설정 예시는 아래입니다.

- `VITE_API_BASE_URL`
- `VITE_APP_ENV`
- `VITE_CHAT_ENABLED`

단, 프론트 빌드에 들어가는 값은 사용자에게 노출될 수 있다는 점을 기억해야 합니다. secret은 절대 프론트 환경 변수에 넣지 않습니다.

# 9. build와 runtime 설정을 구분한다
프론트는 build time 설정과 runtime 설정이 섞이기 쉽습니다.

초기에는 `VITE_API_BASE_URL`처럼 build time 환경 변수로 시작해도 됩니다. 하지만 배포 환경이 많아지면 같은 정적 파일을 여러 환경에 배포하기 어렵습니다. 후속 확장에서는 runtime config 파일을 별도로 주입하는 방식도 고려할 수 있습니다.

백엔드는 보통 runtime 환경 변수로 설정을 읽습니다. 그래서 같은 server 이미지를 staging과 prod에 재사용하기 쉽습니다.

# 10. 배포 전 아티팩트 검증
이미지를 만들기 전에 아래를 확인합니다.

- backend test 통과
- storefront build 통과
- admin build 통과
- lint 또는 typecheck 통과
- 환경 변수 샘플 문서 최신화
- Docker build 성공
- 이미지 실행 후 health check 통과

빌드가 성공해도 컨테이너 실행이 실패할 수 있습니다. 따라서 최소한 `docker run` 또는 compose 기반 smoke check를 한 번 거쳐야 합니다.

# 11. 이미지 내부에서 확인할 것
이미지를 만든 뒤에는 아래를 확인합니다.

- 예상한 포트가 열린다
- health endpoint가 응답한다
- 정적 파일이 존재한다
- 불필요한 dev dependency가 과도하게 들어가지 않았다
- secret이나 `.env` 파일이 이미지에 포함되지 않았다
- 로그가 stdout/stderr로 나온다

컨테이너 런타임에서는 파일 로그보다 stdout/stderr 로그가 수집하기 쉽습니다.

# 12. 아티팩트 목록은 어떻게 문서화하는가
릴리스마다 아래 항목을 남기면 좋습니다.

- 앱 이름
- 이미지 이름
- 이미지 태그
- git commit
- build command
- runtime command
- 필요한 환경 변수
- health check URL
- rollback 대상 태그

이 표가 있으면 배포와 롤백이 훨씬 명확해집니다.

# 13. 이번 장의 구현 완료 기준은 무엇인가
이번 장에서 완료라고 볼 수 있는 상태는 아래 정도입니다.

- storefront 배포 아티팩트가 정의되어 있다
- admin 배포 아티팩트가 정의되어 있다
- server 배포 이미지가 정의되어 있다
- 이미지 태그 규칙이 있다
- secret이 이미지에 들어가지 않는 기준이 있다
- Docker build와 실행 smoke check가 있다
- 릴리스별 아티팩트 목록을 남길 수 있다

즉 이제 코드는 배포 가능한 단위로 포장될 준비가 된 상태입니다.

# 14. 이번 페이지를 실제 구현 산출물로 바꾸면 무엇이 나와야 하나
이번 페이지를 코드와 실행 결과로 옮기면 최소한 아래 산출물이 있어야 합니다.

- storefront Dockerfile
- admin Dockerfile
- server Dockerfile
- image build script
- image tag 규칙
- `.env.example`
- container smoke test
- release artifact table
- secret 포함 여부 점검

이 산출물이 있어야 다음 페이지에서 환경 분리, GitOps, 런타임 연결을 안정적으로 다룰 수 있습니다.

# 15. 자주 하는 실수
- 모든 앱을 하나의 이미지에 넣어 배포와 롤백을 어렵게 만든다
- `latest` 태그만 사용해 어떤 코드가 배포됐는지 알 수 없다
- `.env`나 secret을 이미지에 포함한다
- build 성공만 보고 컨테이너 실행 검증을 하지 않는다
- storefront와 admin이 서로 다른 API 계약을 보고 있는지 확인하지 않는다
- 프론트 환경 변수에 secret을 넣는다
- health check 없이 배포한다

이 일곱 가지 실수는 배포 이후 원인 분석과 롤백을 어렵게 만듭니다.

# 정리
이번 페이지에서는 storefront, admin, server를 배포 가능한 아티팩트로 나누고, 각 아티팩트의 이미지 구조, 태그 규칙, 환경 변수 분리, 검증 기준을 정리했습니다. 핵심은 컨테이너 이미지를 만드는 것 자체가 아니라, 어떤 코드와 설정이 어떤 런타임 단위로 배포되는지 추적 가능하게 만드는 것입니다.

# 다음으로 이어지는 것
다음 페이지에서는 환경 분리와 GitOps와 런타임 연결을 정리합니다.
