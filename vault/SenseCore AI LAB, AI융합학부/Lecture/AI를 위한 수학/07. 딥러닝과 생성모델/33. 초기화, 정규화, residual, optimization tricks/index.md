---
title: "33. 초기화, 정규화, residual, optimization tricks"
---
# 33강. 초기화, 정규화, residual, optimization tricks

이 강의의 목표는 깊은 신경망이 안정적으로 학습되도록 돕는 세 가지 기법, 즉 초기화, 정규화, residual 연결을 수식으로 이해하는 것입니다.

먼저 오늘의 핵심 식을 봅니다.

$$
h_{l+1}=h_l+F(h_l)
$$

이 식을 외우기 전에, 식 안의 말과 기호를 먼저 하나씩 풀어야 합니다.

# 1. 먼저 오늘 쓸 말을 정리하자

| 말 | 뜻 |
|---|---|
| $h_l$ | $l$번째 층의 값(활성값) |
| $F(h_l)$ | 그 층이 학습하는 변환(예: 선형 + 비선형) |
| residual 연결 | 입력 $h_l$을 변환 결과 $F(h_l)$에 더하는 구조 |
| 초기화 | 학습 시작 전 가중치를 정하는 방법 |
| 정규화 | 층의 값 분포를 안정적으로 맞추는 방법 |
| 기울기 소실 | 기울기가 층을 지나며 너무 작아지는 문제 |
| 기울기 폭발 | 기울기가 층을 지나며 너무 커지는 문제 |

수학에서 어려운 부분은 계산보다 읽기입니다. 뜻을 모르고 계산하면 공식이 암호처럼 보입니다.

# 2. 먼저 떠올릴 장면

아주 긴 전달 게임에서 말이 뒤로 갈수록 조금씩 작아지면, 마지막 사람에게는 거의 아무것도 남지 않습니다. 깊은 신경망에서도 기울기가 층을 지날 때마다 곱해지면서, 뒤로 갈수록 0에 가까워지거나 반대로 폭발할 수 있습니다.

# 3. 핵심 식을 천천히 읽어 보자

이제 핵심 식에 실제 기호를 넣어 읽어 봅니다.

$$
h_{l+1}=h_l+F(h_l)
$$

- $h_l$: 지금 층으로 들어온 값입니다.
- $F(h_l)$: 이 층이 새로 배우는 변화분입니다.
- $h_{l+1}=h_l+F(h_l)$: 다음 층의 값은 "들어온 값 그대로"에 "새로 배운 변화분"을 더한 것입니다.

보통의 층은 $h_{l+1}=F(h_l)$처럼 입력을 통째로 바꿔 버립니다. 반면 residual 연결은 입력 $h_l$을 그대로 통과시키는 지름길을 하나 두고, $F$에게는 "얼마나 바꿀지"라는 차이만 배우게 합니다. 이 지름길이 기울기를 안전하게 뒤로 흘려보냅니다.

# 4. 왜 이런 생각이 필요한가

층을 깊게 쌓을수록 표현력은 커지지만, 학습은 오히려 불안정해집니다. 층을 지날 때마다 신호와 기울기가 일정 비율로 곱해지는데, 그 비율이 1보다 작으면 신호가 사라지고 1보다 크면 폭발하기 때문입니다.

그래서 세 가지 장치를 함께 씁니다. 초기화는 학습 시작 시점에 이 비율이 대략 1이 되도록 가중치의 분산을 맞춥니다. 정규화는 학습 도중 각 층의 값 분포를 다시 안정적으로 맞춥니다. residual 연결은 기울기가 지나가는 지름길을 만들어 소실을 막습니다. 이 세 장치가 없으면 수십 층짜리 모델은 사실상 학습되지 않습니다.

# 5. residual 연결의 기울기를 유도하기

핵심 식을 $h_l$로 미분해 봅니다.

$$
\frac{\partial h_{l+1}}{\partial h_l}
=\frac{\partial}{\partial h_l}\bigl(h_l+F(h_l)\bigr)
=1+\frac{\partial F(h_l)}{\partial h_l}
$$

여기서 나온 $+1$이 핵심입니다. 역전파에서 층 $0$까지 기울기를 전달하려면 각 층의 미분을 모두 곱해야 합니다.

**residual이 없을 때** 한 층의 미분이 $\dfrac{\partial F}{\partial h_l}$이라면, $L$개 층을 지나며

$$
\frac{\partial h_L}{\partial h_0}=\prod_{l=0}^{L-1}\frac{\partial F(h_l)}{\partial h_l}
$$

이 됩니다. 각 항이 예를 들어 $0.1$이라면 $10$개 층을 지나면

$$
0.1^{10}=10^{-10}
$$

으로 기울기가 사실상 0이 됩니다. 이것이 기울기 소실입니다.

**residual이 있을 때** 각 층의 미분은 $1+\dfrac{\partial F}{\partial h_l}$이므로

$$
\frac{\partial h_L}{\partial h_0}=\prod_{l=0}^{L-1}\left(1+\frac{\partial F(h_l)}{\partial h_l}\right)
$$

이 됩니다. 같은 값 $\dfrac{\partial F}{\partial h_l}=0.1$을 넣으면

$$
(1+0.1)^{10}=1.1^{10}\approx 2.59
$$

로, $F$의 기울기가 아무리 작아도 지름길이 만든 $1$ 덕분에 전체 곱이 0으로 죽지 않습니다. 최소한 입력 $h_l$의 기울기는 항상 그대로 뒤로 전달됩니다. 이것이 residual 연결이 기울기 소실을 완화하는 이유입니다.

# 6. 예제 1: 초기화의 분산식

층이 $z=\sum_{i=1}^{n_\text{in}} w_i x_i$처럼 $n_\text{in}$개의 입력을 가중합한다고 합시다. 입력과 가중치가 서로 독립이고 평균 0이면, 출력의 분산은

$$
\operatorname{Var}(z)=n_\text{in}\,\operatorname{Var}(w)\,\operatorname{Var}(x)
$$

입니다. 출력의 분산이 입력의 분산과 같아지려면, 즉 층을 지나도 신호 크기가 유지되려면

$$
n_\text{in}\,\operatorname{Var}(w)=1
\quad\Longrightarrow\quad
\operatorname{Var}(w)=\frac{1}{n_\text{in}}
$$

이어야 합니다. 이것이 **Xavier(Glorot) 초기화**입니다. 순전파와 역전파를 함께 고려하면 입력 수와 출력 수의 평균을 써서

$$
\operatorname{Var}(w)=\frac{2}{n_\text{in}+n_\text{out}}
$$

로 둡니다.

$\operatorname{ReLU}$를 쓰면 음수 절반이 0으로 잘려 나가 분산이 절반이 됩니다. 이를 보정하려면 분산을 두 배로 키워야 하므로

$$
\operatorname{Var}(w)=\frac{2}{n_\text{in}}
$$

로 둡니다. 이것이 **He 초기화**입니다. 예를 들어 입력이 $n_\text{in}=100$개인 $\operatorname{ReLU}$ 층은 $\operatorname{Var}(w)=0.02$, 즉 표준편차 약 $0.141$로 가중치를 뽑으면 됩니다.

# 7. 예제 2: 정규화 수식(BatchNorm과 LayerNorm)

정규화는 층의 값 $x$를 평균 0, 분산 1로 맞춘 뒤, 학습되는 두 수 $\gamma$(스케일)와 $\beta$(이동)로 다시 조정합니다.

$$
\hat{x}=\frac{x-\mu}{\sqrt{\sigma^2+\varepsilon}},\qquad
y=\gamma\,\hat{x}+\beta
$$

- $\mu$: 값들의 평균
- $\sigma^2$: 값들의 분산
- $\varepsilon$: 분모가 0이 되지 않게 더하는 아주 작은 수
- $\gamma,\ \beta$: 정규화한 값을 다시 늘이거나 옮기는 학습 파라미터

**BatchNorm**은 미니배치 안의 같은 채널 값들로 $\mu$와 $\sigma^2$를 구합니다. **LayerNorm**은 한 샘플 안의 특징들로 $\mu$와 $\sigma^2$를 구합니다. 후자는 배치 크기에 영향받지 않아 트랜스포머 같은 모델에서 주로 쓰입니다.

작은 예로 $x=(1,2,3)$을 LayerNorm 한다고 하면

$$
\mu=\frac{1+2+3}{3}=2,\qquad
\sigma^2=\frac{(1-2)^2+(2-2)^2+(3-2)^2}{3}=\frac{2}{3}\approx 0.667
$$

이고, $\varepsilon$을 무시하면

$$
\hat{x}=\left(\frac{1-2}{\sqrt{0.667}},\ 0,\ \frac{3-2}{\sqrt{0.667}}\right)\approx(-1.225,\ 0,\ 1.225)
$$

가 됩니다. 값이 평균 0, 분산 1로 맞춰졌고, 이후 $\gamma$와 $\beta$로 모델이 필요한 크기로 되돌립니다.

# 8. 한 줄씩 다시 요약하기

- residual 연결 $h_{l+1}=h_l+F(h_l)$은 입력을 그대로 통과시키는 지름길이다.
- 그 미분은 $1+\dfrac{\partial F}{\partial h_l}$이라 $+1$이 항상 남아 기울기 소실을 막는다.
- 층을 여러 개 지날 때 residual이 없으면 $0.1^{10}$처럼 죽고, 있으면 $1.1^{10}$처럼 살아 있다.
- Xavier 초기화는 $\operatorname{Var}(w)=1/n_\text{in}$, He 초기화는 $\operatorname{Var}(w)=2/n_\text{in}$이다.
- 정규화는 $\dfrac{x-\mu}{\sqrt{\sigma^2+\varepsilon}}\gamma+\beta$로 분포를 안정화한다.
- BatchNorm은 배치로, LayerNorm은 한 샘플의 특징으로 통계를 구한다.
- 핵심 식은 다음과 같습니다.

$$
h_{l+1}=h_l+F(h_l)
$$

# 9. 스스로 점검

- $\dfrac{\partial h_{l+1}}{\partial h_l}=1+\dfrac{\partial F}{\partial h_l}$에서 $+1$이 왜 기울기 소실을 막는지 설명할 수 있는가?
- $\operatorname{ReLU}$ 층에서 He 초기화가 Xavier보다 분산을 두 배로 두는 이유는 무엇인가?
- BatchNorm과 LayerNorm은 각각 어느 축으로 $\mu$와 $\sigma^2$를 구하는가?
