---
title: "문제집 - 03. 복소수와 복소해석 입문"
---
# 문제집 - 03. 복소수와 복소해석 입문

3단원의 세 강의(9강 복소수와 극형식, 10강 복소함수와 오일러 공식, 11강 복소미분·해석함수 개관)를 강의별로 묶어 정리한 누적 문제집입니다. 각 문제는 문제·답·풀이 세 줄로 되어 있으며, 본문 강의보다 한 단계 어렵게 구성했습니다. $n$제곱근 전체 구하기와 기하 배치, 드무아브르로 $\cos n\theta,\sin n\theta$ 유도, 오일러 공식으로 합 공식·급수, 복소로그·복소거듭제곱의 주값, 코시-리만 방정식으로 해석성 판정, 조화켤레 복원처럼 손이 많이 가는 계산이 섞여 있으니, 답만 맞히지 말고 풀이의 계산과 검산을 따라가며 스스로 다시 써 보는 것이 좋습니다. 복소수 계산은 반드시 직교형식으로 되돌리거나 극형식으로 환원해, 또는 원식에 대입해 검산합니다. 표기는 KaTeX를 따릅니다.

## 9강. 복소수와 극형식

> **문제 1.** (표준) $\dfrac{(1+i)^3}{(1-i)^2}$을 $a+bi$ 꼴로 쓰십시오.
> **답.** $-1-i$.
> **풀이.** $(1+i)^2=2i$이라 $(1+i)^3=(1+i)\cdot2i=2i+2i^2=-2+2i$입니다. $(1-i)^2=-2i$입니다. 따라서 $\dfrac{-2+2i}{-2i}$이고 분자·분모에 $i$를 곱하면 $\dfrac{(-2+2i)i}{-2i\cdot i}=\dfrac{-2i+2i^2}{-2i^2}=\dfrac{-2-2i}{2}=-1-i$입니다. 극형식으로 검산합니다. $1+i=\sqrt2\operatorname{cis}\dfrac\pi4$, $1-i=\sqrt2\operatorname{cis}\left(-\dfrac\pi4\right)$이라 $\dfrac{(\sqrt2)^3\operatorname{cis}\frac{3\pi}4}{(\sqrt2)^2\operatorname{cis}(-\frac\pi2)}=\dfrac{2\sqrt2}{2}\operatorname{cis}\left(\dfrac{3\pi}4+\dfrac\pi2\right)=\sqrt2\operatorname{cis}\dfrac{5\pi}4=\sqrt2\left(-\dfrac{\sqrt2}2-\dfrac{\sqrt2}2 i\right)=-1-i$입니다. 두 방법이 일치합니다.

> **문제 2.** (표준) $z=1+i\sqrt3$일 때 $z^{2026}$을 극형식으로 구하십시오.
> **답.** $2^{2026}\operatorname{cis}\dfrac{4\pi}{3}=2^{2026}\left(-\dfrac12-\dfrac{\sqrt3}{2}i\right)$.
> **풀이.** $z=2\operatorname{cis}\dfrac\pi3$입니다. 드무아브르로 $z^{2026}=2^{2026}\operatorname{cis}\dfrac{2026\pi}{3}$입니다. 각에서 $2\pi$의 배수를 뺍니다. $2026=3\cdot675+1$이라 $\dfrac{2026\pi}{3}=675\pi+\dfrac\pi3$입니다. $675$가 홀수라 $675\pi=674\pi+\pi\equiv\pi\pmod{2\pi}$이므로 $\pi+\dfrac\pi3=\dfrac{4\pi}{3}$가 남습니다. 곧 $z^{2026}=2^{2026}\operatorname{cis}\dfrac{4\pi}{3}=2^{2026}\left(-\dfrac12-\dfrac{\sqrt3}{2}i\right)$입니다. 검산: $\dfrac{4\pi}{3}$은 제3사분면 각이라 실·허수부가 모두 음수인 것과 맞습니다.

> **문제 3.** (표준) $-64$의 여섯제곱근을 모두 구하십시오.
> **답.** $2\operatorname{cis}\dfrac{(2k+1)\pi}{6}$, $k=0,\dots,5$: $\sqrt3+i,\ 2i,\ -\sqrt3+i,\ -\sqrt3-i,\ -2i,\ \sqrt3-i$.
> **풀이.** $-64=64\operatorname{cis}\pi$이라 $w_k=64^{1/6}\operatorname{cis}\dfrac{\pi+2\pi k}{6}=2\operatorname{cis}\dfrac{(2k+1)\pi}{6}$, $k=0,\dots,5$입니다. $k=0$: $2\operatorname{cis}\dfrac\pi6=\sqrt3+i$. $k=1$: $2\operatorname{cis}\dfrac{3\pi}6=2\operatorname{cis}\dfrac\pi2=2i$. $k=2$: $2\operatorname{cis}\dfrac{5\pi}6=-\sqrt3+i$. $k=3$: $2\operatorname{cis}\dfrac{7\pi}6=-\sqrt3-i$. $k=4$: $2\operatorname{cis}\dfrac{9\pi}6=2\operatorname{cis}\dfrac{3\pi}2=-2i$. $k=5$: $2\operatorname{cis}\dfrac{11\pi}6=\sqrt3-i$. 여섯 근이 반지름 $2$인 원 위 정육각형을 이룹니다.

> **문제 4.** (표준) $z$가 $\lvert z\rvert=1$이고 $z\ne1$일 때 $\dfrac{1}{1-z}$의 실수부가 $\dfrac12$임을 보이십시오.
> **답.** $\operatorname{Re}\dfrac{1}{1-z}=\dfrac12$.
> **풀이.** $z=\operatorname{cis}\theta$로 두면 $1-z=1-\cos\theta-i\sin\theta$입니다. $\dfrac{1}{1-z}=\dfrac{\overline{1-z}}{\lvert1-z\rvert^2}$이고 분자의 실수부는 $1-\cos\theta$입니다. 분모 $\lvert1-z\rvert^2=(1-\cos\theta)^2+\sin^2\theta=1-2\cos\theta+\cos^2\theta+\sin^2\theta=2-2\cos\theta=2(1-\cos\theta)$입니다. 따라서 실수부는 $\dfrac{1-\cos\theta}{2(1-\cos\theta)}=\dfrac12$입니다($z\ne1$이라 $1-\cos\theta\ne0$). $\square$

> **문제 5.** (표준) 방정식 $z^4=-1$의 네 근을 구하고, 그 근들을 두 실계수 이차식의 곱으로 인수분해하는 데 쓰십시오.
> **답.** 근 $\operatorname{cis}\dfrac{(2k+1)\pi}{4}$; $z^4+1=(z^2-\sqrt2 z+1)(z^2+\sqrt2 z+1)$.
> **풀이.** $z^4=-1=\operatorname{cis}\pi$이라 $z_k=\operatorname{cis}\dfrac{(2k+1)\pi}{4}$, $k=0,1,2,3$입니다. 곧 $\operatorname{cis}\dfrac\pi4,\operatorname{cis}\dfrac{3\pi}4,\operatorname{cis}\dfrac{5\pi}4,\operatorname{cis}\dfrac{7\pi}4$로 $\dfrac{\pm1\pm i}{\sqrt2}$입니다. 켤레쌍끼리 묶으면 각 이차식이 실계수가 됩니다. $\operatorname{cis}\dfrac\pi4$와 $\operatorname{cis}\dfrac{7\pi}4$(=$\operatorname{cis}(-\frac\pi4)$)는 합 $2\cos\dfrac\pi4=\sqrt2$, 곱 $1$이라 $z^2-\sqrt2 z+1$입니다. 나머지 쌍은 합 $2\cos\dfrac{3\pi}4=-\sqrt2$, 곱 $1$이라 $z^2+\sqrt2 z+1$입니다. 따라서 $z^4+1=(z^2-\sqrt2 z+1)(z^2+\sqrt2 z+1)$입니다. 검산: $(z^2+1)^2-(\sqrt2 z)^2=z^4+2z^2+1-2z^2=z^4+1$로 맞습니다.

> **문제 6.** (심화) $\left(\dfrac{-1+\sqrt3\,i}{2}\right)^n$이 $1$이 되는 가장 작은 양의 정수 $n$을 구하십시오.
> **답.** $3$.
> **풀이.** $\dfrac{-1+\sqrt3\,i}{2}=\operatorname{cis}\dfrac{2\pi}{3}$입니다($r=1$, 제2사분면 각 $\dfrac{2\pi}3$). $\left(\operatorname{cis}\dfrac{2\pi}3\right)^n=\operatorname{cis}\dfrac{2\pi n}{3}$이 $1=\operatorname{cis}0$이 되려면 $\dfrac{2\pi n}{3}$이 $2\pi$의 배수, 곧 $n$이 $3$의 배수여야 합니다. 가장 작은 양의 정수는 $n=3$입니다. 이 값은 $1$의 원시 세제곱근입니다.

> **문제 7.** (심화) $\lvert z-3\rvert+\lvert z+3\rvert=10$을 만족하는 $z=x+iy$의 자취가 타원임을 보이고 방정식을 구하십시오.
> **답.** $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$.
> **풀이.** $\lvert z-3\rvert$은 점 $(3,0)$까지, $\lvert z+3\rvert$은 점 $(-3,0)$까지의 거리입니다. 두 초점 $(\pm3,0)$까지 거리의 합이 $10$(일정)인 점들이라 타원입니다. 장반경 $a=5$($2a=10$), 초점거리 $c=3$이라 단반경 $b=\sqrt{a^2-c^2}=\sqrt{25-9}=4$입니다. 따라서 $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$입니다.

> **문제 8.** (심화) $1$의 원시 세제곱근 $\omega$($\omega\ne1$, $\omega^3=1$)에 대해 $(1+\omega)(1+\omega^2)$의 값을 구하십시오.
> **답.** $1$.
> **풀이.** $\omega$는 $1+\omega+\omega^2=0$을 만족합니다(세 세제곱근의 합이 $0$). 따라서 $1+\omega=-\omega^2$, $1+\omega^2=-\omega$입니다. 곱하면 $(1+\omega)(1+\omega^2)=(-\omega^2)(-\omega)=\omega^3=1$입니다. 검산: 직접 전개하면 $1+\omega+\omega^2+\omega^3=(1+\omega+\omega^2)+\omega^3=0+1=1$로 같습니다. $\square$

> **문제 9.** (표준) $-8$의 세제곱근을 모두 구하고 복소평면에서의 배치를 말하십시오.
> **답.** $1+\sqrt3\,i,\ -2,\ 1-\sqrt3\,i$(반지름 $2$인 원 위 정삼각형).
> **풀이.** $-8=8\operatorname{cis}\pi$이라 $w_k=8^{1/3}\operatorname{cis}\dfrac{\pi+2\pi k}{3}=2\operatorname{cis}\dfrac{(2k+1)\pi}{3}$입니다. $k=0$: $2\operatorname{cis}\dfrac\pi3=2\left(\dfrac12+\dfrac{\sqrt3}{2}i\right)=1+\sqrt3\,i$. $k=1$: $2\operatorname{cis}\pi=-2$. $k=2$: $2\operatorname{cis}\dfrac{5\pi}3=1-\sqrt3\,i$. 세 근이 반지름 $2$인 원 위에서 $120^\circ$씩 벌어진 정삼각형을 이룹니다. 검산: 실근 $(-2)^3=-8$이고, 세 근의 합은 $0$입니다.

> **문제 10.** (심화) 이차방정식 $z^2-(3+2i)z+(5+i)=0$을 푸십시오.
> **답.** $z=2+3i$ 또는 $z=1-i$.
> **풀이.** 근의 공식 $z=\dfrac{(3+2i)\pm\sqrt{D}}{2}$에서 판별식 $D=(3+2i)^2-4(5+i)=9+12i-4-20-4i=-15+8i$입니다. $\sqrt{-15+8i}=x+yi$로 두면 $x^2-y^2=-15$, $2xy=8$이고 $x^2+y^2=\lvert-15+8i\rvert=\sqrt{225+64}=17$입니다. 더하면 $2x^2=2$이라 $x^2=1$, 빼면 $y^2=16$입니다. $xy=4>0$이라 부호가 같으므로 $\sqrt D=1+4i$입니다. 따라서 $z=\dfrac{(3+2i)\pm(1+4i)}{2}$이라 $z=\dfrac{4+6i}{2}=2+3i$ 또는 $z=\dfrac{2-2i}{2}=1-i$입니다. 검산: 두 근의 합 $(2+3i)+(1-i)=3+2i$, 곱 $(2+3i)(1-i)=2-2i+3i-3i^2=5+i$로 근·계수 관계와 맞습니다.

> **문제 11.** (표준) $\left(\dfrac{\sqrt3-i}{2}\right)^{2026}$을 직교형식으로 구하십시오.
> **답.** $\dfrac12+\dfrac{\sqrt3}{2}i$.
> **풀이.** $\dfrac{\sqrt3-i}{2}=\operatorname{cis}\left(-\dfrac\pi6\right)$입니다($r=1$, 제4사분면). 드무아브르로 $\left(\operatorname{cis}\left(-\dfrac\pi6\right)\right)^{2026}=\operatorname{cis}\left(-\dfrac{2026\pi}{6}\right)=\operatorname{cis}\left(-\dfrac{1013\pi}{3}\right)$입니다. 각을 $2\pi$로 환원합니다. $1013=3\cdot337+2$이라 $\dfrac{1013\pi}{3}=337\pi+\dfrac{2\pi}{3}$이고 $337$이 홀수라 $337\pi\equiv\pi$이므로 $\dfrac{1013\pi}{3}\equiv\pi+\dfrac{2\pi}{3}=\dfrac{5\pi}{3}\pmod{2\pi}$입니다. 따라서 각은 $-\dfrac{5\pi}{3}\equiv\dfrac\pi3$이라 값은 $\operatorname{cis}\dfrac\pi3=\dfrac12+\dfrac{\sqrt3}{2}i$입니다. 검산: 크기가 $1$이라 결과의 절댓값도 $1$이며 $\left(\dfrac12\right)^2+\left(\dfrac{\sqrt3}{2}\right)^2=1$로 맞습니다.

> **문제 12.** (심화) $1$의 여섯제곱근을 모두 구하고 이웃한 두 근 사이의 거리를 구하십시오.
> **답.** $\operatorname{cis}\dfrac{\pi k}{3}$($k=0,\dots,5$); 이웃 거리 $1$.
> **풀이.** $w_k=\operatorname{cis}\dfrac{2\pi k}{6}=\operatorname{cis}\dfrac{\pi k}{3}$이라 $1,\ \dfrac12+\dfrac{\sqrt3}{2}i,\ -\dfrac12+\dfrac{\sqrt3}{2}i,\ -1,\ -\dfrac12-\dfrac{\sqrt3}{2}i,\ \dfrac12-\dfrac{\sqrt3}{2}i$입니다. 여섯 근은 단위원 위 정육각형의 꼭짓점입니다. 이웃한 두 근은 각이 $\dfrac\pi3$ 벌어져 있으므로 거리는 $\lvert1-\operatorname{cis}\dfrac\pi3\rvert=\left\lvert\dfrac12-\dfrac{\sqrt3}{2}i\right\rvert=\sqrt{\dfrac14+\dfrac34}=1$입니다. 반지름 $r$인 원에 내접한 정육각형은 한 변이 $2r\sin\dfrac\pi6=r$이라는 사실과 일치합니다($r=1$).

> **문제 13.** (표준) $\lvert z-2\rvert=2\lvert z+1\rvert$을 만족하는 $z=x+iy$의 자취를 구하십시오.
> **답.** 중심 $(-2,0)$, 반지름 $2$인 원($(x+2)^2+y^2=4$).
> **풀이.** 양변을 제곱하면 $(x-2)^2+y^2=4\big((x+1)^2+y^2\big)$입니다. 전개하면 $x^2-4x+4+y^2=4x^2+8x+4+4y^2$이라 $0=3x^2+3y^2+12x$, 곧 $x^2+4x+y^2=0$입니다. 완전제곱하면 $(x+2)^2+y^2=4$입니다. 두 점에 이르는 거리의 비가 일정한 점들의 자취(아폴로니우스 원)입니다. 검산: $z=0$이면 $\lvert0-2\rvert=2$, $2\lvert0+1\rvert=2$로 성립하고 $(0+2)^2+0=4$로 원 위에 있습니다.

> **문제 14.** (심화) $\lvert z\rvert=1$이고 $z+\dfrac1z=2\cos\theta$일 때, 임의의 정수 $n$에 대해 $z^n+\dfrac1{z^n}=2\cos n\theta$임을 보이십시오.
> **답.** $z=\operatorname{cis}\theta$이라 $z^n+z^{-n}=2\cos n\theta$입니다.
> **풀이.** $\lvert z\rvert=1$이므로 $\dfrac1z=\bar z$이고 $z+\dfrac1z=z+\bar z=2\operatorname{Re}z$입니다. 이것이 $2\cos\theta$이라 $\operatorname{Re}z=\cos\theta$이고, $\lvert z\rvert=1$과 합치면 $z=\cos\theta\pm i\sin\theta=\operatorname{cis}(\pm\theta)$입니다. 드무아브르로 $z^n=\operatorname{cis}(\pm n\theta)$이고 $\dfrac1{z^n}=\operatorname{cis}(\mp n\theta)$이라 둘의 합은 $\operatorname{cis}(n\theta)+\operatorname{cis}(-n\theta)=2\cos n\theta$입니다(부호는 $\cos$의 우함수성으로 사라짐). $\square$

> **문제 15.** (심화) 방정식 $z^5=\bar z$의 모든 해를 구하십시오.
> **답.** $z=0$ 및 $1$의 여섯제곱근 $\operatorname{cis}\dfrac{\pi k}{3}$($k=0,\dots,5$)로 모두 $7$개.
> **풀이.** $z=0$은 자명한 해입니다. $z\ne0$이면 양변에 절댓값을 취해 $\lvert z\rvert^5=\lvert\bar z\rvert=\lvert z\rvert$이라 $\lvert z\rvert^4=1$, 곧 $\lvert z\rvert=1$입니다. 그러면 $\bar z=\dfrac1z$이므로 $z^5=\dfrac1z$, 곧 $z^6=1$입니다. 따라서 $z\ne0$인 해는 $1$의 여섯제곱근 $\operatorname{cis}\dfrac{2\pi k}{6}=\operatorname{cis}\dfrac{\pi k}{3}$, $k=0,\dots,5$입니다. 전체 $7$개입니다. 검산: $\lvert z\rvert=1$일 때 $z^5=\operatorname{cis}5\theta$, $\bar z=\operatorname{cis}(-\theta)$이라 $5\theta\equiv-\theta$, 곧 $6\theta\equiv0\pmod{2\pi}$로 위 각들이 나옵니다. $\square$

## 10강. 복소함수와 오일러 공식

> **문제 16.** (표준) 오일러 공식으로 $\cos5\theta$를 $\cos\theta,\sin\theta$의 다항식으로 나타내는 실수부를 구하십시오.
> **답.** $\cos5\theta=\cos^5\theta-10\cos^3\theta\sin^2\theta+5\cos\theta\sin^4\theta$.
> **풀이.** $(\cos\theta+i\sin\theta)^5=\cos5\theta+i\sin5\theta$입니다. 이항전개에서 실수부는 $i$의 짝수 거듭제곱 항, 곧 $\binom50\cos^5\theta+\binom52\cos^3\theta(i\sin\theta)^2+\binom54\cos\theta(i\sin\theta)^4$입니다. $(i\sin\theta)^2=-\sin^2\theta$, $(i\sin\theta)^4=\sin^4\theta$이라 $\cos^5\theta-10\cos^3\theta\sin^2\theta+5\cos\theta\sin^4\theta$입니다. 곧 $\cos5\theta$가 이 식입니다($\sin^2=1-\cos^2$로 넣으면 $16\cos^5\theta-20\cos^3\theta+5\cos\theta$).

> **문제 17.** (표준) $\sin^3\theta=\dfrac{3\sin\theta-\sin3\theta}{4}$를 오일러 공식으로 유도하십시오.
> **답.** 세제곱 전개에서 지수 항을 사인으로 되돌립니다.
> **풀이.** $\sin\theta=\dfrac{e^{i\theta}-e^{-i\theta}}{2i}$이라 $\sin^3\theta=\dfrac{(e^{i\theta}-e^{-i\theta})^3}{(2i)^3}$입니다. 분모 $(2i)^3=8i^3=-8i$입니다. 분자를 전개하면 $e^{i3\theta}-3e^{i\theta}+3e^{-i\theta}-e^{-i3\theta}=(e^{i3\theta}-e^{-i3\theta})-3(e^{i\theta}-e^{-i\theta})$입니다. 이는 $2i\sin3\theta-3\cdot2i\sin\theta=2i(\sin3\theta-3\sin\theta)$입니다. 따라서 $\sin^3\theta=\dfrac{2i(\sin3\theta-3\sin\theta)}{-8i}=\dfrac{\sin3\theta-3\sin\theta}{-4}=\dfrac{3\sin\theta-\sin3\theta}{4}$입니다. $\square$

> **문제 18.** (표준) $\left(\dfrac{1+i\sqrt3}{1-i}\right)^{12}$을 계산하십시오.
> **답.** $-64$.
> **풀이.** $1+i\sqrt3=2e^{i\pi/3}$, $1-i=\sqrt2 e^{-i\pi/4}$입니다. 몫은 $\dfrac{2}{\sqrt2}e^{i(\pi/3+\pi/4)}=\sqrt2\,e^{i7\pi/12}$입니다. $12$제곱하면 $(\sqrt2)^{12}e^{i\cdot12\cdot7\pi/12}=2^6 e^{i7\pi}=64e^{i7\pi}$입니다. $7\pi=6\pi+\pi$이라 $e^{i7\pi}=e^{i\pi}=-1$입니다. 따라서 $64\cdot(-1)=-64$입니다.

> **문제 19.** (표준) $e^{z}=1+i$의 모든 해 $z$를 구하십시오.
> **답.** $z=\dfrac12\ln2+i\left(\dfrac\pi4+2\pi k\right)$, $k\in\mathbb Z$.
> **풀이.** $1+i=\sqrt2\,e^{i\pi/4}$입니다. $e^{z}=e^{x}e^{iy}=\sqrt2\,e^{i\pi/4}$가 되려면 크기 $e^{x}=\sqrt2$에서 $x=\ln\sqrt2=\dfrac12\ln2$, 방향 $y=\dfrac\pi4+2\pi k$입니다. 따라서 $z=\dfrac12\ln2+i\left(\dfrac\pi4+2\pi k\right)$입니다. 이는 곧 $\log(1+i)$의 모든 값입니다.

> **문제 20.** (심화) $\operatorname{Log}(-i)$의 주값을 구하고 $(-i)^{i}$의 주값이 $e^{\pi/2}$임을 보이십시오.
> **답.** $\operatorname{Log}(-i)=-i\dfrac\pi2$; $(-i)^{i}=e^{\pi/2}$.
> **풀이.** $-i=1\cdot\operatorname{cis}\left(-\dfrac\pi2\right)$이라 $\lvert-i\rvert=1$, $\operatorname{Arg}(-i)=-\dfrac\pi2$입니다. 따라서 $\operatorname{Log}(-i)=\ln1+i\left(-\dfrac\pi2\right)=-i\dfrac\pi2$입니다. 복소거듭제곱 $(-i)^{i}=e^{i\operatorname{Log}(-i)}=e^{i\cdot(-i\pi/2)}=e^{\pi/2}$입니다($i\cdot(-i)=1$). 실수 $e^{\pi/2}\approx4.81$이 됩니다. $\square$

> **문제 21.** (심화) 단위근을 이용해 $\displaystyle\sum_{k=1}^{n-1}\sin\frac{2\pi k}{n}=0$임을 보이십시오($n\ge2$).
> **답.** 단위근들의 합이 $0$이라 그 허수부의 합도 $0$입니다.
> **풀이.** $\omega_k=e^{i2\pi k/n}$, $k=0,\dots,n-1$은 $1$의 $n$제곱근이고 합이 $0$입니다($n\ge2$). 각 $\omega_k=\cos\dfrac{2\pi k}{n}+i\sin\dfrac{2\pi k}{n}$이라 합의 허수부는 $\sum_{k=0}^{n-1}\sin\dfrac{2\pi k}{n}=0$입니다. $k=0$ 항은 $\sin0=0$이라 빼도 그대로이므로 $\sum_{k=1}^{n-1}\sin\dfrac{2\pi k}{n}=0$입니다. $\square$

> **문제 22.** (심화) $1$의 다섯제곱근의 실수부 합을 이용해 $\cos\dfrac{2\pi}{5}=\dfrac{-1+\sqrt5}{4}$임을 구하십시오.
> **답.** $\cos\dfrac{2\pi}{5}=\dfrac{-1+\sqrt5}{4}$(중간 관계 $\cos\dfrac{2\pi}5+\cos\dfrac{4\pi}5=-\dfrac12$).
> **풀이.** $1$의 다섯제곱근의 합은 $0$이라 실수부 합 $1+2\cos\dfrac{2\pi}5+2\cos\dfrac{4\pi}5=0$입니다(켤레쌍이 두 쌍). 곧 $\cos\dfrac{2\pi}5+\cos\dfrac{4\pi}5=-\dfrac12$입니다. $c=\cos\dfrac{2\pi}5$로 두고 $\cos\dfrac{4\pi}5=2c^2-1$(배각)을 넣으면 $c+2c^2-1=-\dfrac12$, 곧 $4c^2+2c-1=0$입니다. 양의 근이라 $c=\dfrac{-2+\sqrt{4+16}}{8}=\dfrac{-1+\sqrt5}{4}$입니다. 따라서 $\cos\dfrac{2\pi}5=\dfrac{-1+\sqrt5}{4}$입니다(정오각형 작도의 근거). $\square$

> **문제 23.** (심화) $\displaystyle\sum_{k=0}^{n-1}\sin k\theta$의 닫힌 식을 오일러 등비합으로 유도하십시오($\theta$는 $2\pi$의 배수 아님).
> **답.** $\displaystyle\sum_{k=0}^{n-1}\sin k\theta=\frac{\sin(n\theta/2)}{\sin(\theta/2)}\sin\frac{(n-1)\theta}{2}$.
> **풀이.** $\sum_{k=0}^{n-1}e^{ik\theta}=\dfrac{e^{in\theta}-1}{e^{i\theta}-1}$입니다. 분자·분모에서 반각을 뽑으면 $\dfrac{e^{in\theta/2}\cdot2i\sin(n\theta/2)}{e^{i\theta/2}\cdot2i\sin(\theta/2)}=e^{i(n-1)\theta/2}\dfrac{\sin(n\theta/2)}{\sin(\theta/2)}$입니다. 이 복소수의 허수부가 사인 합이라 $\sin\dfrac{(n-1)\theta}{2}\cdot\dfrac{\sin(n\theta/2)}{\sin(\theta/2)}$입니다(10강 코사인 합의 자매식). $\square$

> **문제 24.** (표준) 오일러 공식으로 $\sin5\theta$를 $\sin\theta$의 다항식으로 나타내십시오.
> **답.** $\sin5\theta=16\sin^5\theta-20\sin^3\theta+5\sin\theta$.
> **풀이.** $(\cos\theta+i\sin\theta)^5=\cos5\theta+i\sin5\theta$의 허수부를 봅니다. $i$의 홀수 거듭제곱 항이 허수부에 모이므로 $\sin5\theta=\binom51\cos^4\theta\sin\theta-\binom53\cos^2\theta\sin^3\theta+\binom55\sin^5\theta=5\cos^4\theta\sin\theta-10\cos^2\theta\sin^3\theta+\sin^5\theta$입니다($(i\sin\theta)^1,(i\sin\theta)^3,(i\sin\theta)^5$의 부호가 각각 $+,-,+$). $\cos^2\theta=1-\sin^2\theta$를 넣으면 $5(1-\sin^2\theta)^2\sin\theta-10(1-\sin^2\theta)\sin^3\theta+\sin^5\theta$이고, 전개해 정리하면 $16\sin^5\theta-20\sin^3\theta+5\sin\theta$입니다. 검산: $\theta=\dfrac\pi2$이면 좌변 $\sin\dfrac{5\pi}2=1$, 우변 $16-20+5=1$로 맞습니다. $\square$

> **문제 25.** (표준) $\cos^4\theta=\dfrac18(\cos4\theta+4\cos2\theta+3)$을 오일러 공식으로 유도하십시오(선형화).
> **답.** 위 식이 성립합니다.
> **풀이.** $\cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}{2}$이라 $\cos^4\theta=\dfrac{1}{16}(e^{i\theta}+e^{-i\theta})^4$입니다. 이항전개하면 $(e^{i\theta}+e^{-i\theta})^4=e^{i4\theta}+4e^{i2\theta}+6+4e^{-i2\theta}+e^{-i4\theta}$입니다. 켤레 항끼리 묶으면 $e^{i4\theta}+e^{-i4\theta}=2\cos4\theta$, $4(e^{i2\theta}+e^{-i2\theta})=8\cos2\theta$이라 합은 $2\cos4\theta+8\cos2\theta+6$입니다. 따라서 $\cos^4\theta=\dfrac{2\cos4\theta+8\cos2\theta+6}{16}=\dfrac{\cos4\theta+4\cos2\theta+3}{8}$입니다. 검산: $\theta=0$이면 좌변 $1$, 우변 $\dfrac{1+4+3}{8}=1$로 맞습니다. $\square$

> **문제 26.** (심화) $(1-i)^{1+i}$의 주값을 구하십시오.
> **답.** $\sqrt2\,e^{\pi/4}\left(\cos\left(\dfrac{\ln2}{2}-\dfrac\pi4\right)+i\sin\left(\dfrac{\ln2}{2}-\dfrac\pi4\right)\right)$.
> **풀이.** $z^{w}=e^{w\operatorname{Log}z}$입니다. $1-i=\sqrt2\,e^{-i\pi/4}$이라 $\operatorname{Log}(1-i)=\dfrac12\ln2-i\dfrac\pi4$입니다. 지수 $(1+i)\left(\dfrac12\ln2-i\dfrac\pi4\right)$를 전개하면 $\dfrac12\ln2-i\dfrac\pi4+i\dfrac12\ln2-i^2\dfrac\pi4=\left(\dfrac12\ln2+\dfrac\pi4\right)+i\left(\dfrac12\ln2-\dfrac\pi4\right)$입니다. 따라서 $(1-i)^{1+i}=e^{\frac12\ln2+\frac\pi4}\,e^{i\left(\frac{\ln2}{2}-\frac\pi4\right)}=\sqrt2\,e^{\pi/4}\left(\cos\left(\dfrac{\ln2}{2}-\dfrac\pi4\right)+i\sin\left(\dfrac{\ln2}{2}-\dfrac\pi4\right)\right)$입니다. 검산: 절댓값은 지수의 실수부로 $e^{\frac12\ln2+\frac\pi4}=\sqrt2\,e^{\pi/4}$입니다.

> **문제 27.** (심화) $2^{i}$의 모든 값을 구하고 주값을 쓰십시오.
> **답.** $2^{i}=e^{-2\pi k}\big(\cos(\ln2)+i\sin(\ln2)\big)$($k\in\mathbb Z$), 주값 $\cos(\ln2)+i\sin(\ln2)$.
> **풀이.** $2^{i}=e^{i\log2}$이고 $\log2=\ln2+i(0+2\pi k)=\ln2+2\pi k i$입니다($2$는 양의 실수라 편각 $0$, 주기 $2\pi$). 그러면 $2^{i}=e^{i(\ln2+2\pi k i)}=e^{i\ln2-2\pi k}=e^{-2\pi k}\big(\cos(\ln2)+i\sin(\ln2)\big)$입니다. $k=0$인 주값은 $\cos(\ln2)+i\sin(\ln2)$이며 절댓값 $1$입니다. 실수 밑의 허수 지수도 다가함을 보여 줍니다. $\square$

> **문제 28.** (심화) $1+2\displaystyle\sum_{k=1}^{n}\cos k\theta=\dfrac{\sin\left(\left(n+\frac12\right)\theta\right)}{\sin(\theta/2)}$(디리클레 핵)을 오일러로 유도하십시오($\theta$는 $2\pi$의 배수 아님).
> **답.** 위 식이 성립합니다.
> **풀이.** $S=\displaystyle\sum_{k=-n}^{n}e^{ik\theta}$를 봅니다. 이는 공비 $e^{i\theta}$, 항이 $2n+1$개인 등비수열로 $S=e^{-in\theta}\dfrac{e^{i(2n+1)\theta}-1}{e^{i\theta}-1}$입니다. 분자·분모에서 반각을 뽑으면 $S=\dfrac{e^{i(n+1/2)\theta}-e^{-i(n+1/2)\theta}}{e^{i\theta/2}-e^{-i\theta/2}}=\dfrac{2i\sin\left(\left(n+\frac12\right)\theta\right)}{2i\sin(\theta/2)}=\dfrac{\sin\left(\left(n+\frac12\right)\theta\right)}{\sin(\theta/2)}$입니다. 한편 $S=\sum_{k=-n}^{n}e^{ik\theta}=1+\sum_{k=1}^{n}(e^{ik\theta}+e^{-ik\theta})=1+2\sum_{k=1}^{n}\cos k\theta$이라 두 표현이 같아 원식이 나옵니다. $\square$

> **문제 29.** (심화) $1$의 일곱제곱근의 합이 $0$임을 이용해 $\cos\dfrac{2\pi}{7}+\cos\dfrac{4\pi}{7}+\cos\dfrac{6\pi}{7}=-\dfrac12$임을 보이십시오.
> **답.** $\cos\dfrac{2\pi}{7}+\cos\dfrac{4\pi}{7}+\cos\dfrac{6\pi}{7}=-\dfrac12$.
> **풀이.** $\zeta_k=e^{i2\pi k/7}$, $k=0,\dots,6$은 $1$의 일곱제곱근이고 합이 $0$입니다. $k$와 $7-k$는 켤레라 $\zeta_k+\zeta_{7-k}=2\cos\dfrac{2\pi k}{7}$입니다. 따라서 합 $0=1+2\left(\cos\dfrac{2\pi}{7}+\cos\dfrac{4\pi}{7}+\cos\dfrac{6\pi}{7}\right)$입니다($k=1,2,3$이 각각 $k=6,5,4$와 짝). 정리하면 세 코사인의 합이 $-\dfrac12$입니다. $\square$

> **문제 30.** (심화) $e^{e^{i\theta}}$의 실수부가 $e^{\cos\theta}\cos(\sin\theta)$임을 보이십시오.
> **답.** $\operatorname{Re}\,e^{e^{i\theta}}=e^{\cos\theta}\cos(\sin\theta)$.
> **풀이.** $e^{i\theta}=\cos\theta+i\sin\theta$입니다. 이를 복소지수의 지수로 넣으면 $e^{e^{i\theta}}=e^{\cos\theta+i\sin\theta}=e^{\cos\theta}\cdot e^{i\sin\theta}$입니다. 오일러 공식으로 $e^{i\sin\theta}=\cos(\sin\theta)+i\sin(\sin\theta)$이라 $e^{e^{i\theta}}=e^{\cos\theta}\big(\cos(\sin\theta)+i\sin(\sin\theta)\big)$입니다. 실수부는 $e^{\cos\theta}\cos(\sin\theta)$입니다(허수부는 $e^{\cos\theta}\sin(\sin\theta)$). 이 분해는 지수의 실수부가 크기를, 허수부가 방향을 정한다는 성질을 그대로 쓴 것입니다. $\square$

## 11강. 복소미분·해석함수 개관

> **문제 31.** (표준) $f(z)=z^2\bar z$가 어디서 미분가능한지 판정하십시오.
> **답.** $z=0$에서만 미분가능(어디서도 해석적이지 않음).
> **풀이.** $z=x+iy$에서 $z^2\bar z=z\cdot z\bar z=z\lvert z\rvert^2=(x+iy)(x^2+y^2)$이라 $u=x(x^2+y^2)=x^3+xy^2$, $v=y(x^2+y^2)=x^2y+y^3$입니다. $u_x=3x^2+y^2$, $v_y=x^2+3y^2$이라 $u_x=v_y$는 $3x^2+y^2=x^2+3y^2$, 곧 $x^2=y^2$일 때입니다. $u_y=2xy$, $v_x=2xy$이라 $u_y=-v_x$는 $2xy=-2xy$, 곧 $xy=0$일 때입니다. 두 조건 $x^2=y^2$와 $xy=0$을 동시에 만족하는 점은 $x=y=0$뿐입니다. 따라서 $z=0$에서만 CR을 만족해 그곳에서만 미분가능하고, 근방 조건을 못 채우므로 해석적이지는 않습니다. $\square$

> **문제 32.** (표준) $u=x^3-3xy^2$가 조화함수임을 보이고 조화켤레 $v$를 구해 해석함수 $f$를 $z$의 식으로 쓰십시오.
> **답.** $v=3x^2y-y^3+C$, $f(z)=z^3+iC$.
> **풀이.** $u_x=3x^2-3y^2$, $u_{xx}=6x$; $u_y=-6xy$, $u_{yy}=-6x$이라 $u_{xx}+u_{yy}=0$으로 조화입니다. CR $v_y=u_x=3x^2-3y^2$를 $y$로 적분하면 $v=3x^2y-y^3+g(x)$입니다. $v_x=6xy+g'(x)$이고 CR $v_x=-u_y=6xy$이라 $g'(x)=0$, $g=C$입니다. 따라서 $v=3x^2y-y^3+C$이고 $f=u+iv=(x^3-3xy^2)+i(3x^2y-y^3)+iC=z^3+iC$입니다(11강 2.1에서 $z^3$의 실·허수부와 일치).

> **문제 33.** (표준) $f(z)=e^{\bar z}$가 해석적이지 않음을 CR로 보이십시오.
> **답.** $u=e^x\cos y$, $v=-e^x\sin y$에서 $u_x=e^x\cos y$, $v_y=-e^x\cos y$라 어긋납니다.
> **풀이.** $e^{\bar z}=e^{x-iy}=e^x(\cos y-i\sin y)$이라 $u=e^x\cos y$, $v=-e^x\sin y$입니다. $u_x=e^x\cos y$, $v_y=-e^x\cos y$이라 $u_x=v_y$는 $\cos y=0$인 곳에서만 겨우 성립합니다. $u_y=-e^x\sin y$, $v_x=-e^x\sin y$이라 $u_y=-v_x$는 $\sin y=0$인 곳에서만 성립합니다. 두 조건을 동시에 만족하는 점은 없으므로($\cos y,\sin y$가 동시에 $0$일 수 없음) 어디서도 해석적이지 않습니다. 켤레가 들어간 함수는 해석성을 깨뜨리는 전형적 예입니다. $\square$

> **문제 34.** (표준) 해석함수 $f=u+iv$에서 $u=$ 상수이면 $f$가 상수임을 CR로 보이십시오.
> **답.** $u$가 상수면 $u_x=u_y=0$이고 CR로 $v_x=v_y=0$이라 $v$도 상수입니다.
> **풀이.** $u$가 상수이면 $u_x=0$, $u_y=0$입니다. CR $u_x=v_y$에서 $v_y=0$, $u_y=-v_x$에서 $v_x=0$입니다. $v$의 두 편미분이 모두 $0$이라 $v$도 상수입니다. 따라서 $f=u+iv$가 상수입니다. 실수부만으로 해석함수가 (상수 차이 없이) 거의 결정된다는 강한 성질의 한 조각입니다. $\square$

> **문제 35.** (심화) 극좌표 형태의 코시-리만 방정식 $u_r=\dfrac1r v_\theta$, $v_r=-\dfrac1r u_\theta$를 이용해 $f(z)=z^n$($n$은 양의 정수)이 해석적임을 보이십시오.
> **답.** $u=r^n\cos n\theta$, $v=r^n\sin n\theta$가 극형식 CR을 만족합니다.
> **풀이.** $z=re^{i\theta}$이라 $z^n=r^n e^{in\theta}=r^n(\cos n\theta+i\sin n\theta)$이라 $u=r^n\cos n\theta$, $v=r^n\sin n\theta$입니다. $u_r=nr^{n-1}\cos n\theta$이고 $\dfrac1r v_\theta=\dfrac1r\cdot r^n\cdot n\cos n\theta=nr^{n-1}\cos n\theta$이라 $u_r=\dfrac1r v_\theta$입니다. $v_r=nr^{n-1}\sin n\theta$이고 $-\dfrac1r u_\theta=-\dfrac1r\cdot r^n(-n\sin n\theta)=nr^{n-1}\sin n\theta$이라 $v_r=-\dfrac1r u_\theta$입니다. 극형식 CR을 만족하고 편미분이 연속이라 $z^n$은 해석적입니다. $\square$

> **문제 36.** (심화) $u(x,y)=e^{x}(x\cos y-y\sin y)$가 조화함수임을 보이십시오.
> **답.** $u_{xx}+u_{yy}=0$.
> **풀이.** 이 $u$는 해석함수 $f(z)=ze^{z}$의 실수부입니다($ze^z=(x+iy)e^x(\cos y+i\sin y)$의 실수부가 $e^x(x\cos y-y\sin y)$). 해석함수의 실수부는 조화이므로 $u_{xx}+u_{yy}=0$입니다. 직접 확인하면 $u_x=e^x(x\cos y-y\sin y)+e^x\cos y=e^x((x+1)\cos y-y\sin y)$, $u_{xx}=e^x((x+2)\cos y-y\sin y)$입니다. 한편 $u_y=e^x(-x\sin y-\sin y-y\cos y)=e^x(-(x+1)\sin y-y\cos y)$, $u_{yy}=e^x(-(x+1)\cos y-\cos y+y\sin y)=e^x(-(x+2)\cos y+y\sin y)$입니다. 두 이계편미분을 더하면 $u_{xx}+u_{yy}=e^x((x+2)\cos y-y\sin y-(x+2)\cos y+y\sin y)=0$입니다. $\square$

> **문제 37.** (심화) $f(z)=u+iv$가 해석적이고 $v=u^2$이면 $f$가 상수임을 보이십시오.
> **답.** $v=u^2$을 CR에 넣으면 $u$의 편미분이 모두 $0$이 됩니다.
> **풀이.** $v=u^2$이라 $v_x=2uu_x$, $v_y=2uu_y$입니다. CR $u_x=v_y=2uu_y$와 $u_y=-v_x=-2uu_x$를 얻습니다. 둘째 식을 첫째에 대입하면 $u_x=2u(-2uu_x)=-4u^2 u_x$, 곧 $u_x(1+4u^2)=0$입니다. $1+4u^2>0$이라 $u_x=0$이고, 그러면 $u_y=-2uu_x=0$입니다. $u$의 편미분이 모두 $0$이라 $u$가 상수이고, $v=u^2$도 상수이므로 $f$가 상수입니다. $\square$

> **문제 38.** (심화) $f(z)$가 열린 영역에서 해석적이고 $f'(z)=0$이 그 영역 전체에서 성립하면 $f$가 상수임을 CR로 논증하십시오.
> **답.** $f'=u_x+iv_x=0$과 CR로 $u,v$의 모든 편미분이 $0$이 됩니다.
> **풀이.** $f'=u_x+iv_x=0$이라 $u_x=0$, $v_x=0$입니다. CR $u_x=v_y$에서 $v_y=0$, $u_y=-v_x$에서 $u_y=0$입니다. 곧 $u_x=u_y=0$이라 $u$가 상수, $v_x=v_y=0$이라 $v$가 상수입니다(영역이 연결일 때). 따라서 $f=u+iv$가 상수입니다. 실미분의 "도함수가 $0$이면 상수"가 복소미분에서도, CR을 매개로 성립합니다. $\square$

> **문제 39.** (표준) $u=2xy+3x$가 조화함수임을 보이고 조화켤레 $v$와 해석함수 $f$를 $z$의 식으로 구하십시오.
> **답.** $v=y^2-x^2+3y+C$, $f(z)=-iz^2+3z+iC$.
> **풀이.** $u_x=2y+3$, $u_{xx}=0$; $u_y=2x$, $u_{yy}=0$이라 $u_{xx}+u_{yy}=0$으로 조화입니다. CR $v_y=u_x=2y+3$을 $y$로 적분하면 $v=y^2+3y+g(x)$입니다. $v_x=g'(x)$이고 CR $v_x=-u_y=-2x$이라 $g'(x)=-2x$, 곧 $g(x)=-x^2+C$입니다. 따라서 $v=y^2-x^2+3y+C$입니다. 이제 $f=u+iv$를 $z$로 환원합니다. $-iz^2=-i(x^2-y^2+2xyi)=2xy-i(x^2-y^2)$이라 실수부 $2xy$, 허수부 $y^2-x^2$이고 $3z=3x+3yi$이라 실수부 $3x$, 허수부 $3y$입니다. 합치면 $-iz^2+3z$의 실수부가 $2xy+3x=u$, 허수부가 $y^2-x^2+3y$가 되어 $f=-iz^2+3z+iC$입니다. $\square$

> **문제 40.** (심화) 극형식 CR $u_r=\dfrac1r v_\theta$, $v_r=-\dfrac1r u_\theta$로 주로그 $f(z)=\operatorname{Log}z$가 음의 실축을 뺀 영역에서 해석적이고 $f'(z)=\dfrac1z$임을 보이십시오.
> **답.** $u=\ln r$, $v=\theta$가 극형식 CR을 만족하며 $f'(z)=\dfrac1z$입니다.
> **풀이.** $z=re^{i\theta}$($-\pi<\theta<\pi$)에서 $\operatorname{Log}z=\ln r+i\theta$이라 $u=\ln r$, $v=\theta$입니다. $u_r=\dfrac1r$이고 $\dfrac1r v_\theta=\dfrac1r\cdot1=\dfrac1r$이라 $u_r=\dfrac1r v_\theta$입니다. $v_r=0$이고 $-\dfrac1r u_\theta=-\dfrac1r\cdot0=0$이라 $v_r=-\dfrac1r u_\theta$입니다. 편미분이 이 영역에서 연속이라 해석적입니다. 극형식 도함수 공식 $f'(z)=e^{-i\theta}\left(u_r+i v_r\right)$을 쓰면 $f'(z)=e^{-i\theta}\cdot\dfrac1r=\dfrac1{re^{i\theta}}=\dfrac1z$입니다. 검산: $e^{\operatorname{Log}z}=z$의 양변을 미분한 $e^{\operatorname{Log}z}\cdot(\operatorname{Log}z)'=1$에서도 $(\operatorname{Log}z)'=\dfrac1z$가 나옵니다. $\square$

> **문제 41.** (표준) $f(z)=\sin z$의 $u,v$를 구하고 전평면에서 해석적임을 CR로 보인 뒤 $f'(z)$를 구하십시오.
> **답.** $u=\sin x\cosh y$, $v=\cos x\sinh y$; 해석적, $f'(z)=\cos z$.
> **풀이.** 덧셈정리로 $\sin z=\sin(x+iy)=\sin x\cos(iy)+\cos x\sin(iy)$이고 $\cos(iy)=\cosh y$, $\sin(iy)=i\sinh y$이라 $\sin z=\sin x\cosh y+i\cos x\sinh y$입니다. 곧 $u=\sin x\cosh y$, $v=\cos x\sinh y$입니다. $u_x=\cos x\cosh y$, $v_y=\cos x\cosh y$이라 $u_x=v_y$입니다. $u_y=\sin x\sinh y$, $v_x=-\sin x\sinh y$이라 $u_y=-v_x$입니다. 편미분이 연속이라 전평면에서 해석적입니다. $f'(z)=u_x+iv_x=\cos x\cosh y-i\sin x\sinh y=\cos z$입니다(같은 방식으로 $\cos z=\cos x\cosh y-i\sin x\sinh y$). $\square$

> **문제 42.** (심화) $u=\ln(x^2+y^2)$가 원점을 뺀 영역에서 조화함수임을 보이고 조화켤레 $v$를 구하십시오.
> **답.** $u_{xx}+u_{yy}=0$; $v=2\arg z+C$(곧 $2\theta+C$), $f(z)=2\operatorname{Log}z+iC$.
> **풀이.** $u_x=\dfrac{2x}{x^2+y^2}$, $u_{xx}=\dfrac{2(x^2+y^2)-2x\cdot2x}{(x^2+y^2)^2}=\dfrac{2(y^2-x^2)}{(x^2+y^2)^2}$입니다. 대칭으로 $u_{yy}=\dfrac{2(x^2-y^2)}{(x^2+y^2)^2}$이라 합이 $0$으로 조화입니다($u=2\ln\lvert z\rvert$이라 해석함수 $2\operatorname{Log}z$의 실수부라는 것과도 일치). CR $v_y=u_x=\dfrac{2x}{x^2+y^2}$를 $y$로 적분하면 $v=2\arctan\dfrac yx+g(x)$입니다. $v_x=\dfrac{-2y}{x^2+y^2}+g'(x)$이고 CR $v_x=-u_y=\dfrac{-2y}{x^2+y^2}$이라 $g'(x)=0$, $g=C$입니다. 따라서 $v=2\arctan\dfrac yx+C=2\theta+C=2\arg z+C$이고 $f=2\ln\lvert z\rvert+2i\arg z+iC=2\operatorname{Log}z+iC$입니다. $\square$

> **문제 43.** (심화) 해석함수 $f=u+iv$에서 $3u+2v$가 상수이면 $f$가 상수임을 보이십시오.
> **답.** 계수행렬의 행렬식이 $0$이 아니라 $u_x=v_x=0$, 곧 $f'=0$이 됩니다.
> **풀이.** $3u+2v=c$(상수)를 $x,y$로 각각 미분하면 $3u_x+2v_x=0$과 $3u_y+2v_y=0$입니다. 둘째 식에 CR $u_y=-v_x$, $v_y=u_x$를 넣으면 $3(-v_x)+2u_x=0$, 곧 $2u_x-3v_x=0$입니다. 이제 $3u_x+2v_x=0$과 $2u_x-3v_x=0$을 $u_x,v_x$에 대한 연립식으로 봅니다. 계수행렬의 행렬식은 $3\cdot(-3)-2\cdot2=-13\ne0$이라 유일해는 $u_x=v_x=0$입니다. 그러면 $f'=u_x+iv_x=0$이 전 영역에서 성립하므로 $f$는 상수입니다. $\square$

> **문제 44.** (표준) $u=x^2+axy+by^2$가 조화함수가 되도록 $b$를 정하고($a$는 임의 상수), 조화켤레 $v$를 구하십시오.
> **답.** $b=-1$; $v=2xy-\dfrac a2(x^2-y^2)+C$.
> **풀이.** $u_{xx}=2$, $u_{yy}=2b$이라 조화($u_{xx}+u_{yy}=0$)이려면 $2+2b=0$, 곧 $b=-1$입니다. 이때 $u=x^2+axy-y^2$이라 $u_x=2x+ay$, $u_y=ax-2y$입니다. CR $v_y=u_x=2x+ay$를 $y$로 적분하면 $v=2xy+\dfrac a2 y^2+g(x)$입니다. $v_x=2y+g'(x)$이고 CR $v_x=-u_y=-ax+2y$이라 $g'(x)=-ax$, 곧 $g(x)=-\dfrac a2 x^2+C$입니다. 따라서 $v=2xy-\dfrac a2(x^2-y^2)+C$입니다. 검산: $v_{xx}+v_{yy}=-a+a=0$으로 $v$도 조화이고, $f=u+iv=\left(1-\dfrac{a}{2}i\right)z^2+iC$로 정리됩니다. $\square$

> **문제 45.** (심화) 어떤 해석함수의 허수부가 $v=x^2-y^2$일 수 있는지 판정하고, 가능하면 $f=u+iv$를 $z$의 식으로 구하십시오.
> **답.** 가능합니다($v$가 조화). $u=-2xy+C$, $f(z)=iz^2+C$.
> **풀이.** 먼저 $v$가 조화여야 합니다. $v_{xx}=2$, $v_{yy}=-2$이라 $v_{xx}+v_{yy}=0$으로 조화라 가능합니다. CR로 $u$를 복원합니다. $u_x=v_y=-2y$를 $x$로 적분하면 $u=-2xy+h(y)$입니다. $u_y=-2x+h'(y)$이고 CR $u_y=-v_x=-2x$이라 $h'(y)=0$, 곧 $h=C$입니다. 따라서 $u=-2xy+C$입니다. $z$로 환원하면 $iz^2=i(x^2-y^2+2xyi)=-2xy+i(x^2-y^2)$이라 실수부 $-2xy$, 허수부 $x^2-y^2$가 되어 $f=iz^2+C$입니다. 검산: $f=iz^2+C$의 실수부가 $-2xy+\operatorname{Re}C$, 허수부가 $x^2-y^2$로 맞습니다. $\square$

## 스스로 점검

1. 복소수의 곱·나눗셈·거듭제곱을 직교형식과 극형식 양쪽으로 다루고 서로 검산하는가?
2. $n$제곱근·단위근을 빠짐없이 구하고 정$n$각형 배치·이웃 거리·합이 $0$을 활용하는가?
3. 드무아브르와 오일러 공식으로 $\cos n\theta,\sin n\theta,\sin^n\theta,\cos^n\theta$의 삼각항등식과 선형화를 유도하는가?
4. 복소지수·복소로그·복소거듭제곱의 다가성을 이해하고 주값을 구하는가?
5. 단위근의 합·실수부 합으로 코사인·사인의 합과 특수값($\cos\frac{2\pi}5,\ \cos\frac{2\pi}7$ 등), 디리클레 핵 같은 급수를 얻는가?
6. 코시-리만 방정식(직교·극형식)으로 해석성을 판정하고 도함수를 구하는가?
7. 조화함수를 판정하고 조화켤레를 복원해 해석함수를 $z$의 식으로 되살리는가?

정답 요지: (1) 곱·거듭제곱은 극형식이 빠르고 결과는 직교형식으로 되돌려 확인. (2) $w_k=r^{1/n}\operatorname{cis}\dfrac{\theta+2\pi k}{n}$, 단위근 합은 $0$·정$n$각형·이웃 변 $2r\sin\frac\pi n$. (3) $(\cos\theta+i\sin\theta)^n$의 실·허수부, $\sin\theta=\dfrac{e^{i\theta}-e^{-i\theta}}{2i}$의 거듭제곱 전개와 켤레 항 묶기. (4) $\log z=\ln\lvert z\rvert+i\arg z$, $z^w=e^{w\log z}$는 다가, 주값은 $\operatorname{Arg}$. (5) $1+2\sum\cos\dfrac{2\pi k}n=0$·디리클레 핵 등에서 특수값·급수 유도. (6) $u_x=v_y,\ u_y=-v_x$(극형식은 $u_r=\frac1r v_\theta,\ v_r=-\frac1r u_\theta$), $f'=u_x-iu_y=e^{-i\theta}(u_r+iv_r)$. (7) $u_{xx}+u_{yy}=0$로 조화 판정, CR 적분으로 조화켤레·해석함수 복원. 모든 복소 계산은 직교형식/극형식 환원 또는 원식 대입으로 검산.
