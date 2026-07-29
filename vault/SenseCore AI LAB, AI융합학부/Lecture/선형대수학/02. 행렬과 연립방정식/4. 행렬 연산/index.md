---
title: "4. 행렬 연산"
---
# 4강. 행렬 연산

## 이 강의에서 할 수 있게 되는 것

- 행렬을 수를 직사각형으로 배열한 대상으로 정의하고 크기와 성분을 말할 수 있습니다.
- 행렬의 덧셈과 스칼라배를 정의하고 그 성질을 진술할 수 있습니다.
- 행렬 곱셈을 정의하고 결합법칙과 분배법칙은 성립하지만 교환법칙은 일반적으로 성립하지 않음을 설명할 수 있습니다.
- 전치를 정의하고 단위행렬, 대각행렬, 대칭행렬 같은 특수 행렬을 구별할 수 있습니다.

이 강의는 1단원에서 다룬 벡터를 여러 개 나란히 묶은 행렬을 다룹니다. 이 교본은 정의와 유도를 중심으로 진행합니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $A$ | 행렬 에이 | 수를 직사각형으로 배열한 대상 |
| $A\in\mathbb{R}^{m\times n}$ | 엠 바이 엔 행렬 | 행이 $m$개, 열이 $n$개인 실행렬 |
| $a_{ij}$ | 에이 아이 제이 | $i$번째 행, $j$번째 열의 성분 |
| $A+B$ | 에이 플러스 비 | 같은 크기 두 행렬의 덧셈 |
| $cA$ | 씨 에이 | 스칼라 $c$를 곱한 스칼라배 |
| $AB$ | 에이 비 | 두 행렬의 곱 |
| $A^{T}$ | 에이 전치 | 행과 열을 맞바꾼 행렬 |
| $I_n$ | 단위행렬 | 대각 성분이 1, 나머지가 0인 정사각행렬 |
| $O$ | 영행렬 | 모든 성분이 0인 행렬 |

## 2. 개념

### 2.1 행렬의 정의와 표기

정의부터 세웁니다. 실수를 행이 $m$개, 열이 $n$개가 되도록 직사각형으로 배열한 것을 $m\times n$ 행렬이라고 하고, 이들의 집합을 $\mathbb{R}^{m\times n}$이라고 씁니다.

$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

$a_{ij}$는 $i$번째 행과 $j$번째 열이 만나는 자리의 성분입니다. 앞 첨자가 행, 뒤 첨자가 열이라는 순서가 핵심입니다. 행의 수와 열의 수가 같아 $m=n$이면 정사각행렬이라고 합니다. 열이 하나뿐인 $m\times1$ 행렬은 열벡터이고, 행이 하나뿐인 $1\times n$ 행렬은 행벡터입니다. 즉 벡터는 행렬의 특수한 경우입니다.

두 행렬이 같으려면 크기가 같고 대응하는 모든 성분이 같아야 합니다.

> **문제 1.** (기초) $A=\begin{bmatrix}2&-1&0\\3&4&5\end{bmatrix}$의 크기와 성분 $a_{23}$을 말하십시오.
> **답.** 크기는 $2\times3$, $a_{23}=5$입니다.
> **풀이.** 행이 2개, 열이 3개이므로 $2\times3$입니다. $a_{23}$은 둘째 행 셋째 열의 성분이므로 $5$입니다.

> **문제 2.** (기초) $\begin{bmatrix}x&2\\3&y\end{bmatrix}=\begin{bmatrix}5&2\\3&-1\end{bmatrix}$이 성립하는 $x,y$를 구하십시오.
> **답.** $x=5$, $y=-1$입니다.
> **풀이.** 두 행렬이 같으려면 같은 자리 성분이 모두 같아야 합니다. $(1,1)$ 성분에서 $x=5$, $(2,2)$ 성분에서 $y=-1$입니다.

> **문제 3.** (표준) $3\times2$ 행렬의 성분은 모두 몇 개이며, 정사각행렬이 되려면 어떤 조건이 필요한지 말하십시오.
> **답.** 성분은 6개이고, 정사각행렬이 되려면 행과 열의 수가 같아야 합니다.
> **풀이.** 성분 수는 행의 수 곱하기 열의 수이므로 $3\times2=6$개입니다. $3\times2$는 행이 3, 열이 2로 다르므로 정사각행렬이 아닙니다. 정사각행렬은 $m=n$인 경우입니다.

### 2.2 행렬의 덧셈과 스칼라배

크기가 같은 두 행렬의 덧셈은 같은 자리 성분끼리 더해 정의합니다.

$$
(A+B)_{ij}=a_{ij}+b_{ij}
$$

크기가 다르면 덧셈이 정의되지 않습니다. 스칼라 $c\in\mathbb{R}$와 행렬의 곱, 즉 스칼라배는 모든 성분에 $c$를 곱해 정의합니다.

$$
(cA)_{ij}=c\,a_{ij}
$$

이 두 연산은 벡터의 경우와 같은 성질을 만족합니다. 같은 크기 $A,B,C$와 스칼라 $c,d$에 대해

$$
A+B=B+A,\qquad (A+B)+C=A+(B+C)
$$

$$
A+O=A,\qquad A+(-A)=O
$$

$$
c(A+B)=cA+cB,\qquad (c+d)A=cA+dA,\qquad c(dA)=(cd)A
$$

가 성립합니다. 각 성질은 성분별 실수 계산으로 바로 증명됩니다. 예를 들어 교환법칙은 각 성분에서 $a_{ij}+b_{ij}=b_{ij}+a_{ij}$가 실수 덧셈의 교환법칙으로 성립하기 때문입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, $B=\begin{bmatrix}0&-1\\5&2\end{bmatrix}$일 때 $A+B$를 구하십시오.
> **답.** $\begin{bmatrix}1&1\\8&6\end{bmatrix}$입니다.
> **풀이.** 같은 자리끼리 더합니다. $(1,1)$은 $1+0=1$, $(1,2)$는 $2-1=1$, $(2,1)$은 $3+5=8$, $(2,2)$는 $4+2=6$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}2&-4\\6&0\end{bmatrix}$일 때 $\tfrac12 A$를 구하십시오.
> **답.** $\begin{bmatrix}1&-2\\3&0\end{bmatrix}$입니다.
> **풀이.** 모든 성분에 $\tfrac12$을 곱합니다. $\tfrac12\cdot2=1$, $\tfrac12\cdot(-4)=-2$, $\tfrac12\cdot6=3$, $\tfrac12\cdot0=0$입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&0\\2&1\end{bmatrix}$, $B=\begin{bmatrix}3&1\\0&4\end{bmatrix}$일 때 $2A-B$를 구하십시오.
> **답.** $\begin{bmatrix}-1&-1\\4&-2\end{bmatrix}$입니다.
> **풀이.** $2A=\begin{bmatrix}2&0\\4&2\end{bmatrix}$입니다. 여기서 $B$를 빼면 $(1,1)$은 $2-3=-1$, $(1,2)$는 $0-1=-1$, $(2,1)$은 $4-0=4$, $(2,2)$는 $2-4=-2$입니다.

> **문제 4.** (표준) $2\times2$ 행렬 $X$가 $X+\begin{bmatrix}1&2\\3&4\end{bmatrix}=\begin{bmatrix}0&0\\0&0\end{bmatrix}$을 만족하도록 $X$를 구하십시오.
> **답.** $X=\begin{bmatrix}-1&-2\\-3&-4\end{bmatrix}$입니다.
> **풀이.** 양변에서 주어진 행렬을 빼면 $X=O-\begin{bmatrix}1&2\\3&4\end{bmatrix}$입니다. 각 성분의 부호를 바꾸면 $X$가 나옵니다. 이는 $-A$의 정의와 같습니다.

### 2.3 행렬 곱셈

행렬 곱셈은 덧셈과 달리 성분별 곱이 아닙니다. $A\in\mathbb{R}^{m\times n}$과 $B\in\mathbb{R}^{n\times p}$의 곱 $AB$는 $m\times p$ 행렬이며, 그 $(i,j)$ 성분을 $A$의 $i$번째 행과 $B$의 $j$번째 열의 내적으로 정의합니다.

$$
(AB)_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots+a_{in}b_{nj}
$$

곱이 정의되려면 앞 행렬의 열의 수와 뒤 행렬의 행의 수가 같아야 합니다. 이 값이 곧 내적에서 더하는 항의 개수입니다. 곱셈은 다음 성질을 만족합니다. 크기가 맞는 행렬들과 스칼라 $c$에 대해

$$
(AB)C=A(BC)\quad(\text{결합법칙})
$$

$$
A(B+C)=AB+AC,\qquad (A+B)C=AC+BC\quad(\text{분배법칙})
$$

$$
c(AB)=(cA)B=A(cB)
$$

그러나 곱셈의 교환법칙은 일반적으로 성립하지 않습니다. 즉 대개 $AB\ne BA$입니다. 크기가 맞지 않아 한쪽 곱만 정의되는 경우도 있고, 둘 다 정의되어도 값이 다른 경우가 많습니다. 이 점이 수의 곱셈과 근본적으로 다른 특징입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}2&1\\4&3\end{bmatrix}$입니다.
> **풀이.** $(1,1)=1\cdot0+2\cdot1=2$, $(1,2)=1\cdot1+2\cdot0=1$, $(2,1)=3\cdot0+4\cdot1=4$, $(2,2)=3\cdot1+4\cdot0=3$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}1&2&0\end{bmatrix}$, $B=\begin{bmatrix}3\\-1\\4\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}1\end{bmatrix}$입니다.
> **풀이.** $A$는 $1\times3$, $B$는 $3\times1$이라 곱은 $1\times1$입니다. $1\cdot3+2\cdot(-1)+0\cdot4=3-2+0=1$입니다.

> **문제 3.** (표준) 문제 1의 $A,B$에 대해 $BA$를 구하고 $AB\ne BA$임을 확인하십시오.
> **답.** $BA=\begin{bmatrix}3&4\\1&2\end{bmatrix}$이고 $AB=\begin{bmatrix}2&1\\4&3\end{bmatrix}$과 다릅니다.
> **풀이.** $BA$의 $(1,1)=0\cdot1+1\cdot3=3$, $(1,2)=0\cdot2+1\cdot4=4$, $(2,1)=1\cdot1+0\cdot3=1$, $(2,2)=1\cdot2+0\cdot4=2$입니다. $AB$와 성분이 다르므로 교환법칙이 성립하지 않습니다.

> **문제 4.** (표준) $A=\begin{bmatrix}2&0\\1&3\end{bmatrix}$, $\mathbf{x}=\begin{bmatrix}1\\2\end{bmatrix}$일 때 $A\mathbf{x}$를 구하십시오.
> **답.** $\begin{bmatrix}2\\7\end{bmatrix}$입니다.
> **풀이.** 첫째 성분은 $2\cdot1+0\cdot2=2$, 둘째 성분은 $1\cdot1+3\cdot2=7$입니다. 행렬과 벡터의 곱은 연립방정식의 좌변을 한 번에 나타내는 표기입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, $B=\begin{bmatrix}1&0\\1&1\end{bmatrix}$일 때 $AB$와 $BA$를 각각 구하십시오.
> **답.** $AB=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, $BA=\begin{bmatrix}1&1\\1&2\end{bmatrix}$입니다.
> **풀이.** $AB$의 $(1,1)=1\cdot1+1\cdot1=2$, $(1,2)=1\cdot0+1\cdot1=1$, $(2,1)=0\cdot1+1\cdot1=1$, $(2,2)=0\cdot0+1\cdot1=1$입니다. $BA$의 $(1,1)=1\cdot1+0\cdot1=1$, $(1,2)=1\cdot1+0\cdot1=1$, $(2,1)=1\cdot1+1\cdot0=1$, $(2,2)=1\cdot1+1\cdot1=2$입니다. 두 곱이 다릅니다.

> **문제 6.** (심화) $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$일 때 $A^2$을 구하고, $A\ne O$인데도 $A^2=O$일 수 있음을 확인하십시오.
> **답.** $A^2=O$입니다.
> **풀이.** $A^2=AA$의 $(1,1)=0\cdot0+1\cdot0=0$, $(1,2)=0\cdot1+1\cdot0=0$, $(2,1)=0$, $(2,2)=0\cdot1+0\cdot0=0$입니다. 모든 성분이 0이라 $A^2=O$입니다. 수에서는 제곱이 0이면 그 수가 0이지만 행렬에서는 그렇지 않습니다.

### 2.4 전치와 특수 행렬

행렬 $A\in\mathbb{R}^{m\times n}$의 전치 $A^{T}$는 행과 열을 맞바꾼 $n\times m$ 행렬입니다.

$$
(A^{T})_{ij}=a_{ji}
$$

전치는 다음 성질을 만족합니다.

$$
(A^{T})^{T}=A,\qquad (A+B)^{T}=A^{T}+B^{T},\qquad (cA)^{T}=cA^{T}
$$

$$
(AB)^{T}=B^{T}A^{T}
$$

마지막 성질에서 곱의 전치는 순서가 뒤바뀐다는 점에 유의합니다. 이제 자주 쓰는 특수 정사각행렬을 정의합니다.

- 단위행렬 $I_n$은 대각 성분이 모두 1이고 나머지가 0인 행렬입니다. 임의의 $A$에 대해 $AI_n=A$, $I_mA=A$가 성립해 수의 1과 같은 역할을 합니다.
- 대각행렬은 대각 성분 외에는 모두 0인 정사각행렬입니다.
- 대칭행렬은 $A^{T}=A$인 행렬로, $a_{ij}=a_{ji}$를 뜻합니다.

임의의 $A$와 그 전치의 곱 $A^{T}A$는 항상 대칭입니다. 실제로 $(A^{T}A)^{T}=A^{T}(A^{T})^{T}=A^{T}A$이기 때문입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$의 전치를 구하십시오.
> **답.** $A^{T}=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}$입니다.
> **풀이.** 행과 열을 맞바꿉니다. $A$의 첫째 행 $(1,2,3)$이 $A^{T}$의 첫째 열이 되고, 둘째 행 $(4,5,6)$이 둘째 열이 됩니다.

> **문제 2.** (기초) $\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}$과 임의의 $3\times3$ 행렬 $A$의 곱 $I_3A$는 무엇입니까?
> **답.** $A$ 그 자체입니다.
> **풀이.** 단위행렬은 곱셈의 항등원이라 $I_3A=A$입니다. 성분으로 보면 단위행렬의 $i$번째 행은 $i$번째 성분만 1이라 $A$의 $i$번째 행을 그대로 골라냅니다.

> **문제 3.** (표준) $A=\begin{bmatrix}2&-1\\0&3\end{bmatrix}$가 대칭행렬인지 판정하십시오.
> **답.** 대칭행렬이 아닙니다.
> **풀이.** 대칭이려면 $a_{12}=a_{21}$이어야 하는데 $a_{12}=-1$, $a_{21}=0$으로 다릅니다. 따라서 $A^{T}\ne A$이고 대칭이 아닙니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $B=\begin{bmatrix}3&0\\1&2\end{bmatrix}$에 대해 $(AB)^{T}=B^{T}A^{T}$임을 계산으로 확인하십시오.
> **답.** 양변 모두 $\begin{bmatrix}5&1\\4&2\end{bmatrix}$입니다.
> **풀이.** $AB=\begin{bmatrix}1\cdot3+2\cdot1&1\cdot0+2\cdot2\\0\cdot3+1\cdot1&0\cdot0+1\cdot2\end{bmatrix}=\begin{bmatrix}5&4\\1&2\end{bmatrix}$이라 $(AB)^{T}=\begin{bmatrix}5&1\\4&2\end{bmatrix}$입니다. 한편 $B^{T}=\begin{bmatrix}3&1\\0&2\end{bmatrix}$, $A^{T}=\begin{bmatrix}1&0\\2&1\end{bmatrix}$이라 $B^{T}A^{T}=\begin{bmatrix}3\cdot1+1\cdot2&3\cdot0+1\cdot1\\0\cdot1+2\cdot2&0\cdot0+2\cdot1\end{bmatrix}=\begin{bmatrix}5&1\\4&2\end{bmatrix}$로 일치합니다.

> **문제 5.** (심화) 임의의 정사각행렬 $A$에 대해 $A+A^{T}$가 대칭임을 보이십시오.
> **답.** 전치가 자기 자신과 같기 때문입니다.
> **풀이.** $(A+A^{T})^{T}=A^{T}+(A^{T})^{T}=A^{T}+A=A+A^{T}$입니다. 전치가 원래 행렬과 같으므로 대칭입니다. 이 성질을 이용하면 임의의 정사각행렬을 대칭 부분 $\tfrac12(A+A^{T})$와 반대칭 부분 $\tfrac12(A-A^{T})$의 합으로 나눌 수 있습니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 덧셈 | $(A+B)_{ij}=a_{ij}+b_{ij}$ | 같은 크기에서만, 자리끼리 더한다 |
| 스칼라배 | $(cA)_{ij}=ca_{ij}$ | 모든 성분에 곱한다 |
| 곱셈 | $(AB)_{ij}=\sum_k a_{ik}b_{kj}$ | 앞 행과 뒤 열의 내적, 크기 $(m\times n)(n\times p)$ |
| 곱 크기 판정 | $n$이 맞아야 정의 | 가운데 수가 같으면 곱 가능 |
| 교환법칙 | 일반적으로 $AB\ne BA$ | 성립 가정 금지 |
| 전치 | $(A^{T})_{ij}=a_{ji}$ | 행과 열 교환 |
| 곱의 전치 | $(AB)^{T}=B^{T}A^{T}$ | 순서 뒤집힘 |
| 단위행렬 | $AI=IA=A$ | 곱셈의 1 |
| 대칭행렬 | $A^{T}=A$ | $a_{ij}=a_{ji}$ |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $\begin{bmatrix}2&1\\0&3\end{bmatrix}+\begin{bmatrix}1&-1\\4&2\end{bmatrix}$을 구하십시오.
> **답.** $\begin{bmatrix}3&0\\4&5\end{bmatrix}$입니다.
> **풀이.** 성분별로 $2+1=3$, $1-1=0$, $0+4=4$, $3+2=5$입니다.

> **문제 2.** (기초) $3\begin{bmatrix}1&-2\\0&4\end{bmatrix}$을 구하십시오.
> **답.** $\begin{bmatrix}3&-6\\0&12\end{bmatrix}$입니다.
> **풀이.** 모든 성분에 3을 곱하면 $3,-6,0,12$입니다.

> **문제 3.** (기초) $\begin{bmatrix}1&2\\3&4\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}$을 구하십시오.
> **답.** $\begin{bmatrix}3\\7\end{bmatrix}$입니다.
> **풀이.** 첫째 성분 $1\cdot1+2\cdot1=3$, 둘째 성분 $3\cdot1+4\cdot1=7$입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, $B=\begin{bmatrix}2&0\\1&2\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}4&4\\10&8\end{bmatrix}$입니다.
> **풀이.** $(1,1)=1\cdot2+2\cdot1=4$, $(1,2)=1\cdot0+2\cdot2=4$, $(2,1)=3\cdot2+4\cdot1=10$, $(2,2)=3\cdot0+4\cdot2=8$입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}1&0&2\\0&1&1\end{bmatrix}$, $B=\begin{bmatrix}1&0\\2&1\\0&3\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}1&6\\2&4\end{bmatrix}$입니다.
> **풀이.** $A$는 $2\times3$, $B$는 $3\times2$라 곱은 $2\times2$입니다. $(1,1)=1\cdot1+0\cdot2+2\cdot0=1$, $(1,2)=1\cdot0+0\cdot1+2\cdot3=6$, $(2,1)=0\cdot1+1\cdot2+1\cdot0=2$, $(2,2)=0\cdot0+1\cdot1+1\cdot3=4$입니다.

> **문제 6.** (표준) $A=\begin{bmatrix}2&1\\1&3\end{bmatrix}$일 때 $A^2$을 구하십시오.
> **답.** $\begin{bmatrix}5&5\\5&10\end{bmatrix}$입니다.
> **풀이.** $A^2=AA$입니다. $(1,1)=2\cdot2+1\cdot1=5$, $(1,2)=2\cdot1+1\cdot3=5$, $(2,1)=1\cdot2+3\cdot1=5$, $(2,2)=1\cdot1+3\cdot3=10$입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$일 때 $A^{T}A$를 구하고 대칭임을 확인하십시오.
> **답.** $\begin{bmatrix}10&14\\14&20\end{bmatrix}$이고 대칭입니다.
> **풀이.** $A^{T}=\begin{bmatrix}1&3\\2&4\end{bmatrix}$입니다. $(1,1)=1\cdot1+3\cdot3=10$, $(1,2)=1\cdot2+3\cdot4=14$, $(2,1)=2\cdot1+4\cdot3=14$, $(2,2)=2\cdot2+4\cdot4=20$입니다. $(1,2)$와 $(2,1)$이 모두 14라 대칭입니다.

> **문제 8.** (표준) $A=\begin{bmatrix}1&1\\0&1\end{bmatrix}$일 때 $A^3$을 구하십시오.
> **답.** $\begin{bmatrix}1&3\\0&1\end{bmatrix}$입니다.
> **풀이.** $A^2=\begin{bmatrix}1&2\\0&1\end{bmatrix}$입니다($(1,2)=1\cdot1+1\cdot1=2$). $A^3=A^2A=\begin{bmatrix}1&2\\0&1\end{bmatrix}\begin{bmatrix}1&1\\0&1\end{bmatrix}$의 $(1,2)=1\cdot1+2\cdot1=3$이라 $\begin{bmatrix}1&3\\0&1\end{bmatrix}$입니다.

> **문제 9.** (표준) $A=\begin{bmatrix}2&0\\0&3\end{bmatrix}$, $B=\begin{bmatrix}5&0\\0&-1\end{bmatrix}$인 두 대각행렬의 곱 $AB$를 구하고 규칙을 서술하십시오.
> **답.** $AB=\begin{bmatrix}10&0\\0&-3\end{bmatrix}$이며, 대각행렬의 곱은 대각끼리 곱한 대각행렬입니다.
> **풀이.** $(1,1)=2\cdot5=10$, $(2,2)=3\cdot(-1)=-3$이고 비대각 성분은 모두 0입니다. 대각행렬끼리는 곱이 교환법칙도 만족합니다.

> **문제 10.** (표준) $A=\begin{bmatrix}1&2\\-1&0\end{bmatrix}$, $B=\begin{bmatrix}0&1\\3&1\end{bmatrix}$에 대해 $A(B\mathbf{x})=(AB)\mathbf{x}$가 $\mathbf{x}=\begin{bmatrix}1\\1\end{bmatrix}$에서 성립함을 확인하십시오.
> **답.** 양변 모두 $\begin{bmatrix}9\\-1\end{bmatrix}$입니다.
> **풀이.** $B\mathbf{x}=\begin{bmatrix}0\cdot1+1\cdot1\\3\cdot1+1\cdot1\end{bmatrix}=\begin{bmatrix}1\\4\end{bmatrix}$이고 $A(B\mathbf{x})=\begin{bmatrix}1\cdot1+2\cdot4\\-1\cdot1+0\cdot4\end{bmatrix}=\begin{bmatrix}9\\-1\end{bmatrix}$입니다. 한편 $AB=\begin{bmatrix}1\cdot0+2\cdot3&1\cdot1+2\cdot1\\-1\cdot0+0\cdot3&-1\cdot1+0\cdot1\end{bmatrix}=\begin{bmatrix}6&3\\0&-1\end{bmatrix}$이라 $(AB)\mathbf{x}=\begin{bmatrix}6+3\\0-1\end{bmatrix}=\begin{bmatrix}9\\-1\end{bmatrix}$로 일치합니다. 이것이 결합법칙의 예입니다.

> **문제 11.** (심화) $A=\begin{bmatrix}1&2\\3&6\end{bmatrix}$에 대해 $A\mathbf{x}=\mathbf{0}$을 만족하는 영벡터가 아닌 $\mathbf{x}$를 하나 구하십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}2\\-1\end{bmatrix}$입니다.
> **풀이.** $A\mathbf{x}=\begin{bmatrix}x_1+2x_2\\3x_1+6x_2\end{bmatrix}$이고 두 식 모두 $x_1+2x_2=0$으로 귀결됩니다($3x_1+6x_2=3(x_1+2x_2)$). $x_2=-1$로 두면 $x_1=2$이라 $\mathbf{x}=\begin{bmatrix}2\\-1\end{bmatrix}$입니다. 검산하면 $\begin{bmatrix}2-2\\6-6\end{bmatrix}=\mathbf{0}$입니다.

> **문제 12.** (심화) $A=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$일 때 $A^{T}A=I$임을 보이십시오.
> **답.** 삼각함수 항등식 $\cos^2\theta+\sin^2\theta=1$로 단위행렬이 됩니다.
> **풀이.** $A^{T}=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}$입니다. $A^{T}A$의 $(1,1)=\cos^2\theta+\sin^2\theta=1$, $(2,2)=\sin^2\theta+\cos^2\theta=1$, $(1,2)=\cos\theta(-\sin\theta)+\sin\theta\cos\theta=0$, $(2,1)$도 대칭으로 0입니다. 따라서 $A^{T}A=I$이고 이런 행렬을 직교행렬이라고 합니다.

> **문제 13.** (심화) $A,B$가 같은 크기 대칭행렬일 때 $AB$가 대칭일 필요충분조건이 $AB=BA$임을 보이십시오.
> **답.** $(AB)^{T}=BA$이므로 대칭이려면 $BA=AB$이어야 합니다.
> **풀이.** $(AB)^{T}=B^{T}A^{T}=BA$입니다($A,B$가 대칭이라 $A^{T}=A$, $B^{T}=B$). $AB$가 대칭이라는 것은 $(AB)^{T}=AB$, 즉 $BA=AB$와 같습니다. 역으로 $AB=BA$이면 $(AB)^{T}=BA=AB$라 대칭입니다.

## 5. 스스로 점검

1. $m\times n$ 행렬의 성분 $a_{ij}$에서 두 첨자의 뜻을 말할 수 있는가?
2. 행렬 덧셈과 스칼라배를 성분으로 정의할 수 있는가?
3. 행렬 곱셈의 $(i,j)$ 성분 공식을 쓰고 곱이 정의되는 크기 조건을 말할 수 있는가?
4. $AB\ne BA$가 일반적임을 예로 설명할 수 있는가?
5. 전치의 정의와 $(AB)^{T}=B^{T}A^{T}$를 진술할 수 있는가?
6. 단위행렬, 대각행렬, 대칭행렬을 구별할 수 있는가?
7. $A^{T}A$가 항상 대칭임을 설명할 수 있는가?

**정답 요지.** 1. 앞 첨자는 행, 뒤 첨자는 열. 2. $(A+B)_{ij}=a_{ij}+b_{ij}$, $(cA)_{ij}=ca_{ij}$. 3. $\sum_k a_{ik}b_{kj}$, 앞 열 수와 뒤 행 수가 같아야 함. 4. 예를 들어 $\begin{bmatrix}1&2\\3&4\end{bmatrix}$와 $\begin{bmatrix}0&1\\1&0\end{bmatrix}$의 두 곱이 다름. 5. $(A^{T})_{ij}=a_{ji}$, 곱의 전치는 순서가 뒤집힘. 6. 대각만 1인 정사각행렬 / 대각 외 0 / $A^{T}=A$. 7. $(A^{T}A)^{T}=A^{T}A$.
