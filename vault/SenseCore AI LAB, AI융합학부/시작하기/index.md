---
title: "시작하기 (신입 온보딩)"
---

# 🚀 시작하기 — 신입 온보딩

이 문서는 SCAI LAB(데이터센스)에 새로 합류한 사람이 **여기서 출발해** 위키 전체와 개발·운영 인프라를 막힘 없이 따라가도록 만든 **최상위 입구**다. (Guide·Manual 등 다른 영역과 나란히, 가장 먼저 본다.)

먼저 **0장에서 위키 전체 지도(어디에 뭐가 있나)** 를 잡고, 1~6장에서 우리 인프라·접속·학습 경로·첫 대응을 익힌다.

---

## 0. 위키 전체 지도 (어디에 뭐가 있나)

처음 온 사람은 이 표로 "무엇을 찾을 때 어디로 가는지"를 먼저 잡는다.

| 영역 | 무엇을 담나 | 들어가기 |
| --- | --- | --- |
| 🚀 **시작하기** | 신입 온보딩·학습 경로 (지금 이 문서) | — |
| 📖 **Guide** | 시스템·서비스를 **이해**하는 가이드 (개념 + 실제 우리 설정) | [Guide](../Guide/index.md) |
| 　├ 01. 인프라와 플랫폼 | 기반: k3s·GitOps·ArgoCD·ingress·Harbor·Infisical·Headlamp | [01](../Guide/01. 인프라와 플랫폼/index.md) |
| 　├ 02. 서비스 운영 | 서비스별(do4i·passv·palcar·papersens·wiki) 아키텍처·운영 | [02](../Guide/02. 서비스 운영/index.md) |
| 　└ 03. 관측과 SRE | 관측 솔루션·URL·메트릭/로그 + 서비스별 조치 + SLO·인시던트 | [03](../Guide/03. 관측과 SRE/index.md) |
| 🗓️ **Manual** | **도구 사용 절차**(ArgoCD·k3s·Grafana·Kibana·Infisical·Harbor·Alerta) | [Manual](../Manual/index.md) |
| 🧾 **Domains** | 프로젝트 도메인 문서(DDD: 컨텍스트 맵·UL 등) | [Domains](../Domains/index.md) |
| 💼 **Convention** | 개발·운영에서 지켜야 하는 규칙 | [Convention](../Convention/index.md) |
| 📚 **Wiki** | 분야별 지식베이스(개발·LLM·VLM·기획 등) | [Wiki](../Wiki/index.md) |
| 💻 **Lecture** | 강의 자료(수학·개발·AI) | [Lecture](../Lecture/index.md) |
| 👥 People / 🔍 R&D | 구성원 소개 / 연구·과제(완료·진행 중) | [동료 소개](../SCAI LAB의 동료들을 소개합니다/index.md) |

**핵심 구분 한 줄**: *무엇인지 이해 = Guide / 도구 어떻게 쓰나 = Manual / 신입은 여기(시작하기)부터.*

---

## 1. 우리 인프라 한 장 그림

```
[ 사용자/브라우저 ]
        │  HTTPS
        ▼
[ CloudFront (엣지, TLS 종료) ]              공개 도메인 viewer TLS는 여기서 끝남
        │  HTTP 80 (hidden origin)
        ▼
[ k3s 클러스터의 ingress-nginx ]            클러스터 단일 진입점 (HostPort 80/443)
        │
        ├─► do4i        agents.do4i.com / admin.do4i.com        (ns: do4i)
        ├─► passv        app/api/admin.passv.co.kr               (ns: passv)  ※EC2→K8s 이전 중
        ├─► palcar       palcar.do4ai.com / admin.palcar.do4ai.com (ns: palcar)
        ├─► papersens    papersens.do4ai.com / *.ps.do4ai.com    (ns: papersens)
        └─► wiki         wiki.do4ai.com                          (ns: atlas) ※코드상 atlas = 서비스 wiki
```

**배포(GitOps)**: 개발자가 `gitops` 레포 `main`에 push → ArgoCD가 레포를 "원하는 상태"로 읽고 클러스터를 그 상태로 자동 수렴. 클러스터를 직접 고치는 게 아니라 **레포를 고치면 클러스터가 따라온다.**

**관측/알림**: 메트릭(Prometheus) + 로그(Filebeat→Elasticsearch→ElastAlert) + 트레이스(OTel→Tempo) → **Alerta**(인시던트 집계) → **Discord**. ArgoCD 배포 실패, 앱 발화 실패도 Alerta로 모인다.

---

## 2. 접속 포인트 & 계정 (가장 먼저 북마크)

| 용도 | URL | 비고 |
|------|-----|------|
| 배포 상태 (ArgoCD) | `argocd.do4ai.com` | 앱이 OutOfSync/Degraded인지 1순위 확인 |
| 대시보드 (Grafana) | `grafana.do4ai.com` (dev: `grafana.dev.do4ai.com`) | NodePort 30300 |
| 메트릭 (Prometheus) | `prometheus.do4ai.com` (dev: `prometheus.dev.do4ai.com`) | basic auth |
| 로그 (Kibana) | `kibana.do4ai.com` | 인덱스 `filebeat-*`, 필터 `kubernetes.namespace:<서비스>` |
| 인시던트/알림 (Alerta) | `alerta.do4ai.com` | 알림이 모이고 Discord로 전송 |
| 클러스터 대시보드 (Headlamp) | `headlamp.do4ai.com` | **읽기 전용** |
| 시크릿 관리 (Infisical) | `infisical.do4ai.com` | 모든 앱 시크릿의 원천 |
| 이미지 레지스트리 (Harbor) | `harbor.do4i.com` | 도메인 주의: `do4i.com`. 경로 `harbor.do4i.com/do4ai/*` |

> 실제 자격증명(비밀번호/토큰)은 **담당자에게 발급**받는다. 공개 문서에는 비밀번호를 적지 않는다.

**클러스터**: `do4ai-prod`(운영), `do4ai-dev`(개발). 네임스페이스는 환경 접미사 없이 서비스명만 사용한다(`do4i`, `passv`, `palcar`, `papersens`, `atlas`, `namanva`).

**첫날 체크리스트**

- [ ] 위 URL 접속 가능(네트워크/VPN 포함)
- [ ] `kubectl` 설치 + kubeconfig 수령 + 클러스터 접근 권한
- [ ] GitHub `do4ai` org / `gitops` 레포 접근 권한
- [ ] Discord 운영 알림 채널 초대
- [ ] Infisical / Harbor 계정 발급

---

## 3. 신입 학습 경로 (Guide 연결)

순서대로 다 읽지 말고, 아래 동선으로 "개념 → 우리 환경 → 실전" 순으로 읽는다.

**1주차 — 지도 펴기**

1. 이 문서 1~2장
2. [01. 인프라와 플랫폼 / 01. Kubernetes 기본 구조 가이드](../Guide/01. 인프라와 플랫폼/01. Kubernetes 기본 구조 가이드/index.md)
3. [01. 인프라와 플랫폼 / 03. k3s GitOps 운영 클러스터 초보자 가이드](../Guide/01. 인프라와 플랫폼/03. k3s GitOps 운영 클러스터 초보자 가이드/index.md) — **신입 핵심**
4. [01. 인프라와 플랫폼 / 04. GitOps 운영 모델 가이드](../Guide/01. 인프라와 플랫폼/04. GitOps 운영 모델 가이드/index.md)
5. [03. 관측과 SRE / 06. 모니터링·알림 아키텍처 가이드](../Guide/03. 관측과 SRE/06. 모니터링·알림 아키텍처 가이드/index.md)

> 1주차 목표: "배포는 gitops 레포가 기준이고 ArgoCD가 수렴시킨다", "장애 알림은 Alerta→Discord로 온다"를 말로 설명할 수 있다.

**2주차 — 도구 손에 익히기**

6. [05. ArgoCD 운영 흐름 가이드](../Guide/01. 인프라와 플랫폼/05. ArgoCD 운영 흐름 가이드/index.md) + 실제 `argocd.do4ai.com` 둘러보기
7. 01 섹션의 06 ingress-nginx · 07 Harbor · 08 Infisical · 09 Headlamp
8. 03 섹션의 02 메트릭 · 03 알림 · 04 로그 · 05 트레이싱
9. 실습: 서비스 하나를 골라 ArgoCD → Grafana → Kibana에서 직접 상태 확인

**3주차 — 담당 서비스 + 첫 대응**

10. [02. 서비스 운영 / 서비스 공통 1차 대응 절차](../Guide/02. 서비스 운영/서비스 공통 1차 대응 절차/index.md) — **장애 대응의 뼈대**
11. 담당 서비스의 `02. 서비스 운영/<서비스> 서비스 가이드` 3종(아키텍처·모니터링·운영절차)
12. `03. 관측과 SRE / 07. 서비스별 관측과 조치 / <서비스> 관측과 조치`
13. [10. 장애 대응 의사결정 가이드](../Guide/03. 관측과 SRE/10. 장애 대응 의사결정 가이드/index.md) + [09. 알림에서 인시던트, 에스컬레이션까지](../Guide/03. 관측과 SRE/09. 알림에서 인시던트, 에스컬레이션까지/index.md)
14. 과거 인시던트 1건을 Alerta에서 찾아 선배와 함께 리뷰

> `03`의 11·12번(Discord 리포트 리서치/설계)은 **운영 가이드가 아니라 설계 배경 문서**다. 알림 파이프라인의 "왜 이렇게 만들었나"가 궁금할 때만 본다.

---

## 4. 빠른 용어/도구 사전

| 용어 | 한 줄 설명 |
|------|-----------|
| k3s | 가벼운 Kubernetes 배포판. 우리 클러스터의 실체 |
| GitOps | "Git 레포가 인프라의 정답지". 레포를 바꾸면 클러스터가 따라옴 |
| ArgoCD | GitOps 컨트롤러. 레포(desired)와 클러스터(live)를 비교해 수렴 |
| desired / live / drift / reconcile | 원하는 상태 / 실제 상태 / 둘의 차이 / 차이를 메우는 과정 |
| Sync Status / Health Status | (ArgoCD) Git과 같은가 / 리소스가 정상인가. **둘을 같이 본다** |
| OutOfSync | Git과 클러스터가 다름. **그 자체로 장애 아님**(배포 중일 수 있음) |
| kustomize base/overlay | 공통 매니페스트 + 환경별 차이(overlays/prod·dev) |
| Ingress | 외부 HTTP(S)를 어떤 서비스로 보낼지 정한 라우팅 규칙 |
| Infisical | 시크릿 중앙 저장소. 앱은 받은 값을 K8s Secret으로 주입받음 |
| Harbor | 사설 컨테이너 이미지 저장소(`harbor.do4i.com`) |
| Alerta | 여러 알림을 모아 상태 관리하고 Discord로 보내는 인시던트 허브 |
| Prometheus / Grafana | 메트릭 수집·저장 / 대시보드 |
| Filebeat / Elasticsearch / Kibana / ElastAlert | 로그 수집 / 저장 / 검색 / 로그기반 알림 |
| OpenTelemetry / Tempo | 트레이스 수집 / 저장 (요청이 어디서 느린지 추적) |
| SLO / SLI / 에러 버짓 / 번레이트 | 목표치 / 실측 지표 / 허용 실패량 / 그 소진 속도 |
| CrashLoopBackOff / ImagePullBackOff / OOMKilled / Pending | 앱 반복 죽음 / 이미지 못 받음 / 메모리 초과 종료 / 스케줄 대기 |
| HPA / PDB / StatefulSet | 부하 따라 replica 자동조절 / 동시 중단 최소보장 / 상태를 가진 워크로드(예: DB) |
| LiveKit / Simli / Minimax / OpenRouter / Ollama | 외부 의존성: 실시간통신 / AI아바타 / TTS / LLM API / 로컬 LLM |

---

## 5. 시나리오별 "첫 대응"

**공통 1차 (모든 상황)**

```bash
# 1) ArgoCD 앱 상태 (또는 argocd.do4ai.com)
sudo kubectl get applications -A
# 2) 해당 네임스페이스 리소스
sudo kubectl get deploy,sts,svc,ing -n <namespace>
sudo kubectl get pods -n <namespace>
# 3) 로그
sudo kubectl logs deploy/<name> -n <namespace> --tail=100
```

체크 키워드: `OutOfSync` `Degraded` `CrashLoopBackOff` `ImagePullBackOff` `Pending` `OOMKilled`

**증상별 분기**

| 증상 | 먼저 의심 | 보는 곳 |
|------|----------|---------|
| 배포 후 앱이 안 뜸 | 직전 배포 / 이미지 / 시크릿 | ArgoCD Health → pod events → 로그. 직전 배포면 **롤백** |
| `ImagePullBackOff` | 이미지 태그 / 레지스트리 권한 | overlay `images:` 태그 → Harbor 태그 존재? → pull 시크릿 |
| `CrashLoopBackOff` | 설정 / 시크릿 / 코드 | 앱 로그, env/Secret 주입(Infisical) |
| `OOMKilled` (특히 papersens) | 메모리 한계 | Grafana 메모리 → limit 상향 검토 |
| 특정 도메인만 5xx/접속불가 | ingress / 라우팅 | `kubectl describe ingress`, Grafana `nginx-ingress` 5xx율 |
| 광역 장애 | 공통 인프라 | 노드/PVC/ingress, **즉시 에스컬레이션** |
| 챗봇 발화 실패(passv) | LLM / 아바타 의존성 | Alerta `ChatGenerationFailed`, LLM/LiveKit/Simli 키 |
| 위키 문서 미갱신 | content-sync | `kubectl logs deploy/atlas -c content-sync -n atlas` |

**롤백 판단 요지**

- 최근 배포 직후 critical/에러율 급증 → **즉시 롤백**, 원인분석은 그 다음
- 원인 명확한 단순 버그면 핫픽스가 더 빠를 수 있음
- 인프라 신호(노드 Pressure/PVC/MySQL Ready 0)면 앱 재배포가 아니라 인프라 조치
- **prod의 do4i/passv는 ArgoCD 자동 동기화가 꺼져(게이팅) 있을 수 있음** → 롤백 시 sync 방식 확인
- 자세한 판단표: [10. 장애 대응 의사결정 가이드](../Guide/03. 관측과 SRE/10. 장애 대응 의사결정 가이드/index.md)

---

## 6. 알아두면 헷갈리지 않는 것

- Harbor 도메인만 `harbor.do4i.com`(다른 인프라는 `do4ai.com`).
- 레지스트리 혼용: do4i·palcar는 **Harbor**, papersens·passv·namanva는 **AWS ECR**.
- passv는 현재 prod가 **EC2(docker compose) + S3/CloudFront**, K8s(`passv` 네임스페이스)로 **이전 중**. K8s 절차는 컷오버 후 기준.
- wiki 서비스는 코드/배포상 이름이 **`atlas`**(네임스페이스·ArgoCD Application 모두 atlas). 콘텐츠 정본은 GitHub `do4ai/wiki` 레포.
- 시크릿 실체는 **Infisical Operator**(InfisicalSecret CRD). 일부 README의 Sealed Secrets는 레거시.
