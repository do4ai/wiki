---
title: "3. 운영 절차"
---
# do4i — 운영 절차 (배포 이상 대응)

`do4i`가 배포 후 정상 수렴하지 않거나 대표 기능이 비정상일 때 따르는 절차다. 먼저 [서비스 공통 1차 대응 절차](../../서비스 공통 1차 대응 절차/index.md)로 범위를 좁힌 뒤 아래 do4i 특화 확인으로 내려간다.

## 먼저 확인할 운영 단위
- namespace `do4i` / workload `api` Deployment, `mysql` StatefulSet / ingress `api-ingress` / host `agents.do4i.com/api`, `admin.do4i.com/api`.

## 절차

### 1. `api` 와 `mysql` 관계를 먼저 본다
```bash
sudo kubectl get deploy,sts,pods,svc,ing -n do4i
```
- `api` replica 부족 여부, `mysql` 정상 기동 여부, DB 연결로 readiness가 깨진 것은 아닌지. do4i는 앱과 DB가 같이 흔들릴 수 있어 `api`만 보면 안 된다.

### 2. `api` 로그에서 시작 실패 원인을 본다
```bash
sudo kubectl logs deploy/api -n do4i --tail=100
```
- DB 연결 실패 / 환경변수·secret 누락 / migration·startup 실패.

### 3. ingress·backend 연결을 확인한다
```bash
sudo kubectl describe ingress -n do4i api-ingress
sudo kubectl get svc -n do4i
```
- host가 `agents.do4i.com`/`admin.do4i.com` 기준과 맞는가, `/api` 연결, backend service/port.

### 4. DB 이상 여부를 분리한다
```bash
sudo kubectl logs statefulset/mysql -n do4i --tail=100
```
- 앱 설정 문제 / DB 기동 문제 / 앱-DB 연결 문제로 분리.

## 검증 기준
- `api` 재시작 루프 없이 수렴, `mysql` 정상, ingress·service 연결 유지, 대표 `/api` 응답.

## Escalation 또는 롤백 기준
- `api`·`mysql` 동시 비정상 / DB 연결 실패 반복으로 `api` 재시작 / ingress 정상인데 대표 API 무응답 / 직전 배포가 원인 명확.

## 참고
- 롤백 손절차: [Manual/4 ArgoCD 사용법](../../../../Manual/4. 서버와 배포 작업/ArgoCD 사용법/index.md), [k3s 클러스터 접속과 GitOps 배포 점검](../../../../Manual/4. 서버와 배포 작업/k3s 클러스터 접속과 GitOps 배포 점검/index.md).
