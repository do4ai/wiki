---
title: "do4i — 백업과 복구"
---
# do4i — 백업과 복구

do4i의 MySQL을 S3로 정기 백업하는 체계와 복구 절차를 정리한다. do4i MySQL은 단일 레플리카 StatefulSet이라 복제(replication)가 없으므로, 클러스터 밖 S3로 보내는 논리 백업이 유일한 회복 기준선이다.

## 백업 정책

- **주기**: 6시간마다(`Asia/Seoul` 기준 00·06·12·18시) 자동 실행한다. 데이터 손실 허용폭(RPO)은 최대 6시간이다.
- **방식**: `mysqldump --single-transaction`으로 잠금 없이 일관된 스냅샷을 뜬 뒤 gzip 압축해 S3에 올린다.
- **보관**: S3 Lifecycle로 30일(한 달)만 보관하고, 그보다 오래된 객체와 이전 버전은 자동 삭제한다.
- **자격증명**: put 전용 최소권한 IAM 키를 Infisical로 관리한다. git에는 평문 키를 두지 않는다.

## 구성 요소

| 요소 | 위치 |
| --- | --- |
| 백업 CronJob | `gitops/k8s/apps/do4i/base/mysql/backup-cronjob.yaml` (`do4i` 네임스페이스 `mysql-backup`) |
| 자격증명 동기화 | `gitops/k8s/apps/do4i/overlays/prod/infisical/db-backup-infisical-secret.yaml` → k8s 시크릿 `do4i-backup-aws` |
| Infisical 경로 | 프로젝트 `do4ai`, 환경 `prod`, 경로 `/apps/db-backup` |
| S3 버킷 | `s3://do4i-db-backup-prod-771237845307/do4i/` (리전 `ap-northeast-2`, 버저닝·SSE 활성) |
| S3 프리픽스 | `auto/`(CronJob 자동), `manual/`(수동 덤프) |

CronJob은 initContainer(`mysql:8.0.45`)가 덤프를 떠 `emptyDir`에 저장하고, 본 컨테이너(`amazon/aws-cli`)가 그 파일을 S3로 업로드하는 2단계로 동작한다.

## 즉시 백업 실행

정기 주기를 기다리지 않고 지금 한 번 백업하려면 CronJob에서 Job을 생성한다.

```bash
export KUBECONFIG=~/.kube/do4ai-prod.yaml
kubectl -n do4i create job --from=cronjob/mysql-backup mysql-backup-now
kubectl -n do4i logs -l job-name=mysql-backup-now -c upload -f
```

업로드가 끝나면 S3에서 확인하고, 확인 후 임시 Job을 정리한다.

```bash
aws s3 ls s3://do4i-db-backup-prod-771237845307/do4i/auto/
kubectl -n do4i delete job mysql-backup-now
```

## 복구 절차

특정 시점 백업으로 되돌린다. 운영 데이터를 덮어쓰므로 복구 전 반드시 현재 상태를 한 번 더 백업한다.

1. 복구 대상 백업 파일을 고른다.
   ```bash
   aws s3 ls s3://do4i-db-backup-prod-771237845307/do4i/auto/
   aws s3 cp s3://do4i-db-backup-prod-771237845307/do4i/auto/<파일명>.sql.gz /tmp/restore.sql.gz
   ```
2. 덤프를 `mysql-0` 파드로 보내 적재한다.
   ```bash
   gzip -dc /tmp/restore.sql.gz | \
     kubectl -n do4i exec -i mysql-0 -- sh -c 'mysql -uroot -p"$MYSQL_ROOT_PASSWORD"'
   ```
3. `api` 파드를 재시작해 새 데이터로 수렴시키고, 대표 `/api` 응답과 로그를 확인한다.

주의: 백업 파일은 `--databases do4i`로 떠서 `CREATE DATABASE`/`USE`를 포함하므로 대상 DB를 지정하지 않아도 `do4i` 스키마로 적재된다.

## 한계와 후속 과제

- ⚠️ 복제(replication)는 백업이 아니다. 운영에서의 실수 삭제는 복제본에도 그대로 전파되므로, prod→dev(77→81) 복제를 붙이더라도 이 S3 백업과 병행해야 한다.
- 시점 단위 복구(PITR, binlog 적재)는 구성하지 않았다. 회복 단위는 6시간 스냅샷이다.

## 참고

- 상세 정책은 `do4ai/platform` 레포 `sdd/01_planning/06_iac/do4i_db_backup_policy.md`에 있다.
- 시크릿 관리는 `Manual`의 Infisical 사용법, 그리고 do4i [1. 아키텍처와 배포](../1. 아키텍처와 배포/index.md)를 참고한다.
