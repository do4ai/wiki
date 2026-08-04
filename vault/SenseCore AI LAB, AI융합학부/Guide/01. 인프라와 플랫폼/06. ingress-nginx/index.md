---
title: "06. ingress-nginx"
---
# 06. ingress-nginx

클러스터로 들어오는 모든 HTTP(S) 트래픽의 입구(리버스 프록시)다. 각 서비스의 `Ingress` 리소스를 실제 라우팅으로 구현한다.

## 실제 구성
- **Helm chart 4.10.1**, 두 클러스터(prod·dev) 모두 배포(sync-wave 0, 가장 먼저).
- **노출**: NodePort **30800(HTTP)/30843(HTTPS)** + **hostPort 80/443**(노드에 직접 바인드).
- **ingressClass**: `nginx` (모든 서비스 Ingress가 이 클래스를 지정).
- 주요 설정: `proxy-body-size 100m`, `use-forwarded-headers true`, 메트릭+ServiceMonitor(prod) → Grafana `nginx-ingress` 대시보드·`PlatformAppIngress5xxRatioHigh` 알림의 측정원.
- **TLS**: 공개 트래픽은 보통 **CloudFront(엣지)에서 TLS 종료** 후 백엔드 HTTP로 들어온다(ingress hostPort 80/443은 유지).

## 무엇을 위해 보나
- 5xx·라우팅 문제의 1차 지점. 특정 호스트/경로가 안 되면 해당 서비스 `Ingress`의 host/path/backend(service:port)가 맞는지 확인.
- ingress 5xx는 Grafana `nginx-ingress` 대시보드 + Prometheus 메트릭으로 본다.

## 연결
- 앞단: CloudFront/엣지 → 뒷단: 각 서비스 `Service`. 서비스별 도메인·경로는 [02. 서비스 운영](../../02. 서비스 운영/index.md)의 각 가이드.
- 변경 절차(도메인/경로/환경변수)는 [Manual 05. 운영 변경 작업](../../../Manual/05. 운영 변경 작업/Ingress, 도메인, 이미지, 환경 변수 변경 절차/index.md).

---

> **온보딩 트랙 1부. 인프라와 플랫폼**
> 이전: [ArgoCD 사용법 (Manual)](../../../Manual/04. 서버와 배포 작업/ArgoCD 사용법/index.md) · 다음: [Harbor 컨테이너 레지스트리](../07. Harbor 컨테이너 레지스트리/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../시작하기/index.md)
