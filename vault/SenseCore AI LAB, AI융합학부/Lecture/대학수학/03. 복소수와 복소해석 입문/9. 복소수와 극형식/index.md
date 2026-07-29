---
title: "9. 복소수와 극형식"
---
# 9강. 복소수와 극형식

복소수는 "$x^2=-1$의 해가 없다"는 실수의 한계에서 자라난 수입니다. 제곱해서 $-1$이 되는 새 수 $i$를 하나 들여오면, 방정식의 해가 갑자기 넉넉해지고 셈이 오히려 단순해집니다. 이 강의는 허수단위와 복소수의 정의에서 출발해, 사칙연산과 켤레·절댓값을 익히고, 복소수를 평면 위의 점으로 읽는 복소평면으로 넘어갑니다. 이어 절댓값과 편각으로 복소수를 적는 극형식을 세우고, 곱셈이 "크기는 곱하고 각은 더한다"는 회전으로 읽힌다는 것을 봅니다. 마지막으로 드무아브르 정리로 거듭제곱과 $n$제곱근까지 다룹니다. 여기서 익힌 기하적 그림은 10강의 오일러 공식과 11강의 복소미분으로 그대로 이어집니다.

## 이 강의에서 할 수 있게 되는 것
- 허수단위 $i$와 복소수의 실수부·허수부를 정의하고 사칙연산을 할 수 있습니다.
- 켤레복소수와 절댓값의 성질을 알고 나눗셈을 유리화로 처리할 수 있습니다.
- 복소수를 복소평면 위의 점으로 그리고 절댓값을 거리로 읽을 수 있습니다.
- 절댓값 $r$과 편각 $\theta$로 극형식 $r(\cos\theta+i\sin\theta)$을 세울 수 있습니다.
- 극형식의 곱셈·나눗셈을 "크기 곱·각 합"으로 계산할 수 있습니다.
- 드무아브르 정리로 거듭제곱을 구하고 $n$제곱근을 모두 찾을 수 있습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $i$ | 허수단위 | $i^2=-1$을 만족하는 수 |
| $z=a+bi$ | 복소수 $z$ | 실수 $a,b$에 대한 복소수, $a$는 실수부·$b$는 허수부 |
| $\operatorname{Re}z,\ \operatorname{Im}z$ | 실수부, 허수부 | $\operatorname{Re}(a+bi)=a,\ \operatorname{Im}(a+bi)=b$ |
| $\bar z$ | $z$의 켤레 | $\overline{a+bi}=a-bi$ |
| $\lvert z\rvert$ | $z$의 절댓값 | $\lvert a+bi\rvert=\sqrt{a^2+b^2}$ |
| $\arg z$ | $z$의 편각 | 양의 실수축과 이루는 각 $\theta$ |
| $r(\cos\theta+i\sin\theta)$ | 극형식 | $r=\lvert z\rvert$, $\theta=\arg z$ |
| $\operatorname{cis}\theta$ | 시스 세타 | $\cos\theta+i\sin\theta$의 줄임 표기 |

## 2. 개념

### 2.1 허수단위와 복소수의 정의

**정의.** 제곱하여 $-1$이 되는 수를 **허수단위**라 하고 $i$로 씁니다. 곧 $i^2=-1$입니다. 실수 $a,b$에 대해 $z=a+bi$ 꼴로 쓰는 수를 **복소수**라 하고, $a$를 **실수부** $\operatorname{Re}z$, $b$를 **허수부** $\operatorname{Im}z$라 합니다. $b=0$이면 실수, $a=0$이고 $b\ne0$이면 순허수입니다.

두 복소수가 같다는 것은 실수부와 허수부가 각각 같다는 뜻입니다. 곧 $a+bi=c+di$이면 $a=c$이고 $b=d$입니다. 하나의 등식이 실수 두 개의 등식으로 갈리는 이 성질을 자주 씁니다.

$i$의 거듭제곱은 네 개가 주기로 돕니다. $i^1=i$, $i^2=-1$, $i^3=-i$, $i^4=1$이고 그다음은 다시 $i^5=i$로 되돌아옵니다. 그러므로 $i^n$은 지수를 $4$로 나눈 나머지만 보면 됩니다.

직관은 "실수 직선에 없던 $\sqrt{-1}$을 새 방향으로 하나 세웠다"는 것입니다. 이 한 수를 더하면 모든 다항식이 근을 가지게 됩니다(대수학의 기본정리).

> **문제 1.** (기초) $i^{2026}$을 간단히 하십시오.
> **답.** $-1$.
> **풀이.** $i^n$은 주기 $4$입니다. $2026=4\cdot506+2$이라 $i^{2026}=i^2=-1$입니다.

> **문제 2.** (기초) $z=3-5i$의 실수부와 허수부를 쓰십시오.
> **답.** $\operatorname{Re}z=3$, $\operatorname{Im}z=-5$.
> **풀이.** $z=a+bi$ 꼴에서 $a=3$, $b=-5$입니다. 허수부는 $-5i$가 아니라 계수 $-5$임에 주의합니다.

> **문제 3.** (표준) $x,y$가 실수이고 $(x+2)+(y-3)i=5-i$이면 $x,y$를 구하십시오.
> **답.** $x=3$, $y=2$.
> **풀이.** 실수부끼리 $x+2=5$이라 $x=3$이고, 허수부끼리 $y-3=-1$이라 $y=2$입니다.

> **문제 4.** (표준) $i+i^2+i^3+\cdots+i^{100}$의 값을 구하십시오.
> **답.** $0$.
> **풀이.** 연속한 네 항 $i+i^2+i^3+i^4=i-1-i+1=0$입니다. $100$은 $4$의 배수라 이런 묶음이 $25$개이므로 총합은 $0$입니다.

### 2.2 사칙연산

**정의.** 복소수의 덧셈·뺄셈은 실수부와 허수부끼리 따로 합니다.
$$
(a+bi)\pm(c+di)=(a\pm c)+(b\pm d)i
$$
곱셈은 분배법칙을 쓰고 $i^2=-1$로 정리합니다.
$$
(a+bi)(c+di)=ac+adi+bci+bdi^2=(ac-bd)+(ad+bc)i
$$

나눗셈은 분모의 켤레를 분자·분모에 곱해 분모를 실수로 만드는 **유리화**로 합니다. $\overline{c+di}=c-di$를 곱하면 분모는 $(c+di)(c-di)=c^2+d^2$이 되어 실수가 됩니다.
$$
\frac{a+bi}{c+di}=\frac{(a+bi)(c-di)}{c^2+d^2}
$$

**예시.** $\dfrac{2+3i}{1-i}$를 계산합니다. 분모의 켤레 $1+i$를 곱하면
$$
\frac{(2+3i)(1+i)}{(1-i)(1+i)}=\frac{2+2i+3i+3i^2}{1+1}=\frac{2+5i-3}{2}=\frac{-1+5i}{2}=-\frac12+\frac52 i
$$
입니다. 검산: $\left(-\tfrac12+\tfrac52 i\right)(1-i)=-\tfrac12+\tfrac12 i+\tfrac52 i-\tfrac52 i^2=-\tfrac12+3i+\tfrac52=2+3i$로 맞습니다.

직관은 "복소수는 실수부·허수부라는 두 좌표를 가진 수여서, 더하기는 좌표별로, 곱하기는 $i^2=-1$을 섞어 계산한다"는 것입니다.

> **문제 1.** (기초) $(3+2i)+(1-5i)$를 계산하십시오.
> **답.** $4-3i$.
> **풀이.** 실수부 $3+1=4$, 허수부 $2+(-5)=-3$이라 $4-3i$입니다.

> **문제 2.** (기초) $(2+i)(3-2i)$를 계산하십시오.
> **답.** $8-i$.
> **풀이.** $6-4i+3i-2i^2=6-i+2=8-i$입니다.

> **문제 3.** (표준) $\dfrac{1}{2+i}$를 $a+bi$ 꼴로 쓰십시오.
> **답.** $\dfrac{2}{5}-\dfrac{1}{5}i$.
> **풀이.** 켤레 $2-i$를 곱하면 $\dfrac{2-i}{(2+i)(2-i)}=\dfrac{2-i}{4+1}=\dfrac{2-i}{5}=\dfrac25-\dfrac15 i$입니다. 검산: $\left(\tfrac25-\tfrac15 i\right)(2+i)=\tfrac45+\tfrac25 i-\tfrac25 i-\tfrac15 i^2=\tfrac45+\tfrac15=1$로 맞습니다.

> **문제 4.** (표준) $(1+i)^2$과 $(1+i)^4$를 구하십시오.
> **답.** $(1+i)^2=2i$, $(1+i)^4=-4$.
> **풀이.** $(1+i)^2=1+2i+i^2=2i$입니다. 이를 제곱하면 $(2i)^2=4i^2=-4$입니다.

> **문제 5.** (심화) $z=a+bi$($b\ne0$)가 $z+\dfrac1z$가 실수가 되려면 $\lvert z\rvert=1$이어야 함을 보이십시오.
> **답.** $\dfrac1z=\dfrac{\bar z}{\lvert z\rvert^2}$이라 허수부가 $b\left(1-\tfrac1{\lvert z\rvert^2}\right)$이고, 이것이 $0$이려면 $\lvert z\rvert=1$입니다.
> **풀이.** $\dfrac1z=\dfrac{\bar z}{\lvert z\rvert^2}=\dfrac{a-bi}{a^2+b^2}$입니다. 그러면 $z+\dfrac1z=\left(a+\dfrac{a}{a^2+b^2}\right)+\left(b-\dfrac{b}{a^2+b^2}\right)i$입니다. 실수가 되려면 허수부 $b\left(1-\dfrac{1}{a^2+b^2}\right)=0$이어야 하고, $b\ne0$이므로 $a^2+b^2=1$, 곧 $\lvert z\rvert=1$입니다. $\square$

### 2.3 켤레복소수와 절댓값

**정의.** $z=a+bi$의 **켤레복소수**는 $\bar z=a-bi$입니다. **절댓값**(크기)은
$$
\lvert z\rvert=\sqrt{a^2+b^2}
$$
이며, 원점에서 $z$까지의 거리입니다.

**주요 성질.** 다음이 성립합니다.
$$
z\bar z=a^2+b^2=\lvert z\rvert^2,\qquad \overline{z+w}=\bar z+\bar w,\qquad \overline{zw}=\bar z\,\bar w
$$
$$
\lvert zw\rvert=\lvert z\rvert\lvert w\rvert,\qquad \left\lvert\frac zw\right\rvert=\frac{\lvert z\rvert}{\lvert w\rvert},\qquad \operatorname{Re}z=\frac{z+\bar z}{2},\quad \operatorname{Im}z=\frac{z-\bar z}{2i}
$$
특히 $z\bar z=\lvert z\rvert^2$은 나눗셈 유리화의 근거이자, $z$가 실수일 필요충분조건이 $z=\bar z$임을 줍니다.

**삼각부등식.** $\lvert z+w\rvert\le\lvert z\rvert+\lvert w\rvert$입니다. 두 벡터의 합의 길이가 각 길이의 합을 넘지 못한다는 기하 사실의 복소수판입니다.

**예시.** $z=3+4i$이면 $\lvert z\rvert=\sqrt{9+16}=5$이고 $z\bar z=(3+4i)(3-4i)=9-16i^2=9+16=25=\lvert z\rvert^2$로 성질이 확인됩니다.

직관은 "켤레는 실수축에 대한 거울반사, 절댓값은 원점까지의 거리"라는 것입니다.

> **문제 1.** (기초) $z=5-12i$의 절댓값을 구하십시오.
> **답.** $13$.
> **풀이.** $\lvert z\rvert=\sqrt{5^2+(-12)^2}=\sqrt{25+144}=\sqrt{169}=13$입니다.

> **문제 2.** (기초) $\overline{(2+3i)(1-i)}$를 구하십시오.
> **답.** $5-i$.
> **풀이.** 먼저 $(2+3i)(1-i)=2-2i+3i-3i^2=5+i$이라 켤레는 $5-i$입니다. 또는 $\overline{zw}=\bar z\bar w=(2-3i)(1+i)=5-i$로도 같습니다.

> **문제 3.** (표준) $\lvert z\rvert=1$이면 $\dfrac1z=\bar z$임을 보이십시오.
> **답.** $z\bar z=\lvert z\rvert^2=1$이라 $\dfrac1z=\bar z$입니다.
> **풀이.** 절댓값이 $1$이면 $z\bar z=\lvert z\rvert^2=1$입니다. 양변을 $z$로 나누면 $\bar z=\dfrac1z$입니다. 단위원 위의 복소수는 역수가 켤레와 같다는 유용한 성질입니다.

> **문제 4.** (표준) $\lvert z\rvert^2=z\bar z$를 이용해 $\lvert zw\rvert=\lvert z\rvert\lvert w\rvert$를 증명하십시오.
> **답.** $\lvert zw\rvert^2=zw\overline{zw}=z\bar z\cdot w\bar w=\lvert z\rvert^2\lvert w\rvert^2$이라 양의 제곱근을 취하면 됩니다.
> **풀이.** $\lvert zw\rvert^2=(zw)\overline{(zw)}=(zw)(\bar z\bar w)=(z\bar z)(w\bar w)=\lvert z\rvert^2\lvert w\rvert^2$입니다. 절댓값은 음이 아니므로 양의 제곱근을 취하면 $\lvert zw\rvert=\lvert z\rvert\lvert w\rvert$입니다. $\square$

> **문제 5.** (심화) $\lvert z\rvert=\lvert w\rvert=1$이고 $1+zw\ne0$이면 $\dfrac{z+w}{1+zw}$가 실수임을 보이십시오.
> **답.** 그 켤레가 자기 자신과 같음을 보이면 됩니다.
> **풀이.** $\lvert z\rvert=1$이라 $\bar z=\dfrac1z$, 마찬가지로 $\bar w=\dfrac1w$입니다. $u=\dfrac{z+w}{1+zw}$의 켤레는 $\bar u=\dfrac{\bar z+\bar w}{1+\bar z\bar w}=\dfrac{\frac1z+\frac1w}{1+\frac1{zw}}$입니다. 분자·분모에 $zw$를 곱하면 $\bar u=\dfrac{w+z}{zw+1}=u$입니다. $\bar u=u$이므로 $u$는 실수입니다. $\square$

### 2.4 복소평면

**정의.** 복소수 $z=a+bi$를 좌표평면의 점 $(a,b)$에 대응시킨 평면을 **복소평면**(또는 가우스 평면)이라 합니다. 가로축을 실수축, 세로축을 허수축이라 합니다. 이때 $\lvert z\rvert$는 원점에서 점까지의 거리, $\lvert z-w\rvert$는 두 점 사이의 거리입니다.

덧셈은 벡터의 합처럼 평행이동으로 보입니다. $z$에 $w$를 더하는 것은 점 $z$를 벡터 $w$만큼 옮기는 것입니다. 켤레 $\bar z$는 점 $z$를 실수축에 대해 뒤집은 점입니다.

**예시.** $\lvert z-1\rvert=2$를 만족하는 $z$의 자취는 점 $1$(곧 $(1,0)$)에서 거리가 $2$인 점들이므로 중심 $(1,0)$, 반지름 $2$인 원입니다. 이렇게 복소수 방정식은 곧바로 도형이 됩니다.

직관은 "복소수는 평면 위의 점이자 화살표(벡터)"라는 것입니다. 대수 계산이 그대로 기하 도형으로 번역됩니다.

> **문제 1.** (기초) 두 점 $z_1=1+2i$, $z_2=4+6i$ 사이의 거리를 구하십시오.
> **답.** $5$.
> **풀이.** 거리는 $\lvert z_2-z_1\rvert=\lvert3+4i\rvert=\sqrt{9+16}=5$입니다.

> **문제 2.** (표준) $\lvert z-i\rvert=\lvert z+i\rvert$를 만족하는 $z$의 자취를 구하십시오.
> **답.** 실수축(곧 $\operatorname{Im}z=0$).
> **풀이.** 점 $i=(0,1)$과 점 $-i=(0,-1)$에서 같은 거리에 있는 점들이므로 두 점의 수직이등분선, 곧 실수축입니다. 대수로 확인하면 $z=x+yi$에서 $x^2+(y-1)^2=x^2+(y+1)^2$이라 $-2y=2y$, 곧 $y=0$입니다.

> **문제 3.** (표준) $\lvert z-2\rvert\le1$이 나타내는 영역을 말로 설명하십시오.
> **답.** 중심 $(2,0)$, 반지름 $1$인 원의 내부와 경계(닫힌 원판).
> **풀이.** $\lvert z-2\rvert$는 점 $z$에서 점 $2=(2,0)$까지의 거리입니다. 이것이 $1$ 이하인 점들은 중심 $(2,0)$, 반지름 $1$인 닫힌 원판을 이룹니다.

### 2.5 극형식과 편각

**정의.** $0$이 아닌 복소수 $z$는 절댓값 $r=\lvert z\rvert$과 편각 $\theta=\arg z$로
$$
z=r(\cos\theta+i\sin\theta)
$$
로 쓸 수 있습니다. 이를 **극형식**이라 합니다. $\cos\theta+i\sin\theta$를 줄여 $\operatorname{cis}\theta$로도 씁니다. 직교형식 $a+bi$와의 관계는
$$
a=r\cos\theta,\quad b=r\sin\theta,\qquad r=\sqrt{a^2+b^2},\quad \tan\theta=\frac ba
$$
입니다. 편각은 $2\pi$의 정수배만큼 여러 값을 가지므로, 보통 $-\pi<\theta\le\pi$인 값을 **주편각** $\operatorname{Arg}z$로 삼습니다.

**주의:** $\tan\theta=\dfrac ba$만으로 편각을 정하면 안 됩니다. 점이 어느 사분면에 있는지를 보고 각을 맞춰야 합니다. 예컨대 $-1-i$는 $\tan\theta=1$이지만 제3사분면이라 $\theta=-\dfrac{3\pi}{4}$입니다($\dfrac\pi4$가 아님).

**예시.** $z=1+\sqrt3\,i$의 극형식을 구합니다. $r=\sqrt{1+3}=2$이고 점 $(1,\sqrt3)$은 제1사분면이라 $\theta=\dfrac\pi3$입니다. 곧 $z=2\left(\cos\dfrac\pi3+i\sin\dfrac\pi3\right)$입니다. 검산: $2\cos\dfrac\pi3=2\cdot\dfrac12=1$, $2\sin\dfrac\pi3=2\cdot\dfrac{\sqrt3}{2}=\sqrt3$로 맞습니다.

직관은 "복소수를 원점에서의 거리 $r$과 방향 각 $\theta$로 적는다"는 것입니다. 곱셈의 정체가 여기서 드러납니다.

> **문제 1.** (기초) $z=-2$의 극형식을 구하십시오($-\pi<\theta\le\pi$).
> **답.** $2(\cos\pi+i\sin\pi)$.
> **풀이.** $\lvert z\rvert=2$이고 점 $(-2,0)$은 음의 실수축 위라 편각은 $\pi$입니다.

> **문제 2.** (기초) $z=\sqrt3-i$의 절댓값과 주편각을 구하십시오.
> **답.** $r=2$, $\theta=-\dfrac\pi6$.
> **풀이.** $r=\sqrt{3+1}=2$입니다. 점 $(\sqrt3,-1)$은 제4사분면이고 $\tan\theta=\dfrac{-1}{\sqrt3}$이라 $\theta=-\dfrac\pi6$입니다.

> **문제 3.** (표준) 극형식 $z=4\left(\cos\dfrac{2\pi}{3}+i\sin\dfrac{2\pi}{3}\right)$을 직교형식으로 바꾸십시오.
> **답.** $-2+2\sqrt3\,i$.
> **풀이.** $\cos\dfrac{2\pi}{3}=-\dfrac12$, $\sin\dfrac{2\pi}{3}=\dfrac{\sqrt3}{2}$이라 $z=4\left(-\dfrac12+\dfrac{\sqrt3}{2}i\right)=-2+2\sqrt3\,i$입니다.

> **문제 4.** (표준) $z=-1-i$의 극형식을 구하십시오($-\pi<\theta\le\pi$).
> **답.** $\sqrt2\left(\cos\left(-\dfrac{3\pi}{4}\right)+i\sin\left(-\dfrac{3\pi}{4}\right)\right)$.
> **풀이.** $r=\sqrt{1+1}=\sqrt2$입니다. 점 $(-1,-1)$은 제3사분면이라 편각은 $\pi+\dfrac\pi4=\dfrac{5\pi}{4}$이고, 주편각으로는 $-\dfrac{3\pi}{4}$입니다.

### 2.6 극형식의 곱셈과 드무아브르 정리

**곱셈·나눗셈.** $z_1=r_1(\cos\theta_1+i\sin\theta_1)$, $z_2=r_2(\cos\theta_2+i\sin\theta_2)$이면
$$
z_1z_2=r_1r_2\big(\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\big)
$$
$$
\frac{z_1}{z_2}=\frac{r_1}{r_2}\big(\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)\big)
$$
입니다. 곧 **곱셈은 크기를 곱하고 각을 더하며, 나눗셈은 크기를 나누고 각을 뺍니다.** 유도는 곱을 전개한 뒤 삼각함수의 덧셈정리 $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$, $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$를 쓰면 됩니다.

**드무아브르 정리.** 같은 복소수를 반복해서 곱하면
$$
\big(r(\cos\theta+i\sin\theta)\big)^n=r^n(\cos n\theta+i\sin n\theta)
$$
입니다. 곧 거듭제곱은 크기를 거듭제곱하고 각을 $n$배 합니다. 정수 $n$(음수 포함)에서 성립합니다.

**예시.** $(1+i)^8$을 구합니다. $1+i=\sqrt2\left(\cos\dfrac\pi4+i\sin\dfrac\pi4\right)$이므로 드무아브르로
$$
(1+i)^8=(\sqrt2)^8\left(\cos 8\cdot\tfrac\pi4+i\sin 8\cdot\tfrac\pi4\right)=16(\cos 2\pi+i\sin 2\pi)=16
$$
입니다. 직교형식으로 여덟 번 곱하는 것보다 훨씬 빠릅니다. 검산: $(1+i)^2=2i$, $(2i)^4=16i^4=16$로 맞습니다.

직관은 "복소수 곱셈은 회전과 확대의 합성"이라는 것입니다. 단위복소수 $\cos\theta+i\sin\theta$를 곱하는 것은 각 $\theta$만큼 회전시키는 것입니다.

> **문제 1.** (기초) $2\operatorname{cis}\dfrac\pi6$과 $3\operatorname{cis}\dfrac\pi3$의 곱을 극형식으로 쓰십시오.
> **답.** $6\operatorname{cis}\dfrac\pi2$(곧 $6i$).
> **풀이.** 크기는 $2\cdot3=6$, 각은 $\dfrac\pi6+\dfrac\pi3=\dfrac\pi2$이라 $6\operatorname{cis}\dfrac\pi2=6i$입니다.

> **문제 2.** (기초) $i$를 곱하는 것이 기하적으로 무엇인지 설명하십시오.
> **답.** 원점을 중심으로 반시계방향 $90^\circ$ 회전.
> **풀이.** $i=\operatorname{cis}\dfrac\pi2$이라 크기 $1$, 각 $\dfrac\pi2$입니다. 곱하면 크기는 그대로, 각만 $\dfrac\pi2$(=$90^\circ$) 더해지므로 반시계방향 $90^\circ$ 회전입니다.

> **문제 3.** (표준) 드무아브르 정리로 $(\sqrt3+i)^6$을 구하십시오.
> **답.** $-64$.
> **풀이.** $\sqrt3+i=2\operatorname{cis}\dfrac\pi6$입니다. $(\ )^6=2^6\operatorname{cis}\dfrac{6\pi}{6}=64\operatorname{cis}\pi=64(-1)=-64$입니다.

> **문제 4.** (표준) $\left(\dfrac{1+i}{1-i}\right)^{2026}$을 구하십시오.
> **답.** $-1$.
> **풀이.** $\dfrac{1+i}{1-i}=\dfrac{(1+i)^2}{(1-i)(1+i)}=\dfrac{2i}{2}=i$입니다. 따라서 $i^{2026}=i^2=-1$입니다.

> **문제 5.** (심화) $z=r\operatorname{cis}\theta$($r>0$)의 역수 $\dfrac1z$를 극형식으로 쓰고, 곱셈규칙과 어긋나지 않음을 보이십시오.
> **답.** $\dfrac1z=\dfrac1r\operatorname{cis}(-\theta)$.
> **풀이.** 나눗셈규칙에서 $\dfrac1z=\dfrac{1\cdot\operatorname{cis}0}{r\operatorname{cis}\theta}=\dfrac1r\operatorname{cis}(0-\theta)=\dfrac1r\operatorname{cis}(-\theta)$입니다. 검산으로 $z\cdot\dfrac1z=r\cdot\dfrac1r\operatorname{cis}(\theta-\theta)=1\cdot\operatorname{cis}0=1$이라 실제로 역수가 맞습니다. 크기는 역수, 각은 부호가 바뀝니다. $\square$

### 2.7 복소수의 $n$제곱근

**정의.** $w^n=z$를 만족하는 $w$를 $z$의 **$n$제곱근**이라 합니다. $z=r\operatorname{cis}\theta$($z\ne0$)이면 서로 다른 $n$제곱근이 정확히 $n$개 있고
$$
w_k=r^{1/n}\left(\cos\frac{\theta+2\pi k}{n}+i\sin\frac{\theta+2\pi k}{n}\right),\qquad k=0,1,\dots,n-1
$$
로 주어집니다. 근거는 드무아브르입니다. $w=\rho\operatorname{cis}\varphi$로 두면 $w^n=\rho^n\operatorname{cis}(n\varphi)=r\operatorname{cis}\theta$여야 하므로 $\rho=r^{1/n}$이고 $n\varphi=\theta+2\pi k$, 곧 $\varphi=\dfrac{\theta+2\pi k}{n}$입니다.

기하적으로 $n$개의 근은 모두 크기가 $r^{1/n}$이라 반지름 $r^{1/n}$인 원 위에 있고, 각이 $\dfrac{2\pi}{n}$씩 벌어진 **정$n$각형의 꼭짓점**을 이룹니다. 특히 $1$의 $n$제곱근을 **$1$의 원시근(단위근)**이라 하며, $w_k=\operatorname{cis}\dfrac{2\pi k}{n}$로 단위원을 $n$등분합니다.

**예시.** $1$의 세제곱근을 모두 구합니다. $z=1=\operatorname{cis}0$, $n=3$이라
$$
w_k=\operatorname{cis}\frac{2\pi k}{3},\quad k=0,1,2
$$
곧 $w_0=1$, $w_1=\operatorname{cis}\dfrac{2\pi}{3}=-\dfrac12+\dfrac{\sqrt3}{2}i$, $w_2=\operatorname{cis}\dfrac{4\pi}{3}=-\dfrac12-\dfrac{\sqrt3}{2}i$입니다. 검산: 세 근의 합은 $0$이고(정삼각형 대칭), 곱은 $1$입니다. 또 $w_1^3=\operatorname{cis}2\pi=1$로 맞습니다.

직관은 "$n$제곱근은 크기를 $n$제곱근으로 줄이고 각을 $n$등분하되, 한 바퀴를 $n$갈래로 나눠 $n$개가 나온다"는 것입니다.

> **문제 1.** (기초) $9$의 제곱근을 복소수 범위에서 모두 구하십시오.
> **답.** $3$과 $-3$.
> **풀이.** $9=9\operatorname{cis}0$, $n=2$이라 $w_k=3\operatorname{cis}\dfrac{2\pi k}{2}$, $k=0,1$입니다. $w_0=3\operatorname{cis}0=3$, $w_1=3\operatorname{cis}\pi=-3$입니다.

> **문제 2.** (기초) $-4$의 제곱근을 모두 구하십시오.
> **답.** $2i$와 $-2i$.
> **풀이.** $-4=4\operatorname{cis}\pi$이라 $w_k=2\operatorname{cis}\dfrac{\pi+2\pi k}{2}$입니다. $k=0$이면 $2\operatorname{cis}\dfrac\pi2=2i$, $k=1$이면 $2\operatorname{cis}\dfrac{3\pi}{2}=-2i$입니다. 검산: $(2i)^2=-4$로 맞습니다.

> **문제 3.** (표준) $1$의 네제곱근을 모두 구하고 복소평면에서의 배치를 말하십시오.
> **답.** $1,\ i,\ -1,\ -i$(단위원 위 정사각형 꼭짓점).
> **풀이.** $w_k=\operatorname{cis}\dfrac{2\pi k}{4}=\operatorname{cis}\dfrac{\pi k}{2}$, $k=0,1,2,3$이라 $1,i,-1,-i$입니다. 반지름 $1$인 원 위에서 $90^\circ$씩 벌어진 정사각형을 이룹니다.

> **문제 4.** (표준) $8i$의 세제곱근 중 하나를 구하십시오.
> **답.** 예: $\sqrt3+i$($=2\operatorname{cis}\dfrac\pi6$).
> **풀이.** $8i=8\operatorname{cis}\dfrac\pi2$입니다. $w_k=8^{1/3}\operatorname{cis}\dfrac{\pi/2+2\pi k}{3}=2\operatorname{cis}\dfrac{\pi/2+2\pi k}{3}$입니다. $k=0$이면 $2\operatorname{cis}\dfrac\pi6=2\left(\dfrac{\sqrt3}{2}+\dfrac12 i\right)=\sqrt3+i$입니다. 검산: $(\sqrt3+i)^3=(2\operatorname{cis}\tfrac\pi6)^3=8\operatorname{cis}\tfrac\pi2=8i$로 맞습니다.

## 3. 유형 총정리(치트시트)

| 상황 | 도구 | 핵심 식 |
|---|---|---|
| $i^n$ 계산 | 주기 4 | 지수를 $4$로 나눈 나머지만 봄 |
| 복소수 곱 | 분배 $+\ i^2=-1$ | $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$ |
| 나눗셈 | 켤레로 유리화 | $\dfrac{z}{w}=\dfrac{z\bar w}{\lvert w\rvert^2}$ |
| 절댓값 | 거리 | $\lvert a+bi\rvert=\sqrt{a^2+b^2}$, $z\bar z=\lvert z\rvert^2$ |
| 직교↔극 | 좌표 변환 | $a=r\cos\theta,\ b=r\sin\theta$, 사분면으로 각 확정 |
| 극형식 곱·나눗 | 크기·각 | 곱은 $r_1r_2\operatorname{cis}(\theta_1+\theta_2)$, 나눗은 각 차 |
| 거듭제곱 | 드무아브르 | $(r\operatorname{cis}\theta)^n=r^n\operatorname{cis}(n\theta)$ |
| $n$제곱근 | 각 $n$등분 | $w_k=r^{1/n}\operatorname{cis}\dfrac{\theta+2\pi k}{n},\ k=0,\dots,n-1$ |

핵심 습관: (1) 나눗셈은 분모의 켤레를 곱해 유리화한다. (2) 편각은 반드시 사분면을 보고 정한다($\tan$만으로 정하지 않는다). (3) 큰 거듭제곱은 극형식으로 바꿔 드무아브르를 쓴다. (4) $n$제곱근은 빠짐없이 $n$개를 $k=0,\dots,n-1$로 나열한다. (5) 결과는 직교형식으로 되돌려 검산한다.

## 4. 종합 문제 드릴

> **문제 1.** (기초) $(4-3i)-(1+2i)$를 계산하십시오.
> **답.** $3-5i$.
> **풀이.** 실수부 $4-1=3$, 허수부 $-3-2=-5$이라 $3-5i$입니다.

> **문제 2.** (기초) $\dfrac{3+i}{1+i}$를 $a+bi$ 꼴로 쓰십시오.
> **답.** $2-i$.
> **풀이.** 켤레 $1-i$를 곱하면 $\dfrac{(3+i)(1-i)}{2}=\dfrac{3-3i+i-i^2}{2}=\dfrac{4-2i}{2}=2-i$입니다. 검산: $(2-i)(1+i)=2+2i-i-i^2=3+i$로 맞습니다.

> **문제 3.** (기초) $\lvert(3+4i)(1-2i)\rvert$를 절댓값 성질로 구하십시오.
> **답.** $5\sqrt5$.
> **풀이.** $\lvert zw\rvert=\lvert z\rvert\lvert w\rvert=\sqrt{9+16}\cdot\sqrt{1+4}=5\cdot\sqrt5=5\sqrt5$입니다.

> **문제 4.** (표준) $z=-\sqrt3+i$의 극형식을 구하십시오($-\pi<\theta\le\pi$).
> **답.** $2\operatorname{cis}\dfrac{5\pi}{6}$.
> **풀이.** $r=\sqrt{3+1}=2$입니다. 점 $(-\sqrt3,1)$은 제2사분면이고 참조각이 $\dfrac\pi6$($\tan=\dfrac1{\sqrt3}$)이라 편각은 $\pi-\dfrac\pi6=\dfrac{5\pi}{6}$입니다.

> **문제 5.** (표준) 드무아브르로 $(-1+i)^{10}$을 구하십시오.
> **답.** $-32i$.
> **풀이.** $-1+i=\sqrt2\operatorname{cis}\dfrac{3\pi}{4}$입니다. $(\ )^{10}=(\sqrt2)^{10}\operatorname{cis}\dfrac{30\pi}{4}=32\operatorname{cis}\dfrac{15\pi}{2}$입니다. 각에서 $2\pi$의 배수를 빼면 $\dfrac{15\pi}{2}-6\pi=\dfrac{3\pi}{2}$이라 $\operatorname{cis}\dfrac{3\pi}{2}=-i$입니다. 따라서 $32\cdot(-i)=-32i$입니다. 검산: $(-1+i)^2=1-2i+i^2=-2i$이고 $((-1+i)^2)^5=(-2i)^5=-32i^5=-32i$로 맞습니다.

> **문제 6.** (표준) $27$의 세제곱근을 복소수 범위에서 모두 구하십시오.
> **답.** $3,\ -\dfrac32+\dfrac{3\sqrt3}{2}i,\ -\dfrac32-\dfrac{3\sqrt3}{2}i$.
> **풀이.** $27=27\operatorname{cis}0$이라 $w_k=3\operatorname{cis}\dfrac{2\pi k}{3}$입니다. $k=0$이면 $3$, $k=1$이면 $3\operatorname{cis}\dfrac{2\pi}{3}=3\left(-\dfrac12+\dfrac{\sqrt3}{2}i\right)=-\dfrac32+\dfrac{3\sqrt3}{2}i$, $k=2$이면 켤레인 $-\dfrac32-\dfrac{3\sqrt3}{2}i$입니다.

> **문제 7.** (표준) $\lvert z-1\rvert=\lvert z-i\rvert$의 자취를 직선의 방정식으로 구하십시오.
> **답.** $y=x$.
> **풀이.** 점 $1=(1,0)$과 점 $i=(0,1)$에서 같은 거리인 점들이므로 두 점을 잇는 선분의 수직이등분선입니다. $z=x+yi$에서 $(x-1)^2+y^2=x^2+(y-1)^2$이라 $-2x+1=-2y+1$, 곧 $y=x$입니다.

> **문제 8.** (표준) $z+\bar z=6$이고 $z\bar z=13$일 때 $z$를 구하십시오.
> **답.** $z=3\pm2i$.
> **풀이.** $z=a+bi$로 두면 $z+\bar z=2a=6$이라 $a=3$입니다. $z\bar z=a^2+b^2=9+b^2=13$이라 $b^2=4$, 곧 $b=\pm2$입니다. 따라서 $z=3+2i$ 또는 $3-2i$입니다.

> **문제 9.** (심화) $-16$의 네제곱근을 모두 구하십시오.
> **답.** $\sqrt2(1+i),\ \sqrt2(-1+i),\ \sqrt2(-1-i),\ \sqrt2(1-i)$.
> **풀이.** $-16=16\operatorname{cis}\pi$이라 $w_k=16^{1/4}\operatorname{cis}\dfrac{\pi+2\pi k}{4}=2\operatorname{cis}\dfrac{\pi+2\pi k}{4}$입니다. $k=0$: $2\operatorname{cis}\dfrac\pi4=2\left(\dfrac{\sqrt2}{2}+\dfrac{\sqrt2}{2}i\right)=\sqrt2+\sqrt2 i$. $k=1$: $2\operatorname{cis}\dfrac{3\pi}{4}=-\sqrt2+\sqrt2 i$. $k=2$: $2\operatorname{cis}\dfrac{5\pi}{4}=-\sqrt2-\sqrt2 i$. $k=3$: $2\operatorname{cis}\dfrac{7\pi}{4}=\sqrt2-\sqrt2 i$. 네 근이 반지름 $2$인 원 위 정사각형을 이룹니다.

> **문제 10.** (심화) $1$의 다섯제곱근의 합이 $0$임을 보이십시오.
> **답.** 등비수열의 합 공식으로 $\dfrac{w^5-1}{w-1}=0$이 되기 때문입니다.
> **풀이.** $1$의 다섯제곱근은 $\zeta_k=\operatorname{cis}\dfrac{2\pi k}{5}$, $k=0,\dots,4$입니다. $\omega=\operatorname{cis}\dfrac{2\pi}{5}$로 두면 근은 $1,\omega,\omega^2,\omega^3,\omega^4$입니다. 등비수열 합으로 $1+\omega+\omega^2+\omega^3+\omega^4=\dfrac{\omega^5-1}{\omega-1}$인데 $\omega^5=\operatorname{cis}2\pi=1$이라 분자가 $0$이고 $\omega\ne1$이라 합이 $0$입니다. 기하적으로는 정오각형의 꼭짓점 벡터들이 대칭이라 상쇄됩니다. $\square$

> **문제 11.** (심화) $z^2=3+4i$를 만족하는 $z$를 극형식 없이 직교형식으로 구하십시오.
> **답.** $z=\pm(2+i)$.
> **풀이.** $z=x+yi$로 두면 $z^2=x^2-y^2+2xyi=3+4i$입니다. 실수부에서 $x^2-y^2=3$, 허수부에서 $2xy=4$, 곧 $xy=2$입니다. 또 $\lvert z\rvert^2=\lvert z^2\rvert^{1/1}$... 절댓값을 쓰면 $x^2+y^2=\lvert3+4i\rvert=5$입니다. $x^2-y^2=3$과 $x^2+y^2=5$를 더하면 $2x^2=8$이라 $x^2=4$, 빼면 $y^2=1$입니다. $xy=2>0$이라 부호가 같으므로 $z=2+i$ 또는 $z=-2-i$입니다. 검산: $(2+i)^2=4+4i+i^2=3+4i$로 맞습니다.

> **문제 12.** (심화) $\lvert z\rvert=2$이고 $\arg z=\dfrac\pi3$일 때 $z^3+\dfrac{8}{z^3}$을 구하십시오.
> **답.** $-9$.
> **풀이.** $z=2\operatorname{cis}\dfrac\pi3$이라 $z^3=2^3\operatorname{cis}\pi=8\cdot(-1)=-8$입니다. 그러면 $\dfrac{8}{z^3}=\dfrac{8}{-8}=-1$이라 $z^3+\dfrac{8}{z^3}=-8+(-1)=-9$입니다.

## 5. 스스로 점검

1. $i^n$을 주기 $4$로 정리하고 복소수의 사칙연산·유리화를 할 수 있는가?
2. 켤레·절댓값의 성질($z\bar z=\lvert z\rvert^2$, $\lvert zw\rvert=\lvert z\rvert\lvert w\rvert$)을 증명에 쓸 수 있는가?
3. 복소수를 복소평면 위의 점·벡터로 그리고 절댓값을 거리로 읽는가?
4. 직교형식과 극형식을 오가며 편각을 사분면으로 정확히 정하는가?
5. 극형식 곱셈을 "크기 곱·각 합"으로, 곱셈을 회전으로 이해하는가?
6. 드무아브르 정리로 거듭제곱을 계산하는가?
7. $n$제곱근을 $n$개 모두 구하고 정$n$각형 배치를 설명하는가?

정답 요지: (1) 지수를 $4$로 나눈 나머지로 $i^n$을, 나눗셈은 켤레로 유리화. (2) $z\bar z=\lvert z\rvert^2$에서 절댓값 성질이 따라 나옴. (3) $\lvert z-w\rvert$는 두 점 거리, 덧셈은 평행이동. (4) $r=\sqrt{a^2+b^2}$, 각은 $\tan\theta=\dfrac ba$에 사분면 보정. (5) $r_1r_2\operatorname{cis}(\theta_1+\theta_2)$, 단위복소수 곱은 회전. (6) $(r\operatorname{cis}\theta)^n=r^n\operatorname{cis}(n\theta)$. (7) $w_k=r^{1/n}\operatorname{cis}\dfrac{\theta+2\pi k}{n}$, $k=0,\dots,n-1$로 정$n$각형.
