---
title: "32. 신경망, 계산그래프, backprop"
---
# 32강. 신경망, 계산그래프, backprop

이 강의의 목표는 신경망을 작은 계산들의 연결로 보고, 역전파가 어떻게 미분을 뒤에서 앞으로 전달하는지 아주 기초부터 이해하는 것입니다.

먼저 오늘의 핵심 식을 봅니다.

$$
\frac{\partial L}{\partial w}=\frac{\partial L}{\partial y}\frac{\partial y}{\partial w}
$$

이 식을 외우기 전에, 식 안의 말과 기호를 먼저 하나씩 풀어야 합니다.

# 1. 먼저 오늘 쓸 말을 정리하자

| 말 | 뜻 |
|---|---|
| 신경망 | 작은 함수들을 층으로 쌓은 모델 |
| 뉴런 | 가중합과 비선형 변환을 하는 단위 |
| 계산그래프 | 계산 순서를 화살표로 나타낸 그림 |
| 손실 $L$ | 예측이 정답과 얼마나 다른지를 하나의 숫자로 나타낸 값 |
| 가중치 $w$ | 입력에 곱해지는, 학습으로 조정되는 수 |
| 역전파 | 미분을 뒤에서 앞으로 전달하는 알고리즘 |

수학에서 어려운 부분은 계산보다 읽기입니다. 뜻을 모르고 계산하면 공식이 암호처럼 보입니다.

# 2. 먼저 떠올릴 장면

공장 조립 라인에서 마지막 제품에 문제가 있으면, 어느 단계가 얼마나 영향을 줬는지 거꾸로 추적해야 합니다. 역전파도 마지막에 나온 손실에서 시작해, 앞 단계의 계산으로 원인을 거꾸로 추적합니다.

# 3. 핵심 식을 천천히 읽어 보자

이제 핵심 식에 실제 기호를 넣어 읽어 봅니다.

$$
\frac{\partial L}{\partial w}=\frac{\partial L}{\partial y}\frac{\partial y}{\partial w}
$$

- $\dfrac{\partial L}{\partial w}$: 가중치 $w$를 아주 조금 바꿀 때 손실 $L$이 얼마나 바뀌는가.
- $\dfrac{\partial L}{\partial y}$: 출력 $y$를 아주 조금 바꿀 때 손실 $L$이 얼마나 바뀌는가.
- $\dfrac{\partial y}{\partial w}$: 가중치 $w$를 아주 조금 바꿀 때 출력 $y$가 얼마나 바뀌는가.

핵심은 이것입니다. 손실 $L$은 가중치 $w$에 직접 매달려 있지 않고, 중간에 있는 출력 $y$를 거쳐서만 $w$와 연결됩니다.

$$
w \;\longrightarrow\; y \;\longrightarrow\; L
$$

그래서 $w$가 $L$에 주는 영향은 "$w$가 $y$에 주는 영향"과 "$y$가 $L$에 주는 영향"을 곱한 것입니다. 이것이 바로 연쇄법칙입니다.

# 4. 왜 이런 생각이 필요한가

신경망에는 가중치가 수백만 개 있습니다. 이 가중치 하나하나가 손실을 얼마나 바꾸는지 알아야, 손실이 줄어드는 방향으로 가중치를 조금씩 고칠 수 있습니다.

만약 가중치마다 손실을 처음부터 다시 계산해서 기울기를 구한다면, 계산량이 감당할 수 없이 커집니다. 그런데 연쇄법칙을 쓰면, 뒤 층에서 이미 구한 $\dfrac{\partial L}{\partial y}$를 앞 층이 그대로 받아서 자기 몫만 곱하면 됩니다. 즉 한 번의 뒤로 가는 계산으로 모든 가중치의 기울기를 얻습니다. 역전파가 필요한 이유가 바로 이것입니다.

# 5. 연쇄법칙으로 핵심 식 유도하기

손실 $L$이 출력 $y$의 함수이고, 출력 $y$가 가중치 $w$의 함수라고 합시다.

$$
y=y(w),\qquad L=L(y)
$$

가중치를 $w$에서 $w+\Delta w$로 아주 조금 바꾸면, 출력이 다음만큼 바뀝니다.

$$
\Delta y \approx \frac{\partial y}{\partial w}\,\Delta w
$$

그리고 출력이 $\Delta y$만큼 바뀌면, 손실이 다음만큼 바뀝니다.

$$
\Delta L \approx \frac{\partial L}{\partial y}\,\Delta y
$$

두 식을 이어 붙이면

$$
\Delta L \approx \frac{\partial L}{\partial y}\,\frac{\partial y}{\partial w}\,\Delta w
$$

입니다. 양변을 $\Delta w$로 나누고 아주 작게 보내면

$$
\frac{\partial L}{\partial w}=\frac{\partial L}{\partial y}\frac{\partial y}{\partial w}
$$

가 됩니다. 중간 변수가 여러 개면 같은 방법을 반복해서 곱을 늘리면 됩니다.

$$
\frac{\partial L}{\partial w}=\frac{\partial L}{\partial y}\frac{\partial y}{\partial a}\frac{\partial a}{\partial z}\frac{\partial z}{\partial w}
$$

# 6. 예제 1: 2층 신경망 한 스텝을 손으로 계산하기

작은 신경망을 하나 정합니다. 입력은 $x=1$이고, 두 층으로 되어 있습니다.

**1층(은닉층):**

$$
z_1=w_1 x+b_1,\qquad a_1=\operatorname{ReLU}(z_1)=\max(0,z_1)
$$

**2층(출력층):**

$$
y=w_2 a_1+b_2
$$

**손실(제곱오차):**

$$
L=\tfrac12 (y-t)^2
$$

가중치와 정답을 다음처럼 둡니다.

$$
w_1=2,\quad b_1=0,\quad w_2=3,\quad b_2=1,\quad t=5
$$

## 순전파

$$
z_1=2\cdot 1+0=2,\qquad a_1=\operatorname{ReLU}(2)=2
$$

$$
y=3\cdot 2+1=7
$$

$$
L=\tfrac12 (7-5)^2=\tfrac12\cdot 4=2
$$

## 역전파

먼저 출력에서 손실의 기울기를 구합니다.

$$
\frac{\partial L}{\partial y}=y-t=7-5=2
$$

출력층 가중치 $w_2$로 갑니다. $\dfrac{\partial y}{\partial w_2}=a_1=2$이므로

$$
\frac{\partial L}{\partial w_2}=\frac{\partial L}{\partial y}\frac{\partial y}{\partial w_2}=2\cdot 2=4
$$

입력층 가중치 $w_1$은 $y \to a_1 \to z_1 \to w_1$을 거칩니다. 각 조각은

$$
\frac{\partial y}{\partial a_1}=w_2=3,\qquad
\frac{\partial a_1}{\partial z_1}=1\ (\because z_1>0),\qquad
\frac{\partial z_1}{\partial w_1}=x=1
$$

이므로 연쇄법칙으로 곱합니다.

$$
\frac{\partial L}{\partial w_1}
=\frac{\partial L}{\partial y}\frac{\partial y}{\partial a_1}\frac{\partial a_1}{\partial z_1}\frac{\partial z_1}{\partial w_1}
=2\cdot 3\cdot 1\cdot 1=6
$$

## 가중치 갱신

학습률을 $\eta=0.1$로 두고 기울기 반대 방향으로 한 스텝 갑니다.

$$
w_2 \leftarrow 3-0.1\cdot 4=2.6
$$

$$
w_1 \leftarrow 2-0.1\cdot 6=1.4
$$

바뀐 가중치로 다시 순전파하면 $z_1=1.4$, $a_1=1.4$, $y=2.6\cdot 1.4+1=4.64$, $L=\tfrac12(4.64-5)^2\approx 0.065$가 되어 손실이 $2$에서 크게 줄어듭니다. 한 스텝의 역전파가 실제로 손실을 낮춘 것입니다.

# 7. 예제 2: 비선형성이 없으면 왜 층을 쌓아도 소용없는가

방금 예제에서 $\operatorname{ReLU}$를 뺀다고 합시다. 그러면 두 층은 다음처럼 됩니다.

$$
a_1=W_1 x,\qquad y=W_2 a_1
$$

$a_1$을 대입하면

$$
y=W_2(W_1 x)=(W_2 W_1)x
$$

입니다. 여기서 $W_2 W_1$은 또 하나의 행렬입니다. 그것을 $W=W_2 W_1$이라고 두면

$$
y=Wx
$$

가 됩니다. 즉 층을 두 개 쌓아도 결국 **하나의 선형변환**과 완전히 같습니다. 아무리 많은 선형 층을 쌓아도

$$
y=W_n\cdots W_2 W_1 x=Wx
$$

가 되어 표현력이 한 층과 다르지 않습니다.

그래서 층 사이에 $\operatorname{ReLU}$나 시그모이드 같은 비선형함수를 넣습니다.

$$
a_1=\operatorname{ReLU}(W_1 x),\qquad y=W_2 a_1
$$

이렇게 하면 $y$를 $x$의 하나의 행렬곱으로 합칠 수 없습니다. 비선형성이 있어야 곡선 형태의 복잡한 결정경계를 만들 수 있고, 층을 깊게 쌓는 의미가 생깁니다.

# 8. 한 줄씩 다시 요약하기

- 신경망은 작은 계산들을 화살표로 이은 계산그래프다.
- 손실 $L$은 가중치 $w$에 직접 붙지 않고, 중간 출력 $y$를 거쳐 연결된다.
- 그래서 $w$가 손실에 주는 영향은 조각들의 곱, 즉 연쇄법칙으로 구한다.
- 역전파는 뒤 층에서 구한 기울기를 앞 층이 받아 자기 몫만 곱해 전달하는 절차다.
- 2층 신경망도 순전파로 $y$와 $L$을 구하고, 역전파로 각 가중치의 기울기를 구해 한 스텝 갱신할 수 있다.
- 비선형함수가 없으면 여러 층이 하나의 선형변환으로 합쳐져 층을 쌓는 의미가 사라진다.
- 핵심 식은 다음과 같습니다.

$$
\frac{\partial L}{\partial w}=\frac{\partial L}{\partial y}\frac{\partial y}{\partial w}
$$

# 9. 스스로 점검

- 손실 $L$이 가중치 $w$에 직접 연결되지 않는데, 왜 두 미분의 곱으로 기울기를 구할 수 있는지 설명할 수 있는가?
- 위 2층 예제에서 학습률을 $0.5$로 바꾸면 $w_1$, $w_2$는 각각 얼마가 되는가?
- $\operatorname{ReLU}$를 빼면 왜 $y=Wx$ 하나로 합쳐지는지 식으로 보일 수 있는가?
