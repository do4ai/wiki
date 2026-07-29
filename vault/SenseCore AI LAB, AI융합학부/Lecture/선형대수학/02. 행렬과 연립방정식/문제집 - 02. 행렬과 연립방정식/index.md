---
title: "문제집 - 02. 행렬과 연립방정식"
---
# 문제집 - 02. 행렬과 연립방정식

이 문제집은 2단원 네 강의(행렬 연산 / 가우스 소거와 계수 / 역행렬과 LU 분해 / 행렬식)의 내용을 본문보다 한 단계 어렵게 훈련하기 위한 것입니다. 각 문제는 난이도(기초·표준·심화)를 표시했고, 답과 단계별 풀이를 함께 실었습니다. 손으로 풀 때는 답을 가리고 풀이의 중간식을 스스로 재현해 보시기 바랍니다. 행렬 계산은 반드시 곱을 다시 전개해 검산하시기 바랍니다.

## 1. 행렬 연산

> **문제 1.** (기초) $A=\begin{bmatrix}2&-1\\1&3\end{bmatrix}$, $B=\begin{bmatrix}0&4\\2&-1\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}-2&9\\6&1\end{bmatrix}$입니다.
> **풀이.** $(1,1)=2\cdot0+(-1)\cdot2=-2$, $(1,2)=2\cdot4+(-1)\cdot(-1)=9$, $(2,1)=1\cdot0+3\cdot2=6$, $(2,2)=1\cdot4+3\cdot(-1)=1$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}1&-2\\0&3\end{bmatrix}$일 때 $(2A)^{T}$를 구하십시오.
> **답.** $\begin{bmatrix}2&0\\-4&6\end{bmatrix}$입니다.
> **풀이.** $2A=\begin{bmatrix}2&-4\\0&6\end{bmatrix}$입니다. 여기서 행과 열을 맞바꾸면 첫째 행 $(2,-4)$가 첫째 열이 되어 $(2A)^{T}=\begin{bmatrix}2&0\\-4&6\end{bmatrix}$입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&2&-1\\0&3&1\end{bmatrix}$, $B=\begin{bmatrix}2&0\\1&1\\3&-2\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}1&4\\6&1\end{bmatrix}$입니다.
> **풀이.** $A$는 $2\times3$, $B$는 $3\times2$라 곱은 $2\times2$입니다. $(1,1)=1\cdot2+2\cdot1+(-1)\cdot3=1$, $(1,2)=1\cdot0+2\cdot1+(-1)\cdot(-2)=4$, $(2,1)=0\cdot2+3\cdot1+1\cdot3=6$, $(2,2)=0\cdot0+3\cdot1+1\cdot(-2)=1$입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&2\\-1&3\end{bmatrix}$일 때 $A^{2}$을 구하십시오.
> **답.** $\begin{bmatrix}-1&8\\-4&7\end{bmatrix}$입니다.
> **풀이.** $A^{2}=AA$입니다. $(1,1)=1\cdot1+2\cdot(-1)=-1$, $(1,2)=1\cdot2+2\cdot3=8$, $(2,1)=-1\cdot1+3\cdot(-1)=-4$, $(2,2)=-1\cdot2+3\cdot3=7$입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}2&1\\0&3\end{bmatrix}$, $B=\begin{bmatrix}1&-1\\2&4\end{bmatrix}$에 대해 $(AB)^{T}=B^{T}A^{T}$임을 계산으로 확인하십시오.
> **답.** 양변 모두 $\begin{bmatrix}4&6\\2&12\end{bmatrix}$입니다.
> **풀이.** $AB=\begin{bmatrix}2\cdot1+1\cdot2&2\cdot(-1)+1\cdot4\\0\cdot1+3\cdot2&0\cdot(-1)+3\cdot4\end{bmatrix}=\begin{bmatrix}4&2\\6&12\end{bmatrix}$이라 $(AB)^{T}=\begin{bmatrix}4&6\\2&12\end{bmatrix}$입니다. 한편 $B^{T}=\begin{bmatrix}1&2\\-1&4\end{bmatrix}$, $A^{T}=\begin{bmatrix}2&0\\1&3\end{bmatrix}$이라 $B^{T}A^{T}=\begin{bmatrix}1\cdot2+2\cdot1&1\cdot0+2\cdot3\\-1\cdot2+4\cdot1&-1\cdot0+4\cdot3\end{bmatrix}=\begin{bmatrix}4&6\\2&12\end{bmatrix}$로 일치합니다.

> **문제 6.** (표준) $A=\begin{bmatrix}1&1\\0&1\end{bmatrix}$일 때 $A^{4}$을 구하십시오.
> **답.** $\begin{bmatrix}1&4\\0&1\end{bmatrix}$입니다.
> **풀이.** $A^{2}=\begin{bmatrix}1&2\\0&1\end{bmatrix}$입니다($(1,2)=1\cdot1+1\cdot1=2$). $A^{4}=A^{2}A^{2}$의 $(1,2)=1\cdot2+2\cdot1=4$이고 나머지는 그대로라 $\begin{bmatrix}1&4\\0&1\end{bmatrix}$입니다. 일반적으로 $A^{n}=\begin{bmatrix}1&n\\0&1\end{bmatrix}$입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&2\\0&1\\2&1\end{bmatrix}$일 때 $A^{T}A$를 구하고 대칭임을 확인하십시오.
> **답.** $\begin{bmatrix}5&4\\4&6\end{bmatrix}$이고 대칭입니다.
> **풀이.** $A^{T}=\begin{bmatrix}1&0&2\\2&1&1\end{bmatrix}$입니다. $(1,1)=1\cdot1+0\cdot0+2\cdot2=5$, $(1,2)=1\cdot2+0\cdot1+2\cdot1=4$, $(2,1)=2\cdot1+1\cdot0+1\cdot2=4$, $(2,2)=2\cdot2+1\cdot1+1\cdot1=6$입니다. $(1,2)=(2,1)=4$라 대칭입니다.

> **문제 8.** (심화) $A=\begin{bmatrix}1&2&0\\0&1&1\\1&0&1\end{bmatrix}$, $B=\begin{bmatrix}2&0&1\\1&1&0\\0&1&3\end{bmatrix}$일 때 $AB$를 구하십시오.
> **답.** $\begin{bmatrix}4&2&1\\1&2&3\\2&1&4\end{bmatrix}$입니다.
> **풀이.** 첫째 행: $(1,1)=1\cdot2+2\cdot1+0\cdot0=4$, $(1,2)=1\cdot0+2\cdot1+0\cdot1=2$, $(1,3)=1\cdot1+2\cdot0+0\cdot3=1$입니다. 둘째 행: $(2,1)=0\cdot2+1\cdot1+1\cdot0=1$, $(2,2)=0\cdot0+1\cdot1+1\cdot1=2$, $(2,3)=0\cdot1+1\cdot0+1\cdot3=3$입니다. 셋째 행: $(3,1)=1\cdot2+0\cdot1+1\cdot0=2$, $(3,2)=1\cdot0+0\cdot1+1\cdot1=1$, $(3,3)=1\cdot1+0\cdot0+1\cdot3=4$입니다.

> **문제 9.** (심화) $A=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}$일 때 $A^{2}$과 $A^{3}$을 구하고 $A$가 멱영행렬임을 보이십시오.
> **답.** $A^{2}=\begin{bmatrix}0&0&1\\0&0&0\\0&0&0\end{bmatrix}$, $A^{3}=O$입니다.
> **풀이.** $A^{2}=AA$의 $(1,3)=0\cdot0+1\cdot0+0\cdot0$… 성분을 직접 봅니다. $A$의 첫째 행 $(0,1,0)$과 $A$의 셋째 열 $(0,1,0)$의 내적이 $(1,3)=0\cdot0+1\cdot1+0\cdot0=1$이고, 그 밖의 자리는 모두 0입니다. 다시 $A^{3}=A^{2}A$는 $A^{2}$의 유일한 0 아닌 자리 $(1,3)$이 $A$의 셋째 행 $(0,0,0)$과 만나 사라지므로 $O$입니다. $A\ne O$인데 $A^{3}=O$이라 멱영행렬입니다.

> **문제 10.** (심화) $A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $B=\begin{bmatrix}0&1\\0&0\end{bmatrix}$에 대해 $(A+B)^{2}\ne A^{2}+2AB+B^{2}$임을 계산으로 확인하십시오.
> **답.** $(A+B)^{2}=\begin{bmatrix}1&1\\0&0\end{bmatrix}$이지만 $A^{2}+2AB+B^{2}=\begin{bmatrix}1&2\\0&0\end{bmatrix}$입니다.
> **풀이.** $A+B=\begin{bmatrix}1&1\\0&0\end{bmatrix}$이라 $(A+B)^{2}=\begin{bmatrix}1&1\\0&0\end{bmatrix}\begin{bmatrix}1&1\\0&0\end{bmatrix}=\begin{bmatrix}1&1\\0&0\end{bmatrix}$입니다. 한편 $A^{2}=A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $B^{2}=O$, $AB=\begin{bmatrix}0&1\\0&0\end{bmatrix}$이라 $2AB=\begin{bmatrix}0&2\\0&0\end{bmatrix}$입니다. 합은 $\begin{bmatrix}1&2\\0&0\end{bmatrix}$입니다. 두 결과가 다른 까닭은 $BA=O\ne AB$라 교환법칙이 성립하지 않기 때문입니다. 곱셈이 교환되지 않으면 $(A+B)^{2}=A^{2}+AB+BA+B^{2}$가 옳은 전개입니다.

> **문제 11.** (심화) 임의의 $2\times2$ 행렬 $A,B$에 대해 $\operatorname{tr}(AB)=\operatorname{tr}(BA)$임을 $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$에서 확인하십시오(단 $\operatorname{tr}$는 대각합).
> **답.** 양변 모두 $5$입니다.
> **풀이.** $AB=\begin{bmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot0\\3\cdot0+4\cdot1&3\cdot1+4\cdot0\end{bmatrix}=\begin{bmatrix}2&1\\4&3\end{bmatrix}$이라 $\operatorname{tr}(AB)=2+3=5$입니다. $BA=\begin{bmatrix}0\cdot1+1\cdot3&0\cdot2+1\cdot4\\1\cdot1+0\cdot3&1\cdot2+0\cdot4\end{bmatrix}=\begin{bmatrix}3&4\\1&2\end{bmatrix}$이라 $\operatorname{tr}(BA)=3+2=5$입니다. $AB\ne BA$이지만 대각합은 같습니다.

## 2. 가우스 소거와 계수

> **문제 1.** (기초) $\begin{cases}x+2y=4\\3x+2y=8\end{cases}$을 가우스 소거로 푸십시오.
> **답.** $x=2$, $y=1$입니다.
> **풀이.** $\left[\begin{array}{cc|c}1&2&4\\3&2&8\end{array}\right]$에서 $R_2-3R_1$로 $\left[\begin{array}{cc|c}1&2&4\\0&-4&-4\end{array}\right]$을 얻습니다. 둘째 행 $-4y=-4$에서 $y=1$, 첫째 행 $x+2=4$에서 $x=2$입니다. 검산하면 $2+2=4$, $6+2=8$입니다.

> **문제 2.** (기초) $\begin{bmatrix}1&2&1\\2&4&3\end{bmatrix}$의 계수를 구하십시오.
> **답.** $\operatorname{rank}=2$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행이 $(0,0,1)$이 됩니다. 피벗은 첫째 행의 $(1,1)$과 둘째 행의 $(2,3)$으로 두 개라 계수는 2입니다.

> **문제 3.** (표준) $\begin{cases}x+y+z=6\\x+2y-z=1\\2x-y+z=6\end{cases}$을 푸십시오.
> **답.** $x=2$, $y=1$, $z=3$입니다.
> **풀이.** $\left[\begin{array}{ccc|c}1&1&1&6\\1&2&-1&1\\2&-1&1&6\end{array}\right]$에서 $R_2-R_1$로 둘째 행 $(0,1,-2\mid-5)$, $R_3-2R_1$로 셋째 행 $(0,-3,-1\mid-6)$을 얻습니다. $R_3+3R_2$로 셋째 행이 $(0,0,-7\mid-21)$이 되어 $z=3$입니다. 둘째 행 $y-2\cdot3=-5$에서 $y=1$, 첫째 행 $x+1+3=6$에서 $x=2$입니다. 검산하면 $2+1+3=6$, $2+2-3=1$, $4-1+3=6$입니다.

> **문제 4.** (표준) $\begin{cases}x+y+z=3\\x+2y+3z=4\end{cases}$의 해를 자유변수로 표현하십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}2\\1\\0\end{bmatrix}+t\begin{bmatrix}1\\-2\\1\end{bmatrix}$입니다.
> **풀이.** $R_2-R_1$로 둘째 행이 $(0,1,2\mid1)$이 되어 $y+2z=1$입니다. $z=t$로 두면 $y=1-2t$이고, 첫째 행 $x+y+z=3$에서 $x=3-(1-2t)-t=2+t$입니다. 벡터로 정리하면 특수해 $(2,1,0)$에 방향 $(1,-2,1)$을 더한 꼴입니다. 검산하면 첫 식 $(2+t)+(1-2t)+t=3$, 둘째 식 $(2+t)+2(1-2t)+3t=4$로 모두 맞습니다.

> **문제 5.** (표준) $\begin{cases}x+2y=1\\3x+6y=5\end{cases}$의 해를 판정하십시오.
> **답.** 해가 없습니다.
> **풀이.** $R_2-3R_1$로 둘째 행이 $(0,0\mid2)$, 즉 $0=2$입니다. 모순이라 해가 존재하지 않습니다. 두 직선이 평행하기 때문입니다.

> **문제 6.** (표준) 동차방정식 $\begin{cases}x+y+2z=0\\2x+3y+z=0\end{cases}$의 영벡터가 아닌 해를 하나 구하십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}-5\\3\\1\end{bmatrix}$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행이 $(0,1,-3\mid0)$이 되어 $y=3z$입니다. 첫 식에 넣으면 $x=-y-2z=-3z-2z=-5z$입니다. $z=1$로 두면 $\begin{bmatrix}-5\\3\\1\end{bmatrix}$이고, 검산하면 $-5+3+2=0$, $-10+9+1=0$입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&2&3\\2&4&6\\1&1&1\end{bmatrix}$의 계수를 구하십시오.
> **답.** $\operatorname{rank}(A)=2$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행이 $(0,0,0)$, $R_3-R_1$로 셋째 행이 $(0,-1,-2)$가 됩니다. 0이 아닌 행을 정리하면 피벗이 첫째 행의 $(1,1)$과 셋째 행의 $(0,-1,-2)$의 $(2)$ 자리로 두 개라 계수는 2입니다.

> **문제 8.** (심화) 매개변수 $a$에 대해 $\begin{cases}x+y+z=1\\x+2y+z=2\\x+y+az=3\end{cases}$이 유일해를 갖도록 하는 $a$의 조건을 구하십시오.
> **답.** $a\ne1$입니다.
> **풀이.** $R_2-R_1$로 둘째 행 $(0,1,0\mid1)$, $R_3-R_1$로 셋째 행 $(0,0,a-1\mid2)$을 얻습니다. $a-1\ne0$이면 셋째 행에서 $z=\dfrac{2}{a-1}$로 정해지고, 둘째 행에서 $y=1$, 첫째 행에서 $x$가 유일하게 결정됩니다. $a=1$이면 셋째 행이 $0=2$라 해가 없습니다. 따라서 유일해 조건은 $a\ne1$입니다.

> **문제 9.** (심화) $\begin{cases}x+2y+z=1\\2x+5y+3z=2\\3x+7y+4z=k\end{cases}$가 해를 가질 $k$를 구하십시오.
> **답.** $k=3$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,1,1\mid0)$, $R_3-3R_1$로 셋째 행 $(0,1,1\mid k-3)$을 얻습니다. $R_3-R_2$로 셋째 행이 $(0,0,0\mid k-3)$이 됩니다. 해가 있으려면 $k-3=0$, 즉 $k=3$이어야 하고, 이때 자유변수가 하나라 해가 무수히 많습니다.

> **문제 10.** (심화) $A=\begin{bmatrix}1&2&1&0\\2&4&1&1\\3&6&2&1\end{bmatrix}$의 계수와 $A\mathbf{x}=\mathbf{0}$의 자유변수 개수를 구하십시오.
> **답.** $\operatorname{rank}(A)=2$, 자유변수 $2$개입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,0,-1,1)$, $R_3-3R_1$로 셋째 행 $(0,0,-1,1)$을 얻습니다. $R_3-R_2$로 셋째 행이 $(0,0,0,0)$이 됩니다. 피벗은 첫째 열과 셋째 열의 두 개라 계수는 2입니다. 미지수가 $n=4$이므로 자유변수는 $4-2=2$개입니다.

> **문제 11.** (심화) $\begin{cases}2x+y-z=2\\x+2y+z=4\\x-y+3z=3\end{cases}$을 가우스-조던 소거로 기약 행 사다리꼴까지 정리해 푸십시오.
> **답.** $x=y=z=1$입니다.
> **풀이.** $R_1\leftrightarrow R_2$로 $\left[\begin{array}{ccc|c}1&2&1&4\\2&1&-1&2\\1&-1&3&3\end{array}\right]$을 만듭니다. $R_2-2R_1$로 둘째 행 $(0,-3,-3\mid-6)$, $R_3-R_1$로 셋째 행 $(0,-3,2\mid-1)$을 얻습니다. $-\tfrac13R_2$로 둘째 행 $(0,1,1\mid2)$, 이어 $R_3+3R_2$로 셋째 행 $(0,0,5\mid5)$이 되어 $z=1$입니다. 둘째 행 $y+z=2$에서 $y=1$, 첫째 행 $x+2y+z=4$에서 $x=1$입니다. 검산하면 $2+1-1=2$, $1+2+1=4$, $1-1+3=3$입니다.

> **문제 12.** (심화) 어떤 연립방정식 $A\mathbf{x}=\mathbf{b}$가 서로 다른 두 해 $\mathbf{x}_1\ne\mathbf{x}_2$를 가지면 무수히 많은 해를 가짐을 설명하십시오.
> **답.** 두 해의 차가 동차방정식의 영벡터가 아닌 해가 되어 해의 직선 전체가 생기기 때문입니다.
> **풀이.** $A\mathbf{x}_1=\mathbf{b}$, $A\mathbf{x}_2=\mathbf{b}$를 빼면 $A(\mathbf{x}_1-\mathbf{x}_2)=\mathbf{0}$입니다. $\mathbf{x}_1\ne\mathbf{x}_2$이므로 $\mathbf{d}=\mathbf{x}_1-\mathbf{x}_2\ne\mathbf{0}$은 $A\mathbf{x}=\mathbf{0}$의 영벡터가 아닌 해입니다. 그러면 임의의 실수 $t$에 대해 $A(\mathbf{x}_1+t\mathbf{d})=\mathbf{b}+t\mathbf{0}=\mathbf{b}$이라 $\mathbf{x}_1+t\mathbf{d}$가 모두 해입니다. 서로 다른 $t$는 서로 다른 해를 주므로 해가 무수히 많습니다.

## 3. 역행렬과 LU 분해

> **문제 1.** (기초) $A=\begin{bmatrix}4&7\\1&2\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}2&-7\\-1&4\end{bmatrix}$입니다.
> **풀이.** $\det A=4\cdot2-7\cdot1=1$이라 $A^{-1}=\tfrac11\begin{bmatrix}2&-7\\-1&4\end{bmatrix}$입니다. 검산하면 $AA^{-1}=\begin{bmatrix}4\cdot2+7\cdot(-1)&4\cdot(-7)+7\cdot4\\1\cdot2+2\cdot(-1)&1\cdot(-7)+2\cdot4\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}3&6\\2&4\end{bmatrix}$이 가역인지 판정하십시오.
> **답.** 비가역입니다.
> **풀이.** $\det A=3\cdot4-6\cdot2=0$입니다. 행렬식이 0이라 역행렬이 없습니다. 둘째 열이 첫째 열의 2배라 열이 종속입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}2&1\\5&3\end{bmatrix}$의 역행렬로 $A\mathbf{x}=\begin{bmatrix}1\\2\end{bmatrix}$을 푸십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}1\\-1\end{bmatrix}$입니다.
> **풀이.** $\det A=2\cdot3-1\cdot5=1$이라 $A^{-1}=\begin{bmatrix}3&-1\\-5&2\end{bmatrix}$입니다. $\mathbf{x}=A^{-1}\mathbf{b}=\begin{bmatrix}3\cdot1-1\cdot2\\-5\cdot1+2\cdot2\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix}$입니다. 검산하면 $\begin{bmatrix}2&1\\5&3\end{bmatrix}\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}$입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&0&0\\3&1&0\\2&4&1\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}1&0&0\\-3&1&0\\10&-4&1\end{bmatrix}$입니다.
> **풀이.** $[\,A\mid I\,]$에서 $R_2-3R_1$로 둘째 행 오른쪽 $(-3,1,0)$, $R_3-2R_1$로 셋째 행 오른쪽 $(-2,0,1)$이 됩니다. 이어 $R_3-4R_2$로 셋째 행 오른쪽이 $(-2,0,1)-4(-3,1,0)=(10,-4,1)$이 됩니다. 검산하면 $A A^{-1}$의 셋째 행은 $2\cdot(1,0,0)+4\cdot(-3,1,0)+1\cdot(10,-4,1)=(0,0,1)$입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}1&2\\3&5\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}-5&2\\3&-1\end{bmatrix}$입니다.
> **풀이.** $\det A=1\cdot5-2\cdot3=-1$이라 $A^{-1}=\tfrac{1}{-1}\begin{bmatrix}5&-2\\-3&1\end{bmatrix}=\begin{bmatrix}-5&2\\3&-1\end{bmatrix}$입니다. 검산하면 $AA^{-1}=\begin{bmatrix}-5+6&2-2\\-15+15&6-5\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$입니다.

> **문제 6.** (심화) $A=\begin{bmatrix}2&1&0\\1&2&1\\0&1&2\end{bmatrix}$의 역행렬을 가우스-조던 소거로 구하십시오.
> **답.** $A^{-1}=\tfrac14\begin{bmatrix}3&-2&1\\-2&4&-2\\1&-2&3\end{bmatrix}$입니다.
> **풀이.** $[\,A\mid I\,]$에서 $R_1-2R_2$… 대신 표준 소거로 진행합니다. $R_2-\tfrac12R_1$로 둘째 행이 $(0,\tfrac32,1)$, $R_3-\tfrac23R_2$로 셋째 행이 $(0,0,\tfrac43)$이 되어 왼쪽이 상삼각이 됩니다. 계속 후진 소거해 왼쪽을 $I$로 만들면 오른쪽에 위 결과가 남습니다. 검산하면 $A A^{-1}$의 첫째 행은 $\tfrac14\big(2\cdot(3,-2,1)+1\cdot(-2,4,-2)\big)=\tfrac14(4,0,0)=(1,0,0)$이고, 대칭성으로 나머지 행도 단위행렬이 됩니다.

> **문제 7.** (표준) $A=\begin{bmatrix}2&3\\6&7\end{bmatrix}$의 LU 분해를 구하십시오.
> **답.** $L=\begin{bmatrix}1&0\\3&1\end{bmatrix}$, $U=\begin{bmatrix}2&3\\0&-2\end{bmatrix}$입니다.
> **풀이.** $R_2-3R_1$로 둘째 행이 $(0,7-9)=(0,-2)$가 되어 $U=\begin{bmatrix}2&3\\0&-2\end{bmatrix}$입니다. 승수가 3이라 $L$의 $(2,1)$이 3입니다. 검산하면 $LU$의 둘째 행은 $3\cdot(2,3)+(0,-2)=(6,7)$로 맞습니다.

> **문제 8.** (심화) $A=\begin{bmatrix}1&2&1\\2&6&3\\3&10&6\end{bmatrix}$의 LU 분해를 구하십시오.
> **답.** $L=\begin{bmatrix}1&0&0\\2&1&0\\3&2&1\end{bmatrix}$, $U=\begin{bmatrix}1&2&1\\0&2&1\\0&0&1\end{bmatrix}$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,2,1)$, $R_3-3R_1$로 셋째 행 $(0,4,3)$을 얻습니다. 이어 $R_3-2R_2$로 셋째 행이 $(0,0,1)$이 되어 $U$가 완성됩니다. 승수는 $(2,1)=2$, $(3,1)=3$, $(3,2)=2$이라 $L$이 정해집니다. 검산하면 $LU$의 셋째 행은 $3\cdot(1,2,1)+2\cdot(0,2,1)+1\cdot(0,0,1)=(3,10,6)$으로 맞습니다.

> **문제 9.** (심화) 문제 8의 분해를 이용해 $A\mathbf{x}=\begin{bmatrix}4\\11\\19\end{bmatrix}$을 푸십시오.
> **답.** $\mathbf{x}=\begin{bmatrix}1\\1\\1\end{bmatrix}$입니다.
> **풀이.** 먼저 $L\mathbf{y}=\mathbf{b}$를 전진 대입합니다. $y_1=4$, $2y_1+y_2=11$이라 $y_2=3$, $3y_1+2y_2+y_3=19$이라 $y_3=19-12-6=1$입니다. 다음 $U\mathbf{x}=\mathbf{y}$를 후진 대입합니다. $x_3=1$, $2x_2+x_3=3$이라 $x_2=1$, $x_1+2x_2+x_3=4$이라 $x_1=1$입니다. 검산하면 $A\mathbf{x}$의 둘째 성분 $2+6+3=11$로 맞습니다.

> **문제 10.** (심화) 가역행렬 $A,B$에 대해 $A^{-1}=\begin{bmatrix}1&0\\1&1\end{bmatrix}$, $B^{-1}=\begin{bmatrix}2&1\\0&1\end{bmatrix}$일 때 $(AB)^{-1}$을 구하십시오.
> **답.** $(AB)^{-1}=\begin{bmatrix}3&1\\1&1\end{bmatrix}$입니다.
> **풀이.** $(AB)^{-1}=B^{-1}A^{-1}=\begin{bmatrix}2&1\\0&1\end{bmatrix}\begin{bmatrix}1&0\\1&1\end{bmatrix}$입니다. $(1,1)=2\cdot1+1\cdot1=3$, $(1,2)=2\cdot0+1\cdot1=1$, $(2,1)=0\cdot1+1\cdot1=1$, $(2,2)=0\cdot0+1\cdot1=1$이라 $\begin{bmatrix}3&1\\1&1\end{bmatrix}$입니다. 순서를 뒤집어 곱해야 함에 유의합니다.

> **문제 11.** (심화) 정사각행렬 $A$가 $A^{2}-3A+2I=O$을 만족하면 $A$가 가역이고 $A^{-1}=\tfrac12(3I-A)$임을 보이십시오.
> **답.** $A(3I-A)=2I$에서 곧바로 나옵니다.
> **풀이.** $A^{2}-3A+2I=O$을 옮기면 $2I=3A-A^{2}=A(3I-A)$입니다. 양변을 2로 나누면 $A\cdot\tfrac12(3I-A)=I$이고, 같은 계산으로 $\tfrac12(3I-A)\cdot A=I$입니다. 곱이 단위행렬이 되는 행렬이 존재하므로 $A$는 가역이고 그 역행렬이 $\tfrac12(3I-A)$입니다.

> **문제 12.** (표준) $A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$에 대해 $(A^{-1})^{T}=(A^{T})^{-1}$임을 확인하십시오.
> **답.** 양변 모두 $\begin{bmatrix}1&0\\-2&1\end{bmatrix}$입니다.
> **풀이.** $\det A=1$이라 $A^{-1}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}$이고 $(A^{-1})^{T}=\begin{bmatrix}1&0\\-2&1\end{bmatrix}$입니다. 한편 $A^{T}=\begin{bmatrix}1&0\\2&1\end{bmatrix}$이라 $(A^{T})^{-1}=\begin{bmatrix}1&0\\-2&1\end{bmatrix}$로 같습니다.

## 4. 행렬식

> **문제 1.** (기초) 사뤼스 규칙으로 $\det\begin{bmatrix}2&1&1\\1&3&2\\1&0&2\end{bmatrix}$을 구하십시오.
> **답.** $9$입니다.
> **풀이.** $aei+bfg+cdh-ceg-bdi-afh$에 $a=2,b=1,c=1,d=1,e=3,f=2,g=1,h=0,i=2$를 대입하면 $2\cdot3\cdot2+1\cdot2\cdot1+1\cdot1\cdot0-1\cdot3\cdot1-1\cdot1\cdot2-2\cdot2\cdot0=12+2+0-3-2-0=9$입니다.

> **문제 2.** (기초) $\det\begin{bmatrix}3&2&1\\0&-1&4\\0&0&2\end{bmatrix}$을 구하십시오.
> **답.** $-6$입니다.
> **풀이.** 상삼각행렬이라 대각의 곱 $3\cdot(-1)\cdot2=-6$입니다.

> **문제 3.** (표준) $\det\begin{bmatrix}1&0&3\\2&1&4\\5&0&6\end{bmatrix}$을 둘째 열로 여인수 전개하십시오.
> **답.** $-9$입니다.
> **풀이.** 둘째 열은 $0,1,0$이라 가운데 항만 남습니다. $\det=1\cdot(-1)^{2+2}\det\begin{bmatrix}1&3\\5&6\end{bmatrix}=1\cdot(6-15)=-9$입니다.

> **문제 4.** (표준) 행 소거로 $\det\begin{bmatrix}1&2&-1\\2&3&1\\1&1&4\end{bmatrix}$을 구하십시오.
> **답.** $-2$입니다.
> **풀이.** $R_2-2R_1$, $R_3-R_1$은 행렬식을 바꾸지 않습니다. 결과는 $\begin{bmatrix}1&2&-1\\0&-1&3\\0&-1&5\end{bmatrix}$입니다. $R_3-R_2$로 셋째 행이 $(0,0,2)$가 됩니다. 상삼각의 대각 곱은 $1\cdot(-1)\cdot2=-2$이고, 부호를 바꾸는 연산을 쓰지 않았으므로 $\det=-2$입니다. 사뤼스로 검산하면 $12+2-2+3-16-1=-2$로 일치합니다.

> **문제 5.** (표준) $\det\begin{bmatrix}2&1&0&0\\0&3&0&0\\5&1&1&2\\0&0&0&4\end{bmatrix}$을 구하십시오.
> **답.** $24$입니다.
> **풀이.** 넷째 행 $(0,0,0,4)$로 전개하면 $4\cdot(-1)^{4+4}\det\begin{bmatrix}2&1&0\\0&3&0\\5&1&1\end{bmatrix}$입니다. 이 $3\times3$을 셋째 열 $(0,0,1)$로 전개하면 $1\cdot\det\begin{bmatrix}2&1\\0&3\end{bmatrix}=6$입니다. 따라서 $4\cdot6=24$입니다.

> **문제 6.** (표준) $A$가 $3\times3$이고 $\det A=4$일 때 $\det(2A)$, $\det(A^{-1})$, $\det(A^{T}A)$를 각각 구하십시오.
> **답.** $\det(2A)=32$, $\det(A^{-1})=\tfrac14$, $\det(A^{T}A)=16$입니다.
> **풀이.** $2A$는 세 행에 각각 2를 곱한 것이라 $\det(2A)=2^{3}\det A=8\cdot4=32$입니다. $\det(A^{-1})=\dfrac{1}{\det A}=\tfrac14$입니다. 곱셈성과 전치 불변으로 $\det(A^{T}A)=\det(A^{T})\det A=(\det A)^{2}=16$입니다.

> **문제 7.** (표준) $\det\begin{bmatrix}1&2&0&0\\3&4&0&0\\0&0&2&1\\0&0&5&3\end{bmatrix}$을 구하십시오.
> **답.** $-2$입니다.
> **풀이.** 블록 대각행렬이라 두 대각 블록의 행렬식을 곱합니다. $\det\begin{bmatrix}1&2\\3&4\end{bmatrix}=4-6=-2$, $\det\begin{bmatrix}2&1\\5&3\end{bmatrix}=6-5=1$이라 곱은 $(-2)\cdot1=-2$입니다.

> **문제 8.** (표준) 크라메르 공식으로 $\begin{cases}2x+3y=8\\x-y=-1\end{cases}$을 푸십시오.
> **답.** $x=1$, $y=2$입니다.
> **풀이.** $A=\begin{bmatrix}2&3\\1&-1\end{bmatrix}$, $\det A=-2-3=-5$입니다. $\det A_1=\det\begin{bmatrix}8&3\\-1&-1\end{bmatrix}=-8+3=-5$이라 $x=\tfrac{-5}{-5}=1$입니다. $\det A_2=\det\begin{bmatrix}2&8\\1&-1\end{bmatrix}=-2-8=-10$이라 $y=\tfrac{-10}{-5}=2$입니다.

> **문제 9.** (심화) 크라메르 공식으로 $\begin{cases}x+y+z=2\\2x-y+z=-1\\x+2y-z=6\end{cases}$을 푸십시오.
> **답.** $x=1$, $y=2$, $z=-1$입니다.
> **풀이.** $A=\begin{bmatrix}1&1&1\\2&-1&1\\1&2&-1\end{bmatrix}$입니다. 첫째 행 전개로 $\det A=1(1-2)-1(-2-1)+1(4+1)=-1+3+5=7$입니다. $A_1$은 첫 열을 $\mathbf{b}=(2,-1,6)$으로 바꾼 것이라 $\det A_1=2(1-2)-1(1-6)+1(-2+6)=-2+5+4=7$이라 $x=\tfrac77=1$입니다. $A_2$는 둘째 열을 바꿔 $\det A_2=1(1-6)-2(-2-1)+1(12+1)=-5+6+13=14$이라 $y=\tfrac{14}{7}=2$입니다. $A_3$은 셋째 열을 바꿔 $\det A_3=1(-6+2)-1(12+1)+2(4+1)=-4-13+10=-7$이라 $z=\tfrac{-7}{7}=-1$입니다.

> **문제 10.** (심화) $A,B$가 $3\times3$이고 $\det A=2$, $\det B=-3$일 때 $\det(A^{2}B^{-1})$과 $\det(2A^{-1})$을 구하십시오.
> **답.** $\det(A^{2}B^{-1})=-\tfrac43$, $\det(2A^{-1})=4$입니다.
> **풀이.** 곱셈성으로 $\det(A^{2}B^{-1})=(\det A)^{2}\cdot\dfrac{1}{\det B}=4\cdot\left(-\tfrac13\right)=-\tfrac43$입니다. $\det(2A^{-1})=2^{3}\cdot\dfrac{1}{\det A}=8\cdot\tfrac12=4$입니다.

> **문제 11.** (심화) 딸림행렬로 $A=\begin{bmatrix}1&2&3\\0&1&4\\5&6&0\end{bmatrix}$의 역행렬을 구하십시오.
> **답.** $A^{-1}=\begin{bmatrix}-24&18&5\\20&-15&-4\\-5&4&1\end{bmatrix}$입니다.
> **풀이.** 첫째 행 전개로 $\det A=1(1\cdot0-4\cdot6)-2(0\cdot0-4\cdot5)+3(0\cdot6-1\cdot5)=-24+40-15=1$입니다. 여인수를 계산하면 $C_{11}=-24,\ C_{12}=20,\ C_{13}=-5$, $C_{21}=18,\ C_{22}=-15,\ C_{23}=4$, $C_{31}=5,\ C_{32}=-4,\ C_{33}=1$입니다. 이를 전치해 딸림행렬 $\operatorname{adj}A=\begin{bmatrix}-24&18&5\\20&-15&-4\\-5&4&1\end{bmatrix}$을 얻습니다. $\det A=1$이라 $A^{-1}=\operatorname{adj}A$입니다. 검산하면 $A$의 첫째 행과 $A^{-1}$의 첫째 열의 내적이 $1\cdot(-24)+2\cdot20+3\cdot(-5)=1$입니다.

> **문제 12.** (심화) $\det\begin{bmatrix}x&1&1\\1&x&1\\1&1&x\end{bmatrix}=0$이 되는 $x$를 모두 구하십시오.
> **답.** $x=1$ 또는 $x=-2$입니다.
> **풀이.** 사뤼스로 전개하면 $\det=x^{3}+1+1-x-x-x=x^{3}-3x+2$입니다. 인수분해하면 $x^{3}-3x+2=(x-1)(x^{2}+x-2)=(x-1)(x-1)(x+2)=(x-1)^{2}(x+2)$입니다. 이 값이 0이 되는 $x$는 $x=1$(중근)과 $x=-2$입니다. 실제로 $x=1$이면 세 행이 모두 같아 종속이고, $x=-2$이면 세 행의 합이 영행이 됩니다.

> **문제 13.** (심화) $3\times3$ 반대칭행렬 $A$($A^{T}=-A$)의 행렬식이 0임을 보이십시오.
> **답.** $\det A=-\det A$가 되어 $\det A=0$입니다.
> **풀이.** 전치 불변으로 $\det A=\det(A^{T})$입니다. 반대칭이라 $A^{T}=-A$이므로 $\det(A^{T})=\det(-A)$입니다. $-A$는 세 행 각각에 $-1$을 곱한 것이라 $\det(-A)=(-1)^{3}\det A=-\det A$입니다. 따라서 $\det A=-\det A$, 즉 $2\det A=0$이라 $\det A=0$입니다. 홀수 차수 반대칭행렬은 항상 특이행렬입니다.
