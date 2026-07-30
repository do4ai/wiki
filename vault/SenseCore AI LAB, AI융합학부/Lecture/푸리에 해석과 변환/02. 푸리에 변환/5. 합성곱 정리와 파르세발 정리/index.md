---
title: "5. 합성곱 정리와 파르세발 정리"
---
# 5강. 합성곱 정리와 파르세발 정리

## 이 강의에서 할 수 있게 되는 것

- 합성곱을 정의하고 교환법칙, 결합법칙, 분배법칙을 증명할 수 있습니다.
- 합성곱 정리로 시간 영역의 합성곱을 주파수 영역의 곱으로 바꿀 수 있습니다.
- 시간 영역의 곱이 주파수 영역에서 합성곱이 됨을 계수까지 정확히 쓸 수 있습니다.
- 상관과 자기상관을 정의하고 에너지 스펙트럼 밀도와 연결할 수 있습니다.
- 파르세발·플랑셰렐 정리를 증명하고 에너지 보존으로 해석할 수 있습니다.
- 델타함수의 변환쌍을 진술하고 임펄스 응답과 전달함수의 관계를 설명할 수 있습니다.

이 강의는 [4. 푸리에 변환의 정의와 성질](../4. 푸리에 변환의 정의와 성질/index.md) 강의의 변환쌍과 성질을 그대로 사용합니다. 여기서 얻는 전달함수 관점은 [9. 신호 처리와 필터링](../../04. 변환의 응용/9. 신호 처리와 필터링/index.md) 강의의 출발점입니다.

## 1. 오늘 쓸 기호

규약은 4강과 동일합니다. 변환은 $\hat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt$이고 $1/2\pi$는 역변환에만 붙입니다.

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $(f*g)(t)$ | 에프 콘볼루션 지 | $\displaystyle\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau$, 두 함수의 합성곱 |
| $(f\star g)(t)$ | 에프 스타 지 | $\displaystyle\int_{-\infty}^{\infty}\overline{f(\tau)}\,g(t+\tau)\,d\tau$, 두 함수의 상관 |
| $R_f(t)$ | 자기상관 함수 | $(f\star f)(t)$, 함수와 자기 자신의 상관 |
| $E[f]$ | 에너지 | $\displaystyle\int_{-\infty}^{\infty}|f(t)|^{2}\,dt$ |
| $\lVert f\rVert_2$ | 에프의 $L^2$ 노름 | $\sqrt{E[f]}$ |
| $S_f(\omega)$ | 에너지 스펙트럼 밀도 | $|\hat f(\omega)|^{2}$ |
| $\delta(t)$ | 델타 | 원점에 질량 1이 모인 분포, $\int\delta(t)\varphi(t)\,dt=\varphi(0)$ |
| $h(t)$ | 임펄스 응답 | 입력이 $\delta$일 때 선형시불변 시스템의 출력 |
| $H(\omega)$ | 전달함수 | $\mathcal{F}[h]\,(\omega)$, 주파수 응답 |
| $\langle f,g\rangle$ | 에프와 지의 내적 | $\displaystyle\int_{-\infty}^{\infty}f(t)\overline{g(t)}\,dt$ |

## 2. 개념

### 2.1 합성곱의 정의와 성질

**정의.** 두 함수 $f,g$에 대해 다음 적분이 존재할 때 이를 합성곱이라고 합니다.

$$
(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)\,g(t-\tau)\,d\tau
$$

$g$의 인수가 $t-\tau$이므로 $g$를 좌우로 뒤집어 $t$만큼 밀어 놓고 $f$와 겹치는 부분의 면적을 재는 연산입니다. 결과는 $t$의 함수입니다. $f,g\in L^1(\mathbb{R})$이면 합성곱도 $L^1$에 속하고 $\lVert f*g\rVert_1\le\lVert f\rVert_1\lVert g\rVert_1$이 성립하므로 변환을 취할 수 있습니다.

세 가지 대수 성질이 성립합니다.

$$
f*g=g*f,\qquad (f*g)*h=f*(g*h),\qquad f*(g+h)=f*g+f*h
$$

교환법칙을 증명합니다. $s=t-\tau$로 치환하면 $\tau=t-s$이고 $d\tau=-ds$이며 적분 방향이 뒤집혀 다시 $-\infty$에서 $\infty$가 됩니다.

$$
(f*g)(t)=\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau=\int_{-\infty}^{\infty}f(t-s)g(s)\,ds=(g*f)(t)
$$

결합법칙은 이중적분의 순서 교환으로 나옵니다.

$$
\big((f*g)*h\big)(t)=\int\!\!\int f(\sigma)g(\tau-\sigma)h(t-\tau)\,d\sigma\,d\tau
$$

여기서 $\tau=\sigma+u$로 치환하면 피적분함수는 $f(\sigma)g(u)h(t-\sigma-u)$가 되고, 이는 $\big(f*(g*h)\big)(t)$의 이중적분과 같습니다. 분배법칙은 적분의 선형성에서 곧바로 나옵니다. $\square$

성질 하나를 더 기억합니다. 지지집합이 각각 $[a,b]$와 $[c,d]$인 함수의 합성곱은 $[a+c,b+d]$ 밖에서 0입니다. 겹치는 구간이 없으면 적분값이 0이기 때문입니다.

> **문제 1.** (기초) $f(t)=g(t)=1$ ($0\le t\le1$), 그 밖에서 0일 때 $(f*g)(0.5)$를 구하십시오.
> **답.** $0.5$입니다.
> **풀이.** $f(\tau)g(0.5-\tau)$가 0이 아니려면 $0\le\tau\le1$이면서 $0\le0.5-\tau\le1$, 즉 $-0.5\le\tau\le0.5$입니다. 두 조건의 교집합은 $0\le\tau\le0.5$이고 피적분함수는 1이므로 적분값은 구간 길이 $0.5$입니다.

> **문제 2.** (기초) 지지집합이 $[-1,2]$와 $[0,3]$인 두 함수의 합성곱은 어느 구간 밖에서 0인지 답하십시오.
> **답.** $[-1,5]$ 밖에서 0입니다.
> **풀이.** 지지집합의 양 끝을 각각 더합니다. 왼쪽 끝은 $-1+0=-1$, 오른쪽 끝은 $2+3=5$입니다. 이 밖에서는 두 함수가 겹치지 않아 적분값이 0입니다.

> **문제 3.** (표준) $f(t)=e^{-at}u(t)$와 자기 자신의 합성곱을 구하십시오. $a>0$입니다.
> **답.** $(f*f)(t)=te^{-at}$ ($t\ge0$), $t<0$에서 0입니다.
> **풀이.** $t\ge0$에서 $f(\tau)f(t-\tau)$가 0이 아닌 범위는 $0\le\tau\le t$입니다. 이때 피적분함수는 $e^{-a\tau}e^{-a(t-\tau)}=e^{-at}$로 $\tau$와 무관하므로 적분값은 $e^{-at}\cdot t$입니다. $t<0$이면 두 조건 $\tau\ge0$과 $t-\tau\ge0$을 함께 만족하는 $\tau$가 없어 0입니다.

### 2.2 합성곱 정리

**정리(합성곱 정리).** $f,g\in L^1(\mathbb{R})$이면

$$
\mathcal{F}[f*g]\,(\omega)=\hat f(\omega)\,\hat g(\omega)
$$

입니다. 즉 시간 영역의 합성곱은 주파수 영역의 점별 곱입니다.

증명을 봅니다. 정의를 대입하고 이중적분으로 씁니다.

$$
\mathcal{F}[f*g]\,(\omega)=\int_{-\infty}^{\infty}\left(\int_{-\infty}^{\infty}f(\tau)g(t-\tau)\,d\tau\right)e^{-i\omega t}\,dt
$$

피적분함수의 절댓값 이중적분이 $\lVert f\rVert_1\lVert g\rVert_1$로 유한하므로 푸비니 정리에 의해 적분 순서를 바꿀 수 있습니다. 안쪽에서 $s=t-\tau$로 치환하면 $e^{-i\omega t}=e^{-i\omega\tau}e^{-i\omega s}$입니다.

$$
=\int f(\tau)\left(\int g(t-\tau)e^{-i\omega t}\,dt\right)d\tau
=\int f(\tau)e^{-i\omega\tau}\,d\tau\int g(s)e^{-i\omega s}\,ds
=\hat f(\omega)\hat g(\omega)
$$

두 적분이 분리되므로 결과는 두 변환의 곱입니다. $\square$

역방향으로 읽으면 $\mathcal{F}^{-1}[\hat f\hat g]=f*g$입니다. 계산에서는 이 방향을 더 자주 씁니다. 곱을 두 변환의 곱으로 쪼갤 수 있으면 어려운 합성곱 적분을 계산하지 않고 답을 얻습니다.

**예제 1. 사각펄스의 자기 합성곱.** $p(t)=1$ ($|t|\le a$), 밖에서 0으로 둡니다. 4강에서 $\hat p(\omega)=2a\operatorname{sinc}(a\omega)$였으므로

$$
\mathcal{F}[p*p]\,(\omega)=\hat p(\omega)^{2}=\frac{4\sin^{2}(a\omega)}{\omega^{2}}
$$

입니다. 한편 직접 계산하면 $t\ge0$에서 겹치는 구간의 길이가 $2a-t$ ($0\le t\le2a$)이므로

$$
(p*p)(t)=
\begin{cases}
2a-|t| & |t|\le 2a\\
0 & |t|>2a
\end{cases}
$$

로 삼각펄스입니다. 사각펄스 두 개의 합성곱이 삼각펄스이고, 그 스펙트럼이 sinc의 제곱이라는 대응을 얻습니다. 제곱이 되었으므로 고주파 감쇠가 $1/\omega$에서 $1/\omega^{2}$로 빨라졌고, 이는 삼각펄스가 사각펄스보다 매끄럽다는 사실과 맞습니다.

**예제 2. 지수감쇠의 자기 합성곱.** 2.1절 문제 3에서 $(f*f)(t)=te^{-at}u(t)$였습니다. 합성곱 정리로 검산합니다. $\hat f(\omega)=\frac{1}{a+i\omega}$이므로

$$
\mathcal{F}[f*f]\,(\omega)=\frac{1}{(a+i\omega)^{2}}
$$

입니다. 한편 4강의 $t$ 곱 규칙으로 $\mathcal{F}[te^{-at}u(t)]=i\frac{d}{d\omega}\frac{1}{a+i\omega}=i\cdot\frac{-i}{(a+i\omega)^{2}}=\frac{1}{(a+i\omega)^{2}}$입니다. 두 결과가 일치합니다.

> **문제 1.** (기초) $\hat f(\omega)=\dfrac{1}{1+i\omega}$이고 $\hat g(\omega)=\dfrac{1}{2+i\omega}$일 때 $\mathcal{F}[f*g]$를 쓰십시오.
> **답.** $\dfrac{1}{(1+i\omega)(2+i\omega)}$입니다.
> **풀이.** 합성곱 정리로 두 변환을 곱하기만 합니다. 시간 영역에서는 $\int_{0}^{t}e^{-\tau}e^{-2(t-\tau)}d\tau=e^{-t}-e^{-2t}$라는 적분을 해야 하지만, 주파수 영역에서는 곱셈으로 끝납니다.

> **문제 2.** (표준) $\mathcal{F}^{-1}\!\left[\dfrac{1}{(2+i\omega)^{2}}\right]$을 구하십시오.
> **답.** $te^{-2t}u(t)$입니다.
> **풀이.** 주어진 함수는 $\frac{1}{2+i\omega}$의 제곱이므로 합성곱 정리의 역방향에 따라 $e^{-2t}u(t)$와 자기 자신의 합성곱입니다. 2.1절 문제 3에서 그 값은 $te^{-2t}u(t)$입니다.

### 2.3 곱의 변환과 상관

시간 영역의 곱은 주파수 영역에서 합성곱이 됩니다. 다만 이 규약에서는 계수 $\frac{1}{2\pi}$가 붙습니다.

$$
\mathcal{F}[f\,g]\,(\omega)=\frac{1}{2\pi}\big(\hat f*\hat g\big)(\omega)
$$

증명은 $f$를 역변환 표현으로 바꾸고 순서를 교환하는 것입니다.

$$
\mathcal{F}[fg]\,(\omega)=\int\left(\frac{1}{2\pi}\int\hat f(\alpha)e^{i\alpha t}\,d\alpha\right)g(t)e^{-i\omega t}\,dt
=\frac{1}{2\pi}\int\hat f(\alpha)\left(\int g(t)e^{-i(\omega-\alpha)t}\,dt\right)d\alpha
$$

안쪽 적분이 $\hat g(\omega-\alpha)$이므로 전체는 $\frac{1}{2\pi}\int\hat f(\alpha)\hat g(\omega-\alpha)\,d\alpha$, 즉 $\frac{1}{2\pi}(\hat f*\hat g)(\omega)$입니다. $\square$

이 결과는 4강의 변조 규칙을 일반화한 것입니다. $g(t)=e^{i\omega_0 t}$처럼 하나의 진동수만 가진 함수를 곱하면 스펙트럼이 그 진동수만큼 평행이동하고, 여러 진동수를 가진 함수를 곱하면 스펙트럼이 그 모양으로 번집니다. 6강에서 창함수를 곱할 때 스펙트럼이 퍼지는 현상, 곧 누출이 바로 이 정리의 결과입니다.

**상관.** 겹침을 재는 또 다른 연산이 상관입니다.

$$
(f\star g)(t)=\int_{-\infty}^{\infty}\overline{f(\tau)}\,g(t+\tau)\,d\tau
$$

합성곱과 달리 한쪽을 뒤집지 않고 그대로 밀어 겹칩니다. 실함수에서는 $(f\star g)(t)=(f(-\cdot)*g)(t)$이므로 두 연산은 반사 하나만큼 차이가 납니다. 변환은 다음과 같습니다.

$$
\mathcal{F}[f\star g]\,(\omega)=\overline{\hat f(\omega)}\,\hat g(\omega)
$$

특히 $g=f$로 두면 자기상관 $R_f(t)=(f\star f)(t)$이고

$$
\mathcal{F}[R_f]\,(\omega)=|\hat f(\omega)|^{2}=S_f(\omega)
$$

입니다. 자기상관의 변환이 에너지 스펙트럼 밀도라는 이 관계를 위너-킨친 관계라고 합니다. 자기상관은 $t=0$에서 최대이며 그 값이 신호의 에너지 $E[f]$입니다. 신호를 얼마나 밀어도 자기 자신과의 겹침이 원래 위치보다 커질 수 없기 때문입니다.

> **문제 1.** (표준) $f(t)=e^{-a|t|}$의 자기상관의 변환을 구하십시오.
> **답.** $S_f(\omega)=\dfrac{4a^{2}}{(a^{2}+\omega^{2})^{2}}$입니다.
> **풀이.** 4강에서 $\hat f(\omega)=\frac{2a}{a^{2}+\omega^{2}}$입니다. 실 짝함수이므로 $\overline{\hat f}=\hat f$이고 $S_f=|\hat f|^{2}$은 위 식입니다. 위너-킨친 관계에 따라 이 함수의 역변환이 자기상관입니다.

> **문제 2.** (심화) 자기상관이 $t=0$에서 최대임을 코시-슈바르츠 부등식으로 보이십시오.
> **답.** $|R_f(t)|\le\lVert f\rVert_2^{2}=R_f(0)$입니다.
> **풀이.** $R_f(t)=\int\overline{f(\tau)}f(t+\tau)\,d\tau$은 $f$와 $f$를 $t$만큼 민 함수의 내적입니다. 코시-슈바르츠 부등식에서 $|R_f(t)|\le\lVert f\rVert_2\lVert f(\cdot+t)\rVert_2=\lVert f\rVert_2^{2}$입니다. 평행이동은 노름을 바꾸지 않기 때문입니다. 한편 $R_f(0)=\int|f|^{2}=\lVert f\rVert_2^{2}$이므로 최대값이 $t=0$에서 달성됩니다. $\square$

### 2.4 파르세발 정리와 플랑셰렐 정리

**정리(파르세발 정리, 일반형).** $f,g$가 적절한 조건을 만족하면

$$
\int_{-\infty}^{\infty}f(t)\overline{g(t)}\,dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)\overline{\hat g(\omega)}\,d\omega
$$

입니다. 특히 $g=f$로 두면 다음 플랑셰렐 정리를 얻습니다.

$$
\int_{-\infty}^{\infty}|f(t)|^{2}\,dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}|\hat f(\omega)|^{2}\,d\omega
$$

증명을 봅니다. $\overline{g(t)}$를 역변환 표현의 공액으로 바꿉니다. $g(t)=\frac{1}{2\pi}\int\hat g(\omega)e^{i\omega t}d\omega$이므로 $\overline{g(t)}=\frac{1}{2\pi}\int\overline{\hat g(\omega)}e^{-i\omega t}\,d\omega$입니다. 대입하고 푸비니 정리로 순서를 바꿉니다.

$$
\int f(t)\overline{g(t)}\,dt
=\frac{1}{2\pi}\int\overline{\hat g(\omega)}\left(\int f(t)e^{-i\omega t}\,dt\right)d\omega
=\frac{1}{2\pi}\int\hat f(\omega)\overline{\hat g(\omega)}\,d\omega
$$

이것이 주장하는 식입니다. $\square$

해석은 다음과 같습니다. $\int|f|^{2}$은 신호의 전체 에너지이고, $\frac{1}{2\pi}|\hat f(\omega)|^{2}$은 단위 각주파수당 에너지 밀도입니다. 변환은 에너지를 만들거나 없애지 않고 진동수별로 재배치할 뿐입니다. 즉 $\mathcal{F}$는 $\frac{1}{\sqrt{2\pi}}$로 규격을 맞추면 $L^2$에서 등거리 변환입니다. 일반형은 내적을 보존한다는 더 강한 진술이며, 파르세발 정리를 각도까지 보존하는 회전으로 읽게 해 줍니다.

**예제 3. 적분값을 파르세발로 얻기.** $p(t)=1$ ($|t|\le1$), 밖에서 0인 사각펄스를 씁니다. 시간 영역의 에너지는 $\int_{-1}^{1}1\,dt=2$입니다. 주파수 영역에서는 $\hat p(\omega)=\frac{2\sin\omega}{\omega}$이므로

$$
2=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{4\sin^{2}\omega}{\omega^{2}}\,d\omega
\quad\Longrightarrow\quad
\int_{-\infty}^{\infty}\frac{\sin^{2}\omega}{\omega^{2}}\,d\omega=\pi
$$

입니다. 직접 계산이 번거로운 이상적분이 에너지 등식 한 줄로 나왔습니다. 같은 방식으로 $f(t)=e^{-at}u(t)$를 쓰면 $\int_{0}^{\infty}e^{-2at}dt=\frac{1}{2a}$이고 $\frac{1}{2\pi}\int\frac{d\omega}{a^{2}+\omega^{2}}=\frac{1}{2\pi}\cdot\frac{\pi}{a}=\frac{1}{2a}$로 양변이 맞습니다.

> **문제 1.** (기초) 파르세발 정리에서 $1/2\pi$가 어느 쪽에 붙는지 답하십시오.
> **답.** 주파수 영역 적분 쪽에 붙습니다.
> **풀이.** 이 교본은 역변환에만 $\frac{1}{2\pi}$를 붙이는 규약을 쓰므로 $\int|f|^{2}dt=\frac{1}{2\pi}\int|\hat f|^{2}d\omega$입니다. 대칭 규약에서는 양변에 계수가 없어지므로 규약을 먼저 확인해야 합니다.

> **문제 2.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{d\omega}{(1+\omega^{2})^{2}}$를 파르세발 정리로 구하십시오.
> **답.** $\dfrac{\pi}{2}$입니다.
> **풀이.** $f(t)=\frac12 e^{-|t|}$로 두면 4강에서 $\hat f(\omega)=\frac{1}{1+\omega^{2}}$입니다. 시간 영역 에너지는 $\int\frac14e^{-2|t|}dt=\frac14\cdot2\cdot\frac12=\frac14$입니다. 플랑셰렐 정리로 $\frac14=\frac{1}{2\pi}\int\frac{d\omega}{(1+\omega^{2})^{2}}$이므로 적분값은 $\frac{\pi}{2}$입니다.

> **문제 3.** (표준) 삼각펄스 $(p*p)(t)$의 에너지를 이용해 $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^{4}\omega}{\omega^{4}}\,d\omega$를 구하십시오. 여기서 $p$는 $a=1$인 사각펄스입니다.
> **답.** $\dfrac{2\pi}{3}$입니다.
> **풀이.** $(p*p)(t)=2-|t|$ ($|t|\le2$)이므로 에너지는 $2\int_{0}^{2}(2-t)^{2}dt=2\cdot\frac{8}{3}=\frac{16}{3}$입니다. 변환은 $\frac{4\sin^{2}\omega}{\omega^{2}}$이므로 플랑셰렐 정리에서 $\frac{16}{3}=\frac{1}{2\pi}\int\frac{16\sin^{4}\omega}{\omega^{4}}d\omega$입니다. 정리하면 $\int\frac{\sin^{4}\omega}{\omega^{4}}d\omega=\frac{2\pi}{3}$입니다.

### 2.5 델타함수와 분포적 확장

$L^1$ 조건은 편리하지만 상수함수, 사인, 코사인처럼 절대적분가능하지 않은 함수를 배제합니다. 이들의 스펙트럼을 다루려면 델타함수를 허용해야 합니다.

델타함수 $\delta$는 통상적 함수가 아니라 시험함수에 작용하는 규칙, 즉 분포로 정의합니다.

$$
\int_{-\infty}^{\infty}\delta(t)\varphi(t)\,dt=\varphi(0)
$$

이 규칙만으로 변환이 결정됩니다.

$$
\mathcal{F}[\delta]\,(\omega)=\int\delta(t)e^{-i\omega t}\,dt=e^{-i\omega\cdot0}=1
$$

모든 진동수에 균등하게 퍼진 스펙트럼입니다. 4강 2.3절에서 면적을 1로 고정한 사각펄스의 변환이 1로 수렴했던 결과와 같습니다. 여기에 쌍대성을 적용하면 상수함수의 변환을 얻습니다.

$$
\mathcal{F}[1]\,(\omega)=2\pi\delta(\omega),\qquad
\mathcal{F}\!\left[e^{i\omega_0t}\right]\,(\omega)=2\pi\delta(\omega-\omega_0),\qquad
\mathcal{F}[\cos\omega_0t]\,(\omega)=\pi\delta(\omega-\omega_0)+\pi\delta(\omega+\omega_0)
$$

또한 델타는 합성곱의 항등원입니다.

$$
(f*\delta)(t)=\int f(\tau)\delta(t-\tau)\,d\tau=f(t),\qquad
(f*\delta(\cdot-t_0))(t)=f(t-t_0)
$$

변환 쪽에서 보면 $\hat f\cdot1=\hat f$이고 $\hat f\cdot e^{-i\omega t_0}$이므로 4강의 시간이동 규칙과 정확히 맞물립니다. 이 확장 덕분에 합성곱 정리와 파르세발 정리를 주기함수와 상수 성분까지 넓혀 쓸 수 있고, 6강의 임펄스열도 이 언어로 다룹니다.

> **문제 1.** (기초) $\mathcal{F}[\sin\omega_0 t]$를 구하십시오.
> **답.** $-i\pi\delta(\omega-\omega_0)+i\pi\delta(\omega+\omega_0)$입니다.
> **풀이.** $\sin\omega_0t=\frac{1}{2i}(e^{i\omega_0t}-e^{-i\omega_0t})$이므로 각 항의 변환 $2\pi\delta(\omega\mp\omega_0)$을 대입하면 $\frac{2\pi}{2i}\left(\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\right)$입니다. $\frac{1}{i}=-i$를 정리하면 위 식이며, 실 홀함수의 변환이 순허수라는 4강의 대칭성과 일치합니다.

> **문제 2.** (표준) $\mathcal{F}[u(t)]=\pi\delta(\omega)+\dfrac{1}{i\omega}$가 되는 까닭을 설명하십시오.
> **답.** 단위계단은 상수 $\frac12$과 부호함수 $\frac12\operatorname{sgn}(t)$의 합이기 때문입니다.
> **풀이.** $u(t)=\frac12+\frac12\operatorname{sgn}(t)$입니다. 상수 $\frac12$의 변환은 $\pi\delta(\omega)$이고 $\operatorname{sgn}$의 변환은 $\frac{2}{i\omega}$이므로 절반을 취하면 $\frac{1}{i\omega}$입니다. 두 항을 더하면 위 식입니다. 4강 적분 규칙에서 $\hat f(0)\ne0$일 때 델타 항이 추가된다고 했던 것이 이 결과입니다.

### 2.6 임펄스 응답과 전달함수

선형시불변 시스템은 입력 $x$를 출력 $y$로 보내는 사상 $T$ 중에서 두 조건을 만족하는 것입니다. 선형성은 $T[\alpha x_1+\beta x_2]=\alpha T[x_1]+\beta T[x_2]$이고, 시불변성은 입력을 $t_0$만큼 밀면 출력도 그만큼 밀린다는 조건입니다. 이 두 조건만으로 시스템은 하나의 함수로 완전히 결정됩니다.

입력이 델타일 때의 출력 $h=T[\delta]$를 임펄스 응답이라고 합니다. 임의의 입력은 $x=x*\delta$로 쓸 수 있고, 이는 델타를 여러 위치에 놓고 $x$의 값으로 가중한 합입니다. 선형성과 시불변성으로 각 델타의 출력은 그만큼 밀린 $h$이므로

$$
y(t)=(x*h)(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau
$$

입니다. 여기에 합성곱 정리를 적용하면 다음을 얻습니다.

$$
\hat y(\omega)=H(\omega)\hat x(\omega),\qquad H(\omega)=\mathcal{F}[h]\,(\omega)
$$

$H$를 전달함수 또는 주파수 응답이라고 합니다. 시간 영역에서 적분으로 얽혀 있던 시스템의 작용이 주파수 영역에서는 진동수별 곱셈입니다. $|H(\omega)|$는 그 진동수 성분을 몇 배로 키우거나 줄이는지, $\arg H(\omega)$는 얼마나 지연시키는지를 나타냅니다. 필터 설계가 곧 $H$의 모양을 정하는 일이 되는 이유입니다.

**예제 4. 저역통과 필터.** $h(t)=\frac{1}{\tau}e^{-t/\tau}u(t)$인 시스템을 봅니다. 4강 예제 2에서

$$
H(\omega)=\frac{1}{\tau}\cdot\frac{1}{\frac1\tau+i\omega}=\frac{1}{1+i\omega\tau},
\qquad
|H(\omega)|=\frac{1}{\sqrt{1+\omega^{2}\tau^{2}}}
$$

입니다. $\omega\to0$에서 $|H|\to1$이라 낮은 진동수는 그대로 통과하고, $\omega\to\infty$에서 $|H|\to0$이라 높은 진동수는 막힙니다. $|H|$가 $1/\sqrt2$가 되는 $\omega=1/\tau$가 차단 진동수입니다. 시간상수 $\tau$를 키우면 차단 진동수가 낮아지고 출력이 더 매끄러워집니다.

> **문제 1.** (표준) 임펄스 응답이 $h(t)=\delta(t)-\dfrac{1}{\tau}e^{-t/\tau}u(t)$인 시스템의 전달함수를 구하고 성격을 판정하십시오.
> **답.** $H(\omega)=\dfrac{i\omega\tau}{1+i\omega\tau}$이고 고역통과 필터입니다.
> **풀이.** $\mathcal{F}[\delta]=1$이고 두 번째 항의 변환은 예제 4의 $\frac{1}{1+i\omega\tau}$입니다. 차를 정리하면 $1-\frac{1}{1+i\omega\tau}=\frac{i\omega\tau}{1+i\omega\tau}$입니다. $\omega\to0$에서 0, $\omega\to\infty$에서 1이므로 낮은 진동수를 막고 높은 진동수를 통과시킵니다.

> **문제 2.** (심화) 두 시스템을 직렬로 연결하면 전달함수가 곱이 됨을 보이십시오.
> **답.** $h_1*h_2$의 변환이 $H_1H_2$이기 때문입니다.
> **풀이.** 첫 시스템의 출력 $y_1=x*h_1$이 두 번째 입력이 되므로 최종 출력은 $y=(x*h_1)*h_2$입니다. 결합법칙으로 $y=x*(h_1*h_2)$이므로 전체 임펄스 응답은 $h_1*h_2$입니다. 합성곱 정리에서 $\hat y=H_1H_2\hat x$이므로 전달함수는 두 전달함수의 곱입니다. 순서를 바꾸어도 곱은 같으므로 직렬 연결의 순서는 결과에 영향을 주지 않습니다. $\square$

## 3. 유형 총정리

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 합성곱 정의 | $(f*g)(t)=\int f(\tau)g(t-\tau)d\tau$ | 뒤집어 밀고 겹친 면적, 교환·결합·분배 성립 |
| 지지집합 | $[a+c,\,b+d]$ | 양 끝을 더한다 |
| 합성곱 정리 | $\mathcal{F}[f*g]=\hat f\hat g$ | 어려운 적분을 곱으로 바꾼다 |
| 곱의 변환 | $\mathcal{F}[fg]=\frac{1}{2\pi}(\hat f*\hat g)$ | 계수 $\frac{1}{2\pi}$를 빠뜨리지 않는다 |
| 상관 | $\mathcal{F}[f\star g]=\overline{\hat f}\hat g$ | 뒤집지 않고 밀어 겹친다 |
| 자기상관 | $\mathcal{F}[R_f]=|\hat f|^{2}$ | 위너-킨친, $R_f(0)=E[f]$ |
| 파르세발 | $\int f\overline g\,dt=\frac{1}{2\pi}\int\hat f\overline{\hat g}\,d\omega$ | 내적 보존 |
| 플랑셰렐 | $\int|f|^{2}dt=\frac{1}{2\pi}\int|\hat f|^{2}d\omega$ | 에너지 보존, 이상적분 계산에 쓴다 |
| 델타 | $\mathcal{F}[\delta]=1$, $\mathcal{F}[1]=2\pi\delta$ | 합성곱의 항등원, 정현파는 선스펙트럼 |
| 전달함수 | $\hat y=H\hat x$, $H=\mathcal{F}[h]$ | 진동수별 곱셈으로 본다 |
| 직렬 연결 | $H=H_1H_2$ | 임펄스 응답은 합성곱 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $f(t)=g(t)=1$ ($|t|\le1$), 밖에서 0일 때 $(f*g)(0)$과 $(f*g)(1.5)$를 구하십시오.
> **답.** 각각 $2$와 $0.5$입니다.
> **풀이.** 예제 1에서 $(f*g)(t)=2-|t|$ ($|t|\le2$)입니다. $t=0$이면 $2$, $t=1.5$이면 $0.5$입니다. 두 펄스가 완전히 겹칠 때 최대이고 밀면서 줄어듭니다.

> **문제 2.** (기초) $\mathcal{F}[\delta(t-3)]$을 구하십시오.
> **답.** $e^{-3i\omega}$입니다.
> **풀이.** 정의에서 $\int\delta(t-3)e^{-i\omega t}dt=e^{-3i\omega}$입니다. 크기가 1이고 위상만 기울어 있으므로 이 시스템은 신호를 3만큼 지연시키기만 합니다.

> **문제 3.** (표준) $\mathcal{F}^{-1}\!\left[\dfrac{1}{(1+i\omega)(2+i\omega)}\right]$을 구하십시오.
> **답.** $\left(e^{-t}-e^{-2t}\right)u(t)$입니다.
> **풀이.** 합성곱 정리로 두 인수의 역변환 $e^{-t}u(t)$와 $e^{-2t}u(t)$의 합성곱입니다. $t\ge0$에서 $\int_{0}^{t}e^{-\tau}e^{-2(t-\tau)}d\tau=e^{-2t}\int_{0}^{t}e^{\tau}d\tau=e^{-2t}(e^{t}-1)=e^{-t}-e^{-2t}$입니다. 부분분수 $\frac{1}{1+i\omega}-\frac{1}{2+i\omega}$로 나눠 각각 역변환해도 같은 답이 나옵니다.

> **문제 4.** (표준) $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^{2}(3\omega)}{\omega^{2}}\,d\omega$를 파르세발 정리로 구하십시오.
> **답.** $3\pi$입니다.
> **풀이.** $a=3$인 사각펄스의 에너지는 $\int_{-3}^{3}1\,dt=6$이고 변환은 $\frac{2\sin3\omega}{\omega}$입니다. 플랑셰렐 정리에서 $6=\frac{1}{2\pi}\int\frac{4\sin^{2}3\omega}{\omega^{2}}d\omega$이므로 적분값은 $3\pi$입니다. 일반적으로 이 적분은 $\pi a$입니다.

> **문제 5.** (표준) 저역통과 필터 $H(\omega)=\frac{1}{1+i\omega\tau}$에 입력 $x(t)=\cos\omega_0t$를 넣었을 때 출력의 진폭을 구하십시오.
> **답.** $\dfrac{1}{\sqrt{1+\omega_0^{2}\tau^{2}}}$입니다.
> **풀이.** 정현파 입력의 스펙트럼은 $\pm\omega_0$의 선스펙트럼이므로 출력은 그 위치의 $H$ 값이 곱해진 것입니다. 진폭은 $|H(\omega_0)|=\frac{1}{\sqrt{1+\omega_0^{2}\tau^{2}}}$이고 위상은 $-\arctan(\omega_0\tau)$만큼 늦어집니다.

> **문제 6.** (심화) $f$가 실함수이면 자기상관이 짝함수임을 보이십시오.
> **답.** $R_f(-t)=R_f(t)$입니다.
> **풀이.** $R_f(-t)=\int f(\tau)f(\tau-t)\,d\tau$에서 $s=\tau-t$로 치환하면 $\int f(s+t)f(s)\,ds=R_f(t)$입니다. 변환 쪽에서 보아도 $\mathcal{F}[R_f]=|\hat f|^{2}$가 실 짝함수이므로 그 역변환은 실 짝함수여야 합니다. 두 근거가 같은 결론을 줍니다. $\square$

> **문제 7.** (심화) 합성곱 정리를 이용해 $f*g$가 $f$나 $g$보다 매끄러워지는 경향을 설명하십시오.
> **답.** 스펙트럼이 두 변환의 곱이라 고주파가 더 빨리 잦아들기 때문입니다.
> **풀이.** $\hat f$와 $\hat g$가 각각 $1/|\omega|^{m}$, $1/|\omega|^{n}$로 감쇠하면 곱은 $1/|\omega|^{m+n}$로 감쇠합니다. 고주파 성분이 작아질수록 시간 영역 함수의 미분가능 횟수가 늘어납니다. 사각펄스가 삼각펄스로 매끄러워지는 예제 1이 그 사례입니다.

## 5. 스스로 점검

1. 합성곱을 정의하고 교환법칙을 치환으로 증명할 수 있는가?
2. 합성곱 정리를 푸비니 정리를 근거로 증명할 수 있는가?
3. 시간 영역 곱의 변환에 $\frac{1}{2\pi}$가 붙는 이유를 설명할 수 있는가?
4. 상관과 합성곱의 차이를 말하고 자기상관의 변환이 무엇인지 답할 수 있는가?
5. 플랑셰렐 정리를 증명하고 이상적분 계산에 적용할 수 있는가?
6. 델타함수의 변환쌍을 쓰고 합성곱의 항등원임을 확인할 수 있는가?
7. 임펄스 응답과 전달함수의 관계를 합성곱 정리로 설명할 수 있는가?

**정답 요지.** 1. $(f*g)(t)=\int f(\tau)g(t-\tau)d\tau$이며 $s=t-\tau$ 치환으로 $g*f$가 됩니다. 2. 이중적분의 절댓값이 $\lVert f\rVert_1\lVert g\rVert_1$로 유한해 순서를 바꿀 수 있고, 두 적분이 분리됩니다. 3. $f$를 역변환 표현으로 바꿀 때 계수 $\frac{1}{2\pi}$가 함께 들어옵니다. 4. 상관은 뒤집지 않고 밀어 겹치며, $\mathcal{F}[R_f]=|\hat f|^{2}$입니다. 5. $\overline{g}$를 역변환 공액으로 바꾸고 순서를 교환하며, 사각펄스에 적용하면 $\int\frac{\sin^{2}\omega}{\omega^{2}}d\omega=\pi$입니다. 6. $\mathcal{F}[\delta]=1$, $\mathcal{F}[1]=2\pi\delta$이고 $f*\delta=f$입니다. 7. $y=x*h$이므로 $\hat y=H\hat x$이며 시스템의 작용이 진동수별 곱셈이 됩니다.
