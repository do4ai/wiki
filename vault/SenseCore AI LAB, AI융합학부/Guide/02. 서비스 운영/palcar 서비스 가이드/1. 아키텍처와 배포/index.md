---
title: "1. 아키텍처와 배포"
---
# palcar 아키텍처와 배포

## 아키텍처 구조

```
[프론트엔드] React 18 + Vite (2종)
  ├ client/palcar (딜러/셀러)  palcar.do4ai.com
  └ client/admin  (운영)       admin.palcar.do4ai.com
        │  /api/v1*
        ▼
   ingress-nginx
        ▼
   api (FastAPI, :8000) ── MySQL (StatefulSet)
                        └─ AWS S3 (차량 이미지)
```

### 프론트엔드 (2종)
- `client/palcar`: 딜러/셀러 사용자 앱(React 18 + Vite + TypeScript, Radix UI + Tailwind). `palcar.do4ai.com`
- `client/admin`: 운영 대시보드(React 18 + Vite, TanStack Table + Recharts). `admin.palcar.do4ai.com`

### 백엔드
- **Python 3.11 + FastAPI + SQLAlchemy 2.0** 기반 **DDD 모놀리스**.
- 포트 8000, 헬스 `/health`, API 프리픽스 `/api/v1`.
- 바운디드 컨텍스트(9): `identity`(인증) · `dealers`(딜러 온보딩/KYC) · `vehicles`(차량) · `bidding`(입찰) · `trades`(검수·정산 단계) · `settlement`(정산) · `support` · `settings` · `admin`.
- 마이그레이션: **Alembic 아님**: 코드 우선(`Base.metadata.create_all()` + 보강 헬퍼).

### 데이터
- **MySQL 8.0** StatefulSet(SQLAlchemy + pymysql, utf8mb4).
- **AWS S3**(boto3)에 차량 이미지 저장(프리사인 URL), 로컬 폴백 있음.

### 외부 의존성
- 인증은 **자체 JWT**(python-jose), 외부 OAuth 없음. **LLM 사용 없음**. 외부 경매 API 연동 없음(자체 입찰 로직).

## 배포 구조

- **네임스페이스**: `palcar` (prod·dev). *프론트는 별도 빌드/배포.*
- **GitOps 경로**: `gitops/k8s/apps/palcar` (base + overlays/prod·dev), ArgoCD Application `palcar`.
- **이미지**: API `harbor.do4i.com/do4ai/palcar-api`.
- **시크릿**: Infisical → `InfisicalSecret`(api/mysql/harbor).
- **prod 규모**: 신규 HPA(min 2 / max 6) + PDB minAvailable 1.
- **도메인**: prod `palcar.do4ai.com`, `admin.palcar.do4ai.com` / dev `palcar.dev.do4ai.com` 등.

> 배포 이상 대응은 [3. 운영 절차](../3. 운영 절차/index.md). 도구는 [Manual/04 ArgoCD 사용법](../../../../Manual/04. 서버와 배포 작업/ArgoCD 사용법/index.md).

---

> **온보딩 트랙 2부. 서비스 운영**
> 이전: [palcar 서비스 가이드](../index.md) · 다음: [palcar 모니터링·알람·SRE](../2. 모니터링·알람·SRE/index.md) · 전체 경로: [시작하기: 신입 온보딩](../../../../시작하기/index.md)
