---
title: "9. 상공간, 영공간, 계수정리"
---
# 9강. 상공간·영공간·계수정리

## 이 강의에서 할 수 있게 되는 것

- 선형변환의 상공간(치역)을 표현행렬의 열공간으로 이해하고 그 기저와 차원을 구할 수 있습니다.
- 영공간(핵)을 동차방정식의 해집합으로 정의하고 그 기저와 차원을 구할 수 있습니다.
- 계수와 nullity를 정의하고 계수정리 $\operatorname{rank}+\operatorname{nullity}=n$을 진술·활용할 수 있습니다.
- 계수정리로 선형변환의 단사·전사 여부를 판정할 수 있습니다.

이 강의는 8강에서 정의한 선형변환의 내부 구조를 상공간과 영공간이라는 두 부분공간으로 읽습니다. 이 교본은 정의와 유도를 중심으로 진행합니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $T:\mathbb{R}^n\to\mathbb{R}^m$ | 티 | 표현행렬이 $A$인 선형변환 |
| $\operatorname{Im}(T)$, $\operatorname{Col}(A)$ | 상공간, 열공간 | $T$의 치역, $A$의 열이 생성하는 공간 |
| $\ker(T)$, $\operatorname{Nul}(A)$ | 핵, 영공간 | $A\mathbf{x}=\mathbf{0}$의 해집합 |
| $\operatorname{rank}(A)$ | 계수 | 상공간의 차원, 피벗 개수 |
| $\operatorname{nullity}(A)$ | 널리티 | 영공간의 차원, 자유변수 개수 |
| $\dim V$ | 브이의 차원 | 부분공간 $V$의 기저 크기 |
| $n$ | 엔 | 정의역 차원, $A$의 열 수 |

## 2. 개념

### 2.1 상공간(치역)

정의부터 세웁니다. 선형변환 $T:\mathbb{R}^n\to\mathbb{R}^m$의 상공간은 실제로 도달하는 벡터를 모은 집합입니다.

$$
\operatorname{Im}(T)=\{\,T(\mathbf{x})\ :\ \mathbf{x}\in\mathbb{R}^n\,\}
$$

표현행렬 $A$로 쓰면 $T(\mathbf{x})=A\mathbf{x}=x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n$입니다($\mathbf{a}_j$는 $A$의 $j$번째 열). 즉 상은 언제나 $A$의 열들의 일차결합이므로, 상공간은 열들이 생성하는 열공간 $\operatorname{Col}(A)$와 같습니다.

$$
\operatorname{Im}(T)=\operatorname{Col}(A)=\operatorname{span}\{\mathbf{a}_1,\dots,\mathbf{a}_n\}
$$

상공간은 공역 $\mathbb{R}^m$의 부분공간입니다. 그 기저는 소거하여 피벗이 있는 열에 대응하는 원래 행렬의 열들을 고르면 됩니다. 차원이 곧 계수 $\operatorname{rank}(A)$입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$일 때 상공간의 차원을 구하십시오.
> **답.** 차원은 1입니다.
> **풀이.** 둘째 열 $(2,4)$가 첫째 열 $(1,2)$의 2배라 두 열이 종속입니다. 독립인 열이 하나뿐이므로 상공간은 직선이고 차원은 1입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$일 때 상공간의 기저와 차원을 구하십시오.
> **답.** 기저는 $\{(1,0,0),(0,1,0)\}$, 차원은 2입니다.
> **풀이.** 두 열 $(1,0,0)$, $(0,1,0)$이 독립이라 그대로 기저입니다. 상공간은 $\mathbb{R}^3$ 안에서 $xy$평면이고 차원은 2입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&2&3\\0&1&1\\1&1&2\end{bmatrix}$의 상공간 차원을 구하십시오.
> **답.** 차원은 2입니다.
> **풀이.** $R_3-R_1$로 셋째 행이 $(0,-1,-1)$, 이어 $R_3+R_2$로 $(0,0,0)$이 됩니다. 피벗은 첫째·둘째 열의 두 개라 계수가 2이고 상공간 차원도 2입니다. 셋째 열 $(3,1,2)$는 첫 두 열의 결합($1\cdot$첫째$+1\cdot$둘째)입니다.

> **문제 4.** (표준) $T(x,y)=(x+y,\ x+y)$의 상공간을 구하십시오.
> **답.** 직선 $\{(t,t):t\in\mathbb{R}\}$입니다.
> **풀이.** 표현행렬은 $\begin{bmatrix}1&1\\1&1\end{bmatrix}$이고 두 열이 모두 $(1,1)$입니다. 상은 $(1,1)$의 배수뿐이라 직선 $y=x$이고 차원 1입니다.

> **문제 5.** (심화) $A=\begin{bmatrix}1&2&0\\0&0&1\\1&2&1\end{bmatrix}$의 상공간의 기저를 원래 열로 제시하십시오.
> **답.** 기저는 $\{(1,0,1),(0,1,1)\}$입니다.
> **풀이.** $R_3-R_1$로 셋째 행이 $(0,0,1)$, 이어 $R_3-R_2$로 $(0,0,0)$이 됩니다. 피벗은 첫째 열과 셋째 열에 생깁니다. 따라서 원래 행렬의 첫째 열 $(1,0,1)$과 셋째 열 $(0,1,1)$이 상공간의 기저입니다. 둘째 열 $(2,0,2)$는 첫째 열의 2배라 종속입니다.

### 2.2 영공간(핵)

선형변환 $T$의 영공간(핵)은 영벡터로 보내지는 입력을 모은 집합입니다.

$$
\ker(T)=\{\,\mathbf{x}\in\mathbb{R}^n\ :\ T(\mathbf{x})=\mathbf{0}\,\}=\{\mathbf{x}:A\mathbf{x}=\mathbf{0}\}
$$

이는 동차방정식 $A\mathbf{x}=\mathbf{0}$의 해집합이며 정의역 $\mathbb{R}^n$의 부분공간입니다. 실제로 $A\mathbf{u}=\mathbf{0}$, $A\mathbf{v}=\mathbf{0}$이면 $A(c\mathbf{u}+d\mathbf{v})=c\mathbf{0}+d\mathbf{0}=\mathbf{0}$이라 일차결합에 대해 닫혀 있습니다.

영공간의 기저는 가우스 소거 후 자유변수마다 하나씩 얻는 해벡터로 이루어지며, 그 개수가 nullity $\operatorname{nullity}(A)$, 곧 자유변수의 개수입니다. 영공간이 $\{\mathbf{0}\}$뿐이면 nullity는 0입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&0\\0&1\end{bmatrix}$의 영공간을 구하십시오.
> **답.** $\{\mathbf{0}\}$이고 nullity는 0입니다.
> **풀이.** $A\mathbf{x}=\mathbf{x}=\mathbf{0}$의 해는 $\mathbf{x}=\mathbf{0}$뿐입니다. 자유변수가 없어 영공간은 원점 하나입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$의 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\}$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행이 $(0,0)$이 되어 $x+2y=0$ 하나만 남습니다. $y=t$로 두면 $x=-2t$라 해는 $t(-2,1)$입니다. 기저는 $(-2,1)$이고 nullity는 1입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&1&1\\0&1&2\end{bmatrix}$의 영공간의 기저와 차원을 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}1\\-2\\1\end{bmatrix}\right\}$, 차원은 1입니다.
> **풀이.** 이미 사다리꼴에 가깝습니다. 둘째 행에서 $y+2z=0$이라 $y=-2z$, 첫째 행 $x+y+z=0$에 넣으면 $x=-y-z=2z-z=z$입니다. $z=t$로 두면 해는 $t(1,-2,1)$입니다. 자유변수 하나라 차원 1입니다. 검산하면 첫 식 $1-2+1=0$, 둘째 식 $-2+2=0$입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&2&1&1\\2&4&3&4\end{bmatrix}$의 nullity를 구하십시오.
> **답.** nullity는 2입니다.
> **풀이.** $R_2-2R_1$로 둘째 행이 $(0,0,1,2)$가 됩니다. 피벗은 첫째 열과 셋째 열에 있으므로 계수는 2입니다. 열이 $n=4$개라 자유변수는 $4-2=2$개, 즉 nullity는 2입니다.

> **문제 5.** (심화) $A=\begin{bmatrix}1&2&3\\2&4&6\\1&2&3\end{bmatrix}$의 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}-2\\1\\0\end{bmatrix},\ \begin{bmatrix}-3\\0\\1\end{bmatrix}\right\}$입니다.
> **풀이.** 세 행이 모두 $(1,2,3)$의 배수라 소거하면 $x+2y+3z=0$ 하나만 남습니다. 계수는 1, 자유변수는 $y,z$의 두 개입니다. $y=1,z=0$이면 $x=-2$, $y=0,z=1$이면 $x=-3$이라 두 해벡터를 얻습니다. 검산하면 각각 $-2+2+0=0$, $-3+0+3=0$입니다.

### 2.3 계수와 nullity, 계수정리

계수 $\operatorname{rank}(A)$는 상공간의 차원, nullity $\operatorname{nullity}(A)$는 영공간의 차원입니다. 가우스 소거를 하면 피벗이 있는 열의 수가 계수이고, 피벗이 없는(자유변수) 열의 수가 nullity입니다. 열 전체는 이 두 종류로 남김없이 나뉘므로 다음이 성립합니다.

$$
\operatorname{rank}(A)+\operatorname{nullity}(A)=n\quad(\text{계수정리, rank–nullity})
$$

여기서 $n$은 정의역의 차원, 곧 $A$의 열 수입니다. 이 정리는 선형변환이 "무엇을 짓눌러 없애는지"($\operatorname{nullity}$)와 "무엇을 남겨 도달하는지"($\operatorname{rank}$)의 합이 항상 입력 차원과 같다는 보존 법칙입니다. 상공간은 공역의 부분, 영공간은 정의역의 부분이라는 소속 공간이 다르다는 점에 유의합니다.

> **문제 1.** (기초) $A$가 $3\times5$ 행렬이고 $\operatorname{rank}(A)=3$이면 nullity를 구하십시오.
> **답.** nullity는 2입니다.
> **풀이.** 열 수 $n=5$이라 계수정리로 $\operatorname{nullity}=5-3=2$입니다.

> **문제 2.** (기초) $A$가 $4\times4$이고 $\operatorname{nullity}(A)=0$이면 계수를 구하고 가역 여부를 말하십시오.
> **답.** 계수는 4이고 가역입니다.
> **풀이.** $\operatorname{rank}=n-\operatorname{nullity}=4-0=4$입니다. 정사각행렬이 full rank이므로 가역입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&2&1\\1&2&1\\2&4&2\end{bmatrix}$의 계수와 nullity를 구하고 계수정리를 확인하십시오.
> **답.** $\operatorname{rank}=1$, $\operatorname{nullity}=2$이고 $1+2=3=n$입니다.
> **풀이.** 세 행이 모두 $(1,2,1)$의 배수라 소거하면 피벗이 하나뿐이라 계수는 1입니다. 열이 3개이므로 nullity는 $3-1=2$입니다. 합이 열 수 3과 같아 계수정리가 성립합니다.

> **문제 4.** (표준) $A$가 $2\times4$일 때 $\operatorname{rank}(A)$의 가능한 최댓값과 그때의 nullity를 구하십시오.
> **답.** 최대 계수는 2, 그때 nullity는 2입니다.
> **풀이.** 계수는 행 수와 열 수 중 작은 값 $\min(2,4)=2$를 넘지 못합니다. 계수가 2이면 $\operatorname{nullity}=4-2=2$입니다. $2\times4$는 열이 행보다 많아 영공간이 반드시 자명하지 않습니다.

> **문제 5.** (심화) $A=\begin{bmatrix}1&1&0&2\\0&1&1&1\\1&2&1&3\end{bmatrix}$의 계수와 nullity를 구하십시오.
> **답.** $\operatorname{rank}=2$, $\operatorname{nullity}=2$입니다.
> **풀이.** $R_3-R_1$로 셋째 행이 $(0,1,1,1)$이 되고, 이는 둘째 행과 같아 $R_3-R_2$로 $(0,0,0,0)$이 됩니다. 피벗은 첫째·둘째 열의 두 개라 계수는 2입니다. 열이 $n=4$개이므로 nullity는 $4-2=2$입니다.

### 2.4 단사·전사 판정

계수정리는 선형변환의 단사(일대일)와 전사(위로의) 여부를 바로 판정하게 해 줍니다.

- $T$가 단사일 필요충분조건은 $\ker(T)=\{\mathbf{0}\}$, 즉 $\operatorname{nullity}(A)=0$이며, 계수정리로 $\operatorname{rank}(A)=n$과 같습니다.
- $T$가 전사일 필요충분조건은 $\operatorname{Im}(T)=\mathbb{R}^m$, 즉 $\operatorname{rank}(A)=m$입니다.

정사각행렬($m=n$)이면 단사와 전사가 동치이고, 둘 다 $\operatorname{rank}=n$(가역)과 같습니다. 한편 열이 행보다 많으면($n>m$) 전사는 가능해도 $\operatorname{rank}\le m<n$이라 단사가 불가능하고, 행이 열보다 많으면($m>n$) 단사는 가능해도 전사가 불가능합니다.

> **문제 1.** (기초) $T:\mathbb{R}^3\to\mathbb{R}^2$가 선형일 때 단사가 될 수 없음을 계수정리로 설명하십시오.
> **답.** $\operatorname{nullity}\ge1$이라 단사가 불가능합니다.
> **풀이.** 상공간은 $\mathbb{R}^2$의 부분이라 $\operatorname{rank}\le2$입니다. 계수정리로 $\operatorname{nullity}=3-\operatorname{rank}\ge3-2=1$이라 영공간이 자명하지 않습니다. 따라서 단사가 아닙니다.

> **문제 2.** (표준) $A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$로 정의된 $T:\mathbb{R}^2\to\mathbb{R}^3$의 단사·전사를 판정하십시오.
> **답.** 단사이고 전사가 아닙니다.
> **풀이.** 두 열이 독립이라 $\operatorname{rank}=2=n$이므로 $\operatorname{nullity}=0$이라 단사입니다. 그러나 $\operatorname{rank}=2<3=m$이라 상공간이 $\mathbb{R}^3$ 전체가 아니어서 전사가 아닙니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&2&0\\0&1&1\end{bmatrix}$로 정의된 $T:\mathbb{R}^3\to\mathbb{R}^2$의 전사 여부를 판정하십시오.
> **답.** 전사입니다.
> **풀이.** 피벗이 첫째·둘째 열에 있어 $\operatorname{rank}=2=m$입니다. 상공간이 $\mathbb{R}^2$ 전체이므로 전사입니다. 한편 $\operatorname{nullity}=3-2=1$이라 단사는 아닙니다.

> **문제 4.** (심화) 정사각행렬 $A$에 대해 "단사이면 전사"임을 계수정리로 보이십시오.
> **답.** $\operatorname{nullity}=0\Rightarrow\operatorname{rank}=n=m$이라 전사입니다.
> **풀이.** $A$가 $n\times n$이라 하면 단사는 $\operatorname{nullity}=0$과 같습니다. 계수정리로 $\operatorname{rank}=n-0=n$입니다. 공역도 $\mathbb{R}^n$이라 $\operatorname{rank}=n=m$이 곧 전사입니다. 따라서 정사각의 경우 단사와 전사가 동치입니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 상공간 | $\operatorname{Im}(T)=\operatorname{Col}(A)$ | 피벗 열에 대응하는 원래 열이 기저 |
| 상공간 차원 | $\dim\operatorname{Im}(T)=\operatorname{rank}(A)$ | 피벗 개수 |
| 영공간 | $\ker(T)=\{A\mathbf{x}=\mathbf{0}\}$ | 자유변수별 해벡터가 기저 |
| nullity | 자유변수 개수 | $n-\operatorname{rank}$ |
| 계수정리 | $\operatorname{rank}+\operatorname{nullity}=n$ | $n$은 열 수(정의역 차원) |
| 단사 | $\operatorname{nullity}=0\Leftrightarrow\operatorname{rank}=n$ | 영공간이 자명 |
| 전사 | $\operatorname{rank}=m$ | 상공간이 공역 전체 |
| 정사각 | 단사$\Leftrightarrow$전사$\Leftrightarrow$가역 | full rank |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $A=\begin{bmatrix}2&4\\1&2\end{bmatrix}$의 계수를 구하십시오.
> **답.** $\operatorname{rank}=1$입니다.
> **풀이.** 둘째 열이 첫째 열의 2배라 종속입니다. 독립 열이 하나뿐이라 계수는 1입니다.

> **문제 2.** (기초) $A$가 $5\times3$이고 $\operatorname{rank}(A)=3$이면 nullity를 구하십시오.
> **답.** nullity는 0입니다.
> **풀이.** 열 수 $n=3$이라 $\operatorname{nullity}=3-3=0$입니다. 열이 모두 독립이라 영공간이 자명합니다.

> **문제 3.** (기초) $A=\begin{bmatrix}1&0&2\\0&1&3\end{bmatrix}$의 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}-2\\-3\\1\end{bmatrix}\right\}$입니다.
> **풀이.** 이미 기약 사다리꼴입니다. $x+2z=0$, $y+3z=0$이라 $z=t$로 두면 $x=-2t$, $y=-3t$입니다. 해는 $t(-2,-3,1)$입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix}$의 계수와 nullity를 구하십시오.
> **답.** $\operatorname{rank}=2$, $\operatorname{nullity}=1$입니다.
> **풀이.** $R_2-4R_1$로 둘째 행 $(0,-3,-6)$, $R_3-7R_1$로 셋째 행 $(0,-6,-12)$을 얻습니다. $R_3-2R_2$로 셋째 행이 $(0,0,0)$이 됩니다. 피벗 두 개라 계수는 2, nullity는 $3-2=1$입니다.

> **문제 5.** (표준) 문제 4의 $A$에 대해 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}1\\-2\\1\end{bmatrix}\right\}$입니다.
> **풀이.** 소거 후 $x+2y+3z=0$, $-3y-6z=0$입니다. 둘째에서 $y=-2z$, 첫째에 넣으면 $x=-2y-3z=4z-3z=z$입니다. $z=t$로 두면 $t(1,-2,1)$입니다. 검산하면 첫 행 $1-4+3=0$입니다.

> **문제 6.** (표준) $A=\begin{bmatrix}1&1\\1&1\\1&1\end{bmatrix}$로 정의된 $T:\mathbb{R}^2\to\mathbb{R}^3$의 상공간과 영공간의 차원을 각각 구하십시오.
> **답.** 상공간 차원 1, 영공간 차원 1입니다.
> **풀이.** 두 열이 모두 $(1,1,1)$이라 계수는 1이고 상공간은 직선입니다. 계수정리로 $\operatorname{nullity}=2-1=1$입니다. 실제로 $A\mathbf{x}=\mathbf{0}$은 $x+y=0$이라 $(1,-1)$이 영공간 기저입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&2&1\\2&4&2\\3&6&3\end{bmatrix}$의 상공간의 기저를 원래 열로 제시하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}1\\2\\3\end{bmatrix}\right\}$입니다.
> **풀이.** 둘째 열은 첫째 열의 2배, 셋째 열은 첫째 열과 같습니다. 독립 열은 첫째 열 하나뿐이라 이것이 상공간의 기저이고 계수는 1입니다.

> **문제 8.** (표준) $A$가 $3\times3$이고 $\operatorname{rank}(A)=2$이면 $A\mathbf{x}=\mathbf{b}$의 해의 구조를 설명하십시오.
> **답.** 해가 있으면 자유변수 하나짜리 직선(무수히 많은 해)입니다.
> **풀이.** $\operatorname{nullity}=3-2=1$이라 동차해가 직선을 이룹니다. $\mathbf{b}$가 상공간에 있으면 특수해에 이 직선을 더한 것이 해집합이라 해가 무수히 많고, 상공간 밖이면 해가 없습니다.

> **문제 9.** (표준) $T:\mathbb{R}^4\to\mathbb{R}^4$가 $\operatorname{rank}=4$이면 단사·전사·가역 여부를 판정하십시오.
> **답.** 단사이며 전사이고 가역입니다.
> **풀이.** $\operatorname{nullity}=4-4=0$이라 단사입니다. $\operatorname{rank}=4=m$이라 전사입니다. 정사각 full rank이므로 가역입니다.

> **문제 10.** (심화) $A=\begin{bmatrix}1&2&0&1\\0&0&1&2\\1&2&1&3\end{bmatrix}$의 계수와 nullity를 구하고 영공간의 기저를 제시하십시오.
> **답.** $\operatorname{rank}=2$, $\operatorname{nullity}=2$이고 기저는 $\left\{\begin{bmatrix}-2\\1\\0\\0\end{bmatrix},\ \begin{bmatrix}-1\\0\\-2\\1\end{bmatrix}\right\}$입니다.
> **풀이.** $R_3-R_1$로 셋째 행이 $(0,0,1,2)$가 되고 이는 둘째 행과 같아 $R_3-R_2$로 $(0,0,0,0)$이 됩니다. 피벗은 첫째 열과 셋째 열이라 계수 2, nullity $4-2=2$입니다. 자유변수는 $x_2,x_4$입니다. 방정식은 $x_1+2x_2+x_4=0$, $x_3+2x_4=0$입니다. $x_2=1,x_4=0$이면 $x_1=-2,x_3=0$이라 $(-2,1,0,0)$, $x_2=0,x_4=1$이면 $x_3=-2$, $x_1=-1$이라 $(-1,0,-2,1)$입니다.

> **문제 11.** (심화) 선형변환 $T:\mathbb{R}^5\to\mathbb{R}^3$이 전사일 때 nullity를 구하십시오.
> **답.** nullity는 2입니다.
> **풀이.** 전사이면 $\operatorname{rank}=m=3$입니다. 정의역 차원 $n=5$이라 계수정리로 $\operatorname{nullity}=5-3=2$입니다.

> **문제 12.** (심화) $A$의 열이 일차독립일 필요충분조건이 $\operatorname{nullity}(A)=0$임을 설명하십시오.
> **답.** 열의 독립은 동차해가 자명한 것과 같기 때문입니다.
> **풀이.** 열 $\mathbf{a}_1,\dots,\mathbf{a}_n$의 일차결합 $x_1\mathbf{a}_1+\cdots+x_n\mathbf{a}_n=\mathbf{0}$은 $A\mathbf{x}=\mathbf{0}$과 같습니다. 열이 독립이라는 것은 이 식의 해가 $\mathbf{x}=\mathbf{0}$뿐이라는 뜻, 곧 영공간이 자명해 $\operatorname{nullity}=0$과 동치입니다. 이때 계수정리로 $\operatorname{rank}=n$입니다.

## 5. 스스로 점검

1. 상공간이 열공간과 같은 이유를 설명할 수 있는가?
2. 영공간이 정의역의 부분공간임을 보일 수 있는가?
3. 계수와 nullity를 피벗·자유변수로 셀 수 있는가?
4. 계수정리 $\operatorname{rank}+\operatorname{nullity}=n$을 진술할 수 있는가?
5. 상공간과 영공간이 각각 어느 공간의 부분공간인지 구별할 수 있는가?
6. $\operatorname{nullity}=0$이 단사, $\operatorname{rank}=m$이 전사와 동치임을 말할 수 있는가?
7. 정사각행렬에서 단사·전사·가역이 동치임을 설명할 수 있는가?

**정답 요지.** 1. $A\mathbf{x}$가 언제나 열들의 일차결합이라 상 $=\operatorname{Col}(A)$. 2. 동차해는 일차결합에 닫혀 있음. 3. 피벗 열 수 $=\operatorname{rank}$, 자유변수 수 $=\operatorname{nullity}$. 4. 두 차원의 합이 열 수 $n$. 5. 상공간은 공역 $\mathbb{R}^m$의 부분, 영공간은 정의역 $\mathbb{R}^n$의 부분. 6. 영공간 자명 $\Leftrightarrow$ 단사, 상공간이 공역 전체 $\Leftrightarrow$ 전사. 7. $m=n$이면 $\operatorname{rank}=n$이 셋을 동시에 보장.
