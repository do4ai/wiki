---
title: "2. 모니터링·알람·SRE"
---
# wiki — 모니터링·알람·SRE

## 모니터링·관측

- 프로브: liveness/readiness + **startup 프로브(신규)** `/healthz:3000`.
- 합성 모니터링: blackbox 프로브가 `wiki.do4ai.com/healthz` 점검.
- 로그/리소스는 플랫폼 공통 스택에서 `atlas` 네임스페이스로 확인.

## 장애 알람

- 런타임 공통 규칙(CrashLoop/OOM/throttle) + 합성 프로브(PlatformEndpointDown: `wiki.do4ai.com`) 대상.
- `Recreate` 전략이라 **배포 중 짧은 다운이 정상** — 알림 노이즈 판단 기준으로 둔다.

## SRE·SLO

- **가용성**: 단일 인스턴스 + SQLite라 SLO는 보수적으로 본다(`TODO 확정 필요`). 내부 문서 도구라 사용자 영향도는 외부 서비스보다 낮음.
- **데이터**: 콘텐츠 정본은 GitHub `do4ai/wiki` 레포. WikiJS SQLite는 캐시/런타임이라 복구는 레포 재동기화로 대부분 해결.
- **개선 여지**: SQLite→외부 DB 전환 시 HA 가능(향후 `TODO`).

## 1차 확인 포인트

1. `wiki.do4ai.com/healthz` 응답(또는 blackbox 알림).
2. ArgoCD `atlas` Sync/Health, `atlas` 네임스페이스 파드(wikijs/content-sync).
3. 콘텐츠 미갱신 시 `content-sync` 로그(레포 pull 실패) 확인.

상세 절차: [3. 운영 절차](../3. 운영 절차/index.md).
