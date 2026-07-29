---
title: "35. variational inference, ELBO, VAE"
---
# 35강. variational inference, ELBO, VAE

이 강의의 목표는 직접 구하기 어려운 데이터 확률 $\log p(x)$를, 쉬운 분포로 근사해 최적화하는 방법과 그 아래 경계인 ELBO를 수식으로 이해하는 것입니다.

먼저 오늘의 핵심 식을 봅니다.

$$
\log p(x)\ge \mathbb{E}_{q(z\mid x)}\bigl[\log p(x,z)-\log q(z\mid x)\bigr]
$$

이 식을 외우기 전에, 식 안의 말과 기호를 먼저 하나씩 풀어야 합니다.

# 1. 먼저 오늘 쓸 말을 정리하자

| 말 | 뜻 |
|---|---|
| $x$ | 관찰한 데이터(예: 이미지) |
| $z$ | 관찰 뒤에 숨어 있다고 보는 잠재변수 |
| $p(x,z)$ | 데이터와 잠재변수의 결합확률 |
| $p(z\mid x)$ | 데이터를 본 뒤의 잠재변수 분포(posterior). 구하기 어렵다 |
| $q(z\mid x)$ | posterior를 흉내 내는 쉬운 근사 분포 |
| ELBO | $\log p(x)$의 아래 경계(Evidence Lower BOund) |
| VAE | encoder $q$와 decoder $p$로 데이터를 생성하는 모델 |

수학에서 어려운 부분은 계산보다 읽기입니다. 뜻을 모르고 계산하면 공식이 암호처럼 보입니다.

# 2. 먼저 떠올릴 장면

얼굴 사진에는 표정, 조명, 방향 같은 숨은 요인이 있습니다. 이것들을 정확히 알기는 어렵지만 그럴듯한 범위를 추정할 수는 있습니다. VAE는 이런 숨은 공간 $z$를 배우고, 그 공간에서 새 얼굴을 만들어 냅니다.

# 3. 핵심 식을 천천히 읽어 보자

핵심 식의 오른쪽을 ELBO라고 부릅니다.

$$
\text{ELBO}=\mathbb{E}_{q(z\mid x)}\bigl[\log p(x,z)-\log q(z\mid x)\bigr]
$$

- $\mathbb{E}_{q(z\mid x)}[\cdot]$: 근사 분포 $q$에서 $z$를 뽑아 평균을 낸다는 뜻입니다.
- $\log p(x,z)$: 뽑은 $z$와 데이터 $x$가 함께 나타날 로그확률. 클수록 그 $z$가 데이터를 잘 설명합니다.
- $-\log q(z\mid x)$: 그 $z$를 얼마나 확신했는지에 대한 벌점. $q$가 한 점에 몰리지 않도록 퍼뜨립니다.

핵심 식은 "직접 구하기 어려운 $\log p(x)$가, 우리가 계산할 수 있는 ELBO보다 항상 크거나 같다"고 말합니다. 그래서 $\log p(x)$를 직접 키우는 대신 ELBO를 키우면 됩니다.

# 4. 왜 이런 생각이 필요한가

데이터의 확률 $p(x)$는 모든 가능한 잠재변수를 적분해야 나옵니다.

$$
p(x)=\int p(x,z)\,dz
$$

$z$가 고차원이면 이 적분은 사실상 계산할 수 없습니다. posterior $p(z\mid x)=\dfrac{p(x,z)}{p(x)}$도 분모에 같은 적분이 들어 있어 구할 수 없습니다.

그래서 posterior를 직접 구하는 대신, 다루기 쉬운 분포 $q(z\mid x)$(예: 정규분포)로 흉내 냅니다. 이것이 variational inference입니다. 그리고 계산 불가능한 $\log p(x)$ 대신, 계산 가능한 아래 경계 ELBO를 최대화합니다. VAE는 $q$를 신경망 encoder로, $p(x\mid z)$를 신경망 decoder로 두어 이 아이디어를 실제 모델로 만든 것입니다.

# 5. ELBO 부등식 유도하기

$\log p(x)$는 $z$와 무관하므로, $q(z\mid x)$로 평균을 내도 값이 그대로입니다.

$$
\log p(x)=\mathbb{E}_{q(z\mid x)}\bigl[\log p(x)\bigr]
$$

여기에 $p(x)=\dfrac{p(x,z)}{p(z\mid x)}$를 넣습니다.

$$
\log p(x)=\mathbb{E}_{q}\!\left[\log\frac{p(x,z)}{p(z\mid x)}\right]
$$

분자·분모에 $q(z\mid x)$를 곱하고 나눠 두 덩어리로 가릅니다.

$$
\log p(x)
=\mathbb{E}_{q}\!\left[\log\frac{p(x,z)}{q(z\mid x)}\right]
+\mathbb{E}_{q}\!\left[\log\frac{q(z\mid x)}{p(z\mid x)}\right]
$$

앞 항이 ELBO이고, 뒤 항은 $q$와 posterior의 KL 발산입니다.

$$
\log p(x)=\underbrace{\mathbb{E}_{q}\bigl[\log p(x,z)-\log q(z\mid x)\bigr]}_{\text{ELBO}}
+\underbrace{\operatorname{KL}\!\bigl(q(z\mid x)\,\|\,p(z\mid x)\bigr)}_{\ge 0}
$$

KL 발산은 항상 0 이상이므로

$$
\log p(x)\ge \text{ELBO}
$$

가 됩니다. 이것이 핵심 식입니다. 또한 이 분해는 ELBO를 키우는 것이 곧 근사 $q$를 진짜 posterior에 가깝게(KL을 줄이는) 만드는 것과 같음을 보여 줍니다.

> 참고: KL이 0 이상이라는 사실은 젠슨 부등식 $\log \mathbb{E}[Y]\ge \mathbb{E}[\log Y]$에서도 곧바로 나옵니다. $\log p(x)=\log\mathbb{E}_q\!\left[\frac{p(x,z)}{q(z\mid x)}\right]\ge \mathbb{E}_q\!\left[\log\frac{p(x,z)}{q(z\mid x)}\right]=\text{ELBO}$입니다.

# 6. 예제 1: reparameterization trick

ELBO 안의 기댓값 $\mathbb{E}_{q(z\mid x)}[\cdot]$은 $z$를 $q$에서 뽑아 계산합니다. 그런데 "뽑기"는 무작위라서, 그대로는 encoder의 파라미터에 대해 미분할 수 없습니다.

이를 해결하려고, encoder가 평균 $\mu$와 표준편차 $\sigma$를 내보내게 하고, 무작위성은 바깥에서 뽑은 $\varepsilon$에만 맡깁니다.

$$
z=\mu+\sigma\odot\varepsilon,\qquad \varepsilon\sim\mathcal{N}(0,I)
$$

- $\odot$: 성분별 곱
- $\varepsilon$: 표준정규에서 뽑은 잡음. 파라미터와 무관합니다.

이제 $z$는 $\mu$와 $\sigma$의 매끄러운 함수라, $\mu$와 $\sigma$에 대해 미분이 흘러갈 수 있습니다. 무작위 뽑기를 결정적 계산과 바깥 잡음으로 분리한 것입니다. 예를 들어 $\mu=2$, $\sigma=0.5$이고 뽑힌 $\varepsilon=1$이면 $z=2+0.5\cdot 1=2.5$이며, 이 경로로 기울기가 $\mu$, $\sigma$까지 전달됩니다.

# 7. 예제 2: VAE 손실

ELBO를 다시 두 조각으로 정리하면 VAE의 손실이 됩니다. $\log p(x,z)=\log p(x\mid z)+\log p(z)$를 넣으면

$$
\text{ELBO}
=\underbrace{\mathbb{E}_{q(z\mid x)}\bigl[\log p(x\mid z)\bigr]}_{\text{재구성}}
-\underbrace{\operatorname{KL}\!\bigl(q(z\mid x)\,\|\,p(z)\bigr)}_{\text{정리}}
$$

가 됩니다. 학습에서는 ELBO를 최대화, 즉 그 음수를 최소화하므로 VAE 손실은

$$
\mathcal{L}_{\text{VAE}}
=\underbrace{\mathbb{E}_{q(z\mid x)}\bigl[-\log p(x\mid z)\bigr]}_{\text{재구성 손실}}
+\underbrace{\operatorname{KL}\!\bigl(q(z\mid x)\,\|\,p(z)\bigr)}_{\text{KL 정칙화}}
$$

입니다.

- **재구성 손실**: decoder가 $z$로부터 원본 $x$를 얼마나 잘 복원하는가. 잘 복원할수록 작아집니다.
- **KL 정칙화**: encoder의 분포 $q(z\mid x)$가 사전분포 $p(z)=\mathcal{N}(0,I)$에서 너무 벗어나지 않게 붙잡습니다.

사전분포와 근사 분포가 모두 정규분포일 때 KL 항은 닫힌 식으로 나옵니다. 잠재차원 $d$에 대해

$$
\operatorname{KL}\!\bigl(\mathcal{N}(\mu,\sigma^2 I)\,\|\,\mathcal{N}(0,I)\bigr)
=\frac12\sum_{i=1}^{d}\bigl(\mu_i^2+\sigma_i^2-1-\log\sigma_i^2\bigr)
$$

입니다. 두 손실이 균형을 이루어야, 잠재공간이 매끄럽게 정리되면서도 데이터를 잘 복원하는 모델이 됩니다.

# 8. 한 줄씩 다시 요약하기

- $p(x)=\int p(x,z)\,dz$와 posterior $p(z\mid x)$는 직접 구하기 어렵다.
- 그래서 쉬운 $q(z\mid x)$로 posterior를 근사한다(variational inference).
- $\log p(x)=\text{ELBO}+\operatorname{KL}(q\|p(z\mid x))$이고 KL$\ge 0$이라 $\log p(x)\ge\text{ELBO}$이다.
- 그래서 계산 불가능한 $\log p(x)$ 대신 ELBO를 최대화한다.
- reparameterization trick $z=\mu+\sigma\odot\varepsilon$으로 무작위 뽑기를 미분 가능하게 만든다.
- VAE 손실은 재구성 손실 + KL 정칙화다.
- 핵심 식은 다음과 같습니다.

$$
\log p(x)\ge \mathbb{E}_{q(z\mid x)}\bigl[\log p(x,z)-\log q(z\mid x)\bigr]
$$

# 9. 스스로 점검

- $\log p(x)=\text{ELBO}+\operatorname{KL}(q\|p(z\mid x))$ 분해를 직접 유도할 수 있는가?
- KL이 0 이상이라는 사실이 왜 ELBO를 아래 경계로 만드는가?
- reparameterization trick이 없으면 왜 encoder를 미분으로 학습할 수 없는가?
