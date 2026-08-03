---
title: "2. 벡터공간과 부분공간"
---
# 2강. 벡터공간과 부분공간

## 이 강의에서 할 수 있게 되는 것

- 벡터공간을 여덟 개의 공리로 정의할 수 있습니다.
- 주어진 집합이 부분공간인지 세 조건으로 판정할 수 있습니다.
- 일차결합과 생성(span)의 뜻을 정확히 진술할 수 있습니다.
- 열공간, 영공간 같은 대표적 부분공간을 구별할 수 있습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $V$ | 벡터공간 브이 | 공리를 만족하는 벡터들의 집합 |
| $W\subseteq V$ | 더블유는 브이의 부분집합 | $W$가 $V$의 부분집합 |
| $\mathbf{0}$ | 영벡터 | 덧셈의 항등원 |
| $c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k$ | 일차결합 | 벡터들에 스칼라를 곱해 더한 것 |
| $\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$ | 스팬 | 벡터들의 모든 일차결합의 집합 |
| $\operatorname{Col}(A)$ | 콜 오브 에이 | 행렬 $A$의 열공간 |
| $\operatorname{Nul}(A)$ | 널 오브 에이 | 행렬 $A$의 영공간 |
| $P_n$ | 피 엔 | 차수가 $n$ 이하인 다항식의 공간 |

## 2. 개념

### 2.1 벡터공간의 공리

1강에서 $\mathbb{R}^n$의 덧셈과 스칼라배가 여덟 가지 성질을 만족함을 봤습니다. 이 성질들을 만족하는 임의의 집합을 벡터공간이라고 부르면, $\mathbb{R}^n$뿐 아니라 다항식, 함수, 행렬의 집합도 같은 언어로 다룰 수 있습니다.

**정의.** 집합 $V$에 덧셈과 스칼라배가 정의되어 있고, 임의의 $\mathbf{u},\mathbf{v},\mathbf{w}\in V$와 스칼라 $c,d\in\mathbb{R}$에 대해 다음 여덟 공리를 모두 만족하면 $V$를 (실)벡터공간이라고 합니다.

1. $\mathbf{u}+\mathbf{v}\in V$ (덧셈에 대한 닫힘)
2. $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$
3. $(\mathbf{u}+\mathbf{v})+\mathbf{w}=\mathbf{u}+(\mathbf{v}+\mathbf{w})$
4. $\mathbf{u}+\mathbf{0}=\mathbf{u}$인 영벡터 $\mathbf{0}$이 존재
5. 각 $\mathbf{u}$에 대해 $\mathbf{u}+(-\mathbf{u})=\mathbf{0}$인 $-\mathbf{u}$가 존재
6. $c\mathbf{u}\in V$ (스칼라배에 대한 닫힘)
7. $c(\mathbf{u}+\mathbf{v})=c\mathbf{u}+c\mathbf{v}$, $(c+d)\mathbf{u}=c\mathbf{u}+d\mathbf{u}$
8. $c(d\mathbf{u})=(cd)\mathbf{u}$, $1\mathbf{u}=\mathbf{u}$

직관은 이렇습니다. 벡터공간이란 그 안에서 덧셈과 스칼라배를 아무리 해도 밖으로 나가지 않고, 그 연산이 익숙한 규칙을 따르는 세계입니다. $\mathbb{R}^n$이 가장 기본 예이고, 차수가 $n$ 이하인 다항식의 집합 $P_n$, $m\times n$ 실행렬 전체, 실수 구간에서 정의된 연속함수 전체도 모두 벡터공간입니다.

> **문제 1.** (기초) $\mathbb{R}^2$가 공리 4를 만족하도록 하는 영벡터는 무엇입니까?
> **답.** $\mathbf{0}=\begin{bmatrix}0\\0\end{bmatrix}$입니다.
> **풀이.** 임의의 $\mathbf{u}=\begin{bmatrix}u_1\\u_2\end{bmatrix}$에 대해 $\mathbf{u}+\mathbf{0}=\begin{bmatrix}u_1+0\\u_2+0\end{bmatrix}=\mathbf{u}$가 되려면 두 성분이 모두 0이어야 합니다.

> **문제 2.** (기초) 차수가 2 이하인 다항식 $p(x)=1+2x$와 $q(x)=3x-x^2$의 합이 $P_2$ 안에 있는지 확인하십시오.
> **답.** $P_2$ 안에 있습니다.
> **풀이.** $p(x)+q(x)=1+5x-x^2$이고 차수가 2이므로 $P_2$에 속합니다. 다항식 덧셈은 차수를 높이지 않으므로 닫힘이 성립합니다.

> **문제 3.** (표준) 실수 전체 $\mathbb{R}$을 스칼라가 실수인 벡터공간으로 볼 수 있는지 설명하십시오.
> **답.** 볼 수 있습니다.
> **풀이.** $\mathbb{R}$은 1차원 벡터공간 $\mathbb{R}^1$과 같습니다. 실수 덧셈과 실수배가 여덟 공리를 모두 만족하므로 벡터공간입니다.

### 2.2 부분공간

큰 벡터공간 안에 그 자체로 벡터공간이 되는 부분집합이 자주 나타납니다. 이를 부분공간이라고 합니다.

**정의.** 벡터공간 $V$의 부분집합 $W$가 다음 세 조건을 만족하면 $W$를 $V$의 부분공간이라고 합니다.

1. $\mathbf{0}\in W$ (영벡터 포함)
2. $\mathbf{u},\mathbf{v}\in W \Rightarrow \mathbf{u}+\mathbf{v}\in W$ (덧셈에 닫힘)
3. $\mathbf{u}\in W,\ c\in\mathbb{R} \Rightarrow c\mathbf{u}\in W$ (스칼라배에 닫힘)

왜 세 조건만으로 충분한지 봅니다. 나머지 공리(교환, 결합, 분배 등)는 $W$가 $V$의 부분집합이므로 $V$에서 이미 성립하고, $W$가 두 연산에 대해 닫혀 있기만 하면 그 성립이 그대로 물려받아집니다. 조건 1은 $W$가 비어 있지 않고 항등원을 가짐을 보장합니다. 실제로 조건 2와 3에서 $c=-1$을 쓰면 역원도 자동으로 $W$ 안에 들어옵니다.

부분공간을 판정할 때 가장 빠른 첫 점검은 "$\mathbf{0}$을 포함하는가"입니다. 영벡터를 포함하지 않으면 곧바로 부분공간이 아닙니다.

예를 들어 $\mathbb{R}^2$에서 원점을 지나는 직선 $\{c\begin{bmatrix}1\\2\end{bmatrix}:c\in\mathbb{R}\}$은 부분공간입니다. 반면 원점을 지나지 않는 직선 $\{\begin{bmatrix}1\\0\end{bmatrix}+c\begin{bmatrix}1\\2\end{bmatrix}\}$은 $\mathbf{0}$을 포함하지 않아 부분공간이 아닙니다.

> **문제 1.** (기초) $W=\{\begin{bmatrix}x\\0\end{bmatrix}:x\in\mathbb{R}\}$이 $\mathbb{R}^2$의 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** $\mathbf{0}=\begin{bmatrix}0\\0\end{bmatrix}\in W$입니다. 두 원소의 합 $\begin{bmatrix}x_1\\0\end{bmatrix}+\begin{bmatrix}x_2\\0\end{bmatrix}=\begin{bmatrix}x_1+x_2\\0\end{bmatrix}$도 둘째 성분이 0이라 $W$에 있고, $c\begin{bmatrix}x\\0\end{bmatrix}=\begin{bmatrix}cx\\0\end{bmatrix}$도 $W$에 있습니다. 세 조건을 만족합니다.

> **문제 2.** (표준) $W=\{\begin{bmatrix}x\\y\end{bmatrix}:x+y=1\}$이 $\mathbb{R}^2$의 부분공간인지 판정하십시오.
> **답.** 부분공간이 아닙니다.
> **풀이.** $\mathbf{0}=\begin{bmatrix}0\\0\end{bmatrix}$은 $0+0=0\ne1$이므로 $W$에 속하지 않습니다. 영벡터를 포함하지 않으므로 부분공간이 아닙니다.

> **문제 3.** (표준) $W=\{\begin{bmatrix}x\\y\end{bmatrix}:x+y=0\}$이 $\mathbb{R}^2$의 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** $0+0=0$이므로 $\mathbf{0}\in W$입니다. $\begin{bmatrix}x_1\\y_1\end{bmatrix},\begin{bmatrix}x_2\\y_2\end{bmatrix}\in W$이면 $(x_1+x_2)+(y_1+y_2)=(x_1+y_1)+(x_2+y_2)=0$이라 합도 $W$에 있고, $c$배도 $cx+cy=c(x+y)=0$이라 $W$에 있습니다.

> **문제 4.** (표준) $W=\{\begin{bmatrix}x\\y\end{bmatrix}:xy=0\}$이 $\mathbb{R}^2$의 부분공간인지 판정하십시오.
> **답.** 부분공간이 아닙니다.
> **풀이.** $\mathbf{0}\in W$이고 스칼라배에는 닫혀 있지만, 덧셈에는 닫혀 있지 않습니다. $\begin{bmatrix}1\\0\end{bmatrix}$과 $\begin{bmatrix}0\\1\end{bmatrix}$은 각각 곱이 0이라 $W$에 있으나, 합 $\begin{bmatrix}1\\1\end{bmatrix}$은 $1\cdot1=1\ne0$이라 $W$에 없습니다.

> **문제 5.** (심화) 부분공간의 조건 2, 3이 성립하면 조건 "각 $\mathbf{u}\in W$에 대해 $-\mathbf{u}\in W$"가 자동으로 따라옴을 보이십시오.
> **답.** 스칼라 $-1$을 곱하면 됩니다.
> **풀이.** 조건 3에서 $c=-1$을 택하면 $(-1)\mathbf{u}=-\mathbf{u}\in W$입니다. 따라서 역원의 존재를 따로 요구할 필요가 없습니다.

### 2.3 일차결합과 생성

부분공간을 만드는 가장 자연스러운 방법이 생성입니다. 먼저 일차결합을 정의합니다.

**정의.** 벡터 $\mathbf{v}_1,\dots,\mathbf{v}_k$와 스칼라 $c_1,\dots,c_k$에 대해

$$
c_1\mathbf{v}_1+c_2\mathbf{v}_2+\cdots+c_k\mathbf{v}_k
$$

를 이 벡터들의 일차결합이라고 합니다. 이 벡터들로 만들 수 있는 모든 일차결합의 집합을 생성이라고 하고

$$
\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}
=\{c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k : c_1,\dots,c_k\in\mathbb{R}\}
$$

로 씁니다.

**정리.** $\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$는 항상 부분공간입니다.

증명은 세 조건을 확인하면 됩니다. 모든 $c_i=0$으로 두면 $\mathbf{0}$을 얻으므로 영벡터를 포함합니다. 두 일차결합의 합은 다시 같은 벡터들의 일차결합이고(대응 계수끼리 더함), 일차결합의 스칼라배도 계수 전체에 그 스칼라를 곱한 일차결합이므로 두 연산에 닫혀 있습니다. 따라서 부분공간입니다.

직관적으로 $\operatorname{span}$은 주어진 벡터들을 재료로 도달할 수 있는 모든 점의 집합입니다. $\mathbb{R}^3$에서 한 벡터의 span은 직선, 평행하지 않은 두 벡터의 span은 평면입니다.

> **문제 1.** (기초) $\begin{bmatrix}3\\6\end{bmatrix}$이 $\operatorname{span}\{\begin{bmatrix}1\\2\end{bmatrix}\}$에 속하는지 판정하십시오.
> **답.** 속합니다.
> **풀이.** $\begin{bmatrix}3\\6\end{bmatrix}=3\begin{bmatrix}1\\2\end{bmatrix}$이므로 계수 $c=3$인 일차결합입니다. 따라서 span에 속합니다.

> **문제 2.** (표준) $\begin{bmatrix}1\\1\end{bmatrix}$이 $\operatorname{span}\{\begin{bmatrix}2\\0\end{bmatrix},\begin{bmatrix}0\\3\end{bmatrix}\}$에 속하는지 판정하십시오.
> **답.** 속합니다.
> **풀이.** $c_1\begin{bmatrix}2\\0\end{bmatrix}+c_2\begin{bmatrix}0\\3\end{bmatrix}=\begin{bmatrix}2c_1\\3c_2\end{bmatrix}=\begin{bmatrix}1\\1\end{bmatrix}$에서 $c_1=\tfrac12$, $c_2=\tfrac13$입니다. 해가 존재하므로 속합니다.

> **문제 3.** (표준) $\operatorname{span}\{\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}0\\1\\0\end{bmatrix}\}$은 $\mathbb{R}^3$에서 무엇을 이루는지 말하십시오.
> **답.** $xy$평면입니다.
> **풀이.** 두 벡터의 일차결합은 $\begin{bmatrix}c_1\\c_2\\0\end{bmatrix}$ 형태로 셋째 성분이 항상 0입니다. 이는 $z=0$인 평면, 즉 $xy$평면입니다.

> **문제 4.** (심화) $\operatorname{span}\{\mathbf{v}_1,\mathbf{v}_2\}$가 부분공간임을 세 조건으로 직접 확인하십시오.
> **답.** 영벡터 포함, 덧셈 닫힘, 스칼라배 닫힘이 모두 성립합니다.
> **풀이.** $0\mathbf{v}_1+0\mathbf{v}_2=\mathbf{0}$이라 영벡터를 포함합니다. $(a_1\mathbf{v}_1+a_2\mathbf{v}_2)+(b_1\mathbf{v}_1+b_2\mathbf{v}_2)=(a_1+b_1)\mathbf{v}_1+(a_2+b_2)\mathbf{v}_2$로 다시 일차결합이라 덧셈에 닫혀 있고, $c(a_1\mathbf{v}_1+a_2\mathbf{v}_2)=(ca_1)\mathbf{v}_1+(ca_2)\mathbf{v}_2$로 스칼라배에도 닫혀 있습니다.

### 2.4 행렬이 만드는 부분공간: 열공간과 영공간

행렬 $A$는 두 개의 중요한 부분공간을 낳습니다. 이는 다음 단원의 선형변환과 연립방정식으로 곧장 이어집니다.

**열공간.** $A$의 열벡터들이 생성하는 부분공간을 열공간이라고 합니다. $A=[\mathbf{a}_1\ \cdots\ \mathbf{a}_n]$이면

$$
\operatorname{Col}(A)=\operatorname{span}\{\mathbf{a}_1,\dots,\mathbf{a}_n\}=\{A\mathbf{x}:\mathbf{x}\in\mathbb{R}^n\}
$$

두 표현이 같은 이유는 $A\mathbf{x}=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n$이 바로 열벡터들의 일차결합이기 때문입니다. 따라서 $A\mathbf{x}=\mathbf{b}$가 해를 가질 필요충분조건은 $\mathbf{b}\in\operatorname{Col}(A)$입니다.

**영공간.** $A\mathbf{x}=\mathbf{0}$을 만족하는 모든 $\mathbf{x}$의 집합을 영공간이라고 합니다.

$$
\operatorname{Nul}(A)=\{\mathbf{x}\in\mathbb{R}^n : A\mathbf{x}=\mathbf{0}\}
$$

영공간이 부분공간임을 확인합니다. $A\mathbf{0}=\mathbf{0}$이라 $\mathbf{0}\in\operatorname{Nul}(A)$이고, $A\mathbf{x}_1=\mathbf{0}$, $A\mathbf{x}_2=\mathbf{0}$이면 $A(\mathbf{x}_1+\mathbf{x}_2)=\mathbf{0}$, $A(c\mathbf{x})=cA\mathbf{x}=\mathbf{0}$이므로 두 연산에 닫혀 있습니다. 여기서 행렬곱의 선형성 $A(\mathbf{x}+\mathbf{y})=A\mathbf{x}+A\mathbf{y}$와 $A(c\mathbf{x})=cA\mathbf{x}$을 사용했습니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&0\\0&1\end{bmatrix}$의 열공간은 무엇입니까?
> **답.** $\mathbb{R}^2$ 전체입니다.
> **풀이.** 두 열 $\begin{bmatrix}1\\0\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}$의 일차결합으로 $\mathbb{R}^2$의 임의의 벡터 $\begin{bmatrix}x\\y\end{bmatrix}$를 $x\begin{bmatrix}1\\0\end{bmatrix}+y\begin{bmatrix}0\\1\end{bmatrix}$로 만들 수 있습니다.

> **문제 2.** (표준) $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$의 영공간을 구하십시오.
> **답.** $\operatorname{Nul}(A)=\operatorname{span}\{\begin{bmatrix}-2\\1\end{bmatrix}\}$입니다.
> **풀이.** $A\mathbf{x}=\mathbf{0}$은 $x_1+2x_2=0$ 하나로 요약됩니다(둘째 식은 첫 식의 2배). $x_1=-2x_2$이므로 $\mathbf{x}=x_2\begin{bmatrix}-2\\1\end{bmatrix}$입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$의 열공간을 구하십시오.
> **답.** $\operatorname{Col}(A)=\operatorname{span}\{\begin{bmatrix}1\\2\end{bmatrix}\}$인 직선입니다.
> **풀이.** 둘째 열 $\begin{bmatrix}2\\4\end{bmatrix}=2\begin{bmatrix}1\\2\end{bmatrix}$은 첫째 열의 배수라 새 방향을 더하지 않습니다. 따라서 열공간은 $\begin{bmatrix}1\\2\end{bmatrix}$이 생성하는 직선입니다.

> **문제 4.** (심화) 영공간이 부분공간임을 세 조건으로 보이십시오.
> **답.** $A$의 선형성으로 세 조건이 성립합니다.
> **풀이.** $A\mathbf{0}=\mathbf{0}$이라 $\mathbf{0}\in\operatorname{Nul}(A)$입니다. $A\mathbf{x}_1=A\mathbf{x}_2=\mathbf{0}$이면 $A(\mathbf{x}_1+\mathbf{x}_2)=A\mathbf{x}_1+A\mathbf{x}_2=\mathbf{0}$, $A(c\mathbf{x}_1)=cA\mathbf{x}_1=\mathbf{0}$입니다. 세 조건이 모두 성립합니다.

## 3. 유형 총정리(치트시트)

| 유형 | 판정 방법 | 요령 |
|---|---|---|
| 벡터공간 여부 | 여덟 공리 확인 | 닫힘 두 개가 자주 깨진다 |
| 부분공간 여부 | $\mathbf{0}$ 포함, 덧셈 닫힘, 스칼라배 닫힘 | $\mathbf{0}$부터 확인 |
| 부분공간 아님 반례 | 두 원소의 합이 밖으로 나감 | 곱=0 같은 비선형 조건 의심 |
| 일차결합 | $c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k$ | 계수를 미지수로 놓고 방정식 |
| span 소속 | 일차결합 방정식의 해 존재 여부 | 해 있으면 소속 |
| 열공간 | $\operatorname{Col}(A)=\{A\mathbf{x}\}$ | $A\mathbf{x}=\mathbf{b}$ 해 존재 $\iff$ $\mathbf{b}\in\operatorname{Col}(A)$ |
| 영공간 | $A\mathbf{x}=\mathbf{0}$의 해집합 | 항상 부분공간 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $W=\{\begin{bmatrix}0\\y\\z\end{bmatrix}:y,z\in\mathbb{R}\}$이 $\mathbb{R}^3$의 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** 첫 성분이 0인 벡터들의 집합입니다. $\mathbf{0}$을 포함하고, 합과 스칼라배 모두 첫 성분이 0으로 유지되므로 세 조건을 만족합니다.

> **문제 2.** (기초) $W=\{\begin{bmatrix}x\\y\end{bmatrix}:x\ge0\}$이 부분공간인지 판정하십시오.
> **답.** 부분공간이 아닙니다.
> **풀이.** $\begin{bmatrix}1\\0\end{bmatrix}\in W$이지만 $(-1)\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}-1\\0\end{bmatrix}$은 첫 성분이 음수라 $W$에 없습니다. 스칼라배에 닫혀 있지 않습니다.

> **문제 3.** (표준) $\begin{bmatrix}4\\5\end{bmatrix}$이 $\operatorname{span}\{\begin{bmatrix}1\\1\end{bmatrix},\begin{bmatrix}1\\2\end{bmatrix}\}$에 속하는지 판정하십시오.
> **답.** 속합니다.
> **풀이.** $c_1\begin{bmatrix}1\\1\end{bmatrix}+c_2\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}c_1+c_2\\c_1+2c_2\end{bmatrix}=\begin{bmatrix}4\\5\end{bmatrix}$입니다. 두 식을 빼면 $c_2=1$, 대입하면 $c_1=3$입니다. 해가 있으므로 속합니다.

> **문제 4.** (표준) $\operatorname{span}\{\begin{bmatrix}1\\2\end{bmatrix},\begin{bmatrix}2\\4\end{bmatrix}\}$은 $\mathbb{R}^2$ 전체인지 판정하십시오.
> **답.** 전체가 아니라 직선입니다.
> **풀이.** 둘째 벡터가 첫째의 2배라 새 방향을 주지 않습니다. 두 벡터의 일차결합은 모두 $\begin{bmatrix}1\\2\end{bmatrix}$ 방향의 직선 위에 놓입니다. 예를 들어 $\begin{bmatrix}1\\0\end{bmatrix}$은 이 직선 위에 없습니다.

> **문제 5.** (표준) $A=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$의 영공간을 구하십시오.
> **답.** $\operatorname{Nul}(A)=\{\mathbf{0}\}$입니다.
> **풀이.** $x_1+x_2=0$, $x_1-x_2=0$을 더하면 $2x_1=0$이라 $x_1=0$, 따라서 $x_2=0$입니다. 자명해만 있으므로 영공간은 영벡터 하나입니다.

> **문제 6.** (표준) 다항식 공간 $P_2$에서 $W=\{p\in P_2 : p(0)=0\}$이 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** 영다항식은 $0$에서 값이 0이라 $W$에 있습니다. $p(0)=q(0)=0$이면 $(p+q)(0)=0$, $(cp)(0)=0$이므로 두 연산에 닫혀 있습니다.

> **문제 7.** (표준) $\mathbb{R}^3$에서 $W=\{\begin{bmatrix}x\\y\\z\end{bmatrix}:x+2y-z=0\}$이 부분공간인지 판정하고, 생성 벡터를 구하십시오.
> **답.** 부분공간이며 $\operatorname{span}\{\begin{bmatrix}-2\\1\\0\end{bmatrix},\begin{bmatrix}1\\0\\1\end{bmatrix}\}$입니다.
> **풀이.** $x+2y-z=0$은 원점을 지나는 평면이라 부분공간입니다. $x=-2y+z$로 두면 $\begin{bmatrix}x\\y\\z\end{bmatrix}=y\begin{bmatrix}-2\\1\\0\end{bmatrix}+z\begin{bmatrix}1\\0\\1\end{bmatrix}$입니다.

> **문제 8.** (심화) 두 부분공간 $U,W\subseteq V$의 교집합 $U\cap W$가 부분공간임을 보이십시오.
> **답.** 세 조건이 양쪽에서 동시에 성립하므로 부분공간입니다.
> **풀이.** $\mathbf{0}$은 $U,W$ 모두에 있으므로 교집합에 있습니다. $\mathbf{x},\mathbf{y}\in U\cap W$이면 $\mathbf{x}+\mathbf{y}$가 $U$에도 $W$에도 있으므로 교집합에 있고, $c\mathbf{x}$도 마찬가지입니다.

> **문제 9.** (심화) 두 부분공간의 합집합 $U\cup W$는 일반적으로 부분공간이 아님을 반례로 보이십시오.
> **답.** $x$축과 $y$축의 합집합이 반례입니다.
> **풀이.** $\mathbb{R}^2$에서 $U$를 $x$축, $W$를 $y$축이라 하면 $\begin{bmatrix}1\\0\end{bmatrix}\in U$, $\begin{bmatrix}0\\1\end{bmatrix}\in W$이지만 합 $\begin{bmatrix}1\\1\end{bmatrix}$은 어느 축에도 없습니다. 덧셈에 닫혀 있지 않으므로 부분공간이 아닙니다.

> **문제 10.** (심화) $A\mathbf{x}=\mathbf{b}$가 $\mathbf{b}\ne\mathbf{0}$일 때 그 해집합이 부분공간이 아닌 이유를 말하십시오.
> **답.** 영벡터를 포함하지 않기 때문입니다.
> **풀이.** $\mathbf{x}=\mathbf{0}$이면 $A\mathbf{0}=\mathbf{0}\ne\mathbf{b}$이므로 $\mathbf{0}$은 해가 아닙니다. 영벡터를 포함하지 않으므로 부분공간이 아닙니다. 다만 해집합은 특수해에 영공간을 더한 아핀 집합입니다.

## 5. 스스로 점검

1. 벡터공간의 여덟 공리를 큰 항목으로 나눠 말할 수 있는가?
2. 부분공간 판정의 세 조건을 말할 수 있는가?
3. 부분공간이 아님을 보이려면 무엇을 찾아야 하는가?
4. 일차결합과 span의 정의를 진술할 수 있는가?
5. span이 항상 부분공간인 이유를 설명할 수 있는가?
6. 열공간과 영공간을 정의하고 구별할 수 있는가?
7. $A\mathbf{x}=\mathbf{b}$의 가해성이 열공간과 어떻게 연결되는가?

**정답 요지.** 1. 덧셈 관련(닫힘·교환·결합·항등원·역원)과 스칼라배 관련(닫힘·분배·결합·항등). 2. $\mathbf{0}$ 포함, 덧셈 닫힘, 스칼라배 닫힘. 3. 세 조건 중 하나를 깨는 반례(특히 합이 밖으로 나가는 예). 4. 일차결합은 $\sum c_i\mathbf{v}_i$, span은 그 전체 집합. 5. 영벡터 포함하고 두 연산에 닫혀 있으므로. 6. 열공간은 열의 span=$\{A\mathbf{x}\}$, 영공간은 $A\mathbf{x}=\mathbf{0}$의 해집합. 7. $A\mathbf{x}=\mathbf{b}$가 풀림 $\iff$ $\mathbf{b}\in\operatorname{Col}(A)$.
