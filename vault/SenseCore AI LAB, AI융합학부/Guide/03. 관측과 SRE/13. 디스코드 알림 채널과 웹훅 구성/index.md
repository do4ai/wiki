---
title: "13. 디스코드 알림 채널과 웹훅 구성"
---
# 13. 디스코드 알림 채널과 웹훅 구성

디스코드로 무엇이, 어디서, 어떤 웹훅을 타고 오는지를 한곳에 모은 문서다. "알림이 왜 안 오지", "이 메시지는 누가 보낸 거지", "dev 알림은 어디로 가지"를 여기서 판단한다. 파이프라인 구조 자체는 [03. 알림 - Alertmanager와 Alerta](../03. 알림 - Alertmanager와 Alerta/index.md), 심각도와 에스컬레이션 기준은 [09. 알림에서 인시던트, 에스컬레이션까지](../09. 알림에서 인시던트, 에스컬레이션까지/index.md)에 있다.

> **웹훅 URL 자체는 이 문서에도, 레포 어디에도 적지 않는다.** URL을 아는 사람은 누구나 그 채널에 글을 쓸 수 있으므로 값은 Infisical에만 두고, 문서와 매니페스트에는 **키 이름만** 적는다.

## 웹훅 키 다섯 종, 실제로 살아 있는 채널 네 개

디스코드로 나가는 경로는 키 이름 기준으로 다섯 종이다. 그중 **실제로 값이 들어 있는 것은 네 개이고, 네 개는 서로 다른 채널을 가리킨다**(2026-08-03 운영 클러스터에서 값 해시 대조로 확인). 나머지 하나(`DISCORD_WEBHOOK_URL_DEV`)는 매니페스트가 참조만 하고 시크릿에는 존재하지 않는다. 인프라용 키는 Infisical `/platform/incident-alerting`에, 앱 직송용 키는 서비스별 앱 시크릿 경로에 둔다.

| 키 이름 | 무엇이 오나 | 보내는 주체 | 빈도 | 상태 |
| --- | --- | --- | --- | --- |
| `DISCORD_WEBHOOK_URL` | 운영 장애·복구 알림 | Alerta Discord 플러그인 | 사건 발생 시 | 설정됨 |
| `DISCORD_WEBHOOK_URL_DEV` | 개발 환경 장애 알림 | Alerta Discord 플러그인 | 사건 발생 시 | ⚠️ **키 자체가 없음** |
| `DISCORD_METRICS_WEBHOOK` | 시간별 메트릭 리포트 | `metrics-digest` CronJob | 매시 정각 | 설정됨 |
| `DISCORD_DEPLOY_WEBHOOK` | 배포 완료 알림 | ArgoCD Notifications | 배포 성공 시 | 설정됨 |
| `DISCORD_ALERT_WEBHOOK_URL` | 앱 런타임 오류 직송 | 앱(`platform_runtime`) | 오류 발생 시 | do4i·palcar만 설정됨 |

```
Prometheus 규칙 ─┐
Loki ruler       ─┼─ Alertmanager ─┐
ArgoCD(헬스·동기화 실패) ───────────┼─ Alerta ─ Discord 플러그인 ─┬─ DISCORD_WEBHOOK_URL      (운영)
                                                                  └─ DISCORD_WEBHOOK_URL_DEV  (개발, 현재 비어 운영으로 폴백)

ArgoCD(배포 성공) ──────────────────────────────────────────────── DISCORD_DEPLOY_WEBHOOK
metrics-digest CronJob(매시 정각) ─────────────────────────────── DISCORD_METRICS_WEBHOOK
앱 런타임 오류 ───────────────────────────────────────────────── DISCORD_ALERT_WEBHOOK_URL
```

경로를 나눈 이유는 신호의 성격이 다르기 때문이다. 배포 성공은 하루에도 여러 번 나오는 정상 신호이고, 장애 알림은 사람이 즉시 봐야 하는 신호다. 같은 채널에 섞으면 장애 알림이 배포 로그에 묻힌다. 앱 오류 직송은 Alerta가 죽어 있어도 도착해야 하므로 아예 파이프라인을 타지 않는다.

## 운영과 개발을 가르는 기준

Alerta의 Discord 플러그인은 **알림에 붙은 `environment` 라벨**만 보고 목적지를 정한다. 값이 `dev`로 시작하면 개발 웹훅, 아니면 운영 웹훅으로 보낸다.

| 알림 출처 | `environment` 값이 붙는 곳 |
| --- | --- |
| Prometheus·Loki 규칙 | 각 클러스터 `prometheusSpec.externalLabels` (운영 `Production`, 개발 `Development`) |
| ArgoCD Notifications | 알림 템플릿에 직접 기술. dev는 오버레이 패치로 `Development` 로 덮어쓴다 |
| 앱 직접 전송 | 앱 설정 `ALERTA_ENVIRONMENT` |

⚠️ **현재 `DISCORD_WEBHOOK_URL_DEV`가 비어 있어 개발 알림이 운영 채널로 간다.** 플러그인은 dev 웹훅이 없을 때 운영 웹훅으로 폴백한다. 알림을 잃지 않으려는 의도적인 동작이다. 채널을 나누려면 Infisical `/platform/incident-alerting`에 이 키를 추가하면 되고, 매니페스트는 손댈 필요가 없다.

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

**디스코드로는 처음 한 번만 나간다.** Alertmanager가 2시간마다 다시 보내더라도 Alerta는 그것을 중복으로 판정하고, Discord 플러그인은 중복 알림을 건너뛴다(`if alert.repeat: return`). 채널이 같은 문구로 도배되지 않는 대신, **오래 열려 있는 알림은 디스코드에서 보이지 않는다.** 예를 들어 `KubePodNotReady` 는 2026-07-12부터 열린 채로 중복 1,273회를 기록했지만 디스코드에는 최초 1회만 찍혔다. 지금 무엇이 열려 있는지는 반드시 Alerta 화면에서 확인한다. 상태가 `ack` 나 `closed` 로 바뀔 때는 다시 한 번 알림이 나간다.

### 시간별 메트릭 리포트 (`metrics-digest`)

매시 정각(Asia/Seoul)에 Prometheus를 조회해 지난 한 시간을 요약한다. 대상 서비스는 `do4i`·`palcar`·`papersens`·`passv` 네 개로 **고정**이라, 트래픽이 없어도 항목이 빠지지 않는다.

⚠️ **고정 목록이라는 점 때문에 생기는 착시가 있다.** `passv` 는 이 클러스터에서 돌지 않고(네임스페이스·인그레스 모두 없음) `papersens` 도 인그레스 요청 시계열이 잡히지 않는다. 두 서비스는 리포트에 늘 `요청 0건 · 5xx 0건 🟢` 로 찍히는데, 이는 **건강하다는 뜻이 아니라 이 클러스터에서 측정되지 않는다는 뜻**이다. 0건이 계속되는 항목은 정상이 아니라 측정 범위 밖임을 의심한다.

서비스마다 다음을 적고 앞에 신호등을 붙인다.

- 요청 수와 5xx 건수, 그리고 5xx 비율을 적는다.
- 🟢 는 5xx가 없음, 🟡 는 5xx가 있으나 비율 5% 미만, 🔴 는 5% 이상을 뜻한다.
- 파드가 재시작했으면 횟수를 덧붙인다.
- 가용 레플리카가 모자라면 결손 개수를 덧붙인다.

마지막에 외부 엔드포인트 합성 프로브 결과를 붙인다. 성공률이 99.5% 미만인 대상만 나열하고, 모두 정상이면 정상이라고 한 줄로 적는다.

✅ **이 항목은 2026-08-08 기준 신뢰할 수 있다.** 예전에는 합성 프로브가 수집되지 않는데도 리포트에 "🟢 전체 엔드포인트가 정상입니다"로 찍히는 거짓 정상 문제가 있었다. 지금은 리포트가 세 상태를 구분한다. 조회 실패는 "조회에 실패했습니다", 조회는 됐지만 시계열이 0건이면 "⚠️ 합성 프로브 시계열이 없습니다"로 경고하고, 시계열이 있을 때만 정상·비정상을 판정한다. 경위는 아래 [해소된 결함](#해소된-결함)에 적었다.

인그레스 트래픽 데이터가 아예 없으면 "메트릭 수집 상태를 확인해야 합니다"라는 문구가 대신 나온다. 이 문구가 보이면 서비스가 조용한 것이 아니라 **수집이 멈춘 것**을 의심한다.

### 배포 완료 알림 (ArgoCD)

동기화가 성공하고 헬스가 `Healthy`가 된 시점에 한 번 보낸다. 커밋 리비전 단위로 한 번만 나가므로 같은 배포가 반복해서 알리지 않는다. 필드는 네임스페이스·프로젝트·헬스·리비전(앞 7자리)이다.

반대로 **헬스 저하와 동기화 실패는 디스코드로 직접 가지 않는다.** 이 둘은 Alerta로 보내 인시던트로 쌓은 뒤, Alerta가 장애 웹훅으로 내보낸다. 배포 실패를 배포 채널이 아니라 장애 채널에서 보게 되는 이유다.

## 앱에서 직접 보내는 장애 알림

인프라 지표로는 안 잡히는 실패가 있다. 챗봇 응답 생성이 실패하거나 로그인이 깨지는 경우인데, 파드는 살아 있고 HTTP 200이 나갈 수도 있어서 Prometheus 규칙만으로는 잡히지 않는다.

**현재 동작하는 경로는 `platform_runtime` 의 디스코드 직송 하나다.** Alerta를 거치지 않고 앱이 `DISCORD_ALERT_WEBHOOK_URL` 로 바로 쏜다. Alerta가 죽어 있거나 키가 없어도 오류가 채널에 도착해야 한다는 판단에서 독립 경로로 만들었다.

이 노티파이어의 규칙은 다음과 같다.

- 전송 실패를 포함한 모든 예외를 안에서 삼켜 **본 기능을 절대 막지 않는다**.
- **첫 발생을 즉시 보낸다.** 임계로 묶지 않고, 같은 지문만 최소 간격(기본 60초) 동안 억제해 폭주를 막는다.
- 표준 라이브러리만 쓰고 전송은 스레드로 넘겨 이벤트 루프를 막지 않는다.
- `DISCORD_ALERT_WEBHOOK_URL` 이 없으면 조용히 아무것도 하지 않는다.

운영 클러스터 기준으로 이 시크릿은 **`do4i` 와 `palcar` 두 곳에만 있다.** `papersens` 와 `namanva` 에는 없어서, 두 서비스에서 발생하는 런타임 오류는 디스코드로 오지 않는다.

### Alerta 기반 앱 알림은 비활성 상태다

`ctx-chatbot-core` 와 `ctx-identity` 에도 Alerta REST API로 보내는 헬퍼가 있다(`ChatGenerationFailed`, 로그인 실패 급증). 다만 **이 경로는 운영에서 한 번도 발사된 적이 없다.**

| 이유 | 설명 |
| --- | --- |
| 키 부재 | 파드에 `ALERTA_API_KEY` 가 주입되지 않아 모듈이 스스로 비활성화된다 |
| 임계 조건 | 윈도 안에서 3회를 넘어야 보내므로 단발·2회 실패는 묶여서 사라진다 |

⚠️ 앱 네임스페이스 시크릿을 확인한 결과 `ALERTA_API_KEY` 는 어디에도 없다(2026-08-01 기준). 직송 경로가 이 자리를 대신하고 있으므로, 두 경로를 모두 켤 필요는 없다. **정본은 직송 경로이고, Alerta 헬퍼는 비활성으로 남아 있다**고 이해하면 된다.

## 시크릿 보관과 주입 경로

인프라 쪽 웹훅은 Infisical **`do4ai` 프로젝트 / `prod` 환경 / `/platform/incident-alerting`** 에, 앱 직송 웹훅은 서비스별 앱 시크릿 경로에 있다.

| 쓰는 곳 | 쿠버네티스 시크릿 | 네임스페이스 |
| --- | --- | --- |
| Alerta, `metrics-digest` | `alerta-secrets` | `monitoring` |
| ArgoCD Notifications | `argocd-notifications-secret` | `argocd` |
| 앱 런타임 직송 | `alert-webhook` | `do4i`, `palcar` |

`alerta-secrets` 와 `argocd-notifications-secret` 은 같은 Infisical 경로를 읽기 때문에 **키 구성이 완전히 같다**. 그래서 ArgoCD 쪽 시크릿에도 `DISCORD_METRICS_WEBHOOK` 과 `DISCORD_WEBHOOK_URL` 이 들어 있지만, ArgoCD가 실제로 쓰는 것은 `DISCORD_DEPLOY_WEBHOOK` 과 Alerta 접속용 키뿐이다. 나머지는 쓰이지 않는 잔여 키이므로 여기서 값을 찾지 않는다.

Infisical Operator가 이 경로를 통째로 읽어 시크릿으로 만든다. 값을 바꾸면 **Infisical에서만 바꾸면 되고 매니페스트는 손대지 않는다.**

주의할 점이 하나 있다. **개발 클러스터도 `prod` 환경 스코프를 읽는다.** dev 오버레이는 Infisical 접속 주소만 바꾸고 환경 슬러그는 그대로 두기 때문에, 양쪽 클러스터가 같은 키 묶음을 본다. `DISCORD_WEBHOOK_URL_DEV`를 이 경로에 넣으면 개발 클러스터에서도 그대로 읽힌다.

## 알림이 안 올 때 보는 순서

1. Alerta(`alerta.do4ai.com`)에 인시던트가 쌓였는지 본다. 아예 없으면 **알림이 생성되지 않은 것**이다.
2. 인시던트는 있는데 디스코드가 조용하다면 먼저 **중복 여부**를 본다. 중복 횟수가 올라가는 알림은 플러그인이 의도적으로 건너뛰므로 고장이 아니다. 중복이 아닌 새 알림인데도 조용할 때만 웹훅 문제로 좁힌다.
3. 웹훅 문제로 좁혀지면 Alerta 파드 로그에서 `alerta.plugins.discord` 경고를 찾는다. `DISCORD_WEBHOOK_URL not configured`가 보이면 시크릿이 주입되지 않은 것이다.
4. 인시던트가 아예 없으면 Alertmanager가 Alerta로 넘기는 구간을 본다. 알림 자체가 없으면 Prometheus 규칙과 대상 메트릭이 있는지 확인한다.
5. 개발 알림만 안 보이면 채널을 착각한 경우가 많다. `DISCORD_WEBHOOK_URL_DEV`가 없으면 운영 채널에 섞여 들어간다.
6. 매시 리포트만 안 오면 `metrics-digest` CronJob의 마지막 실행 결과를 본다. `DISCORD_METRICS_WEBHOOK 미설정` 로그가 있으면 키가 비어 있는 것이다.
7. 앱 오류 알림만 안 오면 그 서비스 네임스페이스에 `alert-webhook` 시크릿이 있는지 먼저 본다. 없으면 직송 경로가 통째로 꺼져 있다. 이 경로는 Alerta와 무관하므로 Alerta 상태를 봐도 소용이 없다.

절차 상세는 [Manual 06. 모니터링-로그 작업](../../../Manual/06. 모니터링-로그 작업/index.md)에 있다.

## 해소된 결함

### 합성 모니터링이 수집되지 않던 문제 (2026-08-08 해소)

예전에는 `Probe` 리소스가 정의되어 있고 blackbox-exporter도 정상 가동 중인데 **`probe_success` 시계열이 하나도 없었다.**

원인은 라벨 불일치였다. Prometheus의 `probeSelector` 는 `release: kube-prometheus-stack` 라벨을 요구하는데, `Probe` 리소스에는 `app.kubernetes.io/name: blackbox-exporter` 만 붙어 있었다. 선택되지 않으니 스크레이프 대상이 되지 않았다. `serviceMonitorSelector` 만 빈 셀렉터로 열려 있었던 것이 대조점이다.

**같은 원인이 프로브에만 있었던 것이 아니다.** `ruleSelector` 도 선언되지 않아 같은 기본값이 걸려 있었고, 그래서 플랫폼이 정의한 커스텀 알림 룰 네 종(배포 가용성·ingress 5xx, APM 에러율·p95, SLO 번레이트, CrashLoop·OOMKilled·PVC 압박)이 통째로 로드되지 않았다. 리소스는 생성되고 ArgoCD는 `Synced`·`Healthy`이며 에러 로그도 없는 **소리 없는 실패**였다.

조치는 커스텀 `PrometheusRule`·`Probe` 여섯 건에 `release: kube-prometheus-stack` 라벨을 붙이는 것이었다. `probeSelector` 를 비우는 방법도 있었지만, 그렇게 하면 Prometheus가 클러스터의 임의 룰까지 흡수하게 되므로 영향 범위가 작은 쪽을 택했다. 리포트는 빈 결과와 정상을 구분하도록 함께 고쳤다.

| 확인 항목 | 해소 전 | 해소 후 |
| --- | --- | --- |
| 로드된 룰 그룹 | 30개 (전부 차트 기본) | **41개** |
| `probe_success` 시계열 | 0개 | **8개** (공개 5 + 컴포저블 3, 전부 `1`) |
| 매시 리포트 프로브 항목 | 시계열 0건을 초록불로 보고 | 세 상태를 구분해 보고 |

합성 감시가 살아나자마자 실제로 죽어 있던 대상 하나를 잡아냈다. 다섯 번째 대상이던 `pc.do4ai.com` 이 연결 자체가 되지 않았고, 확인 결과 **은퇴한 별칭**이었다. 운영 클러스터의 공개 `443` 은 설계상 닫혀 있고 공개 TLS는 CloudFront에서 종단하므로, 클러스터 IP를 직접 가리키던 이 베어 A 레코드는 https로 성공할 수 있었던 적이 없다. DNS 레코드를 회수하고 프로브 대상은 살아 있는 `palcar.co.kr/health` 로 옮겼다. 대상을 지우기만 하면 알림은 조용해져도 palcar 감시가 사라지기 때문이다.

## 알려진 결함

2026-08-03에 운영 클러스터에서 대조하며 확인했고, 2026-08-08 재확인에도 아래 세 건은 그대로 남아 있다.

### 개발 알림이 운영 채널로 섞인다

`DISCORD_WEBHOOK_URL_DEV` 는 Alerta 배포 매니페스트가 `optional: true` 로 참조하지만 시크릿에는 키 자체가 없다. 그래서 파드는 정상 기동하고, 개발 클러스터 알림은 조용히 운영 채널로 들어온다. Infisical `/platform/incident-alerting` 에 키를 추가하면 해소되며 매니페스트는 손대지 않아도 된다.

### papersens와 namanva의 런타임 오류가 디스코드로 오지 않는다

`alert-webhook` 시크릿이 `do4i` 와 `palcar` 에만 있다. `papersens` 와 `namanva` 에서 나는 앱 오류는 직송 경로를 타지 못한다. 특히 `namanva` 는 `api` 디플로이가 `0/1` 로 떠 있지 못한 상태여서 알림 공백이 실제 장애와 겹쳐 있다.

### 오래 열린 알림이 디스코드에서 사라진다

Discord 플러그인이 중복 알림을 건너뛰기 때문에, 처음 한 번 알린 뒤로는 해결될 때까지 채널에 아무것도 남지 않는다. 실제로 `KubePodNotReady` 는 2026-07-12부터 22일째 열린 채로 중복 1,273회를 기록하고 있지만 디스코드만 보고 있으면 이를 알 수 없다. 도배를 막으려는 의도된 동작이므로 코드를 고치기보다, **열린 인시던트는 Alerta 화면으로 주기 점검한다**는 운영 습관으로 메운다.

### 그 밖에

- ⚠️ Alerta는 replica 1이다. Alerta가 내려가면 Alerta를 거치는 알림이 전부 멈춘다. 앱 직송 경로는 영향을 받지 않는다.
- ⚠️ `node-exporter` 파드가 재시작 774회를 기록하고 있다. 알림 경로와 직접 관계는 없지만 노드 메트릭 결손 가능성이 있어 별도로 봐야 한다.

## 확인된 현황 (2026-08-03 기준, 프로브 항목은 2026-08-08 재확인)

| 항목 | 상태 |
| --- | --- |
| Alerta / Loki / Alloy / blackbox-exporter 파드 | 모두 Running, 재시작 0회 |
| `metrics-digest` CronJob | 매시 정각(Asia/Seoul) 정상 실행, 직전 회차 전송 성공 |
| Alertmanager → Alerta 전달 | 정상. webhook POST가 계속 `201` 로 수신됨 |
| ArgoCD → 디스코드 배포 알림 | 정상 동작 확인 |
| 고유 디스코드 웹훅 값 | **4개** (서로 다른 채널). 키 이름은 5종 |
| `DISCORD_WEBHOOK_URL_DEV` | 키 없음 (운영 채널로 폴백 중) |
| `ALERTA_API_KEY` | 어디에도 없음 (직송 경로로 대체됨) |
| `probe_success` 시계열 | **8개, 전부 `1`** (2026-08-08). `blackbox-public` 이 스크레이프 대상 목록에 정상 등재됨 |
| `PlatformEndpointDown` 발화 | 0건 (2026-08-08). 발화도 pending도 없음 |
| Alerta 열린 인시던트 | 4건, 모두 `Production` · `warning` |

이 문서 이전의 설계 배경은 [11. 운영 장애 Discord 리포트 솔루션 리서치](../11. 운영 장애 Discord 리포트 솔루션 리서치/index.md)와 [12. k3s 운영 장애 Discord 리포트 설계](../12. k3s 운영 장애 Discord 리포트 설계/index.md)에 있다. 두 문서는 2026-03-29 시점 기록이라 현행 구성과 다른 부분이 있고, 실제 구성은 이 문서를 따른다.

---

> **관련 문서**
> 파이프라인 구조: [03. 알림 - Alertmanager와 Alerta](../03. 알림 - Alertmanager와 Alerta/index.md) · 심각도와 에스컬레이션: [09. 알림에서 인시던트, 에스컬레이션까지](../09. 알림에서 인시던트, 에스컬레이션까지/index.md) · 섹션 목차: [03. 관측과 SRE](../index.md)
