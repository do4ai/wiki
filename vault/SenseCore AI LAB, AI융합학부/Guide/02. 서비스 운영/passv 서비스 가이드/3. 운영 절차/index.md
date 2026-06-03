---
title: "3. 운영 절차"
---
# passv — 운영 절차 (배포 이상 대응)

`passv`는 현재 prod 정본이 **EC2(docker-compose) + S3/CloudFront**이고 중앙 gitops(K8s)로 **이전 중**이라, 환경에 따라 보는 곳이 다르다. 먼저 [서비스 공통 1차 대응 절차](../../서비스 공통 1차 대응 절차/index.md)를 적용한다.

## 먼저 확인할 운영 단위
- **현재 prod(EC2)**: API 컨테이너(`passv-server`, `/api/health`), `.env.production`, EC2 호스트, CloudFront(프론트 S3).
- **dev / 컷오버 후(K8s)**: namespace `passv`, workload `api`·`mysql`, ingress `api-ingress`, host `app/api.passv.co.kr/api`.

## 절차 (K8s 기준)

### 1. `api` 와 `mysql` 관계를 본다
```bash
sudo kubectl get deploy,sts,pods,svc,ing -n passv
sudo kubectl logs deploy/api -n passv --tail=100
```
- replica 부족, DB 연결로 readiness 깨짐, 환경변수·secret(Infisical `/apps/passv-*`) 누락, migration·startup 실패.

### 2. ingress·도메인 연결을 확인한다
```bash
sudo kubectl describe ingress -n passv api-ingress
```
- host `app.passv.co.kr`/`api.passv.co.kr` 기준, `/api` 연결. 화면은 뜨는데 API만 죽으면 CloudFront `/api*` origin이 ingress를 가리키는지 확인.

### 3. 현재 prod(EC2)인 경우
```bash
ssh <EC2_HOST_PROD>
docker compose -f infra/compose/prod.yml ps
docker logs passv-server --tail=100
curl -f http://localhost:8000/api/health
```
- 롤백은 passv 레포 `rollback.yml` 또는 직전 `.env.production`/이미지로 재기동.

## 발화 실패 알림 (앱 레벨)
챗봇 발화 실패는 인프라 지표로 안 잡혀, passv 백엔드가 Alerta로 직접 알림을 보낸다. 개요는 [2. 모니터링·알람·SRE](../2. 모니터링·알람·SRE/index.md), 켜기·키 발급·검증은 [Manual/06 Alerta 사용법](../../../../Manual/06. 모니터링-로그 작업/Alerta 사용법/index.md).

## 검증 기준
- `api` 재시작 루프 없이 수렴, `mysql` 정상, `/api/health` 200, 대표 로그인/대화 흐름 동작.

## Escalation 또는 롤백 기준
- `api`·`mysql` 동시 비정상 / DB 연결 실패 반복 / 직전 배포 원인 명확 / 결제·인증 등 핵심 도메인 장애.
- 컷오버 중 장애는 [Manual/04 passv gitops 이전·컷오버 점검](../../../../Manual/04. 서버와 배포 작업/passv gitops 이전·컷오버 점검/index.md)의 롤백 단계.
