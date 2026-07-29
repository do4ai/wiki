---
title: "1. 벡터와 연산"
---
# 1강. 벡터와 연산

## 이 강의에서 할 수 있게 되는 것

- 벡터를 순서쌍이자 방향으로 정의하고 두 관점을 오갈 수 있습니다.
- 벡터의 덧셈과 스칼라배를 정의하고 그 성질을 진술할 수 있습니다.
- 내적을 정의하고 노름과 각도를 내적으로 표현할 수 있습니다.
- 코시-슈바르츠 부등식과 삼각부등식을 이해하고 사용할 수 있습니다.

이 강의는 `AI를 위한 수학`의 [07. 벡터공간과 기저](../../../AI를 위한 수학/02. 벡터와 행렬의 시작/07. 벡터공간과 기저/index.md) 강의와 관련 주제를 더 볼 수 있습니다. 이 교본은 정의와 증명을 중심으로 진행합니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\mathbb{R}$ | 실수 전체 | 실수들의 집합 |
| $\mathbb{R}^n$ | 알엔 | 실수 $n$개를 순서대로 묶은 벡터들의 집합 |
| $\mathbf{v}$ | 벡터 브이 | 여러 실수를 순서대로 모은 대상 |
| $v_i$ | 브이 아이 | 벡터 $\mathbf{v}$의 $i$번째 성분 |
| $\mathbf{u}+\mathbf{v}$ | 유 플러스 브이 | 두 벡터의 덧셈 |
| $c\mathbf{v}$ | 씨 브이 | 스칼라 $c$를 벡터에 곱한 스칼라배 |
| $\mathbf{u}\cdot\mathbf{v}$ | 유 닷 브이 | 두 벡터의 내적 |
| $\mathbf{u}^T\mathbf{v}$ | 유 전치 브이 | 내적을 행렬곱으로 쓴 표기 |
| $\lVert\mathbf{v}\rVert$ | 브이의 노름 | 벡터의 길이 |
| $\mathbf{0}$ | 영벡터 | 모든 성분이 0인 벡터 |

## 2. 개념

### 2.1 벡터의 정의

정의부터 세웁니다. 실수 $n$개를 순서대로 묶은 것을 $n$차원 실벡터라고 하고, 이들의 집합을 $\mathbb{R}^n$이라고 씁니다.

$$
\mathbf{v}=
\begin{bmatrix}
v_1 \\ v_2 \\ \vdots \\ v_n
\end{bmatrix},
\qquad v_1,\dots,v_n\in\mathbb{R}
$$

여기서 $v_i$를 $\mathbf{v}$의 $i$번째 성분이라고 합니다. "순서대로"가 핵심입니다. 성분의 순서를 바꾸면 다른 벡터입니다.

벡터에는 두 가지 관점이 있습니다.

- 대수적 관점: 벡터는 성분들의 순서 있는 목록입니다.
- 기하적 관점: 벡터는 원점에서 어떤 점으로 향하는 화살표, 즉 방향과 크기를 가진 양입니다.

예를 들어 $\mathbf{v}=\begin{bmatrix}3\\2\end{bmatrix}$는 오른쪽으로 3, 위로 2만큼 가는 평면 위의 화살표입니다. 두 관점은 같은 대상을 다르게 보는 것이며, 앞으로 필요에 따라 자유롭게 오갑니다.

> **문제 1.** (기초) 벡터 $\mathbf{v}=\begin{bmatrix}-1\\4\end{bmatrix}$를 평면 위의 화살표로 말로 설명하십시오.
> **답.** 왼쪽으로 1, 위로 4만큼 가는 화살표입니다.
> **풀이.** 첫 성분 $-1$은 $x$축 방향 이동량이므로 왼쪽으로 1, 둘째 성분 $4$는 $y$축 방향 이동량이므로 위로 4를 뜻합니다. 원점에서 점 $(-1,4)$로 향하는 화살표입니다.

> **문제 2.** (기초) $\mathbb{R}^3$의 벡터 $\begin{bmatrix}2\\0\\-5\end{bmatrix}$에서 세 번째 성분은 무엇입니까?
> **답.** $-5$입니다.
> **풀이.** 성분은 위에서부터 순서대로 첫째 $2$, 둘째 $0$, 셋째 $-5$입니다. 세 번째 성분 $v_3=-5$입니다.

> **문제 3.** (표준) 두 벡터 $\begin{bmatrix}1\\2\end{bmatrix}$와 $\begin{bmatrix}2\\1\end{bmatrix}$이 같은 벡터인지 판정하십시오.
> **답.** 같지 않습니다.
> **풀이.** 두 벡터가 같으려면 대응하는 모든 성분이 같아야 합니다. 첫 성분은 $1$과 $2$로 다릅니다. 성분의 순서가 다르면 다른 벡터이므로 두 벡터는 같지 않습니다.

### 2.2 벡터의 덧셈과 스칼라배

두 벡터의 덧셈은 같은 자리 성분끼리 더해 정의합니다.

$$
\mathbf{u}+\mathbf{v}=
\begin{bmatrix}
u_1+v_1 \\ \vdots \\ u_n+v_n
\end{bmatrix}
$$

스칼라 $c\in\mathbb{R}$와 벡터의 곱, 즉 스칼라배는 모든 성분에 $c$를 곱해 정의합니다.

$$
c\mathbf{v}=
\begin{bmatrix}
cv_1 \\ \vdots \\ cv_n
\end{bmatrix}
$$

기하적으로 덧셈은 화살표를 이어 붙이는 것입니다. $\mathbf{u}$의 끝에서 $\mathbf{v}$만큼 더 가면 $\mathbf{u}+\mathbf{v}$의 끝에 도착합니다. 이를 평행사변형 법칙이라고도 합니다. 스칼라배는 화살표의 길이를 $|c|$배로 늘리고, $c<0$이면 방향을 반대로 뒤집는 것입니다.

이 두 연산은 다음 성질을 만족합니다. $\mathbf{u},\mathbf{v},\mathbf{w}\in\mathbb{R}^n$, $c,d\in\mathbb{R}$에 대해

$$
\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u},\qquad
(\mathbf{u}+\mathbf{v})+\mathbf{w}=\mathbf{u}+(\mathbf{v}+\mathbf{w})
$$

$$
\mathbf{v}+\mathbf{0}=\mathbf{v},\qquad
\mathbf{v}+(-\mathbf{v})=\mathbf{0}
$$

$$
c(d\mathbf{v})=(cd)\mathbf{v},\qquad
c(\mathbf{u}+\mathbf{v})=c\mathbf{u}+c\mathbf{v},\qquad
(c+d)\mathbf{v}=c\mathbf{v}+d\mathbf{v},\qquad
1\mathbf{v}=\mathbf{v}
$$

이 성질들은 각각 성분별 계산으로 바로 증명됩니다. 예를 들어 교환법칙은 각 성분에서 $u_i+v_i=v_i+u_i$가 실수 덧셈의 교환법칙으로 성립하기 때문입니다. 이 여덟 성질은 다음 강의에서 벡터공간의 공리로 다시 등장합니다.

> **문제 1.** (기초) $\mathbf{u}=\begin{bmatrix}1\\3\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}4\\-1\end{bmatrix}$일 때 $\mathbf{u}+\mathbf{v}$를 구하십시오.
> **답.** $\begin{bmatrix}5\\2\end{bmatrix}$입니다.
> **풀이.** 같은 자리끼리 더합니다. 첫 성분은 $1+4=5$, 둘째 성분은 $3+(-1)=2$입니다. 따라서 $\mathbf{u}+\mathbf{v}=\begin{bmatrix}5\\2\end{bmatrix}$입니다.

> **문제 2.** (기초) $\mathbf{v}=\begin{bmatrix}2\\-4\\6\end{bmatrix}$일 때 $-\tfrac{1}{2}\mathbf{v}$를 구하십시오.
> **답.** $\begin{bmatrix}-1\\2\\-3\end{bmatrix}$입니다.
> **풀이.** 모든 성분에 $-\tfrac12$를 곱합니다. $-\tfrac12\cdot 2=-1$, $-\tfrac12\cdot(-4)=2$, $-\tfrac12\cdot 6=-3$입니다.

> **문제 3.** (표준) $\mathbf{u}=\begin{bmatrix}1\\0\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}0\\1\end{bmatrix}$일 때 $3\mathbf{u}-2\mathbf{v}$를 구하십시오.
> **답.** $\begin{bmatrix}3\\-2\end{bmatrix}$입니다.
> **풀이.** 먼저 $3\mathbf{u}=\begin{bmatrix}3\\0\end{bmatrix}$, $2\mathbf{v}=\begin{bmatrix}0\\2\end{bmatrix}$입니다. 빼면 $\begin{bmatrix}3-0\\0-2\end{bmatrix}=\begin{bmatrix}3\\-2\end{bmatrix}$입니다.

> **문제 4.** (표준) 덧셈의 교환법칙 $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$가 왜 성립하는지 성분으로 설명하십시오.
> **답.** 각 성분에서 실수 덧셈의 교환법칙이 성립하기 때문입니다.
> **풀이.** $\mathbf{u}+\mathbf{v}$의 $i$번째 성분은 $u_i+v_i$이고, $\mathbf{v}+\mathbf{u}$의 $i$번째 성분은 $v_i+u_i$입니다. 실수에서 $u_i+v_i=v_i+u_i$이므로 모든 성분이 같습니다. 따라서 두 벡터는 같습니다.

> **문제 5.** (심화) $\mathbf{a}=\begin{bmatrix}2\\1\end{bmatrix}$, $\mathbf{b}=\begin{bmatrix}-1\\3\end{bmatrix}$에 대해 $\mathbf{a}$와 $\mathbf{b}$를 두 변으로 하는 평행사변형의 네 꼭짓점을 원점을 한 꼭짓점으로 하여 구하십시오.
> **답.** $\mathbf{0}=\begin{bmatrix}0\\0\end{bmatrix}$, $\mathbf{a}=\begin{bmatrix}2\\1\end{bmatrix}$, $\mathbf{b}=\begin{bmatrix}-1\\3\end{bmatrix}$, $\mathbf{a}+\mathbf{b}=\begin{bmatrix}1\\4\end{bmatrix}$입니다.
> **풀이.** 평행사변형 법칙에 따라 네 꼭짓점은 원점, $\mathbf{a}$의 끝, $\mathbf{b}$의 끝, 그리고 대각선 끝인 $\mathbf{a}+\mathbf{b}$입니다. $\mathbf{a}+\mathbf{b}=\begin{bmatrix}2+(-1)\\1+3\end{bmatrix}=\begin{bmatrix}1\\4\end{bmatrix}$입니다.

### 2.3 내적

두 벡터의 관계를 재려면 내적이 필요합니다. $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$의 내적을 다음처럼 정의합니다.

$$
\mathbf{u}\cdot\mathbf{v}=\sum_{i=1}^{n}u_i v_i=u_1v_1+u_2v_2+\cdots+u_nv_n
$$

이는 같은 자리 성분끼리 곱해서 모두 더한 값이며, 결과는 벡터가 아니라 하나의 실수입니다. 행렬곱 표기로는 $\mathbf{u}$를 가로로 눕힌 $\mathbf{u}^T$를 $\mathbf{v}$에 곱한 것과 같으므로

$$
\mathbf{u}\cdot\mathbf{v}=\mathbf{u}^T\mathbf{v}
$$

라고도 씁니다. 두 표기는 같은 값을 가리킵니다.

내적은 다음 성질을 만족합니다.

$$
\mathbf{u}\cdot\mathbf{v}=\mathbf{v}\cdot\mathbf{u}\quad(\text{대칭성})
$$

$$
(c\mathbf{u}+d\mathbf{w})\cdot\mathbf{v}=c(\mathbf{u}\cdot\mathbf{v})+d(\mathbf{w}\cdot\mathbf{v})\quad(\text{선형성})
$$

$$
\mathbf{v}\cdot\mathbf{v}\ge 0,\quad \text{그리고 } \mathbf{v}\cdot\mathbf{v}=0 \iff \mathbf{v}=\mathbf{0}\quad(\text{양의 정부호성})
$$

양의 정부호성은 $\mathbf{v}\cdot\mathbf{v}=\sum v_i^2$가 제곱합이라 항상 0 이상이고, 0이 되려면 모든 $v_i=0$이어야 하기 때문에 성립합니다.

> **문제 1.** (기초) $\mathbf{u}=\begin{bmatrix}2\\3\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}4\\-1\end{bmatrix}$의 내적을 구하십시오.
> **답.** $5$입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=2\cdot4+3\cdot(-1)=8-3=5$입니다.

> **문제 2.** (기초) $\mathbf{v}=\begin{bmatrix}1\\-2\\2\end{bmatrix}$일 때 $\mathbf{v}\cdot\mathbf{v}$를 구하십시오.
> **답.** $9$입니다.
> **풀이.** $\mathbf{v}\cdot\mathbf{v}=1^2+(-2)^2+2^2=1+4+4=9$입니다. 이는 제곱합이므로 항상 0 이상임을 확인할 수 있습니다.

> **문제 3.** (표준) 내적의 선형성을 이용해 $(2\mathbf{u})\cdot\mathbf{v}=2(\mathbf{u}\cdot\mathbf{v})$임을 보이십시오.
> **답.** 성분별로 각 항에 2가 곱해지기 때문입니다.
> **풀이.** $(2\mathbf{u})\cdot\mathbf{v}=\sum_i (2u_i)v_i=2\sum_i u_iv_i=2(\mathbf{u}\cdot\mathbf{v})$입니다. 합 기호 밖으로 상수 2를 빼낼 수 있으므로 성립합니다.

> **문제 4.** (표준) $\mathbf{u}=\begin{bmatrix}1\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}2\\-1\end{bmatrix}$의 내적을 구하고 두 벡터의 방향 관계를 말하십시오.
> **답.** 내적은 $0$이고, 두 벡터는 직교합니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=1\cdot2+2\cdot(-1)=2-2=0$입니다. 영벡터가 아닌 두 벡터의 내적이 0이면 직교합니다.

### 2.4 노름과 각도

벡터의 길이, 즉 노름을 내적으로 정의합니다.

$$
\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}=\sqrt{v_1^2+\cdots+v_n^2}
$$

이는 피타고라스 정리를 $n$차원으로 확장한 것입니다. 노름은 다음 성질을 만족합니다.

$$
\lVert\mathbf{v}\rVert\ge 0,\quad \lVert\mathbf{v}\rVert=0\iff\mathbf{v}=\mathbf{0},\qquad
\lVert c\mathbf{v}\rVert=|c|\,\lVert\mathbf{v}\rVert
$$

두 번째 성질은 스칼라배가 길이를 $|c|$배 한다는 뜻입니다. 노름이 1인 벡터를 단위벡터라고 하고, 영벡터가 아닌 $\mathbf{v}$를 그 노름으로 나누면

$$
\hat{\mathbf{v}}=\frac{\mathbf{v}}{\lVert\mathbf{v}\rVert}
$$

로 단위벡터를 얻습니다. 이를 정규화라고 합니다.

두 벡터 사이의 각도 $\theta$는 내적으로 정의합니다. 영벡터가 아닌 $\mathbf{u},\mathbf{v}$에 대해

$$
\cos\theta=\frac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert},\qquad 0\le\theta\le\pi
$$

이 정의가 뜻을 가지려면 우변이 항상 $[-1,1]$ 안에 있어야 하는데, 이는 다음 절의 코시-슈바르츠 부등식이 보장합니다. 내적이 0이면 $\cos\theta=0$, 즉 $\theta=90^\circ$이므로 두 벡터는 직교합니다.

> **문제 1.** (기초) $\mathbf{v}=\begin{bmatrix}3\\4\end{bmatrix}$의 노름을 구하십시오.
> **답.** $5$입니다.
> **풀이.** $\lVert\mathbf{v}\rVert=\sqrt{3^2+4^2}=\sqrt{9+16}=\sqrt{25}=5$입니다.

> **문제 2.** (표준) $\mathbf{v}=\begin{bmatrix}3\\4\end{bmatrix}$를 정규화하십시오.
> **답.** $\begin{bmatrix}3/5\\4/5\end{bmatrix}$입니다.
> **풀이.** 노름이 $5$이므로 $\hat{\mathbf{v}}=\tfrac15\begin{bmatrix}3\\4\end{bmatrix}=\begin{bmatrix}3/5\\4/5\end{bmatrix}$입니다. 확인하면 $(3/5)^2+(4/5)^2=9/25+16/25=1$입니다.

> **문제 3.** (표준) $\mathbf{u}=\begin{bmatrix}1\\0\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}1\\1\end{bmatrix}$ 사이의 각도를 구하십시오.
> **답.** $45^\circ$입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=1$, $\lVert\mathbf{u}\rVert=1$, $\lVert\mathbf{v}\rVert=\sqrt2$입니다. 따라서 $\cos\theta=\tfrac{1}{1\cdot\sqrt2}=\tfrac{1}{\sqrt2}$이고 $\theta=45^\circ$입니다.

> **문제 4.** (심화) $\lVert c\mathbf{v}\rVert=|c|\,\lVert\mathbf{v}\rVert$임을 정의로부터 보이십시오.
> **답.** 제곱근 안에서 $c^2$을 빼내면 $|c|$가 됩니다.
> **풀이.** $\lVert c\mathbf{v}\rVert=\sqrt{\sum_i (cv_i)^2}=\sqrt{c^2\sum_i v_i^2}=\sqrt{c^2}\sqrt{\sum_i v_i^2}=|c|\,\lVert\mathbf{v}\rVert$입니다. $\sqrt{c^2}=|c|$임에 유의합니다.

### 2.5 코시-슈바르츠 부등식과 삼각부등식

각도 정의가 성립하려면 다음 부등식이 필요합니다.

**코시-슈바르츠 부등식.** 임의의 $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$에 대해

$$
|\mathbf{u}\cdot\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert
$$

이고, 등호는 $\mathbf{u}$와 $\mathbf{v}$가 평행할 때만 성립합니다.

증명을 봅니다. $\mathbf{v}=\mathbf{0}$이면 양변이 0이므로 성립합니다. $\mathbf{v}\ne\mathbf{0}$이라 하고, 임의의 실수 $t$에 대해 $\lVert\mathbf{u}-t\mathbf{v}\rVert^2\ge 0$을 전개합니다.

$$
0\le\lVert\mathbf{u}-t\mathbf{v}\rVert^2
=(\mathbf{u}-t\mathbf{v})\cdot(\mathbf{u}-t\mathbf{v})
=\lVert\mathbf{u}\rVert^2-2t(\mathbf{u}\cdot\mathbf{v})+t^2\lVert\mathbf{v}\rVert^2
$$

이는 $t$에 대한 이차식이며 항상 0 이상이므로 판별식이 0 이하입니다.

$$
(2\,\mathbf{u}\cdot\mathbf{v})^2-4\lVert\mathbf{v}\rVert^2\lVert\mathbf{u}\rVert^2\le 0
$$

정리하면 $(\mathbf{u}\cdot\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$이고, 양변에 제곱근을 취하면 부등식을 얻습니다. 등호는 이차식이 실근을 가질 때, 즉 어떤 $t$에서 $\mathbf{u}-t\mathbf{v}=\mathbf{0}$일 때이므로 두 벡터가 평행할 때입니다.

이 부등식에서 곧바로 **삼각부등식**이 따라 나옵니다.

$$
\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert
$$

유도는 다음과 같습니다.

$$
\lVert\mathbf{u}+\mathbf{v}\rVert^2
=\lVert\mathbf{u}\rVert^2+2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2
\le\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2
=(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2
$$

가운데에서 $\mathbf{u}\cdot\mathbf{v}\le|\mathbf{u}\cdot\mathbf{v}|\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$을 썼습니다. 양변에 제곱근을 취하면 삼각부등식입니다. 기하적으로는 한 변의 길이가 다른 두 변의 합보다 클 수 없다는 뜻입니다.

> **문제 1.** (표준) $\mathbf{u}=\begin{bmatrix}1\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}2\\4\end{bmatrix}$에서 코시-슈바르츠 부등식의 등호가 성립하는지 확인하십시오.
> **답.** 등호가 성립합니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=1\cdot2+2\cdot4=10$이고 $\lVert\mathbf{u}\rVert=\sqrt5$, $\lVert\mathbf{v}\rVert=\sqrt{20}=2\sqrt5$이므로 $\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert=10$입니다. 좌변과 우변이 모두 $10$이고, $\mathbf{v}=2\mathbf{u}$로 평행하므로 등호가 성립합니다.

> **문제 2.** (표준) $\mathbf{u}=\begin{bmatrix}3\\0\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}0\\4\end{bmatrix}$에서 삼각부등식의 양변을 계산해 비교하십시오.
> **답.** 좌변 $5$, 우변 $7$로 좌변이 더 작습니다.
> **풀이.** $\mathbf{u}+\mathbf{v}=\begin{bmatrix}3\\4\end{bmatrix}$이므로 좌변은 $\lVert\mathbf{u}+\mathbf{v}\rVert=5$입니다. 우변은 $\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert=3+4=7$입니다. 두 벡터가 직교해 평행이 아니므로 등호가 아닌 진부등식 $5<7$이 성립합니다.

> **문제 3.** (심화) 코시-슈바르츠 부등식에서 판별식 조건이 왜 등장하는지 설명하십시오.
> **답.** 이차식이 모든 $t$에서 0 이상이려면 실근이 하나 이하여야 하고, 이는 판별식이 0 이하임과 같기 때문입니다.
> **풀이.** $f(t)=\lVert\mathbf{u}-t\mathbf{v}\rVert^2$은 노름의 제곱이라 항상 0 이상입니다. 위로 볼록한 이차식이 음수가 되지 않으려면 $t$축과 두 점에서 만날 수 없으므로 판별식이 0 이하입니다. 이 조건을 정리하면 코시-슈바르츠 부등식이 나옵니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 벡터 덧셈 | $(\mathbf{u}+\mathbf{v})_i=u_i+v_i$ | 같은 자리끼리 더한다 |
| 스칼라배 | $(c\mathbf{v})_i=cv_i$ | 모든 성분에 곱한다, 부호는 방향 반전 |
| 내적 | $\mathbf{u}\cdot\mathbf{v}=\sum u_iv_i$ | 곱해서 더한다, 결과는 스칼라 |
| 노름 | $\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}$ | 제곱합의 제곱근 |
| 정규화 | $\hat{\mathbf{v}}=\mathbf{v}/\lVert\mathbf{v}\rVert$ | 노름으로 나눈다, 영벡터 제외 |
| 각도 | $\cos\theta=\dfrac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$ | 내적을 노름 곱으로 나눈다 |
| 직교 판정 | $\mathbf{u}\cdot\mathbf{v}=0$ | 내적이 0이면 직교 |
| 코시-슈바르츠 | $|\mathbf{u}\cdot\mathbf{v}|\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$ | 등호는 평행일 때 |
| 삼각부등식 | $\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ | 한 변은 두 변 합 이하 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $\begin{bmatrix}2\\-1\\3\end{bmatrix}+\begin{bmatrix}1\\4\\-2\end{bmatrix}$을 구하십시오.
> **답.** $\begin{bmatrix}3\\3\\1\end{bmatrix}$입니다.
> **풀이.** 성분별로 $2+1=3$, $-1+4=3$, $3+(-2)=1$입니다.

> **문제 2.** (기초) $5\begin{bmatrix}2\\-1\end{bmatrix}$을 구하십시오.
> **답.** $\begin{bmatrix}10\\-5\end{bmatrix}$입니다.
> **풀이.** 모든 성분에 5를 곱하면 $5\cdot2=10$, $5\cdot(-1)=-5$입니다.

> **문제 3.** (기초) $\begin{bmatrix}1\\1\\1\end{bmatrix}\cdot\begin{bmatrix}2\\-3\\4\end{bmatrix}$을 구하십시오.
> **답.** $3$입니다.
> **풀이.** $1\cdot2+1\cdot(-3)+1\cdot4=2-3+4=3$입니다.

> **문제 4.** (기초) $\begin{bmatrix}-6\\8\end{bmatrix}$의 노름을 구하십시오.
> **답.** $10$입니다.
> **풀이.** $\sqrt{(-6)^2+8^2}=\sqrt{36+64}=\sqrt{100}=10$입니다.

> **문제 5.** (표준) $\mathbf{u}=\begin{bmatrix}1\\2\\2\end{bmatrix}$를 정규화하십시오.
> **답.** $\begin{bmatrix}1/3\\2/3\\2/3\end{bmatrix}$입니다.
> **풀이.** 노름은 $\sqrt{1+4+4}=3$이므로 각 성분을 3으로 나눕니다.

> **문제 6.** (표준) $\mathbf{u}=\begin{bmatrix}2\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}0\\3\end{bmatrix}$ 사이 각도를 구하십시오.
> **답.** $45^\circ$입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=0+6=6$, $\lVert\mathbf{u}\rVert=2\sqrt2$, $\lVert\mathbf{v}\rVert=3$이므로 $\cos\theta=\tfrac{6}{6\sqrt2}=\tfrac{1}{\sqrt2}$, $\theta=45^\circ$입니다.

> **문제 7.** (표준) $\mathbf{u}=\begin{bmatrix}k\\2\end{bmatrix}$가 $\mathbf{v}=\begin{bmatrix}3\\-6\end{bmatrix}$와 직교하도록 $k$를 구하십시오.
> **답.** $k=4$입니다.
> **풀이.** 직교 조건 $\mathbf{u}\cdot\mathbf{v}=0$은 $3k+2\cdot(-6)=0$, 즉 $3k-12=0$이므로 $k=4$입니다.

> **문제 8.** (표준) $\mathbf{u}=\begin{bmatrix}1\\-1\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}3\\1\end{bmatrix}$에 대해 $\lVert\mathbf{u}+\mathbf{v}\rVert^2$을 두 방법으로 구해 일치함을 보이십시오.
> **답.** 둘 다 $16$입니다.
> **풀이.** 직접 계산하면 $\mathbf{u}+\mathbf{v}=\begin{bmatrix}4\\0\end{bmatrix}$이므로 $\lVert\mathbf{u}+\mathbf{v}\rVert^2=4^2+0^2=16$입니다. 전개식으로는 $\lVert\mathbf{u}\rVert^2+2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2=2+2(2)+10=16$입니다($\mathbf{u}\cdot\mathbf{v}=3-1=2$). 두 방법 모두 $16$으로 일치합니다.

> **문제 9.** (표준) 세 벡터 $\mathbf{a}=\begin{bmatrix}1\\0\end{bmatrix}$, $\mathbf{b}=\begin{bmatrix}0\\1\end{bmatrix}$, $\mathbf{c}=\begin{bmatrix}2\\3\end{bmatrix}$에 대해 $\mathbf{c}=x\mathbf{a}+y\mathbf{b}$인 $x,y$를 구하십시오.
> **답.** $x=2$, $y=3$입니다.
> **풀이.** $x\mathbf{a}+y\mathbf{b}=\begin{bmatrix}x\\y\end{bmatrix}$이므로 $\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2\\3\end{bmatrix}$에서 $x=2$, $y=3$입니다.

> **문제 10.** (심화) $\mathbf{u},\mathbf{v}$가 직교하면 $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$임을 보이십시오.
> **답.** 교차항 $2(\mathbf{u}\cdot\mathbf{v})$가 0이 되기 때문입니다.
> **풀이.** $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2$인데 직교하면 $\mathbf{u}\cdot\mathbf{v}=0$이므로 교차항이 사라집니다. 이것이 피타고라스 정리의 벡터 형태입니다.

> **문제 11.** (심화) 임의의 단위벡터 $\hat{\mathbf{v}}$에 대해 $\mathbf{u}\cdot\hat{\mathbf{v}}$가 $\mathbf{u}$의 $\hat{\mathbf{v}}$ 방향 성분의 크기임을 각도 정의로 설명하십시오.
> **답.** $\mathbf{u}\cdot\hat{\mathbf{v}}=\lVert\mathbf{u}\rVert\cos\theta$이므로 $\hat{\mathbf{v}}$ 방향으로 사영한 길이입니다.
> **풀이.** $\mathbf{u}\cdot\hat{\mathbf{v}}=\lVert\mathbf{u}\rVert\lVert\hat{\mathbf{v}}\rVert\cos\theta=\lVert\mathbf{u}\rVert\cos\theta$입니다($\lVert\hat{\mathbf{v}}\rVert=1$). 이는 직각삼각형에서 빗변 $\lVert\mathbf{u}\rVert$의 $\hat{\mathbf{v}}$ 방향 밑변 길이이므로 사영 성분입니다.

> **문제 12.** (심화) $\mathbf{u}=\begin{bmatrix}1\\2\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}2\\0\\1\end{bmatrix}$에서 코시-슈바르츠 부등식이 성립함을 수치로 확인하십시오.
> **답.** $|\mathbf{u}\cdot\mathbf{v}|=4\le 3\sqrt5\approx6.7$로 성립합니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=2+0+2=4$, $\lVert\mathbf{u}\rVert=3$, $\lVert\mathbf{v}\rVert=\sqrt5$이므로 우변은 $3\sqrt5\approx6.7$입니다. $4\le6.7$이므로 부등식이 성립하고, 평행이 아니라 진부등식입니다.

## 5. 스스로 점검

1. 벡터의 대수적 정의와 기하적 정의를 각각 말할 수 있는가?
2. 벡터 덧셈과 스칼라배를 성분으로 정의할 수 있는가?
3. 내적을 정의하고 그 결과가 스칼라임을 설명할 수 있는가?
4. 노름을 내적으로 정의하고 $\lVert c\mathbf{v}\rVert=|c|\lVert\mathbf{v}\rVert$을 증명할 수 있는가?
5. 두 벡터 사이 각도를 내적으로 표현할 수 있는가?
6. 코시-슈바르츠 부등식을 진술하고 등호 조건을 말할 수 있는가?
7. 삼각부등식을 코시-슈바르츠에서 유도할 수 있는가?

**정답 요지.** 1. 순서 있는 실수 목록 / 방향과 크기를 가진 화살표. 2. $(\mathbf{u}+\mathbf{v})_i=u_i+v_i$, $(c\mathbf{v})_i=cv_i$. 3. $\sum u_iv_i$, 실수 하나. 4. $\sqrt{\sum(cv_i)^2}=|c|\sqrt{\sum v_i^2}$. 5. $\cos\theta=\frac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$. 6. $|\mathbf{u}\cdot\mathbf{v}|\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$, 등호는 평행. 7. $\lVert\mathbf{u}+\mathbf{v}\rVert^2$ 전개 후 교차항에 코시-슈바르츠 적용.
</content>
