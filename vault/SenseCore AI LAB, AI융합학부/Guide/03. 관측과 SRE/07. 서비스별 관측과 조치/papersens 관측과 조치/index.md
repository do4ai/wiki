---
title: "papersens 관측과 조치"
---
# papersens 관측과 조치

논문 검사 솔루션 papersens(namespace `papersens`). **메모리가 무겁고 영속 DB가 없다(인메모리)** 는 점을 전제로 본다.

## 접속
- **메트릭**: `grafana.do4ai.com` → `papersens-operations`(가용 replica·재시작·5xx·리소스).
- **로그**: Grafana Explore → `{namespace="papersens"}` (LLM/OpenRouter 오류).
- **트레이스**: Grafana Explore → Tempo, service `papersens-api`.
- **배포 상태**: `argocd.do4ai.com` → `papersens`.

## 볼 수 있는 메트릭·로그
- ingress `papersens-ingress`(+ `*.ps.do4ai.com`) 5xx, **메모리 사용(OOM 위험)**·재시작, 단일 deployment 수렴.
- 로그: startup/secret 누락/OpenRouter·Ollama 외부 호출 실패/host 라우팅.

## 이 서비스에 걸린 알림 → 조치
| 알림 | 의미 | 조치 |
| --- | --- | --- |
| PlatformContainerOOMKilled(papersens) | 메모리 초과 종료 | 메모리 limit 상향과 요청 크기 점검. **무거운 워크로드라 1순위 주의** |
| PlatformAppIngress5xxRatioHigh(papersens-ingress) | 5xx | 대표·wildcard host 분리 확인 → 앱 로그 |
| PlatformAppServerErrorRateHigh / LatencyP95High | 에러율·지연 | LLM 외부 호출 병목 여부(스케일아웃 효과 제한적) |
| PlatformPodCrashLooping / CPUThrottling | 워크로드 이상 | 로그·리소스 |

> ⚠️ 인메모리라 **파드 재시작 = 업로드/분석 결과 소실**. 재기동 전 영향 인지.

## 더 보기
- 서비스 구조: [papersens 서비스 가이드](../../../02. 서비스 운영/papersens 서비스 가이드/index.md)
- 손절차: [papersens 운영 절차](../../../02. 서비스 운영/papersens 서비스 가이드/3. 운영 절차/index.md)

---

> **온보딩 트랙 3부. 관측과 SRE**
> 이전: [palcar 관측과 조치](../palcar 관측과 조치/index.md) · 다음: [wiki 관측과 조치](../wiki 관측과 조치/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../../시작하기/index.md)
