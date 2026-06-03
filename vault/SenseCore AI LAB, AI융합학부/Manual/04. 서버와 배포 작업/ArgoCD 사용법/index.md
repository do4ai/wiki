---
title: "ArgoCD 사용법"
---
# ArgoCD 사용법

데이터센스 배포의 핵심 도구인 ArgoCD를 운영에서 어떻게 쓰는지 정리한다. 개념(왜 GitOps인가)은 [Guide/01 05. ArgoCD 운영 흐름 가이드](../../../Guide/01. 인프라와 플랫폼/05. ArgoCD 운영 흐름 가이드/index.md)를 본다. 여기서는 손에 잡히는 사용법이다.

## 접속
- UI: `argocd.do4ai.com` (또는 NodePort 30080). 기본 계정 `admin` (시크릿은 Infisical, 평문 로테이션은 진행 예정).
- CLI/kubectl: 클러스터 접속은 [k3s 클러스터 접속과 GitOps 배포 점검](../k3s 클러스터 접속과 GitOps 배포 점검/index.md).

## 자주 쓰는 확인
```bash
sudo kubectl get applications -A          # 전체 앱 상태
sudo kubectl describe application <앱> -n argocd
```
- 상태 읽는 법: `Synced/OutOfSync`(Git과 일치 여부), `Healthy/Degraded/Progressing`(실제 워크로드 건강).

## 동기화(Sync)
- prod의 `do4i`·`passv`는 **자동 동기화 off**(수동 sync로 시점 통제). dev는 자동 동기화 on.
- 수동 sync: UI에서 앱 선택 → `Sync`. CLI는 `argocd app sync <앱>`.

## 롤백
1. 무엇을 되돌릴지 결정([장애 대응 의사결정 가이드](../../../Guide/03. 관측과 SRE/10. 장애 대응 의사결정 가이드/index.md)).
2. **방법 A(GitOps 정석)**: gitops 레포에서 이미지 태그/digest를 직전 정상으로 되돌려 커밋 → sync.
3. **방법 B(임시)**: ArgoCD UI에서 `History and Rollback` → 이전 리비전 선택.
- 정본은 Git이므로, B로 임시 롤백했어도 Git을 맞춰두지 않으면 self-heal/다음 sync에서 되돌아온다.

## 자주 만나는 상태
- `OutOfSync`만 있고 Healthy: 변경이 아직 반영 안 됨(즉시 장애 아님일 수 있음).
- `Degraded`: 워크로드 비정상 → 해당 namespace 파드/로그 확인.
- `ImagePullBackOff`: 이미지 태그·레지스트리 접근 → [Harbor 사용법](../Harbor 사용법/index.md).

## 함께 보기
- 서비스별 배포 이상 대응은 각 서비스 가이드의 `3. 운영 절차`와 [서비스 공통 1차 대응 절차](../../../Guide/02. 서비스 운영/서비스 공통 1차 대응 절차/index.md).
