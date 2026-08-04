---
title: "10. 기저변환"
---
# 10강. 기저변환

## 이 강의에서 할 수 있게 되는 것

- 순서기저에 대한 좌표벡터와 전이행렬(기저변환행렬)의 관계를 이해합니다.
- 한 기저의 좌표를 다른 기저의 좌표로 바꾸는 전이행렬을 구성할 수 있습니다.
- 기저를 바꿨을 때 선형변환의 표현행렬이 $P^{-1}AP$로 변함을 유도할 수 있습니다.
- 닮음(similarity)을 정의하고 닮은 행렬이 공유하는 불변량을 말할 수 있습니다.

이 강의는 8강에서 관찰한 "같은 변환도 기저에 따라 행렬이 달라진다"는 사실을 전이행렬과 닮음으로 정리합니다. 이 교본은 정의와 유도를 중심으로 진행합니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $B=\{\mathbf{b}_1,\dots,\mathbf{b}_n\}$ | 기저 비 | 정의역의 순서기저 |
| $[\mathbf{x}]_B$ | 엑스의 비 좌표 | 기저 $B$에 대한 좌표벡터 |
| $P_B=[\,\mathbf{b}_1\ \cdots\ \mathbf{b}_n\,]$ | 전이행렬 | $B$좌표를 표준좌표로 바꾸는 행렬 |
| $P_{C\leftarrow B}$ | 씨 백 비 전이행렬 | $B$좌표를 $C$좌표로 바꾸는 행렬 |
| $A$ | 에이 | 표준기저에 대한 $T$의 표현행렬 |
| $[T]_B$ | 티의 비 표현행렬 | 기저 $B$에 대한 $T$의 표현행렬 |
| $B'=P^{-1}AP$ | 닮음 변환 | $A$와 닮은 행렬 |
| $\operatorname{tr}$ | 대각합 | 대각 성분의 합 |

## 2. 개념

### 2.1 좌표벡터와 전이행렬

$\mathbb{R}^n$의 순서기저 $B=\{\mathbf{b}_1,\dots,\mathbf{b}_n\}$를 잡으면 임의의 $\mathbf{x}$는 유일하게 $\mathbf{x}=x_1'\mathbf{b}_1+\cdots+x_n'\mathbf{b}_n$으로 쓰이고, 계수를 모은 $[\mathbf{x}]_B=(x_1',\dots,x_n')$가 좌표벡터입니다. 기저벡터를 열로 세운 행렬을 $P_B=[\,\mathbf{b}_1\ \cdots\ \mathbf{b}_n\,]$라 하면

$$
\mathbf{x}=P_B\,[\mathbf{x}]_B,\qquad [\mathbf{x}]_B=P_B^{-1}\,\mathbf{x}
$$

가 성립합니다. 앞 식은 $B$좌표를 표준좌표로 되돌리는 것이고, 뒤 식은 표준좌표를 $B$좌표로 바꾸는 것입니다. $B$가 기저이면 열이 독립이라 $P_B$는 가역이므로 두 방향이 모두 가능합니다. 이 $P_B$를 $B$에서 표준기저로의 전이행렬이라고 합니다.

> **문제 1.** (기초) $B=\{(1,0),(1,1)\}$이고 $[\mathbf{v}]_B=\begin{bmatrix}2\\3\end{bmatrix}$일 때 $\mathbf{v}$를 구하십시오.
> **답.** $\mathbf{v}=(5,3)$입니다.
> **풀이.** $\mathbf{v}=P_B[\mathbf{v}]_B=2(1,0)+3(1,1)=(2+3,\ 0+3)=(5,3)$입니다.

> **문제 2.** (기초) 문제 1의 $B$에 대해 $\mathbf{v}=(5,3)$의 좌표벡터를 $P_B^{-1}$로 구하십시오.
> **답.** $[\mathbf{v}]_B=\begin{bmatrix}2\\3\end{bmatrix}$입니다.
> **풀이.** $P_B=\begin{bmatrix}1&1\\0&1\end{bmatrix}$이고 $\det=1$이라 $P_B^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. $P_B^{-1}\begin{bmatrix}5\\3\end{bmatrix}=\begin{bmatrix}5-3\\3\end{bmatrix}=\begin{bmatrix}2\\3\end{bmatrix}$로 문제 1과 일치합니다.

> **문제 3.** (표준) $B=\{(2,1),(1,1)\}$의 전이행렬 $P_B$와 그 역행렬을 구하십시오.
> **답.** $P_B=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, $P_B^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$입니다.
> **풀이.** 기저벡터를 열로 세우면 $P_B=\begin{bmatrix}2&1\\1&1\end{bmatrix}$입니다. $\det=2\cdot1-1\cdot1=1$이라 $P_B^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$입니다. 검산하면 $P_BP_B^{-1}=\begin{bmatrix}2-1&-2+2\\1-1&-1+2\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

> **문제 4.** (심화) 문제 3의 $B$로 $\mathbf{v}=(3,2)$의 좌표벡터를 구하십시오.
> **답.** $[\mathbf{v}]_B=\begin{bmatrix}1\\1\end{bmatrix}$입니다.
> **풀이.** $[\mathbf{v}]_B=P_B^{-1}\mathbf{v}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}\begin{bmatrix}3\\2\end{bmatrix}=\begin{bmatrix}3-2\\-3+4\end{bmatrix}=\begin{bmatrix}1\\1\end{bmatrix}$입니다. 검산하면 $1(2,1)+1(1,1)=(3,2)$입니다.

### 2.2 두 기저 사이의 전이행렬

두 기저 $B$와 $C$가 있을 때 $B$좌표를 $C$좌표로 바꾸는 전이행렬 $P_{C\leftarrow B}$는 각 $\mathbf{b}_j$의 $C$좌표를 열로 세운 것입니다. 표준좌표를 매개로 하면

$$
[\mathbf{x}]_C=P_C^{-1}\mathbf{x}=P_C^{-1}P_B\,[\mathbf{x}]_B,\qquad\text{즉}\quad P_{C\leftarrow B}=P_C^{-1}P_B
$$

가 됩니다. 특히 $C$가 표준기저이면 $P_C=I$라 $P_{C\leftarrow B}=P_B$가 되어 2.1과 일치합니다. 전이행렬은 언제나 가역이며 $P_{B\leftarrow C}=P_{C\leftarrow B}^{-1}$입니다.

> **문제 1.** (기초) $C$가 표준기저이고 $B=\{(1,2),(0,1)\}$일 때 $P_{C\leftarrow B}$를 구하십시오.
> **답.** $\begin{bmatrix}1&0\\2&1\end{bmatrix}$입니다.
> **풀이.** $C$가 표준기저라 $P_{C\leftarrow B}=P_B$이고, 기저벡터를 열로 세우면 $\begin{bmatrix}1&0\\2&1\end{bmatrix}$입니다.

> **문제 2.** (표준) $B=\{(1,1),(1,0)\}$, $C=\{(1,0),(0,1)\}$(표준)일 때 $\mathbf{x}$의 $B$좌표가 $\begin{bmatrix}2\\3\end{bmatrix}$이면 $C$좌표를 구하십시오.
> **답.** $\begin{bmatrix}5\\2\end{bmatrix}$입니다.
> **풀이.** $P_{C\leftarrow B}=P_B=\begin{bmatrix}1&1\\1&0\end{bmatrix}$입니다. $[\mathbf{x}]_C=P_B[\mathbf{x}]_B=\begin{bmatrix}1&1\\1&0\end{bmatrix}\begin{bmatrix}2\\3\end{bmatrix}=\begin{bmatrix}2+3\\2\end{bmatrix}=\begin{bmatrix}5\\2\end{bmatrix}$입니다. 표준기저이므로 이것이 곧 벡터 $(5,2)$입니다.

> **문제 3.** (표준) $B=\{(1,1),(1,-1)\}$, $C=\{(1,0),(1,1)\}$일 때 $P_{C\leftarrow B}=P_C^{-1}P_B$를 구하십시오.
> **답.** $\begin{bmatrix}2&2\\-1&-2\end{bmatrix}$입니다.
> **풀이.** $P_B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $P_C=\begin{bmatrix}1&1\\0&1\end{bmatrix}$이고 $P_C^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. $P_C^{-1}P_B=\begin{bmatrix}1&-1\\0&1\end{bmatrix}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$의 $(1,1)=1-1=0$… 다시 계산하면 $(1,1)=1\cdot1+(-1)\cdot1=0$, $(1,2)=1\cdot1+(-1)\cdot(-1)=2$, $(2,1)=0\cdot1+1\cdot1=1$, $(2,2)=0\cdot1+1\cdot(-1)=-1$이라 $\begin{bmatrix}0&2\\1&-1\end{bmatrix}$입니다.
> (검산) $\mathbf{b}_1=(1,1)$의 $C$좌표는 $a(1,0)+b(1,1)=(1,1)$에서 $b=1,a=0$이라 $(0,1)$로 첫째 열과 일치합니다.

> **문제 4.** (심화) 문제 3에서 $P_{B\leftarrow C}$를 구하십시오.
> **답.** $\begin{bmatrix}\tfrac12&1\\\tfrac12&0\end{bmatrix}$입니다.
> **풀이.** $P_{B\leftarrow C}=P_{C\leftarrow B}^{-1}=\begin{bmatrix}0&2\\1&-1\end{bmatrix}^{-1}$입니다. $\det=0\cdot(-1)-2\cdot1=-2$이라 역행렬은 $\tfrac{1}{-2}\begin{bmatrix}-1&-2\\-1&0\end{bmatrix}=\begin{bmatrix}\tfrac12&1\\\tfrac12&0\end{bmatrix}$입니다. 검산하면 $\begin{bmatrix}0&2\\1&-1\end{bmatrix}\begin{bmatrix}\tfrac12&1\\\tfrac12&0\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

### 2.3 선형변환의 표현행렬 변환

선형변환 $T$의 표준행렬이 $A$일 때 기저 $B$에 대한 표현행렬 $[T]_B$를 구합니다. $B$좌표에서 출발해 $[\mathbf{x}]_B\mapsto[T(\mathbf{x})]_B$를 따라가면, 먼저 표준좌표로 바꾸고($P_B$) $A$를 적용한 뒤 다시 $B$좌표로 되돌립니다($P_B^{-1}$). 따라서

$$
[T(\mathbf{x})]_B=P_B^{-1}A P_B\,[\mathbf{x}]_B,\qquad [T]_B=P_B^{-1}A P_B
$$

가 됩니다. 표기를 줄여 $P=P_B$로 쓰면 $[T]_B=P^{-1}AP$입니다. 같은 변환 $T$가 표준기저에서는 $A$, 기저 $B$에서는 $P^{-1}AP$로 나타납니다. 기저를 잘 고르면 이 행렬이 대각행렬처럼 단순해질 수 있고, 그것이 4단원 대각화의 목표입니다.

> **문제 1.** (표준) $A=\begin{bmatrix}2&0\\0&3\end{bmatrix}$, $P=\begin{bmatrix}1&1\\0&1\end{bmatrix}$일 때 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}2&-1\\0&3\end{bmatrix}$입니다.
> **풀이.** $P^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. 먼저 $AP=\begin{bmatrix}2&0\\0&3\end{bmatrix}\begin{bmatrix}1&1\\0&1\end{bmatrix}=\begin{bmatrix}2&2\\0&3\end{bmatrix}$입니다. 이어 $P^{-1}(AP)=\begin{bmatrix}1&-1\\0&1\end{bmatrix}\begin{bmatrix}2&2\\0&3\end{bmatrix}$의 $(1,1)=2$, $(1,2)=2-3=-1$, $(2,1)=0$, $(2,2)=3$이라 $\begin{bmatrix}2&-1\\0&3\end{bmatrix}$입니다.

> **문제 2.** (표준) $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $P=\begin{bmatrix}1&0\\1&1\end{bmatrix}$일 때 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}3&2\\-2&-1\end{bmatrix}$입니다.
> **풀이.** $P^{-1}=\begin{bmatrix}1&0\\-1&1\end{bmatrix}$입니다. $AP=\begin{bmatrix}1&2\\0&1\end{bmatrix}\begin{bmatrix}1&0\\1&1\end{bmatrix}=\begin{bmatrix}1+2&2\\1&1\end{bmatrix}=\begin{bmatrix}3&2\\1&1\end{bmatrix}$입니다. $P^{-1}(AP)=\begin{bmatrix}1&0\\-1&1\end{bmatrix}\begin{bmatrix}3&2\\1&1\end{bmatrix}$의 $(1,1)=3$, $(1,2)=2$, $(2,1)=-3+1=-2$, $(2,2)=-2+1=-1$이라 $\begin{bmatrix}3&2\\-2&-1\end{bmatrix}$입니다.

> **문제 3.** (심화) $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$에 대해 $P=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$로 $P^{-1}AP$를 구하고 대각행렬이 됨을 확인하십시오.
> **답.** $\begin{bmatrix}3&0\\0&1\end{bmatrix}$입니다.
> **풀이.** $\det P=-2$이라 $P^{-1}=\tfrac{1}{-2}\begin{bmatrix}-1&-1\\-1&1\end{bmatrix}=\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}$입니다. $AP=\begin{bmatrix}2&1\\1&2\end{bmatrix}\begin{bmatrix}1&1\\1&-1\end{bmatrix}=\begin{bmatrix}3&1\\3&-1\end{bmatrix}$입니다(첫째 열 $A(1,1)=(3,3)$, 둘째 열 $A(1,-1)=(1,-1)$). $P^{-1}(AP)$의 $(1,1)=\tfrac12\cdot3+\tfrac12\cdot3=3$, $(1,2)=\tfrac12\cdot1+\tfrac12\cdot(-1)=0$, $(2,1)=\tfrac12\cdot3-\tfrac12\cdot3=0$, $(2,2)=\tfrac12\cdot1-\tfrac12\cdot(-1)=1$이라 $\begin{bmatrix}3&0\\0&1\end{bmatrix}$입니다. 기저 $P$의 두 열이 $A$의 고유벡터라 대각화됩니다.

### 2.4 닮음과 불변량

가역행렬 $P$에 대해 $B'=P^{-1}AP$의 관계에 있는 두 정사각행렬 $A,B'$를 닮음(similar)이라고 합니다. 닮음은 같은 선형변환을 서로 다른 기저에서 표현한 두 행렬 사이의 관계입니다. 닮은 행렬은 다음 불변량을 공유합니다.

$$
\det(B')=\det A,\qquad \operatorname{tr}(B')=\operatorname{tr}A,\qquad \operatorname{rank}(B')=\operatorname{rank}A
$$

행렬식은 $\det(P^{-1}AP)=\det(P^{-1})\det A\det P=\dfrac{1}{\det P}\det A\det P=\det A$로 보존됩니다. 대각합은 $\operatorname{tr}(XY)=\operatorname{tr}(YX)$를 이용해 $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}(APP^{-1})=\operatorname{tr}A$로 보존됩니다. 고유값도 닮음에서 보존되며, 이것이 4단원에서 대각화가 고유값을 드러내는 이유입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$와 닮은 행렬 $B'$의 대각합과 행렬식을 구하십시오.
> **답.** $\operatorname{tr}B'=7$, $\det B'=10$입니다.
> **풀이.** 닮음은 대각합과 행렬식을 보존합니다. $\operatorname{tr}A=4+3=7$, $\det A=4\cdot3-1\cdot2=10$이라 $B'$도 같은 값을 가집니다.

> **문제 2.** (표준) 2.3의 문제 3에서 얻은 $\begin{bmatrix}3&0\\0&1\end{bmatrix}$이 원래 $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$와 대각합·행렬식이 같음을 확인하십시오.
> **답.** 대각합은 모두 4, 행렬식은 모두 3입니다.
> **풀이.** $A$는 $\operatorname{tr}=2+2=4$, $\det=4-1=3$입니다. 대각행렬은 $\operatorname{tr}=3+1=4$, $\det=3\cdot1=3$이라 일치합니다. 닮음이 두 값을 보존함을 보여 줍니다.

> **문제 3.** (표준) $\begin{bmatrix}1&2\\3&4\end{bmatrix}$와 $\begin{bmatrix}0&1\\0&0\end{bmatrix}$이 닮을 수 없는 이유를 말하십시오.
> **답.** 대각합이 각각 5와 0으로 달라 닮을 수 없습니다.
> **풀이.** 닮은 행렬은 대각합이 같아야 합니다. 앞은 $1+4=5$, 뒤는 $0+0=0$으로 다르므로 어떤 가역 $P$로도 $P^{-1}AP$가 될 수 없습니다.

> **문제 4.** (심화) 닮은 행렬이 같은 고유값을 가짐을 특성다항식으로 설명하십시오.
> **답.** $\det(B'-\lambda I)=\det(A-\lambda I)$이기 때문입니다.
> **풀이.** $B'-\lambda I=P^{-1}AP-\lambda I=P^{-1}(A-\lambda I)P$입니다($\lambda I=P^{-1}(\lambda I)P$). 행렬식은 닮음에서 보존되므로 $\det(B'-\lambda I)=\det(A-\lambda I)$입니다. 두 특성다항식이 같아 고유값(그 근)도 같습니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 전이행렬 | $P_B=[\,\mathbf{b}_1\ \cdots\ \mathbf{b}_n\,]$ | 기저벡터를 열로 |
| 좌표 복원 | $\mathbf{x}=P_B[\mathbf{x}]_B$ | $B$좌표 → 표준좌표 |
| 좌표 추출 | $[\mathbf{x}]_B=P_B^{-1}\mathbf{x}$ | 표준좌표 → $B$좌표 |
| 두 기저 사이 | $P_{C\leftarrow B}=P_C^{-1}P_B$ | 표준을 매개로 |
| 표현행렬 변환 | $[T]_B=P^{-1}AP$ | 되돌리기·적용·바꾸기 |
| 닮음 | $B'=P^{-1}AP$ | 같은 변환, 다른 기저 |
| 불변량 | $\det,\ \operatorname{tr},\ \operatorname{rank}$, 고유값 | 닮음에서 보존 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $B=\{(3,0),(0,2)\}$의 전이행렬과 그 역행렬을 구하십시오.
> **답.** $P_B=\begin{bmatrix}3&0\\0&2\end{bmatrix}$, $P_B^{-1}=\begin{bmatrix}\tfrac13&0\\0&\tfrac12\end{bmatrix}$입니다.
> **풀이.** 대각행렬이라 역행렬은 대각 성분의 역수입니다.

> **문제 2.** (기초) $B=\{(1,0),(1,1)\}$에서 $[\mathbf{v}]_B=\begin{bmatrix}4\\-1\end{bmatrix}$일 때 $\mathbf{v}$를 구하십시오.
> **답.** $\mathbf{v}=(3,-1)$입니다.
> **풀이.** $\mathbf{v}=4(1,0)-1(1,1)=(4-1,\ 0-1)=(3,-1)$입니다.

> **문제 3.** (기초) $A=\begin{bmatrix}5&2\\1&4\end{bmatrix}$와 닮은 행렬의 대각합을 구하십시오.
> **답.** $9$입니다.
> **풀이.** 닮음은 대각합을 보존하므로 $5+4=9$입니다.

> **문제 4.** (표준) $B=\{(2,1),(-1,1)\}$로 $\mathbf{v}=(1,4)$의 좌표벡터를 구하십시오.
> **답.** $[\mathbf{v}]_B=\begin{bmatrix}\tfrac53\\\tfrac73\end{bmatrix}$입니다.
> **풀이.** $P_B=\begin{bmatrix}2&-1\\1&1\end{bmatrix}$, $\det=3$이라 $P_B^{-1}=\tfrac13\begin{bmatrix}1&1\\-1&2\end{bmatrix}$입니다. $[\mathbf{v}]_B=\tfrac13\begin{bmatrix}1&1\\-1&2\end{bmatrix}\begin{bmatrix}1\\4\end{bmatrix}=\tfrac13\begin{bmatrix}5\\7\end{bmatrix}$입니다. 검산하면 $\tfrac53(2,1)+\tfrac73(-1,1)=\big(\tfrac{10-7}{3},\tfrac{5+7}{3}\big)=(1,4)$입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}3&0\\0&5\end{bmatrix}$, $P=\begin{bmatrix}1&2\\0&1\end{bmatrix}$일 때 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}3&-4\\0&5\end{bmatrix}$입니다.
> **풀이.** $P^{-1}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}$입니다. $AP=\begin{bmatrix}3&0\\0&5\end{bmatrix}\begin{bmatrix}1&2\\0&1\end{bmatrix}=\begin{bmatrix}3&6\\0&5\end{bmatrix}$입니다. $P^{-1}(AP)=\begin{bmatrix}1&-2\\0&1\end{bmatrix}\begin{bmatrix}3&6\\0&5\end{bmatrix}$의 $(1,1)=3$, $(1,2)=1\cdot6+(-2)\cdot5=-4$, $(2,1)=0$, $(2,2)=5$이라 $\begin{bmatrix}3&-4\\0&5\end{bmatrix}$입니다.

> **문제 6.** (표준) $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$, $P=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$일 때 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$입니다.
> **풀이.** $\det P=-2$이라 $P^{-1}=\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}$입니다. $AP=\begin{bmatrix}0&1\\1&0\end{bmatrix}\begin{bmatrix}1&1\\1&-1\end{bmatrix}=\begin{bmatrix}1&-1\\1&1\end{bmatrix}$입니다. $P^{-1}(AP)$의 $(1,1)=\tfrac12\cdot1+\tfrac12\cdot1=1$, $(1,2)=\tfrac12\cdot(-1)+\tfrac12\cdot1=0$, $(2,1)=\tfrac12\cdot1-\tfrac12\cdot1=0$, $(2,2)=\tfrac12\cdot(-1)-\tfrac12\cdot1=-1$이라 $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$입니다. 대각합 0, 행렬식 $-1$이 원래 $A$와 일치합니다.

> **문제 7.** (표준) $\begin{bmatrix}2&0\\0&2\end{bmatrix}$와 닮은 행렬은 자기 자신뿐임을 설명하십시오.
> **답.** $P^{-1}(2I)P=2I$라 언제나 자기 자신입니다.
> **풀이.** 스칼라행렬 $2I$는 임의의 가역 $P$에 대해 $P^{-1}(2I)P=2P^{-1}P=2I$입니다. 어떤 기저에서 보아도 표현행렬이 변하지 않습니다.

> **문제 8.** (표준) 닮은 두 행렬 $A,B'$에 대해 $\operatorname{tr}A=6$, $\det A=8$이면 $B'$의 고유값의 합과 곱을 구하십시오.
> **답.** 합은 6, 곱은 8입니다.
> **풀이.** 고유값의 합은 대각합, 곱은 행렬식과 같고 둘 다 닮음에서 보존됩니다. 따라서 $B'$의 고유값 합은 6, 곱은 8입니다.

> **문제 9.** (심화) $B=\{(1,1),(2,3)\}$에서 $C=\{(1,0),(1,1)\}$로의 전이행렬 $P_{C\leftarrow B}$를 구하십시오.
> **답.** $\begin{bmatrix}0&-1\\1&3\end{bmatrix}$입니다.
> **풀이.** $P_B=\begin{bmatrix}1&2\\1&3\end{bmatrix}$, $P_C=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, $P_C^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. $P_{C\leftarrow B}=P_C^{-1}P_B=\begin{bmatrix}1&-1\\0&1\end{bmatrix}\begin{bmatrix}1&2\\1&3\end{bmatrix}$의 $(1,1)=1-1=0$, $(1,2)=2-3=-1$, $(2,1)=1$, $(2,2)=3$이라 $\begin{bmatrix}0&-1\\1&3\end{bmatrix}$입니다. 검산하면 $\mathbf{b}_1=(1,1)$의 $C$좌표는 $a(1,0)+b(1,1)=(1,1)$에서 $b=1,a=0$이라 $(0,1)$로 첫째 열과 일치합니다.

> **문제 10.** (심화) $A=\begin{bmatrix}1&1\\0&2\end{bmatrix}$를 고유벡터 기저 $P=\begin{bmatrix}1&1\\0&1\end{bmatrix}$로 대각화해 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}1&0\\0&2\end{bmatrix}$입니다.
> **풀이.** $P^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. $AP=\begin{bmatrix}1&1\\0&2\end{bmatrix}\begin{bmatrix}1&1\\0&1\end{bmatrix}=\begin{bmatrix}1&2\\0&2\end{bmatrix}$입니다. $P^{-1}(AP)$의 $(1,1)=1$, $(1,2)=2-2=0$, $(2,1)=0$, $(2,2)=2$이라 $\begin{bmatrix}1&0\\0&2\end{bmatrix}$입니다. 대각 성분 $1,2$가 $A$의 고유값입니다.

> **문제 11.** (심화) $A$와 $B'$가 닮고 $A$가 가역이면 $B'$도 가역이고 $A^{-1}$과 $B'^{-1}$이 닮음을 보이십시오.
> **답.** $B'^{-1}=P^{-1}A^{-1}P$라 닮습니다.
> **풀이.** $B'=P^{-1}AP$이면 $B'^{-1}=(P^{-1}AP)^{-1}=P^{-1}A^{-1}(P^{-1})^{-1}=P^{-1}A^{-1}P$입니다. $A$가 가역이라 $A^{-1}$이 존재하고 이 식이 정의되므로 $B'$도 가역이며, 같은 $P$로 $A^{-1}$과 $B'^{-1}$이 닮습니다.

## 5. 스스로 점검

1. 전이행렬 $P_B$를 기저벡터로 구성하는 방법을 말할 수 있는가?
2. $\mathbf{x}=P_B[\mathbf{x}]_B$와 $[\mathbf{x}]_B=P_B^{-1}\mathbf{x}$의 두 방향을 구별할 수 있는가?
3. 두 기저 사이의 전이행렬을 $P_C^{-1}P_B$로 구성할 수 있는가?
4. 표현행렬 변환 $[T]_B=P^{-1}AP$를 유도할 수 있는가?
5. 닮음의 정의를 쓸 수 있는가?
6. 닮은 행렬이 공유하는 불변량을 말할 수 있는가?
7. 대각합·행렬식이 닮음에서 보존되는 이유를 설명할 수 있는가?

**정답 요지.** 1. 기저벡터를 열로 세움. 2. 앞은 $B$좌표를 표준으로, 뒤는 표준을 $B$좌표로. 3. $C$의 전이행렬 역과 $B$의 전이행렬의 곱. 4. 되돌리기($P$)·적용($A$)·바꾸기($P^{-1}$)를 합성. 5. 가역 $P$로 $B'=P^{-1}AP$. 6. $\det$, $\operatorname{tr}$, $\operatorname{rank}$, 고유값. 7. $\det(P^{-1}AP)=\det A$, $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}(APP^{-1})=\operatorname{tr}A$.
