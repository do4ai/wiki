---
title: "passv 배포 이상 대응 절차"
---
# passv 배포 이상 대응 절차

## 문서 목적

이 문서는 `passv` 서비스가 배포 후 정상 수렴하지 않거나 대표 기능이 비정상일 때 따르는 상세 대응 절차를 정리한다.

`passv`는 **현재 prod 정본이 EC2(docker-compose) + S3/CloudFront**이고, 중앙 gitops(K8s)로 **이전 중**이다. 그래서 환경에 따라 보는 곳이 다르다.

## 먼저 확인할 운영 단위

- **현재 prod(EC2)**: API 컨테이너(`passv-server`, `/api/health`), `.env.production`, EC2 호스트, CloudFront(프론트 S3) 캐시.
- **dev / 컷오버 후(K8s)**:
  - namespace: `passv`
  - 핵심 workload: `api` Deployment, `mysql` StatefulSet
  - 핵심 ingress: `api-ingress`
  - host/path: `app.passv.co.kr/api`, `api.passv.co.kr/api` (dev `pv.dev.do4ai.com/api`)

## 절차 (K8s 기준)

### 1. 공통 1차 대응을 먼저 적용한다
`서비스 배포 이상 1차 대응 절차`로 Application 상태 → namespace live → 대표 로그를 끝낸 뒤 passv 특화 확인으로 내려간다.

### 2. `api` 와 `mysql` 관계를 본다
```bash
sudo kubectl get deploy,sts,pods,svc,ing -n passv
```
- `api` replica 부족 여부, `mysql` 기동 여부, DB 연결로 readiness가 깨졌는지.

### 3. `api` 로그에서 시작 실패 원인을 본다
```bash
sudo kubectl logs deploy/api -n passv --tail=100
```
- DB 연결 실패 / 환경변수·secret 누락(Infisical `/apps/passv-*` 동기화 여부) / migration·startup 실패.

### 4. ingress·도메인 연결을 확인한다
```bash
sudo kubectl describe ingress -n passv api-ingress
```
- host가 `app.passv.co.kr`/`api.passv.co.kr` 기준과 맞는가, `/api` path 연결, backend service/port.
- 프론트는 S3/CloudFront이므로, 화면은 뜨는데 API만 죽는 경우 CloudFront `/api*` origin이 ingress를 가리키는지 확인.

### 5. 현재 prod(EC2)인 경우
```bash
ssh <EC2_HOST_PROD>
docker compose -f infra/compose/prod.yml ps
docker logs passv-server --tail=100
curl -f http://localhost:8000/api/health
```
- 롤백은 passv 레포 `rollback.yml`(이미지 태그 되돌리기) 또는 직전 `.env.production`/이미지로 재기동.

## 발화 실패 등 앱 레벨 장애를 디스코드로 받기 (Alerta 직접 전송)

챗봇 발화 실패는 인프라 지표(ingress 5xx·배포 가용성)로는 안 잡힌다(200 응답에 오류 본문이거나 외부 LLM/아바타 의존성 실패, 저트래픽 단발 등). 그래서 passv 백엔드가 **Alerta REST API로 직접** 알림을 쏘고, Alerta Discord 플러그인이 디스코드에 게시하게 한다. **EC2/K8s 어디서 돌든** 동작한다.

경로: `passv 백엔드 → https://alerta.do4ai.com/api/alert (Key 인증) → Alerta Discord 플러그인 → 디스코드`

### 활성화 (passv 설정)
`server/config.py`의 Alerta 설정을 환경변수로 켠다(`.env.example` 참고).
```bash
ALERTA_ENABLED=true
ALERTA_API_URL=https://alerta.do4ai.com/api
ALERTA_API_KEY=<passv 전용 키>          # 아래 절차로 발급, Infisical /apps/passv-api 에 저장
ALERTA_CHAT_FAILURE_THRESHOLD=3         # 5분(WINDOW) 내 발화 실패 N건 이상이면 발사(제안값)
ALERTA_CHAT_FAILURE_WINDOW_SECONDS=300
```
구현: `server/shared/infrastructure/alerta.py`의 `notify_chat_failure()`가 `chat_streaming.py`의 발화 실패 except에 연결돼 있다. 알림 실패는 내부에서 삼켜 본 기능을 막지 않는다.

### Alerta 전용 API 키 발급 (ADMIN_KEY 재사용 금지)
1. Alerta(`alerta.do4ai.com`) 관리자 로그인 → **API Keys**에서 `scope=write`, 용도 `passv` 키 생성.
   - 또는 API로: `curl -XPOST https://alerta.do4ai.com/api/key -H "Authorization: Key <ADMIN_KEY>" -H 'Content-Type: application/json' -d '{"user":"passv","scopes":["write:alerts"],"text":"passv app alerts"}'`
2. 발급된 키를 Infisical `do4ai/prod/apps/passv-api`의 `ALERTA_API_KEY`로 저장(EC2면 `.env.production`).
3. ADMIN_KEY(=`alerta-secrets`)는 절대 앱에 넣지 않는다.

### 노이즈 제어
- (resource=`passv/chat`, event=`ChatGenerationFailed`) 단위로 윈도 내 임계·최소 재전송 간격을 둔다.
- Alerta가 (environment, resource, event)로 중복을 묶고 `timeout`(기본 600s)으로 자동 resolve한다.
- 즉시 1건부터 받고 싶으면 `ALERTA_CHAT_FAILURE_THRESHOLD=1`.

### 검증
- 비활성(`ALERTA_ENABLED=false`)이면 아무것도 전송하지 않는다(기본값).
- 임시로 켜고 발화 실패를 N건 유발하면 디스코드에 `major passv/chat` 알림이 떠야 한다.
- 키/URL 점검: `curl -XPOST $ALERTA_API_URL/alert -H "Authorization: Key $ALERTA_API_KEY" -H 'Content-Type: application/json' -d '{"environment":"Production","service":["passv"],"resource":"passv/chat","event":"AlertaSmokeTest","severity":"warning","text":"smoke"}'`

## 검증 기준
- `api` 가 재시작 루프 없이 수렴, `mysql` 정상, `/api/health` 200, 대표 로그인/대화 흐름 동작.

## Escalation 또는 롤백 기준
- `api`·`mysql` 동시 비정상 / DB 연결 실패 반복 / 직전 배포가 원인 명확 / 결제·인증 등 핵심 도메인 장애 → 즉시 공유·롤백.
- 컷오버 중 장애는 [Manual/30 passv gitops 이전·컷오버 점검](../../30. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md)의 롤백 단계를 따른다.

## 작업 후 기록
- 환경(EC2/K8s), Application·파드 상태, ingress/도메인 검증, 최종 조치(관찰/조사/롤백).
