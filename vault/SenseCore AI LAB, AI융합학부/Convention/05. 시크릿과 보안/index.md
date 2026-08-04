---
title: "05. 시크릿과 보안"
---
# 05. 시크릿과 보안

시크릿 취급 규칙이다. 개념·구조는 [Guide 01. 인프라와 플랫폼 / Infisical 시크릿 관리](../../Guide/01. 인프라와 플랫폼/08. Infisical 시크릿 관리 가이드/index.md).

## 원칙

- **시크릿 정본은 Infisical(중앙)** 이다. 클러스터에는 Infisical Operator가 `InfisicalSecret` CRD로 K8s Secret을 주입한다.
- **평문 시크릿 금지.** 매니페스트·Helm values·코드에 비밀번호·토큰·키를 하드코딩하지 않는다. 발견 시 Infisical로 이관하고 값을 로테이션한다.
- **문서·위키에 비밀번호/토큰을 적지 않는다.** 자격증명은 담당자에게 발급받는다.

## Infisical 경로

- 앱 시크릿: `/apps/<서비스>-*` (예: `/apps/api`, `/apps/mysql`, `/apps/passv-api`).
- 플랫폼 공용: `/platform/*` (예: `/platform/harbor-credentials`, `/platform/incident-alerting`).
- 환경: `prod`, `dev`.

## 변경

- 시크릿 반영·권한 변경 절차는 [Manual / Infisical 시크릿 반영과 권한 변경 절차](../../Manual/07. 시크릿-권한 작업/Infisical 시크릿 반영과 권한 변경 절차/index.md).

---

> **온보딩 트랙 4부. 운영 변경과 컨벤션**
> 이전: [네이밍과 환경](../04. 네이밍과 환경/index.md) · 다음: [관측, 알림, SRE](../06. 관측, 알림, SRE/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../시작하기/index.md)
