---
title: "41. VLM, multimodal generation, fusion architectures"
---
# 41강. VLM, multimodal generation, fusion architectures

이 강의의 목표는 텍스트와 이미지를 함께 읽고 답하거나 생성하는 모델 구조를 아주 기초부터 이해하는 것입니다.

먼저 오늘의 핵심 식을 봅니다.

$$
p(y\mid x_{\mathrm{text}},x_{\mathrm{image}})
$$

이 식을 외우기 전에, 식 안의 말과 기호를 먼저 하나씩 풀어야 합니다.

# 1. 먼저 오늘 쓸 말을 정리하자

| 말 | 뜻 |
|---|---|
| $x_{\mathrm{text}}$ | 입력 텍스트(질문 등) |
| $x_{\mathrm{image}}$ | 입력 이미지 |
| $y$ | 모델이 생성하는 출력 토큰들 |
| fusion | 서로 다른 모달 정보를 합치는 과정 |
| early fusion | 초기에 정보를 섞는 구조 |
| late fusion | 따로 처리한 뒤 나중에 섞는 구조 |
| cross-attention | 한 모달이 다른 모달을 참고하는 attention |

수학에서 어려운 부분은 계산보다 읽기입니다. 뜻을 모르고 계산하면 공식이 암호처럼 보입니다.

# 2. 먼저 떠올릴 장면

사람은 사진을 보며 질문에 답할 수 있습니다. 사진 속 색, 위치, 숫자를 보고 언어로 설명합니다. VLM은 이미지와 텍스트를 함께 읽어 답을 만듭니다.

# 3. 핵심 식을 값을 넣어 읽어 보자

## 3.1 출력은 조건부확률로 한 토큰씩 생성된다

$p(y\mid x_{\mathrm{text}},x_{\mathrm{image}})$는 "텍스트와 이미지가 함께 주어졌을 때 출력 $y$가 나올 확률"입니다. $y$는 여러 토큰 $y_1,\dots,y_T$로 이루어지므로, 이 확률은 연쇄법칙으로 한 토큰씩 풀립니다.

$$
p(y\mid x_{\mathrm{text}},x_{\mathrm{image}})
=\prod_{t=1}^{T} p\big(y_t\mid y_{<t},x_{\mathrm{text}},x_{\mathrm{image}}\big)
$$

즉 37강·38강의 언어모델과 골격은 같습니다. 다른 점은 매 토큰을 고를 때 앞 토큰뿐 아니라 이미지 정보 $x_{\mathrm{image}}$까지 조건으로 함께 본다는 것입니다. 학습은 38강처럼 정답 토큰의 로그확률을 최대화하는 것으로, 손실은

$$
L=-\sum_{t}\log p\big(y_t\mid y_{<t},x_{\mathrm{text}},x_{\mathrm{image}}\big)
$$

입니다.

## 3.2 cross-attention이 이미지를 조건으로 끌어온다

이미지를 조건으로 넣는 대표적인 방법이 cross-attention입니다. 텍스트 쪽에서 Query를 만들고, 이미지 토큰에서 Key와 Value를 만듭니다.

$$
\operatorname{CrossAttn}=\operatorname{softmax}\!\left(\frac{Q_{\mathrm{text}}\,K_{\mathrm{image}}^{T}}{\sqrt{d_k}}\right)V_{\mathrm{image}}
$$

37강의 attention과 식이 같지만, Query는 텍스트에서, Key·Value는 이미지에서 온다는 점이 핵심입니다. 그래서 텍스트의 각 위치가 "이미지의 어느 패치를 얼마나 볼지"를 softmax 비율로 정하고, 그 비율로 이미지 정보를 가져옵니다. "빨간 컵은 어디 있나"라는 질문 토큰이 이미지에서 빨간 영역 패치에 높은 점수를 주는 식입니다.

# 4. 왜 fusion 구조를 고민해야 하는가

이미지와 텍스트는 정보의 밀도와 형태가 다릅니다. 이미지는 수백 개의 패치 벡터로, 텍스트는 토큰 벡터로 표현됩니다. 이 둘을 언제, 어디서 합치느냐에 따라 성능과 비용이 크게 달라지기 때문에 fusion 구조가 중요합니다.

- early fusion: 이미지 패치와 텍스트 토큰을 처음부터 한 줄로 이어 붙여 하나의 Transformer에 넣습니다. 두 모달이 모든 층에서 서로 참고하므로 상호작용이 깊지만, 토큰 수가 늘어 연산이 무겁습니다.
- late fusion: 이미지와 텍스트를 각자의 인코더로 끝까지 따로 처리한 뒤, 마지막에 벡터를 합치거나 유사도만 비교합니다. 가볍고 모듈을 재사용하기 좋지만, 세밀한 상호작용은 약합니다(40강 CLIP이 late fusion에 가깝습니다).
- cross-attention fusion: 텍스트는 텍스트대로 흐르되, 중간중간 cross-attention 층에서만 이미지를 참고합니다. early와 late의 절충으로, 상호작용을 살리면서 비용을 조절할 수 있어 많은 VLM이 채택합니다.

이 강의에서는 VLM을 "언어모델의 조건에 이미지를 어떤 방식으로 끼워 넣을지 정하는 문제"로 이해합니다.

# 5. 계산 순서로 다시 보기

1. 이미지를 패치나 특징 벡터로 바꾼다.
2. 텍스트를 토큰 벡터로 바꾼다.
3. 두 정보를 fusion 구조(early/late/cross-attention)로 섞는다.
4. 조건부확률 $p(y_t\mid y_{<t},x_{\mathrm{text}},x_{\mathrm{image}})$로 출력 토큰을 하나씩 생성한다.
5. 출력이 이미지 근거를 제대로 썼는지 확인한다.

이 순서를 말로 설명할 수 있으면, 공식을 완전히 외우지 않아도 다시 만들어 낼 수 있습니다.

# 6. 예제: cross-attention으로 이미지 참고 한 번 계산하기

문제: 질문 토큰의 Query $Q_{\mathrm{text}}=[1,\ 1]$이 이미지 패치 두 개를 참고한다. $d_k=2$이다.

$$
K_1=\begin{bmatrix}2 \\ 0\end{bmatrix},\quad
K_2=\begin{bmatrix}0 \\ 1\end{bmatrix},\qquad
V_1=\begin{bmatrix}1 \\ 0\end{bmatrix}(\text{빨강}),\quad
V_2=\begin{bmatrix}0 \\ 1\end{bmatrix}(\text{파랑})
$$

풀이:

내적 점수를 구합니다.

$$
Q^T K_1=1\cdot 2+1\cdot 0=2,\qquad
Q^T K_2=1\cdot 0+1\cdot 1=1
$$

$\sqrt{d_k}=\sqrt{2}\approx 1.414$로 나눕니다.

$$
\frac{2}{1.414}\approx 1.414,\qquad \frac{1}{1.414}\approx 0.707
$$

softmax를 적용합니다.

$$
e^{1.414}\approx 4.11,\quad e^{0.707}\approx 2.03,\quad \text{합}=6.14
$$

$$
\alpha_1\approx 0.669,\qquad \alpha_2\approx 0.331
$$

이미지 정보를 이 비율로 가져옵니다.

$$
\text{출력}=0.669\begin{bmatrix}1 \\ 0\end{bmatrix}+0.331\begin{bmatrix}0 \\ 1\end{bmatrix}
=\begin{bmatrix}0.669 \\ 0.331\end{bmatrix}
$$

질문 Query가 첫 번째 패치(빨강)와 더 잘 맞아 그쪽을 약 67% 참고했습니다. cross-attention이 "질문에 맞는 이미지 영역을 골라 가져온다"는 것을 수치로 확인할 수 있습니다.

# 7. 한 줄씩 다시 요약하기

- 오늘 배운 핵심은 텍스트와 이미지를 함께 읽고 답하거나 생성하는 모델 구조입니다.
- 출력은 $\prod_t p(y_t\mid y_{<t},x_{\mathrm{text}},x_{\mathrm{image}})$로 한 토큰씩 생성됩니다.
- cross-attention은 텍스트를 Query로, 이미지를 Key·Value로 써서 필요한 패치를 가져옵니다.
- early/late/cross-attention fusion은 상호작용 깊이와 비용의 절충이 다릅니다.
- 핵심 식은 다음과 같습니다.

$$
p(y\mid x_{\mathrm{text}},x_{\mathrm{image}})
$$

# 8. 스스로 점검

- 출력 확률을 왜 토큰별 조건부확률의 곱으로 쓰는가?
- cross-attention에서 Query, Key, Value는 각각 어느 모달에서 오는가?
- early fusion과 late fusion의 장단점은 무엇인가?
- cross-attention fusion이 둘의 절충인 이유는 무엇인가?
