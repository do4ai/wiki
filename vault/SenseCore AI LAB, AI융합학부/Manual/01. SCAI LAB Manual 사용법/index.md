---
title: "01. SCAI LAB Manual 사용법"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/manual/330e313f58b98098b619f0e3ef2d0fa0__Manual/children/330e313f58b98111b39ee4127f3a5fb3__01. SCAI LAB Manual 사용법
notion_id: 330e313f58b98111b39ee4127f3a5fb3
notion_url: https://www.notion.so/330e313f58b98111b39ee4127f3a5fb3
parent_notion_id: 330e313f58b98098b619f0e3ef2d0fa0
---
# 01. SCAI LAB Manual 사용법

`Manual`은 운영에 쓰는 **솔루션(도구)을 어떻게 쓰는가**를 도구 단위로 정리한 문서 모음이다(ArgoCD·kubectl/k3s·Grafana·Kibana·Tempo·Infisical·Harbor·Alerta 등).

이 페이지 아래 문서는 준비물, 작업 순서, 검증 방법, 실패 시 되돌리는 방법까지 포함하는 것을 기본 원칙으로 한다.

서비스별 아키텍처와 그 서비스의 운영 절차는 `Guide`의 `02. 서비스 운영`에서 서비스 폴더로 본다(Manual = 도구, Guide = 서비스).

## 넘버링 규칙 (Guide·Manual 공통)

- **1부터 빈칸 없이 연속**으로 번호를 매긴다.
- **두 자리 zero-pad**(`01`, `02`, … `10`, `11`)를 쓴다. 한 자리(`1`,`2`,…,`10`)로 두면 WikiJS 트리가 문자열 정렬이라 **`10`이 `2`보다 앞에** 와서 순서가 깨진다.
- 중간에 새 항목이 생기면 그 자리부터 **뒤 번호를 한 칸씩 민다**(예: 4번에 새로 넣으면 기존 04→05, 05→06 …).
- **같은 레벨은 모두 `NN. 제목/index.md`(폴더+인덱스) 형태로 통일**한다. 폴더와 단일 파일(`NN. 제목.md`)을 같은 레벨에 섞으면 WikiJS가 폴더와 페이지를 따로 묶어 번호를 매겨도 순서가 어긋날 수 있다.
- 번호를 바꿀 때는 **폴더명·frontmatter title·H1·문서 간 링크·Page Tree**를 함께 갱신한다.
- 한 레벨이 항상 9개 이하로 유지되는 깊은 하위 항목은 한 자리(`1`,`2`,`3`)도 허용한다(예: 서비스 가이드의 `1. 아키텍처와 배포` 등).
