---
title: "13. 디스코드 알림 채널과 웹훅 구성"
---
# 13. 디스코드 알림 채널과 웹훅 구성

디스코드로 무엇이, 어디서, 어떤 웹훅을 타고 오는지를 한곳에 모은 문서다. "알림이 왜 안 오지", "이 메시지는 누가 보낸 거지", "dev 알림은 어디로 가지"를 여기서 판단한다. 파이프라인 구조 자체는 [03. 알림 - Alertmanager와 Alerta](../03. 알림 - Alertmanager와 Alerta/index.md), 심각도와 에스컬레이션 기준은 [09. 알림에서 인시던트, 에스컬레이션까지](../09. 알림에서 인시던트, 에스컬레이션까지/index.md)에 있다.

> **웹훅 URL 자체는 이 문서에도, 레포 어디에도 적지 않는다.** URL을 아는 사람은 누구나 그 채널에 글을 쓸 수 있으므로 값은 Infisical에만 두고, 문서와 매니페스트에는 **키 이름만** 적는다.

## 웹훅 네 개와 각자의 역할

디스코드로 나가는 경로는 네 개다. 모두 Infisical `/platform/incident-alerting` 한곳에 키로 보관한다.

| 키 이름 | 무엇이 오나 | 보내는 주체 | 빈도 |
| --- | --- | --- | --- |
| `DISCORD_WEBHOOK_URL` | 운영 장애·복구 알림 | Alerta Discord 플러그인 | 사건 발생 시 |
| `DISCORD_WEBHOOK_URL_DEV` | 개발 환경 장애 알림 | Alerta Discord 플러그인 | 사건 발생 시 |
| `DISCORD_METRICS_WEBHOOK` | 시간별 메트릭 리포트 | `metrics-digest` CronJob | 매시 정각 |
| `DISCORD_DEPLOY_WEBHOOK` | 배포 완료 알림 | ArgoCD Notifications | 배포 성공 시 |

```
Prometheus 규칙 ─┐
Loki ruler       ─┼─ Alertmanager ─┐
ArgoCD(헬스·동기화 실패) ───────────┼─ Alerta ─ Discord 플러그인 ─┬─ DISCORD_WEBHOOK_URL      (운영)
앱 직접 전송(챗봇·로그인) ──────────┘                             └─ DISCORD_WEBHOOK_URL_DEV  (개발)

ArgoCD(배포 성공) ──────────────────────────────────────────────── DISCORD_DEPLOY_WEBHOOK
metrics-digest CronJob(매시 정각) ─────────────────────────────── DISCORD_METRICS_WEBHOOK
```

장애 알림과 배포 알림이 다른 웹훅을 쓰는 이유는 성격이 다르기 때문이다. 배포 성공은 하루에도 여러 번 나오는 정상 신호이고, 장애 알림은 사람이 즉시 봐야 하는 신호다. 같은 채널에 섞으면 장애 알림이 배포 로그에 묻힌다.

## 운영과 개발을 가르는 기준

Alerta의 Discord 플러그인은 **알림에 붙은 `environment` 라벨**만 보고 목적지를 정한다. 값이 `dev`로 시작하면 개발 웹훅, 아니면 운영 웹훅으로 보낸다.

| 알림 출처 | `environment` 값이 붙는 곳 |
| --- | --- |
| Prometheus·Loki 규칙 | 각 클러스터 `prometheusSpec.externalLabels` (운영 `Production`, 개발 `Development`) |
| ArgoCD Notifications | 알림 템플릿에 직접 기술. dev는 오버레이 패치로 `Development` 로 덮어쓴다 |
| 앱 직접 전송 | 앱 설정 `ALERTA_ENVIRONMENT` |

⚠️ **`DISCORD_WEBHOOK_URL_DEV`가 비어 있으면 개발 알림이 운영 채널로 간다.** 플러그인은 dev 웹훅이 없을 때 운영 웹훅으로 폴백한다. 알림을 잃지 않으려는 의도적인 동작이지만, 채널을 나누려면 이 키를 반드시 채워야 한다. 현재 값 설정 여부는 `TODO(확정 필요)`.

## 디스코드에 찍히는 메시지 형태

### 장애·복구 알림 (Alerta)

제목은 `[장애] <이벤트명>` 또는 `[복구] <이벤트명>`이고, 조치가 있으면 `[조치:확인]`·`[조치:종료]`로 온다. 본문 필드는 **자원 · 심각도 · 환경 · 서비스 · 출처 · 상태 · 태그** 일곱 개이며 모두 한글 이름이다.

심각도는 한글과 영문을 함께 적고 색으로도 구분한다.

| 표기 | 원문 | 색 |
| --- | --- | --- |
| 심각 | `critical` | 빨강 |
| 주요 | `major` | 진한 주황 |
| 경고 | `warning` | 노랑 |
| 보조 | `minor` | 주황 |
| 정상 | `ok` / `normal` | 초록 |

Alertmanager는 `severity`가 `critical·major·warning·minor` 중 하나인 알림만 Alerta로 넘긴다. 같은 알림은 **2시간마다 한 번만** 다시 보낸다(`repeatInterval`). 알림을 묶는 단위는 `alertname`·`service`·`instance`다.

### 시간별 메트릭 리포트 (`metrics-digest`)

매시 정각(Asia/Seoul)에 Prometheus를 조회해 지난 한 시간을 요약한다. 대상 서비스는 `do4i`·`palcar`·`papersens`·`passv` 네 개로 **고정**이라, 트래픽이 없어도 항목이 빠지지 않는다.

서비스마다 다음을 적고 앞에 신호등을 붙인다.

- 요청 수와 5xx 건수, 그리고 5xx 비율을 적는다.
- 🟢 는 5xx가 없음, 🟡 는 5xx가 있으나 비율 5% 미만, 🔴 는 5% 이상을 뜻한다.
- 파드가 재시작했으면 횟수를 덧붙인다.
- 가용 레플리카가 모자라면 결손 개수를 덧붙인다.

마지막에 외부 엔드포인트 합성 프로브 결과를 붙인다. 성공률이 99.5% 미만인 대상만 나열하고, 모두 정상이면 정상이라고 한 줄로 적는다.

인그레스 트래픽 데이터가 아예 없으면 "메트릭 수집 상태를 확인해야 합니다"라는 문구가 대신 나온다. 이 문구가 보이면 서비스가 조용한 것이 아니라 **수집이 멈춘 것**을 의심한다.

### 배포 완료 알림 (ArgoCD)

동기화가 성공하고 헬스가 `Healthy`가 된 시점에 한 번 보낸다. 커밋 리비전 단위로 한 번만 나가므로 같은 배포가 반복해서 알리지 않는다. 필드는 네임스페이스·프로젝트·헬스·리비전(앞 7자리)이다.

반대로 **헬스 저하와 동기화 실패는 디스코드로 직접 가지 않는다.** 이 둘은 Alerta로 보내 인시던트로 쌓은 뒤, Alerta가 장애 웹훅으로 내보낸다. 배포 실패를 배포 채널이 아니라 장애 채널에서 보게 되는 이유다.

## 앱에서 직접 보내는 장애 알림

인프라 지표로는 안 잡히는 실패가 있다. 챗봇 응답 생성이 실패하거나 로그인이 연속으로 깨지는 경우인데, 파드는 살아 있고 HTTP 200이 나갈 수도 있어서 Prometheus 규칙만으로는 잡히지 않는다. 그래서 앱이 Alerta REST API로 직접 보낸다.

| 보내는 곳 | 이벤트 | 자원 | 심각도 |
| --- | --- | --- | --- |
| `ctx-chatbot-core` | `ChatGenerationFailed` | `<서비스>/chat` | 주요(major) |
| `ctx-identity` | 로그인 실패 급증·인증 오류 | `<서비스>/auth` | 주요(major) |

두 모듈 모두 **노이즈를 억제한다.** 정해진 시간창 안에서 실패가 임계 횟수를 넘어야 보내고, 한 번 보낸 뒤에는 최소 간격이 지나야 다시 보낸다. 일시적인 한 번의 실패로 채널이 울리지 않게 하려는 장치다. 챗봇 기본값은 5분 안에 3회다.

⚠️ **이 경로는 `ALERTA_API_KEY`가 있어야 동작한다.** 키가 없으면 모듈이 스스로 비활성화되고 조용히 아무것도 보내지 않는다. 앱 레벨 알림을 켜려면 Alerta에서 쓰기 키를 발급해 Infisical `/apps/api`에 `ALERTA_API_KEY`로 넣어야 한다. 현재 발급 여부는 `TODO(확정 필요)`.

## 시크릿 보관과 주입 경로

네 웹훅 값은 모두 Infisical **`do4ai` 프로젝트 / `prod` 환경 / `/platform/incident-alerting`** 경로에 있다.

| 쓰는 곳 | 쿠버네티스 시크릿 | 네임스페이스 |
| --- | --- | --- |
| Alerta, `metrics-digest` | `alerta-secrets` | `monitoring` |
| ArgoCD Notifications | `argocd-notifications-secret` | `argocd` |

Infisical Operator가 이 경로를 통째로 읽어 시크릿으로 만든다. 값을 바꾸면 **Infisical에서만 바꾸면 되고 매니페스트는 손대지 않는다.**

주의할 점이 하나 있다. **개발 클러스터도 `prod` 환경 스코프를 읽는다.** dev 오버레이는 Infisical 접속 주소만 바꾸고 환경 슬러그는 그대로 두기 때문에, 양쪽 클러스터가 같은 키 묶음을 본다. `DISCORD_WEBHOOK_URL_DEV`를 이 경로에 넣으면 개발 클러스터에서도 그대로 읽힌다.

## 알림이 안 올 때 보는 순서

1. Alerta(`alerta.do4ai.com`)에 인시던트가 쌓였는지 본다. 쌓여 있는데 디스코드만 조용하면 **웹훅 문제**이고, 아예 없으면 **알림이 생성되지 않은 것**이다.
2. 웹훅 문제로 좁혀지면 Alerta 파드 로그에서 `alerta.plugins.discord` 경고를 찾는다. `DISCORD_WEBHOOK_URL not configured`가 보이면 시크릿이 주입되지 않은 것이다.
3. 인시던트가 아예 없으면 Alertmanager가 Alerta로 넘기는 구간을 본다. 알림 자체가 없으면 Prometheus 규칙과 대상 메트릭이 있는지 확인한다.
4. 개발 알림만 안 보이면 채널을 착각한 경우가 많다. `DISCORD_WEBHOOK_URL_DEV`가 비어 있으면 운영 채널에 섞여 들어간다.
5. 매시 리포트만 안 오면 `metrics-digest` CronJob의 마지막 실행 결과를 본다. `DISCORD_METRICS_WEBHOOK 미설정` 로그가 있으면 키가 비어 있는 것이다.

절차 상세는 [Manual 06. 모니터링-로그 작업](../../../Manual/06. 모니터링-로그 작업/index.md)에 있다.

## 남은 과제

- ⚠️ `DISCORD_WEBHOOK_URL_DEV`를 채우기 전까지 개발 알림이 운영 채널로 섞인다.
- ⚠️ `ALERTA_API_KEY`가 없으면 챗봇·로그인 실패 알림이 전송되지 않는다. 실패해도 조용하므로 켜졌는지 주기적으로 확인한다.
- ⚠️ Alerta는 replica 1이다. Alerta가 내려가면 디스코드 알림이 전부 멈춘다.

이 문서 이전의 설계 배경은 [11. 운영 장애 Discord 리포트 솔루션 리서치](../11. 운영 장애 Discord 리포트 솔루션 리서치/index.md)와 [12. k3s 운영 장애 Discord 리포트 설계](../12. k3s 운영 장애 Discord 리포트 설계/index.md)에 있다. 두 문서는 2026-03-29 시점 기록이라 현행 구성과 다른 부분이 있고, 실제 구성은 이 문서를 따른다.

---

> **관련 문서**
> 파이프라인 구조: [03. 알림 - Alertmanager와 Alerta](../03. 알림 - Alertmanager와 Alerta/index.md) · 심각도와 에스컬레이션: [09. 알림에서 인시던트, 에스컬레이션까지](../09. 알림에서 인시던트, 에스컬레이션까지/index.md) · 섹션 목차: [03. 관측과 SRE](../index.md)
