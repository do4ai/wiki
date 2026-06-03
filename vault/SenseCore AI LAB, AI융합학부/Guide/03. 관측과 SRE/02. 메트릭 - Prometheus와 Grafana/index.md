---
title: "11. 메트릭 - Prometheus와 Grafana"
---
# 11. 메트릭 — Prometheus와 Grafana

우리가 실제 구축해 쓰는 메트릭 스택이다. `monitoring` 네임스페이스에 **kube-prometheus-stack(Helm chart 58.7.2)** 한 묶음으로 배포되며 Prometheus·Grafana·Alertmanager·node-exporter·kube-state-metrics를 함께 설치한다. (알림 라우팅/Alerta는 [12. 알림](../03. 알림 - Alertmanager와 Alerta/index.md) 참고.)

```
앱/노드/ingress(/metrics)
   │  ServiceMonitor·PodMonitor (셀렉터 비움 = 전 네임스페이스 수집)
   ▼
Prometheus ──(remote-write 수신)── Tempo 스팬 메트릭
   │                                  └ traces_spanmetrics_* (APM)
   └─ Grafana (대시보드, 데이터소스: Prometheus + Tempo)
```

## Prometheus
- **역할**: 메트릭 수집·저장·쿼리(PromQL), 알림 규칙 평가.
- **보존/스토리지**: retention **30d**, PVC **50Gi**.
- **스크레이프 대상**: `serviceMonitorSelector`/`podMonitorSelector`가 **비어 있어(`{}`) 전 네임스페이스의 모든 ServiceMonitor/PodMonitor를 수집**한다. node-exporter·kube-state-metrics·ingress-nginx·otel-gateway·tempo 등이 포함된다.
- **외부 라벨**: `environment=Production`, `cluster=do4ai-prod`.
- **remote-write 수신 활성**: Tempo가 스팬 메트릭을 Prometheus로 remote-write 한다(APM 대시보드 근거).
- **접속**: `prometheus.do4ai.com` (nginx **basic-auth**, `prometheus-basic-auth` 시크릿).

## Grafana
- **역할**: 대시보드·시각화. 메트릭(Prometheus)과 트레이스(Tempo)를 한곳에서 본다.
- **접속**: `grafana.do4ai.com` (NodePort **30300**). 영속 스토리지 10Gi.
- **계정**: `admin / Admin12!` — ⚠️ **values.yaml 평문 기본값. 로테이션 대상**([개선 과제]). 
- **데이터소스**: `Prometheus`(기본), `Tempo`(`http://tempo.observability.svc.cluster.local:3200`, traces→metrics 연동).
- **프로비저닝 대시보드**(코드로 관리):
  | 대시보드 | 출처 | 용도 |
  | --- | --- | --- |
  | kubernetes-cluster | Grafana #7249 | 클러스터 전반 |
  | node-exporter | Grafana #1860 | 노드 리소스 |
  | nginx-ingress | Grafana #9614 | ingress 트래픽·5xx |
  | do4i-api-operations | 커스텀 | do4i 가용 replica·재시작·5xx·CPU/메모리 |
  | papersens-operations | 커스텀 | papersens 동일 관점 |
  | platform-api-apm | 커스텀(Tempo 스팬 메트릭) | 요청율·에러율·p95(서비스 템플릿) |

## 배포·연결
- **배포**: ArgoCD `monitoring` 앱이 **멀티소스**로 설치 — ① Helm 차트(kube-prometheus-stack 58.7.2) ② `k8s/infra/monitoring/values.yaml` ③ `k8s/infra/monitoring/manifests/`(Alerta·알림 규칙·blackbox 등 kustomize).
- **dev**: `values-dev.yaml` + `manifests-dev/`.

## 1차 확인 포인트
1. Grafana `grafana.do4ai.com` → 서비스 대시보드(5xx·재시작·리소스).
2. 특정 메트릭이 안 보이면 대상이 ServiceMonitor/PodMonitor를 노출하는지, Prometheus Targets(`prometheus.do4ai.com`)에 떠 있는지 확인.
3. 도구 사용 절차는 [Manual 06. 모니터링-로그 작업](../../../Manual/06. 모니터링-로그 작업/Grafana, Kibana, Tempo 1차 장애 확인 절차/index.md).
