---
title: "37. Attention, Transformer, positional math"
---
# 37강. Attention, Transformer, positional math

이 강의의 목표는 토큰들이 서로를 얼마나 참고할지 계산하는 법을 아주 기초부터 이해하는 것입니다.

먼저 오늘의 핵심 식을 봅니다.

$$
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

이 식을 외우기 전에, 식 안의 말과 기호를 먼저 하나씩 풀어야 합니다.

# 1. 먼저 오늘 쓸 말을 정리하자

| 말 | 뜻 |
|---|---|
| 토큰 | 문장을 모델이 처리하는 작은 단위 |
| 임베딩 | 토큰을 숫자 벡터로 바꾼 것 |
| Query $Q$ | 무엇을 찾는지 나타내는 벡터 |
| Key $K$ | 각 토큰이 가진 표지 벡터 |
| Value $V$ | 실제로 섞어 가져올 정보 |
| $d_k$ | Query와 Key 벡터의 길이(차원 수) |
| softmax | 점수를 확률처럼 더해서 1이 되게 바꾸는 함수 |
| 위치정보 | 단어 순서를 알려 주는 정보 |

수학에서 어려운 부분은 계산보다 읽기입니다. 뜻을 모르고 계산하면 공식이 암호처럼 보입니다.

# 2. 먼저 떠올릴 장면

문장을 읽을 때 어떤 단어는 바로 앞 단어를, 어떤 단어는 멀리 떨어진 단어를 참고해야 합니다. attention은 이 참고 비율을 숫자로 계산합니다.

# 3. 핵심 식을 기호에 값을 넣어 읽어 보자

핵심 식을 오른쪽 안쪽부터 바깥으로 한 단계씩 읽습니다. 기호에 실제 벡터를 넣어 보면 각 단계가 무엇을 하는지 분명해집니다.

## 3.1 $QK^T$는 Query와 Key의 내적 점수다

Query 하나 $q$와 Key 두 개 $k_1,k_2$를 생각합니다. 차원은 $d_k=2$입니다.

$$
q=\begin{bmatrix}1 \\ 1\end{bmatrix},\qquad
k_1=\begin{bmatrix}1 \\ 0\end{bmatrix},\qquad
k_2=\begin{bmatrix}0 \\ 2\end{bmatrix}
$$

$q$가 각 Key와 얼마나 맞는지는 내적으로 잽니다.

$$
q^T k_1=1\cdot 1+1\cdot 0=1,\qquad
q^T k_2=1\cdot 0+1\cdot 2=2
$$

이것이 $QK^T$가 하는 일입니다. Query 행과 Key 행을 모두 내적해 점수 행렬을 만듭니다. 지금은 점수가 $[\,1,\ 2\,]$입니다. $k_2$ 쪽 점수가 더 크므로, 아직 정규화하기 전이지만 $q$는 두 번째 토큰을 더 많이 참고하려는 상태입니다.

## 3.2 $\sqrt{d_k}$로 나누는 이유는 점수의 크기를 눌러 주기 위함이다

$d_k=2$이므로 $\sqrt{d_k}=\sqrt{2}\approx 1.414$입니다. 점수를 이 값으로 나눕니다.

$$
\frac{q^T k_1}{\sqrt{d_k}}=\frac{1}{1.414}\approx 0.707,\qquad
\frac{q^T k_2}{\sqrt{d_k}}=\frac{2}{1.414}\approx 1.414
$$

왜 하필 $\sqrt{d_k}$일까요? 내적은 성분을 $d_k$개 더한 값입니다.

$$
q^T k=\sum_{i=1}^{d_k} q_i k_i
$$

각 성분 $q_i,k_i$가 평균 0, 분산 1 정도로 서로 무관하게 흩어져 있다고 보면, 서로 무관한 항 $d_k$개를 더하므로 내적의 분산은 대략 $d_k$가 됩니다. 즉 표준편차는 $\sqrt{d_k}$입니다. 차원이 커질수록 점수가 통째로 커지고, 그러면 softmax에 큰 값이 들어가 한 곳만 1에 가깝고 나머지는 0에 가까워집니다(포화). $\sqrt{d_k}$로 나누면 점수의 표준편차가 다시 1 근처로 돌아와, 학습 초반에 기울기가 죽지 않고 여러 토큰을 골고루 볼 수 있습니다.

## 3.3 softmax는 점수를 확률로 바꾼다

softmax는 점수 벡터 $z=[z_1,\dots,z_n]$을 다음처럼 바꿉니다.

$$
\operatorname{softmax}(z)_i=\frac{e^{z_i}}{\sum_{j=1}^{n} e^{z_j}}
$$

앞의 점수 $z=[0.707,\ 1.414]$를 넣습니다.

$$
e^{0.707}\approx 2.028,\qquad e^{1.414}\approx 4.113
$$

합은 $2.028+4.113=6.141$입니다. 따라서

$$
\alpha_1=\frac{2.028}{6.141}\approx 0.330,\qquad
\alpha_2=\frac{4.113}{6.141}\approx 0.670
$$

입니다. 이 두 값 $\alpha_1,\alpha_2$가 참고 비율입니다.

softmax 결과가 왜 확률이 될까요? 이유는 두 가지입니다.

- $e^{z_i}$는 항상 양수이므로 모든 비율이 0보다 큽니다.
- 분모가 모든 항의 합이므로, 비율을 모두 더하면 반드시 1이 됩니다.

$$
\alpha_1+\alpha_2\approx 0.330+0.670=1
$$

즉 각 항이 0과 1 사이이고 전체 합이 1이므로, softmax 결과는 "각 토큰을 얼마의 비율로 볼지"라는 확률분포가 됩니다.

## 3.4 마지막으로 Value를 그 비율로 섞는다

Value 두 개가 다음과 같다고 합시다.

$$
v_1=\begin{bmatrix}1 \\ 0\end{bmatrix},\qquad
v_2=\begin{bmatrix}0 \\ 1\end{bmatrix}
$$

출력은 참고 비율로 Value를 가중합한 것입니다.

$$
\text{출력}=\alpha_1 v_1+\alpha_2 v_2
=0.330\begin{bmatrix}1 \\ 0\end{bmatrix}+0.670\begin{bmatrix}0 \\ 1\end{bmatrix}
=\begin{bmatrix}0.330 \\ 0.670\end{bmatrix}
$$

이것이 핵심 식 전체가 하는 일입니다. 점수를 내적으로 만들고, $\sqrt{d_k}$로 크기를 맞추고, softmax로 확률을 만들고, 그 확률로 Value를 섞습니다.

# 4. 왜 attention이라는 생각이 필요한가

기존의 순차 모델은 단어를 앞에서부터 하나씩 읽으며 정보를 좁은 상태 하나에 눌러 담았습니다. 그래서 문장이 길어지면 멀리 떨어진 단어 사이의 관계가 흐려졌습니다. 예를 들어 "철수는 어제 도서관에서 빌린 책을 오늘 그에게 돌려주었다"에서 "그에게"가 누구인지 알려면 문장 앞쪽을 다시 봐야 합니다.

attention은 이 문제를 정면으로 풉니다. 각 토큰이 모든 토큰과 직접 점수를 매기고, 필요한 곳을 골라 봅니다. 거리가 멀어도 점수만 높으면 바로 참고할 수 있습니다. 게다가 이 계산은 토큰마다 독립이라 한꺼번에(병렬로) 처리할 수 있습니다. Transformer가 큰 데이터에서 빠르게 학습되는 이유가 여기에 있습니다. 그래서 이 강의에서는 attention을 "먼 관계를 직접, 그리고 확률적으로 참고하는 장치"로 이해합니다.

# 5. 계산 순서로 다시 보기

1. 토큰을 임베딩으로 바꾼다.
2. 각 토큰에서 Query, Key, Value를 만든다.
3. Query와 Key를 내적해 점수 $QK^T$를 만든다.
4. $\sqrt{d_k}$로 나눠 크기를 맞춘다.
5. softmax로 참고 비율(확률)을 만든다.
6. 그 비율로 Value를 섞는다.

이 순서를 말로 설명할 수 있으면, 공식을 완전히 외우지 않아도 다시 만들어 낼 수 있습니다.

# 6. 위치정보는 어떻게 넣는가

attention은 점수를 내적으로만 계산하므로, 토큰의 순서를 그대로는 알지 못합니다. "개가 사람을 물었다"와 "사람이 개를 물었다"는 단어 집합이 같아 구분이 어렵습니다. 그래서 각 토큰 임베딩에 위치에 따라 달라지는 벡터를 더해 줍니다. 이것을 positional encoding이라고 합니다.

가장 널리 쓰이는 사인·코사인 방식은 위치 $pos$와 차원 번호 $i$에 대해 다음과 같습니다.

$$
PE(pos,2i)=\sin\!\left(\frac{pos}{10000^{2i/d}}\right),\qquad
PE(pos,2i+1)=\cos\!\left(\frac{pos}{10000^{2i/d}}\right)
$$

여기서 $d$는 임베딩 차원입니다. 짝수 자리에는 사인, 홀수 자리에는 코사인을 넣습니다. 차원 번호 $i$가 커질수록 분모가 커져 주기가 길어집니다. 그래서 앞쪽 차원은 짧은 주기로 이웃 위치를, 뒤쪽 차원은 긴 주기로 먼 위치를 구분합니다. 위치마다 벡터가 달라지므로, 같은 단어라도 어디에 있는지에 따라 임베딩이 달라져 순서를 구분할 수 있습니다.

# 7. 예제: 작은 수치로 attention 한 번 계산하기

문제: Query $q=[2,\ 0]$이 다음 두 Key와 Value를 참고합니다. $d_k=2$입니다.

$$
k_1=\begin{bmatrix}2 \\ 0\end{bmatrix},\quad
k_2=\begin{bmatrix}0 \\ 2\end{bmatrix},\qquad
v_1=\begin{bmatrix}10 \\ 0\end{bmatrix},\quad
v_2=\begin{bmatrix}0 \\ 10\end{bmatrix}
$$

풀이:

먼저 내적 점수를 구합니다.

$$
q^T k_1=2\cdot 2+0\cdot 0=4,\qquad
q^T k_2=2\cdot 0+0\cdot 2=0
$$

$\sqrt{d_k}=\sqrt{2}\approx 1.414$로 나눕니다.

$$
\frac{4}{1.414}\approx 2.828,\qquad
\frac{0}{1.414}=0
$$

softmax를 적용합니다.

$$
e^{2.828}\approx 16.92,\qquad e^{0}=1,\qquad \text{합}=17.92
$$

$$
\alpha_1=\frac{16.92}{17.92}\approx 0.944,\qquad
\alpha_2=\frac{1}{17.92}\approx 0.056
$$

Value를 섞습니다.

$$
\text{출력}=0.944\begin{bmatrix}10 \\ 0\end{bmatrix}+0.056\begin{bmatrix}0 \\ 10\end{bmatrix}
=\begin{bmatrix}9.44 \\ 0.56\end{bmatrix}
$$

$q$가 $k_1$과 방향이 같았기 때문에 점수가 크게 나왔고, 그래서 출력은 첫 번째 Value $v_1$ 쪽으로 크게 기울었습니다. attention이 "방향이 맞는 토큰을 더 많이 가져온다"는 것을 수치로 확인할 수 있습니다.

# 8. 한 줄씩 다시 요약하기

- 오늘 배운 핵심은 토큰들이 서로를 얼마나 참고할지 계산하는 법입니다.
- $QK^T$는 Query와 Key의 내적 점수입니다.
- $\sqrt{d_k}$로 나누는 이유는 차원이 커지면 내적의 표준편차가 $\sqrt{d_k}$로 커져 softmax가 포화되기 때문입니다.
- softmax 결과는 각 항이 양수이고 합이 1이라 확률이 됩니다.
- 그 확률로 Value를 가중합한 것이 attention 출력입니다.
- 순서를 구분하려면 positional encoding을 임베딩에 더합니다.
- 핵심 식은 다음과 같습니다.

$$
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

# 9. 스스로 점검

- $QK^T$는 무엇을 계산한 값인가?
- 점수를 $\sqrt{d_k}$로 나누지 않으면 softmax에서 어떤 문제가 생기는가?
- softmax 결과가 왜 확률분포가 되는가?
- positional encoding은 왜 필요한가?
