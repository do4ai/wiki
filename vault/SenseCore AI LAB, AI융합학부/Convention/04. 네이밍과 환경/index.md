---
title: "04. 네이밍과 환경"
---
# 04. 네이밍과 환경

클러스터·네임스페이스·도메인·레지스트리 이름 규칙이다.

## 클러스터

- `do4ai-prod`(운영), `do4ai-dev`(개발) 두 개를 쓴다.

## 네임스페이스

- **환경 접미사 없이 서비스명만** 쓴다: `do4i`, `passv`, `palcar`, `papersens`, `atlas`.
- 같은 서비스는 prod·dev 클러스터에서 같은 네임스페이스 이름을 쓴다(환경은 클러스터로 구분).
- `atlas`는 코드/배포상 이름이고 서비스 명칭은 `wiki`다.

## 도메인

- 서비스·인프라 도메인은 `*.do4ai.com`을 기본으로 한다.
- **레지스트리만 `harbor.do4i.com`** 이다(`.do4i`, `do4ai` 아님, 혼동 주의).
- passv는 별도 회사·브랜드라 `passv.co.kr`·`kon.ai.kr` 계열을 쓴다.

## 레지스트리

- `do4i`·`palcar`: **Harbor**(`harbor.do4i.com/do4ai/*`).
- `papersens`·`passv`(prod 일부): **AWS ECR**.
- 이미지 경로·태그 규칙은 [03. GitOps와 배포](../03. GitOps와 배포/index.md).

---

> **온보딩 트랙 4부. 운영 변경과 컨벤션**
> 이전: [GitOps와 배포](../03. GitOps와 배포/index.md) · 다음: [시크릿과 보안](../05. 시크릿과 보안/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../시작하기/index.md)
