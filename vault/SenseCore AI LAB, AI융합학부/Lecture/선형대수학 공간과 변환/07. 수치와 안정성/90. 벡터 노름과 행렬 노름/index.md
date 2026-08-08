---
title: "90. 벡터 노름과 행렬 노름"
---
# 90강. 벡터 노름과 행렬 노름

이 과목 내내 "크기"를 재 왔습니다.

62강에서 $\lVert\mathbf{v}\rVert=\sqrt{\mathbf{v}\cdot\mathbf{v}}$로 벡터의 길이를 정의했고, 82강에서 $\lVert A\mathbf{x}-\mathbf{b}\rVert$를 최소화했으며, 88강 문제 5에서 $\lVert A\rVert_{2}=\sigma_{1}$이라 썼습니다.

**그런데 "크기"가 하나가 아닙니다.**

$$\mathbf{v}=(3,-4,12)\quad\Longrightarrow\quad19,\ 13,\ 12$$

세 값이 모두 이 벡터의 크기입니다. 어느 것을 쓰느냐가 답을 바꿉니다. 82강 문제 1에서 최소제곱 대신 절댓값의 합이나 최댓값을 최소화할 수 있다고 했는데, **그 선택이 곧 노름의 선택**이었습니다.

이 강의는 **크기 재는 법을 정리**합니다. 그리고 행렬의 크기로 넘어갑니다. 행렬은 변환이므로 크기를 재는 자연스러운 방법이 하나 있습니다.

$$\lVert A\rVert=\max_{\lVert\mathbf{x}\rVert=1}\lVert A\mathbf{x}\rVert$$

**가장 많이 늘이는 배율**입니다. 91강의 조건수가 이 위에 세워집니다.

## 이 강의에서 할 수 있게 되는 것
- 세 가지 벡터 노름을 계산하고 관계를 말할 수 있습니다.
- 노름의 세 공리를 확인할 수 있습니다.
- 유도 행렬 노름을 정의하고 계산할 수 있습니다.
- 부등식들을 쓰고 언제 등호인지 압니다.
- 스펙트럼 반지름과 노름의 차이를 설명할 수 있습니다.

## 문제 1. 크기를 재는 방법이 몇 가지인가

> **문제.** $\mathbf{v}=(3,-4,12)$를 봅니다.
> (1) 성분의 절댓값을 모두 더하세요.
> (2) 제곱합의 제곱근을 구하세요.
> (3) 절댓값의 최댓값을 구하세요.

**생각의 실마리.** 세 값이 모두 "이 벡터가 얼마나 큰가"에 답합니다. **무엇을 재려느냐에 따라** 다른 것을 씁니다.

**풀이.** 검산에서

| 방식 | 값 |
|---|---|
| 절댓값의 합 | $19$ |
| 제곱합의 제곱근 | $13$ |
| 절댓값의 최댓값 | $12$ |

**언제나 이 순서**입니다. 문제 2에서 확인합니다.

**이 문제에서 배우는 것: $p$-노름.**

> **$p$-노름.** $p\ge1$에 대해
> $$\lVert\mathbf{v}\rVert_{p}=\left(\sum_{i}|v_{i}|^{p}\right)^{1/p}$$
> 이며 $p=\infty$이면 $\lVert\mathbf{v}\rVert_{\infty}=\max_{i}|v_{i}|$입니다.

세 가지가 특히 중요합니다.

| 이름 | 기호 | 뜻 |
|---|---|---|
| 맨해튼 | $\lVert\cdot\rVert_{1}$ | 격자 위를 걸은 거리 |
| 유클리드 | $\lVert\cdot\rVert_{2}$ | 직선 거리 |
| 최대 | $\lVert\cdot\rVert_{\infty}$ | 가장 큰 성분 |

**$p\to\infty$이면 최댓값으로 갑니다.** 검산에서 확인됩니다.

| $p$ | $\lVert\mathbf{v}\rVert_{p}$ |
|---|---|
| $1$ | $19.00000000$ |
| $2$ | $13.00000000$ |
| $4$ | $12.04846143$ |
| $8$ | $12.00025149$ |
| $32$ | $12.00000000$ |

**$p=32$에서 이미 최댓값 $12$와 구별되지 않습니다.** 가장 큰 성분이 지수적으로 지배하기 때문입니다.

$$\lVert\mathbf{v}\rVert_{p}=|v_{\max}|\left(\sum_{i}\Bigl|\frac{v_{i}}{v_{\max}}\Bigr|^{p}\right)^{1/p}$$

괄호 안의 항들이 $1$ 이하라 $p$가 크면 $1$만 남습니다.

**단위구의 모양**도 다릅니다.

| 노름 | $\lVert\mathbf{v}\rVert=1$ ($n=2$) |
|---|---|
| $p=1$ | 마름모 |
| $p=2$ | 원 |
| $p=\infty$ | 정사각형 |

**$p$가 커지면 마름모에서 원을 거쳐 정사각형으로** 부풀어 갑니다. 82강 심화 2의 라소가 $\ell^{1}$을 쓰는 이유가 이 모양에 있으며, 마름모의 꼭짓점이 축 위에 있어 **해가 축에 붙기 쉽습니다.**

**바로 확인 1.**

**확인 1-1.** $p$-노름의 정의를 쓰세요.

*답.* $\left(\sum|v_{i}|^{p}\right)^{1/p}$입니다.

**확인 1-2.** $p\to\infty$이면 무엇이 됩니까?

*답.* 절댓값의 최댓값입니다.

**확인 1-3.** $\ell^{1}$ 단위구의 모양을 쓰세요.

*답.* 마름모입니다.

## 문제 2. 노름이 되려면 무엇이 필요한가

> **문제.** 노름의 조건과 세 노름의 관계를 봅니다.
> (1) 노름의 공리 셋을 쓰세요.
> (2) $\lVert\mathbf{v}\rVert_{2}/\lVert\mathbf{v}\rVert_{1}$의 범위를 구하세요.
> (3) $\lVert\mathbf{v}\rVert_{\infty}/\lVert\mathbf{v}\rVert_{2}$는 어떻습니까?

**생각의 실마리.** (2)와 (3)에서 **극단적인 경우**를 생각합니다. 성분이 하나만 있을 때와 모두 같을 때입니다.

**풀이.** (1) 세 조건입니다.

$$\lVert\mathbf{v}\rVert\ge0\ \text{이고}\ =0\Leftrightarrow\mathbf{v}=\mathbf{0}$$
$$\lVert c\mathbf{v}\rVert=|c|\,\lVert\mathbf{v}\rVert$$
$$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$$

(2) $n=6$에서 검산합니다. 표본 $5000$개의 비가 $[0.410780,\ 0.804342]$이고 이론적 범위가 $[1/\sqrt6,\ 1]=[0.408248,\ 1]$입니다.

(3) 비가 $[0.465581,\ 0.989490]$이고 범위가 같습니다.

**이 문제에서 배우는 것: 노름의 공리와 동치성.**

> **노름.** 세 조건(양정치성, 동차성, 삼각부등식)을 만족하는 함수를 **노름**이라 합니다.

63강에서 내적으로 노름을 만들었는데, **모든 노름이 내적에서 오는 것은 아닙니다.** $\ell^{1}$과 $\ell^{\infty}$이 그렇습니다.

$$\text{내적에서 온 노름}\ \Longleftrightarrow\ \text{평행사변형 법칙을 만족}$$

$$\lVert\mathbf{u}+\mathbf{v}\rVert^{2}+\lVert\mathbf{u}-\mathbf{v}\rVert^{2}=2\lVert\mathbf{u}\rVert^{2}+2\lVert\mathbf{v}\rVert^{2}$$

**$\ell^{2}$만 이것을 만족**하므로, 정사영과 직교의 이론이 $\ell^{2}$에서만 성립합니다. 05단원 전체가 $\ell^{2}$를 전제한 이유입니다.

**동치성**이 중요합니다.

> **정리.** 유한차원에서 모든 노름은 **동치**입니다. 즉 상수 $c,C>0$이 있어
> $$c\lVert\mathbf{v}\rVert_{a}\le\lVert\mathbf{v}\rVert_{b}\le C\lVert\mathbf{v}\rVert_{a}$$

구체적인 상수를 정리합니다.

| 관계 | 부등식 | 등호 조건 |
|---|---|---|
| $\lVert\cdot\rVert_{2}$와 $\lVert\cdot\rVert_{1}$ | $\frac{1}{\sqrt n}\lVert\mathbf{v}\rVert_{1}\le\lVert\mathbf{v}\rVert_{2}\le\lVert\mathbf{v}\rVert_{1}$ | 왼쪽은 성분이 모두 같을 때, 오른쪽은 성분이 하나일 때 |
| $\lVert\cdot\rVert_{\infty}$와 $\lVert\cdot\rVert_{2}$ | $\frac{1}{\sqrt n}\lVert\mathbf{v}\rVert_{2}\le\lVert\mathbf{v}\rVert_{\infty}\le\lVert\mathbf{v}\rVert_{2}$ | 같습니다 |

**왼쪽 부등식이 코시-슈바르츠**입니다. 62강 심화 2에서 증명했습니다.

$$\lVert\mathbf{v}\rVert_{1}=\mathbf{1}\cdot|\mathbf{v}|\le\lVert\mathbf{1}\rVert\,\lVert\mathbf{v}\rVert_{2}=\sqrt n\,\lVert\mathbf{v}\rVert_{2}$$

**동치성이 뜻하는 것**은 "수렴이냐 발산이냐"가 노름 선택에 무관하다는 것입니다. 어느 노름으로 $0$에 가면 다른 노름으로도 갑니다.

$$\text{정성적 결론은 노름과 무관}$$

**그런데 정량적으로는 다릅니다.** 상수 $\sqrt n$이 붙으며, $n$이 크면 그 차이가 큽니다. $n=10^{6}$이면 $\sqrt n=1000$배입니다.

**무한차원에서는 동치가 아닙니다.** 71강 심화 4에서 미분이 유계가 아니라 한 것이 그 예입니다.

**바로 확인 2.**

**확인 2-1.** 노름의 세 공리를 쓰세요.

*답.* 양정치성, 동차성, 삼각부등식입니다.

**확인 2-2.** 내적에서 온 노름의 특징을 쓰세요.

*답.* 평행사변형 법칙을 만족합니다.

**확인 2-3.** 유한차원 노름의 동치성이 뜻하는 것을 쓰세요.

*답.* 수렴 여부가 노름 선택과 무관합니다.

## 문제 3. 행렬의 크기는 어떻게 재는가

> **문제.** $A=\begin{pmatrix}1&2\\ 3&-4\end{pmatrix}$를 봅니다.
> (1) $\lVert A\rVert_{1}$과 $\lVert A\rVert_{\infty}$를 구하세요.
> (2) $\lVert A\rVert_{2}$를 구하세요.
> (3) 프로베니우스 노름과 비교하세요.

**생각의 실마리.** 행렬은 변환이므로 **"얼마나 늘이는가"**로 재는 것이 자연스럽습니다.

$$\lVert A\rVert=\max_{\lVert\mathbf{x}\rVert=1}\lVert A\mathbf{x}\rVert$$

**어느 벡터 노름을 쓰느냐에 따라** 다른 행렬 노름이 나옵니다.

**풀이.** (1) 검산에서 $\lVert A\rVert_{1}=6$이고 열의 절댓값 합의 최댓값과 같습니다. $\lVert A\rVert_{\infty}=7$이고 행의 절댓값 합의 최댓값입니다.

$$\text{열 합}:\ |1|+|3|=4,\ |2|+|-4|=6\quad\Longrightarrow\quad6$$
$$\text{행 합}:\ |1|+|2|=3,\ |3|+|-4|=7\quad\Longrightarrow\quad7$$

(2) $\lVert A\rVert_{2}=5.11667274$이고 최대 특이값과 같습니다.

**표본으로도 확인**합니다. 단위원에서 $20$만 개를 뽑아 $\lVert A\mathbf{x}\rVert$의 최댓값을 재면 $5.116673$입니다.

(3) $\lVert A\rVert_{F}=5.47722558$이고 $\sqrt{\sum\sigma_{i}^{2}}$와 같습니다.

**이 문제에서 배우는 것: 유도 노름.**

> **유도 노름.** 벡터 노름 $\lVert\cdot\rVert_{p}$에 대해
> $$\lVert A\rVert_{p}=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert A\mathbf{x}\rVert_{p}}{\lVert\mathbf{x}\rVert_{p}}$$
> 를 **유도 노름**이라 합니다.

세 경우에 계산 공식이 있습니다.

| 노름 | 공식 | 기억법 |
|---|---|---|
| $\lVert A\rVert_{1}$ | 열의 절댓값 합의 최댓값 | **세로로** 더합니다 |
| $\lVert A\rVert_{\infty}$ | 행의 절댓값 합의 최댓값 | **가로로** 더합니다 |
| $\lVert A\rVert_{2}$ | $\sigma_{1}$ | 계산이 비쌉니다 |

**$1$과 $\infty$가 헷갈리기 쉽습니다.** $\lVert A\rVert_{1}$이 열이고 $\lVert A\rVert_{\infty}$가 행입니다.

이유를 봅니다. $\lVert A\mathbf{x}\rVert_{1}$을 최대로 하려면 **가장 큰 열 하나에 몰아주면** 됩니다. $\mathbf{x}=\mathbf{e}_{j}$이면 $A\mathbf{x}$가 $j$번째 열이므로

$$\lVert A\rVert_{1}=\max_{j}\lVert\mathbf{a}_{j}\rVert_{1}$$

$\lVert A\mathbf{x}\rVert_{\infty}$는 가장 큰 성분이므로, 한 행과 $\mathbf{x}$의 내적을 최대로 만듭니다. $\lVert\mathbf{x}\rVert_{\infty}\le1$에서 각 성분을 그 행의 부호에 맞추면

$$\lVert A\rVert_{\infty}=\max_{i}\lVert\mathbf{a}^{(i)}\rVert_{1}$$

**프로베니우스 노름은 유도 노름이 아닙니다.**

$$\lVert A\rVert_{F}=\sqrt{\sum_{i,j}a_{ij}^{2}}=\sqrt{\sum_{i}\sigma_{i}^{2}}$$

**성분을 벡터처럼 보고 $\ell^{2}$를 적용**한 것이며, 63강 심화 2의 행렬 내적에서 옵니다.

$$\lVert A\rVert_{F}^{2}=\operatorname{tr}(A^{\top}A)$$

**유도가 아니라는 증거**는 $\lVert I_{n}\rVert_{F}=\sqrt n$이라는 것입니다. 유도 노름이면 항등변환이 아무것도 늘이지 않으므로 $1$이어야 합니다.

| 노름 | $\lVert I_{n}\rVert$ |
|---|---|
| 유도 노름 (아무 $p$) | $1$ |
| 프로베니우스 | $\sqrt n$ |

**계산 비용**도 다릅니다.

| 노름 | 비용 |
|---|---|
| $\lVert A\rVert_{1}$, $\lVert A\rVert_{\infty}$ | $O(mn)$ |
| $\lVert A\rVert_{F}$ | $O(mn)$ |
| $\lVert A\rVert_{2}$ | SVD 필요 |

**둘째 줄이 싸기 때문에** 실무에서 $\ell^{2}$ 대신 프로베니우스를 자주 씁니다.

**바로 확인 3.**

**확인 3-1.** 유도 노름의 정의를 쓰세요.

*답.* 단위벡터를 가장 많이 늘이는 배율입니다.

**확인 3-2.** $\lVert A\rVert_{1}$과 $\lVert A\rVert_{\infty}$의 공식을 쓰세요.

*답.* 각각 열과 행의 절댓값 합의 최댓값입니다.

**확인 3-3.** 프로베니우스 노름이 유도가 아닌 증거를 쓰세요.

*답.* $\lVert I_{n}\rVert_{F}=\sqrt n\ne1$입니다.

## 문제 4. 어떤 부등식이 성립하는가

> **문제.** 무작위 $4\times4$ 행렬로 확인하세요.
> (1) $\lVert A\mathbf{x}\rVert$와 $\lVert A\rVert\lVert\mathbf{x}\rVert$
> (2) $\lVert AB\rVert$와 $\lVert A\rVert\lVert B\rVert$
> (3) $\lVert A\rVert_{2}$와 $\lVert A\rVert_{F}$

**생각의 실마리.** (1)과 (2)는 **유도 노름의 정의에서 바로** 나옵니다. 최대이므로 다른 것들은 그보다 작습니다.

**풀이.** 검산에서 확인합니다.

| 비교 | 왼쪽 | 오른쪽 |
|---|---|---|
| $\lVert A\mathbf{x}\rVert$ 대 $\lVert A\rVert_{2}\lVert\mathbf{x}\rVert$ | $2.580921$ | $6.042044$ |
| $\lVert AB\rVert_{2}$ 대 곱 | $3.894395$ | $5.510624$ |
| $\lVert A\rVert_{2}$ 대 $\lVert A\rVert_{F}$ | $2.599891$ | $3.193091$ |
| $\lVert A\rVert_{F}$ 대 $\sqrt n\lVert A\rVert_{2}$ | $3.193091$ | $5.199782$ |

**모두 왼쪽이 작거나 같습니다.**

**이 문제에서 배우는 것: 노름 부등식.**

> **부등식.**
>
> | 이름 | 식 |
> |---|---|
> | 일관성 | $\lVert A\mathbf{x}\rVert\le\lVert A\rVert\lVert\mathbf{x}\rVert$ |
> | 준곱셈성 | $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$ |
> | 노름 비교 | $\lVert A\rVert_{2}\le\lVert A\rVert_{F}\le\sqrt{r}\,\lVert A\rVert_{2}$ |

**첫째 줄이 유도 노름의 정의**입니다. 최댓값이므로 개별 $\mathbf{x}$는 그 이하입니다.

**둘째 줄의 증명**도 한 줄입니다.

$$\lVert AB\mathbf{x}\rVert\le\lVert A\rVert\lVert B\mathbf{x}\rVert\le\lVert A\rVert\lVert B\rVert\lVert\mathbf{x}\rVert$$

**두 번 적용**했습니다.

**셋째 줄이 88강의 특이값**에서 나옵니다.

$$\lVert A\rVert_{2}=\sigma_{1},\qquad\lVert A\rVert_{F}=\sqrt{\sum_{i=1}^{r}\sigma_{i}^{2}}$$

**최댓값 하나 대 전부의 제곱합**이므로 부등식이 자명합니다. 등호는 계수가 $1$일 때입니다.

**이 부등식들이 왜 중요한가.** 오차 분석의 도구이기 때문입니다.

$$\mathbf{x}\to\mathbf{x}+\Delta\mathbf{x}\quad\Longrightarrow\quad\lVert A\Delta\mathbf{x}\rVert\le\lVert A\rVert\lVert\Delta\mathbf{x}\rVert$$

**입력 오차가 출력에 얼마나 전달되는지**의 상한을 줍니다. 91강에서 이것을 조건수로 정리합니다.

**준곱셈성이 없으면 곤란합니다.** 여러 단계의 계산에서 오차를 누적할 수 없기 때문입니다. **프로베니우스 노름도 준곱셈적**이라 이 용도로 쓸 수 있습니다.

$$\lVert AB\rVert_{F}\le\lVert A\rVert_{F}\lVert B\rVert_{F}$$

**바로 확인 4.**

**확인 4-1.** 일관성 부등식을 쓰세요.

*답.* $\lVert A\mathbf{x}\rVert\le\lVert A\rVert\lVert\mathbf{x}\rVert$입니다.

**확인 4-2.** 준곱셈성의 증명을 한 줄로 쓰세요.

*답.* 일관성을 두 번 적용합니다.

**확인 4-3.** $\lVert A\rVert_{2}$와 $\lVert A\rVert_{F}$의 관계를 쓰세요.

*답.* $\lVert A\rVert_{2}\le\lVert A\rVert_{F}\le\sqrt r\lVert A\rVert_{2}$입니다.

## 문제 5. 고유값의 크기가 노름인가

> **문제.** 다음을 비교하세요.
> (1) $N=\begin{pmatrix}0&5\\ 0&0\end{pmatrix}$의 스펙트럼 반지름과 노름
> (2) $S=\begin{pmatrix}4&1\\ 1&3\end{pmatrix}$은 어떻습니까?
> (3) 거듭제곱의 거동을 비교하세요.

**생각의 실마리.** 84강 부록에서 **스펙트럼 반지름**을 고유값 크기의 최댓값이라 했습니다. 노름과 같은지 봅니다.

**풀이.** (1) 검산에서 스펙트럼 반지름이 $0$이고 노름이 $5$입니다. **완전히 다릅니다.**

멱영행렬이라 고유값이 $0$뿐인데, 실제로는 벡터를 $5$배로 늘입니다.

(2) 대칭이면 둘 다 $4.618034$로 같습니다.

(3) 두 행렬로 거듭제곱을 봅니다.

$M=\begin{pmatrix}0&0.9\\ 0.9&0\end{pmatrix}$는 대칭이고 $\rho=0.9$입니다.

| $k$ | $\lVert M^{k}\rVert_{2}$ | $\rho^{k}$ |
|---|---|---|
| $1$ | $0.90000000$ | $0.90000000$ |
| $5$ | $0.59049000$ | $0.59049000$ |
| $20$ | $0.12157665$ | $0.12157665$ |
| $60$ | $0.00179701$ | $0.00179701$ |

**정확히 같습니다.**

$G=\begin{pmatrix}0.5&10\\ 0&0.5\end{pmatrix}$는 결손이고 $\rho=0.5$입니다.

| $k$ | $\lVert G^{k}\rVert_{2}$ | $\rho^{k}$ |
|---|---|---|
| $1$ | $1.0025\times10^{1}$ | $5.0000\times10^{-1}$ |
| $3$ | $7.5021\times10^{0}$ | $1.2500\times10^{-1}$ |
| $10$ | $1.9532\times10^{-1}$ | $9.7656\times10^{-4}$ |
| $40$ | $7.2760\times10^{-10}$ | $9.0949\times10^{-13}$ |

**$k=1$에서 노름이 $20$배 크고, $k=40$에서도 $800$배 차이**가 남습니다.

**이 문제에서 배우는 것: 스펙트럼 반지름과 노름.**

> **스펙트럼 반지름.** $\rho(A)=\max_{i}|\lambda_{i}|$이며 언제나
> $$\rho(A)\le\lVert A\rVert$$
> 입니다. **대칭이면 $\rho(A)=\lVert A\rVert_{2}$**입니다.

**부등식의 증명**은 짧습니다. $A\mathbf{v}=\lambda\mathbf{v}$이면

$$|\lambda|\lVert\mathbf{v}\rVert=\lVert A\mathbf{v}\rVert\le\lVert A\rVert\lVert\mathbf{v}\rVert$$

**등호가 언제인가**를 정리합니다.

| 행렬 | $\rho$와 $\lVert\cdot\rVert_{2}$ |
|---|---|
| 대칭 | 같습니다 |
| 정규 ($A^{*}A=AA^{*}$) | 같습니다 |
| 일반 | $\rho<\lVert A\rVert_{2}$일 수 있습니다 |
| 멱영 | $\rho=0$인데 노름은 양수 |

**둘째 줄이 86강 심화 2의 정규행렬**입니다. 유니터리 대각화되면 노름이 고유값의 크기로 정해집니다.

**$k\to\infty$의 거동은 $\rho$가 결정합니다.**

> **겔판트 공식.**
> $$\lim_{k\to\infty}\lVert A^{k}\rVert^{1/k}=\rho(A)$$

검산에서 $G$에 대해 확인합니다.

| $k$ | $\lVert G^{k}\rVert^{1/k}$ | $\rho$ |
|---|---|---|
| $1$ | $10.02493781$ | $0.50000000$ |
| $5$ | $1.25596833$ | $0.50000000$ |
| $20$ | $0.67464163$ | $0.50000000$ |
| $80$ | $0.54830412$ | $0.50000000$ |
| $200$ | $0.52117108$ | $0.50000000$ |

**천천히 수렴합니다.** $k=200$에서도 $0.521$이며, 결손 행렬이라 $k^{m-1}$ 인자가 붙어 느립니다. 85강 문제 5에서 본 대로입니다.

$$\lVert G^{k}\rVert\approx C\,k\,\rho^{k}\quad\Longrightarrow\quad\lVert G^{k}\rVert^{1/k}\approx\rho\,k^{1/k}\to\rho$$

**실무적 함의**가 중요합니다.

| 묻는 것 | 보는 것 |
|---|---|
| 장기적으로 수렴하는가 | $\rho<1$ |
| 매 단계 줄어드는가 | $\lVert A\rVert<1$ |
| 초기에 커지는가 | $\lVert A\rVert>1$인데 $\rho<1$ |

**셋째 줄이 과도 증폭**입니다. 결국은 수렴하지만 중간에 크게 부풀 수 있습니다. $G$에서 $k=3$일 때 노름이 $7.5$까지 갔습니다.

**246강의 그래디언트 폭발**이 이 현상입니다. 스펙트럼 반지름만 보면 안전해 보이는데 실제로는 중간에 터집니다.

**바로 확인 5.**

**확인 5-1.** 스펙트럼 반지름과 노름의 부등식을 쓰세요.

*답.* $\rho(A)\le\lVert A\rVert$입니다.

**확인 5-2.** 등호가 성립하는 경우를 쓰세요.

*답.* 대칭이거나 정규행렬일 때입니다.

**확인 5-3.** 겔판트 공식을 쓰세요.

*답.* $\lim_{k}\lVert A^{k}\rVert^{1/k}=\rho(A)$입니다.

## 유형 총정리(치트시트)

| 벡터 노름 | 정의 |
|---|---|
| $\lVert\mathbf{v}\rVert_{1}$ | 절댓값의 합 |
| $\lVert\mathbf{v}\rVert_{2}$ | 제곱합의 제곱근 |
| $\lVert\mathbf{v}\rVert_{\infty}$ | 절댓값의 최댓값 |
| 공리 | 양정치, 동차, 삼각부등식 |

| 행렬 노름 | 계산 |
|---|---|
| $\lVert A\rVert_{1}$ | 열 절댓값 합의 최댓값 |
| $\lVert A\rVert_{\infty}$ | 행 절댓값 합의 최댓값 |
| $\lVert A\rVert_{2}$ | $\sigma_{1}$ |
| $\lVert A\rVert_{F}$ | $\sqrt{\sum\sigma_{i}^{2}}=\sqrt{\operatorname{tr}(A^{\top}A)}$ |

| 부등식 | |
|---|---|
| 일관성 | $\lVert A\mathbf{x}\rVert\le\lVert A\rVert\lVert\mathbf{x}\rVert$ |
| 준곱셈 | $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$ |
| 비교 | $\lVert A\rVert_{2}\le\lVert A\rVert_{F}\le\sqrt r\lVert A\rVert_{2}$ |
| 스펙트럼 | $\rho(A)\le\lVert A\rVert$ |

| 자주 하는 실수 | 바로잡기 |
|---|---|
| $\lVert A\rVert_{1}$을 행으로 셉니다 | 열입니다 |
| 프로베니우스를 유도 노름이라 합니다 | $\lVert I\rVert_{F}=\sqrt n$입니다 |
| $\rho$를 노름이라 합니다 | 멱영에서 $0$과 양수로 갈립니다 |
| $\rho<1$이면 안전하다고 봅니다 | 중간에 부풀 수 있습니다 |

## 종합 문제 드릴

> **문제 6.** $(1,-2,2)$의 세 노름을 구하세요.

*답.* $5$, $3$, $2$입니다.

> **문제 7.** $p\to\infty$의 극한을 쓰세요.

*답.* 절댓값의 최댓값입니다.

> **문제 8.** 노름의 세 공리를 쓰세요.

*답.* 양정치성, 동차성, 삼각부등식입니다.

> **문제 9.** 내적에서 온 노름의 특징을 쓰세요.

*답.* 평행사변형 법칙을 만족합니다.

> **문제 10.** 유한차원 노름의 동치성을 쓰세요.

*답.* 두 노름이 상수배 범위로 서로를 감쌉니다.

> **문제 11.** 유도 노름의 정의를 쓰세요.

*답.* 단위벡터를 가장 많이 늘이는 배율입니다.

> **문제 12.** $\begin{pmatrix}2&-1\\ 3&4\end{pmatrix}$의 $\lVert\cdot\rVert_{1}$과 $\lVert\cdot\rVert_{\infty}$를 구하세요.

*답.* 열 합이 $5,5$이므로 $5$이고, 행 합이 $3,7$이므로 $7$입니다.

> **문제 13.** $\lVert A\rVert_{2}$를 특이값으로 쓰세요.

*답.* $\sigma_{1}$입니다.

> **문제 14.** 프로베니우스 노름을 두 가지로 쓰세요.

*답.* $\sqrt{\sum a_{ij}^{2}}$이고 $\sqrt{\operatorname{tr}(A^{\top}A)}$입니다.

> **문제 15.** $\lVert I_{n}\rVert_{F}$를 쓰세요.

*답.* $\sqrt n$입니다.

> **문제 16.** 준곱셈성을 쓰세요.

*답.* $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$입니다.

> **문제 17.** 스펙트럼 반지름과 노름의 관계를 쓰세요.

*답.* $\rho(A)\le\lVert A\rVert$이며 대칭이면 같습니다.

> **문제 18.** $\rho<1$인데 초기에 커질 수 있는 이유를 쓰세요.

*답.* 결손이거나 비정규이면 $\lVert A\rVert>1$일 수 있습니다.

## 심화 문제

> **심화 1.** 노름 동치성의 상수를 구하고 증명하세요.

*풀이.* 문제 2에서 관측한 범위를 증명합니다.

**$\lVert\mathbf{v}\rVert_{2}\le\lVert\mathbf{v}\rVert_{1}$.** 제곱하면

$$\lVert\mathbf{v}\rVert_{1}^{2}=\left(\sum|v_{i}|\right)^{2}=\sum_{i}v_{i}^{2}+2\sum_{i<j}|v_{i}||v_{j}|\ge\lVert\mathbf{v}\rVert_{2}^{2}$$

**교차항이 음이 아니기 때문**입니다. 등호는 성분이 하나만 $0$이 아닐 때입니다.

**$\lVert\mathbf{v}\rVert_{1}\le\sqrt n\lVert\mathbf{v}\rVert_{2}$.** 코시-슈바르츠를 $\mathbf{1}$과 $|\mathbf{v}|$에 적용합니다.

$$\sum_{i}|v_{i}|=\mathbf{1}\cdot|\mathbf{v}|\le\lVert\mathbf{1}\rVert_{2}\lVert\mathbf{v}\rVert_{2}=\sqrt n\lVert\mathbf{v}\rVert_{2}$$

**등호는 $|\mathbf{v}|$가 $\mathbf{1}$과 평행할 때**, 즉 모든 성분의 절댓값이 같을 때입니다.

**$\lVert\mathbf{v}\rVert_{\infty}\le\lVert\mathbf{v}\rVert_{2}\le\sqrt n\lVert\mathbf{v}\rVert_{\infty}$.** 왼쪽은 한 항만 남기는 것이고, 오른쪽은 모든 항을 최댓값으로 바꾸는 것입니다.

정리합니다.

| 부등식 | 상수 | 등호 조건 |
|---|---|---|
| $\lVert\cdot\rVert_{\infty}\le\lVert\cdot\rVert_{2}\le\lVert\cdot\rVert_{1}$ | $1$ | 성분이 하나 |
| $\lVert\cdot\rVert_{1}\le\sqrt n\lVert\cdot\rVert_{2}$ | $\sqrt n$ | 성분이 모두 같음 |
| $\lVert\cdot\rVert_{2}\le\sqrt n\lVert\cdot\rVert_{\infty}$ | $\sqrt n$ | 성분이 모두 같음 |

**차원이 커지면 상수가 커집니다.** $n=10^{6}$이면 $\sqrt n=1000$이며, 73강 심화 4에서 본 고차원의 현상과 이어집니다.

**동치성의 일반 증명**도 봅니다. 유한차원에서 단위구가 컴팩트이고 노름이 연속이므로, 그 위에서 최댓값과 최솟값을 가집니다. **그 두 값이 상수 $c,C$**입니다.

$$c=\min_{\lVert\mathbf{v}\rVert_{a}=1}\lVert\mathbf{v}\rVert_{b},\qquad C=\max_{\lVert\mathbf{v}\rVert_{a}=1}\lVert\mathbf{v}\rVert_{b}$$

**컴팩트성이 유한차원에서만 성립**하므로, 무한차원에서는 이 논증이 무너집니다.

> **심화 2.** 유도 노름의 계산 공식을 증명하세요.

*풀이.* 문제 3에서 제시한 공식을 유도합니다.

**$\lVert A\rVert_{1}=\max_{j}\sum_{i}|a_{ij}|$.**

**상한.** $\mathbf{x}$를 열의 결합으로 보면

$$\lVert A\mathbf{x}\rVert_{1}=\left\lVert\sum_{j}x_{j}\mathbf{a}_{j}\right\rVert_{1}\le\sum_{j}|x_{j}|\lVert\mathbf{a}_{j}\rVert_{1}\le\left(\max_{j}\lVert\mathbf{a}_{j}\rVert_{1}\right)\lVert\mathbf{x}\rVert_{1}$$

**달성.** 최대인 열의 인덱스를 $j^{*}$라 하고 $\mathbf{x}=\mathbf{e}_{j^{*}}$로 두면 등호입니다.

**$\lVert A\rVert_{\infty}=\max_{i}\sum_{j}|a_{ij}|$.**

**상한.** $i$번째 성분이

$$\left|\sum_{j}a_{ij}x_{j}\right|\le\sum_{j}|a_{ij}||x_{j}|\le\left(\sum_{j}|a_{ij}|\right)\lVert\mathbf{x}\rVert_{\infty}$$

**달성.** 최대인 행 $i^{*}$에 대해 $x_{j}=\operatorname{sgn}(a_{i^{*}j})$로 두면 $\lVert\mathbf{x}\rVert_{\infty}=1$이고 등호입니다.

**$\lVert A\rVert_{2}=\sigma_{1}$.** 88강 문제 5에서 봤습니다. 86강 심화 1의 레일리 몫으로 증명합니다.

$$\lVert A\mathbf{x}\rVert^{2}=\mathbf{x}^{\top}A^{\top}A\mathbf{x}\le\lambda_{\max}(A^{\top}A)\lVert\mathbf{x}\rVert^{2}=\sigma_{1}^{2}\lVert\mathbf{x}\rVert^{2}$$

**등호는 $\mathbf{x}=\mathbf{v}_{1}$일 때**입니다.

**전치와의 관계**도 정리합니다.

| 노름 | $\lVert A^{\top}\rVert$ |
|---|---|
| $\lVert\cdot\rVert_{1}$ | $\lVert A\rVert_{\infty}$ |
| $\lVert\cdot\rVert_{\infty}$ | $\lVert A\rVert_{1}$ |
| $\lVert\cdot\rVert_{2}$ | $\lVert A\rVert_{2}$ |
| $\lVert\cdot\rVert_{F}$ | $\lVert A\rVert_{F}$ |

**첫 두 줄이 서로 바뀝니다.** 행과 열이 뒤집히기 때문입니다. 셋째 줄은 88강에서 $A$와 $A^{\top}$의 특이값이 같아서입니다.

**유용한 부등식**도 있습니다.

$$\lVert A\rVert_{2}\le\sqrt{\lVert A\rVert_{1}\lVert A\rVert_{\infty}}$$

**싼 두 노름으로 비싼 것의 상한**을 얻습니다. SVD 없이 $\lVert A\rVert_{2}$를 어림할 때 씁니다. 검산의 $A$에서 $\sqrt{6\cdot7}=6.48$이고 실제 $\lVert A\rVert_{2}=5.12$입니다.

> **심화 3.** 노름 선택이 최적화에서 어떤 차이를 내는지 논하세요.

*풀이.* 82강 문제 1에서 세 기준을 나열했습니다. **노름의 언어로 다시 봅니다.**

$$\min_{\mathbf{x}}\lVert A\mathbf{x}-\mathbf{b}\rVert_{p}$$

| $p$ | 이름 | 성질 |
|---|---|---|
| $2$ | 최소제곱 | 닫힌 해, 이상치에 민감 |
| $1$ | 최소절대편차 | 선형계획, 강건 |
| $\infty$ | 체비셰프 | 선형계획, 최악 관리 |

**$p=2$만 선형대수로 풀립니다.** 나머지는 미분 불가능한 점이 있어 다른 도구가 필요합니다.

**왜 $\ell^{1}$이 강건한가.** 손실함수의 기울기를 봅니다.

| 손실 | 큰 잔차에서의 기울기 |
|---|---|
| $r^{2}$ | $2r$ (선형 증가) |
| $\lvert r\rvert $ | $\pm1$ (일정) |

**제곱은 큰 잔차에 무한정 끌려가고 절댓값은 그렇지 않습니다.** 이상치 하나가 답을 통째로 옮기는 것을 막습니다.

**정칙화에서도 노름 선택이 중요합니다.**

$$\min\lVert A\mathbf{x}-\mathbf{b}\rVert_{2}^{2}+\lambda\lVert\mathbf{x}\rVert_{p}^{p}$$

| $p$ | 이름 | 효과 |
|---|---|---|
| $2$ | 능형 | 계수를 줄입니다 |
| $1$ | 라소 | 계수를 $0$으로 만듭니다 |

**왜 $\ell^{1}$이 희소성을 주는가.** 문제 1에서 본 단위구의 모양 때문입니다.

$$\ell^{1}\text{의 단위구는 마름모}$$

**꼭짓점이 축 위에 있고 뾰족합니다.** 제약 집합과 손실 등고선이 만나는 점이 꼭짓점이 되기 쉬우며, 그 점에서는 성분 일부가 정확히 $0$입니다.

$\ell^{2}$의 단위구는 원이라 꼭짓점이 없고, 접점이 축 위일 확률이 $0$입니다.

$$\text{모서리가 있으면 희소해집니다}$$

**82강 심화 2에서 라소를 언급**했는데, 그 기하적 이유가 이것입니다.

**신경망에서도** 노름이 선택 사항입니다.

| 용도 | 흔한 노름 |
|---|---|
| 회귀 손실 | $\ell^{2}$ |
| 강건 회귀 | 후버 (둘의 절충) |
| 가중치 감쇠 | $\ell^{2}$ |
| 희소화 | $\ell^{1}$ |
| 그래디언트 클리핑 | $\ell^{2}$ |

**둘째 줄의 후버 손실**은 작은 잔차에 제곱, 큰 잔차에 절댓값을 씁니다. 미분 가능하면서 강건합니다.

> **심화 4.** 조건수의 예고로 오차 전파를 다루세요.

*풀이.* 문제 4의 부등식이 무엇에 쓰이는지 봅니다.

**정방향 전파.** $\mathbf{y}=A\mathbf{x}$에서 입력에 오차가 있으면

$$\lVert\Delta\mathbf{y}\rVert=\lVert A\Delta\mathbf{x}\rVert\le\lVert A\rVert\lVert\Delta\mathbf{x}\rVert$$

**상대오차로 바꿉니다.**

$$\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert}\le\lVert A\rVert\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{y}\rVert}=\lVert A\rVert\frac{\lVert\mathbf{x}\rVert}{\lVert\mathbf{y}\rVert}\cdot\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}$$

$\lVert\mathbf{x}\rVert=\lVert A^{-1}\mathbf{y}\rVert\le\lVert A^{-1}\rVert\lVert\mathbf{y}\rVert$이므로

$$\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert}\le\underbrace{\lVert A\rVert\lVert A^{-1}\rVert}_{\kappa(A)}\cdot\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}$$

**조건수가 나타났습니다.** 91강의 주제이며, 여기서 정의만 봅니다.

$$\kappa(A)=\lVert A\rVert\lVert A^{-1}\rVert$$

**$\ell^{2}$에서 특이값으로 표현됩니다.**

$$\lVert A\rVert_{2}=\sigma_{1},\qquad\lVert A^{-1}\rVert_{2}=\frac{1}{\sigma_{n}}\quad\Longrightarrow\quad\kappa_{2}(A)=\frac{\sigma_{1}}{\sigma_{n}}$$

**88강 문제 5에서 쓴 식**이 여기서 유도됩니다.

**둘째 줄의 근거**는 $A^{-1}=V\Sigma^{-1}U^{\top}$이고 $\Sigma^{-1}$의 최대 성분이 $1/\sigma_{n}$이기 때문입니다.

**언제나 $\kappa\ge1$**입니다.

$$1=\lVert I\rVert=\lVert AA^{-1}\rVert\le\lVert A\rVert\lVert A^{-1}\rVert=\kappa(A)$$

**준곱셈성을 썼습니다.** 등호는 직교행렬일 때이며, 75강 심화 4에서 $\kappa(Q)=1$이라 한 근거입니다.

**노름마다 조건수가 다릅니다.**

| 노름 | 표기 |
|---|---|
| $\ell^{1}$ | $\kappa_{1}$ |
| $\ell^{2}$ | $\kappa_{2}=\sigma_{1}/\sigma_{n}$ |
| $\ell^{\infty}$ | $\kappa_{\infty}$ |

**동치성 때문에 서로 $n$배 이내**로 다릅니다. 그래서 "조건수가 크다"는 판단은 노름과 무관하지만, 정확한 값은 다릅니다.

**실무에서는 $\kappa_{1}$을 어림합니다.** $\lVert A^{-1}\rVert_{1}$을 역행렬 없이 추정하는 알고리즘이 있어 $O(n^{2})$에 끝나며, $\kappa_{2}$는 SVD가 필요해 비쌉니다.

> **심화 5.** 노름이 나타나는 자리를 정리하세요.

*풀이.* 이 개념이 어디서 쓰이는지 봅니다.

**최적화의 손실.** 심화 3에서 다뤘습니다.

**수렴 판정.** 반복법에서 $\lVert\mathbf{x}_{k+1}-\mathbf{x}_{k}\rVert<\varepsilon$을 정지 조건으로 씁니다. **상대 기준이 나은 경우**가 많습니다.

$$\frac{\lVert\mathbf{x}_{k+1}-\mathbf{x}_{k}\rVert}{\lVert\mathbf{x}_{k}\rVert}<\varepsilon$$

**규모가 다른 문제에서 절대 기준은 위험**합니다.

**정칙화.** 가중치 감쇠가 $\lVert\mathbf{w}\rVert_{2}^{2}$이고, 233강에서 다룹니다.

**그래디언트 클리핑.** 노름이 문턱을 넘으면 줄입니다.

$$\mathbf{g}\leftarrow\mathbf{g}\cdot\min\left(1,\frac{\tau}{\lVert\mathbf{g}\rVert}\right)$$

**방향은 유지하고 크기만 제한**합니다. 246강의 그래디언트 폭발 대응입니다.

**립시츠 상수.** 함수가 얼마나 급하게 변하는지 재는 양이며

$$\lVert f(\mathbf{x})-f(\mathbf{y})\rVert\le L\lVert\mathbf{x}-\mathbf{y}\rVert$$

입니다. **선형사상이면 $L=\lVert A\rVert$**입니다. 신경망의 강건성 분석에서 각 층의 노름을 곱해 상한을 얻습니다.

$$L\le\prod_{\ell}\lVert W_{\ell}\rVert$$

**준곱셈성**을 쓴 것이며, 느슨하지만 계산이 쉽습니다.

**저계수 근사의 오차.** 88강 심화 2에서 두 노름으로 표현했습니다.

$$\lVert A-A_{k}\rVert_{2}=\sigma_{k+1},\qquad\lVert A-A_{k}\rVert_{F}=\sqrt{\sum_{i>k}\sigma_{i}^{2}}$$

**어느 노름에서도 절단 SVD가 최선**이라는 것이 에카르트-영의 강한 형태입니다.

정리합니다.

| 분야 | 노름이 하는 일 |
|---|---|
| 최적화 | 손실과 정칙화 |
| 수치해석 | 오차와 수렴 판정 |
| 학습 | 클리핑, 감쇠 |
| 이론 | 립시츠 상수, 근사 오차 |

> **심화 6.** 07단원 전체를 예고하세요.

*풀이.* 이 단원이 무엇을 하는지 정리합니다.

**이 과목 내내 경고가 반복됐습니다.**

| 강의 | 경고 |
|---|---|
| 45 | 파국적 상쇄 |
| 67 | 피벗팅 없으면 무너집니다 |
| 69 | 역행렬로 풀지 마세요 |
| 78 | 행렬식이 넘칩니다 |
| 80 | 고전 그람슈미트가 불안정합니다 |
| 81 | 정규방정식이 조건수를 제곱합니다 |
| 85 | 대각화가 위험할 수 있습니다 |
| 88 | $A^{\top}A$를 만들지 마세요 |

**여덟 번의 경고에 공통된 것**이 있습니다. **수학적으로 옳은 식이 부동소수점에서 무너진다**는 것입니다.

07단원이 그 현상을 정리합니다.

| 강의 | 내용 |
|---|---|
| 90 (이 강의) | 크기를 재는 도구 |
| 91 | 조건수와 오차 증폭 |
| 92 | 부동소수점의 실제 규칙 |

**91강이 핵심**입니다. 67강 심화 6에서 "안정성은 알고리즘의 성질이고 조건은 문제의 성질"이라 구별했는데, 그것을 정확히 정의하고 증명합니다.

$$\frac{\text{출력 상대오차}}{\text{입력 상대오차}}\le\kappa(A)$$

**92강은 하드웨어**를 다룹니다. 부동소수점이 실수를 어떻게 표현하고, 어디서 정보가 사라지며, 어떤 코딩 습관이 그것을 피하는지 봅니다.

$$\text{이 단원이 끝나면 S4가 완결됩니다}$$

62강에서 벡터를 정의하고 시작해, 행렬을 변환으로 읽고, 공간과 좌표를 세우고, 분해로 계산하고, 마지막에 그 계산이 얼마나 믿을 만한지 재는 데까지 왔습니다.

## 코드 검산

이 강의에서는 numpy만 씁니다. 세 벡터 노름과 극한을 확인하고, 유도 노름의 공식을 표본으로 검증하며, 스펙트럼 반지름과 노름이 다른 경우를 봅니다.

```python
import numpy as np

# --- 문제 1: 세 벡터 노름과 p 의 극한 -----------------------------------
v = np.array([3.,-4.,12.])
print("%.8f %.8f %.8f" % (np.abs(v).sum(), np.linalg.norm(v), np.abs(v).max()))
# 19.00000000 13.00000000 12.00000000
for p in [1,2,4,8,32,128]:
    print(p, "%.8f" % float(np.sum(np.abs(v)**p)**(1/p)))
# 1 19.00000000
# 2 13.00000000
# 4 12.04846143
# 8 12.00025149
# 32 12.00000000
# 128 12.00000000        <- 최댓값으로 수렴합니다

# --- 문제 2: 노름 동치성의 상수 ------------------------------------------
rng = np.random.default_rng(81)
n = 6
X = rng.standard_normal((5000,n))
r1 = np.abs(X).sum(axis=1); r2 = np.linalg.norm(X,axis=1); ri = np.abs(X).max(axis=1)
print("%.6f %.6f" % ((r2/r1).min(), (r2/r1).max()),
      "%.6f %.6f" % (1/np.sqrt(n), 1.0))
# 0.410780 0.804342 0.408248 1.000000
print("%.6f %.6f" % ((ri/r2).min(), (ri/r2).max()),
      "%.6f %.6f" % (1/np.sqrt(n), 1.0))
# 0.465581 0.989490 0.408248 1.000000     (이론 범위 안에 있습니다)

# --- 문제 3: 유도 노름의 공식 -------------------------------------------
A = np.array([[1.,2.],[3.,-4.]])
print("%.8f %.8f" % (np.linalg.norm(A,1), np.abs(A).sum(axis=0).max()))
# 6.00000000 6.00000000     (열 합의 최댓값)
print("%.8f %.8f" % (np.linalg.norm(A,np.inf), np.abs(A).sum(axis=1).max()))
# 7.00000000 7.00000000     (행 합의 최댓값)
s = np.linalg.svd(A, compute_uv=False)
print("%.8f %.8f" % (np.linalg.norm(A,2), s[0]))
# 5.11667274 5.11667274
print("%.8f %.8f" % (np.linalg.norm(A,'fro'), np.sqrt(np.sum(s**2))))
# 5.47722558 5.47722558
T = rng.standard_normal((200000,2))                 # 단위원에서 최대 늘임
T = T/np.linalg.norm(T,axis=1,keepdims=True)
print("%.6f %.6f" % (np.linalg.norm(T@A.T,axis=1).max(), s[0]))
# 5.116673 5.116673

# --- 문제 4: 부등식 -----------------------------------------------------
B = rng.standard_normal((4,4)); C = rng.standard_normal((4,4))
x = rng.standard_normal(4)
print("%.6f %.6f" % (np.linalg.norm(B@x), np.linalg.norm(B,2)*np.linalg.norm(x)))
# 2.580921 6.042044          (일관성)
print("%.6f %.6f" % (np.linalg.norm(B@C,2), np.linalg.norm(B,2)*np.linalg.norm(C,2)))
# 3.894395 5.510624          (준곱셈성)
print("%.6f %.6f" % (np.linalg.norm(B,2), np.linalg.norm(B,'fro')))
# 2.599891 3.193091
print("%.6f %.6f" % (np.linalg.norm(B,'fro'), np.sqrt(4)*np.linalg.norm(B,2)))
# 3.193091 5.199782

# --- 문제 5: 스펙트럼 반지름은 노름이 아닙니다 --------------------------
N = np.array([[0.,5.],[0.,0.]])                     # 멱영
print("%.6f %.6f" % (max(abs(np.linalg.eigvals(N))), np.linalg.norm(N,2)))
# 0.000000 5.000000          <- 완전히 다릅니다
S = np.array([[4.,1.],[1.,3.]])                     # 대칭
print("%.6f %.6f" % (max(abs(np.linalg.eigvalsh(S))), np.linalg.norm(S,2)))
# 4.618034 4.618034          <- 같습니다
M = np.array([[0.,0.9],[0.9,0.]])                   # 대칭, rho = 0.9
rho = max(abs(np.linalg.eigvals(M)))
for k in [1,5,20,60]:
    print(k, "%.8f %.8f" % (np.linalg.norm(np.linalg.matrix_power(M,k),2), rho**k))
# 1 0.90000000 0.90000000
# 5 0.59049000 0.59049000
# 20 0.12157665 0.12157665
# 60 0.00179701 0.00179701
G = np.array([[0.5,10.],[0.,0.5]])                  # 결손, rho = 0.5
rg = max(abs(np.linalg.eigvals(G)))
for k in [1,3,10,40]:
    print(k, "%.4e %.4e" % (np.linalg.norm(np.linalg.matrix_power(G,k),2), rg**k))
# 1 1.0025e+01 5.0000e-01
# 3 7.5021e+00 1.2500e-01
# 10 1.9532e-01 9.7656e-04
# 40 7.2760e-10 9.0949e-13     <- 40 번 뒤에도 800 배 차이가 납니다

# --- 심화: 겔판트 공식은 천천히 수렴합니다 ------------------------------
for k in [1,5,20,80,200]:
    nk = np.linalg.norm(np.linalg.matrix_power(G,k),2)
    print(k, "%.8f %.8f" % (nk**(1/k), rg))
# 1 10.02493781 0.50000000
# 5 1.25596833 0.50000000
# 20 0.67464163 0.50000000
# 80 0.54830412 0.50000000
# 200 0.52117108 0.50000000
```

실행하면 주석과 같은 값이 나옵니다. 다섯 곳을 짚어 둡니다.

첫째, 같은 벡터의 크기가 $19$, $13$, $12$로 다릅니다. 그리고 $p$를 키우면 **$p=32$에서 이미 최댓값 $12$와 구별되지 않습니다.**

둘째, 노름 비의 표본 범위가 이론값 $[1/\sqrt6,\ 1]=[0.408,\ 1]$ 안에 있습니다. 상한에는 거의 닿는데($0.99$) 하한에는 덜 닿습니다. **모든 성분의 절댓값이 같아야 하한이 달성되므로** 무작위로는 잘 나오지 않습니다.

셋째, 유도 노름의 공식이 정확히 맞습니다. **$\lVert A\rVert_{1}=6$이 열 합이고 $\lVert A\rVert_{\infty}=7$이 행 합**입니다. 그리고 단위원에서 $20$만 개를 뽑아 잰 최대 늘임이 $\sigma_{1}$과 소수 여섯 자리까지 같습니다.

넷째, 세 부등식이 모두 성립합니다. 일관성에서 $2.58\le6.04$인데, **$\mathbf{x}$가 $\mathbf{v}_{1}$ 방향이 아니라 여유가 큽니다.**

다섯째가 이 강의의 핵심 경고입니다. 멱영행렬에서 **스펙트럼 반지름이 $0$인데 노름이 $5$**입니다. 대칭행렬에서는 둘이 같습니다. 그리고 결손 행렬 $G$에서 $k=40$까지 가도 노름이 $\rho^{k}$의 $800$배입니다. **$\rho<1$이라고 안심하면 안 됩니다.**

겔판트 공식의 수렴도 느립니다. $k=200$에서 $0.521$로 아직 $\rho=0.5$에 못 미칩니다.

코드로 할 수 없는 일도 분명히 해 둡니다. **유도 노름의 공식은 표본으로 증명되지 않습니다.** $20$만 개의 표본이 $\sigma_{1}$에 매우 가깝게 갔지만, 그것은 최댓값이 그 이상이 아님을 보장하지 않습니다. 심화 2의 논증이 상한과 달성을 모두 보입니다. 또 노름 동치성의 상수도 **표본이 범위 안에 있음을 확인한 것**이지 상수가 최선임을 증명한 것이 아닙니다.

## 스스로 점검

1. 세 벡터 노름을 쓰세요.
2. $p\to\infty$의 극한과 그 이유를 쓰세요.
3. 노름의 세 공리를 쓰세요.
4. 내적에서 온 노름의 특징을 쓰세요.
5. 유도 노름의 정의를 쓰세요.
6. $\lVert A\rVert_{1}$과 $\lVert A\rVert_{\infty}$의 공식을 쓰세요.
7. 프로베니우스 노름이 유도가 아닌 증거를 쓰세요.
8. 일관성과 준곱셈성을 쓰세요.
9. 스펙트럼 반지름과 노름의 관계를 쓰세요.
10. $\rho<1$인데 위험한 경우를 쓰세요.

**정답.**
1. 절댓값의 합, 제곱합의 제곱근, 절댓값의 최댓값입니다.
2. 최댓값이며 가장 큰 성분이 지수적으로 지배하기 때문입니다.
3. 양정치성, 동차성, 삼각부등식입니다.
4. 평행사변형 법칙을 만족합니다.
5. 단위벡터를 가장 많이 늘이는 배율입니다.
6. 각각 열과 행의 절댓값 합의 최댓값입니다.
7. $\lVert I_{n}\rVert_{F}=\sqrt n\ne1$입니다.
8. $\lVert A\mathbf{x}\rVert\le\lVert A\rVert\lVert\mathbf{x}\rVert$이고 $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$입니다.
9. $\rho(A)\le\lVert A\rVert$이며 대칭이면 같습니다.
10. 결손이거나 비정규이면 초기에 크게 부풀 수 있습니다.

## 부록. 기호 정리

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\lVert\mathbf{v}\rVert_{p}$ | $p$-노름 | $(\sum\lvert v_{i}\rvert ^{p})^{1/p}$입니다 |
| $\lVert A\rVert_{p}$ | 유도 노름 | 최대 늘임 배율입니다 |
| $\lVert A\rVert_{F}$ | 프로베니우스 | 성분의 $\ell^{2}$입니다 |
| $\rho(A)$ | 스펙트럼 반지름 | 고유값 크기의 최댓값입니다 |
| 일관성 | consistency | $\lVert A\mathbf{x}\rVert\le\lVert A\rVert\lVert\mathbf{x}\rVert$ |
| 준곱셈성 | submultiplicativity | $\lVert AB\rVert\le\lVert A\rVert\lVert B\rVert$ |
| 겔판트 공식 | Gelfand | $\lVert A^{k}\rVert^{1/k}\to\rho$ |
| 립시츠 상수 | Lipschitz | 변화율의 상한입니다 |

다음 91강에서는 **조건수**를 정면으로 다룹니다. 심화 4에서 유도만 해 두었는데, 그 정의와 성질을 세우고 **오차가 왜 그만큼 증폭되는지 증명**합니다. 67강 심화 6에서 구별한 "문제의 조건"과 "알고리즘의 안정성"이 여기서 정확한 뜻을 얻습니다.
