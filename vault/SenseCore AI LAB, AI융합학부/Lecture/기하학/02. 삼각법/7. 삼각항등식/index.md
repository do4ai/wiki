---
title: "7. 삼각항등식"
---
# 7강. 삼각항등식

## 이 강의에서 할 수 있게 되는 것
- 피타고라스 항등식 $\sin^2\theta+\cos^2\theta=1$을 단위원으로 유도하고 변형해 쓸 수 있습니다.
- 탄젠트를 포함한 항등식과 여각·음각 공식을 이용할 수 있습니다.
- 사인과 코사인의 덧셈정리를 세우고 값을 계산할 수 있습니다.
- 덧셈정리에서 이배각 공식을 이끌어 낼 수 있습니다.
- 항등식을 이용해 식을 간단히 하고 간단한 삼각방정식을 풀 수 있습니다.

## 1. 오늘 쓸 기호

| 기호 | 읽는 법 | 뜻 |
|---|---|---|
| $\sin^2\theta$ | 사인 제곱 세타 | $(\sin\theta)^2$, 사인 값을 제곱한 것 |
| 항등식 | 항등식 | 변수의 모든 값에서 항상 성립하는 등식 |
| 방정식 | 방정식 | 특정한 값에서만 성립하는 등식 |
| $\alpha$, $\beta$ | 알파, 베타 | 두 각을 나타내는 문자 |
| 덧셈정리 | 덧셈정리 | 두 각의 합·차의 삼각함수를 각각의 삼각함수로 나타낸 식 |
| 이배각 | 이배각 | 각 $\theta$의 두 배인 $2\theta$ |

항등식과 방정식을 구분해 씁니다. $\sin^2\theta+\cos^2\theta=1$은 어떤 $\theta$를 넣어도 성립하는 항등식이고, $\sin\theta=\dfrac{1}{2}$은 특정한 $\theta$에서만 성립하는 방정식입니다.

## 2. 개념

### 2.1 피타고라스 항등식은 단위원에서 나온다

가장 기본이 되는 항등식은 사인과 코사인의 제곱의 합입니다.

> 모든 각 $\theta$에서 $\sin^2\theta+\cos^2\theta=1$이다.

단위원에서 바로 나옵니다. 각 $\theta$에 대응하는 단위원 위의 점은 $(\cos\theta,\ \sin\theta)$이고, 이 점은 반지름이 $1$인 원 위에 있으므로 원의 방정식 $x^2+y^2=1$을 만족합니다.

[그림 설명: 반지름 $1$인 단위원 위의 점 $P=(\cos\theta,\sin\theta)$. 원점에서 $P$까지 거리가 $1$이고, 이 거리의 제곱이 $\cos^2\theta+\sin^2\theta$이므로 $1$과 같다.]

$x=\cos\theta$, $y=\sin\theta$를 대입하면 $\cos^2\theta+\sin^2\theta=1$입니다. 이 식은 자주 다음처럼 변형해 씁니다.

$$
\sin^2\theta=1-\cos^2\theta,\qquad
\cos^2\theta=1-\sin^2\theta
$$

양변을 $\cos^2\theta$로 나누면 탄젠트가 들어간 항등식도 나옵니다. $\dfrac{\sin^2\theta}{\cos^2\theta}=\tan^2\theta$이므로

$$
\tan^2\theta+1=\frac{1}{\cos^2\theta}
$$

가 됩니다.

> **문제 1.** (기초) $\cos\theta=\dfrac{3}{5}$인 예각 $\theta$에 대해 $\sin\theta$를 구하시오.
> **답.** $\dfrac{4}{5}$.
> **풀이.** $\sin^2\theta=1-\cos^2\theta=1-\dfrac{9}{25}=\dfrac{16}{25}$이고 예각이므로 $\sin\theta=\dfrac{4}{5}$입니다.

> **문제 2.** (기초) $\sin\theta=\dfrac{5}{13}$인 예각 $\theta$에 대해 $\cos\theta$를 구하시오.
> **답.** $\dfrac{12}{13}$.
> **풀이.** $\cos^2\theta=1-\dfrac{25}{169}=\dfrac{144}{169}$이고 예각이므로 $\cos\theta=\dfrac{12}{13}$입니다.

> **문제 3.** (표준) $\sin\theta\cos\theta=\dfrac{1}{4}$일 때 $(\sin\theta+\cos\theta)^2$을 구하시오.
> **답.** $\dfrac{3}{2}$.
> **풀이.** $(\sin\theta+\cos\theta)^2=\sin^2\theta+\cos^2\theta+2\sin\theta\cos\theta=1+2\times\dfrac{1}{4}=\dfrac{3}{2}$입니다.

> **문제 4.** (표준) $\dfrac{1}{\cos^2\theta}=\dfrac{5}{4}$일 때 $\tan^2\theta$를 구하시오.
> **답.** $\dfrac{1}{4}$.
> **풀이.** $\tan^2\theta+1=\dfrac{1}{\cos^2\theta}$이므로 $\tan^2\theta=\dfrac{5}{4}-1=\dfrac{1}{4}$입니다.

> **문제 5.** (심화) $\tan\theta=2$인 예각 $\theta$에 대해 $\sin\theta\cos\theta$를 구하시오.
> **답.** $\dfrac{2}{5}$.
> **풀이.** $\dfrac{1}{\cos^2\theta}=\tan^2\theta+1=5$이므로 $\cos^2\theta=\dfrac{1}{5}$입니다. $\sin\theta=\tan\theta\cos\theta=2\cos\theta$이므로 $\sin\theta\cos\theta=2\cos^2\theta=2\times\dfrac{1}{5}=\dfrac{2}{5}$입니다.

### 2.2 음각과 여각의 공식

각의 부호를 바꾸거나 여각으로 옮길 때 쓰는 공식이 있습니다. 단위원에서 각 $-\theta$에 대응하는 점은 $\theta$의 점을 $x$축에 대해 뒤집은 점이므로 $x$좌표는 그대로, $y$좌표는 부호가 바뀝니다. 따라서

$$
\cos(-\theta)=\cos\theta,\qquad
\sin(-\theta)=-\sin\theta,\qquad
\tan(-\theta)=-\tan\theta
$$

입니다. 코사인은 부호가 그대로인 우함수, 사인과 탄젠트는 부호가 바뀌는 기함수입니다.

여각 공식은 앞 강의에서 본 대로

$$
\sin(90^\circ-\theta)=\cos\theta,\qquad
\cos(90^\circ-\theta)=\sin\theta
$$

입니다.

> **문제 6.** (기초) $\cos(-60^\circ)$의 값을 구하시오.
> **답.** $\dfrac{1}{2}$.
> **풀이.** $\cos(-\theta)=\cos\theta$이므로 $\cos(-60^\circ)=\cos 60^\circ=\dfrac{1}{2}$입니다.

> **문제 7.** (기초) $\sin(-30^\circ)$의 값을 구하시오.
> **답.** $-\dfrac{1}{2}$.
> **풀이.** $\sin(-\theta)=-\sin\theta$이므로 $\sin(-30^\circ)=-\sin 30^\circ=-\dfrac{1}{2}$입니다.

> **문제 8.** (표준) $\sin(-\theta)+\cos(-\theta)$를 $\sin\theta$, $\cos\theta$로 나타내시오.
> **답.** $-\sin\theta+\cos\theta$.
> **풀이.** $\sin(-\theta)=-\sin\theta$, $\cos(-\theta)=\cos\theta$이므로 합은 $-\sin\theta+\cos\theta$입니다.

### 2.3 덧셈정리는 두 각의 합을 각각의 삼각함수로 나눈다

두 각의 합이나 차의 삼각함수는 각각의 삼각함수로 나타낼 수 있습니다. 이것이 덧셈정리입니다.

> $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$
> $\sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta$
> $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$
> $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$

부호에 규칙이 있습니다. 사인의 덧셈정리는 좌변과 같은 부호, 코사인의 덧셈정리는 좌변과 반대 부호입니다. 코사인은 "코코 빼기 사사", 사인은 "사코 더하기 코사"로 외우면 편합니다.

이 공식의 쓸모는 특수각의 합·차로 새로운 각의 값을 얻는 데 있습니다. 예를 들어 $75^\circ=45^\circ+30^\circ$이므로

$$
\sin 75^\circ=\sin 45^\circ\cos 30^\circ+\cos 45^\circ\sin 30^\circ
=\frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2}+\frac{\sqrt{2}}{2}\cdot\frac{1}{2}
=\frac{\sqrt{6}+\sqrt{2}}{4}
$$

를 구할 수 있습니다.

> **문제 9.** (기초) $\cos 75^\circ$를 덧셈정리로 구하시오.
> **답.** $\dfrac{\sqrt{6}-\sqrt{2}}{4}$.
> **풀이.** $\cos 75^\circ=\cos(45^\circ+30^\circ)=\cos 45^\circ\cos 30^\circ-\sin 45^\circ\sin 30^\circ=\dfrac{\sqrt{2}}{2}\cdot\dfrac{\sqrt{3}}{2}-\dfrac{\sqrt{2}}{2}\cdot\dfrac{1}{2}=\dfrac{\sqrt{6}-\sqrt{2}}{4}$입니다.

> **문제 10.** (표준) $\sin 15^\circ$를 덧셈정리로 구하시오.
> **답.** $\dfrac{\sqrt{6}-\sqrt{2}}{4}$.
> **풀이.** $\sin 15^\circ=\sin(45^\circ-30^\circ)=\sin 45^\circ\cos 30^\circ-\cos 45^\circ\sin 30^\circ=\dfrac{\sqrt{2}}{2}\cdot\dfrac{\sqrt{3}}{2}-\dfrac{\sqrt{2}}{2}\cdot\dfrac{1}{2}=\dfrac{\sqrt{6}-\sqrt{2}}{4}$입니다.

> **문제 11.** (표준) $\sin\alpha=\dfrac{3}{5}$, $\cos\beta=\dfrac{5}{13}$이고 $\alpha$, $\beta$가 모두 예각일 때 $\sin(\alpha+\beta)$를 구하시오.
> **답.** $\dfrac{63}{65}$.
> **풀이.** $\cos\alpha=\dfrac{4}{5}$, $\sin\beta=\dfrac{12}{13}$입니다. $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta=\dfrac{3}{5}\cdot\dfrac{5}{13}+\dfrac{4}{5}\cdot\dfrac{12}{13}=\dfrac{15}{65}+\dfrac{48}{65}=\dfrac{63}{65}$입니다.

> **문제 12.** (심화) $\cos 40^\circ\cos 10^\circ+\sin 40^\circ\sin 10^\circ$의 값을 구하시오.
> **답.** $\dfrac{\sqrt{3}}{2}$.
> **풀이.** 코사인 차 공식 $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$에서 $\alpha=40^\circ$, $\beta=10^\circ$이므로 값은 $\cos(40^\circ-10^\circ)=\cos 30^\circ=\dfrac{\sqrt{3}}{2}$입니다.

### 2.4 이배각 공식은 덧셈정리의 특별한 경우다

덧셈정리에서 $\beta=\alpha$로 놓으면 각의 두 배에 대한 공식이 나옵니다.

사인은 $\sin(\alpha+\alpha)=\sin\alpha\cos\alpha+\cos\alpha\sin\alpha$이므로

$$
\sin 2\alpha=2\sin\alpha\cos\alpha
$$

이고, 코사인은 $\cos(\alpha+\alpha)=\cos\alpha\cos\alpha-\sin\alpha\sin\alpha$이므로

$$
\cos 2\alpha=\cos^2\alpha-\sin^2\alpha
$$

입니다. 코사인의 이배각은 피타고라스 항등식으로 두 가지 형태로 더 쓸 수 있습니다.

$$
\cos 2\alpha=1-2\sin^2\alpha=2\cos^2\alpha-1
$$

> **문제 13.** (기초) $\sin\theta=\dfrac{3}{5}$, $\cos\theta=\dfrac{4}{5}$일 때 $\sin 2\theta$를 구하시오.
> **답.** $\dfrac{24}{25}$.
> **풀이.** $\sin 2\theta=2\sin\theta\cos\theta=2\times\dfrac{3}{5}\times\dfrac{4}{5}=\dfrac{24}{25}$입니다.

> **문제 14.** (표준) $\cos\theta=\dfrac{3}{5}$일 때 $\cos 2\theta$를 구하시오.
> **답.** $-\dfrac{7}{25}$.
> **풀이.** $\cos 2\theta=2\cos^2\theta-1=2\times\dfrac{9}{25}-1=\dfrac{18}{25}-\dfrac{25}{25}=-\dfrac{7}{25}$입니다.

> **문제 15.** (표준) $\sin 15^\circ\cos 15^\circ$의 값을 구하시오.
> **답.** $\dfrac{1}{4}$.
> **풀이.** $\sin 2\alpha=2\sin\alpha\cos\alpha$에서 $\sin\alpha\cos\alpha=\dfrac{1}{2}\sin 2\alpha$입니다. $\alpha=15^\circ$이므로 $\dfrac{1}{2}\sin 30^\circ=\dfrac{1}{2}\times\dfrac{1}{2}=\dfrac{1}{4}$입니다.

> **문제 16.** (심화) $\sin\theta=\dfrac{1}{3}$일 때 $\cos 2\theta$를 구하시오.
> **답.** $\dfrac{7}{9}$.
> **풀이.** $\cos 2\theta=1-2\sin^2\theta=1-2\times\dfrac{1}{9}=1-\dfrac{2}{9}=\dfrac{7}{9}$입니다.

### 2.5 항등식으로 식을 간단히 하고 방정식을 푼다

항등식은 복잡한 식을 간단히 하거나, 삼각방정식을 푸는 도구가 됩니다.

식을 간단히 할 때는 $\sin^2\theta+\cos^2\theta=1$을 자주 씁니다. 예를 들어 $\dfrac{1-\cos^2\theta}{\sin\theta}=\dfrac{\sin^2\theta}{\sin\theta}=\sin\theta$입니다.

간단한 삼각방정식은 특수각의 값을 거꾸로 읽어 풉니다. 예를 들어 $0^\circ\le\theta<360^\circ$에서 $\sin\theta=\dfrac{1}{2}$이면, 사인이 $\dfrac{1}{2}$인 각은 1사분면 $30^\circ$와 2사분면 $150^\circ$이므로 $\theta=30^\circ$ 또는 $\theta=150^\circ$입니다.

> **문제 17.** (기초) $\dfrac{\sin\theta}{\cos\theta}\times\cos\theta$를 간단히 하시오.
> **답.** $\sin\theta$.
> **풀이.** $\dfrac{\sin\theta}{\cos\theta}=\tan\theta$이므로 $\tan\theta\times\cos\theta=\dfrac{\sin\theta}{\cos\theta}\times\cos\theta=\sin\theta$입니다.

> **문제 18.** (표준) $(1+\sin\theta)(1-\sin\theta)$를 간단히 하시오.
> **답.** $\cos^2\theta$.
> **풀이.** $(1+\sin\theta)(1-\sin\theta)=1-\sin^2\theta=\cos^2\theta$입니다.

> **문제 19.** (표준) $0^\circ\le\theta<360^\circ$에서 $\cos\theta=\dfrac{\sqrt{3}}{2}$인 $\theta$를 모두 구하시오.
> **답.** $30^\circ$, $330^\circ$.
> **풀이.** 코사인이 양이므로 1사분면과 4사분면입니다. 기준각이 $30^\circ$이므로 $\theta=30^\circ$ 또는 $\theta=360^\circ-30^\circ=330^\circ$입니다.

> **문제 20.** (심화) $0^\circ\le\theta<360^\circ$에서 $2\sin^2\theta-1=0$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $45^\circ$, $135^\circ$, $225^\circ$, $315^\circ$.
> **풀이.** $\sin^2\theta=\dfrac{1}{2}$이므로 $\sin\theta=\pm\dfrac{\sqrt{2}}{2}$입니다. 기준각이 $45^\circ$이고 네 사분면 모두 해당하므로 $\theta=45^\circ,135^\circ,225^\circ,315^\circ$입니다.

## 3. 유형 총정리(치트시트)

| 상황 | 쓰는 항등식 | 형태 |
|---|---|---|
| $\sin$과 $\cos$의 제곱 | 피타고라스 항등식 | $\sin^2\theta+\cos^2\theta=1$ |
| $\tan$과 $\cos$ 섞임 | 변형 항등식 | $\tan^2\theta+1=\dfrac{1}{\cos^2\theta}$ |
| 각의 부호 바꿈 | 음각 공식 | $\cos(-\theta)=\cos\theta$, $\sin(-\theta)=-\sin\theta$ |
| 두 각의 합·차 | 덧셈정리 | $\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$ |
| 두 각의 합·차(코사인) | 덧셈정리 | $\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$ |
| 각의 두 배 | 이배각 | $\sin 2\alpha=2\sin\alpha\cos\alpha$, $\cos 2\alpha=2\cos^2\alpha-1$ |
| 방정식 풀기 | 특수각 역읽기 | 사분면마다 해를 찾기 |

식에 제곱이 보이면 피타고라스 항등식, 각이 합·차로 쪼개지면 덧셈정리, 각이 두 배면 이배각 공식을 떠올립니다.

## 4. 종합 문제 드릴

> **문제 21.** (기초) $\sin^2 20^\circ+\cos^2 20^\circ$의 값을 구하시오.
> **답.** $1$.
> **풀이.** 피타고라스 항등식으로 어떤 각이든 $\sin^2\theta+\cos^2\theta=1$이므로 값은 $1$입니다.

> **문제 22.** (기초) $\cos(-45^\circ)+\sin(-45^\circ)$의 값을 구하시오.
> **답.** $0$.
> **풀이.** $\cos(-45^\circ)=\cos 45^\circ=\dfrac{\sqrt{2}}{2}$, $\sin(-45^\circ)=-\sin 45^\circ=-\dfrac{\sqrt{2}}{2}$이므로 합은 $0$입니다.

> **문제 23.** (표준) $\sin\alpha=\dfrac{4}{5}$, $\cos\beta=\dfrac{12}{13}$이고 $\alpha$, $\beta$가 모두 예각일 때 $\cos(\alpha-\beta)$를 구하시오.
> **답.** $\dfrac{63}{65}$.
> **풀이.** $\cos\alpha=\dfrac{3}{5}$, $\sin\beta=\dfrac{5}{13}$입니다. $\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta=\dfrac{3}{5}\cdot\dfrac{12}{13}+\dfrac{4}{5}\cdot\dfrac{5}{13}=\dfrac{36}{65}+\dfrac{20}{65}=\dfrac{56}{65}$입니다.

> **문제 24.** (표준) $\tan\theta=\dfrac{1}{2}$인 예각 $\theta$에 대해 $\sin 2\theta$를 구하시오.
> **답.** $\dfrac{4}{5}$.
> **풀이.** 높이 $1$, 밑변 $2$, 빗변 $\sqrt{5}$이므로 $\sin\theta=\dfrac{1}{\sqrt{5}}$, $\cos\theta=\dfrac{2}{\sqrt{5}}$입니다. $\sin 2\theta=2\sin\theta\cos\theta=2\times\dfrac{1}{\sqrt{5}}\times\dfrac{2}{\sqrt{5}}=\dfrac{4}{5}$입니다.

> **문제 25.** (표준) $\cos 2\theta=\dfrac{7}{25}$이고 $\theta$가 예각일 때 $\cos\theta$를 구하시오.
> **답.** $\dfrac{4}{5}$.
> **풀이.** $\cos 2\theta=2\cos^2\theta-1$이므로 $2\cos^2\theta=1+\dfrac{7}{25}=\dfrac{32}{25}$, $\cos^2\theta=\dfrac{16}{25}$입니다. 예각이므로 $\cos\theta=\dfrac{4}{5}$입니다.

> **문제 26.** (표준) $\dfrac{\cos^2\theta}{1+\sin\theta}$를 간단히 하시오.
> **답.** $1-\sin\theta$.
> **풀이.** $\cos^2\theta=1-\sin^2\theta=(1+\sin\theta)(1-\sin\theta)$이므로 $\dfrac{(1+\sin\theta)(1-\sin\theta)}{1+\sin\theta}=1-\sin\theta$입니다.

> **문제 27.** (심화) $\sin\theta+\cos\theta=\dfrac{1}{2}$일 때 $\sin 2\theta$를 구하시오.
> **답.** $-\dfrac{3}{4}$.
> **풀이.** 양변을 제곱하면 $1+2\sin\theta\cos\theta=\dfrac{1}{4}$이므로 $2\sin\theta\cos\theta=-\dfrac{3}{4}$입니다. $\sin 2\theta=2\sin\theta\cos\theta=-\dfrac{3}{4}$입니다.

> **문제 28.** (심화) $0^\circ\le\theta<360^\circ$에서 $2\cos^2\theta-\cos\theta=0$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $60^\circ$, $90^\circ$, $270^\circ$, $300^\circ$.
> **풀이.** $\cos\theta(2\cos\theta-1)=0$이므로 $\cos\theta=0$ 또는 $\cos\theta=\dfrac{1}{2}$입니다. $\cos\theta=0$이면 $\theta=90^\circ,270^\circ$이고, $\cos\theta=\dfrac{1}{2}$이면 $\theta=60^\circ,300^\circ$입니다.

> **문제 29.** (심화) $0^\circ\le\theta<360^\circ$에서 $\sin 2\theta=\dfrac{1}{2}$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $15^\circ$, $75^\circ$, $195^\circ$, $255^\circ$.
> **풀이.** $2\theta$의 범위는 $0^\circ\le 2\theta<720^\circ$입니다. $\sin(2\theta)=\dfrac{1}{2}$인 각은 $30^\circ,150^\circ,390^\circ,510^\circ$이므로 $2\theta$가 이 값들이 됩니다. 각각 $2$로 나누면 $\theta=15^\circ,75^\circ,195^\circ,255^\circ$입니다.

## 5. 스스로 점검

1. 피타고라스 항등식 $\sin^2\theta+\cos^2\theta=1$을 단위원으로 유도할 수 있는가?
2. $\tan^2\theta+1=\dfrac{1}{\cos^2\theta}$을 만들 수 있는가?
3. 음각 공식과 여각 공식을 구분해 쓸 수 있는가?
4. 사인·코사인의 덧셈정리를 정확한 부호로 쓸 수 있는가?
5. 덧셈정리로 $75^\circ$, $15^\circ$ 같은 각의 값을 구할 수 있는가?
6. 이배각 공식을 덧셈정리에서 이끌어 낼 수 있는가?
7. 항등식으로 삼각식을 간단히 할 수 있는가?
8. 특수각을 거꾸로 읽어 간단한 삼각방정식의 해를 모두 찾을 수 있는가?

정답
1. 단위원 위의 점 $(\cos\theta,\sin\theta)$가 $x^2+y^2=1$을 만족하므로 성립한다.
2. 피타고라스 항등식의 양변을 $\cos^2\theta$로 나누면 얻는다.
3. 음각은 $\cos(-\theta)=\cos\theta$, $\sin(-\theta)=-\sin\theta$이고, 여각은 사인과 코사인이 서로 바뀐다.
4. 사인은 좌변과 같은 부호, 코사인은 반대 부호로 쓴다.
5. $75^\circ=45^\circ+30^\circ$, $15^\circ=45^\circ-30^\circ$처럼 특수각의 합·차로 쪼개 대입한다.
6. 덧셈정리에서 $\beta=\alpha$로 놓으면 $\sin 2\alpha=2\sin\alpha\cos\alpha$, $\cos 2\alpha=\cos^2\alpha-\sin^2\alpha$가 나온다.
7. $\sin^2\theta+\cos^2\theta=1$과 인수분해로 분모나 분자를 지운다.
8. 값이 되는 기준각을 찾고, 그 삼각비가 맞는 부호가 되는 사분면마다 해를 적는다.
</content>
