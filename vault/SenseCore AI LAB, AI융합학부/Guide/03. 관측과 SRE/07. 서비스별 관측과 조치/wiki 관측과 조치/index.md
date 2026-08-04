---
title: "wiki 관측과 조치"
---
# wiki 관측과 조치

사내 위키 런타임 wiki(코드상 `atlas`, namespace `atlas`, prod 전용).

## 접속
- **합성 모니터링**: blackbox 프로브가 `wiki.do4ai.com/healthz` 점검 → `PlatformEndpointDown` 알림. 직접 확인 `curl -I https://wiki.do4ai.com/healthz`.
- **로그**: Grafana Explore → `{namespace="atlas"}` (특히 `content-sync` 컨테이너).
- **배포 상태**: `argocd.do4ai.com` → `atlas`.

## 볼 수 있는 메트릭·로그
- wikijs(`/healthz`) 가용성, 파드 재시작. `content-sync` 사이드카가 `do4ai/wiki` 레포를 60초마다 pull → 반영 로그.

## 이 서비스에 걸린 알림 → 조치
| 알림/증상 | 의미 | 조치 |
| --- | --- | --- |
| PlatformEndpointDown(wiki.do4ai.com) | 위키 접속 불가 | 파드/`/healthz`/ingress 확인. `Recreate` 전략이라 배포 중 짧은 다운은 정상 |
| 문서 미갱신 | content-sync 실패 | `content-sync` 로그(레포 pull/토큰) 확인. 정본은 레포라 재동기화로 복구한다 |
| CrashLoop/OOM | 워크로드 이상 | 로그·리소스 확인 |

> 데이터 정본은 GitHub `do4ai/wiki` 레포. SQLite는 런타임/캐시라 복구는 레포 재동기화 우선.

## 더 보기
- 서비스 구조: [wiki 서비스 가이드](../../../02. 서비스 운영/wiki 서비스 가이드/index.md)
- 손절차: [wiki 운영 절차](../../../02. 서비스 운영/wiki 서비스 가이드/3. 운영 절차/index.md)

---

> **온보딩 트랙 3부. 관측과 SRE**
> 이전: [papersens 관측과 조치](../papersens 관측과 조치/index.md) · 다음: [SLO·SLI와 에러 버짓 가이드](../../08. SLO·SLI와 에러 버짓 가이드/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../../시작하기/index.md)
