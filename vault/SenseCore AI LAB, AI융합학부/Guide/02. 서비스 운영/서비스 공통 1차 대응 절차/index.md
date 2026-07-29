---
title: "서비스 공통 1차 대응 절차"
---
# 서비스 공통 1차 대응 절차

모든 서비스(do4i·passv·palcar·papersens·wiki)에 공통으로 적용하는 배포/장애 1차 대응 흐름이다. 서비스별 상세는 각 서비스 가이드의 `3. 운영 절차`에서 본다.

## 준비물

- 장애가 난 서비스명 / 대상 namespace
- 최근 배포 시각 또는 최근 변경 커밋
- 확인 가능한 health endpoint 또는 대표 URL

## 절차

### 1. 서비스 범위를 먼저 고정한다
1. 장애가 하나인지 여러 서비스인지 구분한다. 2. namespace를 고정한다. 3. 최근 배포 여부를 확인한다.

### 2. ArgoCD 상태를 본다
```bash
sudo kubectl get applications -A
```
- 대상 `Application`이 보이는가 / `OutOfSync` / `Degraded` / sync 후 수렴이 멈췄는가.

### 3. namespace live 상태를 본다
```bash
sudo kubectl get deploy,sts,svc,ing -n <namespace>
sudo kubectl get pods -n <namespace>
```
- deployment/statefulset 존재, available replica 부족, `CrashLoopBackOff`/`ImagePullBackOff`/`Pending`, ingress·service 단절 여부.

### 4. 앱 로그를 확인한다
```bash
sudo kubectl logs deploy/<deploy-name> -n <namespace> --tail=100
```
- 환경변수·secret 누락 / DB 연결 실패 / 외부 API 인증 실패 / migration·startup 실패.

### 5. 변경 유형별로 원인을 좁힌다
- `ImagePullBackOff`: 이미지 태그·registry 접근 / `CrashLoopBackOff`: 앱 시작 설정·secret·코드 / ingress 이상: 도메인·path·backend / `OutOfSync`만: 즉시 장애 여부 구분.

## 롤백 또는 중단 기준
- 기동 자체가 안 됨 / 대표 기능 무응답 / 새 변경이 원인 명확 → 롤백 우선.
- 단, 외부 의존성 원인이거나 동시 긴급 변경으로 기준이 불분명하면 먼저 기준 커밋·원인 범위를 확정.

판단 기준은 [장애 대응 의사결정 가이드](../../03. 관측과 SRE/10. 장애 대응 의사결정 가이드/index.md) 참고. 도구 사용법은 `Manual`.

## 작업 후 기록
- 대상 서비스/namespace, 장애 시각, `Application` 상태, pod 상태·핵심 로그, 최종 조치(관찰/조사/롤백).

---

> **온보딩 트랙 — 2부 서비스 운영**
> 이전: [02. 서비스 운영 (서비스 카탈로그)](../index.md) · 다음: [do4i 서비스 가이드](../do4i 서비스 가이드/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../../시작하기/index.md)
