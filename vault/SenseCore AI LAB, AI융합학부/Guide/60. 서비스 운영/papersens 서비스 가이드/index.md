---
title: "papersens 서비스 가이드"
---
# papersens 서비스 가이드

이 문서는 논문 검사 솔루션 `papersens`를 서비스 관점에서 설명한다. 모든 서비스 가이드는 같은 7개 절 순서를 따른다.

## 1. 서비스 개요

- **무엇인가**: 논문 문서를 분석·검사하는 LLM/VLM 기반 솔루션(텍스트·도표 분석).
- **누구를 위한 것인가**: 논문 검사 사용자(`papersens.do4ai.com`, 테넌트별 `*.ps.do4ai.com`).
- **회사·브랜드**: do4i 계열 서비스.

## 2. 아키텍처 구조

```
사용자 ─ papersens.do4ai.com, *.ps.do4ai.com ─ ingress-nginx ─ papersens (:8082)
                                                                  │
                                              OpenRouter(gpt-4o-mini) / Ollama (LLM·VLM)
```

- **앱**: Deployment `papersens`(라벨 `app: papersens`), 포트 8082, 헬스 `/health`. 리소스 req 1Gi / limit 4Gi(무거움).
- **LLM 백엔드**: OpenRouter(`openai/gpt-4o-mini`) 기본, Ollama 폴백(`PAPERSENS_OPENROUTER_FALLBACK_TO_OLLAMA`).
- **이미지**: ECR `741323757384.dkr.ecr.ap-northeast-2.amazonaws.com/do4ai/papersens`.

## 3. 배포 구조

- **네임스페이스**: `papersens` (prod·dev).
- **GitOps 경로**: `gitops/k8s/apps/papersens` (base + overlays/prod·dev), ArgoCD Application `papersens`.
- **시크릿**: Infisical `InfisicalSecret`(api) + ECR registry secret.
- **prod 규모**: 신규 HPA(min 2 / max 4) + PDB minAvailable 1. `TODO(확정 필요)`: 무거운 워크로드라 min 2는 노드 용량 의존 — 단일/저용량 노드면 min 1로 조정.
- **도메인**: `papersens.do4ai.com`, 와일드카드 `*.ps.do4ai.com`(테넌트).

## 4. 모니터링·관측

- 플랫폼 공통 스택 사용. Grafana `papersens-operations` 대시보드(가용 replica·재시작·5xx·리소스).
- LLM 외부 호출 실패는 로그(Kibana)·트레이스(Tempo `papersens-api`)에서 확인.

## 5. 장애 알람

| 알림 | 조건 | 심각도 |
| --- | --- | --- |
| PlatformAppDeploymentUnavailable | `papersens/papersens` 가용 replica 부족 | critical |
| PlatformAppIngress5xxRatioHigh | `papersens-ingress` 5xx > 5% | major |
| PlatformAppServerErrorRateHigh / LatencyP95High | `papersens-api` 에러율·지연 | major/warning |
| 런타임/용량/SLO 공통 규칙 | CrashLoop·OOM(메모리 주의)·throttle·번레이트 | critical~warning |

> papersens는 메모리 사용이 크므로 **OOMKilled·CPU throttling 알림**을 특히 주시한다.

## 6. SRE·SLO

- **가용성/지연 SLO**: `TODO(확정 필요)` 제안값 99.9% / p95는 LLM 호출 특성상 별도 기준 검토 필요(현 공통 1500ms는 과도할 수 있음).
- **확장**: HPA로 부하 대응하되, LLM 외부 호출이 병목이면 단순 스케일아웃 효과가 제한적임을 유의.

## 7. 1차 확인 포인트

1. ArgoCD `papersens` Sync/Health.
2. `papersens` 네임스페이스 파드, `/health`(:8082).
3. Grafana 리소스(메모리)·5xx → Kibana 로그(LLM/OpenRouter 오류).

상세 절차는 [Manual/70 papersens 배포 이상 대응 절차](../../../Manual/70. 서비스별 운영 작업/papersens 배포 이상 대응 절차/index.md).
