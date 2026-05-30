---
title: "palcar 서비스 가이드"
---
# palcar 서비스 가이드

이 문서는 자동차 경매 워크플로 서비스 `palcar`를 서비스 관점에서 설명한다. 모든 서비스 가이드는 같은 7개 절 순서를 따른다.

## 1. 서비스 개요

- **무엇인가**: 자동차 경매에서 딜러·셀러의 업무 흐름을 관리하는 시스템(DDD 모놀리스).
- **누구를 위한 것인가**: 딜러·셀러(`palcar.do4ai.com`), 운영자(`admin.palcar.do4ai.com`).
- **회사·브랜드**: do4i 계열 서비스.

## 2. 아키텍처 구조

```
딜러/셀러 ─ palcar.do4ai.com /api ─┐
운영자   ─ admin.palcar...  /api ─┤
                                  ▼
                          ingress-nginx
                                  ▼
                          api (:8000) ── MySQL (StatefulSet)
```

- **API**: Deployment `api`(라벨 `app: palcar-api`), 포트 8000, 헬스 `/health`.
- **DB**: MySQL 8.0 StatefulSet.
- **이미지**: `harbor.do4i.com/do4ai/palcar-api`.

## 3. 배포 구조

- **네임스페이스**: `palcar` (prod·dev).
- **GitOps 경로**: `gitops/k8s/apps/palcar` (base + overlays/prod·dev), ArgoCD Application `palcar`.
- **시크릿**: Infisical `/apps/...` → `InfisicalSecret`(api/mysql/harbor).
- **prod 규모**: 신규 HPA(min 2 / max 6) + PDB minAvailable 1 적용.
- **도메인**: prod `palcar.do4ai.com`, `admin.palcar.do4ai.com` / dev `palcar.dev.do4ai.com` 등.

## 4. 모니터링·관측

- 플랫폼 공통 스택 사용. 메트릭/로그/트레이스에서 `palcar` 네임스페이스·`palcar-api` 서비스로 필터.
- 보는 순서: Grafana(5xx·리소스) → Kibana(로그) → Tempo(`palcar-api` 스팬).

## 5. 장애 알람

| 알림 | 조건 | 심각도 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable | `palcar/api` 가용 replica 부족 | critical |
| PlatformAppIngress5xxRatioHigh | `palcar` ingress 5xx > 5% | major |
| PlatformAppServerErrorRateHigh / LatencyP95High | `palcar-api` 에러율·지연 | major/warning |
| 런타임/용량/SLO 공통 규칙 | CrashLoop·OOM·throttle·MySQLNotReady·번레이트 | critical~warning |

## 6. SRE·SLO

- **가용성/지연 SLO**: `TODO(확정 필요)` 제안값 99.9% / p95 < 1500ms.
- **확장**: 기존 1 replica → HPA로 prod 최소 2 replica 확보(HA 개선).

## 7. 1차 확인 포인트

1. ArgoCD `palcar` Sync/Health.
2. `palcar` 네임스페이스 파드(api/mysql), `/health`, `/api` 경로.
3. Grafana 5xx·리소스 → Kibana 로그.

상세 절차는 [Manual/70 palcar 배포 이상 대응 절차](../../../Manual/70. 서비스별 운영 작업/palcar 배포 이상 대응 절차/index.md).
