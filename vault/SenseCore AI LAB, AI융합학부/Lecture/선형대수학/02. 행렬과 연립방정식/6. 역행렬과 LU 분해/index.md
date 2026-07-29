---
title: "6. 역행렬과 LU 분해"
---
# 6강. 역행렬과 LU 분해

## 이 강의에서 할 수 있게 되는 것

- 역행렬을 정의하고 가역과 비가역(특이) 행렬을 구별할 수 있습니다.
- $2\times2$ 역행렬 공식과 가우스-조던 소거로 역행렬을 계산할 수 있습니다.
- 역행렬의 성질 $(AB)^{-1}=B^{-1}A^{-1}$과 가역성의 동치 조건을 진술할 수 있습니다.
- LU 분해를 이해하고 이를 이용해 연립방정식을 전진 대입과 후진 대입으로 풀 수 있습니다.

이 강의는 5강의 가우스 소거를 이용해 정사각행렬의 역행렬을 구하고, 소거 과정 자체를 행렬 분해로 기록하는 LU 분해를 다룹니다. 이 교본은 정의와 유도를 중심으로 진행합니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $A^{-1}$ | 에이 인버스 | $AA^{-1}=A^{-1}A=I$인 역행렬 |
| $I$ | 단위행렬 | 대각이 1, 나머지가 0인 행렬 |
| $\det A$ | 행렬식 | $2\times2$에서 $ad-bc$ |
| $L$ | 로어 | 대각 아래가 채워진 하삼각행렬 |
| $U$ | 어퍼 | 대각 위가 채워진 상삼각행렬 |
| $A=LU$ | 엘유 분해 | 하삼각과 상삼각의 곱으로 나눈 것 |
| $[\,A\mid I\,]$ | 첨가행렬 | 역행렬을 구하기 위해 붙인 단위행렬 |

## 2. 개념

### 2.1 역행렬의 정의

정사각행렬 $A\in\mathbb{R}^{n\times n}$에 대해

$$
AB=BA=I
$$

를 만족하는 행렬 $B$가 있으면 $A$를 가역이라고 하고, $B$를 $A$의 역행렬이라 하여 $A^{-1}$로 씁니다. 이런 $B$가 없으면 $A$를 비가역 또는 특이행렬이라고 합니다. 역행렬은 존재하면 유일합니다. 실제로 $B,C$가 모두 역행렬이면

$$
B=BI=B(AC)=(BA)C=IC=C
$$

이므로 같습니다. 역행렬은 방정식 $A\mathbf{x}=\mathbf{b}$의 해를 $\mathbf{x}=A^{-1}\mathbf{b}$로 직접 준다는 점에서 중요합니다. 양변 왼쪽에 $A^{-1}$을 곱하면 $A^{-1}A\mathbf{x}=A^{-1}\mathbf{b}$, 즉 $\mathbf{x}=A^{-1}\mathbf{b}$가 나오기 때문입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}2&0\\0&5\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1/2&0\\0&1/5\end{bmatrix}$입니다.
> **풀이.** 대각행렬의 역행렬은 각 대각 성분의 역수입니다. 검산하면 $\begin{bmatrix}2&0\\0&5\end{bmatrix}\begin{bmatrix}1/2&0\\0&1/5\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

> **문제 2.** (기초) $B=\begin{bmatrix}3&2\\1&1\end{bmatrix}$이 $A=\begin{bmatrix}1&-2\\-1&3\end{bmatrix}$의 역행렬인지 확인하십시오.
> **답.** 역행렬이 맞습니다.
> **풀이.** $AB=\begin{bmatrix}1\cdot3+(-2)\cdot1&1\cdot2+(-2)\cdot1\\-1\cdot3+3\cdot1&-1\cdot2+3\cdot1\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다. 곱이 단위행렬이므로 서로 역행렬입니다.

> **문제 3.** (표준) $A\mathbf{x}=\mathbf{b}$에서 $A^{-1}=\begin{bmatrix}2&-1\\-3&2\end{bmatrix}$, $\mathbf{b}=\begin{bmatrix}1\\4\end{bmatrix}$일 때 해를 구하십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}-2\\5\end{bmatrix}$입니다.
> **풀이.** $\mathbf{x}=A^{-1}\mathbf{b}=\begin{bmatrix}2\cdot1+(-1)\cdot4\\-3\cdot1+2\cdot4\end{bmatrix}=\begin{bmatrix}-2\\5\end{bmatrix}$입니다.

### 2.2 2×2 역행렬 공식

$2\times2$ 행렬 $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$의 역행렬은 다음 공식으로 구합니다.

$$
A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix},\qquad ad-bc\ne0
$$

여기서 $ad-bc$를 $A$의 행렬식이라 하고 $\det A$로 씁니다. 공식이 성립함은 직접 곱으로 확인됩니다.

$$
\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}
=\begin{bmatrix}ad-bc&0\\0&ad-bc\end{bmatrix}
=(ad-bc)I
$$

따라서 $ad-bc\ne0$이면 양변을 $ad-bc$로 나눠 역행렬을 얻습니다. 반대로 $ad-bc=0$이면 역행렬이 없습니다. 즉 $2\times2$ 행렬은 행렬식이 0이 아닐 때만 가역입니다.

> **문제 1.** (기초) $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}-2&1\\3/2&-1/2\end{bmatrix}$입니다.
> **풀이.** $\det A=1\cdot4-2\cdot3=-2$입니다. 공식에 넣으면 $A^{-1}=\tfrac{1}{-2}\begin{bmatrix}4&-2\\-3&1\end{bmatrix}=\begin{bmatrix}-2&1\\3/2&-1/2\end{bmatrix}$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}2&4\\1&2\end{bmatrix}$이 가역인지 판정하십시오.
> **답.** 비가역입니다.
> **풀이.** $\det A=2\cdot2-4\cdot1=0$입니다. 행렬식이 0이라 역행렬이 없습니다. 둘째 열이 첫째 열의 2배라 열이 종속입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}3&1\\5&2\end{bmatrix}$의 역행렬을 구하고 검산하십시오.
> **답.** $A^{-1}=\begin{bmatrix}2&-1\\-5&3\end{bmatrix}$입니다.
> **풀이.** $\det A=3\cdot2-1\cdot5=1$이라 $A^{-1}=\begin{bmatrix}2&-1\\-5&3\end{bmatrix}$입니다. 검산하면 $AA^{-1}=\begin{bmatrix}3\cdot2+1\cdot(-5)&3\cdot(-1)+1\cdot3\\5\cdot2+2\cdot(-5)&5\cdot(-1)+2\cdot3\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

### 2.3 가우스-조던 소거로 역행렬 구하기

$3\times3$ 이상에서는 공식 대신 소거를 씁니다. 첨가행렬 $[\,A\mid I\,]$를 만들고 행 연산으로 왼쪽 절반을 $I$로 만들면, 오른쪽 절반이 $A^{-1}$이 됩니다.

$$
[\,A\mid I\,]\ \xrightarrow{\ \text{행 연산}\ }\ [\,I\mid A^{-1}\,]
$$

원리는 이렇습니다. 왼쪽을 $I$로 만드는 행 연산들의 전체 효과는 $A$에 어떤 행렬 $M$을 곱하는 것과 같아 $MA=I$이므로 $M=A^{-1}$입니다. 같은 연산이 오른쪽 $I$에는 $MI=M=A^{-1}$을 남깁니다. 만약 왼쪽을 $I$로 만들 수 없다면(피벗이 부족해 0 행이 생기면) $A$는 비가역입니다.

예를 들어 $A=\begin{bmatrix}1&2\\1&3\end{bmatrix}$을 봅니다. $\left[\begin{array}{cc|cc}1&2&1&0\\1&3&0&1\end{array}\right]$에서 $R_2-R_1$로 $\left[\begin{array}{cc|cc}1&2&1&0\\0&1&-1&1\end{array}\right]$을 얻고, $R_1-2R_2$로 $\left[\begin{array}{cc|cc}1&0&3&-2\\0&1&-1&1\end{array}\right]$을 얻습니다. 따라서 $A^{-1}=\begin{bmatrix}3&-2\\-1&1\end{bmatrix}$입니다.

> **문제 1.** (표준) $A=\begin{bmatrix}1&0&2\\0&1&0\\0&0&1\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1&0&-2\\0&1&0\\0&0&1\end{bmatrix}$입니다.
> **풀이.** $R_1-2R_3$만 하면 왼쪽이 $I$가 됩니다. 오른쪽 $I$에 같은 연산을 적용하면 첫째 행이 $(1,0,-2)$가 됩니다. 나머지는 그대로입니다.

> **문제 2.** (심화) $A=\begin{bmatrix}1&1&0\\0&1&1\\0&0&1\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1&-1&1\\0&1&-1\\0&0&1\end{bmatrix}$입니다.
> **풀이.** $\left[\begin{array}{ccc|ccc}1&1&0&1&0&0\\0&1&1&0&1&0\\0&0&1&0&0&1\end{array}\right]$에서 $R_2-R_3$로 둘째 행 오른쪽이 $(0,1,-1)$, $R_1-R_2$로 첫째 행 오른쪽이 $(1,-1,0)$이 됩니다. 이때 $R_2$는 이미 바뀐 뒤이므로 $R_1$은 원래 $R_2-R_3$ 값을 뺍니다. 다시 정리하면 첫째 행 오른쪽은 $(1,-1,1)$입니다. 검산하면 $A A^{-1}$의 첫째 행은 $\begin{bmatrix}1&1&0\end{bmatrix}\begin{bmatrix}1&-1&1\\0&1&-1\\0&0&1\end{bmatrix}=(1,0,0)$으로 맞습니다.

> **문제 3.** (심화) $A=\begin{bmatrix}2&1&1\\1&2&1\\1&1&2\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\tfrac14\begin{bmatrix}3&-1&-1\\-1&3&-1\\-1&-1&3\end{bmatrix}$입니다.
> **풀이.** 이 행렬은 $A=I+J$ 꼴($J$는 모든 성분이 1)로 대칭입니다. 가우스-조던으로 소거하거나, $A^{-1}=aI+bJ$로 가정해 $A A^{-1}=I$를 풀면 $a=\tfrac34$, $b=-\tfrac14$이 나옵니다. 검산하면 첫째 행 $\begin{bmatrix}2&1&1\end{bmatrix}\cdot\tfrac14\begin{bmatrix}3\\-1\\-1\end{bmatrix}=\tfrac14(6-1-1)=1$이고, $\begin{bmatrix}2&1&1\end{bmatrix}\cdot\tfrac14\begin{bmatrix}-1\\3\\-1\end{bmatrix}=\tfrac14(-2+3-1)=0$으로 맞습니다.

### 2.4 역행렬의 성질과 가역성의 동치 조건

역행렬은 다음 성질을 만족합니다. $A,B$가 같은 크기 가역행렬일 때

$$
(A^{-1})^{-1}=A,\qquad (AB)^{-1}=B^{-1}A^{-1},\qquad (A^{T})^{-1}=(A^{-1})^{T}
$$

곱의 역행렬에서 순서가 뒤집힌다는 점에 유의합니다. $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I$로 확인됩니다. 또한 정사각행렬 $A\in\mathbb{R}^{n\times n}$에 대해 다음은 모두 동치입니다.

- $A$는 가역이다.
- $\operatorname{rank}(A)=n$이다.
- $A\mathbf{x}=\mathbf{0}$의 해가 $\mathbf{x}=\mathbf{0}$뿐이다.
- 모든 $\mathbf{b}$에 대해 $A\mathbf{x}=\mathbf{b}$가 유일한 해를 가진다.
- $A$의 기약 행 사다리꼴이 $I$이다.
- $\det A\ne0$이다.

이 목록을 가역행렬 정리라고 부릅니다. 한 조건만 확인하면 나머지가 모두 따라옵니다.

> **문제 1.** (기초) $A$가 가역일 때 $(A^{-1})^{-1}$은 무엇입니까?
> **답.** $A$입니다.
> **풀이.** $A^{-1}$의 역행렬은 $A^{-1}$과 곱해 $I$가 되는 행렬인데, $A^{-1}A=I$이므로 그것이 바로 $A$입니다.

> **문제 2.** (표준) $A,B$가 가역이고 $A^{-1}=\begin{bmatrix}1&0\\2&1\end{bmatrix}$, $B^{-1}=\begin{bmatrix}1&3\\0&1\end{bmatrix}$일 때 $(AB)^{-1}$을 구하십시오.
> **답.** $(AB)^{-1}=\begin{bmatrix}1&3\\2&7\end{bmatrix}$입니다.
> **풀이.** $(AB)^{-1}=B^{-1}A^{-1}=\begin{bmatrix}1&3\\0&1\end{bmatrix}\begin{bmatrix}1&0\\2&1\end{bmatrix}=\begin{bmatrix}1\cdot1+3\cdot2&1\cdot0+3\cdot1\\0\cdot1+1\cdot2&0\cdot0+1\cdot1\end{bmatrix}=\begin{bmatrix}7&3\\2&1\end{bmatrix}$… 순서에 유의합니다. $B^{-1}A^{-1}$의 $(1,1)=1\cdot1+3\cdot2=7$, $(1,2)=1\cdot0+3\cdot1=3$, $(2,1)=0\cdot1+1\cdot2=2$, $(2,2)=1$이라 $\begin{bmatrix}7&3\\2&1\end{bmatrix}$입니다.

> **문제 3.** (심화) $A=\begin{bmatrix}1&2\\2&4\end{bmatrix}$가 왜 비가역인지 가역행렬 정리의 세 조건으로 설명하십시오.
> **답.** $\det A=0$, $\operatorname{rank}(A)=1<2$, 그리고 $A\mathbf{x}=\mathbf{0}$이 영벡터가 아닌 해를 갖기 때문입니다.
> **풀이.** $\det A=1\cdot4-2\cdot2=0$입니다. $R_2-2R_1$로 둘째 행이 0이 되어 계수가 1입니다. $A\mathbf{x}=\mathbf{0}$은 $x_1+2x_2=0$뿐이라 $\mathbf{x}=\begin{bmatrix}-2\\1\end{bmatrix}$ 같은 영벡터가 아닌 해가 있습니다. 세 조건이 모두 비가역을 가리킵니다.

### 2.5 LU 분해

가우스 소거의 전진 과정은 행렬 분해로 기록할 수 있습니다. 행 교환이 필요 없는 경우, 정사각행렬 $A$를 하삼각행렬 $L$과 상삼각행렬 $U$의 곱으로 쓸 수 있습니다.

$$
A=LU
$$

여기서 $U$는 전진 소거로 얻은 상삼각 꼴이고, $L$은 대각이 1이며 대각 아래 성분이 소거에 쓴 배수(승수)인 하삼각행렬입니다. $R_i-\ell_{ij}R_j$로 소거했다면 $L$의 $(i,j)$ 성분이 $\ell_{ij}$입니다.

LU 분해가 유용한 까닭은 방정식 $A\mathbf{x}=\mathbf{b}$를 두 단계로 나눠 풀 수 있기 때문입니다. $A\mathbf{x}=LU\mathbf{x}=\mathbf{b}$에서 $\mathbf{y}=U\mathbf{x}$로 두면

$$
L\mathbf{y}=\mathbf{b}\ (\text{전진 대입})\quad\to\quad U\mathbf{x}=\mathbf{y}\ (\text{후진 대입})
$$

의 순서로 풉니다. 삼각행렬은 대입만으로 바로 풀리므로 계산이 빠릅니다. 특히 같은 $A$에 대해 여러 $\mathbf{b}$를 풀 때 분해를 한 번만 해두면 되므로 효율적입니다.

예를 들어 $A=\begin{bmatrix}2&1\\4&5\end{bmatrix}$을 봅니다. $R_2-2R_1$로 $U=\begin{bmatrix}2&1\\0&3\end{bmatrix}$을 얻습니다. 승수가 2이므로 $L=\begin{bmatrix}1&0\\2&1\end{bmatrix}$입니다. 검산하면 $LU=\begin{bmatrix}1&0\\2&1\end{bmatrix}\begin{bmatrix}2&1\\0&3\end{bmatrix}=\begin{bmatrix}2&1\\4&5\end{bmatrix}=A$입니다.

> **문제 1.** (표준) $A=\begin{bmatrix}1&2\\3&8\end{bmatrix}$의 LU 분해를 구하십시오.
> **답.** $L=\begin{bmatrix}1&0\\3&1\end{bmatrix}$, $U=\begin{bmatrix}1&2\\0&2\end{bmatrix}$입니다.
> **풀이.** $R_2-3R_1$로 둘째 행이 $(0,2)$가 되어 $U=\begin{bmatrix}1&2\\0&2\end{bmatrix}$입니다. 승수가 3이라 $L$의 $(2,1)$이 3입니다. 검산하면 $LU=\begin{bmatrix}1&2\\3&8\end{bmatrix}$입니다.

> **문제 2.** (심화) $A=\begin{bmatrix}2&1&1\\4&3&3\\8&7&9\end{bmatrix}$의 LU 분해를 구하십시오.
> **답.** $L=\begin{bmatrix}1&0&0\\2&1&0\\4&3&1\end{bmatrix}$, $U=\begin{bmatrix}2&1&1\\0&1&1\\0&0&2\end{bmatrix}$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,1,1)$, $R_3-4R_1$로 셋째 행 $(0,3,5)$을 얻습니다. 이어 $R_3-3R_2$로 셋째 행이 $(0,0,2)$가 되어 $U$가 완성됩니다. 승수는 $(2,1)=2$, $(3,1)=4$, $(3,2)=3$이라 $L$이 정해집니다. 검산하면 $LU$의 셋째 행은 $4\cdot(2,1,1)+3\cdot(0,1,1)+1\cdot(0,0,2)=(8,7,9)$로 맞습니다.

> **문제 3.** (심화) 위 문제 2의 분해를 이용해 $A\mathbf{x}=\begin{bmatrix}4\\10\\24\end{bmatrix}$을 푸십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}1\\1\\1\end{bmatrix}$입니다.
> **풀이.** 먼저 $L\mathbf{y}=\mathbf{b}$를 전진 대입합니다. $y_1=4$, $2y_1+y_2=10$이라 $y_2=2$, $4y_1+3y_2+y_3=24$이라 $y_3=24-16-6=2$입니다. 다음 $U\mathbf{x}=\mathbf{y}$를 후진 대입합니다. $2x_3=2$이라 $x_3=1$, $x_2+x_3=2$이라 $x_2=1$, $2x_1+x_2+x_3=4$이라 $x_1=1$입니다. 검산하면 $A\mathbf{x}$의 첫 성분 $2+1+1=4$로 맞습니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 역행렬 정의 | $AA^{-1}=A^{-1}A=I$ | 정사각행렬에서만 |
| $2\times2$ 역행렬 | $\tfrac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$ | 대각 교환, 비대각 부호 반전 |
| 가역 판정 | $\det A\ne0$ 또는 $\operatorname{rank}=n$ | 하나만 확인하면 충분 |
| 소거로 역행렬 | $[\,A\mid I\,]\to[\,I\mid A^{-1}\,]$ | 왼쪽을 $I$로 만든다 |
| 곱의 역행렬 | $(AB)^{-1}=B^{-1}A^{-1}$ | 순서 뒤집힘 |
| 방정식 풀이 | $\mathbf{x}=A^{-1}\mathbf{b}$ | 가역일 때만 |
| LU 분해 | $A=LU$ | $U$는 소거 결과, $L$은 승수 |
| LU로 풀기 | $L\mathbf{y}=\mathbf{b}\to U\mathbf{x}=\mathbf{y}$ | 전진 대입 후 후진 대입 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $A=\begin{bmatrix}4&3\\1&1\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1&-3\\-1&4\end{bmatrix}$입니다.
> **풀이.** $\det A=4\cdot1-3\cdot1=1$이라 $A^{-1}=\begin{bmatrix}1&-3\\-1&4\end{bmatrix}$입니다. 검산하면 $AA^{-1}=\begin{bmatrix}4-3&-12+12\\1-1&-3+4\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}6&3\\4&2\end{bmatrix}$이 가역인지 판정하십시오.
> **답.** 비가역입니다.
> **풀이.** $\det A=6\cdot2-3\cdot4=0$입니다. 행렬식이 0이라 역행렬이 없습니다.

> **문제 3.** (기초) 대각행렬 $A=\begin{bmatrix}3&0&0\\0&-2&0\\0&0&5\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1/3&0&0\\0&-1/2&0\\0&0&1/5\end{bmatrix}$입니다.
> **풀이.** 대각행렬의 역행렬은 각 대각 성분의 역수입니다. 어떤 대각 성분도 0이 아니라 가역입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&2\\3&5\end{bmatrix}$의 역행렬로 $A\mathbf{x}=\begin{bmatrix}1\\2\end{bmatrix}$을 푸십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}-1\\1\end{bmatrix}$입니다.
> **풀이.** $\det A=1\cdot5-2\cdot3=-1$이라 $A^{-1}=\tfrac{1}{-1}\begin{bmatrix}5&-2\\-3&1\end{bmatrix}=\begin{bmatrix}-5&2\\3&-1\end{bmatrix}$입니다. $\mathbf{x}=A^{-1}\mathbf{b}=\begin{bmatrix}-5\cdot1+2\cdot2\\3\cdot1-1\cdot2\end{bmatrix}=\begin{bmatrix}-1\\1\end{bmatrix}$입니다. 검산하면 $\begin{bmatrix}1&2\\3&5\end{bmatrix}\begin{bmatrix}-1\\1\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}$입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}1&0&0\\2&1&0\\1&3&1\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1&0&0\\-2&1&0\\5&-3&1\end{bmatrix}$입니다.
> **풀이.** $[\,A\mid I\,]$에서 $R_2-2R_1$로 둘째 행 오른쪽 $(-2,1,0)$, $R_3-R_1$로 셋째 행 오른쪽 $(-1,0,1)$이 됩니다. 이어 $R_3-3R_2$로 셋째 행 오른쪽이 $(-1-3(-2),0-3,1)=(5,-3,1)$이 됩니다. 검산하면 $A A^{-1}$의 셋째 행은 $1\cdot(1,0,0)+3\cdot(-2,1,0)+1\cdot(5,-3,1)=(0,0,1)$입니다.

> **문제 6.** (표준) $A=\begin{bmatrix}3&6\\2&5\end{bmatrix}$의 LU 분해를 구하십시오.
> **답.** $L=\begin{bmatrix}1&0\\2/3&1\end{bmatrix}$, $U=\begin{bmatrix}3&6\\0&1\end{bmatrix}$입니다.
> **풀이.** $R_2-\tfrac23R_1$로 둘째 행이 $(0,5-4)=(0,1)$이 되어 $U=\begin{bmatrix}3&6\\0&1\end{bmatrix}$입니다. 승수가 $\tfrac23$이라 $L$의 $(2,1)$이 $\tfrac23$입니다. 검산하면 $LU$의 둘째 행은 $\tfrac23(3,6)+(0,1)=(2,5)$로 맞습니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&1&1\\2&3&5\\4&6&8\end{bmatrix}$의 LU 분해에서 $U$를 구하십시오.
> **답.** $U=\begin{bmatrix}1&1&1\\0&1&3\\0&0&-2\end{bmatrix}$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,1,3)$, $R_3-4R_1$로 셋째 행 $(0,2,4)$을 얻습니다. 이어 $R_3-2R_2$로 셋째 행이 $(0,0,4-6)=(0,0,-2)$가 됩니다. 이것이 $U$입니다.

> **문제 8.** (표준) $A=\begin{bmatrix}1&2\\2&3\end{bmatrix}$에 대해 $(A^{-1})^{T}=(A^{T})^{-1}$임을 확인하십시오.
> **답.** 양변 모두 $\begin{bmatrix}-3&2\\2&-1\end{bmatrix}$입니다.
> **풀이.** $\det A=1\cdot3-2\cdot2=-1$이라 $A^{-1}=\tfrac{1}{-1}\begin{bmatrix}3&-2\\-2&1\end{bmatrix}=\begin{bmatrix}-3&2\\2&-1\end{bmatrix}$이고 이것은 대칭이라 $(A^{-1})^{T}$도 같습니다. $A^{T}=\begin{bmatrix}1&2\\2&3\end{bmatrix}=A$이라 $(A^{T})^{-1}=A^{-1}$로 같습니다.

> **문제 9.** (심화) $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$은 행 교환이 필요해 $A=LU$로 바로 분해되지 않음을 설명하십시오.
> **답.** $(1,1)$ 성분이 0이라 피벗이 없어 순열 없이는 하삼각·상삼각 곱으로 쓸 수 없습니다.
> **풀이.** LU 분해는 소거 중 대각에 0 아닌 피벗이 계속 나올 때 가능합니다. $A$는 첫 피벗 자리가 0이라 $R_1\leftrightarrow R_2$가 필요합니다. 이 교환을 순열행렬 $P$로 기록하면 $PA=LU$ 꼴의 부분 피벗 분해가 됩니다. 여기서 $PA=\begin{bmatrix}1&0\\0&1\end{bmatrix}$이라 $L=U=I$입니다.

> **문제 10.** (심화) $A,B$가 가역일 때 $(ABA^{-1})^{-1}=AB^{-1}A^{-1}$임을 보이십시오.
> **답.** 곱의 역행렬 규칙을 두 번 적용하면 됩니다.
> **풀이.** $(ABA^{-1})^{-1}=(A^{-1})^{-1}B^{-1}A^{-1}=AB^{-1}A^{-1}$입니다. 순서를 뒤집으면 $A^{-1}$의 역행렬은 $A$가 되고, 가운데 $B$가 $B^{-1}$이 되며, 맨 앞 $A$가 뒤로 가 $A^{-1}$이 됩니다.

> **문제 11.** (심화) $A$가 가역이고 $A^2=A$이면 $A=I$임을 보이십시오.
> **답.** 양변에 $A^{-1}$을 곱하면 $A=I$가 됩니다.
> **풀이.** $A^2=A$의 양변 왼쪽에 $A^{-1}$을 곱하면 $A^{-1}A^2=A^{-1}A$, 즉 $A=I$입니다. 가역이라는 조건이 없으면 $A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$ 같은 반례가 있어 성립하지 않습니다.

## 5. 스스로 점검

1. 역행렬을 정의하고 유일함을 설명할 수 있는가?
2. $2\times2$ 역행렬 공식을 쓰고 가역 조건을 말할 수 있는가?
3. $[\,A\mid I\,]$ 소거로 역행렬을 구하는 원리를 설명할 수 있는가?
4. $(AB)^{-1}=B^{-1}A^{-1}$을 진술하고 증명할 수 있는가?
5. 가역행렬 정리의 동치 조건을 세 개 이상 말할 수 있는가?
6. LU 분해에서 $L$과 $U$가 각각 무엇인지 말할 수 있는가?
7. LU 분해로 방정식을 전진·후진 대입으로 풀 수 있는가?

**정답 요지.** 1. $AB=BA=I$인 $B$, 두 역행렬이 같음을 결합법칙으로 보임. 2. $\tfrac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$, $ad-bc\ne0$. 3. 왼쪽을 $I$로 만드는 연산이 $A^{-1}$을 곱하는 것과 같아 오른쪽에 $A^{-1}$이 남음. 4. $(AB)(B^{-1}A^{-1})=I$. 5. 가역 / $\operatorname{rank}=n$ / $A\mathbf{x}=\mathbf{0}$이 자명해뿐 / $\det A\ne0$ 등. 6. $U$는 소거로 얻은 상삼각, $L$은 승수로 채운 대각 1의 하삼각. 7. $L\mathbf{y}=\mathbf{b}$ 전진 대입 후 $U\mathbf{x}=\mathbf{y}$ 후진 대입.
