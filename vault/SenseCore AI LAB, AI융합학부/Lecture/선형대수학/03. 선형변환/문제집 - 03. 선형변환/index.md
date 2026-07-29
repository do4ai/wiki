---
title: "문제집 - 03. 선형변환"
---
# 문제집 - 03. 선형변환

이 문제집은 3단원 세 강의(선형변환과 표현행렬 / 상공간·영공간·계수정리 / 기저변환)의 내용을 본문보다 한 단계 어렵게 훈련하기 위한 것입니다. 선형성 판정, 표현행렬 구성, 계수정리 응용, 기저변환행렬과 닮음을 집중적으로 다룹니다. 각 문제는 난이도(기초·표준·심화)를 표시했고, 답과 단계별 풀이를 함께 실었습니다. 손으로 풀 때는 답을 가리고 풀이의 중간식을 스스로 재현해 보시기 바랍니다. 행렬 곱과 표현행렬은 반드시 다시 전개해 검산하시기 바랍니다.

## 1. 선형변환과 표현행렬

> **문제 1.** (기초) $T(x,y)=(2x-y,\ 3x+y)$의 표준행렬을 구하십시오.
> **답.** $\begin{bmatrix}2&-1\\3&1\end{bmatrix}$입니다.
> **풀이.** $T(1,0)=(2,3)$이 첫째 열, $T(0,1)=(-1,1)$이 둘째 열입니다.

> **문제 2.** (기초) $T(x,y)=(x^{2}+y,\ x)$가 선형인지 판정하십시오.
> **답.** 선형이 아닙니다.
> **풀이.** 스칼라배를 봅니다. $T(c\mathbf{u})$의 첫 성분은 $(cx)^{2}+cy=c^{2}x^{2}+cy$인데 $cT(\mathbf{u})$의 첫 성분은 $c(x^{2}+y)=cx^{2}+cy$입니다. $c=2,x=1,y=0$이면 $4\ne2$라 어긋납니다. 제곱항 때문에 비선형입니다.

> **문제 3.** (기초) $T(x,y,z)=(x+2y,\ 3z)$의 표준행렬을 구하십시오.
> **답.** $\begin{bmatrix}1&2&0\\0&0&3\end{bmatrix}$입니다.
> **풀이.** $T(1,0,0)=(1,0)$, $T(0,1,0)=(2,0)$, $T(0,0,1)=(0,3)$을 열로 세웁니다. 크기는 $2\times3$입니다.

> **문제 4.** (표준) $T(x,y)=(|x|,\ y)$가 선형인지 판정하십시오.
> **답.** 선형이 아닙니다.
> **풀이.** 스칼라배 보존이 깨집니다. $c=-1$, $\mathbf{u}=(1,0)$이면 $T(-1,0)=(|-1|,0)=(1,0)$이지만 $-T(1,0)=-(1,0)=(-1,0)$입니다. 두 결과가 다르므로 비선형입니다. 절댓값이 음의 스칼라에서 어긋나기 때문입니다.

> **문제 5.** (표준) 선형변환 $T$가 $T(1,1)=(4,2)$, $T(1,-1)=(0,4)$일 때 표준행렬을 구하십시오.
> **답.** $\begin{bmatrix}2&2\\3&-1\end{bmatrix}$입니다.
> **풀이.** $(1,0)=\tfrac12(1,1)+\tfrac12(1,-1)$이라 $T(1,0)=\tfrac12(4,2)+\tfrac12(0,4)=(2,3)$입니다. $(0,1)=\tfrac12(1,1)-\tfrac12(1,-1)$이라 $T(0,1)=\tfrac12(4,2)-\tfrac12(0,4)=(2,-1)$입니다. 두 상을 열로 세우면 $\begin{bmatrix}2&2\\3&-1\end{bmatrix}$입니다.

> **문제 6.** (표준) 직선 $y=x$에 대한 대칭의 표준행렬을 구하고 $(3,5)$의 상을 구하십시오.
> **답.** $\begin{bmatrix}0&1\\1&0\end{bmatrix}$이고 상은 $(5,3)$입니다.
> **풀이.** $y=x$ 대칭은 좌표를 맞바꾸므로 $(1,0)\mapsto(0,1)$, $(0,1)\mapsto(1,0)$입니다. 행렬은 $\begin{bmatrix}0&1\\1&0\end{bmatrix}$이고 $(3,5)$의 상은 $(5,3)$입니다.

> **문제 7.** (표준) $y=x$ 대칭 $T$ 다음에 $90^\circ$ 회전 $S$를 하는 합성 $S\circ T$의 표현행렬을 구하십시오.
> **답.** $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$입니다.
> **풀이.** $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$, $B=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$입니다. $S\circ T$의 행렬은 $BA$입니다. $(1,1)=0\cdot0+(-1)\cdot1=-1$, $(1,2)=0\cdot1+(-1)\cdot0=0$, $(2,1)=1\cdot0+0\cdot1=0$, $(2,2)=1\cdot1+0\cdot0=1$이라 $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$입니다. 이는 $y$축 대칭입니다.

> **문제 8.** (표준) $T(x,y)=(x+2y,\ 3x+4y)$일 때 $T\circ T$의 표준행렬을 구하십시오.
> **답.** $\begin{bmatrix}7&10\\15&22\end{bmatrix}$입니다.
> **풀이.** $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$이고 합성의 행렬은 $A^{2}$입니다. $(1,1)=1\cdot1+2\cdot3=7$, $(1,2)=1\cdot2+2\cdot4=10$, $(2,1)=3\cdot1+4\cdot3=15$, $(2,2)=3\cdot2+4\cdot4=22$입니다.

> **문제 9.** (표준) 행렬 전치 사상 $T\!\left(\begin{bmatrix}a&b\\c&d\end{bmatrix}\right)=\begin{bmatrix}a&c\\b&d\end{bmatrix}$가 선형임을 보이십시오.
> **답.** $(X+Y)^{T}=X^{T}+Y^{T}$, $(cX)^{T}=cX^{T}$이므로 선형입니다.
> **풀이.** 전치는 성분을 자리만 바꿔 옮기는 사상입니다. 두 행렬의 합의 전치는 각 전치의 합이고, 스칼라배의 전치는 전치의 스칼라배입니다. 두 조건을 모두 만족하므로 $2\times2$ 행렬 공간 위의 선형변환입니다.

> **문제 10.** (표준) 선형변환 $T:\mathbb{R}^3\to\mathbb{R}^2$가 $T(\mathbf{e}_1)=(1,0)$, $T(\mathbf{e}_2)=(1,1)$, $T(\mathbf{e}_3)=(0,1)$일 때 $T(2,-1,3)$을 구하십시오.
> **답.** $(1,2)$입니다.
> **풀이.** $T(2,-1,3)=2T(\mathbf{e}_1)-T(\mathbf{e}_2)+3T(\mathbf{e}_3)=2(1,0)-(1,1)+3(0,1)=(2-1,\ -1+3)=(1,2)$입니다.

> **문제 11.** (표준) $T(x,y)=(2x,\ x+y)$이고 기저 $B=\{(1,0),(1,1)\}$일 때 $[T]_B$를 구하십시오(정의역·공역 모두 $B$).
> **답.** $\begin{bmatrix}1&0\\1&2\end{bmatrix}$입니다.
> **풀이.** $T(1,0)=(2,1)$을 $B$로 나타내면 $a(1,0)+b(1,1)=(2,1)$에서 $b=1,a=1$이라 $(1,1)$이 첫째 열입니다. $T(1,1)=(2,2)$는 $a(1,0)+b(1,1)=(2,2)$에서 $b=2,a=0$이라 $(0,2)$가 둘째 열입니다. 따라서 $\begin{bmatrix}1&0\\1&2\end{bmatrix}$입니다.

> **문제 12.** (심화) $45^\circ$ 회전을 두 번 합성하면 $90^\circ$ 회전이 됨을 표준행렬 곱으로 보이십시오.
> **답.** $A^{2}=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$로 $90^\circ$ 회전입니다.
> **풀이.** $A=\begin{bmatrix}\tfrac{\sqrt2}{2}&-\tfrac{\sqrt2}{2}\\[2pt]\tfrac{\sqrt2}{2}&\tfrac{\sqrt2}{2}\end{bmatrix}$입니다. $A^{2}$의 $(1,1)=\tfrac12-\tfrac12=0$, $(1,2)=-\tfrac12-\tfrac12=-1$, $(2,1)=\tfrac12+\tfrac12=1$, $(2,2)=-\tfrac12+\tfrac12=0$이라 $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$입니다. 각이 더해져 $90^\circ$ 회전이 됩니다.

> **문제 13.** (심화) 선형변환 $T:\mathbb{R}^2\to\mathbb{R}^2$가 $T(2,1)=(1,0)$, $T(1,1)=(0,1)$일 때 표준행렬을 구하십시오.
> **답.** $\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$입니다.
> **풀이.** $\mathbf{e}_1,\mathbf{e}_2$를 두 벡터로 나타냅니다. $(1,0)=(2,1)-(1,1)$이라 $T(1,0)=T(2,1)-T(1,1)=(1,0)-(0,1)=(1,-1)$입니다. $(0,1)=2(1,1)-(2,1)$이라 $T(0,1)=2(0,1)-(1,0)=(-1,2)$입니다. 두 상을 열로 세우면 $\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$입니다. 검산하면 $A(2,1)=(2-1,-2+2)=(1,0)$입니다.

> **문제 14.** (심화) $x$축 위로의 정사영 $P$와 $y$축 위로의 정사영 $Q$에 대해 $P+Q=I$이지만 $PQ=O$임을 표준행렬로 확인하십시오.
> **답.** $P+Q=\begin{bmatrix}1&0\\0&1\end{bmatrix}$, $PQ=\begin{bmatrix}0&0\\0&0\end{bmatrix}$입니다.
> **풀이.** $P=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $Q=\begin{bmatrix}0&0\\0&1\end{bmatrix}$입니다. 합은 대각이 모두 1인 $I$입니다. 곱 $PQ$의 $(1,1)=1\cdot0+0\cdot0=0$이고 모든 성분이 0이라 $O$입니다. 두 축이 서로 수직이라 한 축에 정사영한 뒤 다른 축에 정사영하면 원점만 남습니다.

> **문제 15.** (심화) 선형변환 $T$가 $T\circ T=T$(멱등)이고 표준행렬이 $A=\begin{bmatrix}a&b\\0&0\end{bmatrix}$ 꼴이면 $a=1$ 또는 $a=0$임을 보이십시오.
> **답.** $A^{2}=A$에서 $a^{2}=a$이라 $a=0$ 또는 $a=1$입니다.
> **풀이.** $A^{2}$의 $(1,1)=a\cdot a+b\cdot0=a^{2}$, $(1,2)=a\cdot b+b\cdot0=ab$이고 둘째 행은 0입니다. $A^{2}=A$이려면 $a^{2}=a$, $ab=b$가 필요합니다. 첫 식에서 $a(a-1)=0$이라 $a=0$ 또는 $a=1$입니다. 멱등변환의 대각 성분은 0 또는 1이라는 일반 성질의 한 예입니다.

## 2. 상공간·영공간·계수정리

> **문제 1.** (기초) $A=\begin{bmatrix}1&3\\2&6\end{bmatrix}$의 계수와 nullity를 구하십시오.
> **답.** $\operatorname{rank}=1$, $\operatorname{nullity}=1$입니다.
> **풀이.** 둘째 열이 첫째 열의 3배라 종속이라 계수는 1입니다. 열이 2개이므로 nullity는 $2-1=1$입니다.

> **문제 2.** (기초) $A=\begin{bmatrix}1&0&2\\0&1&-1\end{bmatrix}$의 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}-2\\1\\1\end{bmatrix}\right\}$입니다.
> **풀이.** 기약 사다리꼴이라 $x+2z=0$, $y-z=0$입니다. $z=t$로 두면 $x=-2t$, $y=t$라 해는 $t(-2,1,1)$입니다. 검산하면 첫 행 $-2+2=0$, 둘째 행 $1-1=0$입니다.

> **문제 3.** (표준) $A=\begin{bmatrix}1&2&3\\2&4&6\\3&6&9\end{bmatrix}$의 상공간과 영공간의 차원을 구하십시오.
> **답.** 상공간 차원 1, 영공간 차원 2입니다.
> **풀이.** 둘째·셋째 행이 첫째 행의 배수라 계수는 1입니다. 열도 종속으로 $(1,2,3)$ 하나만 독립이라 상공간은 직선입니다. 계수정리로 $\operatorname{nullity}=3-1=2$입니다.

> **문제 4.** (표준) $A=\begin{bmatrix}1&1&2\\2&3&5\\1&2&3\end{bmatrix}$의 계수와 nullity를 구하십시오.
> **답.** $\operatorname{rank}=2$, $\operatorname{nullity}=1$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,1,1)$, $R_3-R_1$로 셋째 행 $(0,1,1)$을 얻습니다. $R_3-R_2$로 셋째 행이 $(0,0,0)$이 됩니다. 피벗 두 개라 계수 2, nullity는 $3-2=1$입니다.

> **문제 5.** (표준) 문제 4의 $A$에 대해 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}$입니다.
> **풀이.** 소거 후 $x+y+2z=0$, $y+z=0$입니다. 둘째에서 $y=-z$, 첫째에 넣으면 $x=-y-2z=z-2z=-z$입니다. $z=t$로 두면 해는 $t(-1,-1,1)$입니다. 검산하면 첫 식 $-1-1+2=0$, 둘째 식 $-1+1=0$입니다.

> **문제 6.** (표준) $A=\begin{bmatrix}1&2&1\\0&1&1\\1&1&0\end{bmatrix}$의 상공간의 기저를 원래 열로 제시하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}1\\0\\1\end{bmatrix},\ \begin{bmatrix}2\\1\\1\end{bmatrix}\right\}$입니다.
> **풀이.** $R_3-R_1$로 셋째 행 $(0,-1,-1)$, 이어 $R_3+R_2$로 $(0,0,0)$이 됩니다. 피벗은 첫째·둘째 열에 있으므로 원래 행렬의 첫째 열 $(1,0,1)$과 둘째 열 $(2,1,1)$이 기저입니다. 셋째 열 $(1,1,0)$은 두 열의 결합입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&0\\2&1\\0&1\\1&1\end{bmatrix}$로 정의된 $T:\mathbb{R}^2\to\mathbb{R}^4$의 단사·전사를 판정하십시오.
> **답.** 단사이고 전사가 아닙니다.
> **풀이.** 두 열이 독립이라($(1,2,0,1)$과 $(0,1,1,1)$은 배수 관계가 아님) $\operatorname{rank}=2=n$이라 $\operatorname{nullity}=0$이므로 단사입니다. 그러나 $\operatorname{rank}=2<4=m$이라 상공간이 $\mathbb{R}^4$ 전체가 아니어서 전사가 아닙니다.

> **문제 8.** (표준) 매개변수 $a$에 대해 $A=\begin{bmatrix}1&2\\2&a\end{bmatrix}$의 계수가 1이 되도록 하는 $a$를 구하십시오.
> **답.** $a=4$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행이 $(0,a-4)$가 됩니다. 계수가 1이려면 이 행이 영행이어야 하므로 $a-4=0$, 즉 $a=4$입니다. 이때 둘째 열이 첫째 열의 2배라 종속입니다.

> **문제 9.** (표준) $T:\mathbb{R}^4\to\mathbb{R}^3$이 전사일 때 $\ker(T)$의 차원을 구하십시오.
> **답.** 차원은 1입니다.
> **풀이.** 전사이면 $\operatorname{rank}=m=3$입니다. 정의역 차원 $n=4$이라 계수정리로 $\operatorname{nullity}=4-3=1$입니다.

> **문제 10.** (표준) $A=\begin{bmatrix}1&1&0&2\\2&2&1&5\\1&1&1&3\end{bmatrix}$의 계수와 nullity를 구하십시오.
> **답.** $\operatorname{rank}=2$, $\operatorname{nullity}=2$입니다.
> **풀이.** $R_2-2R_1$로 둘째 행 $(0,0,1,1)$, $R_3-R_1$로 셋째 행 $(0,0,1,1)$을 얻습니다. $R_3-R_2$로 셋째 행이 $(0,0,0,0)$이 됩니다. 피벗은 첫째 열과 셋째 열이라 계수 2, nullity는 $4-2=2$입니다.

> **문제 11.** (심화) 문제 10의 $A$에 대해 영공간의 기저를 구하십시오.
> **답.** 기저는 $\left\{\begin{bmatrix}-1\\1\\0\\0\end{bmatrix},\ \begin{bmatrix}-2\\0\\-1\\1\end{bmatrix}\right\}$입니다.
> **풀이.** 피벗 열은 첫째·셋째, 자유변수는 $x_2,x_4$입니다. 방정식은 $x_1+x_2+2x_4=0$, $x_3+x_4=0$입니다. $x_2=1,x_4=0$이면 $x_1=-1,x_3=0$이라 $(-1,1,0,0)$, $x_2=0,x_4=1$이면 $x_3=-1$, $x_1=-2$라 $(-2,0,-1,1)$입니다.

> **문제 12.** (심화) $A$가 $3\times3$이고 $A\begin{bmatrix}1\\1\\1\end{bmatrix}=\mathbf{0}$을 만족하면 $\operatorname{rank}(A)\le2$임을 설명하십시오.
> **답.** 영공간이 자명하지 않아 $\operatorname{nullity}\ge1$이기 때문입니다.
> **풀이.** $(1,1,1)\ne\mathbf{0}$이 영공간에 속하므로 $\operatorname{nullity}(A)\ge1$입니다. 계수정리로 $\operatorname{rank}(A)=3-\operatorname{nullity}(A)\le3-1=2$입니다. 세 열의 합이 영벡터라 열이 종속임을 뜻합니다.

> **문제 13.** (심화) $A=\begin{bmatrix}1&1\\1&1\end{bmatrix}$, $B=\begin{bmatrix}1&1\\-1&-1\end{bmatrix}$일 때 $\operatorname{rank}(AB)$가 $\min(\operatorname{rank}A,\operatorname{rank}B)$보다 작을 수 있음을 보이십시오.
> **답.** $AB=O$이라 $\operatorname{rank}(AB)=0<1$입니다.
> **풀이.** $\operatorname{rank}A=\operatorname{rank}B=1$이라 최솟값은 1입니다. $AB$의 $(1,1)=1\cdot1+1\cdot(-1)=0$, $(1,2)=1\cdot1+1\cdot(-1)=0$이고 둘째 행도 같은 계산으로 0이라 $AB=O$입니다. 따라서 $\operatorname{rank}(AB)=0$으로, 곱의 계수는 각 계수보다 작아질 수 있습니다.

> **문제 14.** (심화) $A$가 $m\times n$이고 열이 일차독립이면 $A^{T}A$가 가역임을 계수로 설명하십시오.
> **답.** $A^{T}A$가 $n\times n$이고 계수가 $n$이라 가역입니다.
> **풀이.** 열이 독립이면 $A\mathbf{x}=\mathbf{0}$의 해는 $\mathbf{x}=\mathbf{0}$뿐입니다. $A^{T}A\mathbf{x}=\mathbf{0}$이면 $\mathbf{x}^{T}A^{T}A\mathbf{x}=\|A\mathbf{x}\|^{2}=0$이라 $A\mathbf{x}=\mathbf{0}$, 곧 $\mathbf{x}=\mathbf{0}$입니다. 따라서 $A^{T}A$의 영공간이 자명해 $\operatorname{rank}(A^{T}A)=n$이고 $n\times n$ full rank이므로 가역입니다.

> **문제 15.** (심화) $T:\mathbb{R}^n\to\mathbb{R}^n$이 단사이면 전사임을, 계수정리로 보이십시오.
> **답.** $\operatorname{nullity}=0\Rightarrow\operatorname{rank}=n=m$이라 전사입니다.
> **풀이.** 단사는 $\ker(T)=\{\mathbf{0}\}$, 곧 $\operatorname{nullity}=0$과 같습니다. 계수정리로 $\operatorname{rank}=n-0=n$입니다. 공역이 $\mathbb{R}^n$이라 $\operatorname{rank}=n=m$이 전사입니다. 유한차원에서 같은 차원 사이의 선형변환은 단사와 전사가 동치입니다.

## 3. 기저변환

> **문제 1.** (기초) $B=\{(1,0),(2,1)\}$의 전이행렬 $P_B$와 그 역행렬을 구하십시오.
> **답.** $P_B=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $P_B^{-1}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}$입니다.
> **풀이.** 기저벡터를 열로 세우면 $P_B=\begin{bmatrix}1&2\\0&1\end{bmatrix}$입니다. $\det=1$이라 $P_B^{-1}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}$입니다. 검산하면 $P_BP_B^{-1}=I$입니다.

> **문제 2.** (기초) $B=\{(1,0),(2,1)\}$에서 $\mathbf{v}=(5,2)$의 좌표벡터를 구하십시오.
> **답.** $[\mathbf{v}]_B=\begin{bmatrix}1\\2\end{bmatrix}$입니다.
> **풀이.** $[\mathbf{v}]_B=P_B^{-1}\mathbf{v}=\begin{bmatrix}1&-2\\0&1\end{bmatrix}\begin{bmatrix}5\\2\end{bmatrix}=\begin{bmatrix}5-4\\2\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}$입니다. 검산하면 $1(1,0)+2(2,1)=(5,2)$입니다.

> **문제 3.** (기초) $A=\begin{bmatrix}5&1\\2&4\end{bmatrix}$와 닮은 행렬의 대각합과 행렬식을 구하십시오.
> **답.** 대각합 9, 행렬식 18입니다.
> **풀이.** 닮음은 대각합과 행렬식을 보존합니다. $\operatorname{tr}A=5+4=9$, $\det A=5\cdot4-1\cdot2=18$입니다.

> **문제 4.** (표준) $B=\{(1,2),(2,3)\}$로 $\mathbf{v}=(0,1)$의 좌표벡터를 구하십시오.
> **답.** $[\mathbf{v}]_B=\begin{bmatrix}2\\-1\end{bmatrix}$입니다.
> **풀이.** $P_B=\begin{bmatrix}1&2\\2&3\end{bmatrix}$, $\det=3-4=-1$이라 $P_B^{-1}=\tfrac{1}{-1}\begin{bmatrix}3&-2\\-2&1\end{bmatrix}=\begin{bmatrix}-3&2\\2&-1\end{bmatrix}$입니다. $[\mathbf{v}]_B=\begin{bmatrix}-3&2\\2&-1\end{bmatrix}\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}2\\-1\end{bmatrix}$입니다. 검산하면 $2(1,2)-1(2,3)=(0,1)$입니다.

> **문제 5.** (표준) $A=\begin{bmatrix}4&0\\0&1\end{bmatrix}$, $P=\begin{bmatrix}1&1\\0&1\end{bmatrix}$일 때 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}4&3\\0&1\end{bmatrix}$입니다.
> **풀이.** $P^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. $AP=\begin{bmatrix}4&0\\0&1\end{bmatrix}\begin{bmatrix}1&1\\0&1\end{bmatrix}=\begin{bmatrix}4&4\\0&1\end{bmatrix}$입니다. $P^{-1}(AP)$의 $(1,1)=4$, $(1,2)=1\cdot4+(-1)\cdot1=3$, $(2,1)=0$, $(2,2)=1$이라 $\begin{bmatrix}4&3\\0&1\end{bmatrix}$입니다. 대각합 5, 행렬식 4가 $A$와 일치합니다.

> **문제 6.** (표준) $B=\{(1,1),(1,2)\}$, $C=\{(1,0),(0,1)\}$(표준)일 때 $\mathbf{x}$의 $B$좌표가 $\begin{bmatrix}3\\-1\end{bmatrix}$이면 표준좌표를 구하십시오.
> **답.** $\begin{bmatrix}2\\1\end{bmatrix}$입니다.
> **풀이.** $P_{C\leftarrow B}=P_B=\begin{bmatrix}1&1\\1&2\end{bmatrix}$입니다. $[\mathbf{x}]_C=P_B[\mathbf{x}]_B=\begin{bmatrix}1&1\\1&2\end{bmatrix}\begin{bmatrix}3\\-1\end{bmatrix}=\begin{bmatrix}3-1\\3-2\end{bmatrix}=\begin{bmatrix}2\\1\end{bmatrix}$입니다.

> **문제 7.** (표준) $\begin{bmatrix}2&1\\0&3\end{bmatrix}$과 $\begin{bmatrix}1&5\\0&4\end{bmatrix}$이 닮을 수 없는 이유를 말하십시오.
> **답.** 행렬식이 각각 6과 4로 달라 닮을 수 없습니다.
> **풀이.** 닮은 행렬은 행렬식이 같아야 합니다. 앞은 $2\cdot3-1\cdot0=6$, 뒤는 $1\cdot4-5\cdot0=4$로 다릅니다. 대각합은 둘 다 5로 같지만 행렬식이 달라 닮음이 성립하지 않습니다.

> **문제 8.** (표준) $A=\begin{bmatrix}3&1\\1&3\end{bmatrix}$를 $P=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$로 $P^{-1}AP$를 구하고 대각화됨을 확인하십시오.
> **답.** $\begin{bmatrix}4&0\\0&2\end{bmatrix}$입니다.
> **풀이.** $\det P=-2$이라 $P^{-1}=\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}$입니다. $AP=\begin{bmatrix}3&1\\1&3\end{bmatrix}\begin{bmatrix}1&1\\1&-1\end{bmatrix}=\begin{bmatrix}4&2\\4&-2\end{bmatrix}$입니다(첫째 열 $A(1,1)=(4,4)$, 둘째 열 $A(1,-1)=(2,-2)$). $P^{-1}(AP)$의 $(1,1)=\tfrac12\cdot4+\tfrac12\cdot4=4$, $(1,2)=\tfrac12\cdot2+\tfrac12\cdot(-2)=0$, $(2,1)=\tfrac12\cdot4-\tfrac12\cdot4=0$, $(2,2)=\tfrac12\cdot2-\tfrac12\cdot(-2)=2$이라 $\begin{bmatrix}4&0\\0&2\end{bmatrix}$입니다. 대각 성분 $4,2$가 고유값입니다.

> **문제 9.** (심화) $B=\{(1,1),(2,1)\}$에서 $C=\{(1,0),(1,1)\}$로의 전이행렬 $P_{C\leftarrow B}$를 구하십시오.
> **답.** $\begin{bmatrix}0&1\\1&1\end{bmatrix}$입니다.
> **풀이.** $P_B=\begin{bmatrix}1&2\\1&1\end{bmatrix}$, $P_C=\begin{bmatrix}1&1\\0&1\end{bmatrix}$, $P_C^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix}$입니다. $P_{C\leftarrow B}=P_C^{-1}P_B=\begin{bmatrix}1&-1\\0&1\end{bmatrix}\begin{bmatrix}1&2\\1&1\end{bmatrix}$의 $(1,1)=1-1=0$, $(1,2)=2-1=1$, $(2,1)=1$, $(2,2)=1$이라 $\begin{bmatrix}0&1\\1&1\end{bmatrix}$입니다. 검산하면 $\mathbf{b}_1=(1,1)$의 $C$좌표는 $a(1,0)+b(1,1)=(1,1)$에서 $b=1,a=0$이라 $(0,1)$로 첫째 열과 일치합니다.

> **문제 10.** (심화) $A=\begin{bmatrix}2&1\\0&2\end{bmatrix}$가 대각화될 수 없음을 고유공간의 차원으로 설명하십시오.
> **답.** 고유값 2가 중근인데 고유공간의 차원이 1뿐이라 대각화되지 않습니다.
> **풀이.** 특성다항식은 $\det(A-\lambda I)=(2-\lambda)^{2}=0$이라 고유값은 $\lambda=2$(중근)입니다. $A-2I=\begin{bmatrix}0&1\\0&0\end{bmatrix}$의 영공간은 $x_2=0$을 만족하는 $(t,0)$이라 차원이 1입니다. 대각화하려면 독립 고유벡터가 2개 필요한데 1개뿐이라 어떤 기저에서도 대각행렬이 될 수 없습니다.

> **문제 11.** (심화) 닮은 두 행렬 $A,B'=P^{-1}AP$에 대해 임의의 자연수 $k$에서 $B'^{k}=P^{-1}A^{k}P$임을 보이십시오.
> **답.** 가운데 $PP^{-1}=I$가 소거되어 성립합니다.
> **풀이.** $B'^{k}=(P^{-1}AP)(P^{-1}AP)\cdots(P^{-1}AP)$입니다. 인접한 $P$와 $P^{-1}$이 만나 $PP^{-1}=I$로 사라지므로 $B'^{k}=P^{-1}A^{k}P$가 남습니다. 이 성질 덕분에 $A$를 대각행렬 $D$로 닮게 만들면 $A^{k}=PD^{k}P^{-1}$로 거듭제곱을 쉽게 계산할 수 있습니다.

> **문제 12.** (심화) $A=\begin{bmatrix}0&1\\2&1\end{bmatrix}$를 $P=\begin{bmatrix}1&1\\-1&2\end{bmatrix}$로 $P^{-1}AP$를 구하십시오.
> **답.** $\begin{bmatrix}-1&0\\0&2\end{bmatrix}$입니다.
> **풀이.** $\det P=1\cdot2-1\cdot(-1)=3$이라 $P^{-1}=\tfrac13\begin{bmatrix}2&-1\\1&1\end{bmatrix}$입니다. $AP=\begin{bmatrix}0&1\\2&1\end{bmatrix}\begin{bmatrix}1&1\\-1&2\end{bmatrix}=\begin{bmatrix}-1&2\\1&4\end{bmatrix}$입니다(첫째 열 $A(1,-1)=(-1,1)$, 둘째 열 $A(1,2)=(2,4)$). $P^{-1}(AP)=\tfrac13\begin{bmatrix}2&-1\\1&1\end{bmatrix}\begin{bmatrix}-1&2\\1&4\end{bmatrix}$의 $(1,1)=\tfrac13(2\cdot(-1)+(-1)\cdot1)=\tfrac13(-3)=-1$, $(1,2)=\tfrac13(2\cdot2+(-1)\cdot4)=0$, $(2,1)=\tfrac13(1\cdot(-1)+1\cdot1)=0$, $(2,2)=\tfrac13(1\cdot2+1\cdot4)=2$이라 $\begin{bmatrix}-1&0\\0&2\end{bmatrix}$입니다. 대각합 $1$, 행렬식 $-2$가 $A$와 일치합니다.

> **문제 13.** (심화) 어떤 정사각행렬도 대각합이 곧 고유값의 합임을 $2\times2$에서 특성다항식으로 보이십시오.
> **답.** 특성다항식의 일차항 계수가 $-\operatorname{tr}A$이기 때문입니다.
> **풀이.** $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$의 특성다항식은 $\det(A-\lambda I)=(a-\lambda)(d-\lambda)-bc=\lambda^{2}-(a+d)\lambda+(ad-bc)$입니다. 두 근 $\lambda_1,\lambda_2$의 합은 근과 계수의 관계로 $\lambda_1+\lambda_2=a+d=\operatorname{tr}A$이고 곱은 $\lambda_1\lambda_2=ad-bc=\det A$입니다. 닮음이 대각합과 행렬식을 보존하는 것은 곧 고유값을 보존함과 같습니다.

> **문제 14.** (표준) 표준기저에서 기저 $C=\{(2,0),(0,3)\}$로 $\mathbf{v}=(4,9)$의 좌표벡터를 구하십시오.
> **답.** $[\mathbf{v}]_C=\begin{bmatrix}2\\3\end{bmatrix}$입니다.
> **풀이.** $P_C=\begin{bmatrix}2&0\\0&3\end{bmatrix}$이라 $P_C^{-1}=\begin{bmatrix}\tfrac12&0\\0&\tfrac13\end{bmatrix}$입니다. $[\mathbf{v}]_C=P_C^{-1}\mathbf{v}=\begin{bmatrix}\tfrac12\cdot4\\\tfrac13\cdot9\end{bmatrix}=\begin{bmatrix}2\\3\end{bmatrix}$입니다. 검산하면 $2(2,0)+3(0,3)=(4,9)$입니다.

> **문제 15.** (심화) 문제 8의 $A=\begin{bmatrix}3&1\\1&3\end{bmatrix}$에 대해 $A^{2}$을 구하고 그 고유값이 원래 고유값의 제곱임을 확인하십시오.
> **답.** $A^{2}=\begin{bmatrix}10&6\\6&10\end{bmatrix}$이고 고유값은 $16,4$로 각각 $4^{2},2^{2}$입니다.
> **풀이.** $A^{2}$의 $(1,1)=3\cdot3+1\cdot1=10$, $(1,2)=3\cdot1+1\cdot3=6$, $(2,1)=6$, $(2,2)=1\cdot1+3\cdot3=10$입니다. $A$의 고유값은 문제 8에서 $4,2$였습니다. $A^{2}$의 대각합은 $10+10=20=16+4$, 행렬식은 $100-36=64=16\cdot4$이라 고유값이 $16,4$로 확인되며 이는 $4^{2},2^{2}$입니다. $A=PDP^{-1}$이면 $A^{2}=PD^{2}P^{-1}$이라 고유값이 제곱되기 때문입니다.
