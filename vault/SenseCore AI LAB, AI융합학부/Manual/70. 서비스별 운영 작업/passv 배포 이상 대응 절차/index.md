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

## 검증 기준
- `api` 가 재시작 루프 없이 수렴, `mysql` 정상, `/api/health` 200, 대표 로그인/대화 흐름 동작.

## Escalation 또는 롤백 기준
- `api`·`mysql` 동시 비정상 / DB 연결 실패 반복 / 직전 배포가 원인 명확 / 결제·인증 등 핵심 도메인 장애 → 즉시 공유·롤백.
- 컷오버 중 장애는 [Manual/30 passv gitops 이전·컷오버 점검](../../30. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md)의 롤백 단계를 따른다.

## 작업 후 기록
- 환경(EC2/K8s), Application·파드 상태, ingress/도메인 검증, 최종 조치(관찰/조사/롤백).
