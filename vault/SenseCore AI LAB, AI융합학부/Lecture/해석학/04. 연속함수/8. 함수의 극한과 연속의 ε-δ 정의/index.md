---
title: "8. 함수의 극한과 연속의 ε-δ 정의"
---
# 8강. 함수의 극한과 연속의 ε-δ 정의

## 이 강의에서 할 수 있게 되는 것

- 함수의 극한을 $\varepsilon$-$\delta$ 논법으로 정의하고 한정기호의 순서가 갖는 뜻을 설명할 수 있습니다.
- 주어진 $\varepsilon$에 대응하는 $\delta$를 실제로 구성해 극한값을 증명할 수 있습니다.
- 수열 판정법으로 극한의 존재와 부존재를 판정할 수 있습니다.
- 연속을 정의하고 $\varepsilon$-$\delta$ 조건과 수열 조건이 동등함을 증명할 수 있습니다.
- 불연속을 종류별로 분류하고 합성함수와 초등함수의 연속성을 증명할 수 있습니다.

이 강의는 [3. 수열의 수렴과 ε-N 논법](../../02. 수열의 극한/3. 수열의 수렴과 ε-N 논법/index.md)의 $\varepsilon$-$N$ 논법을 함수로 옮깁니다. 극한값을 실제로 구하는 계산 기술과 불연속점의 도식적 분류는 [2. 극한의 정의와 계산](../../../미적분학/01. 함수와 극한/2. 극한의 정의와 계산/index.md)과 [3. 연속과 불연속](../../../미적분학/01. 함수와 극한/3. 연속과 불연속/index.md)에서 다루고, 이 강의는 그 정의를 엄밀하게 세우고 증명하는 쪽을 맡습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\varepsilon$ | 엡실론 | 목표 오차, 임의로 작게 주어지는 양수 |
| $\delta$ | 델타 | $\varepsilon$에 맞춰 찾아내는 정의역 쪽 폭 |
| $\lim_{x\to c}f(x)=L$ | 엑스가 씨로 갈 때 에프의 극한은 엘 | $x$를 $c$에 충분히 가깝게 하면 $f(x)$가 $L$에 임의로 가까워진다 |
| $0<\lvert x-c\rvert<\delta$ | 영보다 크고 델타보다 작다 | $x$가 $c$의 $\delta$ 근방에 있으면서 $c$ 자신은 아니다 |
| $\forall$ | 모든 | 전칭 한정기호 |
| $\exists$ | 어떤 | 존재 한정기호 |
| $c$의 집적점 조건 | 집적점 | $c$의 임의의 근방이 $c$ 아닌 정의역 점을 담는다 |
| $f(c^+),\ f(c^-)$ | 씨 플러스, 씨 마이너스 | 오른쪽 극한, 왼쪽 극한 |
| $f\circ g$ | 에프 오 지 | 합성함수 $x\mapsto f(g(x))$ |
| $\chi_{\mathbb{Q}}$ | 카이 큐 | 유리수에서 $1$, 무리수에서 $0$인 함수 |
| $\square$ | 증명 끝 | 증명이 종료됨을 표시 |

## 2. 개념

### 2.1 함수의 극한의 ε-δ 정의

수열의 극한은 첨자 $n$이 커질 때의 거동을 다뤘습니다. 함수의 극한은 변수 $x$가 한 점 $c$에 접근할 때의 거동을 다룹니다. 접근하는 지점 $c$에서 함숫값이 정의되어 있을 필요는 없고, 대신 $c$ 주변에 정의역의 점이 계속 남아 있어야 합니다. 이 조건을 집적점 조건이라고 합니다.

정의를 세웁니다. $D\subseteq\mathbb{R}$, $f:D\to\mathbb{R}$이고 $c$가 $D$의 집적점이라고 합니다. 이때

$$
\lim_{x\to c}f(x)=L
\iff
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\ 0<\lvert x-c\rvert<\delta\ \Rightarrow\ \lvert f(x)-L\rvert<\varepsilon
$$

라고 정의합니다. 이 정의는 다음처럼 읽습니다. 어떤 목표 오차 $\varepsilon$을 상대가 먼저 제시하면, 그에 맞춰 폭 $\delta$를 찾아낼 수 있고, $c$에서 $\delta$ 안쪽에 있는 모든 $x$에 대해 오차가 $\varepsilon$ 미만이 됩니다.

한정기호의 순서가 뜻을 결정합니다. $\forall\varepsilon$이 $\exists\delta$보다 앞에 있으므로 $\delta$는 $\varepsilon$을 본 뒤에 고를 수 있습니다. 즉 $\delta$는 $\varepsilon$의 함수입니다. 순서를 바꿔 $\exists\delta\ \forall\varepsilon$이라고 쓰면 하나의 $\delta$가 모든 $\varepsilon$을 동시에 처리해야 하므로 $f$가 $c$ 근방에서 상수 $L$이라는 훨씬 강한 주장이 됩니다.

$0<\lvert x-c\rvert$라는 조건도 필수입니다. 이 조건이 $x=c$를 배제하므로 극한은 $f(c)$의 값과 무관하게 정해집니다. $f(c)$를 마음대로 바꿔도 극한은 변하지 않습니다.

> **문제 1.** (기초) $\lim_{x\to c}f(x)=L$의 정의에서 $\delta$가 $\varepsilon$에 의존해도 되는 이유를 한정기호로 설명하십시오.
> **답.** $\forall\varepsilon$이 $\exists\delta$보다 앞에 있기 때문입니다.
> **풀이.** 정의는 $\forall\varepsilon>0\ \exists\delta>0\ (\cdots)$의 순서입니다. 뒤쪽 존재 한정기호는 앞쪽 전칭 변수의 값을 알고 나서 선택되므로 $\delta$는 $\varepsilon$에 따라 달라질 수 있습니다.

> **문제 2.** (기초) $f(x)=\dfrac{x^2-1}{x-1}$은 $x=1$에서 정의되지 않습니다. $\lim_{x\to 1}f(x)$를 논할 수 있는 이유를 말하십시오.
> **답.** $1$이 정의역 $\mathbb{R}\setminus\{1\}$의 집적점이고, 정의가 $x=c$를 배제하기 때문입니다.
> **풀이.** $1$의 임의의 근방에는 $1$이 아닌 정의역 점이 무수히 있으므로 집적점 조건이 성립합니다. 정의의 가정은 $0<\lvert x-1\rvert<\delta$이므로 $x=1$은 처음부터 검사 대상이 아닙니다. 따라서 $f(1)$이 없어도 극한은 논할 수 있습니다.

> **문제 3.** (표준) $\exists\delta>0\ \forall\varepsilon>0\ \forall x:\ 0<\lvert x-c\rvert<\delta\Rightarrow\lvert f(x)-L\rvert<\varepsilon$이 뜻하는 바를 말하십시오.
> **답.** $c$의 어떤 근방에서 $f$가 상수 $L$이라는 뜻입니다.
> **풀이.** $\delta$를 먼저 고정하면 그 근방의 모든 $x$에서 $\lvert f(x)-L\rvert$이 모든 양수 $\varepsilon$보다 작아야 합니다. 음이 아닌 수가 모든 양수보다 작으면 $0$이므로 $f(x)=L$입니다. 이는 극한의 정의보다 훨씬 강한 조건입니다.

### 2.2 δ를 실제로 구성하는 절차

정의를 만족하는 $\delta$는 찾아내야 합니다. 절차는 언제나 같습니다. 먼저 $\lvert f(x)-L\rvert$을 $\lvert x-c\rvert$가 든 식으로 인수분해합니다. 다음으로 남은 인자를 예비 제한으로 유계화합니다. 마지막으로 두 제한의 최소값을 $\delta$로 잡습니다.

첫 시연으로 $\lim_{x\to 3}x^2=9$를 증명합니다. $\varepsilon>0$이 주어졌다고 합니다.

$$
\lvert x^2-9\rvert=\lvert x-3\rvert\,\lvert x+3\rvert
$$

여기서 $\lvert x+3\rvert$을 유계화합니다. 예비 제한 $\lvert x-3\rvert<1$을 두면 $2<x<4$이므로 $\lvert x+3\rvert<7$입니다. 따라서

$$
\delta=\min\Bigl\{1,\ \frac{\varepsilon}{7}\Bigr\}
$$

으로 잡습니다. $0<\lvert x-3\rvert<\delta$이면 $\lvert x-3\rvert<1$이므로 $\lvert x+3\rvert<7$이고, 동시에 $\lvert x-3\rvert<\varepsilon/7$이므로

$$
\lvert x^2-9\rvert=\lvert x-3\rvert\,\lvert x+3\rvert<\frac{\varepsilon}{7}\cdot 7=\varepsilon
$$

입니다. 따라서 $\lim_{x\to 3}x^2=9$입니다. $\square$

두 번째 시연으로 $\lim_{x\to 2}\dfrac1x=\dfrac12$을 증명합니다.

$$
\left\lvert\frac1x-\frac12\right\rvert=\frac{\lvert 2-x\rvert}{2\lvert x\rvert}
$$

분모의 $\lvert x\rvert$가 작아지면 값이 커지므로 아래에서 막아야 합니다. 예비 제한 $\lvert x-2\rvert<1$을 두면 $1<x<3$이므로 $\lvert x\rvert>1$입니다. 그러면 위 식은 $\lvert x-2\rvert/2$ 이하입니다. 따라서 $\delta=\min\{1,\ 2\varepsilon\}$으로 잡으면 $\lvert 1/x-1/2\rvert<\varepsilon$입니다. $\square$

두 시연에서 공통된 요령은 두 가지입니다. 분자에는 $\lvert x-c\rvert$를 남기고, 나머지 인자는 예비 제한으로 상수 상한을 씌웁니다. 분모에 변수가 있으면 반드시 아래에서 막습니다.

> **문제 1.** (기초) $\lim_{x\to 4}(3x-5)=7$을 $\varepsilon$-$\delta$로 증명하십시오.
> **답.** $\delta=\varepsilon/3$으로 잡으면 됩니다.
> **풀이.** $\lvert(3x-5)-7\rvert=3\lvert x-4\rvert$입니다. $\varepsilon>0$에 대해 $\delta=\varepsilon/3$이라 하면 $0<\lvert x-4\rvert<\delta$일 때 $3\lvert x-4\rvert<3\cdot\varepsilon/3=\varepsilon$입니다. $\square$

> **문제 2.** (표준) $\lim_{x\to 1}x^3=1$을 증명하십시오.
> **답.** $\delta=\min\{1,\ \varepsilon/7\}$로 잡으면 됩니다.
> **풀이.** $\lvert x^3-1\rvert=\lvert x-1\rvert\lvert x^2+x+1\rvert$입니다. 예비 제한 $\lvert x-1\rvert<1$을 두면 $0<x<2$이므로 $\lvert x^2+x+1\rvert<4+2+1=7$입니다. 따라서 $\delta=\min\{1,\varepsilon/7\}$이면 $\lvert x^3-1\rvert<7\cdot(\varepsilon/7)=\varepsilon$입니다. $\square$

> **문제 3.** (심화) $\lim_{x\to 9}\sqrt{x}=3$을 증명하십시오.
> **답.** $\delta=3\varepsilon$으로 잡으면 됩니다.
> **풀이.** $x\ge 0$에서 $\lvert\sqrt{x}-3\rvert=\dfrac{\lvert x-9\rvert}{\sqrt{x}+3}\le\dfrac{\lvert x-9\rvert}{3}$입니다. 분모가 항상 $3$ 이상이므로 예비 제한이 필요하지 않습니다. $\delta=3\varepsilon$이라 하면 $0<\lvert x-9\rvert<\delta$일 때 $\lvert\sqrt{x}-3\rvert<\varepsilon$입니다. $\square$

### 2.3 한쪽 극한

접근 방향을 한쪽으로 제한하면 한쪽 극한을 얻습니다. 오른쪽 극한은

$$
\lim_{x\to c^+}f(x)=L
\iff
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\ c<x<c+\delta\ \Rightarrow\ \lvert f(x)-L\rvert<\varepsilon
$$

으로 정의하고 $f(c^+)$라고 씁니다. 왼쪽 극한 $f(c^-)$는 조건을 $c-\delta<x<c$로 바꿉니다. 양쪽 정의를 비교하면 다음 정리를 얻습니다.

**정리.** $c$가 양쪽에서 모두 집적점이면 $\lim_{x\to c}f(x)=L$일 필요충분조건은 $f(c^+)=f(c^-)=L$입니다.

증명은 조건의 분해입니다. 양쪽 극한이 $L$이면 각각의 $\delta_1,\delta_2$를 얻고 $\delta=\min\{\delta_1,\delta_2\}$로 잡으면 $0<\lvert x-c\rvert<\delta$인 모든 $x$가 두 경우 중 하나에 들어가므로 오차가 $\varepsilon$ 미만입니다. 역방향은 $0<\lvert x-c\rvert<\delta$가 $c<x<c+\delta$와 $c-\delta<x<c$를 모두 포함하므로 자동으로 성립합니다. $\square$

> **문제 1.** (기초) $\operatorname{sgn}(x)$의 $x=0$에서의 한쪽 극한을 각각 구하십시오.
> **답.** $f(0^+)=1$, $f(0^-)=-1$입니다.
> **풀이.** $x>0$에서 $\operatorname{sgn}(x)=1$이므로 오른쪽 극한은 $1$이고, $x<0$에서 $\operatorname{sgn}(x)=-1$이므로 왼쪽 극한은 $-1$입니다. 두 값이 다르므로 $x=0$에서 극한은 존재하지 않습니다.

> **문제 2.** (표준) $f(x)=\lfloor x\rfloor$의 $x=2$에서 한쪽 극한을 구하고 극한의 존재를 판정하십시오.
> **답.** $f(2^+)=2$, $f(2^-)=1$이므로 극한은 존재하지 않습니다.
> **풀이.** $2\le x<3$에서 $\lfloor x\rfloor=2$이므로 오른쪽 극한은 $2$입니다. $1\le x<2$에서 $\lfloor x\rfloor=1$이므로 왼쪽 극한은 $1$입니다. 두 값이 다르므로 위 정리에 의해 양쪽 극한은 존재하지 않습니다.

### 2.4 수열 판정법

$\varepsilon$-$\delta$ 정의를 매번 다루는 대신 수열의 언어로 바꿔 쓰면 편리합니다.

**정리(극한의 수열 특성화).** $c$가 $D$의 집적점일 때 다음 두 조건은 동등합니다.

1. $\lim_{x\to c}f(x)=L$입니다.
2. $x_n\in D\setminus\{c\}$이고 $x_n\to c$인 모든 수열 $(x_n)$에 대해 $f(x_n)\to L$입니다.

증명을 봅니다. 먼저 1에서 2를 얻습니다. $\varepsilon>0$이 주어지면 정의에서 $\delta>0$을 얻습니다. $x_n\to c$이므로 어떤 $N$이 있어 $n\ge N$이면 $\lvert x_n-c\rvert<\delta$이고, $x_n\ne c$이므로 $0<\lvert x_n-c\rvert<\delta$입니다. 따라서 $n\ge N$에서 $\lvert f(x_n)-L\rvert<\varepsilon$이므로 $f(x_n)\to L$입니다.

다음으로 2에서 1을 얻습니다. 대우를 씁니다. 1이 거짓이면 정의의 부정에 의해 어떤 $\varepsilon_0>0$이 있어 모든 $\delta>0$에 대해 $0<\lvert x-c\rvert<\delta$이면서 $\lvert f(x)-L\rvert\ge\varepsilon_0$인 $x$가 존재합니다. $\delta=1/n$을 차례로 대입해 그런 점을 $x_n$이라 하면 $0<\lvert x_n-c\rvert<1/n$이므로 $x_n\to c$이고 $x_n\ne c$이지만 $\lvert f(x_n)-L\rvert\ge\varepsilon_0$이 모든 $n$에서 성립하므로 $f(x_n)\not\to L$입니다. 이는 2의 부정입니다. $\square$

이 정리의 실전 가치는 부존재 증명에 있습니다. $c$로 가는 두 수열에서 $f$의 극한이 다르면 $\lim_{x\to c}f(x)$는 존재하지 않습니다.

> **문제 1.** (표준) 수열 판정법으로 $\lim_{x\to 0}\sin\dfrac1x$이 존재하지 않음을 보이십시오.
> **답.** 극한이 $0$과 $1$로 갈라지는 두 수열이 있기 때문입니다.
> **풀이.** $x_n=\dfrac{1}{2n\pi}$이라 하면 $x_n\to 0$이고 $\sin(1/x_n)=\sin(2n\pi)=0$이므로 $f(x_n)\to 0$입니다. $y_n=\dfrac{1}{2n\pi+\pi/2}$이라 하면 $y_n\to 0$이고 $\sin(1/y_n)=1$이므로 $f(y_n)\to 1$입니다. 수열 판정법에 의해 극한은 존재하지 않습니다. $\square$

> **문제 2.** (표준) $\chi_{\mathbb{Q}}$에 대해 $\lim_{x\to 0}\chi_{\mathbb{Q}}(x)$가 존재하지 않음을 보이십시오.
> **답.** 유리수열과 무리수열이 각각 $1$과 $0$을 주기 때문입니다.
> **풀이.** $x_n=1/n$은 유리수이고 $0$으로 가므로 $\chi_{\mathbb{Q}}(x_n)=1\to 1$입니다. $y_n=\sqrt2/n$은 무리수이고 $0$으로 가므로 $\chi_{\mathbb{Q}}(y_n)=0\to 0$입니다. 두 극한이 다르므로 극한은 존재하지 않습니다. $\square$

### 2.5 극한의 사칙연산

**정리.** $\lim_{x\to c}f(x)=L$, $\lim_{x\to c}g(x)=M$이면 다음이 성립합니다.

$$
\lim_{x\to c}\bigl(f(x)+g(x)\bigr)=L+M,\qquad
\lim_{x\to c}\bigl(f(x)g(x)\bigr)=LM
$$

$$
M\ne 0\ \Rightarrow\ \lim_{x\to c}\frac{f(x)}{g(x)}=\frac{L}{M}
$$

합의 증명은 삼각부등식입니다. $\varepsilon>0$에 대해 $\lvert f(x)-L\rvert<\varepsilon/2$가 되는 $\delta_1$과 $\lvert g(x)-M\rvert<\varepsilon/2$가 되는 $\delta_2$를 얻어 $\delta=\min\{\delta_1,\delta_2\}$로 잡으면

$$
\lvert (f+g)(x)-(L+M)\rvert\le\lvert f(x)-L\rvert+\lvert g(x)-M\rvert<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon
$$

입니다. $\square$

곱의 증명은 한 인자를 유계화하는 단계가 추가됩니다.

$$
\lvert f(x)g(x)-LM\rvert
=\lvert f(x)\bigl(g(x)-M\bigr)+M\bigl(f(x)-L\bigr)\rvert
\le\lvert f(x)\rvert\,\lvert g(x)-M\rvert+\lvert M\rvert\,\lvert f(x)-L\rvert
$$

먼저 $\lvert f(x)-L\rvert<1$이 되는 $\delta_0$을 잡으면 그 근방에서 $\lvert f(x)\rvert<\lvert L\rvert+1$입니다. 이어서 $\lvert g(x)-M\rvert<\dfrac{\varepsilon}{2(\lvert L\rvert+1)}$과 $\lvert f(x)-L\rvert<\dfrac{\varepsilon}{2(\lvert M\rvert+1)}$이 되는 $\delta$들을 잡아 셋의 최소값을 취하면 우변이 $\varepsilon$ 미만입니다. $\square$

몫은 역수만 보면 충분합니다. $\lvert g(x)-M\rvert<\lvert M\rvert/2$가 되는 $\delta$를 잡으면 $\lvert g(x)\rvert>\lvert M\rvert/2$이므로

$$
\left\lvert\frac{1}{g(x)}-\frac1M\right\rvert=\frac{\lvert M-g(x)\rvert}{\lvert g(x)\rvert\lvert M\rvert}\le\frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert
$$

이고, 여기에 $\lvert g(x)-M\rvert<\dfrac{\lvert M\rvert^2\varepsilon}{2}$을 추가로 요구하면 됩니다. $\square$

> **문제 1.** (기초) $\lim_{x\to 2}(x^2+3x-1)$을 구하고 근거를 말하십시오.
> **답.** $9$입니다.
> **풀이.** $\lim_{x\to 2}x=2$와 상수 함수의 극한에서 시작해 곱과 합의 법칙을 적용하면 $2^2+3\cdot2-1=9$입니다. 다항함수는 항등함수와 상수함수에 사칙연산을 유한 번 적용해 얻으므로 극한이 대입값과 같습니다.

> **문제 2.** (표준) 곱의 극한 증명에서 $\lvert f(x)\rvert$를 유계화하는 단계가 필요한 이유를 말하십시오.
> **답.** $\lvert f(x)\rvert$가 변수이므로 상수 상한 없이는 $\varepsilon$을 배분할 수 없기 때문입니다.
> **풀이.** 부등식 우변의 첫 항은 $\lvert f(x)\rvert\lvert g(x)-M\rvert$입니다. $\lvert g(x)-M\rvert$을 작게 만들 계획을 세우려면 곱해질 계수가 미리 알려진 상수여야 합니다. 예비 제한으로 $\lvert f(x)\rvert<\lvert L\rvert+1$을 확보해 그 계수를 상수로 고정합니다.

### 2.6 극한이 존재하지 않음을 보이는 방법

부존재 증명은 정의의 부정을 정확히 쓰는 일에서 출발합니다. $\lim_{x\to c}f(x)=L$의 부정은 다음과 같습니다.

$$
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D:\ 0<\lvert x-c\rvert<\delta\ \wedge\ \lvert f(x)-L\rvert\ge\varepsilon_0
$$

부정을 취하면 한정기호가 모두 뒤바뀌고 함의는 연언으로 바뀝니다. 이 형태를 직접 쓰는 방법이 첫째 방법입니다. 극한이 아무 값도 될 수 없음을 보이려면 임의의 $L$에 대해 위 문장을 세워야 하므로 실전에서는 다음 세 방법이 더 쓰입니다.

- 두 수열 방법입니다. $c$로 가는 두 수열에서 $f$의 극한이 다르면 부존재입니다.
- 한쪽 극한 방법입니다. $f(c^+)\ne f(c^-)$이면 부존재입니다.
- 비유계 방법입니다. $c$의 임의의 근방에서 $\lvert f\rvert$가 유계가 아니면 부존재입니다.

세 번째 방법의 근거를 적어 둡니다. 극한이 $L$로 존재하면 $\varepsilon=1$에 대응하는 $\delta$가 있어 그 근방에서 $\lvert f(x)\rvert<\lvert L\rvert+1$이므로 $f$는 $c$의 어떤 근방에서 유계입니다. 대우를 취하면 근방마다 비유계이면 극한은 없습니다.

> **문제 1.** (표준) $\lim_{x\to 0}\dfrac1{x^2}$이 존재하지 않음을 유계성으로 보이십시오.
> **답.** $0$의 모든 근방에서 비유계이기 때문입니다.
> **풀이.** 임의의 $\delta>0$에 대해 $x=\min\{\delta,1\}/n$을 택하면 $0<\lvert x\rvert<\delta$이면서 $1/x^2\ge n^2/\min\{\delta,1\}^2$이므로 $n$을 키우면 값이 얼마든지 커집니다. 극한이 존재하면 어떤 근방에서 유계여야 하므로 극한은 존재하지 않습니다. $\square$

> **문제 2.** (심화) $f(x)=\dfrac{\lvert x\rvert}{x}$에 대해 $\lim_{x\to 0}f(x)=0$이 거짓임을 정의의 부정 형태로 쓰십시오.
> **답.** $\varepsilon_0=1$을 잡으면 모든 $\delta$에서 반례 점이 존재합니다.
> **풀이.** $\varepsilon_0=1$이라 합니다. 임의의 $\delta>0$에 대해 $x=\delta/2$를 택하면 $0<\lvert x-0\rvert<\delta$이고 $f(x)=1$이므로 $\lvert f(x)-0\rvert=1\ge\varepsilon_0$입니다. 이는 부정 문장을 그대로 실현하므로 극한은 $0$이 아닙니다. $\square$

### 2.7 연속의 정의와 동등 조건

극한과 함숫값이 일치하는 상황을 연속이라고 부릅니다. $c\in D$일 때

$$
f\text{가 }c\text{에서 연속}
\iff
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\ \lvert x-c\rvert<\delta\ \Rightarrow\ \lvert f(x)-f(c)\rvert<\varepsilon
$$

으로 정의합니다. 극한의 정의와 두 곳이 다릅니다. 목표값이 $L$ 대신 $f(c)$로 지정되어 있고, 가정에서 $0<\lvert x-c\rvert$가 빠져 $x=c$가 허용됩니다. $x=c$일 때 좌변이 $0$이므로 이 완화는 조건을 약화시키지 않습니다.

**정리(연속의 동등 조건).** $c\in D$에 대해 다음은 동등합니다.

1. $f$가 $c$에서 위 $\varepsilon$-$\delta$ 조건을 만족합니다.
2. $x_n\in D$, $x_n\to c$인 모든 수열에 대해 $f(x_n)\to f(c)$입니다.
3. $c$가 $D$의 집적점이면 $\lim_{x\to c}f(x)=f(c)$이고, $c$가 고립점이면 조건이 자동으로 성립합니다.

1과 2의 동등성은 2.4의 증명을 목표값 $f(c)$로 바꾸면 그대로 통합니다. 다만 수열에서 $x_n=c$를 허용해도 $\lvert f(x_n)-f(c)\rvert=0$이므로 문제가 없습니다. 1과 3의 동등성은 $x=c$를 넣고 빼는 차이만 다루면 됩니다. $c$가 고립점이면 $\lvert x-c\rvert<\delta$인 정의역 점이 $c$뿐이 되는 $\delta$가 있으므로 조건이 무조건 성립합니다. $\square$

조건 2가 실전에서 가장 자주 쓰입니다. "수렴하는 입력을 넣으면 함숫값도 수렴하고 극한을 함수 안으로 넣을 수 있다"가 연속의 실질적 내용입니다.

> **문제 1.** (기초) 연속의 정의에서 $0<\lvert x-c\rvert$ 조건을 뺀 이유를 말하십시오.
> **답.** $x=c$에서 오차가 $0$이므로 조건이 저절로 성립하기 때문입니다.
> **풀이.** $x=c$이면 $\lvert f(c)-f(c)\rvert=0<\varepsilon$입니다. 따라서 $x=c$를 검사 대상에 넣어도 조건은 변하지 않고, 정의가 간결해집니다.

> **문제 2.** (표준) $f(x)=x\,\chi_{\mathbb{Q}}(x)$가 $x=0$에서만 연속임을 보이십시오.
> **답.** $0$에서는 $\lvert f(x)\rvert\le\lvert x\rvert$로 연속이고, 다른 점에서는 두 수열이 값을 갈라 놓습니다.
> **풀이.** $0$에서는 모든 $x$에 대해 $\lvert f(x)-f(0)\rvert=\lvert f(x)\rvert\le\lvert x\rvert$이므로 $\delta=\varepsilon$으로 잡으면 됩니다. $c\ne 0$에서는 $c$로 가는 유리수열 $x_n$과 무리수열 $y_n$을 잡으면 $f(x_n)=x_n\to c$이고 $f(y_n)=0\to 0$입니다. $c\ne 0$이므로 두 극한이 다르고 조건 2가 깨지므로 불연속입니다. $\square$

> **문제 3.** (심화) $f$가 $c$에서 연속이고 $f(c)>0$이면 $c$의 어떤 근방에서 $f>0$임을 보이십시오.
> **답.** $\varepsilon=f(c)/2$를 잡으면 그 근방에서 $f(x)>f(c)/2>0$입니다.
> **풀이.** $\varepsilon=f(c)/2>0$에 대응하는 $\delta$를 잡습니다. $\lvert x-c\rvert<\delta$이면 $\lvert f(x)-f(c)\rvert<f(c)/2$이므로 $f(x)>f(c)-f(c)/2=f(c)/2>0$입니다. 따라서 그 근방 전체에서 $f$는 양수입니다. $\square$

### 2.8 불연속의 분류

$c$에서 연속이 아닌 경우는 한쪽 극한의 거동으로 분류합니다.

| 종류 | 조건 | 예 |
|---|---|---|
| 제거가능 불연속 | $\lim_{x\to c}f(x)$가 존재하지만 $f(c)$와 다르거나 $f(c)$가 없다 | $f(x)=\dfrac{\sin x}{x}$, $f(0)=1$이 아닐 때 |
| 도약 불연속 | $f(c^+)$와 $f(c^-)$가 모두 존재하고 서로 다르다 | $\operatorname{sgn}(x)$의 $x=0$ |
| 무한 불연속 | 한쪽 근방에서 $\lvert f\rvert$가 비유계다 | $1/x$의 $x=0$ |
| 진동 불연속 | 한쪽 극한이 존재하지 않고 값이 계속 진동한다 | $\sin(1/x)$의 $x=0$ |

제거가능 불연속은 $f(c)$의 값을 극한값으로 다시 정의하면 연속이 됩니다. 나머지 셋은 한 점의 값을 바꿔서는 고칠 수 없습니다. 도약과 무한과 진동을 묶어 본질적 불연속이라고 부릅니다.

> **문제 1.** (기초) $f(x)=\dfrac{x^2-4}{x-2}$의 $x=2$에서 불연속 종류를 판정하십시오.
> **답.** 제거가능 불연속입니다.
> **풀이.** $x\ne 2$에서 $f(x)=x+2$이므로 $\lim_{x\to 2}f(x)=4$입니다. 극한은 존재하지만 $f(2)$가 정의되지 않았습니다. $f(2)=4$로 정의하면 연속이 되므로 제거가능입니다.

> **문제 2.** (표준) $f(x)=\dfrac{1}{1+2^{1/x}}$의 $x=0$에서 불연속 종류를 판정하십시오.
> **답.** 도약 불연속입니다.
> **풀이.** $x\to 0^+$이면 $1/x\to+\infty$이므로 $2^{1/x}\to+\infty$이고 $f(0^+)=0$입니다. $x\to 0^-$이면 $1/x\to-\infty$이므로 $2^{1/x}\to 0$이고 $f(0^-)=1$입니다. 두 한쪽 극한이 존재하고 서로 다르므로 도약 불연속입니다.

### 2.9 합성함수의 연속과 초등함수의 연속성

**정리(합성의 연속).** $g$가 $c$에서 연속이고 $f$가 $g(c)$에서 연속이면 $f\circ g$는 $c$에서 연속입니다.

증명은 두 정의를 사슬로 잇습니다. $\varepsilon>0$이 주어졌다고 합니다. $f$가 $b=g(c)$에서 연속이므로 $\lvert y-b\rvert<\eta\Rightarrow\lvert f(y)-f(b)\rvert<\varepsilon$인 $\eta>0$이 있습니다. 이제 이 $\eta$를 $g$의 목표 오차로 넘깁니다. $g$가 $c$에서 연속이므로 $\lvert x-c\rvert<\delta\Rightarrow\lvert g(x)-b\rvert<\eta$인 $\delta>0$이 있습니다. 두 함의를 이으면 $\lvert x-c\rvert<\delta$일 때 $\lvert f(g(x))-f(g(c))\rvert<\varepsilon$입니다. $\square$

이 증명에서 순서가 중요합니다. 바깥 함수 $f$의 $\delta$가 안쪽 함수 $g$의 $\varepsilon$ 역할을 합니다. 극한만으로는 같은 결론이 나오지 않습니다. $g$의 극한이 $b$이고 $f$의 극한이 $L$이더라도 $g$가 $b$를 실제로 취하면서 $f(b)\ne L$인 경우 합성의 극한이 $L$이 아닐 수 있습니다. 그래서 바깥 함수에 연속을 요구합니다.

초등함수의 연속성을 정의에서 확인합니다.

- 상수함수와 항등함수는 연속입니다. 상수함수는 $\delta$를 아무것으로나 잡으면 되고, 항등함수는 $\delta=\varepsilon$으로 잡으면 됩니다.
- 다항함수는 연속입니다. 위 두 함수에 합과 곱의 법칙을 유한 번 적용해 얻습니다.
- 유리함수는 분모가 $0$이 아닌 모든 점에서 연속입니다. 몫의 법칙을 적용합니다.
- $\sin$과 $\cos$은 모든 점에서 연속입니다. 합차 공식과 $\lvert\sin t\rvert\le\lvert t\rvert$에서 $\lvert\sin x-\sin c\rvert=2\left\lvert\sin\dfrac{x-c}{2}\right\rvert\left\lvert\cos\dfrac{x+c}{2}\right\rvert\le\lvert x-c\rvert$이므로 $\delta=\varepsilon$으로 충분합니다.
- $\sqrt{x}$는 $[0,\infty)$에서 연속입니다. $c>0$에서는 2.2의 계산이 통하고, $c=0$에서는 $\lvert\sqrt{x}\rvert<\varepsilon$이 $x<\varepsilon^2$과 같으므로 $\delta=\varepsilon^2$으로 잡습니다.
- $\tan$과 $\log$처럼 위 함수들의 몫이나 역함수로 얻어지는 함수는 정의역 안에서 연속입니다. 역함수의 연속성은 [9. 중간값 정리와 최대최소 정리](../9. 중간값 정리와 최대최소 정리/index.md)에서 단조성과 함께 증명합니다.

> **문제 1.** (기초) $h(x)=\sin(x^2+1)$이 모든 실수에서 연속인 이유를 말하십시오.
> **답.** 다항함수와 $\sin$이 연속이고 합성이 연속을 보존하기 때문입니다.
> **풀이.** $g(x)=x^2+1$은 다항함수이므로 모든 점에서 연속이고, $f(y)=\sin y$는 모든 점에서 연속입니다. 합성의 연속 정리에 의해 $h=f\circ g$는 모든 점에서 연속입니다.

> **문제 2.** (표준) $\lvert\sin x-\sin c\rvert\le\lvert x-c\rvert$를 이용해 $\sin$의 연속을 $\varepsilon$-$\delta$로 쓰십시오.
> **답.** $\delta=\varepsilon$으로 잡으면 됩니다.
> **풀이.** $\varepsilon>0$에 대해 $\delta=\varepsilon$이라 합니다. $\lvert x-c\rvert<\delta$이면 $\lvert\sin x-\sin c\rvert\le\lvert x-c\rvert<\varepsilon$입니다. 이때 $\delta$가 $c$에 전혀 의존하지 않는데, 이 성질이 10강의 일양연속입니다. $\square$

> **문제 3.** (심화) $g(x)=0$인 상수함수와 $f(y)=\begin{cases}1,& y\ne 0\\ 0,& y=0\end{cases}$에서 $\lim_{y\to 0}f(y)=1$이지만 $\lim_{x\to 0}f(g(x))\ne 1$임을 확인하십시오.
> **답.** $f(g(x))=f(0)=0$이므로 합성의 극한은 $0$입니다.
> **풀이.** $g$는 모든 점에서 $0$이므로 $f(g(x))=f(0)=0$이고 합성의 극한은 $0$입니다. $f$의 $y\to0$ 극한은 $1$이지만 $f$는 $0$에서 연속이 아니므로 극한만으로는 합성이 통하지 않습니다. 합성 정리가 바깥 함수의 연속을 요구하는 이유입니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 문장 | 요령 |
|---|---|---|
| 극한 정의 | $\forall\varepsilon\ \exists\delta\ (0<\lvert x-c\rvert<\delta\Rightarrow\lvert f(x)-L\rvert<\varepsilon)$ | $\delta$는 $\varepsilon$의 함수, $x=c$는 제외 |
| $\delta$ 구성 | $\lvert f(x)-L\rvert=\lvert x-c\rvert\cdot(\text{나머지})$ | 예비 제한으로 나머지를 유계화한 뒤 $\min$을 취한다 |
| 분모 처리 | $\lvert g(x)\rvert>\lvert M\rvert/2$ 확보 | 분모는 반드시 아래에서 막는다 |
| 한쪽 극한 | $\lim_{x\to c}f=L\iff f(c^+)=f(c^-)=L$ | 두 값이 다르면 극한 없음 |
| 수열 판정 | $x_n\to c,\ x_n\ne c\Rightarrow f(x_n)\to L$ | 두 수열이 갈라지면 부존재 |
| 사칙연산 | 합·곱·몫의 극한은 극한의 합·곱·몫 | 곱은 한 인자 유계화, 몫은 $M\ne0$ |
| 부존재 증명 | 두 수열, 한쪽 극한, 비유계 | 정의의 부정을 직접 쓰는 것은 최후 수단 |
| 연속 정의 | $\forall\varepsilon\ \exists\delta\ (\lvert x-c\rvert<\delta\Rightarrow\lvert f(x)-f(c)\rvert<\varepsilon)$ | 목표값이 $f(c)$로 지정됨 |
| 연속 동등 조건 | $\varepsilon$-$\delta$ $\iff$ 수열 조건 $\iff$ 극한이 $f(c)$ | 실전에서는 수열 조건 |
| 불연속 분류 | 제거가능·도약·무한·진동 | 한쪽 극한의 존재와 유계성으로 나눈다 |
| 합성의 연속 | $g$가 $c$에서, $f$가 $g(c)$에서 연속 | 바깥 $\delta$가 안쪽 $\varepsilon$이 된다 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $\lim_{x\to 5}(2x+1)=11$을 $\varepsilon$-$\delta$로 증명하십시오.
> **답.** $\delta=\varepsilon/2$로 잡으면 됩니다.
> **풀이.** $\lvert(2x+1)-11\rvert=2\lvert x-5\rvert$입니다. $\delta=\varepsilon/2$이면 $0<\lvert x-5\rvert<\delta$일 때 $2\lvert x-5\rvert<\varepsilon$입니다. $\square$

> **문제 2.** (기초) $\lim_{x\to c}f(x)=L$의 부정을 한정기호로 쓰십시오.
> **답.** $\exists\varepsilon_0>0\ \forall\delta>0\ \exists x:\ 0<\lvert x-c\rvert<\delta\ \wedge\ \lvert f(x)-L\rvert\ge\varepsilon_0$입니다.
> **풀이.** 부정은 한정기호를 뒤바꾸고 함의 $P\Rightarrow Q$를 $P\wedge\lnot Q$로 바꿉니다. $\forall\varepsilon$은 $\exists\varepsilon_0$이 되고 $\exists\delta$는 $\forall\delta$가 됩니다.

> **문제 3.** (표준) $\lim_{x\to 2}\dfrac{x^2-4}{x-2}=4$를 $\varepsilon$-$\delta$로 증명하십시오.
> **답.** $\delta=\varepsilon$으로 잡으면 됩니다.
> **풀이.** $0<\lvert x-2\rvert$이면 $x\ne 2$이므로 $\dfrac{x^2-4}{x-2}=x+2$입니다. 따라서 $\left\lvert\dfrac{x^2-4}{x-2}-4\right\rvert=\lvert x-2\rvert$이고 $\delta=\varepsilon$이면 조건이 만족됩니다. $x=c$를 제외하는 정의 덕분에 약분이 정당합니다. $\square$

> **문제 4.** (표준) $f(x)=\begin{cases}x^2,& x\le 1\\ 2x,& x>1\end{cases}$의 $x=1$에서 연속성을 판정하십시오.
> **답.** 불연속이며 도약 불연속입니다.
> **풀이.** $f(1^-)=\lim_{x\to1^-}x^2=1$이고 $f(1^+)=\lim_{x\to1^+}2x=2$입니다. 두 한쪽 극한이 존재하지만 다르므로 극한이 없고, $f(1)=1$과도 어긋납니다. 따라서 도약 불연속입니다.

> **문제 5.** (표준) $\lim_{x\to 0}x\sin\dfrac1x=0$을 증명하십시오.
> **답.** $\delta=\varepsilon$으로 잡으면 됩니다.
> **풀이.** $x\ne 0$에서 $\left\lvert x\sin\dfrac1x\right\rvert\le\lvert x\rvert$입니다. $\varepsilon>0$에 대해 $\delta=\varepsilon$이라 하면 $0<\lvert x\rvert<\delta$일 때 좌변이 $\varepsilon$ 미만입니다. $\sin(1/x)$ 자체는 극한이 없지만 유계이므로 $x$가 눌러 줍니다. $\square$

> **문제 6.** (심화) $f$가 $c$에서 연속이면 $\lvert f\rvert$도 $c$에서 연속임을 보이고, 역이 거짓임을 반례로 보이십시오.
> **답.** $\bigl\lvert\lvert f(x)\rvert-\lvert f(c)\rvert\bigr\rvert\le\lvert f(x)-f(c)\rvert$이므로 같은 $\delta$가 통하고, 역의 반례는 $f=\operatorname{sgn}$입니다.
> **풀이.** 삼각부등식의 따름 정리로 $\bigl\lvert\lvert a\rvert-\lvert b\rvert\bigr\rvert\le\lvert a-b\rvert$입니다. 따라서 $f$의 $\delta$를 그대로 쓰면 $\lvert f\rvert$의 조건이 성립합니다. 역의 반례로 $f(x)=\operatorname{sgn}(x)$에 $f(0)=1$을 주면 $\lvert f\rvert\equiv 1$은 연속이지만 $f$는 $0$에서 도약 불연속입니다. $\square$

> **문제 7.** (심화) $f:\mathbb{R}\to\mathbb{R}$이 모든 점에서 연속이고 모든 유리수 $q$에서 $f(q)=0$이면 $f\equiv 0$임을 보이십시오.
> **답.** 임의의 실수로 가는 유리수열을 잡아 수열 조건을 적용하면 됩니다.
> **풀이.** 임의의 $c\in\mathbb{R}$를 택합니다. 유리수의 조밀성에 의해 $q_n\to c$인 유리수열이 있습니다. $f$가 $c$에서 연속이므로 수열 조건에서 $f(c)=\lim f(q_n)=\lim 0=0$입니다. $c$가 임의였으므로 $f\equiv 0$입니다. $\square$

## 5. 스스로 점검

1. 함수의 극한을 $\varepsilon$-$\delta$로 정의하고 집적점 조건이 필요한 이유를 말할 수 있는가?
2. $\forall\varepsilon\ \exists\delta$의 순서를 뒤집으면 무엇이 달라지는지 설명할 수 있는가?
3. $\lim_{x\to 3}x^2=9$를 $\delta$를 명시해 증명할 수 있는가?
4. 극한의 수열 특성화를 진술하고 역방향 증명의 골격을 재현할 수 있는가?
5. 곱의 극한 증명에서 유계화 단계가 왜 필요한지 말할 수 있는가?
6. 연속의 세 동등 조건을 진술하고 서로 옮길 수 있는가?
7. 불연속 네 종류를 예와 함께 구분할 수 있는가?
8. 합성함수의 연속 증명에서 $\varepsilon$과 $\delta$가 전달되는 방향을 말할 수 있는가?

**정답 요지.** 1. $\forall\varepsilon\exists\delta\forall x(0<\lvert x-c\rvert<\delta\Rightarrow\lvert f(x)-L\rvert<\varepsilon)$이고, $c$ 주변에 검사할 정의역 점이 남아 있어야 정의가 뜻을 가집니다. 2. $\exists\delta\forall\varepsilon$이면 근방에서 $f$가 상수 $L$이라는 강한 주장이 됩니다. 3. $\lvert x^2-9\rvert=\lvert x-3\rvert\lvert x+3\rvert$이고 $\delta=\min\{1,\varepsilon/7\}$입니다. 4. 모든 수열 $x_n\to c$, $x_n\ne c$에서 $f(x_n)\to L$과 동등하고, 역방향은 $\delta=1/n$로 반례 수열을 뽑습니다. 5. $\lvert f(x)\rvert$가 변수라 상수 상한이 없으면 $\varepsilon$을 배분할 수 없습니다. 6. $\varepsilon$-$\delta$, 모든 수열 $x_n\to c$에서 $f(x_n)\to f(c)$, 집적점에서 $\lim_{x\to c}f=f(c)$입니다. 7. 제거가능은 $\sin x/x$, 도약은 $\operatorname{sgn}$, 무한은 $1/x$, 진동은 $\sin(1/x)$입니다. 8. 바깥 함수의 $\delta$가 안쪽 함수의 $\varepsilon$으로 전달됩니다.
