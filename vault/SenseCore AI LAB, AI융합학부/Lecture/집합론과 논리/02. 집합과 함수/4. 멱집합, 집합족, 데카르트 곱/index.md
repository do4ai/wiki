---
title: "4. 멱집합, 집합족, 데카르트 곱"
---
# 4강. 멱집합, 집합족, 데카르트 곱

집합 연산을 두 개짜리로만 다루면 곧 한계에 부딪힙니다. 구간 $[0,1/n]$을 $n=1,2,3,\dots$에 걸쳐 모두 교집합하거나, 좌표를 무한히 많이 늘어놓는 일은 이항 연산으로 표현되지 않습니다. 이 강의는 집합의 집합인 멱집합, 임의 개수의 집합을 다루는 집합족, 그리고 곱을 무한히 확장한 데카르트 곱을 세웁니다.

## 이 강의에서 할 수 있게 되는 것

- 멱집합을 정의하고 유한집합에서 그 크기가 $2^n$임을 두 가지 방법으로 증명할 수 있습니다.
- 첨수집합으로 집합족을 표기하고 그 합집합과 교집합을 한정기호로 정의할 수 있습니다.
- 일반화된 드모르간 법칙과 분배법칙을 진술하고 원소 논법으로 증명할 수 있습니다.
- 유한 개와 무한 개 집합의 데카르트 곱을 정의하고 곱의 원소를 함수로 다시 볼 수 있습니다.
- 특성함수를 써서 부분집합과 $\{0,1\}$ 값 함수를 대응시킬 수 있습니다.

이 강의는 [3강 집합과 함수](../3. 집합과 함수/index.md)에서 세운 집합 연산과 함수의 정의를 전제로 합니다. 여기서 만든 곱집합의 부분집합 관점은 [5강 관계와 동치](../../03. 관계/5. 관계와 동치/index.md)로 이어지고, 멱집합의 크기가 원래 집합보다 반드시 크다는 사실은 [9강 기수와 가산집합](../../05. 무한과 공리계/9. 기수와 가산집합/index.md)에서 다룹니다. 무한 곱이 비어 있지 않다는 주장에 필요한 공리는 [11강 ZFC 공리계와 선택공리 개관](../../05. 무한과 공리계/11. ZFC 공리계와 선택공리 개관/index.md)에서 정리합니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\mathcal{P}(A)$ | $A$의 멱집합 | $A$의 부분집합 전체의 집합 |
| $2^A$ | 투 에이 | 멱집합의 다른 표기 |
| $\mathcal{F}$ | 집합족 에프 | 원소가 모두 집합인 모임 |
| $I$ | 첨수집합 | 집합족에 번호를 붙이는 집합 |
| $\{A_i\}_{i\in I}$ | 첨수화된 집합족 | 각 $i\in I$에 집합 $A_i$를 대응시킨 족 |
| $\bigcup_{i\in I}A_i$ | 첨수 합집합 | 어떤 $A_i$에라도 속하는 원소 전체 |
| $\bigcap_{i\in I}A_i$ | 첨수 교집합 | 모든 $A_i$에 속하는 원소 전체 |
| $(a_1,\dots,a_n)$ | 순서 $n$쌍 | 성분의 순서가 뜻을 가지는 $n$개 묶음 |
| $A_1\times\cdots\times A_n$ | 데카르트 곱 | 순서 $n$쌍의 집합 |
| $\prod_{i\in I}A_i$ | 첨수 곱 | 각 $i$에서 $A_i$의 값을 고르는 방법 전체 |
| $B^A$ | 비 에이 | $A$에서 $B$로 가는 함수 전체의 집합 |
| $\pi_j$ | 파이 제이 | $j$번째 성분을 뽑는 사영 |
| $\chi_A$ | 카이 에이 | 집합 $A$의 특성함수 |

## 2. 개념

### 2.1 멱집합

**정의.** 집합 $A$에 대해 $A$의 부분집합 전체를 모은 집합을 $A$의 **멱집합**이라 하고 $\mathcal{P}(A)$로 씁니다.

$$
\mathcal{P}(A)=\{S \mid S\subseteq A\}
$$

멱집합은 원소가 집합인 집합입니다. 따라서 $S\in\mathcal{P}(A)$와 $S\subseteq A$는 정확히 같은 뜻이며, 이 두 표기를 자유롭게 오갈 수 있습니다.

작은 예를 계산합니다.

$$
\mathcal{P}(\{1,2\})=\big\{\varnothing,\ \{1\},\ \{2\},\ \{1,2\}\big\}
$$

$$
\mathcal{P}(\varnothing)=\{\varnothing\},\qquad \mathcal{P}(\{\varnothing\})=\big\{\varnothing,\ \{\varnothing\}\big\}
$$

$\mathcal{P}(\varnothing)$이 공집합이 아니라 원소가 하나인 집합임에 주의합니다. 공집합의 부분집합은 공집합 자신 하나이기 때문입니다. 원소와 부분집합의 구분도 중요합니다. $1\in\{1,2\}$는 참이지만 $1\in\mathcal{P}(\{1,2\})$는 거짓이고, 멱집합의 원소는 수가 아니라 집합이므로 $\{1\}\in\mathcal{P}(\{1,2\})$가 올바른 서술입니다.

**정리.** $A$가 유한집합이고 $|A|=n$이면 $|\mathcal{P}(A)|=2^n$입니다.

첫 번째 증명은 선택의 개수를 세는 방법입니다. 부분집합 하나를 정하는 일은 $A$의 원소 하나하나에 대해 "넣는다" 또는 "넣지 않는다"를 정하는 일과 같습니다. 원소가 $n$개이고 각 선택이 독립적으로 두 가지이므로 서로 다른 부분집합은 $2^n$개입니다.

두 번째 증명은 원소 개수에 대한 귀납법입니다. $n=0$이면 $A=\varnothing$이고 $\mathcal{P}(\varnothing)=\{\varnothing\}$의 크기는 $1=2^0$입니다. $|A|=n$인 모든 집합에서 성립한다고 가정하고 $|A|=n+1$이라 합니다. 원소 $a\in A$를 하나 고정하고 $A'=A\setminus\{a\}$라 두면 $|A'|=n$입니다. $A$의 부분집합은 $a$를 포함하지 않는 것과 포함하는 것으로 정확히 이분됩니다. 앞쪽은 $A'$의 부분집합 전체이므로 $2^n$개입니다. 뒤쪽은 각각 $S\cup\{a\}$의 모양이며 $S\in\mathcal{P}(A')$와 일대일로 대응하므로 역시 $2^n$개입니다. 두 모임은 서로소이므로 전체는 $2^n+2^n=2^{n+1}$개입니다. $\square$

멱집합은 포함관계를 보존합니다. $A\subseteq B$이면 $A$의 부분집합은 모두 $B$의 부분집합이므로 $\mathcal{P}(A)\subseteq\mathcal{P}(B)$입니다. 교집합에 대해서는 등식 $\mathcal{P}(A\cap B)=\mathcal{P}(A)\cap\mathcal{P}(B)$가 성립하지만, 합집합에 대해서는 한쪽 포함 $\mathcal{P}(A)\cup\mathcal{P}(B)\subseteq\mathcal{P}(A\cup B)$만 성립합니다.

> **문제 1.** (표준) $\mathcal{P}(\mathcal{P}(\varnothing))$을 원소나열법으로 쓰고 그 크기를 구하십시오.
> **답.** $\big\{\varnothing,\{\varnothing\}\big\}$이고 크기는 $2$입니다.
> **풀이.** $\mathcal{P}(\varnothing)=\{\varnothing\}$이므로 크기가 $1$인 집합의 멱집합을 구하는 문제가 됩니다. 크기 $1$인 집합의 부분집합은 공집합과 자기 자신이므로 $\big\{\varnothing,\{\varnothing\}\big\}$이고 크기는 $2^1=2$입니다.

> **문제 2.** (심화) $\mathcal{P}(A\cup B)=\mathcal{P}(A)\cup\mathcal{P}(B)$가 일반적으로 성립하지 않음을 반례로 보이십시오.
> **답.** $A=\{1\}$, $B=\{2\}$일 때 $\{1,2\}$가 좌변에는 속하지만 우변에는 속하지 않습니다.
> **풀이.** $A\cup B=\{1,2\}$이므로 $\{1,2\}\in\mathcal{P}(A\cup B)$입니다. 그런데 $\{1,2\}$는 $A$의 부분집합도 아니고 $B$의 부분집합도 아니므로 $\mathcal{P}(A)\cup\mathcal{P}(B)$에 속하지 않습니다. 따라서 등식이 깨집니다. 두 집합에 걸쳐 원소를 섞어 뽑은 부분집합이 우변에서 누락되는 것이 원인이며, 포함 방향 $\mathcal{P}(A)\cup\mathcal{P}(B)\subseteq\mathcal{P}(A\cup B)$는 항상 성립합니다. $\square$

### 2.2 집합족과 첨수집합

**정의.** 원소가 모두 집합인 모임을 **집합족**이라 합니다. 집합족의 원소를 번호로 가리키기 위해 집합 $I$와 각 $i\in I$에 집합 $A_i$를 대응시키는 규칙을 함께 줄 때, 이를 **첨수화된 집합족**이라 하고 $\{A_i\}_{i\in I}$로 씁니다. 이때 $I$를 **첨수집합**이라 합니다.

첨수집합은 자연수 집합일 필요가 없습니다. 다음은 모두 정당한 첨수화입니다.

- $I=\mathbb{N}$, $A_n=\left[0,\tfrac{1}{n}\right]$. 첨수가 커지면 구간이 줄어듭니다.
- $I=\mathbb{R}$, $L_r=\{(x,y)\in\mathbb{R}^2 \mid y=rx\}$. 각 실수 기울기마다 원점을 지나는 직선을 하나 대응시킵니다.
- $I=\mathcal{P}(X)$, $A_S=S$. 멱집합 자체를 첨수집합으로 쓰면 집합족과 첨수화가 같은 대상이 됩니다.

첨수화는 중복을 허용한다는 점에서 단순한 집합족과 다릅니다. $I=\{1,2\}$이고 $A_1=A_2=\{0\}$이면 첨수화된 족은 두 자리를 가지지만, 이를 그냥 집합족으로 보면 원소가 하나인 $\{\{0\}\}$입니다. 첨수를 쓰는 이유는 자리마다 이름을 유지해 계산을 추적할 수 있기 때문이며, 곱집합처럼 자리 수가 결과에 영향을 주는 연산에서 이 구별이 필요합니다.

> **문제 1.** (기초) $I=\{1,2,3\}$, $A_i=\{1,2,\dots,i\}$로 주어진 집합족의 원소를 모두 쓰십시오.
> **답.** $A_1=\{1\}$, $A_2=\{1,2\}$, $A_3=\{1,2,3\}$입니다.
> **풀이.** 각 첨수 $i$에 $1$부터 $i$까지의 자연수 집합을 대응시키므로 위와 같이 세 집합이 나옵니다. 이 족은 $A_1\subseteq A_2\subseteq A_3$으로 증가하는 족입니다.

> **문제 2.** (표준) $I=\mathbb{N}$, $A_n=\{n, n+1, n+2, \dots\}$일 때 $A_5$가 $A_3$의 부분집합인지 판정하십시오.
> **답.** 부분집합입니다.
> **풀이.** $A_5=\{5,6,7,\dots\}$이고 $A_3=\{3,4,5,\dots\}$입니다. $A_5$의 임의의 원소 $k$는 $k\ge 5\ge 3$을 만족하므로 $A_3$에 속합니다. 따라서 $A_5\subseteq A_3$이며 이 족은 첨수가 커질 때 줄어드는 감소족입니다.

### 2.3 집합족의 합집합과 교집합

**정의.** 첨수화된 집합족 $\{A_i\}_{i\in I}$에 대해 다음을 정의합니다.

$$
\bigcup_{i\in I}A_i=\{x \mid \exists i\in I\ (x\in A_i)\}
$$

$$
\bigcap_{i\in I}A_i=\{x \mid \forall i\in I\ (x\in A_i)\}
$$

정의를 보면 합집합이 존재한정기호에, 교집합이 전체한정기호에 대응합니다. 3강에서 $\cup$이 $\lor$에, $\cap$이 $\land$에 대응한 것과 같은 구조이며, 유한 개에서 임의 개로 확장된 것입니다.

첨수집합이 비어 있으면 두 연산이 어긋납니다. $I=\varnothing$이면 존재 조건을 만족하는 원소가 없으므로 $\bigcup_{i\in\varnothing}A_i=\varnothing$입니다. 반면 전체 조건은 공허하게 참이 되어 모든 대상이 조건을 만족하므로 교집합은 전체집합이 되어야 하고, 전체집합을 미리 정하지 않으면 정의되지 않습니다. 그래서 교집합을 다룰 때는 보통 $I\ne\varnothing$을 가정합니다.

구체적 계산을 봅니다. $I=\mathbb{N}$, $A_n=\left[0,\tfrac{1}{n}\right]$이면

$$
\bigcup_{n\in\mathbb{N}}A_n=[0,1],\qquad \bigcap_{n\in\mathbb{N}}A_n=\{0\}
$$

입니다. 합집합은 가장 큰 구간 $A_1=[0,1]$이 나머지를 모두 포함하므로 $[0,1]$입니다. 교집합에서 $0$은 모든 구간에 들어 있고, $x>0$인 실수는 $\tfrac1n<x$가 되는 $n$을 잡으면 $x\notin A_n$이므로 빠집니다. 따라서 교집합은 $\{0\}$입니다. 무한히 많은 집합을 모으면 각 항에는 없던 성질이 결과에 나타날 수 있습니다. $B_n=\left(0,\,1-\tfrac1n\right)$이면 각 $B_n$은 $1$에 못 미치는 열린구간이지만 합집합은 $(0,1)$ 전체가 됩니다.

**정리(일반화된 드모르간 법칙).** 전체집합 $U$ 안에서 $I\ne\varnothing$인 집합족 $\{A_i\}_{i\in I}$에 대해

$$
\Big(\bigcup_{i\in I}A_i\Big)^c=\bigcap_{i\in I}A_i^{\,c},
\qquad
\Big(\bigcap_{i\in I}A_i\Big)^c=\bigcup_{i\in I}A_i^{\,c}
$$

첫 식을 증명합니다. 임의의 $x\in U$에 대해

$$
x\in\Big(\bigcup_{i\in I}A_i\Big)^c
\iff \lnot\,\exists i\in I\ (x\in A_i)
\iff \forall i\in I\ (x\notin A_i)
\iff x\in\bigcap_{i\in I}A_i^{\,c}
$$

가운데 단계가 [2강](../../01. 명제와 논리/2. 술어논리와 한정기호/index.md)의 부정 규칙 $\lnot\exists\equiv\forall\lnot$입니다. 양쪽 조건이 서로 필요충분이므로 두 집합은 같습니다. 둘째 식은 $\lnot\forall\equiv\exists\lnot$으로 같은 방식으로 얻습니다. $\square$

**정리(일반화된 분배법칙).** $I\ne\varnothing$일 때

$$
B\cap\bigcup_{i\in I}A_i=\bigcup_{i\in I}(B\cap A_i),
\qquad
B\cup\bigcap_{i\in I}A_i=\bigcap_{i\in I}(B\cup A_i)
$$

첫 식은 $x\in B \land \exists i\,(x\in A_i)$가 $\exists i\,(x\in B \land x\in A_i)$와 동치라는 사실에서 따라 나옵니다. $x\in B$는 첨수 $i$와 무관하므로 존재기호 안으로 넣거나 밖으로 뺄 수 있습니다. $\square$

> **문제 1.** (표준) $C_n=\left(-\tfrac1n,\tfrac1n\right)$($n\in\mathbb{N}$)일 때 $\bigcap_{n\in\mathbb{N}}C_n$을 구하십시오.
> **답.** $\{0\}$입니다.
> **풀이.** $0$은 모든 $n$에 대해 $-\tfrac1n<0<\tfrac1n$을 만족하므로 교집합에 속합니다. $x\ne 0$이면 $\tfrac1n<|x|$가 되는 자연수 $n$을 잡을 수 있고 그 $n$에서 $x\notin C_n$이므로 교집합에서 빠집니다. 따라서 교집합은 $\{0\}$입니다. 열린구간을 무한히 교집합하면 닫힌 한 점이 남을 수 있습니다.

> **문제 2.** (심화) $\Big(\bigcap_{i\in I}A_i\Big)^c=\bigcup_{i\in I}A_i^{\,c}$를 원소 논법으로 증명하십시오.
> **답.** 한정기호의 부정 규칙 $\lnot\forall\equiv\exists\lnot$을 적용하면 양쪽 조건이 동치가 됩니다.
> **풀이.** 임의의 $x\in U$에 대해 $x\in\big(\bigcap_{i\in I}A_i\big)^c$는 $\lnot\forall i\in I\,(x\in A_i)$와 같습니다. 부정 규칙으로 이는 $\exists i\in I\,(x\notin A_i)$이고, 다시 $\exists i\in I\,(x\in A_i^{\,c})$이므로 $x\in\bigcup_{i\in I}A_i^{\,c}$입니다. 모든 단계가 필요충분이므로 두 집합은 상등입니다. $\square$

### 2.4 데카르트 곱: 유한 곱

3강에서 두 집합의 곱집합 $A\times B=\{(a,b)\mid a\in A \land b\in B\}$를 정의했습니다. 이를 $n$개로 확장합니다.

**정의.** 집합 $A_1,\dots,A_n$에 대해 **데카르트 곱**을 순서 $n$쌍의 집합으로 정의합니다.

$$
A_1\times A_2\times\cdots\times A_n=\{(a_1,a_2,\dots,a_n)\mid a_i\in A_i\ (i=1,\dots,n)\}
$$

모든 $A_i$가 같은 집합 $A$일 때는 $A^n$으로 씁니다. 좌표평면 $\mathbb{R}^2$와 공간 $\mathbb{R}^3$이 대표적인 예입니다.

순서 $n$쌍의 상등은 성분별 상등이므로 $(a_1,\dots,a_n)=(b_1,\dots,b_n)$은 모든 $i$에서 $a_i=b_i$와 같습니다. 유한집합에서 크기는 곱으로 계산됩니다.

$$
\lvert A_1\times\cdots\times A_n\rvert=\lvert A_1\rvert\cdot\lvert A_2\rvert\cdots\lvert A_n\rvert
$$

첫 자리에 $\lvert A_1\rvert$가지, 둘째 자리에 $\lvert A_2\rvert$가지를 독립적으로 고를 수 있기 때문입니다. 특별히 어떤 $A_i$가 공집합이면 그 자리에 놓을 원소가 없으므로 곱 전체가 공집합입니다.

결합성에는 주의가 필요합니다. $(A\times B)\times C$의 원소는 $((a,b),c)$ 모양이고 $A\times(B\times C)$의 원소는 $(a,(b,c))$ 모양이므로, 두 집합은 엄밀히 말해 서로 다릅니다. 그러나 $((a,b),c)\mapsto(a,b,c)$가 전단사이므로 자연스러운 동일시가 가능하고, 실제 계산에서는 셋을 구별하지 않고 $A\times B\times C$로 씁니다.

순서쌍 자체를 집합으로 정의할 수도 있습니다. 쿠라토프스키의 정의 $(a,b)=\big\{\{a\},\{a,b\}\big\}$를 쓰면 "$(a,b)=(c,d)$이면 $a=c$이고 $b=d$"라는 성질이 공리가 아니라 정리로 증명됩니다. 순서라는 개념까지 집합만으로 만들 수 있다는 점이 요지이며, 이 관점은 11강에서 다시 다룹니다.

> **문제 1.** (표준) $A\times B=B\times A$가 성립하는 조건을 구하십시오.
> **답.** $A=B$이거나 $A$와 $B$ 중 하나가 공집합일 때입니다.
> **풀이.** 둘 중 하나가 공집합이면 양변이 모두 공집합이라 성립합니다. 둘 다 비어 있지 않고 $A\ne B$라 하면 한쪽에만 있는 원소가 존재합니다. 예를 들어 $a\in A\setminus B$이고 $b\in B$를 잡으면 $(a,b)\in A\times B$이지만 첫 성분 $a$가 $B$에 없으므로 $(a,b)\notin B\times A$입니다. 따라서 등식이 깨지므로 $A=B$가 필요합니다.

> **문제 2.** (심화) 쿠라토프스키의 정의 $(a,b)=\big\{\{a\},\{a,b\}\big\}$에서 $(a,b)=(a,c)$이면 $b=c$임을 보이십시오.
> **답.** 두 집합이 같으므로 원소를 대조하면 $\{a,b\}=\{a,c\}$가 되고 여기서 $b=c$가 따라 나옵니다.
> **풀이.** 가정은 $\big\{\{a\},\{a,b\}\big\}=\big\{\{a\},\{a,c\}\big\}$입니다. 좌변의 원소 $\{a,b\}$는 우변의 원소이므로 $\{a,b\}=\{a\}$ 또는 $\{a,b\}=\{a,c\}$입니다. 앞의 경우 $b=a$이고, 같은 논법을 우변의 $\{a,c\}$에 적용하면 $c=a$가 나오므로 $b=c=a$입니다. 뒤의 경우 $\{a,b\}=\{a,c\}$에서 $b\ne a$이면 $b$가 우변의 원소여야 하므로 $b=c$입니다. 어느 경우에도 $b=c$입니다. $\square$

### 2.5 무한 곱과 함수로서의 곱

순서 $n$쌍을 함수로 다시 보는 것이 무한 곱으로 가는 열쇠입니다. $(a_1,\dots,a_n)$은 첨수 $i$에 값 $a_i$를 대응시키는 규칙이므로, 정의역이 $\{1,\dots,n\}$인 함수 $f$로 보고 $f(i)=a_i$라 쓸 수 있습니다. 이때 조건은 각 자리의 값이 그 자리에 허용된 집합에 들어 있어야 한다는 것, 즉 $f(i)\in A_i$입니다.

**정의.** 첨수화된 집합족 $\{A_i\}_{i\in I}$에 대해 **데카르트 곱**을 다음으로 정의합니다.

$$
\prod_{i\in I}A_i=\Big\{f: I\to\bigcup_{i\in I}A_i \ \Big|\ \forall i\in I\ \big(f(i)\in A_i\big)\Big\}
$$

첨수집합이 $\{1,\dots,n\}$인 경우 이 정의는 앞 절의 유한 곱과 자연스럽게 일치합니다. 첨수집합이 무한집합이어도 정의는 그대로 통합니다. 곱의 원소를 각 자리에서 값을 하나씩 고른 선택 결과로 보는 것이 이 정의의 뜻입니다.

모든 $A_i$가 같은 집합 $A$이면 조건 $f(i)\in A$가 자동으로 성립하므로 $\prod_{i\in I}A=\{f:I\to A\}=A^{I}$가 됩니다. 일반적으로 $A$에서 $B$로 가는 함수 전체의 집합을 $B^A$로 씁니다. 유한집합에서는 크기가 지수로 계산됩니다.

$$
\lvert B^A\rvert=\lvert B\rvert^{\lvert A\rvert}
$$

정의역의 원소 하나하나에 대해 $\lvert B\rvert$가지 값을 독립적으로 고를 수 있기 때문입니다. 곱집합에서 특정 자리의 값을 뽑아내는 함수를 **사영**이라 하고 $\pi_j:\prod_{i\in I}A_i\to A_j$, $\pi_j(f)=f(j)$로 정의합니다.

모든 $A_i$가 비어 있지 않을 때 곱이 비어 있지 않은가 하는 질문이 남습니다. 첨수집합이 유한하면 자리마다 원소를 하나씩 골라 나열하면 되므로 유한 번의 선택으로 답이 나옵니다. 그러나 첨수집합이 무한하면 무한히 많은 선택을 동시에 해야 하고, 이를 보장하는 원리가 바로 **선택공리**입니다. 실제로 "모든 $A_i$가 비어 있지 않으면 $\prod_{i\in I}A_i\ne\varnothing$"이라는 명제는 선택공리와 동치입니다. 자세한 내용은 11강에서 다룹니다.

> **문제 1.** (표준) $I=\mathbb{N}$이고 모든 $n$에 대해 $A_n=\{0,1\}$일 때 $\prod_{n\in\mathbb{N}}A_n$의 원소가 무엇인지 설명하십시오.
> **답.** $0$과 $1$로 이루어진 무한 수열 전체입니다.
> **풀이.** 정의에 따라 원소는 $f:\mathbb{N}\to\{0,1\}$인 함수이고, 이는 각 자리에 $0$ 또는 $1$을 배정한 것이므로 $(f(1),f(2),f(3),\dots)$라는 무한 이진 수열과 같습니다. 이 집합은 $\{0,1\}^{\mathbb{N}}$으로 쓰며 10강의 대각선 논법에서 비가산성의 대표 예로 등장합니다.

> **문제 2.** (심화) 어떤 $i_0\in I$에 대해 $A_{i_0}=\varnothing$이면 $\prod_{i\in I}A_i=\varnothing$임을 보이십시오.
> **답.** 곱의 원소가 존재한다고 가정하면 $f(i_0)\in A_{i_0}=\varnothing$이 되어 모순입니다.
> **풀이.** $f\in\prod_{i\in I}A_i$가 존재한다고 가정합니다. 정의에 따라 모든 $i\in I$에 대해 $f(i)\in A_i$가 성립해야 하므로 특히 $i=i_0$에서 $f(i_0)\in A_{i_0}$입니다. 그런데 $A_{i_0}=\varnothing$은 원소를 갖지 않으므로 이는 불가능합니다. 따라서 그런 $f$는 존재하지 않고 곱은 공집합입니다. $\square$

### 2.6 특성함수

**정의.** 전체집합 $U$와 부분집합 $A\subseteq U$에 대해 **특성함수** $\chi_A:U\to\{0,1\}$을 다음으로 정의합니다.

$$
\chi_A(x)=\begin{cases}1 & (x\in A)\\ 0 & (x\notin A)\end{cases}
$$

특성함수는 집합 연산을 산술 연산으로 바꿉니다. 모든 $x\in U$에서 다음이 성립합니다.

$$
\chi_{A\cap B}=\chi_A\,\chi_B,\qquad
\chi_{A^c}=1-\chi_A
$$

$$
\chi_{A\cup B}=\chi_A+\chi_B-\chi_A\,\chi_B,\qquad
\chi_{A\setminus B}=\chi_A\,(1-\chi_B)
$$

첫 식은 곱이 $1$이 되는 경우가 두 값이 모두 $1$인 경우, 즉 $x$가 두 집합에 모두 속하는 경우뿐이라는 사실에서 나옵니다. 셋째 식에서 곱을 빼는 이유는 두 집합에 모두 속하는 원소가 두 번 세어지는 것을 보정하기 위한 것이고, 이 형태가 포함배제 원리의 두 집합 판입니다. 포함관계도 특성함수로 판정되며, $A\subseteq B$는 모든 $x\in U$에서 $\chi_A(x)\le\chi_B(x)$인 것과 같습니다.

**정리.** 대응 $A\mapsto\chi_A$는 $\mathcal{P}(U)$에서 $\{0,1\}^U$로 가는 전단사입니다.

증명을 봅니다. 단사성은 다음과 같습니다. $A\ne B$라 하면 한쪽에만 있는 원소 $x_0$가 존재하고, 그 점에서 $\chi_A(x_0)\ne\chi_B(x_0)$이므로 두 함수가 다릅니다. 대우를 취하면 $\chi_A=\chi_B$이면 $A=B$입니다. 전사성은 다음과 같습니다. 임의의 $f\in\{0,1\}^U$에 대해 $A=\{x\in U \mid f(x)=1\}$로 두면 $\chi_A=f$입니다. 따라서 대응은 전단사입니다. $\square$

이 전단사가 $\lvert\mathcal{P}(U)\rvert=2^{\lvert U\rvert}$의 구조적 이유입니다. 유한집합에서 $\lvert\{0,1\}^U\rvert=2^{\lvert U\rvert}$이므로 멱집합의 크기도 같아야 합니다. 멱집합을 $2^A$로 쓰는 표기도 여기서 나왔습니다. 부분집합을 고르는 일과 각 원소에 $0$ 또는 $1$을 배정하는 일이 같은 작업이라는 관찰이 2.1의 첫 번째 증명과 정확히 일치합니다.

> **문제 1.** (표준) $\chi_{A\cup B}=\chi_A+\chi_B-\chi_A\chi_B$를 모든 경우로 나누어 확인하십시오.
> **답.** $x$가 두 집합에 속하는지에 따라 네 경우를 따지면 양변이 항상 일치합니다.
> **풀이.** $x\in A\cap B$이면 좌변은 $1$, 우변은 $1+1-1=1$입니다. $x\in A\setminus B$이면 좌변은 $1$, 우변은 $1+0-0=1$입니다. $x\in B\setminus A$이면 좌변은 $1$, 우변은 $0+1-0=1$입니다. 두 집합에 모두 속하지 않으면 좌변은 $0$, 우변은 $0+0-0=0$입니다. 네 경우 모두 일치하므로 등식이 성립합니다. $\square$

> **문제 2.** (심화) 특성함수를 써서 $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$를 증명하십시오.
> **답.** 양변의 특성함수를 계산하면 둘 다 $\chi_A(1-\chi_B)(1-\chi_C)$가 됩니다.
> **풀이.** 좌변은 $\chi_{A\setminus(B\cup C)}=\chi_A\big(1-\chi_{B\cup C}\big)$이고 $\chi_{B\cup C}=\chi_B+\chi_C-\chi_B\chi_C$이므로 $1-\chi_{B\cup C}=(1-\chi_B)(1-\chi_C)$입니다. 따라서 좌변은 $\chi_A(1-\chi_B)(1-\chi_C)$입니다. 우변은 교집합이 곱이므로 $\chi_{A\setminus B}\,\chi_{A\setminus C}=\chi_A(1-\chi_B)\cdot\chi_A(1-\chi_C)$이고 $\chi_A^2=\chi_A$이므로 역시 $\chi_A(1-\chi_B)(1-\chi_C)$입니다. 두 특성함수가 모든 점에서 같으므로 두 집합은 상등입니다. $\square$

### 2.7 집합 연산 법칙의 일반화

3강의 이항 연산 법칙은 모두 첨수 표기로 확장됩니다. 대응 관계를 정리합니다.

| 이항 형태 | 첨수 형태 | 논리 대응 |
|---|---|---|
| $A\cup B$ | $\bigcup_{i\in I}A_i$ | $\lor$에서 $\exists$로 |
| $A\cap B$ | $\bigcap_{i\in I}A_i$ | $\land$에서 $\forall$로 |
| $(A\cup B)^c=A^c\cap B^c$ | $\big(\bigcup_i A_i\big)^c=\bigcap_i A_i^{\,c}$ | $\lnot\exists\equiv\forall\lnot$ |
| $(A\cap B)^c=A^c\cup B^c$ | $\big(\bigcap_i A_i\big)^c=\bigcup_i A_i^{\,c}$ | $\lnot\forall\equiv\exists\lnot$ |
| $B\cap(A_1\cup A_2)=(B\cap A_1)\cup(B\cap A_2)$ | $B\cap\bigcup_i A_i=\bigcup_i(B\cap A_i)$ | 상수 조건을 $\exists$ 안팎으로 이동 |
| $A\subseteq B \iff \forall x(x\in A\to x\in B)$ | $\bigcup_i A_i\subseteq B \iff \forall i\ (A_i\subseteq B)$ | 두 전체한정의 순서 교환 |

첨수의 결합·교환법칙은 표기 안으로 흡수됩니다. 첨수집합을 조각으로 나누어 $I=\bigcup_{k\in K}I_k$라 두면

$$
\bigcup_{i\in I}A_i=\bigcup_{k\in K}\ \bigcup_{i\in I_k}A_i
$$

가 성립합니다. 어느 조각에 속한 첨수를 먼저 훑든 결과가 같다는 뜻이며, 이는 존재기호의 순서를 바꿀 수 있다는 사실의 집합 판입니다.

곱집합도 합집합·교집합과 분배됩니다. $I\ne\varnothing$일 때

$$
A\times\bigcup_{i\in I}B_i=\bigcup_{i\in I}(A\times B_i),
\qquad
A\times\bigcap_{i\in I}B_i=\bigcap_{i\in I}(A\times B_i)
$$

첫 식을 증명합니다. $(x,y)$가 좌변에 속한다는 것은 $x\in A$이고 어떤 $i$에서 $y\in B_i$라는 뜻입니다. 그 $i$를 그대로 쓰면 $(x,y)\in A\times B_i$이므로 $(x,y)$는 우변에 속합니다. 역으로 $(x,y)$가 우변에 속하면 어떤 $i$에서 $(x,y)\in A\times B_i$이므로 $x\in A$이고 $y\in B_i\subseteq\bigcup_j B_j$이며, 따라서 좌변에 속합니다. 양방향 포함이 성립하므로 두 집합은 상등입니다. $\square$

> **문제 1.** (표준) $\bigcup_{i\in I}A_i\subseteq B \iff \forall i\in I\ (A_i\subseteq B)$를 증명하십시오.
> **답.** 두 조건을 모두 전체한정으로 풀어 쓰면 $\forall x\forall i$와 $\forall i\forall x$의 순서 교환이 되므로 동치입니다.
> **풀이.** 좌변은 $\forall x\big(\exists i\,(x\in A_i)\to x\in B\big)$이고, 이는 $\forall x\,\forall i\,(x\in A_i \to x\in B)$와 같습니다. 우변은 $\forall i\,\forall x\,(x\in A_i\to x\in B)$입니다. 같은 종류의 전체한정기호는 순서를 바꿀 수 있으므로 두 조건이 동치입니다. $\square$

> **문제 2.** (심화) $A\times\bigcap_{i\in I}B_i=\bigcap_{i\in I}(A\times B_i)$가 $I=\varnothing$일 때 왜 문제가 되는지 설명하십시오.
> **답.** $I=\varnothing$이면 양변의 교집합이 모두 전체집합을 가리켜야 하는데 좌우의 전체집합이 달라 등식을 논할 수 없습니다.
> **풀이.** $I=\varnothing$이면 $\bigcap_{i\in\varnothing}B_i$는 전체집합 $U$로 해석되어 좌변은 $A\times U$입니다. 반면 우변 $\bigcap_{i\in\varnothing}(A\times B_i)$는 곱집합이 놓인 전체집합, 즉 $U'\times U$ 같은 더 큰 전체집합으로 해석되어 좌변보다 큽니다. 빈 첨수집합의 교집합은 전체집합을 무엇으로 잡느냐에 따라 값이 달라지므로, 교집합을 다루는 정리에서는 $I\ne\varnothing$을 가정합니다.

## 3. 유형 총정리(치트시트)

| 유형 | 핵심 규칙 |
|---|---|
| 멱집합 정의 | $\mathcal{P}(A)=\{S\mid S\subseteq A\}$, $S\in\mathcal{P}(A)\iff S\subseteq A$ |
| 멱집합 크기 | $\lvert A\rvert=n$이면 $\lvert\mathcal{P}(A)\rvert=2^n$ |
| 빈 집합의 멱집합 | $\mathcal{P}(\varnothing)=\{\varnothing\}$으로 크기 $1$ |
| 원소와 부분집합 | $x\in A$와 $\{x\}\in\mathcal{P}(A)$를 구별한다 |
| 멱집합과 연산 | $\mathcal{P}(A\cap B)=\mathcal{P}(A)\cap\mathcal{P}(B)$, 합집합은 포함만 성립 |
| 첨수 합집합 | $\bigcup_{i\in I}A_i=\{x\mid\exists i\in I\,(x\in A_i)\}$ |
| 첨수 교집합 | $\bigcap_{i\in I}A_i=\{x\mid\forall i\in I\,(x\in A_i)\}$ |
| 빈 첨수집합 | 합집합은 $\varnothing$, 교집합은 정의되지 않으므로 $I\ne\varnothing$을 가정 |
| 일반화 드모르간 | $\big(\bigcup A_i\big)^c=\bigcap A_i^{\,c}$, $\big(\bigcap A_i\big)^c=\bigcup A_i^{\,c}$ |
| 일반화 분배 | $B\cap\bigcup A_i=\bigcup(B\cap A_i)$, $B\cup\bigcap A_i=\bigcap(B\cup A_i)$ |
| 유한 곱 | $\lvert A_1\times\cdots\times A_n\rvert=\prod\lvert A_i\rvert$, 한 자리가 비면 전체가 빈다 |
| 무한 곱 | $\prod_{i\in I}A_i=\{f:I\to\bigcup A_i \mid \forall i\,(f(i)\in A_i)\}$ |
| 함수 집합 | $B^A=\{f:A\to B\}$, 유한이면 $\lvert B^A\rvert=\lvert B\rvert^{\lvert A\rvert}$ |
| 사영 | $\pi_j(f)=f(j)$로 $j$번째 성분을 뽑는다 |
| 특성함수 | $\chi_{A\cap B}=\chi_A\chi_B$, $\chi_{A^c}=1-\chi_A$, $\chi_{A\cup B}=\chi_A+\chi_B-\chi_A\chi_B$ |
| 멱집합 전단사 | $A\mapsto\chi_A$가 $\mathcal{P}(U)\to\{0,1\}^U$의 전단사이며 $2^A$ 표기의 근거 |

## 4. 종합 문제 드릴

> **문제 1.** (기초) $A_n=\{1,2,\dots,n\}$($n\in\mathbb{N}$)일 때 $\bigcup_{n\in\mathbb{N}}A_n$과 $\bigcap_{n\in\mathbb{N}}A_n$을 구하십시오.
> **답.** 합집합은 $\mathbb{N}$, 교집합은 $\{1\}$입니다.
> **풀이.** 임의의 자연수 $k$는 $A_k$에 속하므로 합집합은 $\mathbb{N}$입니다. 교집합의 원소는 모든 $A_n$에 속해야 하는데 $A_1=\{1\}$이므로 후보는 $1$뿐이고, $1$은 모든 $A_n$에 들어 있으므로 교집합은 $\{1\}$입니다.

> **문제 2.** (표준) $\mathcal{P}(A)\subseteq\mathcal{P}(B)$이면 $A\subseteq B$임을 보이십시오.
> **답.** $A\in\mathcal{P}(A)$이므로 가정에서 $A\in\mathcal{P}(B)$, 즉 $A\subseteq B$입니다.
> **풀이.** $A\subseteq A$이므로 $A\in\mathcal{P}(A)$입니다. 가정 $\mathcal{P}(A)\subseteq\mathcal{P}(B)$에 따라 $A\in\mathcal{P}(B)$이고, 멱집합의 정의에서 이는 $A\subseteq B$를 뜻합니다. 역방향도 성립하므로 $A\subseteq B \iff \mathcal{P}(A)\subseteq\mathcal{P}(B)$입니다. $\square$

> **문제 3.** (표준) $D_n=\left[\tfrac1n,\,1\right]$($n\in\mathbb{N}$)일 때 $\bigcup_{n\in\mathbb{N}}D_n$을 구하십시오.
> **답.** $(0,1]$입니다.
> **풀이.** 임의의 $x\in(0,1]$에 대해 $\tfrac1n\le x$가 되는 자연수 $n$이 있으므로 $x\in D_n$이며 합집합에 속합니다. 반대로 각 $D_n$이 $(0,1]$에 포함되므로 합집합도 $(0,1]$에 포함됩니다. $0$은 어떤 $D_n$에도 속하지 않으므로 제외됩니다. 닫힌구간을 무한히 합집합하면 한쪽이 열린구간이 될 수 있습니다.

> **문제 4.** (표준) $U=\{1,2,3,4,5\}$, $A=\{1,3,5\}$, $B=\{3,4\}$일 때 $\chi_{A\cup B}$의 값을 특성함수 공식으로 계산하십시오.
> **답.** $\chi_{A\cup B}=(1,0,1,1,1)$로, $x=2$에서만 $0$입니다.
> **풀이.** $\chi_A=(1,0,1,0,1)$, $\chi_B=(0,0,1,1,0)$입니다. 공식 $\chi_A+\chi_B-\chi_A\chi_B$를 자리별로 계산하면 $1+0-0=1$, $0+0-0=0$, $1+1-1=1$, $0+1-0=1$, $1+0-0=1$입니다. 직접 구한 $A\cup B=\{1,3,4,5\}$의 특성함수와 일치합니다.

> **문제 5.** (표준) $A=\{1,2\}$일 때 $\prod_{i\in\{1,2\}}A_i$에서 $A_1=A$, $A_2=\varnothing$이면 곱이 무엇인지 답하십시오.
> **답.** 공집합입니다.
> **풀이.** 곱의 원소는 각 자리에 그 자리 집합의 원소를 배정한 것인데, 둘째 자리에 놓을 원소가 없습니다. 한 자리가 비면 전체 곱이 비므로 결과는 $\varnothing$입니다.

> **문제 6.** (심화) $\bigcap_{i\in I}A_i\subseteq A_j\subseteq\bigcup_{i\in I}A_i$가 모든 $j\in I$에 대해 성립함을 보이십시오.
> **답.** 교집합은 모든 자리를 요구하고 합집합은 한 자리만 요구하므로 각 $A_j$가 그 사이에 놓입니다.
> **풀이.** $x\in\bigcap_{i\in I}A_i$이면 정의에 따라 모든 $i$에서 $x\in A_i$이므로 특히 $x\in A_j$입니다. 따라서 첫 포함이 성립합니다. 또 $x\in A_j$이면 $i=j$를 증인으로 삼아 $\exists i\,(x\in A_i)$가 참이므로 $x\in\bigcup_{i\in I}A_i$입니다. 따라서 둘째 포함도 성립합니다. $\square$

> **문제 7.** (심화) $\{0,1\}^{\mathbb{N}}$의 원소와 $\mathcal{P}(\mathbb{N})$의 원소 사이의 대응을 구체적으로 서술하십시오.
> **답.** 수열 $f$에 집합 $\{n\in\mathbb{N}\mid f(n)=1\}$을 대응시키면 전단사가 됩니다.
> **풀이.** 이진 수열 $f:\mathbb{N}\to\{0,1\}$에 $A_f=\{n\mid f(n)=1\}$을 대응시킵니다. 서로 다른 수열은 어떤 자리에서 값이 다르므로 그 자리의 포함 여부가 갈려 서로 다른 집합을 주며, 따라서 단사입니다. 임의의 $A\subseteq\mathbb{N}$에 대해 $f=\chi_A$를 취하면 $A_f=A$이므로 전사입니다. 이 대응이 2.6의 전단사를 $U=\mathbb{N}$에 적용한 것이며, 10강에서 $\mathcal{P}(\mathbb{N})$의 비가산성을 보일 때 그대로 쓰입니다. $\square$

> **문제 8.** (심화) $A\times(B\cap C)=(A\times B)\cap(A\times C)$를 원소 논법으로 증명하십시오.
> **답.** 양변의 원소 조건이 모두 $x\in A \land y\in B \land y\in C$로 정리되므로 두 집합은 같습니다.
> **풀이.** $(x,y)$가 좌변에 속한다는 것은 $x\in A$이고 $y\in B\cap C$, 즉 $x\in A \land y\in B \land y\in C$입니다. $(x,y)$가 우변에 속한다는 것은 $(x\in A \land y\in B)$와 $(x\in A \land y\in C)$가 모두 성립한다는 뜻이고, 논리곱의 흡수로 정리하면 역시 $x\in A \land y\in B \land y\in C$입니다. 두 조건이 동치이므로 양방향 포함이 성립하고 두 집합은 상등입니다. $\square$

## 5. 스스로 점검

1. 멱집합의 정의를 쓰고 $S\in\mathcal{P}(A)$와 $S\subseteq A$가 같은 뜻임을 설명할 수 있는가?
2. $|\mathcal{P}(A)|=2^{|A|}$을 셈과 귀납법 두 방식으로 증명할 수 있는가?
3. 첨수 합집합과 교집합의 정의를 한정기호로 쓸 수 있는가?
4. 빈 첨수집합에서 합집합과 교집합이 왜 다르게 처리되는지 말할 수 있는가?
5. 일반화된 드모르간 법칙을 한정기호의 부정 규칙으로 유도할 수 있는가?
6. 순서 $n$쌍을 함수로 다시 보는 관점으로 무한 곱을 정의할 수 있는가?
7. 특성함수 대응이 왜 멱집합의 크기를 $2^{|U|}$로 만드는지 설명할 수 있는가?

**정답 요지.** 1. $\mathcal{P}(A)=\{S\mid S\subseteq A\}$이므로 멱집합의 원소가 되는 조건이 곧 부분집합 조건입니다. 2. 각 원소마다 넣기와 빼기 두 선택이 독립이므로 $2^n$이고, 귀납법에서는 원소 하나를 고정해 그것을 포함하는 부분집합과 포함하지 않는 부분집합으로 이분합니다. 3. 합집합은 $\exists i\in I\,(x\in A_i)$, 교집합은 $\forall i\in I\,(x\in A_i)$입니다. 4. 존재 조건은 증인이 없어 거짓이 되고 전체 조건은 공허하게 참이 되어 전체집합을 지정해야 하기 때문입니다. 5. $\lnot\exists\equiv\forall\lnot$과 $\lnot\forall\equiv\exists\lnot$을 원소 조건에 적용하면 두 등식이 나옵니다. 6. $(a_1,\dots,a_n)$을 $f(i)=a_i$인 함수로 보고 조건 $f(i)\in A_i$를 임의 첨수집합으로 확장합니다. 7. $A\mapsto\chi_A$가 $\mathcal{P}(U)$와 $\{0,1\}^U$ 사이의 전단사이고 후자의 크기가 $2^{|U|}$이기 때문입니다.
