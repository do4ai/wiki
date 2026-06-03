---
title: "14. 트레이싱 - OpenTelemetry와 Tempo"
---
# 14. 트레이싱 — OpenTelemetry와 Tempo

요청이 **어느 구간에서 느려지거나 실패하는지**를 보는 분산 트레이싱 스택이다. `observability` 네임스페이스에서 돈다.

```
앱(Python, 자동계측) ─ OTLP 4317/4318 ─ otel-gateway(2 replica)
        │ batch·k8sattributes·resource
        ▼
Tempo(72h 보존) ── Grafana(Tempo 데이터소스, tempo:3200)
   │ 스팬 메트릭 remote-write
   ▼
Prometheus(traces_spanmetrics_*) → platform-api-apm 대시보드
```

## OpenTelemetry
- **Operator**(chart 0.109.0): `Instrumentation`/`OpenTelemetryCollector` CRD 관리.
- **Collector = otel-gateway**(chart 0.147.1, **replicas 2 = HA**): 수신 OTLP **gRPC 4317 / HTTP 4318**, 처리 `memory_limiter → k8sattributes → resource → batch`, 내보내기 → Tempo `:4317`. 트레이스 파이프라인만 활성(메트릭/로그 off).
- **앱 계측**(`Instrumentation` `platform-python`): 앱은 `otel-gateway.observability.svc:4317/4318`로 스팬 전송. 샘플링 **100%**(parentbased_traceidratio=1), 전파 tracecontext/baggage/b3.
- 관련 알림: `OTelGatewayUnavailable`.

## Tempo
- **chart 1.24.4**, **replicas 1** → ⚠️ **SPOF**. 보존 **72h**, 스토리지 20Gi.
- **스팬 메트릭 생성기**: `service_graphs`+`span_metrics`를 켜고, Prometheus로 **remote-write**(`/api/v1/write`) → `traces_spanmetrics_calls_total`, `..._latency_bucket` 생성.
- Grafana는 Tempo 데이터소스(`tempo.observability.svc:3200`)로 트레이스를 조회하고, 스팬 메트릭은 Prometheus에서 읽어 **platform-api-apm** 대시보드(요청율·에러율·p95)를 그린다.
- 관련 알림: `TempoUnavailable`, APM 기반 `PlatformAppServerErrorRateHigh`/`LatencyP95High`.

## 배포·연결
- ArgoCD 앱: `opentelemetry-operator` → `otel-collector`(otel-gateway) → `tempo` → `apm`(Instrumentation). prod 전용.

## 1차 확인 포인트
1. 특정 요청이 느리면 Grafana → Explore(Tempo)에서 trace 검색, 또는 platform-api-apm에서 서비스별 p95·에러율.
2. APM 알림이 떴는데 트레이스가 비면 otel-gateway(2 replica)·Tempo(SPOF) 상태 확인.
3. 메트릭/로그와 함께 보는 순서는 [10. Observability 운영 가이드](../01. Observability 운영 가이드/index.md).
