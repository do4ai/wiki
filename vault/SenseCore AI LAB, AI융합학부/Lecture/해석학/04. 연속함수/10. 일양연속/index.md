---
title: "10. 일양연속"
---
# 10강. 일양연속

## 이 강의에서 할 수 있게 되는 것

- 일양연속을 $\varepsilon$-$\delta$로 정의하고 각 점의 연속과 한정기호 순서로 구별할 수 있습니다.
- 연속이지만 일양연속이 아닌 함수의 반례를 두 수열로 증명할 수 있습니다.
- 하이네-칸토어 정리를 진술하고 볼차노-바이어슈트라스 정리로 증명할 수 있습니다.
- 립시츠 조건이 일양연속의 충분조건이지만 필요조건이 아님을 예로 설명할 수 있습니다.
- 일양연속함수가 코시 수열을 코시 수열로 보낸다는 성질을 증명하고 확장 정리에 적용할 수 있습니다.

이 강의는 [8. 함수의 극한과 연속의 ε-δ 정의](../8. 함수의 극한과 연속의 ε-δ 정의/index.md)의 연속 정의에서 $\delta$의 점 의존성만 떼어 내 새 개념을 세웁니다. 증명 도구는 [4. 단조수렴정리와 볼차노-바이어슈트라스](../../02. 수열의 극한/4. 단조수렴정리와 볼차노-바이어슈트라스/index.md)의 부분수열 정리와 [5. 코시 수열과 완비성](../../02. 수열의 극한/5. 코시 수열과 완비성/index.md)의 코시 판정입니다. 여기서 얻는 일양연속은 [12. 리만적분의 정의와 적분가능성](../../05. 미분과 적분의 엄밀화/12. 리만적분의 정의와 적분가능성/index.md)에서 연속함수의 적분가능성을 증명할 때 핵심 도구로 다시 쓰입니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\varepsilon$ | 엡실론 | 목표 오차 |
| $\delta$ | 델타 | 정의역 쪽 폭 |
| $\delta(\varepsilon)$ | 델타 오브 엡실론 | $\varepsilon$에만 의존하는 $\delta$, 일양연속의 표시 |
| $\delta(\varepsilon,c)$ | 델타 오브 엡실론 씨 | $\varepsilon$과 점 $c$에 함께 의존하는 $\delta$ |
| $\lvert x-y\rvert<\delta$ | 두 점 거리 | 두 정의역 점 사이의 거리 조건 |
| $L$ | 립시츠 상수 | $\lvert f(x)-f(y)\rvert\le L\lvert x-y\rvert$의 계수 |
| $(x_n),(y_n)$ | 두 수열 | 반례 구성에 쓰는 두 점열 |
| $\varepsilon_0$ | 엡실론 제로 | 부정 문장에서 고정하는 반례 오차 |
| $\overline{D}$ | 디의 폐포 | $D$와 그 집적점을 모두 모은 집합 |
| $\square$ | 증명 끝 | 증명이 종료됨을 표시 |

## 2. 개념

### 2.1 일양연속의 정의

연속의 정의를 정의역 전체에 대해 다시 씁니다. $f:D\to\mathbb{R}$가 $D$에서 연속이라는 것은 다음을 뜻합니다.

$$
\forall c\in D\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\ \lvert x-c\rvert<\delta\ \Rightarrow\ \lvert f(x)-f(c)\rvert<\varepsilon
$$

여기서 $\exists\delta$가 $\forall c$와 $\forall\varepsilon$ 뒤에 놓여 있으므로 $\delta$는 두 값에 모두 의존할 수 있습니다. 즉 $\delta=\delta(\varepsilon,c)$입니다. 점을 옮기면 $\delta$를 다시 골라도 됩니다.

일양연속은 $\delta$가 점에 의존하지 못하게 순서를 바꾼 조건입니다.

$$
f\text{가 }D\text{에서 일양연속}
\iff
\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in D:\ \lvert x-y\rvert<\delta\ \Rightarrow\ \lvert f(x)-f(y)\rvert<\varepsilon
$$

$\exists\delta$가 $\forall x,y$보다 앞에 왔습니다. 하나의 $\delta$가 정의역의 모든 점 쌍을 동시에 처리해야 합니다. 이것이 두 개념의 유일한 차이이며, 그 차이가 전부입니다.

두 정의의 관계는 한 방향으로만 성립합니다. 일양연속이면 각 점 $c$에서 $y=c$로 두면 연속의 조건이 그대로 나오므로 연속입니다. 역은 성립하지 않고, 반례를 다음 절에서 봅니다.

정의를 말로 옮기면 이해가 쉬워집니다. 연속은 "각 점마다 충분히 가까우면 값이 가깝다"이고, 일양연속은 "정의역 전체에 통하는 하나의 가까움 기준이 있다"입니다. 그래프로 보면 폭 $\delta$, 높이 $\varepsilon$의 직사각형을 하나 만들어 그래프 위의 어느 점에 갖다 대도 그 직사각형 안에 그래프가 들어간다는 뜻입니다.

> **문제 1.** (기초) 연속과 일양연속의 정의에서 다른 부분을 한정기호로 지적하십시오.
> **답.** $\exists\delta$가 점을 나타내는 전칭 한정기호보다 앞에 오는지 뒤에 오는지가 다릅니다.
> **풀이.** 연속은 $\forall c\ \forall\varepsilon\ \exists\delta$이므로 $\delta$가 $c$에 의존합니다. 일양연속은 $\forall\varepsilon\ \exists\delta\ \forall x,y$이므로 $\delta$를 고른 뒤에 점 쌍이 결정되고 $\delta$는 점에 의존할 수 없습니다.

> **문제 2.** (기초) $f(x)=3x-1$이 $\mathbb{R}$에서 일양연속임을 보이십시오.
> **답.** $\delta=\varepsilon/3$으로 잡으면 됩니다.
> **풀이.** 임의의 $x,y\in\mathbb{R}$에서 $\lvert f(x)-f(y)\rvert=3\lvert x-y\rvert$입니다. $\varepsilon>0$에 대해 $\delta=\varepsilon/3$이라 하면 $\lvert x-y\rvert<\delta$일 때 $3\lvert x-y\rvert<\varepsilon$입니다. 이 $\delta$가 점에 전혀 의존하지 않으므로 일양연속입니다. $\square$

> **문제 3.** (표준) 일양연속이면 연속임을 정의에서 확인하십시오.
> **답.** 정의의 $y$에 $c$를 대입하면 연속의 조건이 됩니다.
> **풀이.** $\varepsilon>0$에 대해 일양연속의 $\delta$를 얻습니다. 임의의 $c\in D$를 고정하고 정의의 $y$ 자리에 $c$를 넣으면 모든 $x\in D$에서 $\lvert x-c\rvert<\delta\Rightarrow\lvert f(x)-f(c)\rvert<\varepsilon$입니다. 이는 $c$에서의 연속 조건이고 $c$가 임의였으므로 $f$는 연속입니다. $\square$

### 2.2 일양연속의 부정과 두 수열 판정

반례를 만들려면 정의의 부정을 정확히 써야 합니다.

$$
f\text{가 }D\text{에서 일양연속이 아니다}
\iff
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x,y\in D:\ \lvert x-y\rvert<\delta\ \wedge\ \lvert f(x)-f(y)\rvert\ge\varepsilon_0
$$

이 문장을 수열로 바꾸면 훨씬 쓰기 쉽습니다. $\delta=1/n$을 차례로 대입해 나쁜 점 쌍을 뽑으면 다음 판정이 나옵니다.

**정리(두 수열 판정).** $f$가 $D$에서 일양연속이 아닐 필요충분조건은 $\lvert x_n-y_n\rvert\to 0$이면서 어떤 $\varepsilon_0>0$에 대해 모든 $n$에서 $\lvert f(x_n)-f(y_n)\rvert\ge\varepsilon_0$인 두 수열 $(x_n),(y_n)$이 $D$에 존재하는 것입니다.

한 방향은 위에서 설명한 대로 $\delta=1/n$ 대입입니다. 반대 방향은 그런 두 수열이 있으면 임의의 $\delta>0$에 대해 $\lvert x_n-y_n\rvert<\delta$가 되는 $n$이 있고 그 쌍이 부정 문장의 증거가 되기 때문입니다. $\square$

실전에서는 다음 요령을 씁니다. 두 점을 서로 가깝게 붙이면서 함숫값 차이가 줄지 않는 곳을 찾습니다. 그런 곳은 그래프의 기울기가 무한히 커지는 지점이거나 진동이 무한히 빨라지는 지점입니다.

> **문제 1.** (표준) 두 수열 판정이 정의의 부정과 동등한 이유를 말하십시오.
> **답.** 모든 $\delta$에서의 존재 주장을 $\delta=1/n$으로 실현해 수열로 바꾼 것입니다.
> **풀이.** 부정 문장은 모든 $\delta$에 대해 나쁜 쌍이 있다고 말합니다. $\delta=1/n$을 대입해 쌍 $(x_n,y_n)$을 뽑으면 $\lvert x_n-y_n\rvert<1/n\to0$이고 함숫값 차이는 $\varepsilon_0$ 이상으로 유지됩니다. 역으로 그런 수열이 있으면 주어진 $\delta$에 대해 $1/n<\delta$인 $n$의 쌍을 증거로 제시할 수 있습니다.

> **문제 2.** (표준) $f(x)=\dfrac1x$가 $(0,1]$에서 일양연속이 아님을 두 수열로 보이십시오.
> **답.** $x_n=\dfrac1n$, $y_n=\dfrac1{2n}$을 잡으면 됩니다.
> **풀이.** $\lvert x_n-y_n\rvert=\dfrac1{2n}\to0$입니다. 그런데 $\lvert f(x_n)-f(y_n)\rvert=\lvert n-2n\rvert=n\ge1$이므로 $\varepsilon_0=1$에 대해 조건이 모든 $n$에서 유지됩니다. 두 수열 판정에 의해 일양연속이 아닙니다. $\square$

### 2.3 일양연속이 아닌 대표 예 셋

세 반례를 이유별로 정리합니다. 각각 원인이 다릅니다.

첫째, $f(x)=\dfrac1x$를 $(0,1]$에서 봅니다. 원인은 $0$ 근처에서 기울기가 무한히 커지는 것입니다. 2.2의 문제 2에서 보았듯 $x_n=1/n$, $y_n=1/(2n)$이 반례 쌍입니다. 점 $c$에서의 $\delta$를 계산해 보면 $\delta$가 $c^2$ 정도로 작아져야 하므로 $c\to0^+$에서 $\delta$가 $0$으로 눌립니다. 하나의 $\delta$로는 전 구간을 덮을 수 없습니다.

둘째, $f(x)=x^2$을 $\mathbb{R}$에서 봅니다. 원인은 큰 $x$에서 기울기가 무한히 커지는 것입니다. $x_n=n+\dfrac1n$, $y_n=n$이라 하면

$$
\lvert x_n-y_n\rvert=\frac1n\to0,\qquad
\lvert f(x_n)-f(y_n)\rvert=\left(n+\frac1n\right)^2-n^2=2+\frac1{n^2}\ge 2
$$

이므로 $\varepsilon_0=2$에 대해 판정 조건이 성립합니다. 따라서 $x^2$은 $\mathbb{R}$에서 일양연속이 아닙니다. 다만 $[0,M]$처럼 유계 구간으로 제한하면 일양연속입니다. $\lvert x^2-y^2\rvert=\lvert x+y\rvert\lvert x-y\rvert\le 2M\lvert x-y\rvert$이므로 $\delta=\varepsilon/(2M)$으로 잡으면 됩니다.

셋째, $f(x)=\sin\dfrac1x$를 $(0,1]$에서 봅니다. 원인은 기울기가 아니라 진동의 속도입니다. $x_n=\dfrac{1}{2n\pi}$, $y_n=\dfrac{1}{2n\pi+\pi/2}$이라 하면 두 점의 거리는

$$
\lvert x_n-y_n\rvert=\frac{\pi/2}{2n\pi\left(2n\pi+\pi/2\right)}\to 0
$$

이지만 $f(x_n)=0$, $f(y_n)=1$이므로 함숫값 차이가 항상 $1$입니다. $\varepsilon_0=1$로 두면 판정 조건이 성립합니다. 이 함수는 유계인데도 일양연속이 아니므로, 유계성만으로는 일양연속을 보장하지 못함을 보여 줍니다.

세 예의 공통점은 정의역이 닫힌 유계 구간이 아니라는 점입니다. 첫째와 셋째는 왼쪽 끝이 빠졌고, 둘째는 유계가 아닙니다. 다음 절의 정리가 이 관찰을 정리로 만듭니다.

> **문제 1.** (표준) $f(x)=x^2$이 $[-5,5]$에서 일양연속임을 $\delta$를 명시해 보이십시오.
> **답.** $\delta=\varepsilon/10$으로 잡으면 됩니다.
> **풀이.** $x,y\in[-5,5]$에서 $\lvert x^2-y^2\rvert=\lvert x+y\rvert\lvert x-y\rvert\le 10\lvert x-y\rvert$입니다. $\delta=\varepsilon/10$이면 $\lvert x-y\rvert<\delta$일 때 값 차이가 $\varepsilon$ 미만입니다. 이 $\delta$가 점에 의존하지 않으므로 일양연속입니다. $\square$

> **문제 2.** (표준) $f(x)=\sqrt{x}$가 $[0,\infty)$에서 일양연속임을 보이십시오.
> **답.** $\delta=\varepsilon^2$으로 잡으면 됩니다.
> **풀이.** $x\ge y\ge0$이라 해도 무방합니다. $\sqrt{x}\le\sqrt{y}+\sqrt{x-y}$가 성립하므로 $\lvert\sqrt{x}-\sqrt{y}\rvert\le\sqrt{\lvert x-y\rvert}$입니다. 앞 부등식은 양변을 제곱해 $x\le y+2\sqrt{y}\sqrt{x-y}+(x-y)$로 정리하면 확인됩니다. 따라서 $\delta=\varepsilon^2$이면 $\lvert x-y\rvert<\delta$일 때 값 차이가 $\varepsilon$ 미만입니다. 원점에서 기울기가 무한이지만 일양연속임에 유의합니다. $\square$

> **문제 3.** (심화) $f(x)=\sin x$가 $\mathbb{R}$에서 일양연속임을 보이십시오.
> **답.** $\delta=\varepsilon$으로 잡으면 됩니다.
> **풀이.** 합차 공식과 $\lvert\sin t\rvert\le\lvert t\rvert$에서 $\lvert\sin x-\sin y\rvert=2\left\lvert\sin\dfrac{x-y}{2}\right\rvert\left\lvert\cos\dfrac{x+y}{2}\right\rvert\le\lvert x-y\rvert$입니다. $\delta=\varepsilon$으로 잡으면 조건이 성립합니다. $\sin(1/x)$가 일양연속이 아닌 것은 $\sin$의 잘못이 아니라 안쪽 $1/x$가 진동을 무한히 압축하기 때문입니다. $\square$

### 2.4 하이네-칸토어 정리

**정리(하이네-칸토어).** $f$가 닫힌 유계 구간 $[a,b]$에서 연속이면 $f$는 $[a,b]$에서 일양연속입니다.

귀류법으로 증명합니다. $f$가 일양연속이 아니라고 가정합니다. 두 수열 판정에 의해 어떤 $\varepsilon_0>0$과 수열 $(x_n),(y_n)\subseteq[a,b]$가 있어

$$
\lvert x_n-y_n\rvert<\frac1n,\qquad
\lvert f(x_n)-f(y_n)\rvert\ge\varepsilon_0
$$

이 모든 $n$에서 성립합니다. $(x_n)$은 $[a,b]$ 안의 수열이므로 유계이고, 볼차노-바이어슈트라스 정리에 의해 수렴하는 부분수열 $(x_{n_k})$가 있습니다. 그 극한을 $x_0$이라 하면 $a\le x_{n_k}\le b$에서 $x_0\in[a,b]$입니다.

같은 첨자로 $(y_{n_k})$를 보면

$$
\lvert y_{n_k}-x_0\rvert\le\lvert y_{n_k}-x_{n_k}\rvert+\lvert x_{n_k}-x_0\rvert<\frac{1}{n_k}+\lvert x_{n_k}-x_0\rvert\to 0
$$

이므로 $y_{n_k}\to x_0$입니다. 두 수열이 같은 점으로 수렴한다는 것이 핵심입니다.

$f$가 $x_0$에서 연속이므로 수열 판정에 의해 $f(x_{n_k})\to f(x_0)$이고 $f(y_{n_k})\to f(x_0)$입니다. 따라서

$$
\lvert f(x_{n_k})-f(y_{n_k})\rvert\le\lvert f(x_{n_k})-f(x_0)\rvert+\lvert f(x_0)-f(y_{n_k})\rvert\to 0
$$

입니다. 그런데 좌변은 모든 $k$에서 $\varepsilon_0>0$ 이상이므로 $0$으로 수렴할 수 없습니다. 이는 모순입니다. 따라서 $f$는 $[a,b]$에서 일양연속입니다. $\square$

정리가 쓰는 조건을 확인합니다. 유계와 닫힘은 부분수열의 극한을 정의역 안에 붙잡는 데 함께 필요하고, 연속은 그 극한에서 두 함숫값을 같은 값으로 모으는 데 필요합니다. 2.3의 세 반례는 각각 이 조건 중 하나를 위반합니다.

정리의 실질적 의미는 다음과 같습니다. 닫힌 유계 구간에서는 연속과 일양연속을 구별할 필요가 없습니다. 두 개념이 갈라지는 것은 정의역이 열려 있거나 비유계일 때뿐입니다. 리만적분에서 연속함수가 적분가능함을 증명할 때 이 정리를 써서 분할의 폭을 구간 전체에 일률적으로 잡습니다.

> **문제 1.** (기초) 하이네-칸토어 정리로 $f(x)=x^3$이 $[-2,3]$에서 일양연속임을 결론하십시오.
> **답.** 다항함수가 닫힌 유계 구간에서 연속이므로 일양연속입니다.
> **풀이.** $x^3$은 다항함수이므로 모든 점에서 연속이고, $[-2,3]$은 닫힌 유계 구간입니다. 하이네-칸토어 정리의 두 전제가 충족되므로 일양연속입니다. $\delta$를 직접 구성할 필요가 없습니다.

> **문제 2.** (표준) 증명에서 $y_{n_k}\to x_0$을 확인하는 단계가 왜 필요한지 말하십시오.
> **답.** 두 수열이 같은 점으로 모여야 연속에서 두 함숫값이 같은 값으로 수렴하기 때문입니다.
> **풀이.** 모순을 만들려면 $\lvert f(x_{n_k})-f(y_{n_k})\rvert$이 $0$으로 가야 합니다. 그러려면 두 함숫값이 같은 극한을 가져야 하고, 그 근거는 두 정의역 수열이 같은 점 $x_0$으로 수렴한다는 사실입니다. $\lvert x_n-y_n\rvert\to0$ 조건이 이 단계에서 쓰입니다.

> **문제 3.** (심화) $f$가 $(0,1]$에서 연속이고 $\lim_{x\to0^+}f(x)$가 존재하면 $f$가 $(0,1]$에서 일양연속임을 보이십시오.
> **답.** $f(0)$을 그 극한값으로 정의해 $[0,1]$로 확장하고 하이네-칸토어 정리를 적용합니다.
> **풀이.** $L=\lim_{x\to0^+}f(x)$라 하고 $g:[0,1]\to\mathbb{R}$를 $g(0)=L$, $x>0$에서 $g(x)=f(x)$로 정의합니다. 극한이 $L$이므로 $g$는 $0$에서 연속이고 나머지 점에서는 $f$와 같아 연속입니다. 하이네-칸토어 정리에 의해 $g$는 $[0,1]$에서 일양연속이고, 부분집합 $(0,1]$로 제한해도 조건이 유지되므로 $f$는 일양연속입니다. $\square$

### 2.5 립시츠 조건

$\delta$를 구성하는 가장 편한 충분조건이 립시츠 조건입니다.

**정의.** 어떤 상수 $L\ge0$이 있어 모든 $x,y\in D$에서

$$
\lvert f(x)-f(y)\rvert\le L\lvert x-y\rvert
$$

이면 $f$를 $D$에서 립시츠 함수라 하고 $L$을 립시츠 상수라고 합니다.

**정리.** 립시츠 함수는 일양연속입니다.

증명은 한 줄입니다. $L=0$이면 $f$가 상수이므로 자명합니다. $L>0$일 때 $\varepsilon>0$에 대해 $\delta=\varepsilon/L$로 잡으면 $\lvert x-y\rvert<\delta$일 때 $\lvert f(x)-f(y)\rvert\le L\lvert x-y\rvert<L\cdot\varepsilon/L=\varepsilon$입니다. 이 $\delta$가 점에 의존하지 않으므로 일양연속입니다. $\square$

역은 성립하지 않습니다. $f(x)=\sqrt{x}$는 $[0,1]$에서 일양연속이지만 립시츠가 아닙니다. 립시츠라면 어떤 $L$에 대해 $\sqrt{x}=\lvert\sqrt{x}-\sqrt{0}\rvert\le L\lvert x-0\rvert=Lx$이므로 $x>0$에서 $\dfrac1{\sqrt{x}}\le L$이어야 합니다. $x\to0^+$에서 좌변이 무한히 커지므로 그런 $L$은 없습니다.

세 개념의 관계는 다음 포함관계로 정리됩니다.

$$
\text{립시츠}\ \Rightarrow\ \text{일양연속}\ \Rightarrow\ \text{연속}
$$

두 함의는 모두 역이 거짓입니다. 첫 화살표의 반례가 $\sqrt{x}$이고, 둘째 화살표의 반례가 $(0,1]$에서의 $1/x$입니다.

도함수와의 연결도 유용합니다. $f$가 구간에서 미분가능하고 $\lvert f'\rvert\le L$로 유계이면 평균값 정리에 의해 $\lvert f(x)-f(y)\rvert=\lvert f'(\xi)\rvert\lvert x-y\rvert\le L\lvert x-y\rvert$이므로 립시츠이고 따라서 일양연속입니다. 이 판정은 [11. 미분의 정의와 평균값 정리](../../05. 미분과 적분의 엄밀화/11. 미분의 정의와 평균값 정리/index.md)의 평균값 정리를 씁니다.

> **문제 1.** (기초) $f(x)=5x+2$의 립시츠 상수를 구하십시오.
> **답.** $L=5$입니다.
> **풀이.** $\lvert f(x)-f(y)\rvert=\lvert 5x-5y\rvert=5\lvert x-y\rvert$입니다. 등호가 성립하므로 $L=5$가 최소 립시츠 상수입니다.

> **문제 2.** (표준) $f(x)=x^2$이 $[0,3]$에서 립시츠임을 보이고 상수를 구하십시오.
> **답.** $L=6$입니다.
> **풀이.** $\lvert x^2-y^2\rvert=\lvert x+y\rvert\lvert x-y\rvert$이고 $x,y\in[0,3]$에서 $\lvert x+y\rvert\le6$이므로 $\lvert x^2-y^2\rvert\le6\lvert x-y\rvert$입니다. 또는 $f'(x)=2x$가 $[0,3]$에서 $\lvert f'\rvert\le6$이므로 평균값 정리로 같은 결론을 얻습니다. $\square$

> **문제 3.** (심화) $\sqrt{x}$가 $[1,4]$에서는 립시츠임을 보이십시오.
> **답.** $L=\dfrac12$입니다.
> **풀이.** $x,y\in[1,4]$에서 $\lvert\sqrt{x}-\sqrt{y}\rvert=\dfrac{\lvert x-y\rvert}{\sqrt{x}+\sqrt{y}}\le\dfrac{\lvert x-y\rvert}{2}$입니다. 분모가 $2$ 이상이기 때문입니다. $[0,1]$에서는 분모가 $0$에 접근해 이 논의가 깨집니다. 립시츠 여부가 정의역에 달려 있음을 보여 줍니다. $\square$

### 2.6 코시 수열의 보존과 확장 정리

일양연속이 연속보다 강한 성질임을 드러내는 대표 명제입니다.

**정리(코시 수열 보존).** $f$가 $D$에서 일양연속이고 $(x_n)$이 $D$ 안의 코시 수열이면 $(f(x_n))$도 코시 수열입니다.

증명을 봅니다. $\varepsilon>0$이 주어졌다고 합니다. 일양연속에서 $\delta>0$을 얻어 $\lvert x-y\rvert<\delta$이면 $\lvert f(x)-f(y)\rvert<\varepsilon$이 되게 합니다. $(x_n)$이 코시이므로 이 $\delta$에 대해 어떤 $N$이 있어 $m,n\ge N$이면 $\lvert x_n-x_m\rvert<\delta$입니다. 그러면 $m,n\ge N$에서 $\lvert f(x_n)-f(x_m)\rvert<\varepsilon$입니다. 따라서 $(f(x_n))$은 코시 수열입니다. $\square$

증명에서 $\delta$가 점에 의존하지 않는다는 사실이 결정적입니다. 연속만 가정하면 각 $x_n$마다 다른 $\delta$가 나오므로 $N$을 하나로 정할 수 없습니다. 실제로 이 성질은 연속에서 깨집니다. $(0,1]$에서 $f(x)=1/x$는 연속이고 $x_n=1/n$은 코시 수열이지만 $f(x_n)=n$은 코시가 아닙니다. 이 관찰은 $1/x$가 $(0,1]$에서 일양연속이 아님을 다시 증명하는 또 다른 경로이기도 합니다.

이 정리에서 확장 정리가 따라 나옵니다.

**정리(연속 확장, 개관).** $f$가 $D$에서 일양연속이면 $f$는 $D$의 폐포 $\overline{D}$ 전체로 일양연속하게 유일하게 확장됩니다.

증명 방침만 적습니다. $c\in\overline{D}\setminus D$를 택하면 $c$로 수렴하는 $D$ 안의 수열 $(x_n)$이 있고 이는 코시입니다. 위 정리에 의해 $(f(x_n))$이 코시이므로 실수의 완비성에 의해 극한이 존재하고 그 값을 $\tilde f(c)$로 정의합니다. $c$로 가는 다른 수열 $(y_n)$을 잡아도 $\lvert x_n-y_n\rvert\to0$이므로 일양연속에서 $\lvert f(x_n)-f(y_n)\rvert\to0$이고 두 극한이 일치하므로 정의가 잘 세워집니다. 확장된 $\tilde f$가 $\overline{D}$에서 일양연속임은 $\varepsilon$을 $\varepsilon/3$으로 쪼개는 표준 논의로 확인합니다.

이 정리는 $D=(0,1]$일 때 2.4의 문제 3과 정확히 같은 내용을 말합니다. 일양연속인 함수는 경계에서 값이 결정되므로 구멍을 메울 수 있고, 연속이지만 일양연속이 아닌 $1/x$나 $\sin(1/x)$는 경계에서 값이 결정되지 않아 확장할 수 없습니다.

> **문제 1.** (표준) $f(x)=\sin\dfrac1x$가 $(0,1]$에서 일양연속이 아님을 코시 수열 보존으로 다시 보이십시오.
> **답.** 코시 수열을 코시가 아닌 수열로 보내는 예를 만들면 됩니다.
> **풀이.** $z_{2k}=\dfrac1{2k\pi}$, $z_{2k+1}=\dfrac{1}{2k\pi+\pi/2}$로 섞은 수열 $(z_n)$은 $0$으로 수렴하므로 코시입니다. 그런데 $f(z_n)$은 $0$과 $1$을 번갈아 취하므로 코시가 아닙니다. 일양연속이면 코시가 보존되어야 하므로 $f$는 일양연속이 아닙니다. $\square$

> **문제 2.** (표준) $f(x)=\dfrac{\sin x}{x}$가 $(0,1]$에서 일양연속인지 판정하십시오.
> **답.** 일양연속입니다.
> **풀이.** $\lim_{x\to0^+}\dfrac{\sin x}{x}=1$이 존재하므로 $f(0)=1$로 확장하면 $[0,1]$에서 연속입니다. 하이네-칸토어 정리에 의해 확장 함수가 일양연속이고, 제한도 일양연속입니다. $\square$

> **문제 3.** (심화) 코시 수열 보존이 연속만으로는 성립하지 않는 이유를 $\delta$의 의존성으로 설명하십시오.
> **답.** 각 점마다 $\delta$가 달라지면 코시 조건에서 쓸 $N$을 하나로 고정할 수 없기 때문입니다.
> **풀이.** 증명은 하나의 $\delta$를 코시 조건에 넘겨 $N$을 얻는 구조입니다. 연속만 가정하면 $\delta=\delta(\varepsilon,x_n)$이 첨자마다 달라지고 그 값들의 하한이 $0$일 수 있으므로 모든 큰 $m,n$을 동시에 처리하는 $N$이 존재하지 않습니다. $(0,1]$에서 $1/x$와 $x_n=1/n$이 실제 반례입니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 문장 | 요령 |
|---|---|---|
| 연속 | $\forall c\ \forall\varepsilon\ \exists\delta$ | $\delta=\delta(\varepsilon,c)$, 점마다 다시 고른다 |
| 일양연속 | $\forall\varepsilon\ \exists\delta\ \forall x,y$ | $\delta=\delta(\varepsilon)$, 전 구간 공통 |
| 부정 | $\exists\varepsilon_0\ \forall\delta\ \exists x,y$ | 두 수열로 바꿔 쓴다 |
| 두 수열 판정 | $\lvert x_n-y_n\rvert\to0$, $\lvert f(x_n)-f(y_n)\rvert\ge\varepsilon_0$ | 기울기 폭발점 또는 진동 압축점에서 잡는다 |
| $1/x$ on $(0,1]$ | $x_n=1/n$, $y_n=1/(2n)$ | 왼쪽 끝이 빠져 기울기가 폭발한다 |
| $x^2$ on $\mathbb{R}$ | $x_n=n+1/n$, $y_n=n$ | 비유계라 기울기가 폭발한다 |
| $\sin(1/x)$ on $(0,1]$ | $x_n=1/(2n\pi)$, $y_n=1/(2n\pi+\pi/2)$ | 유계인데도 진동이 압축된다 |
| 하이네-칸토어 | 연속 $+$ $[a,b]$ $\Rightarrow$ 일양연속 | 두 수열 $+$ BW $+$ 연속으로 모순 |
| 립시츠 | $\lvert f(x)-f(y)\rvert\le L\lvert x-y\rvert$ | $\delta=\varepsilon/L$, 역은 거짓($\sqrt{x}$) |
| 도함수 판정 | $\lvert f'\rvert\le L$ | 평균값 정리로 립시츠, 따라서 일양연속 |
| 코시 보존 | 일양연속은 코시를 코시로 보낸다 | 하나의 $\delta$를 코시 조건에 넘긴다 |
| 확장 정리 | 일양연속이면 폐포로 확장된다 | 경계에서 극한이 존재하는지로 판정한다 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $f(x)=-4x+7$이 $\mathbb{R}$에서 일양연속임을 보이십시오.
> **답.** $\delta=\varepsilon/4$로 잡으면 됩니다.
> **풀이.** $\lvert f(x)-f(y)\rvert=4\lvert x-y\rvert$입니다. $\delta=\varepsilon/4$이면 $\lvert x-y\rvert<\delta$일 때 값 차이가 $\varepsilon$ 미만이고 이 $\delta$는 점에 의존하지 않습니다. $\square$

> **문제 2.** (기초) $f(x)=\dfrac1x$가 $[1,\infty)$에서 일양연속인지 판정하십시오.
> **답.** 일양연속입니다.
> **풀이.** $x,y\ge1$에서 $\left\lvert\dfrac1x-\dfrac1y\right\rvert=\dfrac{\lvert x-y\rvert}{xy}\le\lvert x-y\rvert$입니다. 분모가 $1$ 이상이기 때문입니다. 따라서 립시츠 상수 $1$의 립시츠 함수이고 $\delta=\varepsilon$으로 잡으면 됩니다. 문제가 되는 것은 $0$ 근처이며 그 부분이 정의역에서 빠졌습니다. $\square$

> **문제 3.** (표준) $f(x)=x^3$이 $\mathbb{R}$에서 일양연속이 아님을 두 수열로 보이십시오.
> **답.** $x_n=n+\dfrac{1}{n^2}$, $y_n=n$을 잡으면 됩니다.
> **풀이.** $\lvert x_n-y_n\rvert=\dfrac1{n^2}\to0$입니다. 한편 $x_n^3-y_n^3=(x_n-y_n)(x_n^2+x_ny_n+y_n^2)\ge\dfrac1{n^2}\cdot3n^2=3$이므로 $\varepsilon_0=3$에 대해 조건이 모든 $n$에서 성립합니다. 따라서 일양연속이 아닙니다. $\square$

> **문제 4.** (표준) $f$와 $g$가 $D$에서 일양연속이면 $f+g$도 일양연속임을 보이십시오.
> **답.** 두 $\delta$의 최소값을 잡으면 됩니다.
> **풀이.** $\varepsilon>0$에 대해 $\lvert f(x)-f(y)\rvert<\varepsilon/2$가 되는 $\delta_1$과 $\lvert g(x)-g(y)\rvert<\varepsilon/2$가 되는 $\delta_2$를 얻습니다. $\delta=\min\{\delta_1,\delta_2\}$로 잡으면 삼각부등식에서 $\lvert(f+g)(x)-(f+g)(y)\rvert<\varepsilon$입니다. 두 $\delta$가 모두 점에 의존하지 않으므로 최소값도 그렇습니다. $\square$

> **문제 5.** (표준) $f(x)=x^2$과 $g(x)=x$가 $\mathbb{R}$에서 일양연속인지 각각 판정하고 곱의 일양연속이 보존되지 않음을 확인하십시오.
> **답.** $g$는 일양연속이지만 $g\cdot g=f$는 일양연속이 아닙니다.
> **풀이.** $g(x)=x$는 $\lvert g(x)-g(y)\rvert=\lvert x-y\rvert$이므로 $\delta=\varepsilon$으로 일양연속입니다. 그런데 2.3에서 $x^2$은 $\mathbb{R}$에서 일양연속이 아님을 보았습니다. 따라서 일양연속은 합에서는 보존되지만 곱에서는 보존되지 않습니다. 정의역이 유계이면 곱도 보존됩니다. $\square$

> **문제 6.** (심화) $f$가 $\mathbb{R}$에서 일양연속이면 어떤 상수 $A,B$가 있어 $\lvert f(x)\rvert\le A\lvert x\rvert+B$임을 보이십시오.
> **답.** $\varepsilon=1$에 대응하는 $\delta$로 구간을 쪼개 계단식으로 누적하면 됩니다.
> **풀이.** $\varepsilon=1$에 대응하는 $\delta>0$을 얻습니다. 임의의 $x>0$에 대해 $n=\lfloor x/\delta\rfloor+1$이라 하면 $x/n<\delta$이므로 $0$에서 $x$까지를 길이 $\delta$ 미만의 구간 $n$개로 나눕니다. 인접한 분점마다 함숫값 차이가 $1$ 미만이므로 $\lvert f(x)-f(0)\rvert<n\le\dfrac{x}{\delta}+1$입니다. 따라서 $\lvert f(x)\rvert\le\dfrac{1}{\delta}\lvert x\rvert+1+\lvert f(0)\rvert$이고 $x<0$도 같습니다. $A=1/\delta$, $B=1+\lvert f(0)\rvert$입니다. $\square$

> **문제 7.** (심화) 문제 6을 이용해 $f(x)=x^2$이 $\mathbb{R}$에서 일양연속이 아님을 다시 보이십시오.
> **답.** $x^2$은 어떤 일차식으로도 위에서 눌릴 수 없기 때문입니다.
> **풀이.** 일양연속이면 문제 6에 의해 $x^2\le A\lvert x\rvert+B$가 모든 $x$에서 성립해야 합니다. 양변을 $\lvert x\rvert$로 나누면 $x>0$에서 $x\le A+B/x$입니다. $x\to\infty$에서 좌변은 무한히 커지고 우변은 $A$에 수렴하므로 부등식이 깨집니다. 따라서 일양연속이 아닙니다. $\square$

## 5. 스스로 점검

1. 연속과 일양연속의 정의를 나란히 쓰고 한정기호 순서의 차이를 지적할 수 있는가?
2. 일양연속의 부정을 쓰고 두 수열 판정으로 옮길 수 있는가?
3. $1/x$, $x^2$, $\sin(1/x)$의 반례 수열을 각각 제시하고 원인을 구분할 수 있는가?
4. 하이네-칸토어 정리를 볼차노-바이어슈트라스 정리로 증명할 수 있는가?
5. 증명에서 두 수열이 같은 점으로 수렴함을 왜 확인해야 하는지 말할 수 있는가?
6. 립시츠 조건이 일양연속을 함의하고 역이 거짓임을 예로 보일 수 있는가?
7. 일양연속이 코시 수열을 보존함을 증명하고 연속에서 깨지는 예를 들 수 있는가?
8. 확장 정리의 진술과 증명 방침을 요약할 수 있는가?

**정답 요지.** 1. 연속은 $\forall c\forall\varepsilon\exists\delta$, 일양연속은 $\forall\varepsilon\exists\delta\forall x,y$이며 $\delta$의 점 의존성만 다릅니다. 2. $\exists\varepsilon_0\forall\delta\exists x,y$로 부정하고 $\delta=1/n$을 대입해 두 수열을 얻습니다. 3. $1/n$과 $1/(2n)$, $n+1/n$과 $n$, $1/(2n\pi)$와 $1/(2n\pi+\pi/2)$이며 원인은 왼쪽 끝 기울기 폭발, 비유계 기울기 폭발, 진동 압축입니다. 4. 반례 수열에 BW를 적용해 부분수열의 극한을 잡고 연속으로 두 함숫값을 모아 모순을 만듭니다. 5. 그래야 두 함숫값이 같은 극한을 가지며 차이가 $0$으로 수렴합니다. 6. $\delta=\varepsilon/L$로 함의하고, $\sqrt{x}$가 $[0,1]$에서 반례입니다. 7. 하나의 $\delta$를 코시 조건에 넘기면 되고, $(0,1]$의 $1/x$와 $x_n=1/n$이 연속에서 깨지는 예입니다. 8. 일양연속이면 폐포로 유일하게 일양연속 확장되고, 코시 보존과 완비성으로 경계값을 정의합니다.
