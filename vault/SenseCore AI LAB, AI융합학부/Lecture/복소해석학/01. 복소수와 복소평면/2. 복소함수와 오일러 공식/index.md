---
title: "2. 복소함수와 오일러 공식"
---
# 2강. 복소함수와 오일러 공식

1강에서 극형식 $r(\cos\theta+i\sin\theta)$의 곱셈이 각의 덧셈으로 나타난다는 것을 보았습니다. 각을 더하면 곱이 된다는 이 성질은 정확히 지수함수의 성질입니다. 그래서 "$\cos\theta+i\sin\theta$가 실은 어떤 지수 $e^{i\theta}$가 아닐까" 하는 물음이 자연스럽게 생깁니다. 이 강의는 그 답인 **오일러 공식** $e^{i\theta}=\cos\theta+i\sin\theta$를 급수로 유도하고, 이를 이용해 극형식을 훨씬 짧게 쓰며, 삼각함수 항등식을 지수 계산으로 뽑아내는 법을 익힙니다. 이어 복소지수 $e^z$와 복소로그 $\log z$를 정의하고, 이 정의들이 왜 여러 값을 가지는지를 봅니다. 마지막으로 오일러 공식으로 드무아브르와 $n$제곱근을 다시 한 줄로 정리합니다. 여기서 세운 $e^{i\theta}$의 언어는 3강의 복소미분에서 그대로 쓰입니다.

## 이 강의에서 할 수 있게 되는 것
- 지수·삼각함수의 급수로 오일러 공식 $e^{i\theta}=\cos\theta+i\sin\theta$를 유도할 수 있습니다.
- 극형식을 $re^{i\theta}$로 간단히 쓰고 곱셈·거듭제곱을 지수법칙으로 처리할 수 있습니다.
- 오일러 공식으로 $\cos\theta,\sin\theta$를 지수로 표현하고 삼각항등식을 유도할 수 있습니다.
- 복소지수 $e^{z}=e^{x}(\cos y+i\sin y)$의 값을 계산할 수 있습니다.
- 복소로그 $\log z=\ln\lvert z\rvert+i\arg z$가 여러 값을 가짐을 이해하고 주값을 구할 수 있습니다.
- 오일러 공식으로 드무아브르 정리와 $n$제곱근을 재정리할 수 있습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $e^{i\theta}$ | 복소지수 | $\cos\theta+i\sin\theta$(오일러 공식) |
| $re^{i\theta}$ | 극형식(지수꼴) | 절댓값 $r$, 편각 $\theta$인 복소수 |
| $e^{z}$ | 복소지수함수 | $z=x+iy$에서 $e^x(\cos y+i\sin y)$ |
| $\ln$ | 자연로그(실수) | 양의 실수에 대한 실로그 |
| $\log z$ | 복소로그 | $\ln\lvert z\rvert+i\arg z$(다가) |
| $\operatorname{Log}z$ | 주로그 | $\ln\lvert z\rvert+i\operatorname{Arg}z$, $-\pi<\operatorname{Arg}z\le\pi$ |
| $\overline{e^{i\theta}}$ | 켤레 | $e^{-i\theta}$ |

## 2. 개념

### 2.1 오일러 공식의 유도

**정리(오일러 공식).** 실수 $\theta$에 대해
$$
e^{i\theta}=\cos\theta+i\sin\theta
$$
가 성립합니다.

**급수에 의한 유도.** 지수·코사인·사인은 다음 멱급수로 정의됩니다.
$$
e^{x}=\sum_{n=0}^{\infty}\frac{x^n}{n!},\quad \cos\theta=\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k}}{(2k)!},\quad \sin\theta=\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}
$$
$e^{x}$의 급수에 $x=i\theta$를 넣습니다. $i$의 거듭제곱이 $1,i,-1,-i$를 주기로 돌므로 짝수 차수 항과 홀수 차수 항으로 갈라집니다.
$$
e^{i\theta}=\sum_{n=0}^{\infty}\frac{(i\theta)^n}{n!}=\underbrace{\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k}}{(2k)!}}_{\cos\theta}+i\underbrace{\sum_{k=0}^{\infty}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}}_{\sin\theta}
$$
짝수 차수 $i^{2k}=(-1)^k$는 실수부로 모여 $\cos\theta$가 되고, 홀수 차수 $i^{2k+1}=(-1)^k i$는 허수부로 모여 $i\sin\theta$가 됩니다. 그래서 $e^{i\theta}=\cos\theta+i\sin\theta$입니다.

특히 $\theta=\pi$를 넣으면 $e^{i\pi}=\cos\pi+i\sin\pi=-1$, 곧 그 유명한
$$
e^{i\pi}+1=0
$$
을 얻습니다. 다섯 개의 기본 상수 $e,i,\pi,1,0$을 한 식에 담은 오일러 항등식입니다.

직관은 "각을 더하면 곱이 되는 성질을 가진 것은 지수뿐이므로, 회전을 나타내는 $\cos\theta+i\sin\theta$는 지수 $e^{i\theta}$일 수밖에 없다"는 것입니다.

> **문제 1.** (기초) $e^{i\pi/2}$의 값을 구하십시오.
> **답.** $i$.
> **풀이.** $e^{i\pi/2}=\cos\dfrac\pi2+i\sin\dfrac\pi2=0+i\cdot1=i$입니다.

> **문제 2.** (기초) $e^{i\pi}+1$의 값을 구하십시오.
> **답.** $0$.
> **풀이.** $e^{i\pi}=\cos\pi+i\sin\pi=-1$이라 $e^{i\pi}+1=0$입니다.

> **문제 3.** (표준) $\overline{e^{i\theta}}=e^{-i\theta}$임을 보이십시오.
> **답.** $\cos$은 우함수, $\sin$은 기함수라 켤레가 각의 부호만 바꾼 것과 같습니다.
> **풀이.** $\overline{e^{i\theta}}=\overline{\cos\theta+i\sin\theta}=\cos\theta-i\sin\theta$입니다. 한편 $e^{-i\theta}=\cos(-\theta)+i\sin(-\theta)=\cos\theta-i\sin\theta$입니다($\cos$은 우함수, $\sin$은 기함수). 두 값이 같으므로 $\overline{e^{i\theta}}=e^{-i\theta}$입니다. $\square$

> **문제 4.** (표준) $\lvert e^{i\theta}\rvert=1$임을 보이십시오.
> **답.** $\cos^2\theta+\sin^2\theta=1$이기 때문입니다.
> **풀이.** $\lvert e^{i\theta}\rvert=\lvert\cos\theta+i\sin\theta\rvert=\sqrt{\cos^2\theta+\sin^2\theta}=\sqrt1=1$입니다. 곧 $e^{i\theta}$는 언제나 단위원 위의 점입니다. $\square$

### 2.2 극형식의 지수 표기와 지수법칙

**정의.** 오일러 공식으로 1강의 극형식을 짧게 쓸 수 있습니다.
$$
z=r(\cos\theta+i\sin\theta)=re^{i\theta}
$$
이제 곱셈·나눗셈·거듭제곱이 모두 지수법칙으로 처리됩니다.
$$
r_1e^{i\theta_1}\cdot r_2e^{i\theta_2}=r_1r_2\,e^{i(\theta_1+\theta_2)},\qquad \frac{r_1e^{i\theta_1}}{r_2e^{i\theta_2}}=\frac{r_1}{r_2}e^{i(\theta_1-\theta_2)}
$$
$$
\big(re^{i\theta}\big)^n=r^n e^{in\theta}
$$
1강에서 삼각함수 덧셈정리로 증명하던 것들이 지수법칙 $e^{a}e^{b}=e^{a+b}$의 한 줄로 정리됩니다. 이것이 오일러 표기를 쓰는 가장 큰 이점입니다.

**예시.** $(1+i)^6$을 구합니다. $1+i=\sqrt2\,e^{i\pi/4}$이므로
$$
(1+i)^6=(\sqrt2)^6 e^{i\cdot6\pi/4}=8\,e^{i3\pi/2}=8\left(\cos\tfrac{3\pi}{2}+i\sin\tfrac{3\pi}{2}\right)=8(0-i)=-8i
$$
입니다. 검산: $(1+i)^2=2i$, $(2i)^3=8i^3=-8i$로 맞습니다.

직관은 "$re^{i\theta}$는 크기 $r$과 각 $\theta$를 지수 한 자리에 담아, 복소수 곱셈을 지수의 덧셈으로 바꾼다"는 것입니다.

> **문제 1.** (기초) $2e^{i\pi/3}\cdot3e^{i\pi/6}$을 지수꼴로 계산하십시오.
> **답.** $6e^{i\pi/2}$(곧 $6i$).
> **풀이.** 크기는 $2\cdot3=6$, 지수는 $\dfrac\pi3+\dfrac\pi6=\dfrac\pi2$이라 $6e^{i\pi/2}=6i$입니다.

> **문제 2.** (기초) $\dfrac{4e^{i\pi}}{2e^{i\pi/3}}$을 계산하십시오.
> **답.** $2e^{i2\pi/3}$.
> **풀이.** 크기는 $\dfrac42=2$, 지수는 $\pi-\dfrac\pi3=\dfrac{2\pi}{3}$이라 $2e^{i2\pi/3}$입니다.

> **문제 3.** (표준) $\left(\sqrt3+i\right)^4$를 지수꼴로 구하십시오.
> **답.** $-8+8\sqrt3\,i$.
> **풀이.** $\sqrt3+i=2e^{i\pi/6}$입니다. $(\ )^4=2^4 e^{i4\pi/6}=16e^{i2\pi/3}=16\left(-\dfrac12+\dfrac{\sqrt3}{2}i\right)=-8+8\sqrt3\,i$입니다.

> **문제 4.** (표준) $e^{i\pi/3}$을 여섯제곱하면 왜 $1$이 되는지 설명하십시오.
> **답.** $\left(e^{i\pi/3}\right)^6=e^{i2\pi}=1$이기 때문입니다.
> **풀이.** 지수법칙으로 $\left(e^{i\pi/3}\right)^6=e^{i\cdot6\pi/3}=e^{i2\pi}=\cos2\pi+i\sin2\pi=1$입니다. 각이 정확히 한 바퀴($2\pi$)를 돌아 제자리로 오기 때문입니다.

### 2.3 오일러 공식으로 삼각함수 표현하기

**표현.** $e^{i\theta}=\cos\theta+i\sin\theta$와 $e^{-i\theta}=\cos\theta-i\sin\theta$를 더하고 빼면
$$
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\qquad \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}
$$
을 얻습니다. 삼각함수를 지수의 조합으로 적은 이 식은 삼각항등식을 지수 계산으로 바꾸는 열쇠입니다.

**항등식 유도의 예.** 덧셈정리 $\cos(\alpha+\beta)$를 유도합니다. $e^{i(\alpha+\beta)}=e^{i\alpha}e^{i\beta}$를 전개하면
$$
\cos(\alpha+\beta)+i\sin(\alpha+\beta)=(\cos\alpha+i\sin\alpha)(\cos\beta+i\sin\beta)
$$
우변을 곱하면 $(\cos\alpha\cos\beta-\sin\alpha\sin\beta)+i(\sin\alpha\cos\beta+\cos\alpha\sin\beta)$입니다. 실수부·허수부를 비교하면
$$
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,\quad \sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta
$$
가 한꺼번에 나옵니다. 두 개의 덧셈정리가 지수 하나의 곱에서 동시에 떨어집니다.

**배각의 예.** 드무아브르 $\left(e^{i\theta}\right)^2=e^{i2\theta}$에서 $(\cos\theta+i\sin\theta)^2=\cos2\theta+i\sin2\theta$이므로, 좌변을 전개해 실수부를 비교하면 $\cos2\theta=\cos^2\theta-\sin^2\theta$, 허수부에서 $\sin2\theta=2\sin\theta\cos\theta$입니다.

직관은 "삼각항등식은 지수법칙 $e^{a}e^{b}=e^{a+b}$의 실수부·허수부 그림자"라는 것입니다.

> **문제 1.** (기초) $\cos0=\dfrac{e^{0}+e^{0}}{2}$로 확인하십시오.
> **답.** $1$.
> **풀이.** $e^{i\cdot0}=1$이라 $\cos0=\dfrac{1+1}{2}=1$입니다.

> **문제 2.** (표준) $\sin2\theta=2\sin\theta\cos\theta$를 오일러 공식으로 유도하십시오.
> **답.** $(\cos\theta+i\sin\theta)^2=\cos2\theta+i\sin2\theta$의 허수부 비교.
> **풀이.** $\left(e^{i\theta}\right)^2=e^{i2\theta}$이라 $(\cos\theta+i\sin\theta)^2=\cos2\theta+i\sin2\theta$입니다. 좌변을 전개하면 $\cos^2\theta-\sin^2\theta+i\cdot2\sin\theta\cos\theta$입니다. 허수부를 비교하면 $\sin2\theta=2\sin\theta\cos\theta$입니다. $\square$

> **문제 3.** (표준) $\cos3\theta=4\cos^3\theta-3\cos\theta$를 드무아브르로 유도하십시오.
> **답.** $(\cos\theta+i\sin\theta)^3$의 실수부를 $\sin^2\theta=1-\cos^2\theta$로 정리.
> **풀이.** $\left(e^{i\theta}\right)^3=e^{i3\theta}$이라 $(\cos\theta+i\sin\theta)^3=\cos3\theta+i\sin3\theta$입니다. 좌변을 이항전개하면 실수부는 $\cos^3\theta-3\cos\theta\sin^2\theta$입니다($i^2=-1$인 항들). $\sin^2\theta=1-\cos^2\theta$를 넣으면 $\cos^3\theta-3\cos\theta(1-\cos^2\theta)=4\cos^3\theta-3\cos\theta$입니다. 따라서 $\cos3\theta=4\cos^3\theta-3\cos\theta$입니다. $\square$

> **문제 4.** (심화) $\sin\theta=\dfrac{e^{i\theta}-e^{-i\theta}}{2i}$를 이용해 $\cos^2\theta+\sin^2\theta=1$을 유도하십시오.
> **답.** 두 표현을 제곱해 더하면 $e^{i\theta}$와 $e^{-i\theta}$의 교차항이 상쇄됩니다.
> **풀이.** $\cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}{2}$이라 $\cos^2\theta=\dfrac{e^{i2\theta}+2+e^{-i2\theta}}{4}$입니다. $\sin\theta=\dfrac{e^{i\theta}-e^{-i\theta}}{2i}$이라 $\sin^2\theta=\dfrac{e^{i2\theta}-2+e^{-i2\theta}}{(2i)^2}=\dfrac{e^{i2\theta}-2+e^{-i2\theta}}{-4}=\dfrac{-e^{i2\theta}+2-e^{-i2\theta}}{4}$입니다. 둘을 더하면 $e^{\pm i2\theta}$ 항이 상쇄되고 $\dfrac{2+2}{4}=1$이 남습니다. 곧 $\cos^2\theta+\sin^2\theta=1$입니다. $\square$

### 2.4 복소지수함수

**정의.** $z=x+iy$에 대해 복소지수함수를 지수법칙과 오일러 공식으로
$$
e^{z}=e^{x+iy}=e^{x}\big(\cos y+i\sin y\big)
$$
로 정의합니다. 절댓값은 $\lvert e^{z}\rvert=e^{x}$(실수부만이 크기를 정함)이고, 편각은 $\arg e^{z}=y$입니다.

**성질.** 실지수와 마찬가지로 $e^{z_1}e^{z_2}=e^{z_1+z_2}$이 성립합니다. 그러나 실지수에 없던 새 성질이 하나 있습니다. **주기성**입니다.
$$
e^{z+2\pi i}=e^{z}
$$
곧 복소지수함수는 허수축 방향으로 주기 $2\pi i$를 가집니다. $e^{2\pi i}=\cos2\pi+i\sin2\pi=1$이기 때문입니다. 이 주기성이 다음 절의 복소로그가 여러 값을 갖는 원인이 됩니다.

**예시.** $e^{1+i\pi}$를 계산합니다. $e^{1+i\pi}=e^{1}(\cos\pi+i\sin\pi)=e(-1+0)=-e$입니다. 실수부 $x=1$이 크기 $e$를, 허수부 $y=\pi$가 방향(음의 실수축)을 정했습니다.

직관은 "복소지수는 크기를 $e^{x}$로, 방향을 $y$로 나눠 담은 함수이며, $y$가 $2\pi$ 늘어도 같은 값이라 주기적이다"는 것입니다.

> **문제 1.** (기초) $e^{i\pi/2}$와 $e^{2+i\pi/2}$를 각각 구하십시오.
> **답.** $i$와 $e^2 i$.
> **풀이.** $e^{i\pi/2}=\cos\dfrac\pi2+i\sin\dfrac\pi2=i$입니다. $e^{2+i\pi/2}=e^2\cdot i=e^2 i$입니다.

> **문제 2.** (기초) $\lvert e^{3+4i}\rvert$을 구하십시오.
> **답.** $e^3$.
> **풀이.** $\lvert e^{x+iy}\rvert=e^{x}$이라 실수부 $3$만 보아 $e^3$입니다. 허수부 $4$는 방향만 정합니다.

> **문제 3.** (표준) $e^{z}=1$의 모든 해 $z$를 구하십시오.
> **답.** $z=2\pi k i$($k$는 정수).
> **풀이.** $e^{z}=e^{x}(\cos y+i\sin y)=1$이려면 크기 $e^{x}=1$이라 $x=0$, 방향 $\cos y+i\sin y=1$이라 $y=2\pi k$입니다. 따라서 $z=0+i\cdot2\pi k=2\pi k i$입니다.

> **문제 4.** (표준) $e^{i\pi}=e^{3i\pi}$인데 왜 지수 $i\pi\ne3i\pi$인지 모순이 아님을 설명하십시오.
> **답.** 복소지수는 주기 $2\pi i$라 지수가 $2\pi i$만큼 달라도 값이 같습니다.
> **풀이.** $3i\pi-i\pi=2i\pi$입니다. $e^{z+2\pi i}=e^{z}$이므로 지수가 $2\pi i$만큼 차이 나면 값이 같습니다. 실지수에서는 지수가 다르면 값도 다르지만, 복소지수는 주기함수라 지수의 허수부가 $2\pi$의 배수만큼 달라도 같은 값을 줍니다. 모순이 아니라 주기성의 자연스러운 결과입니다.

### 2.5 복소로그

**정의.** $e^{w}=z$($z\ne0$)를 만족하는 $w$를 $z$의 **복소로그** $\log z$라 합니다. $z=re^{i\theta}$이면
$$
\log z=\ln r+i(\theta+2\pi k)=\ln\lvert z\rvert+i\arg z,\qquad k\in\mathbb Z
$$
입니다. 편각 $\arg z$가 $2\pi$의 배수만큼 여러 값을 가지므로 복소로그도 **무한히 많은 값**을 가지는 다가함수입니다. 이 중 $-\pi<\operatorname{Arg}z\le\pi$인 주편각을 쓴 것을 **주로그** $\operatorname{Log}z=\ln\lvert z\rvert+i\operatorname{Arg}z$라 합니다.

**주의:** 실수 세계에서 로그는 양수에만 정의됐지만, 복소로그는 음수와 순허수에도 정의됩니다. 예컨대 $\log(-1)$은 $\ln1+i(\pi+2\pi k)=i(\pi+2\pi k)$이고 주값은 $\operatorname{Log}(-1)=i\pi$입니다. 실수에서 "음수의 로그는 없다"던 벽이 복소수에서 사라집니다.

**예시.** $\operatorname{Log}(1+i)$를 구합니다. $1+i=\sqrt2\,e^{i\pi/4}$이라 $\lvert1+i\rvert=\sqrt2$, $\operatorname{Arg}(1+i)=\dfrac\pi4$입니다. 따라서
$$
\operatorname{Log}(1+i)=\ln\sqrt2+i\frac\pi4=\frac12\ln2+i\frac\pi4
$$
입니다. 검산: $e^{\frac12\ln2+i\pi/4}=e^{\frac12\ln2}e^{i\pi/4}=\sqrt2\left(\cos\dfrac\pi4+i\sin\dfrac\pi4\right)=\sqrt2\cdot\dfrac{1+i}{\sqrt2}=1+i$로 맞습니다.

직관은 "복소로그는 절댓값에는 실로그를, 편각에는 각을 담는데, 각이 여러 값이라 로그도 여러 값이 된다"는 것입니다.

> **문제 1.** (기초) $\operatorname{Log}(e^2)$을 구하십시오.
> **답.** $2$.
> **풀이.** $e^2$은 양의 실수라 $\lvert e^2\rvert=e^2$, $\operatorname{Arg}=0$이라 $\operatorname{Log}(e^2)=\ln e^2+i\cdot0=2$입니다.

> **문제 2.** (기초) $\operatorname{Log}(i)$를 구하십시오.
> **답.** $i\dfrac\pi2$.
> **풀이.** $\lvert i\rvert=1$이라 $\ln1=0$이고 $\operatorname{Arg}(i)=\dfrac\pi2$이라 $\operatorname{Log}(i)=0+i\dfrac\pi2=i\dfrac\pi2$입니다.

> **문제 3.** (표준) $\log(-1)$의 모든 값을 구하고 주값을 쓰십시오.
> **답.** $\log(-1)=i(2k+1)\pi$($k\in\mathbb Z$), 주값 $\operatorname{Log}(-1)=i\pi$.
> **풀이.** $-1=1\cdot e^{i\pi}$이라 $\lvert-1\rvert=1$, $\arg(-1)=\pi+2\pi k$입니다. 따라서 $\log(-1)=\ln1+i(\pi+2\pi k)=i(\pi+2\pi k)=i(2k+1)\pi$입니다. $k=0$인 주값은 $i\pi$입니다.

> **문제 4.** (표준) $\operatorname{Log}(-\sqrt3+i)$를 구하십시오.
> **답.** $\ln2+i\dfrac{5\pi}{6}$.
> **풀이.** $\lvert-\sqrt3+i\rvert=\sqrt{3+1}=2$입니다. 점 $(-\sqrt3,1)$은 제2사분면이라 $\operatorname{Arg}=\pi-\dfrac\pi6=\dfrac{5\pi}{6}$입니다. 따라서 $\operatorname{Log}(-\sqrt3+i)=\ln2+i\dfrac{5\pi}{6}$입니다.

> **문제 5.** (심화) $i^{i}$의 주값이 실수 $e^{-\pi/2}$임을 보이십시오.
> **답.** $i^{i}=e^{i\operatorname{Log}i}=e^{i\cdot i\pi/2}=e^{-\pi/2}$.
> **풀이.** 복소거듭제곱은 $z^{w}=e^{w\log z}$로 정의합니다. 주값을 쓰면 $i^{i}=e^{i\operatorname{Log}i}$입니다. $\operatorname{Log}i=i\dfrac\pi2$(문제 2)이라 $i^{i}=e^{i\cdot i\pi/2}=e^{i^2\pi/2}=e^{-\pi/2}\approx0.2079$입니다. 놀랍게도 "허수의 허수 제곱"이 실수가 됩니다. $\square$

### 2.6 오일러 공식으로 다시 본 거듭제곱과 근

**드무아브르(지수판).** 오일러 표기에서 드무아브르 정리는 지수법칙의 특수한 경우입니다.
$$
\big(e^{i\theta}\big)^n=e^{in\theta}\quad\Longleftrightarrow\quad (\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta
$$
따로 증명할 것 없이 $e^{a}$의 거듭제곱이 지수를 곱하는 성질 그대로입니다.

**$n$제곱근(지수판).** $z=re^{i\theta}$의 $n$제곱근은
$$
w_k=r^{1/n}\,e^{i(\theta+2\pi k)/n},\qquad k=0,1,\dots,n-1
$$
입니다. 특히 $1=e^{i0}$의 $n$제곱근인 **단위근**은
$$
\omega_k=e^{i2\pi k/n},\qquad k=0,\dots,n-1
$$
로, $\omega=e^{i2\pi/n}$ 하나의 거듭제곱 $1,\omega,\omega^2,\dots,\omega^{n-1}$로 모두 나옵니다. 이 단위근들은 곱셈에 대해 닫혀 있고(순환군을 이룸), 합이 $0$입니다($n\ge2$).

**예시.** $16$의 네제곱근을 오일러로 구합니다. $16=16e^{i0}$이라 $w_k=16^{1/4}e^{i2\pi k/4}=2e^{i\pi k/2}$입니다. $k=0,1,2,3$에서 $2,\ 2i,\ -2,\ -2i$입니다. 네 근이 반지름 $2$인 원 위 정사각형을 이룹니다. 검산: $(2i)^4=16i^4=16$으로 맞습니다.

직관은 "오일러 표기에서는 거듭제곱도 근도 지수의 곱·나눗셈일 뿐이라, 1강의 결과가 모두 한 줄로 요약된다"는 것입니다.

> **문제 1.** (기초) $\left(e^{i\pi/5}\right)^{10}$을 구하십시오.
> **답.** $1$.
> **풀이.** $\left(e^{i\pi/5}\right)^{10}=e^{i10\pi/5}=e^{i2\pi}=1$입니다.

> **문제 2.** (표준) $1$의 여섯제곱근을 지수꼴로 모두 쓰십시오.
> **답.** $e^{i\pi k/3}$, $k=0,1,\dots,5$.
> **풀이.** $\omega_k=e^{i2\pi k/6}=e^{i\pi k/3}$입니다. 곧 $1,\ e^{i\pi/3},\ e^{i2\pi/3},\ -1,\ e^{i4\pi/3},\ e^{i5\pi/3}$으로 단위원을 $6$등분합니다.

> **문제 3.** (표준) $8$의 세제곱근을 오일러로 모두 구하십시오.
> **답.** $2,\ -1+\sqrt3\,i,\ -1-\sqrt3\,i$.
> **풀이.** $8=8e^{i0}$이라 $w_k=8^{1/3}e^{i2\pi k/3}=2e^{i2\pi k/3}$입니다. $k=0$: $2$. $k=1$: $2e^{i2\pi/3}=2\left(-\dfrac12+\dfrac{\sqrt3}{2}i\right)=-1+\sqrt3\,i$. $k=2$: 켤레 $-1-\sqrt3\,i$입니다. 검산: 세 근의 합 $2+(-1)+(-1)=0$입니다.

> **문제 4.** (심화) $\omega=e^{i2\pi/n}$일 때 $1+\omega+\omega^2+\cdots+\omega^{n-1}=0$($n\ge2$)임을 지수로 보이십시오.
> **답.** 등비수열 합 $\dfrac{\omega^n-1}{\omega-1}$에서 $\omega^n=1$이라 분자가 $0$입니다.
> **풀이.** $\omega=e^{i2\pi/n}\ne1$($n\ge2$)입니다. 등비수열 합 공식으로 $\sum_{k=0}^{n-1}\omega^k=\dfrac{\omega^n-1}{\omega-1}$인데, $\omega^n=e^{i2\pi}=1$이라 분자가 $0$이고 분모는 $0$이 아니므로 합은 $0$입니다. 단위근들이 정$n$각형 꼭짓점이라 벡터로 상쇄된다는 기하와 일치합니다. $\square$

## 3. 유형 총정리(치트시트)

| 상황 | 도구 | 핵심 식 |
|---|---|---|
| 오일러 공식 | 급수 유도 | $e^{i\theta}=\cos\theta+i\sin\theta$, $\lvert e^{i\theta}\rvert=1$ |
| 극형식(지수) | $re^{i\theta}$ | 곱은 지수 합, 거듭제곱은 지수 $\times n$ |
| 삼각함수↔지수 | 오일러 역산 | $\cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}{2},\ \sin\theta=\dfrac{e^{i\theta}-e^{-i\theta}}{2i}$ |
| 삼각항등식 | 지수법칙 | $e^{i(\alpha+\beta)}=e^{i\alpha}e^{i\beta}$의 실·허수부 비교 |
| 복소지수 | 분리 | $e^{x+iy}=e^{x}(\cos y+i\sin y)$, 주기 $2\pi i$ |
| 복소로그 | 다가함수 | $\log z=\ln\lvert z\rvert+i\arg z$, 주값은 $\operatorname{Arg}$ |
| 복소거듭제곱 | 로그·지수 | $z^{w}=e^{w\log z}$ |
| 거듭제곱·근 | 지수판 | $(re^{i\theta})^n=r^n e^{in\theta}$, $w_k=r^{1/n}e^{i(\theta+2\pi k)/n}$ |

핵심 습관: (1) 큰 곱·거듭제곱은 $re^{i\theta}$로 바꿔 지수법칙으로 처리한다. (2) 삼각항등식은 $e^{i\theta}$의 실수부·허수부 비교로 뽑는다. (3) 복소지수의 크기는 $e^{x}$, 방향은 $y$로 분리한다. (4) 복소로그·거듭제곱은 다가임을 잊지 말고 주값을 명시한다. (5) 결과는 직교형식으로 되돌려 검산한다.

## 4. 종합 문제 드릴

> **문제 1.** (기초) $e^{i3\pi/2}$을 직교형식으로 쓰십시오.
> **답.** $-i$.
> **풀이.** $e^{i3\pi/2}=\cos\dfrac{3\pi}{2}+i\sin\dfrac{3\pi}{2}=0+i(-1)=-i$입니다.

> **문제 2.** (기초) $2e^{i\pi/4}\cdot\sqrt2\,e^{i\pi/4}$을 직교형식으로 구하십시오.
> **답.** $2\sqrt2\,i$.
> **풀이.** 크기 $2\cdot\sqrt2=2\sqrt2$, 지수 $\dfrac\pi4+\dfrac\pi4=\dfrac\pi2$이라 $2\sqrt2\,e^{i\pi/2}=2\sqrt2\,i$입니다.

> **문제 3.** (표준) $\left(1-\sqrt3\,i\right)^5$를 오일러로 구하십시오.
> **답.** $16+16\sqrt3\,i$.
> **풀이.** $1-\sqrt3\,i=2e^{-i\pi/3}$입니다($r=2$, 제4사분면 $-\dfrac\pi3$). $(\ )^5=2^5 e^{-i5\pi/3}=32e^{-i5\pi/3}$입니다. $-\dfrac{5\pi}{3}+2\pi=\dfrac\pi3$이라 $32e^{i\pi/3}=32\left(\dfrac12+\dfrac{\sqrt3}{2}i\right)=16+16\sqrt3\,i$입니다.

> **문제 4.** (표준) $\cos4\theta$를 $\cos\theta$에 대한 식으로 나타내는 과정을 오일러로 시작해 실수부까지 쓰십시오.
> **답.** $\cos4\theta=\cos^4\theta-6\cos^2\theta\sin^2\theta+\sin^4\theta$(=$8\cos^4\theta-8\cos^2\theta+1$).
> **풀이.** $(\cos\theta+i\sin\theta)^4=\cos4\theta+i\sin4\theta$입니다. 좌변을 이항전개하면 실수부는 $\cos^4\theta-6\cos^2\theta\sin^2\theta+\sin^4\theta$입니다($i^0,i^2,i^4$ 항). $\sin^2\theta=1-\cos^2\theta$를 넣으면 $\cos^4\theta-6\cos^2\theta(1-\cos^2\theta)+(1-\cos^2\theta)^2=8\cos^4\theta-8\cos^2\theta+1$입니다. 곧 $\cos4\theta=8\cos^4\theta-8\cos^2\theta+1$입니다.

> **문제 5.** (표준) $e^{2+i\pi/3}$을 직교형식으로 구하십시오.
> **답.** $\dfrac{e^2}{2}+\dfrac{e^2\sqrt3}{2}i$.
> **풀이.** $e^{2+i\pi/3}=e^2\left(\cos\dfrac\pi3+i\sin\dfrac\pi3\right)=e^2\left(\dfrac12+\dfrac{\sqrt3}{2}i\right)=\dfrac{e^2}{2}+\dfrac{e^2\sqrt3}{2}i$입니다.

> **문제 6.** (표준) $\operatorname{Log}(-8)$을 구하십시오.
> **답.** $\ln8+i\pi$(=$3\ln2+i\pi$).
> **풀이.** $\lvert-8\rvert=8$, $\operatorname{Arg}(-8)=\pi$(음의 실수축)이라 $\operatorname{Log}(-8)=\ln8+i\pi=3\ln2+i\pi$입니다.

> **문제 7.** (표준) $e^{z}=-2$의 모든 해를 구하십시오.
> **답.** $z=\ln2+i(2k+1)\pi$($k\in\mathbb Z$).
> **풀이.** $-2=2e^{i\pi}$이라 $e^{z}=2e^{i\pi}$가 되려면 크기 $e^{x}=2$에서 $x=\ln2$, 방향 $y=\pi+2\pi k$입니다. 따라서 $z=\ln2+i(\pi+2\pi k)=\ln2+i(2k+1)\pi$입니다.

> **문제 8.** (심화) $\cos\dfrac\pi5+\cos\dfrac{3\pi}{5}+\cos\dfrac{5\pi}{5}+\cos\dfrac{7\pi}{5}+\cos\dfrac{9\pi}{5}$의 값을 단위근으로 구하십시오.
> **답.** $0$.
> **풀이.** 이 각들은 $\dfrac{(2k+1)\pi}{5}$, $k=0,\dots,4$입니다. $\zeta_k=e^{i(2k+1)\pi/5}$로 두면 이들은 $z^5=e^{i\pi}=-1$의 다섯 근입니다. 다섯 근의 합은 다항식 $z^5+1=0$의 근의 합이라 계수로부터 $0$입니다($z^4$ 항이 없으므로). 근의 합이 $0$이면 실수부의 합, 곧 코사인들의 합도 $0$입니다. $\square$

> **문제 9.** (심화) $(1+i)^{i}$의 주값을 구하십시오.
> **답.** $e^{-\pi/4}\left(\cos\dfrac{\ln2}{2}+i\sin\dfrac{\ln2}{2}\right)$.
> **풀이.** $z^{w}=e^{w\operatorname{Log}z}$입니다. $\operatorname{Log}(1+i)=\dfrac12\ln2+i\dfrac\pi4$(2.5 예시)입니다. 그러면 $(1+i)^{i}=e^{i\left(\frac12\ln2+i\frac\pi4\right)}=e^{-\pi/4+i\frac{\ln2}{2}}=e^{-\pi/4}\left(\cos\dfrac{\ln2}{2}+i\sin\dfrac{\ln2}{2}\right)$입니다. 지수의 실수부 $-\dfrac\pi4$가 크기를, 허수부 $\dfrac{\ln2}{2}$가 방향을 정합니다.

> **문제 10.** (심화) 오일러 공식으로 $\displaystyle\sum_{k=0}^{n-1}\cos k\theta$의 닫힌 식을 등비수열 합으로 유도하십시오($\theta$는 $2\pi$의 배수가 아님).
> **답.** $\displaystyle\sum_{k=0}^{n-1}\cos k\theta=\frac{\sin(n\theta/2)}{\sin(\theta/2)}\cos\frac{(n-1)\theta}{2}$.
> **풀이.** $\sum_{k=0}^{n-1}e^{ik\theta}$는 공비 $e^{i\theta}$인 등비수열 합이라 $\dfrac{e^{in\theta}-1}{e^{i\theta}-1}$입니다. 분자·분모에서 각각 절반 각을 뽑으면 $e^{in\theta}-1=e^{in\theta/2}\left(e^{in\theta/2}-e^{-in\theta/2}\right)=e^{in\theta/2}\cdot2i\sin\dfrac{n\theta}{2}$이고 마찬가지로 $e^{i\theta}-1=e^{i\theta/2}\cdot2i\sin\dfrac\theta2$입니다. 나누면 $e^{i(n-1)\theta/2}\dfrac{\sin(n\theta/2)}{\sin(\theta/2)}$입니다. 실수부를 취하면 $\cos\dfrac{(n-1)\theta}{2}\cdot\dfrac{\sin(n\theta/2)}{\sin(\theta/2)}$이 원하는 코사인 합입니다. $\square$

> **문제 11.** (심화) $z^3=-8i$의 세 근을 모두 구하십시오.
> **답.** $2e^{i\pi/2}=2i,\ 2e^{i7\pi/6}=-\sqrt3-i,\ 2e^{i11\pi/6}=\sqrt3-i$.
> **풀이.** $-8i=8e^{-i\pi/2}$입니다. $w_k=8^{1/3}e^{i(-\pi/2+2\pi k)/3}=2e^{i(-\pi/6+2\pi k/3)}$, $k=0,1,2$입니다. $k=0$: $2e^{-i\pi/6}=2\left(\dfrac{\sqrt3}{2}-\dfrac12 i\right)=\sqrt3-i$. $k=1$: $2e^{i(-\pi/6+2\pi/3)}=2e^{i\pi/2}=2i$. $k=2$: $2e^{i(-\pi/6+4\pi/3)}=2e^{i7\pi/6}=2\left(-\dfrac{\sqrt3}{2}-\dfrac12 i\right)=-\sqrt3-i$. 검산: $(2i)^3=8i^3=-8i$로 맞습니다.

## 5. 스스로 점검

1. 급수로 오일러 공식 $e^{i\theta}=\cos\theta+i\sin\theta$를 유도하고 $e^{i\pi}+1=0$을 아는가?
2. 극형식을 $re^{i\theta}$로 쓰고 곱·거듭제곱을 지수법칙으로 처리하는가?
3. $\cos\theta,\sin\theta$를 지수로 표현하고 삼각항등식을 지수 계산으로 유도하는가?
4. 복소지수 $e^{x+iy}=e^{x}(\cos y+i\sin y)$의 크기·방향·주기를 이해하는가?
5. 복소로그가 다가함수임을 알고 주값 $\operatorname{Log}z$를 구하는가?
6. 복소거듭제곱 $z^{w}=e^{w\log z}$로 $i^{i}$ 같은 값을 계산하는가?
7. 오일러로 드무아브르와 $n$제곱근·단위근을 재정리하는가?

**정답 요지.** (1) $e^{x}$ 급수에 $x=i\theta$를 넣어 짝·홀수 항이 $\cos,\sin$으로 갈림; $\theta=\pi$에서 $e^{i\pi}=-1$. (2) $re^{i\theta}$의 곱은 지수 합, $n$제곱은 지수 $\times n$. (3) $\cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}{2}$ 등, 항등식은 $e^{i(\alpha+\beta)}=e^{i\alpha}e^{i\beta}$의 실·허수부. (4) 크기 $e^{x}$·방향 $y$·주기 $2\pi i$. (5) $\log z=\ln\lvert z\rvert+i\arg z$, 주값은 $-\pi<\operatorname{Arg}\le\pi$. (6) $z^{w}=e^{w\log z}$, $i^{i}=e^{-\pi/2}$. (7) $(re^{i\theta})^n=r^n e^{in\theta}$, 단위근 $e^{i2\pi k/n}$의 합은 $0$.
