---
title: "4. 서버와 배포 작업"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b9813fbc22ca7f38ac4014__4. 서버와 배포 작업
notion_id: 330e313f58b9813fbc22ca7f38ac4014
notion_url: https://www.notion.so/330e313f58b9813fbc22ca7f38ac4014
parent_notion_id: 330e313f58b98098b619f0e3ef2d0fa0
---
# 4. 서버와 배포 작업

이 섹션은 서버 접속, 배포 확인, GitOps 반영, 클러스터 점검처럼 운영 환경을 직접 다루는 절차 문서를 정리한다.

실수 비용이 큰 작업이 많으므로 단계별 체크와 검증 방법을 함께 기록하는 것을 기본으로 한다.

도구별 사용법과 배포 절차는 아래에서 본다.

- `ArgoCD 사용법`: 배포 상태 읽기, 수동 sync, 롤백(GitOps 정석/UI)
- `k3s 클러스터 접속과 GitOps 배포 점검`: 운영 서버 접속, live GitOps 기준 확인, `kubectl`·`Application` 상태 점검
- `Harbor 사용법`: 컨테이너 이미지 레지스트리 확인, `ImagePullBackOff` 원인 분리
- `passv gitops 이전·컷오버 점검`: passv를 EC2에서 중앙 gitops(K8s)로 옮기는 dev 롤아웃·prod 컷오버 절차(게이팅)

## Page Tree

- [ArgoCD 사용법](ArgoCD 사용법/index.md)
- [k3s 클러스터 접속과 GitOps 배포 점검](k3s 클러스터 접속과 GitOps 배포 점검/index.md)
- [Harbor 사용법](Harbor 사용법/index.md)
- [passv gitops 이전·컷오버 점검](passv gitops 이전·컷오버 점검/index.md)
