---
title: "3. 운영 절차"
---
# papersens — 운영 절차 (배포 이상 대응)

`papersens`가 배포 후 정상 수렴하지 않거나 대표 도메인 접근이 비정상일 때의 절차다. 먼저 [서비스 공통 1차 대응 절차](../../서비스 공통 1차 대응 절차/index.md)를 적용한 뒤 papersens 특화(단일 deployment + wildcard host)를 본다.

## 먼저 확인할 운영 단위
- namespace `papersens` / workload `papersens` Deployment / ingress `papersens-ingress` / host `papersens.do4ai.com`, `*.ps.do4ai.com`.

## 절차

### 1. 단일 deployment 수렴 여부를 먼저 본다
```bash
sudo kubectl get deploy,pods,svc,ing -n papersens
```
- replica 수렴, pod `Running`/`Ready`, service·ingress 동시 생존 여부.

### 2. 앱 로그에서 startup·요청 실패를 본다
```bash
sudo kubectl logs deploy/papersens -n papersens --tail=100
```
- startup 실패 / 환경변수·secret 누락 / 외부 연동(OpenRouter·Ollama) 실패 / 라우팅·host 처리 오류.

### 3. 대표 host 와 wildcard host 를 같이 확인한다
```bash
sudo kubectl describe ingress -n papersens papersens-ingress
sudo kubectl get svc -n papersens
```
- `papersens.do4ai.com` 정상, `*.ps.do4ai.com` wildcard 연결, backend·service port 일치.

### 4. 접근 장애가 앱인지 ingress인지 나눈다
- pod·service 정상인데 외부 접근만 안 됨 → ingress/host / pod 자체가 안 뜸 → 앱 기동·설정 / 특정 host만 안 됨 → wildcard·host rule.

> papersens는 메모리가 무거워 OOMKilled가 자주 원인이 된다. 리소스(메모리)·재시작을 우선 확인.

## 검증 기준
- deployment 정상 수렴, 대표·wildcard host 응답, ingress·service 연결 유지.

## Escalation 또는 롤백 기준
- deployment 미수렴 지속 / 대표·wildcard host 동시 실패 / ingress rule 변경 직후 외부 접근 전면 실패 / startup 실패가 새 변경과 직결.

## 참고
- 롤백·배포 점검: [Manual/4 ArgoCD 사용법](../../../../Manual/4. 서버와 배포 작업/ArgoCD 사용법/index.md).
