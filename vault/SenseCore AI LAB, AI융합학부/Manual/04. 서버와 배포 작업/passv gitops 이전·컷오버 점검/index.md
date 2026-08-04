---
title: "passv gitops 이전·컷오버 점검"
---
# passv gitops 이전·컷오버 점검

> ⚠️ 이 문서가 참조하는 gitops 경로(`k8s/apps/passv` 등)는 이전 작업에서 생성될 예정이며, 아직 gitops 레포에 존재하지 않는다. TODO(확정 필요): 이전 완료 후 실제 경로 확정.

## 문서 목적

`passv`를 EC2(docker-compose) + S3/CloudFront 운영에서 **중앙 gitops(K8s)** 운영으로 옮기는 절차와 점검 항목을 정리한다.

> ⚠️ **prod 컷오버는 게이팅 작업이다.** MySQL 데이터 이관 + DNS 전환 + 다운타임을 동반하므로, **점검창 합의 후** 진행한다. dev 롤아웃은 안전하게 먼저 검증한다.

## 사전 준비 (확정 필요)

1. **이미지 레지스트리**: prod ECR(`passv-api`) 유지 vs Harbor(`harbor.do4i.com/do4ai/passv-api`)로 통일. 결정 후 overlay `images:` 핀.
2. **Infisical 경로**: `/apps/passv-api`, `/apps/passv-mysql` 생성 + 기존 GitHub Secrets(~30개) 이관.
3. **passv 네임스페이스 universal-auth**: infisical-operator가 `passv` 네임스페이스에 `infisical-universal-auth`를 부트스트랩하도록 설정.
4. **CI 연동**: passv 레포 `backend-dev-harbor.yml` / `update_gitops_image_ref.py`가 `gitops/k8s/apps/passv/overlays/dev/kustomization.yaml`을 갱신하도록 조정.

## 1단계. dev 롤아웃 (안전)

```bash
# gitops 레포에서 렌더 검증
kubectl kustomize k8s/apps/passv/overlays/dev
```
- ArgoCD `passv`(dev) Application이 Synced/Healthy 인지 확인.
- `passv` 네임스페이스 파드(api/mysql), `dev.passv.co.kr/api/health` 응답 확인.
- Infisical 시크릿(`api-secrets`, `mysql-secrets`)이 정상 주입됐는지 확인.

## 2단계. prod 컷오버 (게이팅, 점검창 필요)

1. **데이터 백업**: EC2 MySQL 덤프 확보(롤백 대비 필수).
2. **데이터 이관**: 덤프를 K8s `passv/mysql` StatefulSet로 적재, 무결성 검증.
3. **prod Application 동기화**: `passv`(prod)는 자동 동기화 off → 수동 sync로 워크로드 기동.
4. **DNS/엣지 전환**: `api.passv.co.kr`(및 app/admin의 `/api*`)의 origin을 EC2 → ingress로 전환. CloudFront 캐시/Origin 갱신.
5. **검증**: `/api/health`, 로그인/결제/대화 등 핵심 흐름 스모크 테스트.

## 롤백 기준·방법

- 데이터 무결성 문제 / 핵심 흐름 실패 / 인증·결제 장애 시 즉시 롤백.
- **롤백**: DNS origin을 EC2로 되돌리고, 필요한 경우 EC2를 직전 이미지로 재기동(`rollback.yml`). K8s 측은 prod Application을 동기화 해제 상태로 유지.

## 검증 기준
- dev에서 `passv` 전체 워크로드 정상 + 시크릿 주입 정상.
- prod 컷오버 후 데이터 일치 + 핵심 사용자 흐름 정상 + 모니터링/알림에 `passv` 정상 노출.

## 참고
- 매니페스트 구조·TODO: `gitops/k8s/apps/passv/README.md`.
- 서비스 개요: [passv 서비스 가이드](../../../Guide/02. 서비스 운영/passv 서비스 가이드/index.md).
