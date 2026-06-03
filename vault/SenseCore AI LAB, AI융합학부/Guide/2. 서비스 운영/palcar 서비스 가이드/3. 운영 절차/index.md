---
title: "3. 운영 절차"
---
# palcar — 운영 절차 (배포 이상 대응)

`palcar`가 배포 후 정상 수렴하지 않거나 핵심 경로가 비정상일 때의 절차다. 먼저 [서비스 공통 1차 대응 절차](../../서비스 공통 1차 대응 절차/index.md)를 적용한 뒤 palcar 특화 확인을 본다.

## 먼저 확인할 운영 단위
- namespace `palcar` / workload `api` Deployment, `mysql` StatefulSet / ingress `palcar` / 경로 `/api`, `/health`.

## 절차

### 1. `/health` 와 `/api` 기준을 분리해 본다
```bash
sudo kubectl get deploy,sts,pods,svc,ing -n palcar
```
- 앱이 안 뜨는가 / 앱은 뜨지만 `/health`만 실패하는가 / `/health`는 되는데 `/api`만 실패하는가. 이 분리가 ingress vs 앱 기능 문제를 빠르게 좁힌다.

### 2. `api` 와 `mysql` 상태를 같이 본다
```bash
sudo kubectl logs deploy/api -n palcar --tail=100
sudo kubectl logs statefulset/mysql -n palcar --tail=100
```
- DB 연결 실패 / 환경변수·secret 누락 / startup 실패 / 외부 연동 실패.

### 3. ingress 경로·backend 연결을 확인한다
```bash
sudo kubectl describe ingress -n palcar palcar
sudo kubectl get svc -n palcar
```
- host가 `palcar.do4ai.com`/`admin.palcar.do4ai.com` 기준과 맞는가, `/api`·`/health` path 연결, service port 일치.

### 4. `/health` 기준으로 회복 여부를 먼저 본다
- 대표 기능보다 `/health` 회복을 먼저 확인하면 앱 기동 회복과 사용자 기능 장애를 나눠 볼 수 있다.

## 검증 기준
- `api`·`mysql` 정상 수렴, `/api`·`/health` 단절 없음, 앱 로그 반복 치명 오류 해소.

## Escalation 또는 롤백 기준
- `ImagePullBackOff`/`CrashLoopBackOff` 지속 / `/health` 미회복 / DB 연결 실패 반복 / ingress path 변경 직후 API·health 동시 다운.

## 참고
- 롤백·배포 점검: [Manual/4 ArgoCD 사용법](../../../../Manual/4. 서버와 배포 작업/ArgoCD 사용법/index.md).
