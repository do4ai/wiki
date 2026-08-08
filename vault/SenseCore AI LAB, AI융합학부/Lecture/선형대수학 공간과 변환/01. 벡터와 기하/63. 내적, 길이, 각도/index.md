---
title: "63. 내적, 길이, 각도"
---
# 63강. 내적, 길이, 각도

62강에서 벡터 하나의 길이를 쟀습니다. 그런데 **두 벡터 사이의 관계**는 아직 다루지 못했습니다.

$(1,0)$과 $(0,1)$은 수직이고 $(1,0)$과 $(2,0)$은 같은 방향입니다. 눈으로는 보이는데, 성분만 보고 그것을 판정하는 방법이 없습니다. 차원이 높아지면 눈으로 볼 수도 없습니다.

두 벡터의 관계를 재는 하나의 수가 필요합니다. 그것이 **내적**이며, 정의는 놀랄 만큼 단순합니다.

$$\mathbf{u}\cdot\mathbf{v}=u_{1}v_{1}+u_{2}v_{2}+\cdots+u_{n}v_{n}$$

성분끼리 곱해 더한 것뿐입니다. 그런데 이 하나의 수에서 **길이와 각도가 모두 나옵니다.** 62강의 노름이 $\sqrt{\mathbf{v}\cdot\mathbf{v}}$이고, 두 벡터가 이루는 각의 코사인이 내적을 길이의 곱으로 나눈 값입니다.

**기하가 대수로 옮겨진 것**이 이 강의의 사건입니다. 각도와 수직이 그림 없이 계산되므로 차원이 아무리 높아도 다룰 수 있습니다. 64강의 정사영, 80강의 그람슈미트, 82강의 최소제곱이 모두 이 하나의 연산 위에 세워집니다.

## 이 강의에서 할 수 있게 되는 것
- 코사인 법칙에서 내적을 유도할 수 있습니다.
- 내적의 세 가지 성질을 확인하고 계산에 쓸 수 있습니다.
- 두 벡터가 이루는 각을 계산하고 그 정의가 정당한 근거를 댈 수 있습니다.
- 직교를 판정하고 피타고라스 정리를 벡터로 쓸 수 있습니다.
- 내적이 유사도와 상관계수로 나타나는 방식을 설명할 수 있습니다.

## 문제 1. 두 벡터의 각도를 성분으로 어떻게 아는가

> **문제.** 두 벡터 $\mathbf{u}$, $\mathbf{v}$가 이루는 각을 $\theta$라 합니다.
> (1) 두 벡터의 끝점과 원점이 만드는 삼각형에 코사인 법칙을 적용하세요.
> (2) $\lVert\mathbf{u}-\mathbf{v}\rVert^{2}$을 성분으로 전개하세요.
> (3) 두 결과를 비교해 $\cos\theta$를 성분으로 나타내세요.

**생각의 실마리.** (1)은 16강의 코사인 법칙입니다. 세 변의 길이가 $\lVert\mathbf{u}\rVert$, $\lVert\mathbf{v}\rVert$, $\lVert\mathbf{u}-\mathbf{v}\rVert$인 삼각형입니다. (2)는 62강의 노름 정의를 그대로 전개하면 됩니다. **두 표현이 같은 양을 나타내므로 비교하면 $\cos\theta$가 성분으로 표현됩니다.**

**풀이.** (1) $\mathbf{u}$와 $\mathbf{v}$ 사이의 각이 $\theta$이고 마주 보는 변이 $\mathbf{u}-\mathbf{v}$이므로

$$\lVert\mathbf{u}-\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}-2\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$$

입니다.

(2) 성분으로 전개합니다.

$$\lVert\mathbf{u}-\mathbf{v}\rVert^{2}=\sum_{k}(u_{k}-v_{k})^{2}=\sum u_{k}^{2}-2\sum u_{k}v_{k}+\sum v_{k}^{2}=\lVert\mathbf{u}\rVert^{2}-2\sum u_{k}v_{k}+\lVert\mathbf{v}\rVert^{2}$$

(3) 두 식의 오른쪽을 비교하면 $\lVert\mathbf{u}\rVert^{2}$과 $\lVert\mathbf{v}\rVert^{2}$이 상쇄되고

$$\sum_{k}u_{k}v_{k}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$$

가 남습니다. 따라서

$$\cos\theta=\frac{\sum u_{k}v_{k}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$$

입니다.

**이 문제에서 배우는 것: 내적.**

> **내적(점곱).**
> $$\mathbf{u}\cdot\mathbf{v}=\sum_{k=1}^{n}u_{k}v_{k}$$
> 로 정의합니다. $\langle\mathbf{u},\mathbf{v}\rangle$로도 씁니다.

문제 1이 보인 것은 이 정의가 **기하와 이어진다**는 사실입니다.

$$\mathbf{u}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$$

이 등식이 이 강의의 중심입니다. 왼쪽은 성분만 알면 계산되고 오른쪽은 기하적 뜻을 담고 있습니다. **두 세계를 잇는 다리입니다.**

여기서 여러 사실이 따라옵니다.

| 관계 | 내적의 부호 | 각도 |
|---|---|---|
| 같은 쪽을 향함 | 양수 | $\theta<90^{\circ}$ |
| 수직 | $0$ | $\theta=90^{\circ}$ |
| 반대쪽을 향함 | 음수 | $\theta>90^{\circ}$ |

**내적의 부호만 봐도 두 벡터가 대략 같은 방향인지 알 수 있습니다.** 이 단순한 판정이 219강 이후 경사하강법에서 "이 방향으로 가면 손실이 줄어드는가"를 판단하는 기준이 됩니다.

노름과의 관계도 즉시 나옵니다. $\mathbf{v}$와 자기 자신의 내적을 보면 $\theta=0$이므로

$$\mathbf{v}\cdot\mathbf{v}=\lVert\mathbf{v}\rVert^{2}$$

입니다. **62강에서 따로 정의한 노름이 내적에서 나옵니다.** 그래서 이제부터 노름을 $\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}$로 정의해도 됩니다.

**바로 확인 1.**

**확인 1-1.** $(3,-1,2)\cdot(-1,4,5)$를 계산하세요.

*답.* $-3-4+10=3$입니다.

**확인 1-2.** $\mathbf{v}\cdot\mathbf{v}$가 무엇인지 쓰세요.

*답.* $\lVert\mathbf{v}\rVert^{2}$입니다.

**확인 1-3.** 내적이 음수이면 두 벡터의 각도에 대해 무엇을 알 수 있습니까?

*답.* $90^{\circ}$보다 큽니다. 대략 반대쪽을 향합니다.

## 문제 2. 내적은 어떤 규칙을 따르는가

> **문제.** 다음을 확인하세요.
> (1) $\mathbf{u}\cdot\mathbf{v}=\mathbf{v}\cdot\mathbf{u}$
> (2) $(a\mathbf{u}+b\mathbf{w})\cdot\mathbf{v}=a(\mathbf{u}\cdot\mathbf{v})+b(\mathbf{w}\cdot\mathbf{v})$
> (3) $\mathbf{v}\cdot\mathbf{v}\ge 0$이고 등호는 언제입니까?

**생각의 실마리.** 세 성질 모두 정의에 넣고 실수의 성질을 인용하면 됩니다. **62강에서 벡터공간 공리를 확인할 때와 같은 방식**입니다. (3)에서는 제곱의 합이 언제 $0$이 되는지 생각합니다.

**풀이.** (1) $\sum u_{k}v_{k}=\sum v_{k}u_{k}$인데 실수의 곱이 교환법칙을 만족하기 때문입니다.

(2) 성분으로 쓰면

$$\sum_{k}(au_{k}+bw_{k})v_{k}=a\sum u_{k}v_{k}+b\sum w_{k}v_{k}$$

입니다. 실수의 분배법칙과 합의 선형성(31강)입니다.

(3) $\mathbf{v}\cdot\mathbf{v}=\sum v_{k}^{2}$이고 제곱은 음이 아니므로 합도 음이 아닙니다. 합이 $0$이려면 **모든 항이 $0$**이어야 하므로 $\mathbf{v}=\mathbf{0}$일 때만입니다.

**이 문제에서 배우는 것: 내적의 세 가지 성질.**

> **내적의 성질.**
>
> | 이름 | 식 |
> |---|---|
> | 대칭성 | $\mathbf{u}\cdot\mathbf{v}=\mathbf{v}\cdot\mathbf{u}$ |
> | 선형성 | $(a\mathbf{u}+b\mathbf{w})\cdot\mathbf{v}=a(\mathbf{u}\cdot\mathbf{v})+b(\mathbf{w}\cdot\mathbf{v})$ |
> | 양의 정부호 | $\mathbf{v}\cdot\mathbf{v}\ge 0$이고 $=0$은 $\mathbf{v}=\mathbf{0}$일 때만 |

**이 셋이 내적의 정의로 격상됩니다.** 79강에서 일반적인 벡터공간에 내적을 도입할 때, 성분 공식이 아니라 이 세 성질을 만족하는 연산이면 무엇이든 내적이라 부릅니다. 심화 2에서 미리 봅니다.

대칭성과 선형성을 합치면 **두 번째 자리에서도 선형**임이 따라옵니다.

$$\mathbf{u}\cdot(a\mathbf{v}+b\mathbf{w})=a(\mathbf{u}\cdot\mathbf{v})+b(\mathbf{u}\cdot\mathbf{w})$$

양쪽 모두에서 선형인 연산을 **쌍선형**이라 합니다. 이 성질 덕분에 내적을 다항식처럼 전개할 수 있습니다.

$$(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}+\mathbf{v})=\mathbf{u}\cdot\mathbf{u}+2\,\mathbf{u}\cdot\mathbf{v}+\mathbf{v}\cdot\mathbf{v}$$

즉

$$\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+2\,\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^{2}$$

입니다. **이 전개가 이 과목에서 가장 자주 쓰는 계산**이며, 62강의 평행사변형 법칙과 문제 4의 피타고라스 정리가 모두 여기서 나옵니다.

양의 정부호 조건이 왜 필요한지도 짚어 둡니다. 이 조건이 있어야 $\sqrt{\mathbf{v}\cdot\mathbf{v}}$가 노름이 되고, 노름이 있어야 거리와 수렴을 말할 수 있습니다. **세 성질 중 하나라도 빠지면 기하가 무너집니다.**

**바로 확인 2.**

**확인 2-1.** $\lVert\mathbf{u}-\mathbf{v}\rVert^{2}$을 내적으로 전개하세요.

*답.* $\lVert\mathbf{u}\rVert^{2}-2\,\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^{2}$입니다.

**확인 2-2.** 내적이 쌍선형이라는 말의 뜻을 쓰세요.

*답.* 첫째 자리와 둘째 자리 모두에서 선형이라는 뜻입니다.

**확인 2-3.** $\mathbf{v}\cdot\mathbf{v}=0$이면 무엇을 알 수 있습니까?

*답.* $\mathbf{v}=\mathbf{0}$입니다. 제곱의 합이 $0$이려면 모든 성분이 $0$이어야 하기 때문입니다.

## 문제 3. 각도를 정의해도 되는가

> **문제.** $\cos\theta=\dfrac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$로 각도를 정의하려 합니다.
> (1) 이 정의가 성립하려면 오른쪽이 어떤 범위에 있어야 합니까?
> (2) 실제로 그 범위에 있음을 보이세요.
> (3) $(3,-1,2)$와 $(-1,4,5)$가 이루는 각을 구하세요.

**생각의 실마리.** $\cos$의 치역이 $[-1,1]$이므로 오른쪽이 그 범위를 벗어나면 $\theta$가 존재하지 않습니다. **차원이 높아지면 "각도"를 그림으로 확인할 수 없으므로 대수적으로 보장해야 합니다.** 62강 심화 2에서 증명한 부등식이 정확히 그 일을 합니다.

**풀이.** (1) $\cos\theta\in[-1,1]$이어야 하므로

$$-1\le\frac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}\le 1$$

즉 $\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$여야 합니다.

(2) 이것이 **코시-슈바르츠 부등식**이며 62강 심화 2에서 증명했습니다. 판별식을 쓴 증명을 내적의 언어로 다시 적으면 이렇습니다. 임의의 실수 $t$에 대해

$$0\le\lVert t\mathbf{u}+\mathbf{v}\rVert^{2}=(\mathbf{u}\cdot\mathbf{u})t^{2}+2(\mathbf{u}\cdot\mathbf{v})t+(\mathbf{v}\cdot\mathbf{v})$$

이고 이차식이 언제나 음이 아니므로 판별식이 $0$ 이하입니다.

$$(\mathbf{u}\cdot\mathbf{v})^{2}\le(\mathbf{u}\cdot\mathbf{u})(\mathbf{v}\cdot\mathbf{v})=\lVert\mathbf{u}\rVert^{2}\lVert\mathbf{v}\rVert^{2}$$

**증명에 성분이 한 번도 나오지 않았습니다.** 문제 2의 세 성질만 썼으므로, 79강의 일반 내적공간에서도 그대로 성립합니다.

(3) $\mathbf{u}\cdot\mathbf{v}=3$이고 $\lVert\mathbf{u}\rVert=\sqrt{14}$, $\lVert\mathbf{v}\rVert=\sqrt{42}$입니다.

$$\cos\theta=\frac{3}{\sqrt{14}\sqrt{42}}=\frac{3}{\sqrt{588}}\approx 0.1237$$

이므로 $\theta\approx 82.89^{\circ}$입니다.

**이 문제에서 배우는 것: 코시-슈바르츠가 각도를 가능하게 합니다.**

> **코시-슈바르츠 부등식.**
> $$\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$$
> 등호는 두 벡터가 평행할 때만 성립합니다.

> **각도의 정의.** $\mathbf{u},\mathbf{v}\ne\mathbf{0}$일 때
> $$\theta=\arccos\frac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}\in[0,\pi]$$

**이차원이나 삼차원에서는 각도가 이미 있는 것이라 정의할 필요가 없어 보입니다.** 그런데 $\mathbb{R}^{100}$에서는 사정이 다릅니다. 그림을 그릴 수 없으므로 각도라는 개념 자체를 새로 만들어야 하고, 위의 식이 그 정의입니다.

정의가 정당한 이유는 두 가지입니다.

| 근거 | 내용 |
|---|---|
| 잘 정의됨 | 코시-슈바르츠로 값이 $[-1,1]$에 있습니다 |
| 일관됨 | 이차원·삼차원에서 원래 각도와 같습니다 |

두 번째는 문제 1의 유도가 보장합니다. 코사인 법칙에서 나왔으므로 낮은 차원에서는 우리가 아는 각도와 일치합니다.

특별한 값들을 확인해 둡니다.

| 상황 | $\cos\theta$ | $\theta$ |
|---|---|---|
| $\mathbf{v}=\mathbf{u}$ | $1$ | $0^{\circ}$ |
| $\mathbf{v}=-\mathbf{u}$ | $-1$ | $180^{\circ}$ |
| $\mathbf{u}\cdot\mathbf{v}=0$ | $0$ | $90^{\circ}$ |
| $(1,0)$과 $(1,1)$ | $\dfrac{1}{\sqrt2}$ | $45^{\circ}$ |

**바로 확인 3.**

**확인 3-1.** 코시-슈바르츠 부등식을 쓰고 등호 조건을 말하세요.

*답.* $\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$이며 두 벡터가 평행할 때만 등호입니다.

**확인 3-2.** $(1,0)$과 $(1,1)$이 이루는 각을 구하세요.

*답.* $\cos\theta=\dfrac{1}{\sqrt2}$이므로 $45^{\circ}$입니다.

**확인 3-3.** 고차원에서 각도를 정의할 때 코시-슈바르츠가 필요한 이유를 쓰세요.

*답.* $\arccos$에 넣을 값이 $[-1,1]$ 안에 있음을 보장해야 정의가 성립하기 때문입니다.

## 문제 4. 수직을 어떻게 판정하는가

> **문제.** 다음을 조사합니다.
> (1) $(1,2,3)$과 $(2,-1,0)$이 수직인지 판정하세요.
> (2) 두 벡터가 수직일 때 $\lVert\mathbf{u}+\mathbf{v}\rVert^{2}$을 계산하세요.
> (3) 수직이 아닌 경우와 비교하세요.

**생각의 실마리.** (1)은 내적이 $0$인지 보면 됩니다. (2)는 문제 2에서 얻은 전개식에 $\mathbf{u}\cdot\mathbf{v}=0$을 넣습니다. **교차항이 사라지는 것이 핵심**이며, 그 결과가 익숙한 정리가 됩니다.

**풀이.** (1) 내적을 계산합니다.

$$1\cdot 2+2\cdot(-1)+3\cdot 0=2-2+0=0$$

**수직입니다.**

(2) 문제 2의 전개식에서 교차항이 사라집니다.

$$\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+2\,\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}$$

**피타고라스 정리입니다.**

(3) 수직이 아니면 교차항이 남습니다. 검산에서 $\mathbf{u}=(3,-1,2)$, $\mathbf{v}=(-1,4,5)$일 때 $\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=62$이고 $\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}=56$입니다. **차이 $6$이 정확히 $2\,\mathbf{u}\cdot\mathbf{v}=2\cdot 3$입니다.**

**이 문제에서 배우는 것: 직교.**

> **직교.** $\mathbf{u}\cdot\mathbf{v}=0$이면 두 벡터가 **직교**한다고 하고 $\mathbf{u}\perp\mathbf{v}$로 씁니다.

> **피타고라스 정리.** $\mathbf{u}\perp\mathbf{v}$이면 $\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}$입니다.

**"수직"이라는 기하적 개념이 "내적이 $0$"이라는 대수적 조건이 되었습니다.** 이것이 이 강의의 가장 실용적인 성과입니다. 그림 없이 판정할 수 있으므로 차원이 아무리 높아도 다룰 수 있습니다.

몇 가지 규약도 정해 둡니다.

| 상황 | 규약 |
|---|---|
| $\mathbf{0}$과 임의의 벡터 | 직교한다고 봅니다 |
| 직교하는 벡터들의 모임 | 직교집합 |
| 직교하고 모두 단위벡터 | 정규직교집합 |

첫 줄이 편리한 규약입니다. $\mathbf{0}\cdot\mathbf{v}=0$이므로 정의상 직교이고, 그렇게 두면 예외 처리가 줄어듭니다. 다만 영벡터에는 방향이 없으므로 각도는 정의되지 않습니다.

표준기저가 정규직교집합의 대표적인 예입니다.

$$\mathbf{e}_{i}\cdot\mathbf{e}_{j}=\begin{cases}1 & (i=j)\\ 0 & (i\ne j)\end{cases}$$

**59강에서 본 직교성과 같은 모양**입니다. 그때는 $\{e^{inx}\}$가 함수 공간에서 직교했는데, 여기서는 $\{\mathbf{e}_{k}\}$가 $\mathbb{R}^{n}$에서 직교합니다. 심화 3에서 두 상황이 같은 구조임을 확인합니다.

피타고라스 정리는 항이 여럿일 때로 확장됩니다. $\mathbf{v}_{1},\dots,\mathbf{v}_{k}$가 서로 직교하면

$$\lVert\mathbf{v}_{1}+\cdots+\mathbf{v}_{k}\rVert^{2}=\lVert\mathbf{v}_{1}\rVert^{2}+\cdots+\lVert\mathbf{v}_{k}\rVert^{2}$$

입니다. 전개했을 때 교차항이 모두 $0$이기 때문입니다. **59강의 파스발 항등식이 정확히 이 정리의 무한판**이었습니다.

**바로 확인 4.**

**확인 4-1.** $(2,3)$과 $(3,-2)$가 직교하는지 판정하세요.

*답.* $6-6=0$이므로 직교합니다.

**확인 4-2.** 피타고라스 정리를 벡터로 쓰고 성립 조건을 말하세요.

*답.* $\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}$이며 $\mathbf{u}\perp\mathbf{v}$일 때 성립합니다.

**확인 4-3.** 표준기저가 정규직교집합인 이유를 쓰세요.

*답.* 서로 다른 것끼리 내적이 $0$이고 각각의 길이가 $1$이기 때문입니다.

## 문제 5. 내적은 어디에 쓰이는가

> **문제.** 다음 상황에서 내적이 무엇을 재는지 밝히세요.
> (1) 두 문서를 단어 빈도 벡터로 나타냈을 때
> (2) 두 자료의 상관계수
> (3) 힘과 이동으로 계산하는 일

**생각의 실마리.** 세 경우 모두 **"두 대상이 얼마나 같은 방향을 향하는가"**를 재고 있습니다. 다만 크기를 어떻게 처리하느냐가 다릅니다. (2)에서는 평균을 뺀 뒤 계산한다는 점이 핵심입니다.

**풀이.** (1) 문서의 길이가 다르면 빈도의 절대값이 달라지므로 크기를 빼고 방향만 비교합니다. 정규화한 뒤 내적을 취하는 것이 **코사인 유사도**입니다.

$$\operatorname{sim}(\mathbf{u},\mathbf{v})=\frac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}=\cos\theta$$

값이 $1$에 가까우면 비슷한 문서이고 $0$에 가까우면 무관합니다.

(2) 두 자료 $\mathbf{x}$, $\mathbf{y}$에서 각각 평균을 뺀 것을 $\tilde{\mathbf{x}}$, $\tilde{\mathbf{y}}$라 하면 상관계수는

$$r=\frac{\tilde{\mathbf{x}}\cdot\tilde{\mathbf{y}}}{\lVert\tilde{\mathbf{x}}\rVert\lVert\tilde{\mathbf{y}}\rVert}$$

입니다. **중심화한 벡터의 코사인 유사도가 곧 상관계수입니다.**

(3) 일정한 힘 $\mathbf{F}$가 작용하며 $\mathbf{d}$만큼 이동했을 때의 일은

$$W=\mathbf{F}\cdot\mathbf{d}=\lVert\mathbf{F}\rVert\lVert\mathbf{d}\rVert\cos\theta$$

입니다. **이동 방향 성분만 일을 합니다.** 힘이 이동에 수직이면 일이 $0$입니다.

**이 문제에서 배우는 것: 내적의 여러 얼굴.**

세 상황의 공통 구조를 표로 정리합니다.

| 상황 | $\mathbf{u}$ | $\mathbf{v}$ | 내적이 재는 것 |
|---|---|---|---|
| 문서 유사도 | 문서 A의 빈도 | 문서 B의 빈도 | 주제의 겹침 |
| 상관계수 | 중심화한 $x$ | 중심화한 $y$ | 함께 움직이는 정도 |
| 일 | 힘 | 이동 | 방향이 맞는 성분 |
| 경사하강법 | 그래디언트 | 이동 방향 | 손실의 감소량 |

**"두 대상이 얼마나 나란한가"**가 공통입니다.

(2)의 결과는 특히 값이 큽니다. **상관계수가 기하적으로 각도의 코사인**이므로 여러 성질이 즉시 따라옵니다.

| 상관계수의 성질 | 기하적 이유 |
|---|---|
| $-1\le r\le 1$ | 코시-슈바르츠 |
| $r=1$ | 두 벡터가 같은 방향 |
| $r=-1$ | 정반대 방향 |
| $r=0$ | 직교 |

$r$의 범위가 왜 $[-1,1]$인지가 코시-슈바르츠 하나로 설명됩니다. 129강 이후 통계에서 이 사실을 다시 만나는데, 그때는 기댓값의 언어로 같은 부등식이 나타납니다.

마지막 줄의 경사하강법도 짚어 둡니다. 106강에서 배우겠지만, 어느 방향으로 움직일 때 함수가 가장 빨리 줄어드는지를 묻는 문제의 답이 **그래디언트의 반대 방향**인데, 그 근거가 내적입니다. $\mathbf{g}\cdot\mathbf{d}$를 가장 작게 만드는 단위벡터 $\mathbf{d}$가 $-\hat{\mathbf{g}}$이며, 이는 코시-슈바르츠의 등호 조건입니다.

**바로 확인 5.**

**확인 5-1.** 코사인 유사도의 정의를 쓰세요.

*답.* $\dfrac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$이며 두 벡터가 이루는 각의 코사인입니다.

**확인 5-2.** 상관계수와 코사인 유사도의 차이를 쓰세요.

*답.* 상관계수는 각 벡터에서 평균을 뺀 뒤 코사인 유사도를 계산한 것입니다.

**확인 5-3.** 상관계수가 $[-1,1]$에 있는 이유를 쓰세요.

*답.* 코시-슈바르츠 부등식 때문입니다. 코사인 값이므로 그 범위를 벗어날 수 없습니다.

## 유형 총정리(치트시트)

| 개념 | 정의 |
|---|---|
| 내적 | $\mathbf{u}\cdot\mathbf{v}=\sum u_{k}v_{k}$ |
| 기하 표현 | $\mathbf{u}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$ |
| 노름 | $\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}$ |
| 각도 | $\theta=\arccos\dfrac{\mathbf{u}\cdot\mathbf{v}}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert}$ |
| 직교 | $\mathbf{u}\cdot\mathbf{v}=0$ |

| 성질 | 식 |
|---|---|
| 대칭성 | $\mathbf{u}\cdot\mathbf{v}=\mathbf{v}\cdot\mathbf{u}$ |
| 선형성 | $(a\mathbf{u}+b\mathbf{w})\cdot\mathbf{v}=a(\mathbf{u}\cdot\mathbf{v})+b(\mathbf{w}\cdot\mathbf{v})$ |
| 양의 정부호 | $\mathbf{v}\cdot\mathbf{v}\ge 0$, $=0\iff\mathbf{v}=\mathbf{0}$ |
| 전개 | $\lVert\mathbf{u}\pm\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}\pm 2\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^{2}$ |

| 부등식·정리 | 식 |
|---|---|
| 코시-슈바르츠 | $\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$ |
| 피타고라스 | $\mathbf{u}\perp\mathbf{v}\Rightarrow\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}$ |
| 삼각부등식 | 코시-슈바르츠에서 따라옵니다 |

| 쓰이는 곳 | 내적이 재는 것 |
|---|---|
| 코사인 유사도 | 방향의 겹침 |
| 상관계수 | 중심화한 뒤의 코사인 |
| 일 | 이동 방향 성분 |
| 경사하강 | 손실의 감소량 |

| 자주 하는 실수 | 바로잡기 |
|---|---|
| 내적의 결과를 벡터로 여깁니다 | 스칼라입니다 |
| $\mathbf{u}\cdot\mathbf{v}=0$을 $\mathbf{u}=\mathbf{0}$으로 읽습니다 | 직교라는 뜻입니다 |
| 정규화 없이 유사도를 비교합니다 | 크기 차이가 섞여 듭니다 |
| 상관계수를 정규화 없이 계산합니다 | 평균을 먼저 빼야 합니다 |

## 종합 문제 드릴

> **문제 6.** $(1,2,3)\cdot(4,-5,6)$을 계산하세요.

*답.* $4-10+18=12$입니다.

> **문제 7.** $(2,-1)\cdot(1,2)$를 계산하고 두 벡터의 관계를 말하세요.

*답.* $2-2=0$이므로 직교합니다.

> **문제 8.** $\lVert(3,4)\rVert$를 내적으로 계산하세요.

*답.* $\sqrt{(3,4)\cdot(3,4)}=\sqrt{25}=5$입니다.

> **문제 9.** $(1,1)$과 $(0,1)$이 이루는 각을 구하세요.

*답.* $\cos\theta=\dfrac{1}{\sqrt2}$이므로 $45^{\circ}$입니다.

> **문제 10.** $(1,0,0)$과 $(1,1,1)$이 이루는 각의 코사인을 구하세요.

*답.* $\dfrac{1}{\sqrt3}\approx 0.577$입니다.

> **문제 11.** $\mathbf{u}\cdot\mathbf{v}=-5$일 때 두 벡터의 각도에 대해 무엇을 알 수 있습니까?

*답.* $90^{\circ}$보다 큽니다.

> **문제 12.** $\lVert\mathbf{u}\rVert=3$, $\lVert\mathbf{v}\rVert=4$, $\theta=60^{\circ}$일 때 내적을 구하세요.

*답.* $3\cdot 4\cdot\dfrac12=6$입니다.

> **문제 13.** 문제 12의 조건에서 $\lVert\mathbf{u}+\mathbf{v}\rVert$를 구하세요.

*답.* $\sqrt{9+2\cdot 6+16}=\sqrt{37}$입니다.

> **문제 14.** $k$를 정해 $(1,k,2)$와 $(3,-1,1)$을 직교하게 만드세요.

*답.* $3-k+2=0$에서 $k=5$입니다.

> **문제 15.** 코시-슈바르츠 부등식을 쓰고 등호 조건을 말하세요.

*답.* $\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$이며 평행할 때 등호입니다.

> **문제 16.** 서로 직교하는 세 벡터의 합의 길이 제곱을 쓰세요.

*답.* 각 길이의 제곱의 합입니다. 교차항이 모두 $0$이기 때문입니다.

> **문제 17.** 상관계수를 내적으로 나타내세요.

*답.* 각 자료에서 평균을 뺀 벡터의 코사인 유사도입니다.

> **문제 18.** 내적이 쌍선형이라는 성질을 써서 $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})$를 전개하세요.

*답.* $\lVert\mathbf{u}\rVert^{2}-\lVert\mathbf{v}\rVert^{2}$입니다.

## 심화 문제

> **심화 1.** 코시-슈바르츠의 등호 조건을 증명하고 그 기하적 의미를 설명하세요.

*풀이.* 문제 3의 증명에서 판별식이 $0$인 경우를 봅니다. 그러면 이차식

$$q(t)=\lVert t\mathbf{u}+\mathbf{v}\rVert^{2}$$

이 중근을 가지므로 어떤 $t_{0}$에서 $q(t_{0})=0$입니다. 내적의 양의 정부호 성질에서

$$t_{0}\mathbf{u}+\mathbf{v}=\mathbf{0}\quad\Longrightarrow\quad\mathbf{v}=-t_{0}\mathbf{u}$$

입니다. **두 벡터가 평행합니다.**

거꾸로 $\mathbf{v}=c\mathbf{u}$이면

$$\lvert\mathbf{u}\cdot\mathbf{v}\rvert=\lvert c\rvert\lVert\mathbf{u}\rVert^{2}=\lVert\mathbf{u}\rVert\cdot\lvert c\rvert\lVert\mathbf{u}\rVert=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$$

로 등호입니다.

**기하적 의미**는 이렇습니다. $\lvert\cos\theta\rvert=1$이므로 $\theta$가 $0$이거나 $\pi$입니다. 같은 방향이거나 정반대 방향입니다.

이 조건이 실제로 쓰이는 곳을 봅니다.

| 상황 | 등호가 뜻하는 것 |
|---|---|
| 상관계수 $r=\pm 1$ | 두 자료가 완전한 직선 관계 |
| 코사인 유사도 $=1$ | 두 문서의 방향이 같음 |
| 경사하강 | 그래디언트 방향이 최대 감소 방향 |
| 삼각부등식의 등호 | 두 벡터가 같은 방향 |

**마지막 줄은 62강 문제 5에서 기하적으로 말한 것**을 대수적으로 확인한 것입니다. 삼각부등식을 코시-슈바르츠에서 유도하면

$$\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+2\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^{2}\le\lVert\mathbf{u}\rVert^{2}+2\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^{2}=(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^{2}$$

이고, 등호는 $\mathbf{u}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$일 때, 즉 **같은 방향**일 때입니다. 부호까지 맞아야 하므로 평행보다 강한 조건입니다.

> **심화 2.** 내적의 세 성질을 정의로 삼으면 어떤 대상들이 내적공간이 되는지 설명하세요.

*풀이.* 79강에서 정식으로 다루지만 여기서 미리 봅니다.

> **내적공간.** 벡터공간 $V$에 $\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$이 정의되고 대칭성, 선형성, 양의 정부호를 만족하면 $V$를 **내적공간**이라 합니다.

**성분 공식이 정의에서 빠졌습니다.** 그러면 성분이 없는 대상에도 내적을 줄 수 있습니다.

| 공간 | 내적 |
|---|---|
| $\mathbb{R}^{n}$ | $\sum u_{k}v_{k}$ |
| $C[a,b]$ | $\displaystyle\int_{a}^{b}f(x)g(x)\,dx$ |
| $m\times n$ 행렬 | $\operatorname{tr}(A^{\top}B)=\sum_{i,j}a_{ij}b_{ij}$ |
| 다항식 $P_{n}$ | $\displaystyle\int_{-1}^{1}p(x)q(x)\,dx$ |
| 가중 $\mathbb{R}^{n}$ | $\sum w_{k}u_{k}v_{k}$ ($w_{k}>0$) |

**세 성질만 확인하면 됩니다.** 함수 공간의 경우 대칭성은 곱셈의 교환법칙, 선형성은 적분의 선형성(48강), 양의 정부호는 $\int f^{2}\ge 0$이고 연속함수에서 등호가 $f\equiv 0$일 때만이라는 사실에서 나옵니다.

**중요한 것은 세 성질만으로 증명한 결과가 이 모든 공간에서 성립한다는 점입니다.** 문제 3의 코시-슈바르츠 증명이 성분을 쓰지 않았으므로

$$\left\lvert\int_{a}^{b}fg\right\rvert\le\sqrt{\int f^{2}}\sqrt{\int g^{2}}$$

가 자동으로 따라옵니다. 이를 적분형 코시-슈바르츠라 하며, 57강 심화 3의 불확정성 원리 증명에서 쓴 것이 정확히 이 부등식입니다.

각도도 함수에 정의됩니다. 두 함수가 "직교한다"는 말이 $\displaystyle\int fg=0$을 뜻하며, **59강의 삼각함수계 직교성이 바로 이 뜻이었습니다.**

> **심화 3.** 59강의 푸리에 직교성을 내적의 언어로 다시 읽고, 그때의 계수 추출이 무엇이었는지 밝히세요.

*풀이.* 59강에서 다음을 확인했습니다.

$$\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{inx}\overline{e^{imx}}\,dx=\delta_{nm}$$

이제 이것을 내적으로 읽습니다. $\langle f,g\rangle=\dfrac{1}{2\pi}\displaystyle\int_{-\pi}^{\pi}f\bar g$로 두면

$$\langle e^{inx},e^{imx}\rangle=\delta_{nm}$$

입니다. **$\{e^{inx}\}$가 정규직교집합입니다.** 서로 직교하고 각각의 길이가 $1$입니다.

그러면 계수 추출이 무엇이었는지 분명해집니다. $f=\sum c_{n}e^{inx}$의 양변에 $e^{imx}$를 내적하면 선형성으로

$$\langle f,e^{imx}\rangle=\sum_{n}c_{n}\langle e^{inx},e^{imx}\rangle=c_{m}$$

입니다. **계수가 곧 그 축 방향의 내적입니다.**

$\mathbb{R}^{n}$에서 같은 일을 해 봅니다. $\mathbf{v}=\sum v_{k}\mathbf{e}_{k}$에 $\mathbf{e}_{j}$를 내적하면

$$\mathbf{v}\cdot\mathbf{e}_{j}=v_{j}$$

입니다. **성분이 곧 표준기저 방향의 내적입니다.**

두 상황이 완전히 같은 구조입니다.

| | $\mathbb{R}^{n}$ | 함수 공간 |
|---|---|---|
| 정규직교집합 | $\{\mathbf{e}_{k}\}$ | $\{e^{inx}\}$ |
| 개수 | $n$개 | 무한개 |
| 분해 | $\mathbf{v}=\sum v_{k}\mathbf{e}_{k}$ | $f=\sum c_{n}e^{inx}$ |
| 계수 | $v_{k}=\mathbf{v}\cdot\mathbf{e}_{k}$ | $c_{n}=\langle f,e^{inx}\rangle$ |
| 길이 제곱 | $\sum v_{k}^{2}$ | $\sum\lvert c_{n}\rvert^{2}$ |

**마지막 줄이 파스발 항등식입니다.** 59강에서 "에너지가 진동수별로 나뉘어 보존된다"고 한 것이, 여기서는 피타고라스 정리의 무한판임이 드러납니다.

**푸리에 급수는 함수 공간에서의 좌표 표현이었습니다.** 이 관점이 80강의 그람슈미트와 83강의 정사영 행렬에서 정식화되며, 그때 유한차원에서 배운 것이 무한차원으로 그대로 확장됩니다.

> **심화 4.** 상관계수가 코사인 유사도와 어떻게 다른지 자료로 확인하고, 왜 평균을 빼는지 설명하세요.

*풀이.* 자료 $\mathbf{x}=(1,2,3,4,5)$와 $\mathbf{y}=(2,4,5,4,5)$를 봅니다.

**평균을 빼지 않은 코사인 유사도**를 계산하면 $0.9597$입니다. 두 벡터가 거의 같은 방향을 향합니다.

**상관계수**는 평균을 뺀 뒤 계산합니다. $\bar x=3$, $\bar y=4$이므로

$$\tilde{\mathbf{x}}=(-2,-1,0,1,2),\qquad\tilde{\mathbf{y}}=(-2,0,1,0,1)$$

이고 코사인 유사도를 구하면 $0.7746$입니다.

**두 값이 크게 다릅니다.** 이유는 이렇습니다.

| 지표 | 재는 것 |
|---|---|
| 코사인 유사도 | 원점에서 본 방향의 일치 |
| 상관계수 | **평균에서 본** 변동의 일치 |

두 자료가 모두 양수이고 크기가 비슷하면, 원점에서 보면 방향이 거의 같아 보입니다. 그래서 코사인 유사도가 높게 나옵니다. **하지만 우리가 알고 싶은 것은 "평균보다 클 때 함께 크냐"이지 "둘 다 양수냐"가 아닙니다.**

극단적인 예로 확인해 봅니다. $\mathbf{x}=(100,101,102)$와 $\mathbf{y}=(100,99,101)$이면 코사인 유사도가 $1$에 매우 가깝습니다. 두 벡터 모두 $(1,1,1)$ 방향에 거의 붙어 있기 때문입니다. 그런데 변동만 보면 $\tilde{\mathbf{x}}=(-1,0,1)$이고 $\tilde{\mathbf{y}}=(0,-1,1)$로 관계가 훨씬 약합니다.

**평균을 빼는 것은 $(1,1,1)$ 방향 성분을 제거하는 일**이며, 이것이 64강에서 배울 정사영입니다. 상관계수는 그 방향을 걷어 낸 뒤의 코사인이라고 말할 수 있습니다.

어느 것을 쓸지는 목적에 달렸습니다.

| 목적 | 쓸 지표 |
|---|---|
| 문서·임베딩의 방향 비교 | 코사인 유사도 |
| 두 변량의 함께 움직임 | 상관계수 |
| 크기까지 고려 | 내적 자체 |

256강 이후 임베딩에서 코사인 유사도를 쓰는 이유는 **벡터의 크기가 의미를 담지 않기 때문**입니다. 반면 통계에서는 평균이 기준이므로 상관계수를 씁니다.

> **심화 5.** 가중 내적을 정의하고 그것이 어떤 기하를 만드는지 설명하세요.

*풀이.* 양수 $w_{1},\dots,w_{n}$을 정하고

$$\langle\mathbf{u},\mathbf{v}\rangle_{W}=\sum_{k}w_{k}u_{k}v_{k}$$

로 정의합니다. 세 성질을 확인해 보면 모두 성립합니다. 특히 양의 정부호는 $w_{k}>0$이 보장합니다. **가중치가 하나라도 $0$이거나 음수이면 내적이 아닙니다.**

이 내적이 만드는 기하는 보통의 것과 다릅니다.

| 항목 | 표준 내적 | 가중 내적 |
|---|---|---|
| 길이 | $\sqrt{\sum v_{k}^{2}}$ | $\sqrt{\sum w_{k}v_{k}^{2}}$ |
| 단위원 | 원 | 타원 |
| 직교 | 수직 | 수직으로 보이지 않을 수 있습니다 |

**"수직"이 내적에 따라 달라집니다.** $w=(1,4)$인 가중 내적에서 $(2,1)$과 $(-2,1)$을 보면

$$1\cdot 2\cdot(-2)+4\cdot 1\cdot 1=-4+4=0$$

으로 직교입니다. 그런데 표준 내적으로는 $-4+1=-3\ne 0$이라 직교가 아닙니다. **같은 두 벡터가 어떤 내적에서는 수직이고 다른 내적에서는 아닙니다.**

이 자유도가 실용적으로 쓰입니다. 자료의 성분마다 단위가 다르면 그대로 거리를 재는 것이 부당합니다. 키를 센티미터로 재고 몸무게를 킬로그램으로 잰 자료에서 표준 거리를 쓰면 키의 변동이 지배해 버립니다. **각 성분을 분산으로 나누어 가중하면 단위에 무관한 거리가 됩니다.**

더 일반적으로는 성분끼리 상관이 있는 경우까지 다룰 수 있습니다. 양정치 행렬 $A$에 대해

$$\langle\mathbf{u},\mathbf{v}\rangle_{A}=\mathbf{u}^{\top}A\mathbf{v}$$

로 정의하면 되고, 이것으로 잰 거리를 **마할라노비스 거리**라 합니다. 87강에서 양정치성을 배우면 이 정의가 언제 내적이 되는지 정확히 알게 되며, 131강 이후 다변량 정규분포에서 이 거리가 자연스럽게 나타납니다.

> **심화 6.** 복소벡터의 내적을 정의할 때 무엇이 달라지는지 설명하세요.

*풀이.* 복소수 성분에 실수와 같은 정의를 쓰면 문제가 생깁니다. $\mathbf{v}=(i,0)$에 대해

$$\sum v_{k}^{2}=i^{2}=-1<0$$

이므로 **양의 정부호가 깨집니다.** 길이의 제곱이 음수가 되어 노름을 정의할 수 없습니다.

해결은 한쪽에 켤레를 씌우는 것입니다.

$$\langle\mathbf{u},\mathbf{v}\rangle=\sum_{k}u_{k}\overline{v_{k}}$$

그러면

$$\langle\mathbf{v},\mathbf{v}\rangle=\sum v_{k}\overline{v_{k}}=\sum\lvert v_{k}\rvert^{2}\ge 0$$

으로 양의 정부호가 회복됩니다. **30강에서 $z\bar z=\lvert z\rvert^{2}$이라고 한 것이 여기서 쓰입니다.**

대신 대칭성이 바뀝니다.

$$\langle\mathbf{v},\mathbf{u}\rangle=\sum v_{k}\overline{u_{k}}=\overline{\sum u_{k}\overline{v_{k}}}=\overline{\langle\mathbf{u},\mathbf{v}\rangle}$$

**켤레 대칭**이라 합니다. 그리고 선형성도 한쪽에서만 성립합니다.

| 성질 | 실수 내적 | 복소 내적 |
|---|---|---|
| 대칭 | $\langle\mathbf{u},\mathbf{v}\rangle=\langle\mathbf{v},\mathbf{u}\rangle$ | $\langle\mathbf{v},\mathbf{u}\rangle=\overline{\langle\mathbf{u},\mathbf{v}\rangle}$ |
| 첫째 자리 | 선형 | 선형 |
| 둘째 자리 | 선형 | **켤레선형** ($\langle\mathbf{u},c\mathbf{v}\rangle=\bar c\langle\mathbf{u},\mathbf{v}\rangle$) |
| $\langle\mathbf{v},\mathbf{v}\rangle$ | 실수, $\ge 0$ | 실수, $\ge 0$ |

**켤레 대칭 덕분에 $\langle\mathbf{v},\mathbf{v}\rangle$이 자기 켤레와 같아 자동으로 실수**가 됩니다. 길이를 정의하는 데 필요한 조건이 구조적으로 보장되는 셈입니다.

이 정의가 59강에서 이미 쓰였습니다. 그때 직교성을 $\dfrac{1}{2\pi}\displaystyle\int e^{inx}\overline{e^{imx}}dx$로 적었는데, **켤레를 씌운 것이 바로 이 이유**입니다. 켤레 없이 계산하면 $e^{inx}$와 $e^{-inx}$가 직교하지 않게 되어 계수 추출이 무너집니다.

복소 내적은 양자역학과 신호처리의 표준이며, 이 커리큘럼에서는 60강의 푸리에 변환과 88강의 특이값 분해에서 다시 나타납니다.

## 코드 검산

이 강의에서는 numpy만 씁니다. 내적은 `@` 연산자로 바로 계산되므로 검산이 직접적입니다. **기하 표현과 성분 표현이 같은 값을 주는지, 그리고 부등식이 성립하는지를 확인하는 것이 목적입니다.**

```python
import numpy as np

u = np.array([3.0, -1.0, 2.0]); v = np.array([-1.0, 4.0, 5.0]); w = np.array([2.0, 0.0, -3.0])

# --- 문제 1: 내적과 코사인 법칙 -----------------------------------------
print(float(u @ v), float(np.sum(u*v)))                    # 3.0 3.0
lhs = float(np.linalg.norm(u - v)**2)
rhs = float(np.linalg.norm(u)**2 + np.linalg.norm(v)**2 - 2*(u @ v))
print("%.8f %.8f" % (lhs, rhs))                            # 50.00000000 50.00000000

# --- 문제 2: 내적의 성질 ------------------------------------------------
a, b = 2.5, -1.5
print(bool(np.isclose(u @ v, v @ u)),
      bool(np.isclose((a*u + b*w) @ v, a*(u @ v) + b*(w @ v))),
      bool(u @ u > 0), float(np.zeros(3) @ np.zeros(3)))
# True True True 0.0
print("%.8f %.8f" % (float(u @ u), float(np.linalg.norm(u)**2)))
# 14.00000000 14.00000000

# --- 문제 3: 각도 -------------------------------------------------------
def angle(p, q):
    c = float(p @ q)/(float(np.linalg.norm(p))*float(np.linalg.norm(q)))
    return c, float(np.degrees(np.arccos(c)))
for p, q in [(u, v), (u, u), (u, -u), (np.array([1.0,0.0]), np.array([1.0,1.0]))]:
    c, d = angle(p, q)
    print("%.8f %.6f" % (c, d))
# 0.12371791 82.893277
# 1.00000000 0.000000
# -1.00000000 180.000000
# 0.70710678 45.000000

# --- 문제 4: 직교와 피타고라스 ------------------------------------------
p = np.array([1.0, 2.0, 3.0]); q = np.array([2.0, -1.0, 0.0])
print(float(p @ q))                                        # 0.0
print("%.8f %.8f" % (float(np.linalg.norm(p + q)**2),
                     float(np.linalg.norm(p)**2 + np.linalg.norm(q)**2)))
# 19.00000000 19.00000000
print("%.8f %.8f" % (float(np.linalg.norm(u + v)**2),
                     float(np.linalg.norm(u)**2 + np.linalg.norm(v)**2)))
# 62.00000000 56.00000000     (차이 6 = 2*(u@v))

# --- 심화 1: 코시-슈바르츠 ----------------------------------------------
for p, q in [(u, v), (u, 2*u), (np.array([1.0,1.0]), np.array([1.0,-1.0]))]:
    print("%.8f %.8f" % (abs(float(p @ q)),
                         float(np.linalg.norm(p))*float(np.linalg.norm(q))))
# 3.00000000 24.24871131      (부등식)
# 28.00000000 28.00000000     (평행 -> 등호)
# 0.00000000 2.00000000       (직교)

# --- 심화 4: 코사인 유사도와 상관계수 -----------------------------------
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0]); y = np.array([2.0, 4.0, 5.0, 4.0, 5.0])
xc = x - x.mean(); yc = y - y.mean()
r = float(xc @ yc)/(float(np.linalg.norm(xc))*float(np.linalg.norm(yc)))
print("%.8f %.8f" % (r, float(np.corrcoef(x, y)[0,1])))
# 0.77459667 0.77459667
print("%.8f" % (float(x @ y)/(float(np.linalg.norm(x))*float(np.linalg.norm(y)))))
# 0.95965110                  (평균을 안 빼면 훨씬 큽니다)

# --- 심화 2, 3: 함수의 내적 (다항식의 그람 행렬) -------------------------
t = np.linspace(-1.0, 1.0, 400001)[:-1] + 1.0/400000
dt = 2.0/400000
def ip(f, g): return float(np.sum(f(t)*g(t))*dt)
mono = [lambda z: np.ones_like(z), lambda z: z, lambda z: z**2]
for i in range(3):
    print([round(ip(mono[i], mono[j]), 6) for j in range(3)])
# [2.0, 0.0, 0.666667]
# [0.0, 0.666667, 0.0]
# [0.666667, 0.0, 0.4]
```

실행하면 주석과 같은 값이 나옵니다. 다섯 곳을 짚어 둡니다.

첫째, 코사인 법칙으로 얻은 값과 성분 전개가 양쪽 모두 $50$입니다. **문제 1의 유도가 숫자로 확인됩니다.** 그리고 $\mathbf{u}\cdot\mathbf{u}=14$가 $\lVert\mathbf{u}\rVert^{2}$과 같습니다.

둘째, 각도 계산에서 네 가지 경우가 나옵니다. 자기 자신과는 $0^{\circ}$, 반대 벡터와는 정확히 $180^{\circ}$, $(1,0)$과 $(1,1)$은 $45^{\circ}$입니다. **정의가 우리가 아는 각도와 일치합니다.**

셋째, 피타고라스 정리의 성립과 실패가 나란히 나옵니다. 직교하는 $(1,2,3)$과 $(2,-1,0)$에서는 양변이 $19$로 같지만, 직교하지 않는 $\mathbf{u}$와 $\mathbf{v}$에서는 $62$와 $56$으로 다릅니다. **차이 $6$이 정확히 $2\,\mathbf{u}\cdot\mathbf{v}=2\cdot 3$입니다.**

넷째, 코시-슈바르츠가 세 경우에서 확인됩니다. 일반적인 경우 $3\le 24.25$로 여유가 크고, $\mathbf{u}$와 $2\mathbf{u}$처럼 평행하면 양변이 $28$로 **정확히 같습니다.** 직교하면 왼쪽이 $0$이라 가장 헐거운 부등식이 됩니다.

다섯째, 심화 4의 대비가 인상적입니다. 같은 자료에서 상관계수가 $0.7746$인데 평균을 빼지 않은 코사인 유사도는 $0.9597$입니다. **두 지표가 다른 것을 재고 있습니다.** 마지막 블록의 다항식 그람 행렬도 눈여겨보십시오. $1$과 $x$, $x$와 $x^{2}$은 직교하는데 $1$과 $x^{2}$은 내적이 $\dfrac23$으로 직교하지 않습니다. 80강의 그람슈미트가 이 상황을 정리하는 도구입니다.

코드로 할 수 없는 일도 분명히 해 둡니다. **몇 개의 값에서 성질을 확인한 것은 증명이 아닙니다.** 특히 코시-슈바르츠는 모든 벡터 쌍에 대한 주장이므로 판별식 논법이 필요합니다. 그리고 심화 2에서 말한 대로 세 성질만으로 한 증명은 함수 공간에도 적용되는데, 그 사실은 수치로 확인할 수 있는 종류가 아닙니다.

## 스스로 점검

1. 내적의 정의를 성분으로 쓰세요.
2. 내적의 기하 표현을 쓰고 어떻게 유도합니까?
3. 내적의 세 가지 성질을 쓰세요.
4. $\lVert\mathbf{u}+\mathbf{v}\rVert^{2}$을 내적으로 전개하세요.
5. 코시-슈바르츠 부등식과 등호 조건을 쓰세요.
6. 각도를 정의할 때 코시-슈바르츠가 왜 필요합니까?
7. 직교의 정의와 피타고라스 정리를 쓰세요.
8. 코사인 유사도와 상관계수의 차이를 쓰세요.
9. 상관계수가 $[-1,1]$에 있는 이유를 쓰세요.
10. 복소 내적에서 켤레를 씌우는 이유를 쓰세요.

**정답.**
1. $\mathbf{u}\cdot\mathbf{v}=\sum u_{k}v_{k}$입니다.
2. $\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$이며 코사인 법칙과 성분 전개를 비교해 얻습니다.
3. 대칭성, 선형성, 양의 정부호입니다.
4. $\lVert\mathbf{u}\rVert^{2}+2\,\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^{2}$입니다.
5. $\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$이며 평행할 때 등호입니다.
6. $\arccos$에 넣을 값이 $[-1,1]$ 안에 있음을 보장해야 하기 때문입니다.
7. 내적이 $0$이면 직교이며, 그때 $\lVert\mathbf{u}+\mathbf{v}\rVert^{2}=\lVert\mathbf{u}\rVert^{2}+\lVert\mathbf{v}\rVert^{2}$입니다.
8. 상관계수는 각 벡터에서 평균을 뺀 뒤의 코사인 유사도입니다.
9. 코사인 값이므로 코시-슈바르츠에 의해 그 범위를 벗어날 수 없습니다.
10. 켤레가 없으면 $\langle\mathbf{v},\mathbf{v}\rangle$이 음수가 될 수 있어 양의 정부호가 깨지기 때문입니다.

## 부록. 기호 정리

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\mathbf{u}\cdot\mathbf{v}$ | 내적, 점곱 | $\sum u_{k}v_{k}$입니다 |
| $\langle\mathbf{u},\mathbf{v}\rangle$ | 내적 | 일반 내적공간에서 쓰는 기호입니다 |
| $\mathbf{u}\perp\mathbf{v}$ | 직교 | 내적이 $0$입니다 |
| $\delta_{ij}$ | 크로네커 델타 | $i=j$이면 $1$, 아니면 $0$입니다 |
| 코시-슈바르츠 | Cauchy-Schwarz | $\lvert\langle\mathbf{u},\mathbf{v}\rangle\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$입니다 |
| 정규직교 | orthonormal | 직교하고 길이가 모두 $1$입니다 |
| 코사인 유사도 | cosine similarity | 정규화한 뒤의 내적입니다 |
| 켤레선형 | conjugate linear | 스칼라가 켤레로 나옵니다 |

다음 64강에서는 내적으로 **한 벡터를 다른 벡터 방향으로 분해**합니다. 그림자를 드리우는 것과 같아 정사영이라 부르는데, 그 결과가 두 조각으로 갈라집니다. 방향이 맞는 부분과 수직인 부분입니다. 이 분해가 80강의 그람슈미트와 82강의 최소제곱에서 되풀이해 쓰이며, 심화 4에서 상관계수가 "$(1,1,\dots,1)$ 방향을 걷어 낸 뒤의 코사인"이라고 한 말의 정확한 뜻도 그때 밝혀집니다.
