---
title: "4. 푸리에 변환의 정의와 성질"
---
# 4강. 푸리에 변환의 정의와 성질

## 이 강의에서 할 수 있게 되는 것

- 푸리에 급수에서 주기를 무한으로 보내는 극한으로 푸리에 변환쌍을 유도할 수 있습니다.
- 푸리에 변환과 역변환을 부호와 계수 규약까지 정확히 진술할 수 있습니다.
- 절대적분가능 조건에서 변환이 존재하고 유계·연속임을 설명할 수 있습니다.
- 사각펄스, 지수감쇠 함수, 가우스 함수의 변환을 정의에 따라 직접 계산할 수 있습니다.
- 선형성, 이동, 변조, 스케일링, 미분 규칙을 증명하고 조합해 사용할 수 있습니다.
- 실함수의 대칭성과 시간-주파수 쌍대성, 불확정성 관계를 진술할 수 있습니다.

이 강의는 [3. 복소 푸리에 급수와 스펙트럼](../../01. 푸리에 급수/3. 복소 푸리에 급수와 스펙트럼/index.md) 강의의 복소 계수 $c_n$을 출발점으로 삼습니다. 복소지수의 계산은 `복소해석학`의 [2. 복소함수와 오일러 공식](../../../복소해석학/01. 복소수와 복소평면/2. 복소함수와 오일러 공식/index.md) 강의에서 다루며, 이상적분의 절대수렴은 `해석학`의 [03. 급수](../../../해석학/03. 급수/index.md) 단원이 바탕입니다.

## 1. 오늘 쓸 기호

이 교본은 각주파수 $\omega$를 변수로 쓰고, $1/2\pi$를 역변환에만 붙이는 규약을 씁니다. 이 규약은 4강부터 6강까지 예외 없이 유지합니다.

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\omega$ | 오메가 | 각주파수, 단위는 라디안 매 초이며 보통진동수 $\nu$와 $\omega=2\pi\nu$로 연결됩니다 |
| $\mathcal{F}[f]$ | 에프의 푸리에 변환 | 함수 $f$를 주파수 영역의 함수로 보내는 연산 |
| $\hat{f}(\omega)$ | 에프 햇 오메가 | $\mathcal{F}[f]\,(\omega)=\int_{-\infty}^{\infty} f(t)e^{-i\omega t}\,dt$ |
| $\mathcal{F}^{-1}[\hat f]$ | 역 푸리에 변환 | $\dfrac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)e^{i\omega t}\,d\omega$ |
| $f\leftrightarrow\hat f$ | 변환쌍 | 두 함수가 서로 변환과 역변환으로 대응한다는 표기 |
| $L^1(\mathbb{R})$ | 엘 원 | $\int_{-\infty}^{\infty}|f(t)|\,dt<\infty$인 함수들의 집합 |
| $\lVert f\rVert_1$ | 에프의 $L^1$ 노름 | $\int_{-\infty}^{\infty}|f(t)|\,dt$ |
| $\operatorname{sinc}x$ | 싱크 엑스 | $\dfrac{\sin x}{x}$, 단 $\operatorname{sinc}0=1$로 정의합니다 |
| $u(t)$ | 단위계단함수 | $t\ge 0$에서 1, $t<0$에서 0인 함수 |
| $\overline{z}$ | 제트 바 | 복소수 $z$의 공액 |
| $*$ | 별, 합성곱 | 두 함수의 합성곱이며 5강에서 정의합니다 |

## 2. 개념

### 2.1 주기를 무한으로 보내는 극한

푸리에 급수는 주기함수만 다룹니다. 주기 $2L$인 함수 $f$의 복소 푸리에 급수는 다음과 같습니다.

$$
f(t)=\sum_{n=-\infty}^{\infty} c_n e^{i\omega_n t},\qquad
\omega_n=\frac{n\pi}{L},\qquad
c_n=\frac{1}{2L}\int_{-L}^{L} f(t)e^{-i\omega_n t}\,dt
$$

여기서 진동수는 $\omega_n=n\pi/L$이라는 이산적인 값만 가지며, 인접한 두 진동수의 간격은 $\Delta\omega=\pi/L$입니다. 주기 $2L$을 키우면 이 간격이 좁아집니다. 즉 $L\to\infty$에서 진동수 축은 촘촘히 메워져 연속이 됩니다.

계수를 급수에 대입하고 $\frac{1}{2L}=\frac{\Delta\omega}{2\pi}$를 이용해 다시 씁니다.

$$
f(t)=\sum_{n=-\infty}^{\infty}\frac{\Delta\omega}{2\pi}
\left(\int_{-L}^{L} f(s)e^{-i\omega_n s}\,ds\right)e^{i\omega_n t}
$$

괄호 안의 값을 $F_L(\omega_n)$이라고 두면 우변은 $\frac{1}{2\pi}\sum_n F_L(\omega_n)e^{i\omega_n t}\,\Delta\omega$ 꼴이며, 이는 $\omega$축 위의 리만 합입니다. $L\to\infty$에서 $\Delta\omega\to 0$이고 적분 구간은 실직선 전체로 늘어나므로, 합은 적분으로 바뀝니다.

$$
F_L(\omega)\longrightarrow \hat f(\omega)=\int_{-\infty}^{\infty} f(t)e^{-i\omega t}\,dt,
\qquad
f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)e^{i\omega t}\,d\omega
$$

이 두 식이 푸리에 변환쌍입니다. 계수 수열 $c_n$이 함수 $\hat f(\omega)$로, 이산합이 적분으로 바뀌었을 뿐 구조는 같습니다. 다만 $c_n$은 진폭 자체였고 $\hat f(\omega)$는 단위 진동수당 진폭, 즉 밀도라는 점이 다릅니다. 실제로 $c_n\approx \frac{1}{2L}\hat f(\omega_n)$이므로 $L$이 커질수록 각 성분의 진폭은 0으로 줄어들고 밀도만 남습니다.

> **문제 1.** (기초) 주기 $2L=10$인 함수의 복소 푸리에 급수에서 인접 진동수 간격 $\Delta\omega$를 구하십시오.
> **답.** $\Delta\omega=\pi/5$입니다.
> **풀이.** $\omega_n=n\pi/L$이고 $L=5$이므로 $\omega_{n+1}-\omega_n=\pi/L=\pi/5$입니다. 주기를 키우면 이 값이 0으로 줄어듭니다.

> **문제 2.** (표준) 위 유도에서 $\frac{1}{2L}$이 $\frac{\Delta\omega}{2\pi}$로 바뀌는 근거를 밝히십시오.
> **답.** $\Delta\omega=\pi/L$이므로 $\frac{\Delta\omega}{2\pi}=\frac{\pi/L}{2\pi}=\frac{1}{2L}$입니다.
> **풀이.** 계수의 정규화 상수 $\frac{1}{2L}$을 진동수 간격으로 표현한 것이 핵심입니다. 이렇게 바꾸어야 합이 $\sum(\cdots)\Delta\omega$ 형태의 리만 합이 되고, 극한에서 적분이 됩니다. 남은 $\frac{1}{2\pi}$가 역변환의 계수로 정착합니다.

> **문제 3.** (심화) 이 규약에서 변환에는 $1/2\pi$가 없고 역변환에만 붙는 이유를 설명하십시오.
> **답.** 리만 합의 미소량 $\Delta\omega$가 역변환 쪽 적분에 흡수되기 때문입니다.
> **풀이.** 유도에서 $\Delta\omega$는 진동수 합, 즉 역변환 쪽에만 나타납니다. 그래서 $\frac{1}{2\pi}$도 역변환에만 남습니다. 두 식에 $\frac{1}{\sqrt{2\pi}}$씩 나누어 붙이는 대칭 규약이나 보통진동수 $\nu$를 쓰는 규약도 있으며, 규약이 다르면 성질의 상수도 달라지므로 한 교본 안에서는 하나로 고정합니다.

### 2.2 정의와 존재 조건

**정의.** $f:\mathbb{R}\to\mathbb{C}$에 대해 다음 이상적분이 존재할 때 이를 $f$의 푸리에 변환이라고 합니다.

$$
\mathcal{F}[f]\,(\omega)=\hat f(\omega)=\int_{-\infty}^{\infty} f(t)e^{-i\omega t}\,dt
$$

역변환은 다음과 같이 정의합니다.

$$
\mathcal{F}^{-1}[\hat f]\,(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)e^{i\omega t}\,d\omega
$$

지수의 부호가 변환에서는 음수, 역변환에서는 양수입니다. 부호를 뒤집은 규약도 통용되지만 이 교본은 위 부호를 끝까지 씁니다.

존재를 보장하는 가장 간단한 조건은 절대적분가능, 즉 $f\in L^1(\mathbb{R})$입니다.

**정리.** $f\in L^1(\mathbb{R})$이면 $\hat f$는 모든 $\omega$에서 존재하고, $|\hat f(\omega)|\le\lVert f\rVert_1$로 유계이며, $\omega$에 대해 연속입니다.

증명을 봅니다. $|e^{-i\omega t}|=1$이므로 피적분함수의 절댓값은 $|f(t)|$이고

$$
|\hat f(\omega)|\le\int_{-\infty}^{\infty}|f(t)e^{-i\omega t}|\,dt=\int_{-\infty}^{\infty}|f(t)|\,dt=\lVert f\rVert_1<\infty
$$

입니다. 따라서 적분은 절대수렴하고 값은 $\lVert f\rVert_1$ 이하입니다. 연속성은 $|\hat f(\omega+h)-\hat f(\omega)|\le\int|f(t)||e^{-iht}-1|\,dt$에서 나옵니다. 피적분함수가 $2|f(t)|$로 지배되고 $h\to0$에서 각 점마다 0으로 가므로 지배수렴정리에 의해 전체 적분이 0으로 갑니다. $\square$

여기에 리만-르베그 보조정리를 덧붙이면 $|\omega|\to\infty$에서 $\hat f(\omega)\to 0$입니다. 즉 절대적분가능한 함수의 스펙트럼은 고주파에서 반드시 잦아듭니다.

주의할 점이 있습니다. $f\in L^1$은 충분조건일 뿐이며 필요조건이 아닙니다. $\hat f$가 $L^1$에 속하지 않는 경우도 있어서 역변환 적분이 통상적 의미로 수렴하지 않을 수 있습니다. 이때는 주요값 극한이나 분포 이론으로 확장하며, 그 개관은 [5. 합성곱 정리와 파르세발 정리](../5. 합성곱 정리와 파르세발 정리/index.md) 강의에서 다룹니다. 또 $f$가 불연속점을 가지면 역변환은 그 점에서 좌우극한의 평균으로 수렴하며, 이는 푸리에 급수의 수렴 정리와 같은 양상입니다.

> **문제 1.** (기초) $f(t)=e^{-|t|}$가 $L^1(\mathbb{R})$에 속하는지 판정하십시오.
> **답.** 속합니다.
> **풀이.** $\int_{-\infty}^{\infty}e^{-|t|}\,dt=2\int_{0}^{\infty}e^{-t}\,dt=2$로 유한합니다. 따라서 절대적분가능하고 변환이 모든 $\omega$에서 존재합니다.

> **문제 2.** (표준) $f(t)=\dfrac{1}{1+t^{2}}$과 $g(t)=\dfrac{1}{1+|t|}$ 중 어느 쪽이 $L^1$에 속하는지 판정하십시오.
> **답.** $f$만 속합니다.
> **풀이.** $\int_{-\infty}^{\infty}\frac{dt}{1+t^2}=\pi$로 유한합니다. 반면 $\int_{1}^{\infty}\frac{dt}{1+t}$는 $\log$로 발산하므로 $g\notin L^1$입니다. $1/|t|$ 정도의 감쇠는 절대적분가능성을 주지 못합니다.

> **문제 3.** (표준) $f\in L^1$일 때 $\hat f(0)$의 뜻을 말하십시오.
> **답.** $\hat f(0)=\int_{-\infty}^{\infty}f(t)\,dt$, 즉 함수의 전체 적분값입니다.
> **풀이.** 정의에 $\omega=0$을 넣으면 $e^{0}=1$이므로 $\hat f(0)=\int f(t)\,dt$입니다. 직류 성분, 곧 평균적 크기가 스펙트럼의 원점 값입니다.

### 2.3 대표 함수의 변환

**예제 1. 사각펄스.** $a>0$에 대해 $f(t)=1$ ($|t|\le a$), $f(t)=0$ ($|t|>a$)로 둡니다.

$$
\hat f(\omega)=\int_{-a}^{a}e^{-i\omega t}\,dt
=\left[\frac{e^{-i\omega t}}{-i\omega}\right]_{-a}^{a}
=\frac{e^{i\omega a}-e^{-i\omega a}}{i\omega}
=\frac{2\sin(a\omega)}{\omega}
=2a\operatorname{sinc}(a\omega)
$$

$\omega=0$에서는 정의로 직접 계산해 $\hat f(0)=2a$이고, 이는 위 식의 극한과 일치합니다. 유한한 구간에서만 값을 가지는 함수의 스펙트럼이 실직선 전체로 퍼지며 $1/|\omega|$ 속도로만 잦아듭니다. 시간 폭 $2a$를 좁히면 주엽의 폭 $2\pi/a$가 넓어집니다.

**예제 2. 한쪽 지수감쇠.** $a>0$에 대해 $f(t)=e^{-at}u(t)$로 둡니다.

$$
\hat f(\omega)=\int_{0}^{\infty}e^{-at}e^{-i\omega t}\,dt
=\int_{0}^{\infty}e^{-(a+i\omega)t}\,dt
=\left[\frac{e^{-(a+i\omega)t}}{-(a+i\omega)}\right]_{0}^{\infty}
=\frac{1}{a+i\omega}
$$

$a>0$이므로 $|e^{-(a+i\omega)t}|=e^{-at}\to0$이고 상한에서 항이 사라집니다. 결과는 복소수 값을 가지며 크기와 위상은 다음과 같습니다.

$$
|\hat f(\omega)|=\frac{1}{\sqrt{a^{2}+\omega^{2}}},\qquad
\arg\hat f(\omega)=-\arctan\frac{\omega}{a}
$$

이 함수는 $t<0$에서 0이라 좌우대칭이 아니므로 스펙트럼이 실수가 아니고 위상이 함께 생깁니다.

**예제 3. 양쪽 지수감쇠.** $f(t)=e^{-a|t|}$은 짝함수이므로 두 조각으로 나누어 더합니다.

$$
\hat f(\omega)=\int_{-\infty}^{0}e^{at}e^{-i\omega t}\,dt+\int_{0}^{\infty}e^{-at}e^{-i\omega t}\,dt
=\frac{1}{a-i\omega}+\frac{1}{a+i\omega}
=\frac{2a}{a^{2}+\omega^{2}}
$$

짝함수의 변환이 실수이고 짝함수라는 사실이 그대로 확인됩니다.

**예제 4. 가우스 함수.** $a>0$에 대해 $f(t)=e^{-at^{2}}$의 변환을 구합니다. 정의를 $\omega$로 미분하면

$$
\hat f'(\omega)=\int_{-\infty}^{\infty}(-it)e^{-at^{2}}e^{-i\omega t}\,dt
$$

입니다. 여기서 $te^{-at^{2}}=-\frac{1}{2a}\frac{d}{dt}e^{-at^{2}}$을 대입하고 부분적분을 합니다.

$$
\hat f'(\omega)=\frac{i}{2a}\int_{-\infty}^{\infty}\frac{d}{dt}\!\left(e^{-at^{2}}\right)e^{-i\omega t}\,dt
=\frac{i}{2a}\left(\Big[e^{-at^{2}}e^{-i\omega t}\Big]_{-\infty}^{\infty}+i\omega\hat f(\omega)\right)
=-\frac{\omega}{2a}\hat f(\omega)
$$

경계항은 $e^{-at^2}\to0$이므로 사라집니다. 이 미분방정식의 해는 $\hat f(\omega)=\hat f(0)e^{-\omega^{2}/4a}$이고, $\hat f(0)=\int e^{-at^{2}}dt=\sqrt{\pi/a}$이므로

$$
\mathcal{F}\!\left[e^{-at^{2}}\right]\,(\omega)=\sqrt{\frac{\pi}{a}}\,e^{-\omega^{2}/4a}
$$

입니다. 가우스 함수의 변환은 다시 가우스 함수입니다. 시간 쪽 폭은 $1/\sqrt{a}$ 규모이고 주파수 쪽 폭은 $\sqrt{a}$ 규모이므로 두 폭의 곱이 $a$와 무관한 상수입니다. 이 사실이 2.5절 불확정성 관계의 등호 사례입니다.

> **문제 1.** (기초) $f(t)=1$ ($|t|\le 1$), 그 밖에서 0인 함수의 변환을 구하십시오.
> **답.** $\hat f(\omega)=\dfrac{2\sin\omega}{\omega}$입니다.
> **풀이.** 예제 1에 $a=1$을 넣으면 $\hat f(\omega)=2\sin(\omega)/\omega$입니다. $\omega=0$에서 값은 $2$이며 이는 펄스의 면적과 같습니다.

> **문제 2.** (표준) $f(t)=e^{-3t}u(t)$의 변환과 그 크기를 구하십시오.
> **답.** $\hat f(\omega)=\dfrac{1}{3+i\omega}$, $|\hat f(\omega)|=\dfrac{1}{\sqrt{9+\omega^{2}}}$입니다.
> **풀이.** 예제 2에 $a=3$을 넣습니다. 크기는 분모의 절댓값이 $\sqrt{3^{2}+\omega^{2}}$이므로 그 역수입니다. $\omega=0$에서 $1/3$이고 고주파에서 $1/|\omega|$로 잦아듭니다.

> **문제 3.** (표준) $\mathcal{F}[e^{-t^{2}/2}]$를 구하십시오.
> **답.** $\sqrt{2\pi}\,e^{-\omega^{2}/2}$입니다.
> **풀이.** 예제 4에서 $a=1/2$이므로 $\sqrt{\pi/a}=\sqrt{2\pi}$이고 지수는 $-\omega^{2}/(4\cdot\frac12)=-\omega^{2}/2$입니다. 이 함수는 자기 자신과 같은 모양으로 변환되는 대표적 예입니다.

> **문제 4.** (심화) 예제 1의 결과에서 $a\to0^{+}$일 때 스펙트럼이 어떻게 되는지 설명하십시오.
> **답.** 모든 $\omega$에서 0으로 갑니다.
> **풀이.** $|2a\operatorname{sinc}(a\omega)|\le 2a\to0$입니다. 펄스의 면적 자체가 0으로 줄기 때문입니다. 면적을 1로 고정한 $\frac{1}{2a}$ 높이의 펄스로 바꾸면 변환은 $\operatorname{sinc}(a\omega)\to1$이 되고, 이 극한이 델타함수의 변환에 해당합니다.

### 2.4 기본 성질

이하에서 $f,g\in L^1(\mathbb{R})$이고 $\hat f=\mathcal{F}[f]$, $\hat g=\mathcal{F}[g]$입니다.

| 성질 | 시간 영역 | 주파수 영역 |
|---|---|---|
| 선형성 | $\alpha f+\beta g$ | $\alpha\hat f+\beta\hat g$ |
| 시간이동 | $f(t-t_0)$ | $e^{-i\omega t_0}\hat f(\omega)$ |
| 변조(주파수이동) | $e^{i\omega_0 t}f(t)$ | $\hat f(\omega-\omega_0)$ |
| 스케일링 | $f(at)$, $a\ne0$ | $\dfrac{1}{|a|}\hat f\!\left(\dfrac{\omega}{a}\right)$ |
| 반사 | $f(-t)$ | $\hat f(-\omega)$ |
| 공액 | $\overline{f(t)}$ | $\overline{\hat f(-\omega)}$ |
| 미분 | $f'(t)$ | $i\omega\hat f(\omega)$ |
| $t$ 곱 | $t f(t)$ | $i\dfrac{d}{d\omega}\hat f(\omega)$ |
| 적분 | $\displaystyle\int_{-\infty}^{t}f(s)\,ds$ | $\dfrac{\hat f(\omega)}{i\omega}$, 단 $\hat f(0)=0$ |

선형성은 적분의 선형성에서 곧바로 나옵니다. 나머지를 증명합니다.

시간이동은 $s=t-t_0$ 치환으로 얻습니다.

$$
\mathcal{F}[f(t-t_0)]\,(\omega)=\int f(t-t_0)e^{-i\omega t}\,dt
=\int f(s)e^{-i\omega(s+t_0)}\,ds=e^{-i\omega t_0}\hat f(\omega)
$$

$|e^{-i\omega t_0}|=1$이므로 시간이동은 진폭 스펙트럼을 바꾸지 않고 위상만 $-\omega t_0$만큼 기울입니다. 변조는 지수를 묶으면 됩니다.

$$
\mathcal{F}\!\left[e^{i\omega_0 t}f(t)\right]\,(\omega)=\int f(t)e^{-i(\omega-\omega_0)t}\,dt=\hat f(\omega-\omega_0)
$$

즉 시간 영역에서 복소지수를 곱하면 스펙트럼이 통째로 평행이동합니다. 스케일링은 $a>0$일 때 $s=at$ 치환으로

$$
\mathcal{F}[f(at)]\,(\omega)=\int f(at)e^{-i\omega t}\,dt=\frac{1}{a}\int f(s)e^{-i(\omega/a)s}\,ds=\frac{1}{a}\hat f\!\left(\frac{\omega}{a}\right)
$$

이고, $a<0$이면 치환에서 적분 방향이 뒤집혀 $1/|a|$가 됩니다. 시간축을 $a>1$배로 압축하면 스펙트럼은 같은 비율로 늘어나고 높이는 줄어듭니다.

미분 규칙은 부분적분입니다. $f$가 미분가능하고 $f,f'\in L^1$이면 $|t|\to\infty$에서 $f(t)\to0$이므로

$$
\mathcal{F}[f']\,(\omega)=\int f'(t)e^{-i\omega t}\,dt
=\Big[f(t)e^{-i\omega t}\Big]_{-\infty}^{\infty}+i\omega\int f(t)e^{-i\omega t}\,dt=i\omega\hat f(\omega)
$$

입니다. 반복하면 $\mathcal{F}[f^{(n)}]=(i\omega)^{n}\hat f$입니다. 미분이 곱셈으로 바뀌기 때문에 미분방정식이 대수방정식이 됩니다. $t$ 곱 규칙은 정의를 $\omega$로 미분해 얻습니다. $\frac{d}{d\omega}\hat f(\omega)=\int f(t)(-it)e^{-i\omega t}\,dt=-i\,\mathcal{F}[tf]$이므로 $\mathcal{F}[tf]=i\hat f'(\omega)$입니다. 적분 규칙은 $F(t)=\int_{-\infty}^{t}f$가 $F'=f$를 만족하므로 미분 규칙에서 $\hat f=i\omega\hat F$로 나오며, $\hat F$가 $L^1$의 함수이려면 $F(\infty)=\hat f(0)=0$이어야 합니다. 이 조건이 깨지면 $\pi\hat f(0)\delta(\omega)$ 항이 추가되고, 델타함수는 5강에서 다룹니다. $\square$

> **문제 1.** (기초) $\hat f(\omega)$가 주어졌을 때 $\mathcal{F}[f(t-3)]$를 쓰십시오.
> **답.** $e^{-3i\omega}\hat f(\omega)$입니다.
> **풀이.** 시간이동 규칙에 $t_0=3$을 넣습니다. 크기는 그대로이고 위상만 $-3\omega$ 더해집니다.

> **문제 2.** (표준) $f(t)=e^{-|t|}$일 때 $\mathcal{F}[e^{-|t|}\cos 2t]$를 구하십시오.
> **답.** $\dfrac{1}{1+(\omega-2)^{2}}+\dfrac{1}{1+(\omega+2)^{2}}$입니다.
> **풀이.** 예제 3에서 $a=1$이므로 $\hat f(\omega)=\frac{2}{1+\omega^{2}}$입니다. $\cos2t=\frac12(e^{2it}+e^{-2it})$이므로 변조 규칙과 선형성으로 $\frac12\hat f(\omega-2)+\frac12\hat f(\omega+2)$이고, 대입하면 위 식입니다. 하나의 봉우리가 $\pm2$로 갈라진 두 봉우리가 됩니다.

> **문제 3.** (표준) $\mathcal{F}[f(2t)]$와 $\mathcal{F}[f(t/2)]$를 비교하십시오.
> **답.** 각각 $\frac12\hat f(\omega/2)$와 $2\hat f(2\omega)$입니다.
> **풀이.** 스케일링 규칙에 $a=2$와 $a=1/2$를 넣습니다. 시간축 압축은 스펙트럼을 넓히고 낮추며, 시간축 확대는 스펙트럼을 좁히고 높입니다. 두 폭의 곱은 변하지 않습니다.

### 2.5 대칭성, 쌍대성, 불확정성

$f$가 실함수라고 하면 $\overline{f(t)}=f(t)$이므로

$$
\overline{\hat f(\omega)}=\overline{\int f(t)e^{-i\omega t}\,dt}=\int f(t)e^{i\omega t}\,dt=\hat f(-\omega)
$$

입니다. 즉 실함수의 스펙트럼은 에르미트 대칭 $\hat f(-\omega)=\overline{\hat f(\omega)}$을 만족합니다. 따라서 $|\hat f|$는 짝함수, $\arg\hat f$는 홀함수이고, 음의 주파수 쪽은 새 정보를 담지 않습니다. 여기에 대칭성이 더 붙으면 다음이 성립합니다.

| $f$의 성질 | $\hat f$의 성질 |
|---|---|
| 실함수 | 에르미트 대칭 $\hat f(-\omega)=\overline{\hat f(\omega)}$ |
| 실 짝함수 | 실 짝함수, $\hat f(\omega)=2\int_{0}^{\infty}f(t)\cos\omega t\,dt$ |
| 실 홀함수 | 순허수 홀함수, $\hat f(\omega)=-2i\int_{0}^{\infty}f(t)\sin\omega t\,dt$ |
| 순허수 | 반에르미트 대칭 $\hat f(-\omega)=-\overline{\hat f(\omega)}$ |

실 짝함수인 경우를 확인합니다. $e^{-i\omega t}=\cos\omega t-i\sin\omega t$로 쪼개면 $f(t)\sin\omega t$는 홀함수이므로 대칭구간 적분이 0이고, $f(t)\cos\omega t$는 짝함수이므로 절반의 두 배가 됩니다.

**쌍대성.** 변환과 역변환의 모양이 거의 같으므로 두 영역의 역할을 맞바꿀 수 있습니다. $\hat f$를 다시 변환하면

$$
\mathcal{F}[\hat f]\,(\omega)=2\pi f(-\omega)
$$

입니다. 역변환 정의 $f(t)=\frac{1}{2\pi}\int\hat f(s)e^{ist}\,ds$에서 $t$를 $-\omega$로 두면 $2\pi f(-\omega)=\int\hat f(s)e^{-i\omega s}\,ds=\mathcal{F}[\hat f]\,(\omega)$이기 때문입니다. 이 관계 덕분에 한쪽 변환쌍을 알면 반대쪽을 공짜로 얻습니다. 사각펄스가 sinc로 갔으므로 sinc는 사각펄스로 갑니다.

**불확정성 관계.** $\lVert f\rVert_2^{2}=\int|f|^{2}dt$가 유한하고 0이 아닐 때 시간 폭과 주파수 폭을 분산으로 정의합니다.

$$
(\Delta t)^{2}=\frac{\int t^{2}|f(t)|^{2}\,dt}{\int |f(t)|^{2}\,dt},\qquad
(\Delta\omega)^{2}=\frac{\int \omega^{2}|\hat f(\omega)|^{2}\,d\omega}{\int |\hat f(\omega)|^{2}\,d\omega}
$$

이때 항상 $\Delta t\cdot\Delta\omega\ge\frac{1}{2}$이고, 등호는 $f$가 가우스 함수일 때만 성립합니다. 증명의 골자는 $\mathcal{F}[f']=i\omega\hat f$로 주파수 분산을 $\int|f'|^{2}dt$로 바꾸고, $\int t f\overline{f'}\,dt$에 코시-슈바르츠 부등식과 부분적분을 적용하는 것입니다. 결론의 뜻은 분명합니다. 시간축에서 좁게 뭉친 신호는 주파수축에서 넓게 퍼지며, 두 폭을 동시에 좁히는 것은 불가능합니다. 스케일링 규칙이 이미 이 사실을 예고했고, 사각펄스와 가우스 함수의 계산이 그 구체적 사례입니다.

> **문제 1.** (기초) 실 짝함수의 푸리에 변환은 어떤 함수인지 답하십시오.
> **답.** 실수 값을 가지는 짝함수입니다.
> **풀이.** $\hat f(\omega)=2\int_{0}^{\infty}f(t)\cos\omega t\,dt$이므로 값이 실수이고, $\cos$이 짝함수이므로 $\hat f(-\omega)=\hat f(\omega)$입니다. 예제 3의 $2a/(a^{2}+\omega^{2})$이 그 예입니다.

> **문제 2.** (표준) $\mathcal{F}\!\left[\dfrac{\sin t}{t}\right]$를 쌍대성으로 구하십시오.
> **답.** $|\omega|<1$에서 $\pi$, $|\omega|>1$에서 $0$입니다.
> **풀이.** 예제 1에서 $a=1$인 사각펄스 $p$의 변환이 $2\sin\omega/\omega$입니다. 쌍대성에 따라 $\mathcal{F}[2\sin t/t]\,(\omega)=2\pi p(-\omega)=2\pi p(\omega)$이므로 양변을 2로 나누면 $\mathcal{F}[\sin t/t]\,(\omega)=\pi p(\omega)$입니다. 즉 $|\omega|<1$에서 $\pi$, 밖에서 0이며 $|\omega|=1$에서는 좌우극한의 평균 $\pi/2$입니다.

> **문제 3.** (심화) $f(t)=e^{-at^{2}}$에서 $\Delta t\cdot\Delta\omega$를 계산해 $1/2$임을 확인하십시오.
> **답.** $\Delta t=\dfrac{1}{2\sqrt{a}}$, $\Delta\omega=\sqrt{a}$이므로 곱은 $\dfrac12$입니다.
> **풀이.** $|f|^{2}=e^{-2at^{2}}$이므로 분산은 표준편차가 $\sigma^{2}=\frac{1}{4a}$인 가우스 분포의 분산과 같아 $(\Delta t)^{2}=\frac{1}{4a}$입니다. 한편 $|\hat f|^{2}\propto e^{-\omega^{2}/2a}$이므로 $(\Delta\omega)^{2}=a$입니다. 곱하면 $\Delta t\Delta\omega=\frac{1}{2\sqrt a}\cdot\sqrt a=\frac12$로 등호가 성립합니다.

## 3. 유형 총정리

| 유형 | 핵심 식 | 요령 |
|---|---|---|
| 정의 | $\hat f(\omega)=\int f(t)e^{-i\omega t}dt$ | 부호는 음수, 계수는 없음 |
| 역변환 | $f(t)=\frac{1}{2\pi}\int\hat f(\omega)e^{i\omega t}d\omega$ | 부호는 양수, 계수 $1/2\pi$ |
| 존재 | $f\in L^1\Rightarrow$ 유계·연속·$\hat f(\infty)=0$ | 절대적분 유한을 먼저 확인 |
| 사각펄스 | $2a\operatorname{sinc}(a\omega)$ | 유한 지지는 무한 스펙트럼 |
| 한쪽 지수 | $\dfrac{1}{a+i\omega}$ | 비대칭이면 위상이 생긴다 |
| 양쪽 지수 | $\dfrac{2a}{a^{2}+\omega^{2}}$ | 짝함수면 실수 스펙트럼 |
| 가우스 | $\sqrt{\pi/a}\,e^{-\omega^{2}/4a}$ | 미분방정식으로 유도 |
| 시간이동 | $e^{-i\omega t_0}\hat f$ | 크기 불변, 위상만 기울기 |
| 변조 | $\hat f(\omega-\omega_0)$ | 스펙트럼 평행이동 |
| 스케일링 | $\frac{1}{|a|}\hat f(\omega/a)$ | 압축과 확산은 반비례 |
| 미분 | $(i\omega)^{n}\hat f$ | 미분이 곱셈으로 바뀐다 |
| $t$ 곱 | $i\hat f'(\omega)$ | 곱셈이 미분으로 바뀐다 |
| 실함수 | $\hat f(-\omega)=\overline{\hat f(\omega)}$ | 절반의 주파수만 보면 된다 |
| 쌍대성 | $\mathcal{F}[\hat f]\,(\omega)=2\pi f(-\omega)$ | 한 쌍에서 반대쪽을 얻는다 |
| 불확정성 | $\Delta t\,\Delta\omega\ge\frac12$ | 등호는 가우스뿐 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $f(t)=e^{-2t}u(t)$의 변환을 구하고 $\hat f(0)$의 뜻을 말하십시오.
> **답.** $\hat f(\omega)=\dfrac{1}{2+i\omega}$이고 $\hat f(0)=\dfrac12$은 $f$의 전체 적분값입니다.
> **풀이.** 예제 2에 $a=2$를 넣습니다. $\int_{0}^{\infty}e^{-2t}dt=\frac12$이므로 $\hat f(0)$과 일치합니다.

> **문제 2.** (기초) $\mathcal{F}[f]=\hat f$일 때 $\mathcal{F}[3f(t)-2f(t-1)]$를 쓰십시오.
> **답.** $\left(3-2e^{-i\omega}\right)\hat f(\omega)$입니다.
> **풀이.** 선형성으로 두 항을 나누고 두 번째 항에 시간이동 규칙 $t_0=1$을 적용하면 $-2e^{-i\omega}\hat f(\omega)$입니다. 공통 인수 $\hat f(\omega)$를 묶습니다.

> **문제 3.** (표준) 높이 $h$, 폭 $2a$인 사각펄스의 변환을 구하고 면적과의 관계를 확인하십시오.
> **답.** $2ah\operatorname{sinc}(a\omega)$이고 $\hat f(0)=2ah$는 펄스의 면적입니다.
> **풀이.** 선형성으로 예제 1의 결과에 $h$를 곱하면 $\frac{2h\sin(a\omega)}{\omega}=2ah\operatorname{sinc}(a\omega)$입니다. $\omega=0$에서 값은 밑변 $2a$와 높이 $h$의 곱, 즉 면적입니다.

> **문제 4.** (표준) $\mathcal{F}\!\left[\dfrac{1}{1+t^{2}}\right]$를 쌍대성으로 구하십시오.
> **답.** $\pi e^{-|\omega|}$입니다.
> **풀이.** 예제 3에서 $a=1$이면 $\mathcal{F}[e^{-|t|}]=\frac{2}{1+\omega^{2}}$입니다. 쌍대성에 따라 $\mathcal{F}\!\left[\frac{2}{1+t^{2}}\right]\,(\omega)=2\pi e^{-|-\omega|}=2\pi e^{-|\omega|}$이므로 양변을 2로 나누면 $\pi e^{-|\omega|}$입니다.

> **문제 5.** (표준) $f''-f=g$이고 $\hat g$가 주어졌을 때 $\hat f$를 $\hat g$로 나타내십시오.
> **답.** $\hat f(\omega)=-\dfrac{\hat g(\omega)}{1+\omega^{2}}$입니다.
> **풀이.** 미분 규칙으로 $\mathcal{F}[f'']=(i\omega)^{2}\hat f=-\omega^{2}\hat f$입니다. 방정식을 변환하면 $-\omega^{2}\hat f-\hat f=\hat g$, 즉 $-(1+\omega^{2})\hat f=\hat g$이므로 위 식입니다. 미분방정식이 나눗셈으로 풀립니다.

> **문제 6.** (표준) $\mathcal{F}[f]=\hat f$일 때 $\mathcal{F}\!\left[f(2t-4)\right]$를 구하십시오.
> **답.** $\dfrac{1}{2}e^{-2i\omega}\hat f\!\left(\dfrac{\omega}{2}\right)$입니다.
> **풀이.** $f(2t-4)=g(2t)$로 두면 $g(s)=f(s-4)$이고 $\hat g(\omega)=e^{-4i\omega}\hat f(\omega)$입니다. 스케일링으로 $\mathcal{F}[g(2t)]=\frac12\hat g(\omega/2)=\frac12 e^{-4i(\omega/2)}\hat f(\omega/2)$이므로 위 식입니다. 이동과 스케일링의 순서를 뒤집으면 지수의 계수가 달라지므로 항상 한쪽 순서로 정리합니다.

> **문제 7.** (심화) $f$가 실 홀함수이면 $\hat f$가 순허수임을 보이십시오.
> **답.** $\hat f(\omega)=-2i\int_{0}^{\infty}f(t)\sin\omega t\,dt$이므로 순허수입니다.
> **풀이.** $e^{-i\omega t}=\cos\omega t-i\sin\omega t$로 쪼갭니다. $f$가 홀함수이므로 $f(t)\cos\omega t$는 홀함수이고 대칭구간 적분이 0입니다. $f(t)\sin\omega t$는 짝함수이므로 절반 구간 적분의 두 배가 되어 $\hat f(\omega)=-2i\int_{0}^{\infty}f(t)\sin\omega t\,dt$입니다. 실수 적분값 앞에 $-i$만 붙었으므로 순허수입니다. $\square$

## 5. 스스로 점검

1. 푸리에 급수에서 푸리에 변환으로 넘어가는 극한 과정을 $\Delta\omega$를 써서 설명할 수 있는가?
2. 변환과 역변환의 지수 부호와 $1/2\pi$의 위치를 정확히 쓸 수 있는가?
3. $f\in L^1$에서 $\hat f$가 유계이고 연속임을 증명할 수 있는가?
4. 사각펄스, 한쪽 지수감쇠, 가우스 함수의 변환을 정의에서 유도할 수 있는가?
5. 시간이동과 변조가 각각 무엇을 바꾸고 무엇을 보존하는지 말할 수 있는가?
6. 미분 규칙 $\mathcal{F}[f']=i\omega\hat f$를 부분적분으로 증명할 수 있는가?
7. 실 짝함수의 변환이 실 짝함수임을 보이고 쌍대성으로 새 변환쌍을 만들 수 있는가?

**정답 요지.** 1. $c_n=\frac{\Delta\omega}{2\pi}F_L(\omega_n)$으로 바꾸면 리만 합이 되고 $\Delta\omega\to0$에서 적분이 됩니다. 2. 변환은 $e^{-i\omega t}$에 계수 없음, 역변환은 $e^{i\omega t}$에 $\frac{1}{2\pi}$입니다. 3. $|e^{-i\omega t}|=1$로 $|\hat f|\le\lVert f\rVert_1$, 연속성은 지배수렴정리입니다. 4. 각각 $2a\operatorname{sinc}(a\omega)$, $\frac{1}{a+i\omega}$, $\sqrt{\pi/a}e^{-\omega^{2}/4a}$입니다. 5. 시간이동은 위상만 기울이고 크기를 보존하며, 변조는 스펙트럼을 평행이동합니다. 6. 경계항이 사라지고 $+i\omega\hat f$가 남습니다. 7. $\sin$ 항이 홀함수라 사라지고 $\cos$ 항만 남으며, $\mathcal{F}[\hat f]=2\pi f(-\omega)$로 반대 방향 쌍을 얻습니다.
