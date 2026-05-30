---
title: "do4i 서비스 가이드"
---
# do4i 서비스 가이드

이 문서는 에이전트 플랫폼 `do4i`를 서비스 관점에서 설명한다. 모든 서비스 가이드는 같은 7개 절 순서를 따른다.

## 1. 서비스 개요

- **무엇인가**: AI 에이전트(assistant)를 만들고, 대화하고, 아바타로 실시간 응대하게 하는 플랫폼.
- **누구를 위한 것인가**: 에이전트를 만드는 제작자와 사용하는 사용자(`agents.do4i.com`), 운영자(`admin.do4i.com`).
- **회사·브랜드**: do4i(원본 본체). `passv`와 같은 코드에서 출발했지만 지금은 별개 회사·브랜드로 운영된다. 자세한 관계는 [60. 서비스 운영](../index.md) 카탈로그 참고.

## 2. 아키텍처 구조

```
사용자 ─ agents.do4i.com /api ─┐
운영자 ─ admin.do4i.com  /api ─┤
                               ▼
                      ingress-nginx
                               ▼
                     api (FastAPI, :8000)  ── MySQL (StatefulSet)
                        │                  └─ 런타임 스토리지 PVC (Chroma/업로드)
                        └─ avatar-livekit-worker (LiveKit + Simli, HPA)
```

- **API**: Python 3.12 FastAPI 모놀리스. 컨테이너 포트 8000, 헬스 `/api/health`.
- **DB**: MySQL 8.0 StatefulSet(`mysql`), DB명 `do4i`.
- **아바타 워커**: `avatar-livekit-worker` — LiveKit 실시간 영상 + Simli 렌더링. 메모리 기준 HPA(10~100).
- **상태 저장**: `api-storage` PVC(`/app/runtime/storage`) — Chroma 벡터 DB, 업로드 파일.
- **외부 의존성**: OpenAI(LLM), LiveKit/Simli(아바타), Google OAuth.

## 3. 배포 구조

- **네임스페이스**: `do4i` (prod·dev 클러스터 공통 이름).
- **GitOps 경로**: `gitops/k8s/apps/do4i` (base + overlays/prod·dev), ArgoCD Application `do4i`.
- **이미지**: `harbor.do4i.com/do4ai/do4i-api` (overlay에서 태그+digest 핀).
- **시크릿**: Infisical `do4ai` 프로젝트 `/apps/api`, `/apps/mysql` → `InfisicalSecret`로 주입.
- **prod 규모**: API replicas 2(HA, pod anti-affinity) + HPA(min 2 / max 6, CPU 70%·Mem 80%), PDB minAvailable 1.
- **부트스트랩**: `api-bootstrap` Job이 alembic 마이그레이션 수행(ArgoCD Sync hook).
- **도메인**: `agents.do4i.com`, `admin.do4i.com` (CloudFront `/api*` → ingress).

## 4. 모니터링·관측

- **대시보드**: Grafana `do4i-api-operations`(가용 replica·재시작·5xx·CPU·메모리), `platform-api-apm`(요청율·에러율·p95).
- **로그**: Filebeat → Elasticsearch → Kibana(`kibana.do4ai.com`). 에러/예외 버스트는 ElastAlert로 감지.
- **트레이스**: OTel → Tempo(`do4i-api` 스팬).
- **보는 순서**: 메트릭(범위) → 로그(원인) → 트레이스(병목). [Observability 운영 가이드](../../50. 인프라와 플랫폼/Observability 운영 가이드/index.md) 참고.

## 5. 장애 알람

do4i에 직접 걸리는 알림(모두 Alertmanager→Alerta→Discord):

| 알림 | 조건 | 심각도 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable | `do4i/api` 가용 replica < desired (5m) | critical |
| PlatformAppIngress5xxRatioHigh | `api-ingress` 5xx 비율 > 5% (5m) | major |
| PlatformAppServerErrorRateHigh | `do4i-api` 서버 에러율 > 10% (10m) | major |
| PlatformAppServerLatencyP95High | `do4i-api` p95 > 1500ms (10m) | warning |
| PlatformPodCrashLooping / OOMKilled / CPUThrottling | 워크로드 런타임 이상 | critical~warning |
| PlatformMySQLNotReady | `do4i/mysql` Ready 0 (5m) | critical |
| PlatformAvailabilitySLO*Burn | 가용성 에러버짓 소진 | critical/warning |

## 6. SRE·SLO

- **가용성 SLO**: `TODO(확정 필요)` 제안값 99.9%(월 에러버짓 0.1%). 5xx 비율로 측정, 멀티윈도 번레이트로 감시.
- **지연 SLO**: `TODO(확정 필요)` 제안값 p95 < 1500ms.
- **확장**: API는 HPA로 트래픽 대응, 아바타 워커는 세션 부하에 따라 10~100 스케일.
- **에러버짓 운영**: fast burn(1h&5m) 시 즉시 대응, slow burn(6h&30m) 시 원인 조사. 자세한 기준은 [SLO·SLI와 에러 버짓 가이드](../../90. 장애 대응과 운영 판단/SLO·SLI와 에러 버짓 가이드/index.md).

## 7. 1차 확인 포인트

장애 의심 시 순서:

1. ArgoCD에서 `do4i` Application Sync/Health 확인.
2. `do4i` 네임스페이스 파드 상태(api/mysql/avatar-worker).
3. Grafana `do4i-api-operations` → 5xx·재시작·리소스.
4. Kibana에서 `do4i` 로그 에러.

상세 절차는 [Manual/70 do4i 배포 이상 대응 절차](../../../Manual/70. 서비스별 운영 작업/do4i 배포 이상 대응 절차/index.md).
