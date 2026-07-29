---
title: "12. 적률생성함수"
---
# 12강. 적률생성함수

기대값과 분산은 각각 1차, 2차 적률에서 나옵니다. 적률을 하나씩 적분·합으로 구하는 대신, 모든 적률을 한 함수에 담아 미분만으로 뽑아내는 도구가 적률생성함수(MGF)입니다. MGF는 적률 계산을 쉽게 할 뿐 아니라, 독립합의 분포를 판별하고 분포를 유일하게 결정하는 강력한 성질을 가집니다.

## 이 강의에서 할 수 있게 되는 것
- 적률생성함수를 정의대로 계산할 수 있습니다.
- MGF를 미분해 평균과 분산을 뽑아낼 수 있습니다.
- 주요 분포의 MGF를 알고 그것으로 적률을 유도할 수 있습니다.
- 독립합의 MGF가 곱이 됨을 써서 합의 분포를 판별할 수 있습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $M_X(t)$ | 엠 엑스 오브 티 | 적률생성함수, $E[e^{tX}]$ |
| $E[X^n]$ | 엔차 적률 | $X^n$의 기대값 |
| $M_X'(0)$ | 엠프라임 영 | $M_X(t)$를 미분해 $t=0$을 넣은 값 |
| $M_X^{(n)}(0)$ | 엔차 도함수 영에서 | $n$계 미분 후 $t=0$ 대입, $E[X^n]$과 같음 |
| $e^{tX}$ | 이 티엑스 | 지수함수, MGF의 피적분 대상 |
| $\prod$ | 파이 | 곱 기호 |

## 2. 개념

### 2.1 적률생성함수의 정의

**정의.** 확률변수 $X$의 적률생성함수는 $e^{tX}$의 기대값입니다. 0을 포함하는 어떤 구간의 $t$에서 정의됩니다.

$$
M_X(t)=E\big[e^{tX}\big]=\sum_x e^{tx}p(x)\ \ \text{또는}\ \ \int e^{tx}f(x)\,dx
$$

**유도.** 지수함수를 급수로 펼치면 $e^{tX}=1+tX+\dfrac{t^2X^2}{2!}+\dfrac{t^3X^3}{3!}+\cdots$입니다. 기대값을 취하면 각 항의 계수에 적률이 들어옵니다.

$$
M_X(t)=1+tE[X]+\frac{t^2}{2!}E[X^2]+\frac{t^3}{3!}E[X^3]+\cdots
$$

**직관.** MGF는 모든 적률 $E[X^n]$을 계수로 실어 나르는 하나의 함수입니다. 이름 그대로 적률을 "생성"합니다. $M_X(0)=E[e^0]=1$은 항상 성립합니다.

> **문제 1.** (기초) $p(0)=0.5,\ p(1)=0.5$인 $X$의 MGF를 구하세요.
> **답.** $M_X(t)=\dfrac{1+e^{t}}{2}$
> **풀이.** $M_X(t)=e^{t\cdot0}(0.5)+e^{t\cdot1}(0.5)=\dfrac{1+e^t}{2}$입니다. $t=0$을 넣으면 $\dfrac{1+1}{2}=1$로 확인됩니다.

> **문제 2.** (표준) $X\sim\text{Exp}(\lambda)$($f(x)=\lambda e^{-\lambda x}$, $x\ge0$)의 MGF를 구하고 정의역을 밝히세요.
> **답.** $M_X(t)=\dfrac{\lambda}{\lambda-t}$ $(t<\lambda)$
> **풀이.** $M_X(t)=\int_0^\infty e^{tx}\lambda e^{-\lambda x}\,dx=\lambda\int_0^\infty e^{-(\lambda-t)x}\,dx$입니다. $\lambda-t>0$일 때 적분이 $\dfrac{1}{\lambda-t}$로 수렴하므로 $M_X(t)=\dfrac{\lambda}{\lambda-t}$입니다.

> **문제 3.** (표준) $X\sim\text{Pois}(\lambda)$의 MGF가 $M_X(t)=e^{\lambda(e^t-1)}$임을 유도하세요.
> **답.** $M_X(t)=e^{\lambda(e^t-1)}$
> **풀이.** $M_X(t)=\sum_{x=0}^\infty e^{tx}\dfrac{e^{-\lambda}\lambda^x}{x!}=e^{-\lambda}\sum_{x=0}^\infty\dfrac{(\lambda e^t)^x}{x!}=e^{-\lambda}e^{\lambda e^t}=e^{\lambda(e^t-1)}$입니다. 지수급수 $\sum \tfrac{a^x}{x!}=e^a$를 썼습니다.

### 2.2 미분으로 적률 뽑기

**정의.** MGF를 $n$번 미분해 $t=0$을 넣으면 $n$차 적률이 나옵니다.

$$
M_X^{(n)}(0)=E[X^n],\qquad E[X]=M_X'(0),\quad \operatorname{Var}(X)=M_X''(0)-\big(M_X'(0)\big)^2
$$

**유도.** 급수 $M_X(t)=1+tE[X]+\tfrac{t^2}{2}E[X^2]+\cdots$을 한 번 미분하면 $M_X'(t)=E[X]+tE[X^2]+\cdots$이라 $t=0$에서 $E[X]$만 남습니다. 두 번 미분하면 $M_X''(0)=E[X^2]$입니다. 분산은 간편식으로 이어집니다.

**직관.** 적분·합을 다시 하지 않고 미분만으로 적률을 얻습니다. 분포를 MGF 하나로 요약해 두면 평균·분산이 손쉽게 나옵니다.

> **문제 4.** (표준) 문제 2의 지수분포 MGF $M_X(t)=\dfrac{\lambda}{\lambda-t}$에서 $E[X]$와 $\operatorname{Var}(X)$를 구하세요.
> **답.** $E[X]=\dfrac{1}{\lambda}$, $\operatorname{Var}(X)=\dfrac{1}{\lambda^2}$
> **풀이.** $M_X(t)=\lambda(\lambda-t)^{-1}$이라 $M_X'(t)=\lambda(\lambda-t)^{-2}$, $M_X'(0)=\lambda\cdot\lambda^{-2}=\tfrac1\lambda$입니다. $M_X''(t)=2\lambda(\lambda-t)^{-3}$이라 $M_X''(0)=2\lambda\cdot\lambda^{-3}=\tfrac{2}{\lambda^2}$입니다. $\operatorname{Var}(X)=\tfrac{2}{\lambda^2}-\tfrac{1}{\lambda^2}=\tfrac{1}{\lambda^2}$입니다.

> **문제 5.** (심화) 문제 3의 포아송 MGF $M_X(t)=e^{\lambda(e^t-1)}$에서 $E[X]$와 $\operatorname{Var}(X)$를 구하세요.
> **답.** $E[X]=\lambda$, $\operatorname{Var}(X)=\lambda$
> **풀이.** $M_X'(t)=e^{\lambda(e^t-1)}\cdot\lambda e^t$이라 $M_X'(0)=1\cdot\lambda=\lambda$입니다. $M_X''(t)=\lambda e^t\cdot M_X'(t)+\lambda e^t M_X(t)$... 정리하면 $M_X''(0)=\lambda^2+\lambda$입니다. $\operatorname{Var}(X)=(\lambda^2+\lambda)-\lambda^2=\lambda$입니다.

> **문제 6.** (기초) $M_X(t)=e^{3t+2t^2}$인 $X$의 평균과 분산을 구하세요.
> **답.** $E[X]=3$, $\operatorname{Var}(X)=4$
> **풀이.** 이것은 $N(3,4)$의 MGF $e^{\mu t+\frac12\sigma^2t^2}$ 꼴입니다. $\mu=3$, $\tfrac12\sigma^2=2$라 $\sigma^2=4$입니다. 미분으로도 $M_X'(0)=3$, $M_X''(0)=13$이라 분산 $13-9=4$로 일치합니다.

### 2.3 유일성과 독립합

**정의.** MGF가 존재하면 분포를 유일하게 결정합니다. 또 서로 독립인 변수들의 합의 MGF는 각 MGF의 곱입니다.

$$
M_{X+Y}(t)=M_X(t)\,M_Y(t)\ \ (X,Y\ \text{독립}),\qquad M_{aX+b}(t)=e^{bt}M_X(at)
$$

**유도.** 독립이면 $E[e^{t(X+Y)}]=E[e^{tX}e^{tY}]=E[e^{tX}]E[e^{tY}]$이라 곱이 됩니다. 선형변환은 $E[e^{t(aX+b)}]=e^{bt}E[e^{(at)X}]=e^{bt}M_X(at)$입니다.

**직관.** 합의 MGF가 알려진 분포의 MGF와 같으면, 유일성에 의해 합이 바로 그 분포임을 알 수 있습니다. 이것이 독립 정규합이 정규, 독립 포아송합이 포아송이 되는 근거입니다.

> **문제 7.** (표준) 독립인 $X\sim\text{Pois}(2)$, $Y\sim\text{Pois}(3)$의 합의 MGF로 $X+Y$의 분포를 판별하세요.
> **답.** $X+Y\sim\text{Pois}(5)$
> **풀이.** $M_{X+Y}(t)=e^{2(e^t-1)}e^{3(e^t-1)}=e^{5(e^t-1)}$입니다. 이는 $\text{Pois}(5)$의 MGF이므로 유일성에 의해 $X+Y\sim\text{Pois}(5)$입니다.

> **문제 8.** (심화) 독립인 $X\sim N(1,4)$, $Y\sim N(2,9)$의 합의 분포를 MGF로 판별하세요.
> **답.** $X+Y\sim N(3,13)$
> **풀이.** $M_X(t)=e^{t+2t^2}$, $M_Y(t)=e^{2t+4.5t^2}$입니다. 곱은 $e^{3t+6.5t^2}$이라 $\mu=3$, $\tfrac12\sigma^2=6.5$에서 $\sigma^2=13$입니다. 따라서 $X+Y\sim N(3,13)$입니다.

> **문제 9.** (표준) $M_X(t)=\dfrac{2}{2-t}$인 $X$에 대해 $Y=3X$의 MGF와 평균을 구하세요.
> **답.** $M_Y(t)=\dfrac{2}{2-3t}$, $E[Y]=\dfrac{3}{2}$
> **풀이.** $M_Y(t)=M_X(3t)=\dfrac{2}{2-3t}$입니다. $X\sim\text{Exp}(2)$라 $E[X]=\tfrac12$, $E[Y]=3E[X]=\tfrac32$입니다.

## 3. 유형 총정리(치트시트)

| 분포 | MGF | 평균 | 분산 |
|---|---|---|---|
| 베르누이 $(p)$ | $1-p+pe^t$ | $p$ | $p(1-p)$ |
| 이항 $B(n,p)$ | $(1-p+pe^t)^n$ | $np$ | $np(1-p)$ |
| 포아송 $(\lambda)$ | $e^{\lambda(e^t-1)}$ | $\lambda$ | $\lambda$ |
| 지수 $(\lambda)$ | $\dfrac{\lambda}{\lambda-t}$ | $\dfrac1\lambda$ | $\dfrac{1}{\lambda^2}$ |
| 정규 $N(\mu,\sigma^2)$ | $e^{\mu t+\frac12\sigma^2t^2}$ | $\mu$ | $\sigma^2$ |

핵심 조작은 세 가지입니다. $E[X^n]=M_X^{(n)}(0)$으로 적률을 뽑고, $M_{aX+b}(t)=e^{bt}M_X(at)$로 변환을 다루며, 독립합은 MGF의 곱으로 분포를 판별합니다.

## 4. 종합 문제 드릴

> **문제 10.** (표준) $X\sim\text{Bernoulli}(p)$의 MGF를 구하고 그것으로 평균·분산을 유도하세요.
> **답.** $M_X(t)=1-p+pe^t$, $E[X]=p$, $\operatorname{Var}(X)=p(1-p)$
> **풀이.** $M_X(t)=e^0(1-p)+e^t p=1-p+pe^t$입니다. $M_X'(t)=pe^t$이라 $M_X'(0)=p$, $M_X''(0)=p$입니다. $\operatorname{Var}(X)=p-p^2=p(1-p)$입니다.

> **문제 11.** (심화) 이항 $B(n,p)$가 독립 베르누이 $n$개의 합임을 써서 MGF가 $(1-p+pe^t)^n$임을 보이세요.
> **답.** $M_X(t)=(1-p+pe^t)^n$
> **풀이.** $X=\sum_{i=1}^n X_i$, 각 $X_i$는 독립 베르누이입니다. 독립합의 MGF는 곱이므로 $M_X(t)=\prod_{i=1}^n(1-p+pe^t)=(1-p+pe^t)^n$입니다.

> **문제 12.** (표준) 문제 11의 이항 MGF에서 $E[X]$를 미분으로 구하세요.
> **답.** $np$
> **풀이.** $M_X'(t)=n(1-p+pe^t)^{n-1}\cdot pe^t$입니다. $t=0$에서 밑이 $1$이므로 $M_X'(0)=n\cdot1\cdot p=np$입니다.

> **문제 13.** (심화) $M_X(t)=\dfrac13 e^{t}+\dfrac13 e^{2t}+\dfrac13 e^{3t}$인 $X$의 분포와 평균, 분산을 구하세요.
> **답.** $X$는 $1,2,3$을 등확률로 가짐, $E[X]=2$, $\operatorname{Var}(X)=\dfrac23$
> **풀이.** MGF의 계수가 확률이라 $p(1)=p(2)=p(3)=\tfrac13$입니다. $E[X]=\tfrac{1+2+3}{3}=2$이고 $E[X^2]=\tfrac{1+4+9}{3}=\tfrac{14}{3}$이라 $\operatorname{Var}(X)=\tfrac{14}{3}-4=\tfrac23$입니다.

> **문제 14.** (심화) 독립인 $X_i\sim\text{Exp}(\lambda)$ $n$개의 합 $S=\sum X_i$의 MGF를 구하고, 이것이 감마분포임을 밝히세요.
> **답.** $M_S(t)=\left(\dfrac{\lambda}{\lambda-t}\right)^n$, $S\sim\Gamma(n,\lambda)$
> **풀이.** 독립합이라 $M_S(t)=\prod_{i=1}^n\dfrac{\lambda}{\lambda-t}=\left(\dfrac{\lambda}{\lambda-t}\right)^n$입니다. 이는 형상 $n$, 비율 $\lambda$인 감마분포의 MGF이므로 $S\sim\Gamma(n,\lambda)$입니다.

> **문제 15.** (표준) 문제 14의 $S$에 대해 MGF로 $E[S]$와 $\operatorname{Var}(S)$를 구하세요.
> **답.** $E[S]=\dfrac{n}{\lambda}$, $\operatorname{Var}(S)=\dfrac{n}{\lambda^2}$
> **풀이.** 독립합이라 평균·분산이 그냥 $n$배입니다. $E[S]=n\cdot\tfrac1\lambda=\tfrac{n}{\lambda}$, $\operatorname{Var}(S)=n\cdot\tfrac{1}{\lambda^2}=\tfrac{n}{\lambda^2}$입니다.

> **문제 16.** (심화) $X\sim N(0,1)$의 MGF가 $e^{t^2/2}$임을 급수로 확인하고 $E[X^4]$을 구하세요.
> **답.** $E[X^4]=3$
> **풀이.** $e^{t^2/2}=1+\dfrac{t^2}{2}+\dfrac{t^4}{8}+\cdots$입니다. $E[X^4]$은 $\dfrac{t^4}{4!}$의 계수와 같으므로 $\dfrac{E[X^4]}{24}=\dfrac18$에서 $E[X^4]=3$입니다. 표준정규의 4차 적률입니다.

> **문제 17.** (표준) $M_X(t)=(0.4+0.6e^t)^5$인 $X$의 분포와 평균을 밝히세요.
> **답.** $X\sim B(5,0.6)$, $E[X]=3$
> **풀이.** $(1-p+pe^t)^n$ 꼴과 비교하면 $n=5$, $p=0.6$입니다. $E[X]=np=5\times 0.6=3$입니다.

> **문제 18.** (심화) $X$의 MGF가 $M_X(t)=\dfrac{1}{1-t^2}$ $(|t|<1)$입니다. $E[X]$와 $E[X^2]$을 구하세요.
> **답.** $E[X]=0$, $E[X^2]=2$
> **풀이.** $\dfrac{1}{1-t^2}=1+t^2+t^4+\cdots$입니다. $t$의 계수가 0이라 $E[X]=0$입니다. $t^2$의 계수는 $1=\dfrac{E[X^2]}{2!}$이라 $E[X^2]=2$입니다. 홀수 적률이 모두 0인 대칭 분포입니다.

> **문제 19.** (심화) 독립인 $X\sim N(\mu_1,\sigma_1^2)$, $Y\sim N(\mu_2,\sigma_2^2)$에 대해 $2X-Y$의 분포를 MGF로 구하세요.
> **답.** $2X-Y\sim N(2\mu_1-\mu_2,\ 4\sigma_1^2+\sigma_2^2)$
> **풀이.** $M_{2X}(t)=e^{2\mu_1 t+\frac12(4\sigma_1^2)t^2}$, $M_{-Y}(t)=e^{-\mu_2 t+\frac12\sigma_2^2t^2}$입니다. 곱은 $e^{(2\mu_1-\mu_2)t+\frac12(4\sigma_1^2+\sigma_2^2)t^2}$이라 평균 $2\mu_1-\mu_2$, 분산 $4\sigma_1^2+\sigma_2^2$입니다.

> **문제 20.** (심화) $M_X(t)=\dfrac14+\dfrac12 e^t+\dfrac14 e^{2t}$인 $X$가 독립 베르누이 두 개의 합임을 보이세요.
> **답.** $X\sim B(2,\tfrac12)$
> **풀이.** $\left(\dfrac12+\dfrac12 e^t\right)^2=\dfrac14+\dfrac12 e^t+\dfrac14 e^{2t}$로 정확히 일치합니다. 따라서 $X$는 성공확률 $\tfrac12$인 독립 베르누이 두 개의 합, 즉 $B(2,\tfrac12)$입니다.

## 5. 스스로 점검

1. MGF의 정의는?
2. $M_X(0)$은 항상 얼마인가?
3. $E[X^n]$을 MGF에서 어떻게 얻는가?
4. $M_{aX+b}(t)$는 $M_X$로 어떻게 쓰는가?
5. 독립합의 MGF는 무엇이 되는가?
6. 유일성 성질은 무엇을 보장하는가?
7. $M_X(t)=e^{5(e^t-1)}$인 $X$의 분포와 분산은?
8. $M_X(t)=(0.7+0.3e^t)^{10}$인 $X$의 평균은?

**정답.**
1. $M_X(t)=E[e^{tX}]$.
2. $E[e^0]=1$.
3. $n$번 미분해 $t=0$ 대입: $E[X^n]=M_X^{(n)}(0)$.
4. $M_{aX+b}(t)=e^{bt}M_X(at)$.
5. 각 MGF의 곱.
6. MGF가 같으면 분포가 같음을 보장합니다.
7. $\text{Pois}(5)$, 분산 $5$.
8. $B(10,0.3)$이므로 $E[X]=np=3$.
