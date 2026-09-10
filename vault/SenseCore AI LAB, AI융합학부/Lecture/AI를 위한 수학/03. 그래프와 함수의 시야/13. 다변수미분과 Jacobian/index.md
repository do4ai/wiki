---
title: "13. 다변수미분과 Jacobian"
---
# 13강. 다변수미분과 Jacobian

이 강의의 목표는 공식을 빨리 외우는 것이 아닙니다. 목표는 아래 식을 스스로 설명할 수 있게 되는 것입니다.

$$
J_{ij} = \frac{\partial y_i}{\partial x_j}
$$

이 식은 말로 풀면 다음 뜻입니다.

> 야코비안 행렬 $J$의 $i$행 $j$열 원소는, $j$번째 입력 $x_j$를 살짝 움직였을 때 $i$번째 출력 $y_i$가 얼마나 변하는지를 잰 값이다.

이 한 줄에 여러 개념이 한꺼번에 들어 있습니다.

- $\partial$는 무엇인가? 12강의 $d$와 어떻게 다른가?
- "한 입력만 움직인다"는 게 정확히 어떤 동작인가?
- $i$, $j$가 두 개 붙어 있으니 결과가 행렬이라는 건 알겠는데, 행과 열의 의미는?
- 입력이 하나이거나 출력이 하나일 때는 어떻게 되는가?

이 강의는 이 질문을 하나씩, 아주 작은 단계로 나누어 설명합니다. 12강에서 한 변수 함수의 미분을 봤다면, 13강은 그것을 **여러 변수**로 확장하는 작업입니다.

# 1. 먼저 오늘 쓸 말을 정리하자

이번 강에서 새로 등장하는 어휘만 모았습니다. 함수·정의역·치역(3강), 미분·도함수·연쇄법칙(12강), 벡터·행렬·내적(7~10강)은 앞서 본 그대로 씁니다.

| 말 | 뜻 |
|---|---|
| 다변수 함수 | 입력이 여러 개인 함수. 예: $f(x, y) = x^2 + 3y$ |
| 벡터값 함수 | 출력이 여러 개인 함수. 예: $\mathbf{F}(t) = (\cos t, \sin t)$ |
| 편미분 ($\partial$) | 다른 입력은 멈춘 채 한 입력으로만 미분 |
| 기울기벡터 (그라디언트, $\nabla f$) | 모든 편미분을 모은 벡터. 가장 빨리 증가하는 방향 |
| 방향 미분 | 임의의 방향으로 움직일 때의 변화율 |
| 야코비안 행렬 ($J$) | 벡터값 다변수 함수의 모든 편미분을 모은 행렬 |
| 헤시안 행렬 ($H$) | 2차 편미분을 모은 행렬. 곡률 정보를 담는다 |
| 국소 선형근사 | 한 점 근처에서 함수를 선형식으로 근사하는 일 |
| 다변수 연쇄법칙 | 합성함수의 편미분을 야코비안의 곱으로 쓰는 규칙 |

여기서 가장 중요한 식은 도입부에서 본

$$
J_{ij} = \frac{\partial y_i}{\partial x_j}
$$

입니다. 12강의 $f'(a)$를 행렬로 일반화한 것입니다.

# 2. 다변수 함수: 여러 입력이 함께 출력을 정한다

## 2.1 한 변수에서 여러 변수로

3강의 함수는 보통 입력 하나 → 출력 하나였습니다.

$$
f(x) = x^2
$$

이번 강의 다변수 함수는 입력이 여럿입니다.

$$
f(x, y) = x^2 + 3y
$$

입력 $(x, y) = (2, 1)$을 넣으면 $f(2, 1) = 4 + 3 = 7$. 입력 두 개가 함께 출력 하나를 정합니다.

## 2.2 입력을 벡터로 보기

여러 입력을 묶어 벡터로 봅시다 (7강).

$$
\mathbf{x} =
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

그러면 다변수 함수는

$$
f: \mathbb{R}^n \to \mathbb{R}
$$

즉 "$n$차원 벡터를 받아 한 수를 내보내는 함수"라고 쓸 수 있습니다. 손실함수가 대표적인 예입니다.

## 2.3 출력도 여러 개일 수 있다

출력이 여러 개인 함수도 자주 만납니다.

$$
\mathbf{F}(x, y) =
\begin{bmatrix}
x + y \\
xy \\
x^2 - y^2
\end{bmatrix}
$$

이런 함수를 **벡터값 함수**라고 부르고

$$
\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m
$$

으로 씁니다. AI에서 신경망 한 층 $\mathbf{y} = W \mathbf{x} + \mathbf{b}$도 벡터값 함수입니다.

## 2.4 그래프 그림

- $f: \mathbb{R} \to \mathbb{R}$ → 2차원 평면 위의 곡선
- $f: \mathbb{R}^2 \to \mathbb{R}$ → 3차원 공간 위의 곡면 (지형 같은 모양)
- $f: \mathbb{R}^3 \to \mathbb{R}$ → 그릴 수 없음 (4차원)

3차원 이상은 그림으로 그릴 수 없지만, 다음 절부터 볼 편미분의 직관은 차원에 상관없이 통합니다.

# 3. 편미분: 한 변수만 움직이고 나머지는 멈춘다

## 3.1 직관

요리 맛은 소금, 설탕, 물의 양이 함께 결정합니다. 한 가지가 맛에 미치는 영향만 따로 알고 싶으면, **나머지는 모두 똑같이 둔 채** 그것만 살짝 바꿔 봅니다. 이것이 편미분의 정신입니다.

## 3.2 정의

$f(x, y)$의 $x$에 대한 편미분은 $y$를 상수처럼 두고 $x$에 대해서만 12강의 미분을 적용한 것입니다.

$$
\frac{\partial f}{\partial x}(a, b) = \lim_{h \to 0} \frac{f(a + h, b) - f(a, b)}{h}
$$

기호 $\partial$("partial")는 편미분에서만 쓰는 기호입니다. 12강의 $d$ 대신 $\partial$를 씁니다.

마찬가지로 $y$에 대한 편미분은

$$
\frac{\partial f}{\partial y}(a, b) = \lim_{h \to 0} \frac{f(a, b + h) - f(a, b)}{h}
$$

## 3.3 계산 예시

$f(x, y) = x^2 + 3y$의 편미분을 구해 봅시다.

**$x$에 대한 편미분**: $y$를 상수로 보면 $3y$ 항은 상수, $x^2$만 미분.

$$
\frac{\partial f}{\partial x} = 2x
$$

**$y$에 대한 편미분**: $x$를 상수로 보면 $x^2$이 상수, $3y$만 미분.

$$
\frac{\partial f}{\partial y} = 3
$$

12강의 미분 규칙을 그대로 쓰되, 다른 변수는 상수처럼 취급합니다.

## 3.4 더 복잡한 예시

$f(x, y) = x^2 y + e^{xy}$.

**$x$에 대해**: 첫 항 $x^2 y$는 $y$를 상수로 보면 $2xy$. 둘째 항 $e^{xy}$는 연쇄법칙 (12강 8.4절): 안 $u = xy$, $\partial u/\partial x = y$, 바깥 $e^u$의 미분은 $e^u$. 결과는 $y \cdot e^{xy}$.

$$
\frac{\partial f}{\partial x} = 2xy + y e^{xy}
$$

**$y$에 대해**: 첫 항은 $x^2$. 둘째 항은 $x \cdot e^{xy}$.

$$
\frac{\partial f}{\partial y} = x^2 + x e^{xy}
$$

# 4. 기울기벡터(그라디언트): 가장 가파른 방향

편미분을 하나씩 따로 구해 두면 답이 흩어져 있습니다. 이를 한 벡터로 묶은 것이 **기울기벡터**, 영어로 **그라디언트**입니다.

## 4.1 정의

$$
\nabla f(\mathbf{x}) =
\begin{bmatrix}
\dfrac{\partial f}{\partial x_1} \\[4pt]
\dfrac{\partial f}{\partial x_2} \\[4pt]
\vdots \\[4pt]
\dfrac{\partial f}{\partial x_n}
\end{bmatrix}
$$

기호 $\nabla$는 "나블라" 또는 "델"로 읽습니다. 입력이 $n$차원이면 그라디언트도 $n$차원 벡터입니다.

## 4.2 예시

$f(x, y) = x^2 + 3y$의 그라디언트는

$$
\nabla f(x, y) =
\begin{bmatrix}
2x \\
3
\end{bmatrix}
$$

위치에 따라 그라디언트도 달라집니다. 예: $\nabla f(1, 0) = (2, 3)^T$, $\nabla f(0, 0) = (0, 3)^T$.

## 4.3 가장 빨리 증가하는 방향

핵심 사실 하나.

> 그라디언트 $\nabla f$는 함수 $f$가 가장 빨리 증가하는 방향을 가리키고, 그 크기는 그 방향에서의 증가율과 같다.

지형에 비유하면 등산가가 한 점에 서 있을 때, $\nabla f$는 가장 가파른 오르막 방향입니다. 반대로 $-\nabla f$는 가장 가파른 내리막 방향이고, 이것이 경사하강법의 핵심입니다 (10.2절).

## 4.4 그라디언트가 0인 점

$\nabla f = 0$이 되는 점은 어느 방향으로 움직여도 (1차 근사로) 변화가 없는 곳입니다. 이런 점이 극값(극대·극소·안장점) 후보가 됩니다. 12강 9.2절의 다변수 버전입니다.

# 5. 방향 미분: 임의 방향으로 움직일 때

그라디언트는 편미분, 즉 좌표축 방향 변화율만 모아 둔 것 같지만, 사실 임의의 방향에 대한 변화율을 한 식으로 알려 줍니다.

## 5.1 정의

단위벡터 $\mathbf{u}$ 방향으로 움직일 때 $f$의 변화율을 **방향 미분**이라고 하고

$$
D_\mathbf{u} f(\mathbf{x}) = \lim_{h \to 0} \frac{f(\mathbf{x} + h\mathbf{u}) - f(\mathbf{x})}{h}
$$

으로 정의합니다.

## 5.2 그라디언트와 내적으로 표현

미분 가능한 함수에서는 다음 식이 성립합니다.

$$
D_\mathbf{u} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}
$$

즉 방향 미분은 그라디언트와 단위벡터의 내적입니다 (10강).

## 5.3 가장 큰 방향 미분 = 그라디언트 방향

10강에서 본 내적의 성질로

$$
\nabla f \cdot \mathbf{u} = \|\nabla f\| \cdot \|\mathbf{u}\| \cdot \cos\theta = \|\nabla f\| \cos\theta
$$

이 값은 $\theta = 0$일 때 (즉 $\mathbf{u}$가 $\nabla f$와 같은 방향일 때) 최댓값 $\|\nabla f\|$를 가집니다. 이것이 4.3절의 "그라디언트는 가장 빨리 증가하는 방향"이라는 사실의 증명입니다.

# 6. 야코비안: 벡터값 함수의 완전한 미분

이제 출력도 여러 개인 일반적인 경우로 갑니다.

## 6.1 정의

벡터값 함수 $\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m$의 **야코비안**은

$$
J = \begin{bmatrix}
\dfrac{\partial F_1}{\partial x_1} & \dfrac{\partial F_1}{\partial x_2} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\[4pt]
\dfrac{\partial F_2}{\partial x_1} & \dfrac{\partial F_2}{\partial x_2} & \cdots & \dfrac{\partial F_2}{\partial x_n} \\[4pt]
\vdots & \vdots & \ddots & \vdots \\[4pt]
\dfrac{\partial F_m}{\partial x_1} & \dfrac{\partial F_m}{\partial x_2} & \cdots & \dfrac{\partial F_m}{\partial x_n}
\end{bmatrix}
$$

성분으로 쓰면 도입부의 식 그대로

$$
J_{ij} = \frac{\partial F_i}{\partial x_j}
$$

크기는 $m \times n$입니다 — **행은 출력, 열은 입력**.

## 6.2 그라디언트와의 관계

출력이 하나($m=1$)인 경우 야코비안은 행 하나짜리 행렬, 즉 그라디언트의 가로 형태입니다.

$$
J = (\nabla f)^T
$$

그래서 그라디언트는 야코비안의 특수한 경우입니다.

## 6.3 계산 예시

$\mathbf{F}(x, y) = \begin{bmatrix} x + y \\ xy \end{bmatrix}$의 야코비안.

$F_1 = x + y$의 편미분: $\partial F_1/\partial x = 1$, $\partial F_1/\partial y = 1$.
$F_2 = xy$의 편미분: $\partial F_2/\partial x = y$, $\partial F_2/\partial y = x$.

$$
J(x, y) =
\begin{bmatrix}
1 & 1 \\
y & x
\end{bmatrix}
$$

위치 $(1, 2)$에서는

$$
J(1, 2) =
\begin{bmatrix}
1 & 1 \\
2 & 1
\end{bmatrix}
$$

## 6.4 행과 열의 직관

- $J$의 $i$번째 **행**: $i$번째 출력의 그라디언트 (입력에 대한 민감도).
- $J$의 $j$번째 **열**: $j$번째 입력이 모든 출력에 미치는 영향.

이 관점은 신경망에서 어떤 가중치가 어떤 출력에 영향을 주는지 따질 때 유용합니다.

# 7. 다변수 연쇄법칙: 야코비안의 곱

12강 8.4절의 연쇄법칙은 한 변수에서 $h'(x) = f'(g(x)) \cdot g'(x)$였습니다. 다변수에서는 어떻게 될까요?

## 7.1 핵심 식

$\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m$, $\mathbf{G}: \mathbb{R}^p \to \mathbb{R}^n$의 합성

$$
\mathbf{H} = \mathbf{F} \circ \mathbf{G}: \mathbb{R}^p \to \mathbb{R}^m
$$

의 야코비안은 두 야코비안의 **행렬곱**입니다.

$$
J_\mathbf{H}(\mathbf{x}) = J_\mathbf{F}(\mathbf{G}(\mathbf{x})) \cdot J_\mathbf{G}(\mathbf{x})
$$

12강의 단순 곱셈이 8강의 행렬곱으로 일반화된 것입니다.

## 7.2 크기 확인

- $J_\mathbf{F}$: $m \times n$
- $J_\mathbf{G}$: $n \times p$
- 곱: $m \times p$ ← $J_\mathbf{H}$의 크기와 일치 ✓

8강의 "행렬곱은 변환을 이어붙이는 것"이 그대로 되살아납니다.

## 7.3 신경망 역전파의 뼈대

신경망 한 층의 변환은 벡터값 함수입니다. 깊은 신경망은 여러 층의 합성

$$
\mathbf{y} = \mathbf{F}_L \circ \mathbf{F}_{L-1} \circ \cdots \circ \mathbf{F}_1 (\mathbf{x})
$$

이고, 손실함수에 대한 가중치의 그라디언트는 7.1절의 식을 여러 번 곱해서 얻습니다. 이 계산을 역순으로 효율화한 알고리즘이 **역전파**(backpropagation)입니다.

> 한 줄로: 다변수 연쇄법칙 = 야코비안의 행렬곱 = 역전파의 수학.

# 8. 헤시안: 2차 편미분의 행렬

12강 9.2절에서 한 변수 함수의 극값 판별에 부호 변화를 썼습니다. 다변수에서는 도구가 한 단계 더 필요한데, 그것이 헤시안입니다.

## 8.1 정의

$f: \mathbb{R}^n \to \mathbb{R}$의 **헤시안 행렬**은 모든 2차 편미분을 모은 $n \times n$ 행렬.

$$
H_{ij} = \frac{\partial^2 f}{\partial x_i \, \partial x_j}
$$

## 8.2 예시

$f(x, y) = x^2 + 3xy + y^2$.

$$
\frac{\partial f}{\partial x} = 2x + 3y, \quad \frac{\partial f}{\partial y} = 3x + 2y
$$

각각을 다시 편미분.

$$
\frac{\partial^2 f}{\partial x^2} = 2, \quad
\frac{\partial^2 f}{\partial x \partial y} = 3, \quad
\frac{\partial^2 f}{\partial y \partial x} = 3, \quad
\frac{\partial^2 f}{\partial y^2} = 2
$$

따라서

$$
H = \begin{bmatrix} 2 & 3 \\ 3 & 2 \end{bmatrix}
$$

## 8.3 대칭성

부드러운 함수에서는 편미분 순서를 바꿔도 결과가 같습니다.

$$
\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}
$$

따라서 헤시안은 항상 **대칭행렬**. 9강에서 본 고유값분해가 그대로 적용됩니다.

## 8.4 극값 판별

그라디언트가 0인 점에서 헤시안의 고유값으로 종류를 판별합니다.

- 모든 고유값이 양 → 극소 (그릇 모양)
- 모든 고유값이 음 → 극대 (뒤집힌 그릇)
- 고유값에 부호가 섞여 있음 → 안장점 (말 안장 모양)

# 9. 국소 선형근사: 한 점 근처에서는 직선처럼 본다

12강에서 미분의 의미가 "한 점에서의 접선"이었습니다. 다변수에서는 "한 점에서의 접평면"이 됩니다.

## 9.1 한 변수 복습

12강에서 한 점 $a$ 근처에서의 함수 근사는

$$
f(a + h) \approx f(a) + f'(a) \cdot h
$$

## 9.2 다변수 일반화

다변수 함수의 한 점 근처 근사는

$$
f(\mathbf{x} + \mathbf{h}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x}) \cdot \mathbf{h}
$$

기호만 다를 뿐 구조는 같습니다. 곱하기가 내적으로 바뀐 것뿐.

## 9.3 벡터값 함수 일반화

$\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^m$의 경우

$$
\mathbf{F}(\mathbf{x} + \mathbf{h}) \approx \mathbf{F}(\mathbf{x}) + J(\mathbf{x}) \cdot \mathbf{h}
$$

스칼라 곱하기가 행렬 곱하기로 바뀌었지만, "한 점 근처에서는 선형으로 본다"는 핵심은 변하지 않습니다. 15강 테일러 전개에서 더 자세히 다룹니다.

# 10. 왜 AI 수학에서 다변수미분이 중요한가

거의 모든 머신러닝·딥러닝 기법이 다변수미분에 기댑니다.

## 10.1 손실함수는 매개변수 벡터의 함수

신경망의 매개변수 $\theta$는 수백만~수십억 개. 손실함수 $L(\theta)$는 그 거대한 벡터를 입력으로 받는 다변수 함수입니다. 학습 = $L$이 작아지는 $\theta$ 찾기.

## 10.2 경사하강법: $-\nabla L$ 방향으로

12강 10.2절의 한 변수 식

$$
\theta_{\text{new}} = \theta_{\text{old}} - \eta \cdot L'(\theta_{\text{old}})
$$

은 다변수에서

$$
\boldsymbol\theta_{\text{new}} = \boldsymbol\theta_{\text{old}} - \eta \cdot \nabla L(\boldsymbol\theta_{\text{old}})
$$

가 됩니다. 4.3절에서 본 "$-\nabla L$이 가장 빨리 감소하는 방향"이 이 식의 직관입니다.

## 10.3 역전파 = 야코비안 곱

7.3절. 여러 층 신경망의 손실 그라디언트는 각 층의 야코비안을 차례로 곱해서 얻습니다.

## 10.4 자동 미분

PyTorch나 JAX 같은 프레임워크는 위 계산을 자동으로 해 줍니다. 사용자는 손실 함수만 적으면 그라디언트를 알아서 계산해 줍니다(자동 미분, autograd). 그 이론적 토대가 13강의 야코비안과 연쇄법칙입니다.

# 11. 13강이 이어지는 길

- **14강**: 미분의 반대 작업 — 적분. 다변수 적분은 부피·확률밀도로 이어진다.
- **15강**: 한 점에서의 도함수·헤시안 정보로 함수를 다항식으로 근사하는 다변수 테일러 전개.
- **16강**: 다변수 미분으로 시간에 따른 변화를 표현하는 미분방정식 시스템.
- 5단원 22~23강: 그라디언트와 헤시안을 본격적으로 쓰는 최적화 알고리즘들.

# 12. 예제 1: 편미분 계산

문제: $f(x, y, z) = x^2 y + y z^3 - \ln z$의 모든 편미분을 구하시오.

풀이:

$x$로 편미분 ($y, z$는 상수):

$$
\frac{\partial f}{\partial x} = 2 x y
$$

$y$로 편미분 ($x, z$는 상수):

$$
\frac{\partial f}{\partial y} = x^2 + z^3
$$

$z$로 편미분 ($x, y$는 상수):

$$
\frac{\partial f}{\partial z} = 3 y z^2 - \frac{1}{z}
$$

# 13. 예제 2: 그라디언트 계산과 의미

문제: $f(x, y) = x^2 + 4 y^2$의 점 $(1, 1)$에서의 그라디언트를 구하고, 가장 빨리 증가하는 방향을 말하시오.

풀이:

$$
\nabla f(x, y) = \begin{bmatrix} 2x \\ 8y \end{bmatrix}
\;\Rightarrow\;
\nabla f(1, 1) = \begin{bmatrix} 2 \\ 8 \end{bmatrix}
$$

점 $(1, 1)$에서 가장 빨리 증가하는 방향은 $\begin{bmatrix}2 \\ 8\end{bmatrix}$ 방향입니다. 단위벡터로 정규화하면

$$
\hat{\mathbf{u}} = \frac{1}{\sqrt{4 + 64}} \begin{bmatrix} 2 \\ 8 \end{bmatrix} = \frac{1}{\sqrt{68}} \begin{bmatrix} 2 \\ 8 \end{bmatrix}
$$

증가율(방향 미분의 최댓값)은 $\|\nabla f(1, 1)\| = \sqrt{68} \approx 8.25$.

# 14. 예제 3: 야코비안 계산

문제: $\mathbf{F}(x, y) = \begin{bmatrix} x^2 - y^2 \\ 2xy \end{bmatrix}$의 야코비안을 구하시오. (이 함수는 복소수 제곱 $z \mapsto z^2$에 해당)

풀이:

$F_1 = x^2 - y^2$: $\partial F_1/\partial x = 2x$, $\partial F_1/\partial y = -2y$.
$F_2 = 2xy$: $\partial F_2/\partial x = 2y$, $\partial F_2/\partial y = 2x$.

$$
J(x, y) =
\begin{bmatrix}
2x & -2y \\
2y & 2x
\end{bmatrix}
$$

흥미롭게도 이 야코비안은 9강에서 본 회전+늘리기의 형태입니다. 점 $(1, 0)$에서는 $J = \begin{bmatrix}2 & 0 \\ 0 & 2\end{bmatrix}$ — 단순한 2배 늘리기.

# 15. 예제 4: 다변수 연쇄법칙

문제: $f(x, y) = x^2 + y^2$이고 $x = \cos t$, $y = \sin t$일 때 $\dfrac{df}{dt}$를 구하시오.

풀이:

다변수 연쇄법칙으로

$$
\frac{df}{dt} = \frac{\partial f}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial f}{\partial y} \cdot \frac{dy}{dt}
$$

각각:

$$
\frac{\partial f}{\partial x} = 2x = 2\cos t, \quad
\frac{\partial f}{\partial y} = 2y = 2\sin t
$$

$$
\frac{dx}{dt} = -\sin t, \quad
\frac{dy}{dt} = \cos t
$$

대입:

$$
\frac{df}{dt} = 2\cos t \cdot (-\sin t) + 2\sin t \cdot \cos t = -2\cos t \sin t + 2\sin t \cos t = 0
$$

직관적으로 $f(x, y) = x^2 + y^2 = \cos^2 t + \sin^2 t = 1$ (상수)이므로 도함수가 0인 것이 맞습니다.

# 16. 예제 5: 헤시안과 극값 판별

문제: $f(x, y) = x^2 + xy + y^2 - 4x - 5y$의 임계점을 찾고 종류를 판별하시오.

풀이:

**1단계: 그라디언트 = 0**

$$
\frac{\partial f}{\partial x} = 2x + y - 4 = 0
$$

$$
\frac{\partial f}{\partial y} = x + 2y - 5 = 0
$$

연립하면 $x = 1, y = 2$. 임계점은 $(1, 2)$.

**2단계: 헤시안**

$$
H = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}
$$

**3단계: 고유값으로 판별**

특성방정식 $(2-\lambda)^2 - 1 = 0$에서 $\lambda = 1, 3$. 둘 다 양수이므로 8.4절에 따라 **극소**.

극솟값은 $f(1, 2) = 1 + 2 + 4 - 4 - 10 = -7$.

# 17. 한 줄씩 다시 요약하기

- 다변수 함수는 입력이 여러 개, 벡터값 함수는 출력도 여러 개인 함수다.
- 편미분은 다른 입력은 멈춰 둔 채 한 변수로만 미분한 결과다.
- 그라디언트 $\nabla f$는 편미분들을 모은 벡터, 가장 빨리 증가하는 방향이다.
- 방향 미분 $D_\mathbf{u} f = \nabla f \cdot \mathbf{u}$ — 그라디언트와 단위벡터의 내적.
- 야코비안 $J$는 벡터값 함수의 모든 편미분을 모은 행렬, 행=출력 열=입력.
- 그라디언트는 출력이 하나일 때의 야코비안이다.
- 다변수 연쇄법칙 $J_\mathbf{H} = J_\mathbf{F} \cdot J_\mathbf{G}$ — 야코비안의 행렬곱.
- 헤시안은 2차 편미분의 대칭행렬, 그 고유값으로 극값 종류를 판별한다.
- 국소 선형근사 $f(\mathbf{x} + \mathbf{h}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x}) \cdot \mathbf{h}$.
- AI에서: 경사하강법 = $-\nabla L$ 방향 이동, 역전파 = 야코비안 곱, autograd = 자동 미분.

# 18. 스스로 점검

1. 편미분 기호 $\partial$가 왜 보통 $d$와 다른지 한 줄로 설명할 수 있는가?
2. $f(x, y) = e^x \sin y$의 두 편미분을 구할 수 있는가?
3. $f(x, y, z) = x^2 + y^2 + z^2$의 그라디언트를 구하고, 점 $(1, 2, 2)$에서 그 의미를 말할 수 있는가?
4. 그라디언트가 "가장 빨리 증가하는 방향"인 이유를 내적으로 설명할 수 있는가?
5. 다음 함수의 야코비안을 구할 수 있는가?

$$
\mathbf{F}(x, y) = \begin{bmatrix} x + 2y \\ x^2 - y \\ \sin x \end{bmatrix}
$$

6. 위 야코비안의 크기는 몇 $\times$ 몇인가? 왜 그런가?
7. 다변수 연쇄법칙이 왜 단순 곱이 아니라 행렬곱인지 설명할 수 있는가?
8. 헤시안이 항상 대칭이라는 사실이 왜 중요한지 말할 수 있는가?
9. $f(x, y) = x^2 - y^2$의 점 $(0, 0)$이 안장점인 이유를 헤시안으로 설명할 수 있는가?
10. 신경망 역전파가 결국 어떤 수학적 동작인지 한 줄로 말할 수 있는가?
