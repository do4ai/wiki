---
title: "문제집 - 01. 벡터와 공간"
---
# 문제집 - 01. 벡터와 공간

이 문제집은 1단원 세 강의(벡터와 연산 / 벡터공간과 부분공간 / 일차독립, 기저, 차원)의 내용을 본문보다 한 단계 어렵게 훈련하기 위한 것입니다. 각 문제는 난이도(기초·표준·심화)를 표시했고, 답과 단계별 풀이를 함께 실었습니다. 손으로 풀 때는 답을 가리고 풀이의 중간식을 스스로 재현해 보시기 바랍니다.

## 1. 벡터와 연산

> **문제 1.** (기초) $\mathbf{u}=\begin{bmatrix}3\\-1\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}-2\\4\\1\end{bmatrix}$의 내적을 구하십시오.
> **답.** $-8$입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=3\cdot(-2)+(-1)\cdot4+2\cdot1=-6-4+2=-8$입니다.

> **문제 2.** (기초) $\mathbf{v}=\begin{bmatrix}1\\-4\\8\end{bmatrix}$의 노름을 구하십시오.
> **답.** $9$입니다.
> **풀이.** $\lVert\mathbf{v}\rVert=\sqrt{1^2+(-4)^2+8^2}=\sqrt{1+16+64}=\sqrt{81}=9$입니다.

> **문제 3.** (기초) $\mathbf{v}=\begin{bmatrix}2\\-2\\1\end{bmatrix}$를 정규화하십시오.
> **답.** $\begin{bmatrix}2/3\\-2/3\\1/3\end{bmatrix}$입니다.
> **풀이.** 노름은 $\sqrt{4+4+1}=\sqrt9=3$이므로 각 성분을 3으로 나눕니다. 검산하면 $(2/3)^2+(-2/3)^2+(1/3)^2=\tfrac{4+4+1}{9}=1$이라 단위벡터입니다.

> **문제 4.** (표준) $\mathbf{u}=\begin{bmatrix}k\\2\\-1\end{bmatrix}$가 $\mathbf{v}=\begin{bmatrix}3\\k\\5\end{bmatrix}$와 직교하도록 $k$를 구하십시오.
> **답.** $k=1$입니다.
> **풀이.** 직교 조건 $\mathbf{u}\cdot\mathbf{v}=0$은 $3k+2k+(-1)\cdot5=5k-5=0$이므로 $k=1$입니다. 검산하면 $3\cdot1+2\cdot1-1\cdot5=3+2-5=0$입니다.

> **문제 5.** (표준) $\mathbf{u}=\begin{bmatrix}1\\0\\-1\end{bmatrix}$와 $\mathbf{v}=\begin{bmatrix}1\\1\\0\end{bmatrix}$ 사이의 각도를 구하십시오.
> **답.** $60^\circ$입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=1+0+0=1$, $\lVert\mathbf{u}\rVert=\sqrt2$, $\lVert\mathbf{v}\rVert=\sqrt2$입니다. 따라서 $\cos\theta=\dfrac{1}{\sqrt2\cdot\sqrt2}=\dfrac12$이고 $\theta=60^\circ$입니다.

> **문제 6.** (표준) $\mathbf{u}=\begin{bmatrix}2\\3\end{bmatrix}$를 $\mathbf{v}=\begin{bmatrix}4\\-1\end{bmatrix}$ 방향으로 사영한 벡터를 구하십시오.
> **답.** $\begin{bmatrix}20/17\\-5/17\end{bmatrix}$입니다.
> **풀이.** 사영은 $\operatorname{proj}_{\mathbf{v}}\mathbf{u}=\dfrac{\mathbf{u}\cdot\mathbf{v}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}$입니다. $\mathbf{u}\cdot\mathbf{v}=8-3=5$, $\mathbf{v}\cdot\mathbf{v}=16+1=17$이므로 $\dfrac{5}{17}\begin{bmatrix}4\\-1\end{bmatrix}=\begin{bmatrix}20/17\\-5/17\end{bmatrix}$입니다.

> **문제 7.** (표준) $\mathbf{v}=\begin{bmatrix}a\\1\\1\end{bmatrix}$의 노름이 $3$이 되는 $a\ge0$을 구하십시오.
> **답.** $a=\sqrt7$입니다.
> **풀이.** $\lVert\mathbf{v}\rVert^2=a^2+1+1=9$이므로 $a^2=7$입니다. $a\ge0$이므로 $a=\sqrt7$입니다.

> **문제 8.** (표준) $\mathbf{u}=\begin{bmatrix}2\\2\\1\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}0\\3\\4\end{bmatrix}$ 사이 각도의 코사인 값을 구하십시오.
> **답.** $\cos\theta=\dfrac23$입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=0+6+4=10$, $\lVert\mathbf{u}\rVert=\sqrt{4+4+1}=3$, $\lVert\mathbf{v}\rVert=\sqrt{0+9+16}=5$입니다. 따라서 $\cos\theta=\dfrac{10}{3\cdot5}=\dfrac{10}{15}=\dfrac23$입니다.

> **문제 9.** (표준) $\mathbf{u}=\begin{bmatrix}1\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}2\\-1\end{bmatrix}$에 대해 삼각부등식 $\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$의 양변을 구해 비교하십시오.
> **답.** 좌변 $\sqrt{10}\approx3.16$, 우변 $2\sqrt5\approx4.47$로 진부등식입니다.
> **풀이.** $\mathbf{u}+\mathbf{v}=\begin{bmatrix}3\\1\end{bmatrix}$이므로 좌변은 $\sqrt{9+1}=\sqrt{10}\approx3.16$입니다. $\lVert\mathbf{u}\rVert=\sqrt5$, $\lVert\mathbf{v}\rVert=\sqrt5$이므로 우변은 $2\sqrt5\approx4.47$입니다. $\mathbf{u}\cdot\mathbf{v}=2-2=0$으로 두 벡터가 평행이 아니므로 등호가 아닌 진부등식이 성립합니다.

> **문제 10.** (심화) $\mathbf{u}=\begin{bmatrix}1\\2\\2\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}2\\3\\6\end{bmatrix}$에서 코시-슈바르츠 부등식이 성립함을 수치로 확인하고 등호 여부를 판정하십시오.
> **답.** $|\mathbf{u}\cdot\mathbf{v}|=20\le 21=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$인 진부등식입니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=2+6+12=20$입니다. $\lVert\mathbf{u}\rVert=\sqrt{1+4+4}=3$, $\lVert\mathbf{v}\rVert=\sqrt{4+9+36}=7$이므로 우변은 $21$입니다. $20\le21$이고, $\mathbf{v}$가 $\mathbf{u}$의 배수가 아니어서 평행이 아니므로 등호가 아닌 진부등식입니다.

> **문제 11.** (심화) 두 단위벡터 $\mathbf{u},\mathbf{v}$ 사이 각도가 $120^\circ$일 때 $\lVert\mathbf{u}+\mathbf{v}\rVert$을 구하십시오.
> **답.** $1$입니다.
> **풀이.** $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2$입니다. 단위벡터이므로 $\lVert\mathbf{u}\rVert=\lVert\mathbf{v}\rVert=1$이고 $\mathbf{u}\cdot\mathbf{v}=\cos120^\circ=-\tfrac12$입니다. 따라서 $\lVert\mathbf{u}+\mathbf{v}\rVert^2=1+2(-\tfrac12)+1=1$이라 $\lVert\mathbf{u}+\mathbf{v}\rVert=1$입니다.

> **문제 12.** (심화) $\lVert\mathbf{u}\rVert=\lVert\mathbf{v}\rVert$이면 $\mathbf{u}+\mathbf{v}$와 $\mathbf{u}-\mathbf{v}$가 직교함을 보이십시오.
> **답.** 내적이 $\lVert\mathbf{u}\rVert^2-\lVert\mathbf{v}\rVert^2=0$이 되기 때문입니다.
> **풀이.** $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=\mathbf{u}\cdot\mathbf{u}-\mathbf{u}\cdot\mathbf{v}+\mathbf{v}\cdot\mathbf{u}-\mathbf{v}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert^2-\lVert\mathbf{v}\rVert^2$입니다. 대칭성으로 가운데 두 항이 상쇄됩니다. 두 노름이 같으면 이 값이 0이라 직교합니다. 기하적으로 마름모의 두 대각선이 직교한다는 사실입니다.

> **문제 13.** (심화) 평행사변형 항등식 $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$을 증명하십시오.
> **답.** 두 노름 제곱을 전개해 더하면 교차항이 상쇄됩니다.
> **풀이.** $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2$이고 $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2$입니다. 두 식을 더하면 $2(\mathbf{u}\cdot\mathbf{v})$ 항이 상쇄되어 $2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$이 남습니다.

> **문제 14.** (심화) 코시-슈바르츠 부등식을 이용해 임의의 실수 $x,y,z$에 대해 $(x+y+z)^2\le 3(x^2+y^2+z^2)$임을 보이십시오.
> **답.** $\mathbf{u}=\begin{bmatrix}x\\y\\z\end{bmatrix}$, $\mathbf{v}=\begin{bmatrix}1\\1\\1\end{bmatrix}$에 부등식을 적용하면 됩니다.
> **풀이.** $\mathbf{u}\cdot\mathbf{v}=x+y+z$이고 $\lVert\mathbf{u}\rVert^2=x^2+y^2+z^2$, $\lVert\mathbf{v}\rVert^2=3$입니다. 코시-슈바르츠의 제곱꼴 $(\mathbf{u}\cdot\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$에 대입하면 $(x+y+z)^2\le 3(x^2+y^2+z^2)$입니다. 등호는 $x=y=z$일 때 성립합니다.

> **문제 15.** (심화) 임의의 $\mathbf{u},\mathbf{v}$에 대해 $\mathbf{u}\cdot\mathbf{v}=\tfrac14\left(\lVert\mathbf{u}+\mathbf{v}\rVert^2-\lVert\mathbf{u}-\mathbf{v}\rVert^2\right)$임을 보이십시오(편극 항등식).
> **답.** 두 노름 제곱의 차에서 교차항만 살아남기 때문입니다.
> **풀이.** $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2$에서 $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2(\mathbf{u}\cdot\mathbf{v})+\lVert\mathbf{v}\rVert^2$을 빼면 $4(\mathbf{u}\cdot\mathbf{v})$이 남습니다. 양변을 4로 나누면 항등식을 얻습니다. 이는 노름만으로 내적을 복원할 수 있음을 뜻합니다.

## 2. 벡터공간과 부분공간

> **문제 1.** (기초) $W=\{\begin{bmatrix}x\\y\\z\end{bmatrix}:z=0\}$이 $\mathbb{R}^3$의 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** $\mathbf{0}$은 셋째 성분이 0이라 $W$에 속합니다. 셋째 성분이 0인 두 벡터의 합과 스칼라배도 셋째 성분이 0으로 유지되므로 세 조건을 모두 만족합니다. 이는 $xy$평면입니다.

> **문제 2.** (기초) $W=\{\begin{bmatrix}x\\y\end{bmatrix}:x=2y\}$가 $\mathbb{R}^2$의 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** $\mathbf{0}$은 $0=2\cdot0$을 만족합니다. $x_1=2y_1$, $x_2=2y_2$이면 $x_1+x_2=2(y_1+y_2)$, $cx_1=2(cy_1)$이라 합과 스칼라배도 조건을 유지합니다. 원점을 지나는 직선이라 부분공간입니다.

> **문제 3.** (표준) $W=\{\begin{bmatrix}x\\y\end{bmatrix}:x^2=y^2\}$이 $\mathbb{R}^2$의 부분공간인지 판정하십시오.
> **답.** 부분공간이 아닙니다.
> **풀이.** $\begin{bmatrix}1\\1\end{bmatrix}$과 $\begin{bmatrix}1\\-1\end{bmatrix}$은 모두 $x^2=y^2$을 만족해 $W$에 있습니다. 그러나 합 $\begin{bmatrix}2\\0\end{bmatrix}$은 $2^2=4\ne0=0^2$이라 $W$에 없습니다. 덧셈에 닫혀 있지 않으므로 부분공간이 아닙니다.

> **문제 4.** (표준) $\mathbb{R}^3$에서 $W=\{\begin{bmatrix}x\\y\\z\end{bmatrix}:x+y+z=0\}$의 생성 벡터 두 개를 구하십시오.
> **답.** $\operatorname{span}\left\{\begin{bmatrix}-1\\1\\0\end{bmatrix},\begin{bmatrix}-1\\0\\1\end{bmatrix}\right\}$입니다.
> **풀이.** $x=-y-z$로 두면 $\begin{bmatrix}x\\y\\z\end{bmatrix}=y\begin{bmatrix}-1\\1\\0\end{bmatrix}+z\begin{bmatrix}-1\\0\\1\end{bmatrix}$입니다. $y,z$가 자유변수이므로 두 벡터가 이 평면을 생성합니다.

> **문제 5.** (표준) $\begin{bmatrix}1\\2\\3\end{bmatrix}$이 $\operatorname{span}\left\{\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}0\\1\\1\end{bmatrix}\right\}$에 속하는지 판정하십시오.
> **답.** 속하지 않습니다.
> **풀이.** $c_1\begin{bmatrix}1\\1\\0\end{bmatrix}+c_2\begin{bmatrix}0\\1\\1\end{bmatrix}=\begin{bmatrix}c_1\\c_1+c_2\\c_2\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}$은 $c_1=1$, $c_2=3$을 주지만 둘째 식은 $c_1+c_2=4\ne2$입니다. 모순이라 해가 없으므로 속하지 않습니다.

> **문제 6.** (표준) $A=\begin{bmatrix}1&2&3\\0&1&1\end{bmatrix}$의 영공간을 구하십시오.
> **답.** $\operatorname{Nul}(A)=\operatorname{span}\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}$입니다.
> **풀이.** $x_1+2x_2+3x_3=0$, $x_2+x_3=0$에서 $x_3$을 자유변수로 두면 $x_2=-x_3$, $x_1=-2(-x_3)-3x_3=-x_3$입니다. 따라서 $\mathbf{x}=x_3\begin{bmatrix}-1\\-1\\1\end{bmatrix}$입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&-1&2\\2&-2&4\end{bmatrix}$의 영공간의 차원을 구하십시오.
> **답.** $2$입니다.
> **풀이.** 둘째 행은 첫째 행의 2배라 조건은 $x_1-x_2+2x_3=0$ 하나뿐입니다. $x_2,x_3$이 자유변수이므로 $x_1=x_2-2x_3$이고 $\mathbf{x}=x_2\begin{bmatrix}1\\1\\0\end{bmatrix}+x_3\begin{bmatrix}-2\\0\\1\end{bmatrix}$입니다. 자유변수가 둘이라 차원 2입니다.

> **문제 8.** (표준) $\begin{bmatrix}3\\3\\3\end{bmatrix}$이 $A=\begin{bmatrix}1&0\\1&1\\0&1\end{bmatrix}$의 열공간에 속하는지 판정하십시오.
> **답.** 속하지 않습니다.
> **풀이.** $\operatorname{Col}(A)=\operatorname{span}\left\{\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}0\\1\\1\end{bmatrix}\right\}$입니다. $c_1\begin{bmatrix}1\\1\\0\end{bmatrix}+c_2\begin{bmatrix}0\\1\\1\end{bmatrix}=\begin{bmatrix}c_1\\c_1+c_2\\c_2\end{bmatrix}=\begin{bmatrix}3\\3\\3\end{bmatrix}$은 $c_1=3$, $c_2=3$을 주지만 둘째 식은 $c_1+c_2=6\ne3$이라 모순입니다. 해가 없으므로 속하지 않습니다.

> **문제 9.** (표준) $P_2$에서 $W=\{p\in P_2 : p(1)=0\}$이 부분공간인지 판정하십시오.
> **답.** 부분공간입니다.
> **풀이.** 영다항식은 $1$에서 값이 0이라 $W$에 있습니다. $p(1)=q(1)=0$이면 $(p+q)(1)=p(1)+q(1)=0$, $(cp)(1)=cp(1)=0$이므로 두 연산에 닫혀 있습니다. 세 조건을 만족합니다.

> **문제 10.** (표준) $\mathbb{R}^4$에서 $W=\{\begin{bmatrix}x\\y\\z\\w\end{bmatrix}:x+y=0,\ z=w\}$의 차원을 구하십시오.
> **답.** $2$입니다.
> **풀이.** 두 조건에서 $y=-x$, $w=z$이므로 $x,z$가 자유변수입니다. $\begin{bmatrix}x\\y\\z\\w\end{bmatrix}=x\begin{bmatrix}1\\-1\\0\\0\end{bmatrix}+z\begin{bmatrix}0\\0\\1\\1\end{bmatrix}$이라 생성 벡터가 둘이고, 두 벡터는 독립이라 차원 2입니다.

> **문제 11.** (심화) 두 부분공간 $U,W\subseteq V$의 교집합 $U\cap W$가 부분공간임을 보이십시오.
> **답.** 세 조건이 양쪽에서 동시에 성립하므로 부분공간입니다.
> **풀이.** $\mathbf{0}$은 $U$에도 $W$에도 있으므로 $U\cap W$에 있습니다. $\mathbf{x},\mathbf{y}\in U\cap W$이면 $U$가 부분공간이라 $\mathbf{x}+\mathbf{y}\in U$이고, $W$도 부분공간이라 $\mathbf{x}+\mathbf{y}\in W$이므로 합이 교집합에 있습니다. $c\mathbf{x}$도 같은 이유로 양쪽에 있습니다. 세 조건을 만족합니다.

> **문제 12.** (심화) $A\mathbf{x}=\mathbf{b}$에서 $\mathbf{b}\ne\mathbf{0}$이면 그 해집합이 부분공간이 아님을 보이십시오.
> **답.** 영벡터가 해가 아니기 때문입니다.
> **풀이.** $\mathbf{x}=\mathbf{0}$을 넣으면 $A\mathbf{0}=\mathbf{0}\ne\mathbf{b}$이므로 $\mathbf{0}$은 해집합에 없습니다. 부분공간은 반드시 영벡터를 포함해야 하므로 이 해집합은 부분공간이 아닙니다. 다만 특수해 하나에 영공간을 더한 아핀 집합의 꼴을 가집니다.

> **문제 13.** (심화) $2\times2$ 실행렬 공간에서 대칭행렬 전체 $W=\{A:A=A^{T}\}$가 부분공간임을 보이고 차원을 구하십시오.
> **답.** 부분공간이며 차원은 $3$입니다.
> **풀이.** 영행렬은 대칭이라 $W$에 있습니다. $A=A^T$, $B=B^T$이면 $(A+B)^T=A^T+B^T=A+B$, $(cA)^T=cA^T=cA$이라 두 연산에 닫혀 있습니다. 대칭행렬은 $\begin{bmatrix}a&b\\b&d\end{bmatrix}$로 자유 성분이 $a,b,d$ 셋이므로 차원은 3입니다.

> **문제 14.** (심화) 두 부분공간의 합집합 $U\cup W$가 일반적으로 부분공간이 아님을 반례로 보이십시오.
> **답.** $\mathbb{R}^2$의 두 좌표축의 합집합이 반례입니다.
> **풀이.** $U$를 $x$축, $W$를 $y$축이라 하면 각각 부분공간입니다. $\begin{bmatrix}1\\0\end{bmatrix}\in U$, $\begin{bmatrix}0\\1\end{bmatrix}\in W$이지만 합 $\begin{bmatrix}1\\1\end{bmatrix}$은 어느 축에도 없어 $U\cup W$에 없습니다. 덧셈에 닫혀 있지 않으므로 부분공간이 아닙니다.

> **문제 15.** (심화) $\mathbb{R}^2$에서 $U$가 $x$축, $W=\{\begin{bmatrix}t\\t\end{bmatrix}:t\in\mathbb{R}\}$일 때 $U\cap W$를 구하십시오.
> **답.** $U\cap W=\{\mathbf{0}\}$입니다.
> **풀이.** $U$의 원소는 $\begin{bmatrix}s\\0\end{bmatrix}$, $W$의 원소는 $\begin{bmatrix}t\\t\end{bmatrix}$입니다. 두 꼴이 같으려면 둘째 성분에서 $t=0$이고 첫째 성분에서 $s=t=0$이어야 합니다. 따라서 교집합은 영벡터 하나뿐입니다.

## 3. 일차독립, 기저, 차원

> **문제 1.** (기초) $\begin{bmatrix}2\\4\end{bmatrix},\begin{bmatrix}3\\6\end{bmatrix}$의 일차독립 여부를 판정하십시오.
> **답.** 일차종속입니다.
> **풀이.** $\begin{bmatrix}3\\6\end{bmatrix}=\tfrac32\begin{bmatrix}2\\4\end{bmatrix}$로 배수 관계입니다. $3\begin{bmatrix}2\\4\end{bmatrix}-2\begin{bmatrix}3\\6\end{bmatrix}=\mathbf{0}$인 자명하지 않은 결합이 있으므로 종속입니다.

> **문제 2.** (기초) $\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}0\\2\\0\end{bmatrix},\begin{bmatrix}0\\0\\3\end{bmatrix}$이 $\mathbb{R}^3$의 기저인지 판정하십시오.
> **답.** 기저입니다.
> **풀이.** $c_1\begin{bmatrix}1\\0\\0\end{bmatrix}+c_2\begin{bmatrix}0\\2\\0\end{bmatrix}+c_3\begin{bmatrix}0\\0\\3\end{bmatrix}=\begin{bmatrix}c_1\\2c_2\\3c_3\end{bmatrix}=\mathbf{0}$은 $c_1=c_2=c_3=0$을 강제해 독립입니다. 독립인 3개가 $\dim\mathbb{R}^3=3$과 같으므로 기저입니다.

> **문제 3.** (표준) $\begin{bmatrix}1\\1\\1\end{bmatrix},\begin{bmatrix}1\\2\\4\end{bmatrix},\begin{bmatrix}1\\3\\9\end{bmatrix}$이 일차독립인지 판정하십시오.
> **답.** 일차독립입니다.
> **풀이.** 이 세 열을 나란히 둔 행렬의 행렬식은 노드 $1,2,3$의 판데르몬데 행렬식 $(2-1)(3-1)(3-2)=1\cdot2\cdot1=2\ne0$입니다. 행렬식이 0이 아니므로 세 벡터는 독립입니다.

> **문제 4.** (표준) $\mathbf{v}=\begin{bmatrix}5\\1\end{bmatrix}$의 기저 $B=\left\{\begin{bmatrix}1\\1\end{bmatrix},\begin{bmatrix}1\\-1\end{bmatrix}\right\}$에 대한 좌표 $[\mathbf{v}]_B$를 구하십시오.
> **답.** $[\mathbf{v}]_B=\begin{bmatrix}3\\2\end{bmatrix}$입니다.
> **풀이.** $c_1\begin{bmatrix}1\\1\end{bmatrix}+c_2\begin{bmatrix}1\\-1\end{bmatrix}=\begin{bmatrix}5\\1\end{bmatrix}$은 $c_1+c_2=5$, $c_1-c_2=1$입니다. 더하면 $2c_1=6$이라 $c_1=3$, 따라서 $c_2=2$입니다.

> **문제 5.** (표준) $\operatorname{span}\left\{\begin{bmatrix}1\\2\\3\end{bmatrix},\begin{bmatrix}2\\4\\6\end{bmatrix},\begin{bmatrix}1\\0\\1\end{bmatrix}\right\}$의 차원을 구하십시오.
> **답.** $2$입니다.
> **풀이.** 둘째 벡터는 첫째의 2배라 새 방향을 더하지 않습니다. 남은 $\begin{bmatrix}1\\2\\3\end{bmatrix}$과 $\begin{bmatrix}1\\0\\1\end{bmatrix}$은 배수 관계가 아니라 독립이므로 이 둘이 기저가 되고 차원은 2입니다.

> **문제 6.** (표준) $\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}0\\1\\1\end{bmatrix},\begin{bmatrix}1\\0\\1\end{bmatrix}$이 일차독립인지 판정하십시오.
> **답.** 일차독립입니다.
> **풀이.** $c_1\begin{bmatrix}1\\1\\0\end{bmatrix}+c_2\begin{bmatrix}0\\1\\1\end{bmatrix}+c_3\begin{bmatrix}1\\0\\1\end{bmatrix}=\mathbf{0}$은 성분별로 $c_1+c_3=0$, $c_1+c_2=0$, $c_2+c_3=0$입니다. 첫 식에서 $c_1=-c_3$, 둘째에 넣으면 $c_2=c_3$, 셋째에 넣으면 $2c_3=0$이라 $c_3=0$이고 나머지도 0입니다. 자명해뿐이라 독립입니다.

> **문제 7.** (표준) $A=\begin{bmatrix}1&2&0\\0&0&1\end{bmatrix}$의 열공간의 기저와 차원을 구하십시오.
> **답.** 기저 $\left\{\begin{bmatrix}1\\0\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}\right\}$, 차원 $2$입니다.
> **풀이.** 세 열은 $\begin{bmatrix}1\\0\end{bmatrix},\begin{bmatrix}2\\0\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}$입니다. 둘째 열은 첫째의 2배라 버립니다. 남은 $\begin{bmatrix}1\\0\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}$은 독립이라 열공간은 $\mathbb{R}^2$ 전체이고 차원 2입니다.

> **문제 8.** (표준) $A=\begin{bmatrix}1&2&0&3\\0&0&1&4\end{bmatrix}$의 영공간의 기저와 차원을 구하십시오.
> **답.** 기저 $\left\{\begin{bmatrix}-2\\1\\0\\0\end{bmatrix},\begin{bmatrix}-3\\0\\-4\\1\end{bmatrix}\right\}$, 차원 $2$입니다.
> **풀이.** $x_1+2x_2+3x_4=0$, $x_3+4x_4=0$입니다. $x_2,x_4$가 자유변수이고 $x_1=-2x_2-3x_4$, $x_3=-4x_4$입니다. $(x_2,x_4)=(1,0)$이면 $\begin{bmatrix}-2\\1\\0\\0\end{bmatrix}$, $(0,1)$이면 $\begin{bmatrix}-3\\0\\-4\\1\end{bmatrix}$이라 차원 2입니다.

> **문제 9.** (표준) 문제 8의 행렬 $A$에서 계수정리 $\operatorname{rank}(A)+\dim\operatorname{Nul}(A)=n$이 성립함을 확인하십시오.
> **답.** $2+2=4$로 열의 개수와 같습니다.
> **풀이.** $A$의 서로 독립인 열은 $\begin{bmatrix}1\\0\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}$ 두 개라 $\operatorname{rank}(A)=2$입니다. 문제 8에서 $\dim\operatorname{Nul}(A)=2$입니다. 둘을 더하면 $4$로 $A$의 열의 개수 $n=4$와 같습니다.

> **문제 10.** (표준) $P_2$에서 $\{1+x,\ x+x^2,\ 1+x^2\}$이 기저인지 판정하십시오.
> **답.** 기저입니다.
> **풀이.** 세 다항식을 $\{1,x,x^2\}$ 좌표로 옮기면 $\begin{bmatrix}1\\1\\0\end{bmatrix},\begin{bmatrix}0\\1\\1\end{bmatrix},\begin{bmatrix}1\\0\\1\end{bmatrix}$입니다. 문제 6에서 이 세 벡터가 독립임을 보였고, $\dim P_2=3$과 개수가 같으므로 기저입니다.

> **문제 11.** (심화) $\mathbb{R}^3$의 임의의 네 벡터가 항상 일차종속임을 설명하십시오.
> **답.** 일차독립 집합의 크기는 차원 3을 넘을 수 없기 때문입니다.
> **풀이.** 교환 정리에 따라 $n$개의 벡터로 생성되는 공간에서 일차독립 벡터는 많아야 $n$개입니다. $\dim\mathbb{R}^3=3$이므로 독립인 벡터는 최대 3개입니다. 네 벡터는 3을 넘으므로 반드시 종속입니다.

> **문제 12.** (심화) 일차독립인 집합 $\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$에 벡터 $\mathbf{w}$를 추가해도 독립이 유지될 조건을 말하고 이유를 설명하십시오.
> **답.** $\mathbf{w}\notin\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$이어야 합니다.
> **풀이.** $\mathbf{w}$가 기존 span에 있으면 $\mathbf{w}=\sum c_i\mathbf{v}_i$로 표현되어 $\mathbf{w}-\sum c_i\mathbf{v}_i=\mathbf{0}$인 자명하지 않은 결합이 생기므로 종속입니다. 반대로 $\mathbf{w}$가 span 밖이면 $d\mathbf{w}+\sum c_i\mathbf{v}_i=\mathbf{0}$에서 $d\ne0$이면 $\mathbf{w}$가 span에 들어가 모순이라 $d=0$이고, 이어 기존 독립성으로 모든 $c_i=0$이 되어 독립이 유지됩니다.

> **문제 13.** (심화) $\dim V=n$이고 $S\subseteq V$가 $V$를 생성하는 $n$개의 벡터로 이루어지면 $S$가 기저임을 설명하십시오.
> **답.** 개수가 차원과 같은 생성 집합은 자동으로 독립이기 때문입니다.
> **풀이.** $S$가 종속이라면 어떤 벡터가 나머지의 결합이라 그것을 제거해도 $V$를 생성합니다. 그러면 $n-1$개로 $V$를 생성하게 되는데, 이는 $n$차원 공간의 일차독립 집합(예: 한 기저)의 크기 $n$이 생성 집합의 크기를 넘을 수 없다는 사실에 모순입니다. 따라서 $S$는 독립이고 기저입니다.

> **문제 14.** (심화) $p(x)=2+3x+x^2$의 기저 $B=\{1,\ 1+x,\ 1+x+x^2\}$에 대한 좌표 $[p]_B$를 구하십시오.
> **답.** $[p]_B=\begin{bmatrix}-1\\2\\1\end{bmatrix}$입니다.
> **풀이.** $a\cdot1+b(1+x)+c(1+x+x^2)=2+3x+x^2$로 두고 계수를 비교합니다. $x^2$ 계수에서 $c=1$, $x$ 계수에서 $b+c=3$이라 $b=2$, 상수항에서 $a+b+c=2$이라 $a=2-2-1=-1$입니다. 검산하면 $-1+2(1+x)+(1+x+x^2)=2+3x+x^2$입니다.

> **문제 15.** (심화) 벡터 $\begin{bmatrix}1\\k\\1\end{bmatrix},\begin{bmatrix}1\\1\\k\end{bmatrix},\begin{bmatrix}k\\1\\1\end{bmatrix}$이 일차종속이 되는 $k$를 모두 구하십시오.
> **답.** $k=1$ 또는 $k=-2$입니다.
> **풀이.** 세 벡터를 열로 하는 행렬은 첫 행이 $(1,1,k)$인 순환행렬입니다. $3\times3$ 순환행렬의 행렬식 공식 $(c_0+c_1+c_2)\big(c_0^2+c_1^2+c_2^2-c_0c_1-c_1c_2-c_2c_0\big)$에 $(c_0,c_1,c_2)=(1,1,k)$를 넣습니다. 앞 인수는 $2+k$이고, 뒤 인수는 $(2+k^2)-(1+2k)=k^2-2k+1=(k-1)^2$입니다. 따라서 $\det=(k+2)(k-1)^2$입니다. 이것이 0이 되는 값은 $k=-2$와 $k=1$(중근)입니다. 실제로 $k=1$이면 세 벡터가 모두 $\begin{bmatrix}1\\1\\1\end{bmatrix}$로 같아 종속이고, $k=-2$이면 세 벡터의 합이 $\begin{bmatrix}0\\0\\0\end{bmatrix}$이 되어 종속입니다.
