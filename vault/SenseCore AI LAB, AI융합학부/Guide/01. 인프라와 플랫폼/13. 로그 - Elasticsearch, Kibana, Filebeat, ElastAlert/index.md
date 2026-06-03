---
title: "13. 로그 - Elasticsearch, Kibana, Filebeat, ElastAlert"
---
# 13. 로그 — Elasticsearch · Kibana · Filebeat · ElastAlert (ELK)

우리가 실제 구축한 로그 스택이다. 모두 `observability` 네임스페이스에서 돌고, **ECK(eck-stack 0.18.1)** 로 Elasticsearch/Kibana를, `central-logging` 앱으로 Filebeat/ElastAlert를 배포한다.

```
파드 stdout/stderr → /var/log/containers/*.log
        │ Filebeat(DaemonSet, k8s 메타데이터 추가)
        ▼
Elasticsearch(filebeat-* 인덱스) ── Kibana(검색 UI)
        │
        └ ElastAlert(1분 주기 스캔) → Alerta → 디스코드
```

## Elasticsearch
- **버전 9.3.0**, **노드 1개** → ⚠️ **SPOF**(HA 아님). 스토리지 10Gi, CPU 0.5~2 / 메모리 2~4Gi.
- 내부 엔드포인트 `elasticsearch-es-http.observability.svc:9200`(HTTPS, 자체서명). 스냅샷 경로 호스트 마운트.
- **인덱스**: 컨테이너 로그는 `filebeat-*`.

## Kibana
- **버전 9.3.0**, replicas 1. **접속 `kibana.do4ai.com`**(nginx ingress). 계정 `admin / Admin12!`(⚠️ 평문, 로테이션 대상).
- 용도: 로그 검색·필터(네임스페이스/컨테이너/시간으로 좁히기), 앱 로깅 대시보드.

## Filebeat
- **버전 9.3.0**, **DaemonSet**(모든 노드). `filebeat-wolfi` 이미지, hostNetwork.
- 수집: `/var/log/containers/*.log` → `add_kubernetes_metadata`로 namespace/pod/container/node 라벨 부여, `cluster=do4ai-prod`.
- 전송: Elasticsearch `:9200`(elastic 유저, TLS).

## ElastAlert (ElastAlert2)
- **버전 2.27.0**(`jertel/elastalert2`), replicas 1(⚠️ SPOF). `filebeat-*`를 **1분 주기**로 스캔(15분 버퍼).
- **규칙 2종**(대상 네임스페이스 do4i/palcar/papersens/namanva):
  | 규칙 | 조건 | Alerta severity |
  | --- | --- | --- |
  | error-burst | 5분에 ERROR/Exception/Traceback/CRITICAL/panic/FATAL **5건↑** | warning |
  | http-5xx-burst | 5분에 액세스로그 500/502/503/504 **3건↑** | major |
  - 재알림 30분. → Alerta로 전송(group `logging`).

## 배포·연결
- ArgoCD 앱: `elastic-operator`(ECK 오퍼레이터) → `observability`(ES+Kibana) → `central-logging`(Filebeat+ElastAlert). dev 클러스터에는 **로그 스택 미배포**(prod 전용).

## 1차 확인 포인트
1. 앱 오류는 Kibana(`kibana.do4ai.com`)에서 namespace/시간으로 좁혀 메시지 확인.
2. 로그가 안 들어오면: Filebeat DaemonSet Ready, ES 파드(SPOF), `filebeat-*` 인덱스 순으로 점검.
3. 절차는 [Manual 06. 모니터링-로그 작업](../../../Manual/06. 모니터링-로그 작업/index.md).
