---
title: "04. 로그 - Loki와 Alloy"
---
# 04. 로그 - Loki와 Alloy

우리가 실제 운영하는 로그 스택이다. **`monitoring` 네임스페이스**에서 메트릭 스택과 함께 돌고, ArgoCD `monitoring` 앱이 **dev·prod 양 클러스터에 동일하게** 배포한다. 로그 조회 창구는 별도 UI가 아니라 **Grafana Explore**다.

```
파드 stdout/stderr → /var/log/pods/<ns>_<pod>_<uid>/<container>/*.log
        │ Alloy(DaemonSet, kubernetes_sd + relabel + CRI 파싱)
        ▼
Loki(단일 바이너리, tsdb) ── Grafana Explore(조회)
        │
        └ Loki ruler(1분 주기) → Alertmanager → Alerta → 디스코드
```

2026-07-31 이전에는 Elasticsearch/Kibana/Filebeat/ElastAlert(ELK)를 썼다. 은퇴 경위와 남은 자산은 아래 ELK 은퇴 절에 적었다.

## Loki
- **grafana/loki 3.1.1**, StatefulSet **replicas 1** → ⚠️ **SPOF**(HA 아님). PVC 30Gi(`local-path`), 메모리 0.5~2Gi.
- 단일 바이너리 모드라 한 프로세스가 distributor·ingester·querier·compactor·ruler를 모두 돌린다.
- 내부 엔드포인트 `loki.monitoring.svc.cluster.local:3100`. 인증 없음(`auth_enabled: false`, 단일 테넌트 `fake`).
- **인덱스** tsdb v13, 저장소는 파일시스템. **보존 336시간(14일)** 이고 컴팩터가 보존 삭제를 수행한다.
- 수집 한도는 **16MB/s(버스트 32MB)**, 스트림당 8MB/16MB. 기본값(4MB/s)으로는 수집기 최초 기동 시 기존 로그를 한꺼번에 읽어 올리다 429로 라인이 버려진다.

## Alloy
- **grafana/alloy v1.18.0**, DaemonSet(모든 노드). `/var/log`를 읽기 전용으로 마운트하고, 읽은 위치는 `/var/lib/alloy`에 영속 저장한다.
- 파드를 서비스 디스커버리로 찾아 릴레이블로 로그 파일 경로(`__path__`)와 조회 라벨을 만든다. k3s는 containerd이므로 CRI 포맷으로 파싱한다.
- 부여 라벨: `cluster`, `namespace`, `pod`, `container`, `node`, `app`, `job`, `filename`.
- `cluster` 값은 컨테이너 인자로 주입한다. prod는 `do4ai-prod`, dev는 오버레이 패치로 `do4ai-dev`.

### promtail을 쓰지 않는 이유
promtail은 이 클러스터(k8s v1.34.5+k3s1)에서 동작하지 않는다. 같은 노드·같은 권한·같은 릴레이블 규칙으로 비교한 실측 결과다.

| 수집기 | 발견한 타겟 | Loki 적재 |
| --- | --- | --- |
| promtail 3.1.1 | 0 | 0건 |
| promtail 3.5.1 | 0 | 0건 |
| Alloy v1.18.0 | 정상 | 정상 |

promtail은 디버그 로그에서도 디스커버리 프로바이더 기동 이후 **타겟 그룹을 한 번도 전달받지 못하고 오류도 남기지 않는다**. RBAC·파일 권한·경로 매칭은 모두 정상이므로 번들된 client-go와 API 서버 버전 차이로 판단한다. promtail은 상위 프로젝트에서도 Alloy로 대체된 컴포넌트다.

## 로그 조회
`grafana.do4ai.com` → **Explore** → 데이터소스 **Loki**. dev는 `grafana.dev.do4ai.com`을 쓴다.

| 목적 | 쿼리 |
| --- | --- |
| 네임스페이스 전체 | `{namespace="do4i"}` |
| 특정 파드 | `{namespace="papersens", pod=~"papersens-.*"}` |
| 오류만 | `{namespace="do4i"} \|~ "ERROR\|Exception\|Traceback"` |
| 네임스페이스별 발생량 | `sum by (namespace) (count_over_time({cluster="do4ai-prod"}[5m]))` |

`cluster` 라벨로 운영·개발을 구분한다. 두 클러스터의 Loki는 서로 독립이므로 각 클러스터의 Grafana에서 본다.

## 로그 기반 알림
Loki ruler가 **1분 주기**로 평가하고 Alertmanager를 거쳐 Alerta로 보낸다. 대상 네임스페이스는 `do4i`·`palcar`·`papersens`·`passv`다.

| 규칙 | 조건 | severity |
| --- | --- | --- |
| PlatformLogErrorBurst | 5분에 ERROR/Exception/Traceback/CRITICAL/panic/FATAL **5건 초과** | warning |
| PlatformLogHttp5xxBurst | 5분에 액세스로그 500/502/503/504 **3건 초과** | major |

## 로그 스택 자체 감시
수집이 조용히 멈추는 상황을 잡기 위해 Prometheus 룰 3종을 둔다. **세 식 모두 `absent()` 가드를 포함**한다. 오브젝트가 아예 없으면 시계열도 없어서 단순 비교식만으로는 "배포되지 않은 상태"를 잡지 못하기 때문이다.

| 알림 | 조건 |
| --- | --- |
| LokiUnavailable | Loki StatefulSet이 5분간 준비되지 않거나 존재하지 않음 |
| AlloyNotReady | Alloy DaemonSet이 10분간 목표 준비 수에 미달하거나 배포되지 않음 |
| PlatformLogIngestionStalled | Loki로 들어오는 로그가 20분간 한 줄도 없음 |

## 배포·연결
- ArgoCD `monitoring` 앱이 `gitops/k8s/infra/monitoring/manifests`를 동기화한다. 매니페스트는 `loki.yaml`·`alloy.yaml`이고, dev 차이는 `manifests-dev/patches/`에 있다.
- Loki와 Alloy는 설정을 자동 리로드하지 않는다. ConfigMap만 바꾸면 파드가 재시작되지 않으므로 파드 템플릿의 `checksum/...` 애노테이션을 함께 올린다.

## 1차 확인 포인트
1. 앱 오류는 Grafana Explore에서 `{namespace="<서비스>"}`로 좁혀 시간·메시지를 확인한다.
2. 로그가 안 들어오면 Alloy DaemonSet 준비 상태 → Alloy 파드 로그의 전송 오류 → Loki 파드 상태 순으로 점검한다.
3. 특정 시점 이후 로그가 끊겼다면 Loki 수집 한도(429)와 보존 기간(14일)을 먼저 확인한다.
4. 절차는 [Manual 06. 모니터링-로그 작업](../../../Manual/06. 모니터링-로그 작업/index.md).

## ELK 은퇴 (2026-07-31)
Loki를 양 클러스터에서 검증한 뒤 단계를 나눠 은퇴시켰다. 한 번에 지우면 수집기와 저장소가 동시에 사라지고, Elasticsearch CR을 지울 때 PVC까지 회수되어 과거 로그가 복구 불가가 된다.

| 단계 | 내용 |
| --- | --- |
| 사전 | Elasticsearch 전체 스냅샷. 63개 인덱스, 63:63 샤드 성공, 37GB |
| 1 | Filebeat·ElastAlert(수집·알림) 제거 |
| 2 | Elasticsearch·Kibana 비활성 및 CR 회수 |
| 3 | ECK 오퍼레이터, CRD, 클러스터 RBAC, `elastic-system` 네임스페이스 제거 |

- 스냅샷은 prod 노드 호스트 경로 `/var/lib/elasticsearch-snapshots`에 있다(저장소 `local-fs`, 스냅샷 `pre-elk-retirement-20260731`). Elasticsearch PVC와 별개 경로라 CR 회수 후에도 남아 있다. 복원하려면 ECK와 Elasticsearch를 다시 띄워 이 저장소를 등록해야 한다.
- `kibana.do4ai.com`은 오리진이 사라졌다. ⚠️ CloudFront·Route53 엣지 정리는 `TODO(확정 필요)`.

---

> **온보딩 트랙 — 3부 관측과 SRE**
> 이전: [알림 — Alertmanager와 Alerta](../03. 알림 - Alertmanager와 Alerta/index.md) · 다음: [트레이싱 — OpenTelemetry와 Tempo](../05. 트레이싱 - OpenTelemetry와 Tempo/index.md) · 전체 경로: [시작하기 — 신입 온보딩](../../../시작하기/index.md)
