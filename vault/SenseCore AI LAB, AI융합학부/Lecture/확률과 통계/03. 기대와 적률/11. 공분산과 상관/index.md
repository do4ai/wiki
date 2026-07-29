---
title: "11. 공분산과 상관"
---
# 11강. 공분산과 상관

앞 강의에서 한 변수의 중심과 퍼짐을 다뤘습니다. 이제 두 변수가 함께 어떻게 움직이는지를 잽니다. 하나가 커질 때 다른 하나도 커지는 경향을 공분산으로, 그 관계의 강도를 단위와 무관하게 상관계수로 읽습니다. 공분산은 앞 강의에서 미뤄 둔 합의 분산 규칙도 완성해 줍니다.

## 이 강의에서 할 수 있게 되는 것
- 공분산을 정의와 간편식으로 계산할 수 있습니다.
- 합과 선형결합의 분산을 공분산까지 넣어 계산할 수 있습니다.
- 상관계수를 구하고 그 값이 $-1$과 $1$ 사이임을 설명할 수 있습니다.
- 독립이면 무상관이지만 그 역은 성립하지 않음을 예로 들 수 있습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\operatorname{Cov}(X,Y)$ | 엑스와 와이의 공분산 | 함께 움직이는 정도, $E[(X-\mu_X)(Y-\mu_Y)]$ |
| $E[XY]$ | 엑스와이의 기대값 | 곱의 기대값, $\sum_{x,y}xy\,p(x,y)$ |
| $\rho$ 또는 $\rho_{XY}$ | 로 | 상관계수, $\dfrac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$ |
| $\sigma_X,\sigma_Y$ | 시그마 엑스, 와이 | 각 변수의 표준편차 |
| $\mu_X,\mu_Y$ | 뮤 엑스, 와이 | 각 변수의 기대값 |
| $p(x,y)$ | 결합확률 | $P(X=x,Y=y)$ |

## 2. 개념

### 2.1 공분산의 정의와 간편식

**정의.** 공분산은 두 변수의 편차의 곱의 기대값입니다.

$$
\operatorname{Cov}(X,Y)=E\big[(X-\mu_X)(Y-\mu_Y)\big]
$$

**유도.** 곱을 펼치면 $E[(X-\mu_X)(Y-\mu_Y)]=E[XY-\mu_X Y-\mu_Y X+\mu_X\mu_Y]=E[XY]-\mu_X\mu_Y-\mu_Y\mu_X+\mu_X\mu_Y$입니다. 정리하면 간편식이 나옵니다.

$$
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]
$$

**직관.** $X$가 평균 위일 때 $Y$도 평균 위인 경향이면 편차의 곱이 양수라 공분산이 양수입니다. 반대로 엇갈리면 음수입니다. $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$로, 공분산은 분산의 두 변수 일반화입니다.

> **문제 1.** (기초) $E[XY]=10$, $E[X]=2$, $E[Y]=3$일 때 공분산을 구하세요.
> **답.** $4$
> **풀이.** $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]=10-2\times 3=4$입니다.

다음 결합표를 문제 2~3에서 씁니다.

| $X\backslash Y$ | $Y=1$ | $Y=2$ |
|---|---|---|
| $X=0$ | $0.3$ | $0.1$ |
| $X=1$ | $0.2$ | $0.4$ |

> **문제 2.** (표준) 위 표에서 $E[X]$, $E[Y]$, $E[XY]$를 구하세요.
> **답.** $E[X]=0.6$, $E[Y]=1.5$, $E[XY]=1.0$
> **풀이.** $p_X(1)=0.2+0.4=0.6$이라 $E[X]=0.6$입니다. $p_Y(2)=0.1+0.4=0.5$이라 $E[Y]=1(0.5)+2(0.5)=1.5$입니다. $XY\ne 0$은 $X=1$인 두 칸뿐이라 $E[XY]=1\cdot1\cdot0.2+1\cdot2\cdot0.4=0.2+0.8=1.0$입니다.

> **문제 3.** (표준) 위 표에서 $\operatorname{Cov}(X,Y)$를 구하세요.
> **답.** $0.1$
> **풀이.** $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]=1.0-0.6\times 1.5=1.0-0.9=0.1$로 약한 양의 관계입니다.

> **문제 4.** (심화) $X$가 $-1,0,1$을 등확률로 갖고 $Y=X^2$입니다. $\operatorname{Cov}(X,Y)$를 구하세요.
> **답.** $0$
> **풀이.** $E[X]=0$이고 $E[XY]=E[X^3]=\tfrac13((-1)^3+0+1^3)=0$이므로 $\operatorname{Cov}(X,Y)=0-0\cdot E[Y]=0$입니다. 뒤에서 이 예로 무상관이 독립을 뜻하지 않음을 봅니다.

### 2.2 공분산의 성질과 합의 분산

**정의.** 공분산은 각 인수에 대해 선형이고 대칭입니다. 이를 쓰면 합의 분산이 공분산으로 완성됩니다.

$$
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)
$$

**유도.** $\operatorname{Var}(X+Y)=E[((X-\mu_X)+(Y-\mu_Y))^2]=E[(X-\mu_X)^2]+E[(Y-\mu_Y)^2]+2E[(X-\mu_X)(Y-\mu_Y)]$입니다. 세 항이 각각 $\operatorname{Var}(X)$, $\operatorname{Var}(Y)$, $2\operatorname{Cov}(X,Y)$입니다. 일반 선형결합에서는 $\operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)+2ab\operatorname{Cov}(X,Y)$입니다.

**직관.** 독립이면 $\operatorname{Cov}(X,Y)=0$이라 교차항이 사라져 분산이 그냥 더해집니다. 앞 강의의 독립합 규칙은 이 식의 특수한 경우였습니다.

> **문제 5.** (표준) $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$, $\operatorname{Cov}(X,Y)=3$일 때 $\operatorname{Var}(X+Y)$를 구하세요.
> **답.** $19$
> **풀이.** $\operatorname{Var}(X+Y)=4+9+2\times 3=19$입니다.

> **문제 6.** (표준) 같은 값들로 $\operatorname{Var}(X-Y)$를 구하세요.
> **답.** $7$
> **풀이.** $\operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)-2\operatorname{Cov}(X,Y)=4+9-6=7$입니다. 뺄셈이면 교차항의 부호가 바뀝니다.

> **문제 7.** (심화) $\operatorname{Var}(X)=2$, $\operatorname{Var}(Y)=8$, $\operatorname{Cov}(X,Y)=-1$일 때 $\operatorname{Var}(2X+3Y)$를 구하세요.
> **답.** $68$
> **풀이.** $\operatorname{Var}(2X+3Y)=4(2)+9(8)+2\cdot2\cdot3\cdot(-1)=8+72-12=68$입니다.

### 2.3 상관계수

**정의.** 상관계수는 공분산을 두 표준편차로 나눠 단위를 없앤 값입니다.

$$
\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\,\sigma_Y}
$$

**유도.** $X,Y$를 표준화한 $Z_X=\tfrac{X-\mu_X}{\sigma_X}$, $Z_Y=\tfrac{Y-\mu_Y}{\sigma_Y}$에 대해 $\rho=E[Z_XZ_Y]$입니다. $E[(Z_X\pm Z_Y)^2]\ge 0$을 펼치면 $1+1\pm 2\rho\ge 0$, 즉 $-1\le\rho\le 1$이 나옵니다. 코시-슈바르츠 부등식의 한 형태입니다.

**직관.** $\rho$는 단위와 무관하게 직선관계의 강도와 방향을 잽니다. $\rho=\pm1$은 $Y$가 $X$의 완전한 직선함수일 때이고, $\rho=0$은 직선관계가 없음(무상관)을 뜻합니다. 상관은 직선관계만 재고 인과를 뜻하지는 않습니다.

> **문제 8.** (기초) $\operatorname{Cov}(X,Y)=6$, $\sigma_X=2$, $\sigma_Y=5$일 때 $\rho$를 구하세요.
> **답.** $0.6$
> **풀이.** $\rho=\dfrac{6}{2\times 5}=\dfrac{6}{10}=0.6$입니다.

> **문제 9.** (표준) $\operatorname{Var}(X)=9$, $\operatorname{Var}(Y)=16$, $\operatorname{Cov}(X,Y)=-6$일 때 상관계수를 구하세요.
> **답.** $-0.5$
> **풀이.** $\sigma_X=3$, $\sigma_Y=4$이므로 $\rho=\dfrac{-6}{3\times 4}=\dfrac{-6}{12}=-0.5$입니다.

> **문제 10.** (심화) $Y=aX+b$ $(a>0)$일 때 $\rho_{XY}=1$임을 보이세요.
> **답.** 증명
> **풀이.** $\operatorname{Cov}(X,aX+b)=a\operatorname{Var}(X)$이고 $\sigma_Y=|a|\sigma_X=a\sigma_X$입니다. 따라서 $\rho=\dfrac{a\sigma_X^2}{\sigma_X\cdot a\sigma_X}=1$입니다. $a<0$이면 $\sigma_Y=-a\sigma_X$라 $\rho=-1$이 됩니다.

## 3. 유형 총정리(치트시트)

| 구할 것 | 방법 | 식 |
|---|---|---|
| 공분산 | 간편식 | $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]$ |
| $E[XY]$(이산) | 결합확률로 합 | $\sum_{x,y}xy\,p(x,y)$ |
| 합의 분산 | 공분산 교차항 | $\operatorname{Var}(X\pm Y)=\operatorname{Var}X+\operatorname{Var}Y\pm 2\operatorname{Cov}$ |
| 선형결합 분산 | 이차형식 | $\operatorname{Var}(aX+bY)=a^2\operatorname{Var}X+b^2\operatorname{Var}Y+2ab\operatorname{Cov}$ |
| 상관계수 | 공분산÷표준편차곱 | $\rho=\dfrac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$ |
| 범위 | 항상 성립 | $-1\le\rho\le 1$ |
| 독립 판정 | 독립⇒무상관(역 거짓) | 독립이면 $\operatorname{Cov}=0$ |

계산 순서는 이렇습니다. 주변분포로 $E[X],E[Y]$와 $E[XY]$를 구해 공분산을 얻고, 각 분산으로 상관계수를 만듭니다.

## 4. 종합 문제 드릴

문제 11~13은 다음 결합 PMF를 씁니다: $p(x,y)=c(x+y)$, $x\in\{1,2\}$, $y\in\{1,2,3\}$.

> **문제 11.** (표준) 정규화 상수 $c$를 정하고 $E[X]$, $E[Y]$를 구하세요.
> **답.** $c=\dfrac{1}{21}$, $E[X]=\dfrac{11}{7}$, $E[Y]=\dfrac{46}{21}$
> **풀이.** $\sum(x+y)$는 $x=1$행이 $2+3+4=9$, $x=2$행이 $3+4+5=12$로 합이 $21$이므로 $c=\dfrac{1}{21}$입니다. $p_X(1)=\dfrac{9}{21}$, $p_X(2)=\dfrac{12}{21}$이라 $E[X]=\dfrac{9+24}{21}=\dfrac{33}{21}=\dfrac{11}{7}$입니다. $p_Y(1)=\dfrac{5}{21}$, $p_Y(2)=\dfrac{7}{21}$, $p_Y(3)=\dfrac{9}{21}$이라 $E[Y]=\dfrac{5+14+27}{21}=\dfrac{46}{21}$입니다.

> **문제 12.** (심화) 위 $p(x,y)=\dfrac{x+y}{21}$에서 $E[XY]$와 $\operatorname{Cov}(X,Y)$를 구하세요.
> **답.** $E[XY]=\dfrac{24}{7}$, $\operatorname{Cov}(X,Y)=-\dfrac{2}{147}$
> **풀이.** $xy(x+y)$를 각 칸에서 계산하면 $x{=}1$: $1(2){+}2(3){+}3(4)=2+6+12=20$, $x{=}2$: $2(3){+}4(4){+}6(5)=6+16+30=52$입니다. 합 $72$라 $E[XY]=\dfrac{72}{21}=\dfrac{24}{7}$입니다. $E[X]E[Y]=\dfrac{11}{7}\cdot\dfrac{46}{21}=\dfrac{506}{147}$입니다. $\operatorname{Cov}=\dfrac{24}{7}-\dfrac{506}{147}=\dfrac{504-506}{147}=-\dfrac{2}{147}$입니다.

> **문제 13.** (심화) 위 분포에서 $X$와 $Y$가 독립인지 판정하세요.
> **답.** 독립이 아닙니다.
> **풀이.** 공분산이 $-\dfrac{2}{147}\ne 0$이므로 무상관도 아니고 따라서 독립일 수 없습니다. 결합확률이 주변확률의 곱으로 인수분해되지 않습니다.

> **문제 14.** (표준) $E[X]=1,E[Y]=2,E[X^2]=5,E[Y^2]=8,E[XY]=4$일 때 $\rho$를 구하세요.
> **답.** $\dfrac{2}{2\sqrt2}=\dfrac{1}{\sqrt2}\approx 0.707$
> **풀이.** $\operatorname{Var}(X)=5-1=4$, $\operatorname{Var}(Y)=8-4=4$, $\operatorname{Cov}=4-1\times2=2$입니다. $\rho=\dfrac{2}{\sqrt4\cdot\sqrt4}=\dfrac{2}{4}=0.5$입니다.

> **문제 15.** (심화) 동전 3번 던져 앞면 수를 $X$, 첫 던지기가 앞이면 $Y=1$ 아니면 $0$이라 합니다. $\operatorname{Cov}(X,Y)$를 구하세요.
> **답.** $\dfrac{1}{4}$
> **풀이.** $X=Y+W$로 쓰면 $W$는 뒤 두 번의 앞면 수($\operatorname{Var}=0.5$, $Y$와 독립)입니다. $\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y+W,Y)=\operatorname{Var}(Y)+\operatorname{Cov}(W,Y)=0.25+0=0.25$입니다($\operatorname{Var}(Y)=\tfrac12\cdot\tfrac12=0.25$).

> **문제 16.** (표준) $\operatorname{Var}(X)=\operatorname{Var}(Y)=1$이고 $\rho=0.8$입니다. $\operatorname{Var}(X+Y)$와 $\operatorname{Var}(X-Y)$를 구하세요.
> **답.** $\operatorname{Var}(X+Y)=3.6$, $\operatorname{Var}(X-Y)=0.4$
> **풀이.** $\operatorname{Cov}=\rho\sigma_X\sigma_Y=0.8$입니다. $\operatorname{Var}(X+Y)=1+1+2(0.8)=3.6$, $\operatorname{Var}(X-Y)=1+1-2(0.8)=0.4$입니다. 강한 양의 상관이면 차의 분산이 작습니다.

> **문제 17.** (심화) $\rho_{XY}=0.5$이고 $U=2X+1$, $V=-3Y+4$일 때 $\rho_{UV}$를 구하세요.
> **답.** $-0.5$
> **풀이.** 양의 배율은 상관계수를 바꾸지 않고 음의 배율은 부호만 뒤집습니다. $U$의 배율 $+2$, $V$의 배율 $-3$이라 부호가 한 번 바뀌어 $\rho_{UV}=-0.5$입니다.

> **문제 18.** (표준) $\operatorname{Cov}(X,Y)=5$, $\operatorname{Cov}(X,Z)=-2$일 때 $\operatorname{Cov}(X,\,2Y+3Z)$를 구하세요.
> **답.** $4$
> **풀이.** 공분산의 선형성으로 $\operatorname{Cov}(X,2Y+3Z)=2\operatorname{Cov}(X,Y)+3\operatorname{Cov}(X,Z)=2(5)+3(-2)=10-6=4$입니다.

> **문제 19.** (심화) $X$와 $Y=X^2$에서 $X\sim\text{Uniform}\{-2,-1,1,2\}$(등확률)입니다. $\operatorname{Cov}(X,Y)$와 상관을 구하세요.
> **답.** $\operatorname{Cov}=0$, $\rho=0$이지만 종속
> **풀이.** 대칭이라 $E[X]=0$, $E[XY]=E[X^3]=\tfrac14(-8-1+1+8)=0$이라 공분산 0입니다. 그러나 $Y$가 $X$로 완전히 정해지므로 종속입니다. 무상관≠독립의 예입니다.

> **문제 20.** (심화) 두 자산 수익률 $X,Y$가 각각 분산 $0.04$, 상관 $\rho$입니다. 반반 섞은 포트폴리오 $P=\tfrac12X+\tfrac12Y$의 분산을 $\rho$의 식으로 쓰고 $\rho=-1$일 때 값을 구하세요.
> **답.** $\operatorname{Var}(P)=0.02(1+\rho)$, $\rho=-1$이면 $0$
> **풀이.** $\operatorname{Var}(P)=\tfrac14(0.04)+\tfrac14(0.04)+2\cdot\tfrac12\cdot\tfrac12\operatorname{Cov}$입니다. $\operatorname{Cov}=\rho(0.04)$이므로 $\operatorname{Var}(P)=0.02+\tfrac12\rho(0.04)=0.02+0.02\rho=0.02(1+\rho)$입니다. $\rho=-1$이면 위험이 완전히 상쇄되어 0입니다.

## 5. 스스로 점검

1. 공분산의 간편식은 무엇인가?
2. $\operatorname{Cov}(X,X)$는 무엇과 같은가?
3. 합의 분산에서 교차항은 언제 사라지는가?
4. 상관계수의 범위와 그 이유는?
5. $\rho=\pm1$은 어떤 관계를 뜻하는가?
6. 독립이면 무상관인가? 역은?
7. $\operatorname{Cov}(X,Y)=3,\sigma_X=1,\sigma_Y=6$의 상관계수를 구하시오.
8. $\operatorname{Var}(X)=\operatorname{Var}(Y)=4,\operatorname{Cov}=2$일 때 $\operatorname{Var}(X-Y)$를 구하시오.

**정답.**
1. $\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y]$.
2. $\operatorname{Var}(X)$.
3. $\operatorname{Cov}(X,Y)=0$일 때(특히 독립일 때).
4. $-1\le\rho\le 1$. 표준화한 변수로 $E[(Z_X\pm Z_Y)^2]\ge 0$에서 나옵니다.
5. $Y$가 $X$의 완전한 직선함수($Y=aX+b$)임을 뜻하며, 부호는 $a$의 부호와 같습니다.
6. 독립이면 무상관입니다. 역은 성립하지 않습니다($Y=X^2$ 등 반례).
7. $\rho=\dfrac{3}{1\times 6}=0.5$.
8. $\operatorname{Var}(X-Y)=4+4-2\times2=4$.
