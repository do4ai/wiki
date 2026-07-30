---
title: "9. 유수정리와 실적분 계산"
---
# 9강. 유수정리와 실적분 계산

## 이 강의에서 할 수 있게 되는 것

- 유리함수의 무한구간 실적분을 반원 경로와 유수정리로 계산할 수 있습니다.
- 삼각함수가 든 한 주기 적분을 단위원 경로 적분으로 바꿔 계산할 수 있습니다.
- 조르당 보조정리를 진술하고 푸리에 꼴 적분에 적용할 수 있습니다.
- 분지절단이 있는 적분을 열쇠구멍 경로로 계산할 수 있습니다.
- 실축 위에 극이 있을 때 주요값과 작은 반원의 기여를 나누어 처리할 수 있습니다.
- 문제를 보고 어떤 경로를 쓸지 판단하는 절차를 따라갈 수 있습니다.

이 강의는 [8. 특이점과 유수정리](../8. 특이점과 유수정리/index.md)에서 세운 유수정리를 실적분 계산에 쓰는 응용편입니다. 로랑 전개는 [7. 테일러 급수와 로랑 급수](../7. 테일러 급수와 로랑 급수/index.md)에서, 경로 변형의 근거는 [6. 코시 정리와 코시 적분공식](../../03. 복소적분/6. 코시 정리와 코시 적분공식/index.md)에서 다룹니다. 여기서 계산하는 푸리에 꼴 적분은 [푸리에 해석과 변환](../../../푸리에 해석과 변환/index.md) 교본의 변환 계산에서 다시 쓰입니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\Gamma_R$ | 감마 알 | 반지름 $R$인 상반평면의 반원호 |
| $C_\varepsilon$ | 씨 엡실론 | 실축 위 극을 피해 도는 반지름 $\varepsilon$의 작은 반원호 |
| $\displaystyle\oint_{|z|=1}$ | 단위원 적분 | 단위원을 양의 방향으로 도는 적분 |
| $M_R$ | 엠 알 | $\Gamma_R$ 위에서 $|f|$의 최댓값 |
| $\operatorname{P.V.}\displaystyle\int$ | 주요값 적분 | 특이점을 대칭으로 잘라낸 극한값 |
| $z^{a-1}$ | 지의 $a-1$승 | $e^{(a-1)\operatorname{Log}z}$로 분지를 고정한 거듭제곱 |
| $\operatorname{Res}$ | 유수 | 로랑 전개의 $(z-z_0)^{-1}$ 계수 |
| $\deg P$ | 피의 차수 | 다항식 $P$의 최고차 차수 |

## 2. 개념

### 2.1 유리함수의 실적분과 반원 경로

가장 기본이 되는 꼴은 유리함수의 전구간 적분입니다. $P,Q$가 다항식이고 다음 두 조건을 만족한다고 합니다.

$$
\deg Q\ge \deg P+2,\qquad Q(x)\ne0\ \ (\forall x\in\mathbb{R})
$$

첫 조건은 적분의 수렴을, 둘째 조건은 실축 위에 특이점이 없음을 보장합니다. 이때 실축의 구간 $[-R,R]$과 상반평면의 반원호 $\Gamma_R$을 이어 만든 반원 경로에 유수정리를 적용합니다.

$$
\int_{-R}^{R}\frac{P(x)}{Q(x)}dx+\int_{\Gamma_R}\frac{P(z)}{Q(z)}dz=2\pi i\sum_{\operatorname{Im}z_k>0}\operatorname{Res}_{z=z_k}\frac{P}{Q}
$$

반원호의 기여가 사라지는 것이 핵심입니다. 차수 조건에서 $|z|$가 충분히 클 때 어떤 상수 $C$에 대해 $\left|\frac{P(z)}{Q(z)}\right|\le\frac{C}{|z|^2}$이므로 ML 부등식이 다음을 줍니다.

$$
\left|\int_{\Gamma_R}\frac{P(z)}{Q(z)}dz\right|\le \pi R\cdot\frac{C}{R^2}=\frac{\pi C}{R}\xrightarrow[R\to\infty]{}0
$$

따라서 다음 공식을 얻습니다.

$$
\int_{-\infty}^{\infty}\frac{P(x)}{Q(x)}dx=2\pi i\sum_{\operatorname{Im}z_k>0}\operatorname{Res}_{z=z_k}\frac{P}{Q}
$$

**예제 1.** $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^4+1}$을 계산합니다.

분모의 영점은 $z^4=-1$의 해이므로 $z=e^{i\pi/4},e^{3i\pi/4},e^{5i\pi/4},e^{7i\pi/4}$이고, 이 가운데 상반평면에 있는 것은 $z_1=e^{i\pi/4}$, $z_2=e^{3i\pi/4}$입니다. 모두 단순극이므로 분모 미분 공식을 씁니다. $z_k^4=-1$을 이용하면

$$
\operatorname{Res}_{z=z_k}\frac{1}{z^4+1}=\frac{1}{4z_k^{3}}=\frac{z_k}{4z_k^{4}}=-\frac{z_k}{4}
$$

입니다. 두 유수를 더하면

$$
-\frac{1}{4}\left(e^{i\pi/4}+e^{3i\pi/4}\right)
=-\frac{1}{4}\left(\frac{\sqrt2}{2}+\frac{\sqrt2}{2}i-\frac{\sqrt2}{2}+\frac{\sqrt2}{2}i\right)
=-\frac{\sqrt2}{4}i
$$

이므로 적분값은 다음과 같습니다.

$$
\int_{-\infty}^{\infty}\frac{dx}{x^4+1}=2\pi i\cdot\left(-\frac{\sqrt2}{4}i\right)=\frac{\pi\sqrt2}{2}=\frac{\pi}{\sqrt2}
$$

> **문제 1.** (기초) $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+1}$을 유수정리로 구하십시오.
> **답.** $\pi$입니다.
> **풀이.** 상반평면의 극은 $z=i$뿐이고 유수는 $\frac{1}{2i}$입니다. 차수 차이가 2이므로 반원호의 기여가 0이고, 적분값은 $2\pi i\cdot\frac{1}{2i}=\pi$입니다.

> **문제 2.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{x^2}{(x^2+1)(x^2+4)}dx$를 구하십시오.
> **답.** $\dfrac{\pi}{3}$입니다.
> **풀이.** 상반평면의 단순극은 $z=i,2i$입니다. $z=i$에서 유수는 $\frac{z^2}{(z+i)(z^2+4)}\big|_{z=i}=\frac{-1}{2i\cdot3}=\frac{i}{6}$이고, $z=2i$에서 유수는 $\frac{z^2}{(z^2+1)(z+2i)}\big|_{z=2i}=\frac{-4}{-3\cdot4i}=-\frac{i}{3}$입니다. 합이 $-\frac{i}{6}$이므로 적분값은 $2\pi i\cdot\left(-\frac{i}{6}\right)=\frac{\pi}{3}$입니다.

> **문제 3.** (심화) $\displaystyle\int_{0}^{\infty}\frac{dx}{x^6+1}$을 구하십시오.
> **답.** $\dfrac{\pi}{3}$입니다.
> **풀이.** 피적분함수가 짝함수이므로 전구간 적분의 절반입니다. 상반평면의 극은 $e^{i\pi/6},e^{i\pi/2},e^{5i\pi/6}$이고 각 유수는 $\frac{1}{6z_k^5}=-\frac{z_k}{6}$입니다. 세 값의 합은 $-\frac16\left(e^{i\pi/6}+i+e^{5i\pi/6}\right)=-\frac16(2i)=-\frac{i}{3}$이므로 전구간 적분은 $2\pi i\cdot\left(-\frac{i}{3}\right)=\frac{2\pi}{3}$이고 구하는 값은 $\frac{\pi}{3}$입니다.

### 2.2 삼각함수 적분과 단위원 경로

한 주기에 걸친 삼각함수 적분은 단위원 위의 적분으로 바뀝니다. $\theta$가 $0$에서 $2\pi$까지 움직일 때 $z=e^{i\theta}$는 단위원을 양의 방향으로 한 바퀴 돌므로 다음 치환이 성립합니다.

$$
\cos\theta=\frac{z+z^{-1}}{2},\qquad
\sin\theta=\frac{z-z^{-1}}{2i},\qquad
d\theta=\frac{dz}{iz}
$$

이를 대입하면 $\int_0^{2\pi}F(\cos\theta,\sin\theta)d\theta$는 유리함수의 단위원 적분이 되고, $|z|<1$ 안의 극에서만 유수를 모으면 됩니다.

**예제 2.** $\displaystyle\int_0^{2\pi}\frac{d\theta}{5+4\cos\theta}$를 계산합니다.

치환하면 분모가 $5+2\left(z+\frac1z\right)=\frac{2z^2+5z+2}{z}$이므로

$$
\int_0^{2\pi}\frac{d\theta}{5+4\cos\theta}
=\oint_{|z|=1}\frac{z}{2z^2+5z+2}\cdot\frac{dz}{iz}
=\frac{1}{i}\oint_{|z|=1}\frac{dz}{2z^2+5z+2}
$$

입니다. $2z^2+5z+2=2\left(z+\frac12\right)(z+2)$이므로 단위원 내부의 극은 $z=-\frac12$ 하나이고, 그 유수는

$$
\operatorname{Res}_{z=-1/2}\frac{1}{2(z+\frac12)(z+2)}=\frac{1}{2\left(-\frac12+2\right)}=\frac{1}{3}
$$

입니다. 따라서 적분값은 $\frac{1}{i}\cdot2\pi i\cdot\frac13=\frac{2\pi}{3}$입니다.

같은 계산을 일반화하면 다음 공식이 나오며, 예제 2는 $a=5$, $b=4$인 경우로 $\frac{2\pi}{\sqrt{25-16}}=\frac{2\pi}{3}$과 일치합니다.

$$
\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}\qquad(a>|b|)
$$

> **문제 1.** (기초) $\displaystyle\int_0^{2\pi}\frac{d\theta}{2+\cos\theta}$를 구하십시오.
> **답.** $\dfrac{2\pi}{\sqrt3}$입니다.
> **풀이.** 위 공식에서 $a=2$, $b=1$이므로 $\frac{2\pi}{\sqrt{4-1}}=\frac{2\pi}{\sqrt3}$입니다. 직접 하면 분모가 $\frac{z^2+4z+1}{2z}$이 되고 내부 극은 $z=-2+\sqrt3$이며 유수가 $\frac{1}{\sqrt3}\cdot\frac{1}{i}$ 꼴로 나옵니다.

> **문제 2.** (표준) 치환 $z=e^{i\theta}$에서 $d\theta=\frac{dz}{iz}$가 나오는 이유를 설명하십시오.
> **답.** $dz=ie^{i\theta}d\theta=iz\,d\theta$이므로 양변을 $iz$로 나눈 것입니다.
> **풀이.** $z=e^{i\theta}$를 $\theta$로 미분하면 $\frac{dz}{d\theta}=ie^{i\theta}=iz$입니다. 따라서 $dz=iz\,d\theta$이고 $d\theta=\frac{dz}{iz}$입니다. $\theta$가 $0$에서 $2\pi$까지 움직이면 $z$는 단위원을 정확히 한 바퀴 돕니다.

> **문제 3.** (심화) $\displaystyle\int_0^{2\pi}\frac{\cos\theta}{5-4\cos\theta}d\theta$를 구하십시오.
> **답.** $\dfrac{\pi}{3}$입니다.
> **풀이.** 분모는 $5-2\left(z+\frac1z\right)=\frac{-(2z-1)(z-2)}{z}$이고 분자는 $\frac{z+z^{-1}}{2}$입니다. 정리하면 적분은 $-\frac{1}{2i}\oint_{|z|=1}\frac{z^2+1}{z(2z-1)(z-2)}dz$입니다. 내부의 단순극 $z=0$에서 유수는 $\frac{1}{(-1)(-2)}=\frac12$, $z=\frac12$에서 유수는 $\frac{5/4}{\frac12\cdot2\cdot\left(-\frac32\right)}=-\frac56$이므로 합이 $-\frac13$입니다. 따라서 값은 $-\frac{1}{2i}\cdot2\pi i\cdot\left(-\frac13\right)=\frac{\pi}{3}$입니다.

### 2.3 조르당 보조정리와 푸리에 꼴 적분

$\frac{\cos x}{x^2+1}$처럼 삼각함수가 든 무한구간 적분에서는 $\cos x,\sin x$를 그대로 두면 상반평면에서 크기를 통제할 수 없습니다. $\cos x=\operatorname{Re}e^{ix}$, $\sin x=\operatorname{Im}e^{ix}$로 바꿔 $e^{imz}$를 다루는 것이 표준 전략입니다. 상반평면에서 $|e^{imz}|=e^{-m\operatorname{Im}z}\le1$($m>0$)이므로 지수함수가 감쇠 인자로 작동합니다.

**조르당 보조정리.** $m>0$이고 $f$가 $\Gamma_R$ 위에서 연속이며 $M_R=\max_{z\in\Gamma_R}|f(z)|$일 때

$$
\left|\int_{\Gamma_R}f(z)e^{imz}dz\right|\le\frac{\pi M_R}{m}
$$

증명 개요는 다음과 같습니다. $z=Re^{i\theta}$에서 $|e^{imz}|=e^{-mR\sin\theta}$이고, $[0,\pi/2]$에서 $\sin\theta\ge\frac{2\theta}{\pi}$이므로 다음을 얻습니다.

$$
\left|\int_{\Gamma_R}f(z)e^{imz}dz\right|
\le M_RR\int_0^{\pi}e^{-mR\sin\theta}d\theta
=2M_RR\int_0^{\pi/2}e^{-mR\sin\theta}d\theta
\le 2M_RR\int_0^{\pi/2}e^{-2mR\theta/\pi}d\theta
=\frac{\pi M_R}{m}\left(1-e^{-mR}\right)\le\frac{\pi M_R}{m}
\quad\square
$$

따라서 $M_R\to0$이기만 하면 반원호의 기여가 사라집니다. 2.1절과 달리 차수 차이가 1이어도, 즉 $|f|\sim\frac{1}{R}$이어도 쓸 수 있다는 점이 조르당 보조정리의 힘입니다.

**예제 3.** $\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{x^2+1}dx$를 계산합니다.

$f(z)=\frac{1}{z^2+1}$, $m=1$로 두고 $\frac{e^{iz}}{z^2+1}$을 반원 경로에서 적분합니다. $M_R\le\frac{1}{R^2-1}\to0$이므로 반원호의 기여는 0입니다. 상반평면의 극은 $z=i$이고

$$
\operatorname{Res}_{z=i}\frac{e^{iz}}{z^2+1}=\frac{e^{i\cdot i}}{2i}=\frac{e^{-1}}{2i}
$$

이므로

$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{x^2+1}dx=2\pi i\cdot\frac{e^{-1}}{2i}=\frac{\pi}{e}
$$

입니다. 좌변의 실수부가 구하는 적분이고 허수부 $\int\frac{\sin x}{x^2+1}dx$는 홀함수의 대칭 적분이라 0입니다. 따라서 $\int_{-\infty}^{\infty}\frac{\cos x}{x^2+1}dx=\frac{\pi}{e}$입니다.

> **문제 1.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{\cos 2x}{x^2+4}dx$를 구하십시오.
> **답.** $\dfrac{\pi}{2}e^{-4}$입니다.
> **풀이.** $\frac{e^{2iz}}{z^2+4}$의 상반평면 극은 $z=2i$이고 유수는 $\frac{e^{2i\cdot2i}}{4i}=\frac{e^{-4}}{4i}$입니다. 적분값은 $2\pi i\cdot\frac{e^{-4}}{4i}=\frac{\pi}{2}e^{-4}$이고, 이것이 실수부이므로 구하는 값과 같습니다.

> **문제 2.** (표준) $\displaystyle\int_{0}^{\infty}\frac{x\sin x}{x^2+1}dx$를 구하십시오.
> **답.** $\dfrac{\pi}{2e}$입니다.
> **풀이.** $\frac{ze^{iz}}{z^2+1}$을 씁니다. $M_R\sim\frac{R}{R^2-1}\to0$이므로 조르당 보조정리가 적용됩니다. $z=i$에서 유수는 $\frac{ie^{-1}}{2i}=\frac{e^{-1}}{2}$이므로 $\int_{-\infty}^{\infty}\frac{xe^{ix}}{x^2+1}dx=\pi i e^{-1}$입니다. 허수부를 읽으면 $\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+1}dx=\frac{\pi}{e}$이고 피적분함수가 짝함수이므로 절반인 $\frac{\pi}{2e}$입니다.

> **문제 3.** (심화) 2.1절의 ML 추정으로는 $\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+1}dx$를 다룰 수 없는 이유를 설명하십시오.
> **답.** 분자와 분모의 차수 차이가 1뿐이라 반원호의 기여가 0이라는 보장을 얻지 못하기 때문입니다.
> **풀이.** ML 추정은 $\left|\int_{\Gamma_R}\right|\le\pi R\cdot M_R$ 형태이므로 $M_R$이 $\frac{1}{R}$ 정도면 상계가 상수로 남아 0으로 가지 않습니다. 반면 조르당 보조정리는 상계가 $\frac{\pi M_R}{m}$이므로 $M_R\to0$만으로 충분합니다. $e^{imz}$의 상반평면 감쇠가 여분의 $\frac1R$을 대신합니다.

### 2.4 분지절단이 있는 적분

$x^{a-1}$이나 $\ln x$처럼 다가함수가 들어가면 분지를 고정해야 합니다. 분지절단을 양의 실축에 두고, 절단의 위아래를 지나는 두 선분과 두 원으로 만든 열쇠구멍 경로를 씁니다.

**예제 4.** $0<a<1$일 때 $\displaystyle\int_0^\infty\frac{x^{a-1}}{1+x}dx=\frac{\pi}{\sin \pi a}$를 보입니다.

$z^{a-1}=e^{(a-1)\log z}$에서 $\log z=\ln|z|+i\theta$, $0<\theta<2\pi$로 분지를 고정합니다. 경로는 큰 원 $|z|=R$, 작은 원 $|z|=\varepsilon$, 그리고 절단의 위쪽 선분($\theta=0^+$)과 아래쪽 선분($\theta=2\pi^-$)입니다.

두 원의 기여는 사라집니다. $|z|=R$에서 피적분함수의 크기는 대략 $R^{a-2}$이고 길이가 $2\pi R$이므로 곱이 $R^{a-1}\to0$이며($a<1$), $|z|=\varepsilon$에서는 크기가 대략 $\varepsilon^{a-1}$이고 길이가 $2\pi\varepsilon$이므로 곱이 $\varepsilon^{a}\to0$입니다($a>0$). 조건 $0<a<1$은 이 두 극한이 성립하기 위한 조건이며, 동시에 원래 실적분이 양 끝에서 수렴하는 조건이기도 합니다.

위쪽 선분은 $\int_\varepsilon^R\frac{x^{a-1}}{1+x}dx$를 줍니다. 아래쪽 선분에서는 $z=xe^{2\pi i}$이므로 $z^{a-1}=x^{a-1}e^{2\pi i(a-1)}$이고 진행 방향이 반대이므로 $-e^{2\pi i a}\int_\varepsilon^R\frac{x^{a-1}}{1+x}dx$를 줍니다. 내부의 유일한 극은 $z=-1=e^{i\pi}$이고 단순극이며 유수는 $\operatorname{Res}_{z=-1}\frac{z^{a-1}}{1+z}=e^{i\pi(a-1)}$입니다. $\varepsilon\to0$, $R\to\infty$로 보내고 $I=\int_0^\infty\frac{x^{a-1}}{1+x}dx$라 쓰면 유수정리가 다음을 줍니다.

$$
\left(1-e^{2\pi i a}\right)I=2\pi i\,e^{i\pi(a-1)}=-2\pi i\,e^{i\pi a}
$$

양변을 $e^{i\pi a}$로 정리하면

$$
I=\frac{-2\pi i}{e^{-i\pi a}-e^{i\pi a}}=\frac{-2\pi i}{-2i\sin\pi a}=\frac{\pi}{\sin\pi a}
$$

입니다. $\square$

> **문제 1.** (기초) 예제 4의 결과에서 $a=\frac12$인 값을 구하고 초등적 치환으로 확인하십시오.
> **답.** $\pi$입니다.
> **풀이.** $\frac{\pi}{\sin(\pi/2)}=\pi$입니다. 한편 $\int_0^\infty\frac{dx}{\sqrt x(1+x)}$에서 $x=t^2$로 치환하면 $2\int_0^\infty\frac{dt}{1+t^2}=2\cdot\frac{\pi}{2}=\pi$로 같습니다.

> **문제 2.** (표준) $\displaystyle\int_0^\infty\frac{x^{-1/3}}{1+x}dx$를 구하십시오.
> **답.** $\dfrac{2\pi}{\sqrt3}$입니다.
> **풀이.** $x^{a-1}=x^{-1/3}$에서 $a=\frac23$입니다. 따라서 값은 $\frac{\pi}{\sin(2\pi/3)}=\frac{\pi}{\sqrt3/2}=\frac{2\pi}{\sqrt3}$입니다.

> **문제 3.** (심화) 예제 4에서 $a\ge1$이거나 $a\le0$이면 계산이 성립하지 않는 이유를 말하십시오.
> **답.** $a\ge1$이면 큰 원의 기여가 0으로 가지 않고 적분이 무한대에서 발산하며, $a\le0$이면 작은 원의 기여가 0으로 가지 않고 적분이 원점에서 발산합니다.
> **풀이.** 큰 원의 상계는 $R^{a-1}$이므로 $a\ge1$에서 0으로 수렴하지 않고, 실적분도 피적분함수가 $x^{a-2}$처럼 행동해 $a\ge1$이면 무한대 쪽에서 발산합니다. 작은 원의 상계는 $\varepsilon^{a}$이므로 $a\le0$에서 0으로 수렴하지 않고, 원점 근방에서 $x^{a-1}$이 적분가능하지 않습니다.

### 2.5 주요값 적분과 실축 위의 극

실축 위에 극이 있으면 보통 의미의 적분이 존재하지 않을 수 있습니다. 이때는 특이점 주변을 대칭으로 잘라낸 극한, 즉 주요값을 씁니다. 실축의 $x_0$가 특이점일 때

$$
\operatorname{P.V.}\int_{-\infty}^{\infty}f(x)dx
=\lim_{\varepsilon\to0^+}\left(\int_{-\infty}^{x_0-\varepsilon}f+\int_{x_0+\varepsilon}^{\infty}f\right)
$$

로 정의합니다. 경로는 실축을 따라가다 $x_0$ 위로 작은 반원 $C_\varepsilon$을 얹어 우회합니다. 이 반원은 편각이 $\pi$에서 $0$으로 줄어드는 방향, 즉 음의 방향으로 지나갑니다.

**작은 반원 보조정리.** $x_0$가 $f$의 단순극일 때 위와 같이 잡은 $C_\varepsilon$에 대해

$$
\lim_{\varepsilon\to0^+}\int_{C_\varepsilon}f(z)\,dz=-i\pi\operatorname{Res}_{z=x_0}f
$$

근거는 로랑 전개입니다. $f(z)=\frac{a_{-1}}{z-x_0}+g(z)$에서 $g$는 유계이므로 그 적분은 길이 $\pi\varepsilon$에 비례해 0으로 가고, 첫 항은 $z=x_0+\varepsilon e^{i\theta}$를 대입하면 $\varepsilon$과 무관하게

$$
\int_{\pi}^{0}\frac{a_{-1}}{\varepsilon e^{i\theta}}\,i\varepsilon e^{i\theta}d\theta=ia_{-1}\int_{\pi}^{0}d\theta=-i\pi a_{-1}
$$

이 됩니다. $\square$

정리하면 상반평면 극의 유수는 $2\pi i$ 배, 실축 위 단순극의 유수는 $i\pi$ 배로 기여합니다.

$$
\operatorname{P.V.}\int_{-\infty}^{\infty}f(x)dx=2\pi i\sum_{\operatorname{Im}z_k>0}\operatorname{Res}_{z=z_k}f+i\pi\sum_{x_j\in\mathbb{R}}\operatorname{Res}_{z=x_j}f
$$

**예제 5.** $\displaystyle\int_0^\infty\frac{\sin x}{x}dx=\frac{\pi}{2}$를 보입니다.

$f(z)=\frac{e^{iz}}{z}$를 잡습니다. $z=0$은 단순극이고 유수는 1입니다. 상반평면 내부에는 특이점이 없으므로 우회 경로 전체의 적분은 0입니다. 큰 반원의 기여는 $M_R=\frac1R\to0$이므로 조르당 보조정리에 의해 0이고, 작은 반원의 기여는 위 보조정리에 의해 $-i\pi$입니다. 따라서

$$
\operatorname{P.V.}\int_{-\infty}^{\infty}\frac{e^{ix}}{x}dx-i\pi=0
\quad\Longrightarrow\quad
\operatorname{P.V.}\int_{-\infty}^{\infty}\frac{e^{ix}}{x}dx=i\pi
$$

입니다. 허수부를 읽으면 $\int_{-\infty}^{\infty}\frac{\sin x}{x}dx=\pi$이고, $\frac{\sin x}{x}$가 짝함수이므로 $\int_0^\infty\frac{\sin x}{x}dx=\frac{\pi}{2}$입니다. 여기서 $\frac{\sin x}{x}$는 원점에서 제거가능특이점이라 주요값을 쓸 필요가 없고, 주요값은 $\frac{\cos x}{x}$ 쪽에만 필요합니다.

**예제 6.** $\displaystyle\int_{-\infty}^{\infty}\frac{\sin x}{x(x^2+1)}dx$를 계산합니다.

$f(z)=\frac{e^{iz}}{z(z^2+1)}$을 잡습니다. 실축 위 단순극은 $z=0$이고 유수는 $\frac{1}{0+1}=1$입니다. 상반평면의 단순극은 $z=i$이고

$$
\operatorname{Res}_{z=i}f=\frac{e^{-1}}{i\cdot2i}=-\frac{1}{2e}
$$

입니다. $M_R\sim\frac{1}{R^3}\to0$이므로 큰 반원의 기여는 0입니다. 위 공식에 대입하면

$$
\operatorname{P.V.}\int_{-\infty}^{\infty}\frac{e^{ix}}{x(x^2+1)}dx
=2\pi i\left(-\frac{1}{2e}\right)+i\pi\cdot1=i\pi\left(1-\frac1e\right)
$$

이고, 허수부를 읽으면 $\int_{-\infty}^{\infty}\frac{\sin x}{x(x^2+1)}dx=\pi\left(1-e^{-1}\right)$입니다.

> **문제 1.** (기초) 작은 반원의 기여가 $-i\pi\operatorname{Res}$이고 $+i\pi\operatorname{Res}$가 아닌 이유를 말하십시오.
> **답.** 반원을 편각이 감소하는 음의 방향으로 지나가기 때문입니다.
> **풀이.** 실축을 왼쪽에서 오른쪽으로 진행하면서 극 위로 우회하므로 편각이 $\pi$에서 $0$으로 줄어듭니다. 각의 변화량이 $-\pi$이므로 완전한 원의 $2\pi i$ 대신 $-i\pi$가 나옵니다. 이 반원의 기여는 경로 적분의 일부이므로 이항하면 주요값 쪽에 $+i\pi\operatorname{Res}$로 더해집니다.

> **문제 2.** (표준) $\operatorname{P.V.}\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2-1}$을 구하십시오.
> **답.** $0$입니다.
> **풀이.** 실축 위 단순극은 $z=\pm1$이고 상반평면에는 극이 없습니다. 유수는 $z=1$에서 $\frac{1}{2}$, $z=-1$에서 $-\frac12$입니다. 차수 차이가 2이므로 큰 반원의 기여는 0이고, 주요값은 $i\pi\left(\frac12-\frac12\right)=0$입니다.

> **문제 3.** (심화) $\displaystyle\int_0^\infty\frac{\sin^2x}{x^2}dx=\frac{\pi}{2}$임을 예제 5의 결과에서 유도하십시오.
> **답.** $\sin^2x=\frac{1-\cos2x}{2}$로 바꾸고 부분적분을 쓰면 $\int_0^\infty\frac{\sin 2x}{x}dx$로 환원됩니다.
> **풀이.** $\int_0^\infty\frac{\sin^2x}{x^2}dx$에서 $u=\sin^2x$, $v'=x^{-2}$로 부분적분하면 경계항이 0이고 $\int_0^\infty\frac{2\sin x\cos x}{x}dx=\int_0^\infty\frac{\sin 2x}{x}dx$가 남습니다. $t=2x$로 치환하면 이 값은 $\int_0^\infty\frac{\sin t}{t}dt=\frac{\pi}{2}$입니다.

### 2.6 계산 절차의 정리

문제를 보고 경로를 고르는 순서는 다음과 같이 고정할 수 있습니다.

1. 적분 구간을 확인합니다. $[0,2\pi]$ 같은 한 주기면 단위원 경로, $(-\infty,\infty)$면 반원 경로, $[0,\infty)$면 짝홀 대칭이나 열쇠구멍 경로를 검토합니다.
2. 피적분함수를 복소함수로 승격합니다. $\cos,\sin$은 $e^{imz}$로 묶고, $x^{a-1}$이나 $\ln x$가 있으면 분지를 먼저 고정합니다.
3. 특이점의 위치와 위수를 구하고, 경로 내부에 있는 것과 실축 위에 있는 것을 구분합니다.
4. 보조 경로의 기여가 0인지 확인합니다. 유리함수는 차수 차이 2 이상에서 ML 추정, 지수 인자가 있으면 조르당 보조정리, 분지점 근방은 $\varepsilon^{a}$ 추정을 씁니다.
5. 유수를 계산합니다. 단순극은 $\frac{g(z_0)}{h'(z_0)}$, 위수 $m$ 극은 $(m-1)$번 미분 공식이며, 진성특이점은 로랑 전개로 읽습니다.
6. 유수정리로 항등식을 세우고 필요한 실수부나 허수부를 읽습니다. 짝함수면 절반을 취해 $[0,\infty)$ 값을 얻고, 실적분이므로 결과가 실수인지 검산합니다.

> **문제 1.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{\sin 3x}{x^4+1}dx$의 값을 계산 없이 판정하십시오.
> **답.** $0$입니다.
> **풀이.** 피적분함수는 홀함수와 짝함수의 곱이므로 홀함수이고, 적분이 절대수렴하므로 대칭 구간의 값이 0입니다. 유수정리를 쓰면 $\frac{e^{3iz}}{z^4+1}$의 적분에서 허수부가 0으로 나오는 것과 같은 결론입니다.

> **문제 2.** (표준) $\displaystyle\int_0^{\infty}\frac{dx}{(x^2+1)^2}$에 어떤 경로와 어떤 유수 공식이 필요한지 밝히고 값을 구하십시오.
> **답.** 반원 경로와 위수 2 극의 유수 공식이 필요하며 값은 $\frac{\pi}{4}$입니다.
> **풀이.** 짝함수이므로 전구간 적분의 절반입니다. 차수 차이가 4이므로 반원호의 기여는 0입니다. $z=i$는 위수 2의 극이므로 $\frac{d}{dz}\frac{1}{(z+i)^2}\big|_{z=i}=-\frac{2}{(2i)^3}=-\frac{2}{-8i}=\frac{1}{4i}$입니다. 전구간 적분은 $2\pi i\cdot\frac{1}{4i}=\frac{\pi}{2}$이므로 구하는 값은 $\frac{\pi}{4}$입니다.

## 3. 유형 총정리(치트시트)

| 유형 | 경로 | 조건과 공식 |
|---|---|---|
| 유리함수 전구간 | 반원 경로 | $\deg Q\ge\deg P+2$, 실축에 극 없음, $2\pi i\sum_{\operatorname{Im}>0}\operatorname{Res}$ |
| 짝함수 반구간 | 반원 경로 | 전구간 값의 절반 |
| 삼각함수 한 주기 | 단위원 | $\cos\theta=\frac{z+z^{-1}}{2}$, $\sin\theta=\frac{z-z^{-1}}{2i}$, $d\theta=\frac{dz}{iz}$ |
| 표준 꼴 | 단위원 | $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}$, $a>|b|$ |
| 푸리에 꼴 | 반원 경로 | $\cos,\sin\to e^{imz}$, 조르당 보조정리로 $M_R\to0$만 확인 |
| 분지절단 | 열쇠구멍 | $z^{a-1}$은 $0<\arg z<2\pi$로 고정, $\int_0^\infty\frac{x^{a-1}}{1+x}dx=\frac{\pi}{\sin\pi a}$ |
| 실축 위 단순극 | 우회 반원 | 기여 $-i\pi\operatorname{Res}$, 주요값에는 $+i\pi\operatorname{Res}$로 더한다 |
| 반원호 소멸 판정 | ML 또는 조르당 | ML은 $\pi RM_R$, 조르당은 $\frac{\pi M_R}{m}$ |
| 단순극 유수 | 공통 | $\frac{g(z_0)}{h'(z_0)}$ |
| 위수 $m$ 극 유수 | 공통 | $\frac{1}{(m-1)!}\left[(z-z_0)^mf\right]^{(m-1)}(z_0)$ |
| 검산 | 공통 | 값은 실수여야 하고, 홀함수의 대칭 적분은 0 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+9}$를 구하십시오.
> **답.** $\dfrac{\pi}{3}$입니다.
> **풀이.** 상반평면 극은 $z=3i$이고 유수는 $\frac{1}{6i}$입니다. 값은 $2\pi i\cdot\frac{1}{6i}=\frac{\pi}{3}$입니다.

> **문제 2.** (기초) $\displaystyle\int_0^{2\pi}\frac{d\theta}{3+2\sin\theta}$를 구하십시오.
> **답.** $\dfrac{2\pi}{\sqrt5}$입니다.
> **풀이.** 치환하면 분모가 $3+\frac{z-z^{-1}}{i}=\frac{z^2+3iz-1}{iz}$이므로 적분은 $\oint_{|z|=1}\frac{dz}{z^2+3iz-1}$입니다. 근은 $z=\frac{-3i\pm i\sqrt5}{2}$이고 내부에 있는 것은 $z_+=\frac{(\sqrt5-3)i}{2}$입니다. 유수는 $\frac{1}{2z_++3i}=\frac{1}{i\sqrt5}$이므로 값은 $2\pi i\cdot\frac{1}{i\sqrt5}=\frac{2\pi}{\sqrt5}$입니다.

> **문제 3.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{x^2}{x^4+1}dx$를 구하십시오.
> **답.** $\dfrac{\pi}{\sqrt2}$입니다.
> **풀이.** 상반평면 극은 $e^{i\pi/4},e^{3i\pi/4}$이고 유수는 $\frac{z_k^2}{4z_k^3}=\frac{1}{4z_k}$입니다. $\frac{1}{4}\left(e^{-i\pi/4}+e^{-3i\pi/4}\right)=\frac14\left(-\frac{\sqrt2}{2}i\cdot2\right)=-\frac{\sqrt2}{4}i$이므로 값은 $2\pi i\cdot\left(-\frac{\sqrt2}{4}i\right)=\frac{\pi}{\sqrt2}$입니다.

> **문제 4.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{x^2+x+1}dx$를 계산할 때 쓸 극과 유수를 밝히십시오.
> **답.** 상반평면 극은 $z=\frac{-1+\sqrt3 i}{2}$이고 유수는 $\frac{e^{iz_0}}{2z_0+1}=\frac{e^{iz_0}}{\sqrt3 i}$입니다.
> **풀이.** $z^2+z+1=0$의 근은 $\frac{-1\pm\sqrt3i}{2}$이고 상반평면 쪽은 $z_0=\frac{-1+\sqrt3i}{2}$입니다. 분모 미분은 $2z+1$이므로 $2z_0+1=\sqrt3 i$입니다. $e^{iz_0}=e^{-\sqrt3/2}e^{-i/2}$이므로 적분값은 $2\pi i\cdot\frac{e^{-\sqrt3/2}e^{-i/2}}{\sqrt3 i}$의 실수부, 즉 $\frac{2\pi}{\sqrt3}e^{-\sqrt3/2}\cos\frac12$입니다.

> **문제 5.** (표준) $\displaystyle\int_0^\infty\frac{x^{1/2}}{1+x^2}dx$를 계산할 경로를 밝히고 값을 구하십시오.
> **답.** 분지절단을 양의 실축에 둔 열쇠구멍 경로를 쓰며 값은 $\dfrac{\pi}{\sqrt2}$입니다.
> **풀이.** $x=t^2$로 치환하면 $2\int_0^\infty\frac{t^2}{1+t^4}dt$이고, 이는 종합 문제 3의 짝함수 성질에 의해 $2\cdot\frac12\cdot\frac{\pi}{\sqrt2}=\frac{\pi}{\sqrt2}$입니다. 열쇠구멍 경로로 직접 하면 $z^{1/2}$의 분지를 $0<\arg z<2\pi$로 고정하고 $z=\pm i$의 유수를 모아 같은 값을 얻습니다.

> **문제 6.** (심화) $\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{(x^2+1)^2}dx$를 구하십시오.
> **답.** $\dfrac{\pi}{e}$입니다.
> **풀이.** $\frac{e^{iz}}{(z^2+1)^2}$의 상반평면 극은 $z=i$이고 위수 2입니다. $\varphi(z)=\frac{e^{iz}}{(z+i)^2}$에 대해 $\varphi'(z)=\frac{ie^{iz}(z+i)^2-2(z+i)e^{iz}}{(z+i)^4}=\frac{e^{iz}\left[i(z+i)-2\right]}{(z+i)^3}$이고 $z=i$를 넣으면 $\frac{e^{-1}(i\cdot2i-2)}{(2i)^3}=\frac{e^{-1}(-4)}{-8i}=\frac{1}{2ie}$입니다. 따라서 값은 $2\pi i\cdot\frac{1}{2ie}=\frac{\pi}{e}$입니다.

> **문제 7.** (심화) $\operatorname{P.V.}\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x(x^2+4)}$를 구하십시오.
> **답.** $0$입니다.
> **풀이.** 실축 위 단순극 $z=0$의 유수는 $\frac{1}{4}$이고, 상반평면 단순극 $z=2i$의 유수는 $\frac{1}{2i\cdot4i}=-\frac18$입니다. 차수 차이가 3이므로 큰 반원의 기여는 0입니다. 주요값은 $2\pi i\left(-\frac18\right)+i\pi\cdot\frac14=-\frac{\pi i}{4}+\frac{\pi i}{4}=0$입니다. 피적분함수가 홀함수이므로 주요값이 0인 것과도 일치합니다.

> **문제 8.** (심화) $\displaystyle\int_0^{2\pi}\frac{d\theta}{(2+\cos\theta)^2}$를 계산할 때 어떤 유수 공식이 필요한지 밝히고 값을 구하십시오.
> **답.** 위수 2 극의 유수 공식이 필요하며 값은 $\dfrac{4\pi}{3\sqrt3}$입니다.
> **풀이.** 치환하면 $2+\cos\theta=\frac{z^2+4z+1}{2z}$이므로 적분은 $\oint_{|z|=1}\frac{4z^2}{(z^2+4z+1)^2}\cdot\frac{dz}{iz}=\frac{4}{i}\oint\frac{z\,dz}{(z-\alpha)^2(z-\beta)^2}$이고 $\alpha=-2+\sqrt3$, $\beta=-2-\sqrt3$입니다. 내부의 극은 $z=\alpha$ 하나이고 위수 2이므로 $\frac{d}{dz}\frac{z}{(z-\beta)^2}\big|_{z=\alpha}$를 계산합니다. $\alpha-\beta=2\sqrt3$이므로 값은 $\frac{(\alpha-\beta)^2-2\alpha(\alpha-\beta)}{(\alpha-\beta)^4}=\frac{12-2(-2+\sqrt3)(2\sqrt3)}{144}=\frac{12+8\sqrt3-12}{144}=\frac{\sqrt3}{18}$입니다. 따라서 적분값은 $\frac{4}{i}\cdot2\pi i\cdot\frac{\sqrt3}{18}=\frac{4\pi\sqrt3}{9}=\frac{4\pi}{3\sqrt3}$입니다.

## 5. 스스로 점검

1. 유리함수 전구간 적분에 반원 경로를 쓸 수 있는 조건을 말할 수 있는가?
2. 반원호의 기여가 0임을 ML 부등식으로 보일 수 있는가?
3. $z=e^{i\theta}$ 치환으로 삼각함수 적분을 단위원 적분으로 바꿀 수 있는가?
4. 조르당 보조정리를 진술하고 ML 추정과의 차이를 설명할 수 있는가?
5. 열쇠구멍 경로에서 아래쪽 선분이 $-e^{2\pi ia}$ 배로 나오는 이유를 말할 수 있는가?
6. 실축 위 단순극이 주요값에 $i\pi\operatorname{Res}$로 기여하는 이유를 설명할 수 있는가?
7. $\int_0^\infty\frac{\sin x}{x}dx=\frac{\pi}{2}$의 계산 흐름을 재현할 수 있는가?
8. 주어진 실적분을 보고 경로와 보조정리를 순서대로 선택할 수 있는가?

**정답 요지.** 1. $\deg Q\ge\deg P+2$이고 실축에 극이 없을 때. 2. $|f|\le CR^{-2}$와 길이 $\pi R$의 곱이 $\frac{\pi C}{R}\to0$. 3. $\cos\theta=\frac{z+z^{-1}}{2}$, $\sin\theta=\frac{z-z^{-1}}{2i}$, $d\theta=\frac{dz}{iz}$를 대입하고 $|z|<1$ 내부 유수만 모은다. 4. 상계가 $\frac{\pi M_R}{m}$이므로 $M_R\to0$만으로 충분하며, ML은 $\pi RM_R$이라 차수 차이 1에서는 쓸 수 없다. 5. 절단 아래쪽에서 $\arg z=2\pi$이므로 $z^{a-1}$에 $e^{2\pi i(a-1)}$이 붙고 진행 방향이 반대라 부호가 바뀐다. 6. 우회 반원의 편각 변화가 $-\pi$라 기여가 $-i\pi\operatorname{Res}$이고, 이항하면 주요값 쪽에 $+i\pi\operatorname{Res}$가 남는다. 7. $\frac{e^{iz}}{z}$에 우회 반원 경로를 적용해 $\operatorname{P.V.}\int\frac{e^{ix}}{x}dx=i\pi$를 얻고 허수부를 절반으로 나눈다. 8. 구간 확인, 복소 승격, 특이점 분류, 보조 경로 소멸 확인, 유수 계산, 실수부나 허수부 읽기, 검산의 순서를 따른다.
