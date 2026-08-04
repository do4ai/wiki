---
title: "09. Headlamp 클러스터 대시보드"
---
# 09. Headlamp 클러스터 대시보드

`kubectl` 없이 브라우저에서 클러스터 리소스(파드·디플로이먼트·로그 등)를 둘러보는 웹 대시보드다.

## 실제 구성
- **Helm chart 0.41.0**, 두 클러스터 배포(sync-wave 1).
- **접속**: `headlamp.do4ai.com`. (인프라 ingress에 `heaplamp.do4ai.com` 오타 호스트가 함께 있어 정리 대상.)
- **권한**: in-cluster, ClusterRoleBinding `view`(**읽기 전용**). OIDC 비활성(현재 토큰/세션 기반), 세션 TTL 86400s.
- 리소스: CPU 0.1~0.3 / 메모리 128~256Mi.

## 무엇을 위해 보나
- 빠른 시각 점검: 어떤 네임스페이스에서 파드가 Pending/CrashLoop인지, 이벤트·로그를 클릭으로 확인.
- 읽기 전용이므로 변경 작업은 ArgoCD/`kubectl`로 한다.

## 연결
- 깊은 조사는 `kubectl`([Manual 04. k3s 클러스터 접속과 GitOps 배포 점검](../../../Manual/04. 서버와 배포 작업/k3s 클러스터 접속과 GitOps 배포 점검/index.md)), 배포 상태는 [05. ArgoCD 운영 흐름 가이드](../05. ArgoCD 운영 흐름 가이드/index.md).

---

> **온보딩 트랙 1부. 인프라와 플랫폼**
> 이전: [Infisical 시크릿 반영과 권한 변경 절차 (Manual)](../../../Manual/07. 시크릿-권한 작업/Infisical 시크릿 반영과 권한 변경 절차/index.md) · 다음: [02. 서비스 운영 (서비스 카탈로그)](../../02. 서비스 운영/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../시작하기/index.md)
