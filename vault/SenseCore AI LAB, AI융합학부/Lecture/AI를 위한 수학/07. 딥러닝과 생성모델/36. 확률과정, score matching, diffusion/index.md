---
title: "36. 확률과정, score matching, diffusion"
---
# 36강. 확률과정, score matching, diffusion

이 강의의 목표는 데이터에 노이즈를 조금씩 더하는 정방향 과정과, 그것을 거꾸로 지워 데이터를 만드는 역방향 과정을 수식으로 이해하는 것입니다.

먼저 오늘의 핵심 식을 봅니다.

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon,\qquad \varepsilon\sim\mathcal{N}(0,I)
$$

이 식을 외우기 전에, 식 안의 말과 기호를 먼저 하나씩 풀어야 합니다.

# 1. 먼저 오늘 쓸 말을 정리하자

| 말 | 뜻 |
|---|---|
| $x_0$ | 원본 데이터(예: 깨끗한 이미지) |
| $x_t$ | $t$단계만큼 노이즈를 더한 데이터 |
| $\varepsilon$ | 표준정규에서 뽑은 노이즈 |
| $\bar\alpha_t$ | $0$과 $1$ 사이의 스케줄 값. $t$가 커질수록 0에 가까워진다 |
| score | 로그확률밀도의 기울기 $\nabla_x\log p(x)$ |
| 역과정 | 노이즈에서 데이터로 돌아가는 과정 |

수학에서 어려운 부분은 계산보다 읽기입니다. 뜻을 모르고 계산하면 공식이 암호처럼 보입니다.

# 2. 먼저 떠올릴 장면

깨끗한 그림에 먼지를 조금씩 뿌리면 결국 원래 그림이 안 보입니다. diffusion 모델은 먼지를 뿌리는 쉬운 과정을 정해 두고, 거꾸로 먼지를 지우는 어려운 과정을 학습합니다. 학습이 끝나면 순수한 먼지에서 시작해 그림을 만들어 냅니다.

# 3. 핵심 식을 천천히 읽어 보자

핵심 식에 실제 기호를 넣어 읽어 봅니다.

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon
$$

- $\sqrt{\bar\alpha_t}\,x_0$: 원본을 조금 줄여서 남긴 부분. $t$가 커지면 $\bar\alpha_t$가 작아져 원본이 희미해집니다.
- $\sqrt{1-\bar\alpha_t}\,\varepsilon$: 더해지는 노이즈. $t$가 커지면 계수가 커져 노이즈가 지배합니다.
- 두 계수의 제곱을 더하면 $\bar\alpha_t+(1-\bar\alpha_t)=1$이라, 전체 신호의 크기(분산)가 일정하게 유지됩니다.

즉 $x_t$는 "원본 $x_0$"와 "노이즈 $\varepsilon$"를 정해진 비율로 섞은 것입니다. $t=0$에서는 원본 그대로이고, $t$가 아주 크면 $\bar\alpha_t\to 0$이라 $x_t\approx\varepsilon$, 즉 거의 순수한 노이즈가 됩니다.

# 4. 왜 이런 생각이 필요한가

데이터의 분포 $p(x)$를 직접 모델링해 새 샘플을 뽑는 일은 어렵습니다. 그런데 노이즈를 더하는 정방향 과정은 아주 쉽습니다. 위 핵심 식 하나로 어느 단계 $x_t$든 바로 만들 수 있기 때문입니다.

그래서 diffusion은 문제를 뒤집습니다. 쉬운 정방향 과정을 정해 두고, 모델에게는 "노이즈를 한 단계 지우는 방향"만 배우게 합니다. 이 방향이 바로 score, 즉 로그확률밀도가 커지는 쪽입니다. 데이터 분포 전체를 한 번에 배우는 대신, 각 노이즈 수준에서 국소적으로 "어디로 가야 더 그럴듯한가"만 배우면 되므로 학습이 안정적입니다.

# 5. score와 정방향 과정 정의

score는 확률밀도에 로그를 씌운 뒤 위치로 미분한 벡터입니다.

$$
s(x)=\nabla_x\log p(x)
$$

이 벡터는 "확률이 커지는 방향", 즉 더 그럴듯한 데이터 쪽을 가리킵니다. 밀도가 높은 곳으로 올라가는 나침반이라고 볼 수 있습니다.

정방향 과정에서 $x_t$는 $x_0$이 주어지면 정규분포를 따릅니다.

$$
p(x_t\mid x_0)=\mathcal{N}\!\bigl(x_t;\ \sqrt{\bar\alpha_t}\,x_0,\ (1-\bar\alpha_t)I\bigr)
$$

이것이 핵심 식과 같은 말입니다. 평균이 $\sqrt{\bar\alpha_t}\,x_0$, 분산이 $1-\bar\alpha_t$인 정규분포에서 $x_t$를 뽑는 것이 곧 $x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon$입니다.

# 6. 예제 1: 정방향 과정을 숫자로 보기

스칼라 예로 원본을 $x_0=1$, 노이즈를 $\varepsilon=0.5$로 두고 세 시점을 봅니다.

**이른 시점** $\bar\alpha_t=0.81$일 때 $\sqrt{0.81}=0.9$, $\sqrt{1-0.81}=\sqrt{0.19}\approx 0.436$이므로

$$
x_t=0.9\cdot 1+0.436\cdot 0.5\approx 1.12
$$

원본 $1$에서 크게 벗어나지 않았습니다.

**중간 시점** $\bar\alpha_t=0.36$일 때 $\sqrt{0.36}=0.6$, $\sqrt{0.64}=0.8$이므로

$$
x_t=0.6\cdot 1+0.8\cdot 0.5=0.6+0.4=1.0
$$

원본과 노이즈가 비슷한 비중으로 섞였습니다.

**늦은 시점** $\bar\alpha_t=0.01$일 때 $\sqrt{0.01}=0.1$, $\sqrt{0.99}\approx 0.995$이므로

$$
x_t=0.1\cdot 1+0.995\cdot 0.5\approx 0.60
$$

이제 값의 대부분이 노이즈에서 옵니다. $\bar\alpha_t$가 0으로 갈수록 $x_t$는 표준정규 노이즈에 가까워집니다.

# 7. 예제 2: score matching / denoising 목적함수와 역과정

정방향 분포가 정규분포이므로 그 score를 손으로 구할 수 있습니다. $\log p(x_t\mid x_0)=-\dfrac{\lVert x_t-\sqrt{\bar\alpha_t}\,x_0\rVert^2}{2(1-\bar\alpha_t)}+\text{상수}$를 $x_t$로 미분하면

$$
\nabla_{x_t}\log p(x_t\mid x_0)
=-\frac{x_t-\sqrt{\bar\alpha_t}\,x_0}{1-\bar\alpha_t}
=-\frac{\varepsilon}{\sqrt{1-\bar\alpha_t}}
$$

가 됩니다(마지막 등식은 핵심 식에서 $x_t-\sqrt{\bar\alpha_t}\,x_0=\sqrt{1-\bar\alpha_t}\,\varepsilon$이기 때문입니다). 즉 **score는 더해진 노이즈 $\varepsilon$과 부호만 다른, 비례하는 방향**입니다.

**score matching**은 모델 $s_\theta$가 이 진짜 score를 맞히도록 학습합니다.

$$
\mathcal{L}_{\text{score}}
=\mathbb{E}\Bigl[\bigl\lVert s_\theta(x_t,t)-\nabla_{x_t}\log p(x_t\mid x_0)\bigr\rVert^2\Bigr]
$$

score가 노이즈와 비례하므로, 실제로는 모델이 노이즈 $\varepsilon$을 직접 예측하도록 두는 편이 간단합니다. 이것이 **denoising 목적함수**입니다.

$$
\mathcal{L}_{\text{denoise}}
=\mathbb{E}_{x_0,\varepsilon,t}\Bigl[\bigl\lVert \varepsilon-\varepsilon_\theta(x_t,t)\bigr\rVert^2\Bigr]
$$

모델 $\varepsilon_\theta$는 "지금 $x_t$에 섞인 노이즈가 무엇인지"를 예측합니다.

**역과정**은 이 예측을 이용해 노이즈를 한 단계씩 덜어 냅니다. 순수 노이즈 $x_T\sim\mathcal{N}(0,I)$에서 시작해, 각 단계에서 예측한 $\varepsilon_\theta$(또는 score)만큼 더 그럴듯한 방향으로 조금 이동하며 $x_{t}\to x_{t-1}$로 되돌립니다. 이 과정을 $T$부터 $0$까지 반복하면 노이즈가 점점 걷히고, 마지막에 새로운 데이터 $x_0$이 나타납니다.

# 8. 한 줄씩 다시 요약하기

- 정방향 과정 $x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon$은 원본과 노이즈를 정해진 비율로 섞는다.
- $\bar\alpha_t$가 0으로 갈수록 $x_t$는 순수 노이즈에 가까워진다.
- score $\nabla_x\log p(x)$는 더 그럴듯한 데이터 쪽을 가리키는 방향이다.
- 정방향이 정규분포라, score는 더해진 노이즈 $\varepsilon$과 비례한다.
- 모델은 score를 맞히거나(노이즈 $\varepsilon$을 예측해) denoising 손실을 줄이도록 학습한다.
- 역과정은 순수 노이즈에서 시작해 예측한 노이즈를 단계적으로 지워 데이터를 만든다.
- 핵심 식은 다음과 같습니다.

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon
$$

# 9. 스스로 점검

- 정방향 식에서 두 계수의 제곱을 더하면 왜 1이 되고, 그것이 무엇을 뜻하는가?
- score $\nabla_{x_t}\log p(x_t\mid x_0)$가 왜 노이즈 $\varepsilon$과 비례하는지 유도할 수 있는가?
- denoising 목적함수 $\lVert\varepsilon-\varepsilon_\theta\rVert^2$를 줄이는 것이 왜 역과정 학습이 되는가?
