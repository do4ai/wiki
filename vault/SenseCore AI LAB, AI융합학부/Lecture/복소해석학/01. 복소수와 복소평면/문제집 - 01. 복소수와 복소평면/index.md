---
title: "문제집 - 01. 복소수와 복소평면"
---
# 문제집 - 01. 복소수와 복소평면

1단원의 두 강의(1강 복소수와 극형식, 2강 복소함수와 오일러 공식)를 강의별로 묶어 정리한 문제집입니다. 각 문제는 문제·답·풀이 세 부분으로 되어 있으며, 본문 강의의 드릴보다 한 단계 어렵게 구성했습니다. 직교형식과 극형식을 오가며 몫과 큰 거듭제곱을 정리하는 문항, $n$제곱근 전체를 구해 기하 배치와 실계수 인수분해로 잇는 문항, 복소계수 이차방정식을 복소 제곱근으로 푸는 문항, 드무아브르와 오일러 공식으로 삼각항등식을 유도하고 거듭제곱을 선형화하는 문항, 복소로그와 복소거듭제곱의 다가성을 다루는 문항, 단위근의 합에서 특수값과 급수의 닫힌 식을 뽑는 문항이 섞여 있습니다.

푸는 순서에는 요령이 있습니다. 크기와 각이 따로 노는 계산은 극형식으로 옮기고, 덧셈이 섞인 계산은 직교형식으로 되돌립니다. 각을 다루는 문항은 언제나 $2\pi$의 배수를 덜어내 주편각으로 환원한 뒤 사분면을 확인합니다. 답만 맞히지 말고 풀이의 계산을 스스로 다시 써 보는 것이 좋습니다. 모든 복소 계산은 직교형식으로 되돌리거나 극형식으로 환원해, 또는 원식에 대입해 검산합니다. 표기는 KaTeX를 따릅니다.

## 1강. 복소수와 극형식

> **문제 1.** (표준) $\dfrac{(1+i)^3}{(1-i)^2}$을 $a+bi$ 꼴로 쓰고, 같은 값을 극형식으로 다시 확인하십시오.
> **답.** $-1-i$입니다.
> **풀이.** 먼저 분자와 분모를 따로 정리합니다. $(1+i)^2=1+2i+i^2=2i$이므로 $(1+i)^3=(1+i)\cdot2i=2i+2i^2=-2+2i$이고, $(1-i)^2=1-2i+i^2=-2i$입니다. 몫의 분자와 분모에 $i$를 곱해 분모를 실수로 만듭니다.
> $$\frac{-2+2i}{-2i}=\frac{(-2+2i)i}{-2i\cdot i}=\frac{-2i+2i^2}{-2i^2}=\frac{-2-2i}{2}=-1-i$$
> 극형식으로 검산합니다. $1+i=\sqrt2\operatorname{cis}\dfrac\pi4$, $1-i=\sqrt2\operatorname{cis}\left(-\dfrac\pi4\right)$이므로 다음을 얻습니다.
> $$\frac{(\sqrt2)^3\operatorname{cis}\frac{3\pi}4}{(\sqrt2)^2\operatorname{cis}\left(-\frac\pi2\right)}=\sqrt2\operatorname{cis}\left(\frac{3\pi}4+\frac\pi2\right)=\sqrt2\operatorname{cis}\frac{5\pi}4=\sqrt2\left(-\frac{\sqrt2}2-\frac{\sqrt2}2 i\right)=-1-i$$
> 두 방법의 결과가 일치합니다. 몫의 절댓값이 $\dfrac{(\sqrt2)^3}{(\sqrt2)^2}=\sqrt2$이고 $\lvert-1-i\rvert=\sqrt2$인 것도 함께 맞습니다.

> **문제 2.** (표준) $z=1+i\sqrt3$일 때 $z^{2026}$을 극형식과 직교형식으로 구하십시오.
> **답.** $z^{2026}=2^{2026}\operatorname{cis}\dfrac{4\pi}{3}=2^{2026}\left(-\dfrac12-\dfrac{\sqrt3}{2}i\right)$입니다.
> **풀이.** $\lvert z\rvert=\sqrt{1+3}=2$이고 점 $(1,\sqrt3)$이 제1사분면이라 $\arg z=\dfrac\pi3$이므로 $z=2\operatorname{cis}\dfrac\pi3$입니다. 드무아브르 정리로 다음을 얻습니다.
> $$z^{2026}=2^{2026}\operatorname{cis}\frac{2026\pi}{3}$$
> 각에서 $2\pi$의 배수를 덜어냅니다. $2026=3\cdot675+1$이므로 $\dfrac{2026\pi}{3}=675\pi+\dfrac\pi3$이고, $675$가 홀수라 $675\pi\equiv\pi\pmod{2\pi}$입니다. 따라서 남는 각은 $\pi+\dfrac\pi3=\dfrac{4\pi}{3}$입니다.
> $$z^{2026}=2^{2026}\operatorname{cis}\frac{4\pi}{3}=2^{2026}\left(-\frac12-\frac{\sqrt3}{2}i\right)$$
> 검산합니다. $\dfrac{4\pi}{3}$은 제3사분면의 각이므로 실수부와 허수부가 모두 음수여야 하고 위 결과가 그 조건에 맞습니다. 지수를 각의 주기로 환원할 때 홀수 배의 $\pi$를 놓치는 것이 가장 흔한 실수입니다.

> **문제 3.** (표준) $-64$의 여섯제곱근을 모두 구하고 복소평면에서의 배치를 말하십시오.
> **답.** $2\operatorname{cis}\dfrac{(2k+1)\pi}{6}$($k=0,\dots,5$), 곧 $\sqrt3+i,\ 2i,\ -\sqrt3+i,\ -\sqrt3-i,\ -2i,\ \sqrt3-i$입니다.
> **풀이.** $-64=64\operatorname{cis}\pi$이므로 $n$제곱근 공식이 다음을 줍니다.
> $$w_k=64^{1/6}\operatorname{cis}\frac{\pi+2\pi k}{6}=2\operatorname{cis}\frac{(2k+1)\pi}{6},\qquad k=0,1,\dots,5$$
> 각 $k$를 차례로 대입합니다.
> $$w_0=2\operatorname{cis}\frac\pi6=\sqrt3+i,\qquad w_1=2\operatorname{cis}\frac\pi2=2i,\qquad w_2=2\operatorname{cis}\frac{5\pi}6=-\sqrt3+i$$
> $$w_3=2\operatorname{cis}\frac{7\pi}6=-\sqrt3-i,\qquad w_4=2\operatorname{cis}\frac{3\pi}2=-2i,\qquad w_5=2\operatorname{cis}\frac{11\pi}6=\sqrt3-i$$
> 여섯 근은 모두 절댓값이 $2$이고 각이 $\dfrac\pi3$씩 벌어져 있으므로 반지름 $2$인 원에 내접한 정육각형의 꼭짓점을 이룹니다. 검산으로 한 근을 여섯제곱하면 $\left(2\operatorname{cis}\dfrac\pi6\right)^6=64\operatorname{cis}\pi=-64$이고, 여섯 근의 합은 정육각형의 대칭성으로 $0$입니다. 켤레쌍 $w_0$과 $w_5$, $w_2$와 $w_3$, 그리고 $w_1$과 $w_4$가 각각 상쇄되는 것으로도 확인됩니다.

> **문제 4.** (표준) 방정식 $z^4=-1$의 네 근을 구하고, 이를 이용해 $z^4+1$을 두 실계수 이차식의 곱으로 인수분해하십시오.
> **답.** 근은 $\operatorname{cis}\dfrac{(2k+1)\pi}{4}$이고 $z^4+1=(z^2-\sqrt2 z+1)(z^2+\sqrt2 z+1)$입니다.
> **풀이.** $-1=\operatorname{cis}\pi$이므로 네제곱근 공식이 곧바로 근을 줍니다.
> $$z_k=\operatorname{cis}\frac{(2k+1)\pi}{4}=\frac{\pm1\pm i}{\sqrt2},\qquad k=0,1,2,3$$
> 네 근은 단위원 위에서 $90^\circ$씩 벌어진 정사각형의 꼭짓점입니다. 실계수 인수를 만들려면 켤레인 근끼리 짝지어야 합니다. $\operatorname{cis}\dfrac\pi4$와 $\operatorname{cis}\left(-\dfrac\pi4\right)$는 합이 $2\cos\dfrac\pi4=\sqrt2$이고 곱이 $1$이므로 $z^2-\sqrt2 z+1$을 줍니다. 남은 짝 $\operatorname{cis}\dfrac{3\pi}4$와 $\operatorname{cis}\left(-\dfrac{3\pi}4\right)$는 합이 $2\cos\dfrac{3\pi}4=-\sqrt2$, 곱이 $1$이라 $z^2+\sqrt2 z+1$을 줍니다.
> $$z^4+1=(z^2-\sqrt2 z+1)(z^2+\sqrt2 z+1)$$
> 검산합니다. 우변은 합과 차의 곱 꼴이라 $(z^2+1)^2-(\sqrt2 z)^2=z^4+2z^2+1-2z^2=z^4+1$입니다. 실계수 다항식의 복소근이 항상 켤레쌍으로 나온다는 사실이 이 인수분해의 근거입니다.

> **문제 5.** (심화) 이차방정식 $z^2-(3+2i)z+(5+i)=0$을 푸십시오.
> **답.** $z=2+3i$ 또는 $z=1-i$입니다.
> **풀이.** 근의 공식을 그대로 쓰되 판별식의 제곱근을 복소수 범위에서 구합니다.
> $$D=(3+2i)^2-4(5+i)=(5+12i)-(20+4i)=-15+8i$$
> $\sqrt{D}=x+yi$로 두고 $(x+yi)^2=-15+8i$의 실수부와 허수부를 비교하면 두 식이 나오고, 여기에 절댓값 조건을 하나 더 얹습니다.
> $$x^2-y^2=-15,\qquad 2xy=8,\qquad x^2+y^2=\lvert-15+8i\rvert=\sqrt{225+64}=17$$
> 첫째 식과 셋째 식을 더하면 $2x^2=2$이라 $x^2=1$이고, 빼면 $2y^2=32$이라 $y^2=16$입니다. $xy=4>0$이라 두 부호가 같으므로 $\sqrt D=1+4i$입니다. 실제로 $(1+4i)^2=1+8i-16=-15+8i$로 맞습니다.
> $$z=\frac{(3+2i)\pm(1+4i)}{2}=\frac{4+6i}{2}\ \text{또는}\ \frac{2-2i}{2}$$
> 따라서 $z=2+3i$ 또는 $z=1-i$입니다. 근과 계수의 관계로 검산합니다. 두 근의 합은 $(2+3i)+(1-i)=3+2i$이고 곱은 $(2+3i)(1-i)=2-2i+3i-3i^2=5+i$이므로 원식의 계수와 정확히 맞습니다.

> **문제 6.** (심화) $\lvert z-2\rvert=2\lvert z+1\rvert$을 만족하는 $z=x+iy$의 자취를 구하십시오.
> **답.** 중심 $(-2,0)$, 반지름 $2$인 원 $(x+2)^2+y^2=4$입니다.
> **풀이.** 양변이 모두 음이 아니므로 제곱해도 동치입니다.
> $$(x-2)^2+y^2=4\bigl((x+1)^2+y^2\bigr)$$
> 좌변은 $x^2-4x+4+y^2$이고 우변은 $4x^2+8x+4+4y^2$입니다. 우변에서 좌변을 빼면 이차항의 계수가 살아남습니다.
> $$0=3x^2+3y^2+12x\quad\Longrightarrow\quad x^2+4x+y^2=0$$
> $x$에 대해 완전제곱하면 다음을 얻습니다.
> $$(x+2)^2+y^2=4$$
> 두 정점에 이르는 거리의 비가 일정한 점들의 자취라서 아폴로니우스 원이 나옵니다. 검산합니다. $z=0$이면 $\lvert0-2\rvert=2$이고 $2\lvert0+1\rvert=2$로 원식이 성립하며 $(0+2)^2+0^2=4$로 원 위에 있습니다. $z=-4$도 $\lvert-6\rvert=6$, $2\lvert-3\rvert=6$으로 성립합니다.

> **문제 7.** (심화) 방정식 $z^5=\bar z$의 모든 해를 구하십시오.
> **답.** $z=0$과 $1$의 여섯제곱근 $\operatorname{cis}\dfrac{\pi k}{3}$($k=0,\dots,5$)로 모두 $7$개입니다.
> **풀이.** $z=0$은 양변이 $0$이라 해입니다. $z\ne0$인 해를 찾습니다. 양변에 절댓값을 취하면 $\lvert z\rvert^5=\lvert\bar z\rvert=\lvert z\rvert$이므로 $\lvert z\rvert^4=1$, 곧 $\lvert z\rvert=1$입니다. 절댓값이 $1$이면 $\bar z=\dfrac1z$이므로 원식은 다음이 됩니다.
> $$z^5=\frac1z\quad\Longleftrightarrow\quad z^6=1$$
> 따라서 $z\ne0$인 해는 $1$의 여섯제곱근이며 단위원을 여섯 등분한 점들입니다.
> $$z=\operatorname{cis}\frac{2\pi k}{6}=\operatorname{cis}\frac{\pi k}{3},\qquad k=0,1,\dots,5$$
> 전체 해는 $z=0$을 포함해 $7$개입니다. 극형식으로 검산합니다. $\lvert z\rvert=1$일 때 $z=\operatorname{cis}\theta$이면 $z^5=\operatorname{cis}5\theta$, $\bar z=\operatorname{cis}(-\theta)$이므로 $5\theta\equiv-\theta$, 곧 $6\theta\equiv0\pmod{2\pi}$이고 위와 같은 각들이 나옵니다. $\square$

## 2강. 복소함수와 오일러 공식

> **문제 8.** (표준) $\left(\dfrac{1+i\sqrt3}{1-i}\right)^{12}$을 오일러 표기로 계산하십시오.
> **답.** $-64$입니다.
> **풀이.** 분자와 분모를 각각 지수꼴로 바꿉니다. $1+i\sqrt3=2e^{i\pi/3}$이고 $1-i=\sqrt2\,e^{-i\pi/4}$입니다. 몫은 지수의 차로 정리됩니다.
> $$\frac{2e^{i\pi/3}}{\sqrt2\,e^{-i\pi/4}}=\sqrt2\,e^{i\left(\frac\pi3+\frac\pi4\right)}=\sqrt2\,e^{i\frac{7\pi}{12}}$$
> 여기에 $12$제곱을 취하면 크기는 $(\sqrt2)^{12}=2^6=64$이고 각은 $12\cdot\dfrac{7\pi}{12}=7\pi$입니다.
> $$\left(\sqrt2\,e^{i7\pi/12}\right)^{12}=64\,e^{i7\pi}=64\,e^{i\pi}=-64$$
> $7\pi=6\pi+\pi$이므로 $e^{i7\pi}=e^{i\pi}=-1$을 썼습니다. 검산합니다. 결과의 절댓값은 다음과 같이 크기만 따로 계산해도 같습니다.
> $$\left\lvert\frac{1+i\sqrt3}{1-i}\right\rvert^{12}=\left(\frac{2}{\sqrt2}\right)^{12}=(\sqrt2)^{12}=2^6=64$$
> 편각만 따로 보면 $12\cdot\dfrac{7\pi}{12}=7\pi\equiv\pi$이라 결과가 음의 실수축 위에 놓이고, 실제로 $-64$가 그 조건에 맞습니다.

> **문제 9.** (표준) 드무아브르 정리로 $\sin5\theta$를 $\sin\theta$만의 다항식으로 나타내십시오.
> **답.** $\sin5\theta=16\sin^5\theta-20\sin^3\theta+5\sin\theta$입니다.
> **풀이.** $\left(e^{i\theta}\right)^5=e^{i5\theta}$이므로 $(\cos\theta+i\sin\theta)^5=\cos5\theta+i\sin5\theta$입니다. 좌변을 이항전개하면 $i$의 홀수 거듭제곱 항이 허수부에 모입니다.
> $$\sin5\theta=\binom51\cos^4\theta\sin\theta-\binom53\cos^2\theta\sin^3\theta+\binom55\sin^5\theta=5\cos^4\theta\sin\theta-10\cos^2\theta\sin^3\theta+\sin^5\theta$$
> 부호는 $(i\sin\theta)^1,(i\sin\theta)^3,(i\sin\theta)^5$이 각각 $+,-,+$를 주기 때문입니다. 이제 $\cos^2\theta=1-\sin^2\theta$를 넣고 $s=\sin\theta$로 두어 정리합니다.
> $$5(1-s^2)^2s-10(1-s^2)s^3+s^5=\left(5s-10s^3+5s^5\right)-\left(10s^3-10s^5\right)+s^5$$
> $$=5s-20s^3+16s^5$$
> 따라서 $\sin5\theta=16\sin^5\theta-20\sin^3\theta+5\sin\theta$입니다. 검산합니다. $\theta=\dfrac\pi2$이면 좌변이 $\sin\dfrac{5\pi}2=1$이고 우변이 $16-20+5=1$입니다. $\theta=\dfrac\pi6$이면 좌변이 $\sin\dfrac{5\pi}6=\dfrac12$이고 우변이 $\dfrac{16}{32}-\dfrac{20}{8}+\dfrac52=\dfrac12$로 일치합니다. $\square$

> **문제 10.** (표준) 오일러 공식으로 $\cos^4\theta=\dfrac18\bigl(\cos4\theta+4\cos2\theta+3\bigr)$을 유도하십시오.
> **답.** 위 선형화 공식이 성립합니다.
> **풀이.** $\cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}{2}$이므로 네제곱은 다음과 같습니다.
> $$\cos^4\theta=\frac{1}{16}\left(e^{i\theta}+e^{-i\theta}\right)^4$$
> 괄호를 이항전개합니다. 지수가 $\pm4\theta,\pm2\theta,0$으로만 나타나는 것이 핵심입니다.
> $$\left(e^{i\theta}+e^{-i\theta}\right)^4=e^{i4\theta}+4e^{i2\theta}+6+4e^{-i2\theta}+e^{-i4\theta}$$
> 켤레인 항끼리 묶으면 $e^{i4\theta}+e^{-i4\theta}=2\cos4\theta$이고 $4\left(e^{i2\theta}+e^{-i2\theta}\right)=8\cos2\theta$이므로 전체는 $2\cos4\theta+8\cos2\theta+6$이 됩니다.
> $$\cos^4\theta=\frac{2\cos4\theta+8\cos2\theta+6}{16}=\frac{\cos4\theta+4\cos2\theta+3}{8}$$
> 거듭제곱을 배각의 일차결합으로 바꾸는 이 방향을 선형화라 하며, 적분이나 푸리에 계산에서 표준으로 씁니다. 검산합니다. $\theta=0$이면 좌변이 $1$, 우변이 $\dfrac{1+4+3}{8}=1$입니다. $\theta=\dfrac\pi4$이면 좌변이 $\dfrac14$, 우변이 $\dfrac{-1+0+3}{8}=\dfrac14$로 일치합니다. $\square$

> **문제 11.** (심화) $\operatorname{Log}(-i)$의 주값을 구하고 $(-i)^{i}$의 주값이 실수 $e^{\pi/2}$임을 보이십시오.
> **답.** $\operatorname{Log}(-i)=-i\dfrac\pi2$이고 $(-i)^{i}=e^{\pi/2}$입니다.
> **풀이.** $-i=1\cdot\operatorname{cis}\left(-\dfrac\pi2\right)$이므로 $\lvert-i\rvert=1$이고 $\operatorname{Arg}(-i)=-\dfrac\pi2$입니다. 주로그의 정의에 넣습니다.
> $$\operatorname{Log}(-i)=\ln1+i\left(-\frac\pi2\right)=-i\frac\pi2$$
> 복소거듭제곱은 $z^{w}=e^{w\log z}$로 정의하고 주값은 $\operatorname{Log}$를 씁니다.
> $$(-i)^{i}=e^{i\operatorname{Log}(-i)}=e^{i\cdot\left(-i\frac\pi2\right)}=e^{\pi/2}$$
> $i\cdot(-i)=1$이라 지수가 실수 $\dfrac\pi2$가 되었고, 값은 $e^{\pi/2}\approx4.8105$입니다. 순허수를 순허수 제곱한 결과가 실수가 된다는 점이 복소거듭제곱의 특징입니다. 다른 분지를 쓰면 $\operatorname{Arg}$ 대신 $-\dfrac\pi2+2\pi k$가 들어가 값이 $e^{\pi/2-2\pi k}$로 바뀌므로, 주값임을 반드시 밝혀야 합니다. $\square$

> **문제 12.** (심화) $2^{i}$의 모든 값을 구하고 주값을 쓰십시오.
> **답.** $2^{i}=e^{-2\pi k}\bigl(\cos(\ln2)+i\sin(\ln2)\bigr)$($k\in\mathbb Z$)이고 주값은 $\cos(\ln2)+i\sin(\ln2)$입니다.
> **풀이.** 정의에 따라 $2^{i}=e^{i\log2}$입니다. $2$는 양의 실수라 절댓값이 $2$이고 편각이 $2\pi k$이므로 로그의 모든 값은 $\log2=\ln2+2\pi k i$입니다.
> $$2^{i}=e^{i(\ln2+2\pi ki)}=e^{i\ln2-2\pi k}=e^{-2\pi k}\bigl(\cos(\ln2)+i\sin(\ln2)\bigr)$$
> $k=0$인 주값은 다음과 같습니다.
> $$2^{i}\big\vert_{\text{주값}}=\cos(\ln2)+i\sin(\ln2)\approx0.7692+0.6390\,i$$
> 밑이 양의 실수여도 지수가 허수이면 값이 무한히 많아진다는 것이 요점입니다. 검산합니다. 주값의 절댓값은 $\sqrt{\cos^2(\ln2)+\sin^2(\ln2)}=1$이고, 일반값의 절댓값은 $e^{-2\pi k}$로 $k$에 따라 기하급수적으로 갈라집니다. $\square$

> **문제 13.** (심화) $1$의 다섯제곱근의 합이 $0$임을 이용해 $\cos\dfrac{2\pi}{5}=\dfrac{-1+\sqrt5}{4}$를 구하십시오.
> **답.** $\cos\dfrac{2\pi}{5}=\dfrac{-1+\sqrt5}{4}$이며 중간 관계는 $\cos\dfrac{2\pi}5+\cos\dfrac{4\pi}5=-\dfrac12$입니다.
> **풀이.** $1$의 다섯제곱근은 $\zeta_k=e^{i2\pi k/5}$($k=0,\dots,4$)이고 합이 $0$입니다. $k$와 $5-k$가 켤레쌍이므로 실수부의 합은 다음이 됩니다.
> $$1+2\cos\frac{2\pi}5+2\cos\frac{4\pi}5=0\quad\Longrightarrow\quad \cos\frac{2\pi}5+\cos\frac{4\pi}5=-\frac12$$
> $c=\cos\dfrac{2\pi}5$로 두고 배각공식 $\cos\dfrac{4\pi}5=2c^2-1$을 넣습니다.
> $$c+2c^2-1=-\frac12\quad\Longrightarrow\quad 4c^2+2c-1=0$$
> $\dfrac{2\pi}5$은 예각이라 $c>0$이므로 이차방정식의 양의 근을 취합니다.
> $$c=\frac{-2+\sqrt{4+16}}{8}=\frac{-2+2\sqrt5}{8}=\frac{-1+\sqrt5}{4}$$
> 수치로 확인하면 $\dfrac{-1+2.2360}{4}\approx0.3090$이고 $\cos72^\circ\approx0.3090$으로 일치합니다. 정오각형을 자와 컴퍼스로 작도할 수 있는 근거가 이 값이 제곱근만으로 표현된다는 사실입니다. $\square$

> **문제 14.** (심화) 오일러 공식으로 디리클레 핵 $1+2\displaystyle\sum_{k=1}^{n}\cos k\theta=\dfrac{\sin\left(\left(n+\frac12\right)\theta\right)}{\sin(\theta/2)}$을 유도하십시오($\theta$는 $2\pi$의 배수가 아닙니다).
> **답.** 위 등식이 성립합니다.
> **풀이.** 대칭 구간의 지수합 $S=\displaystyle\sum_{k=-n}^{n}e^{ik\theta}$를 봅니다. 이는 첫 항이 $e^{-in\theta}$, 공비가 $e^{i\theta}$, 항이 $2n+1$개인 등비수열의 합입니다.
> $$S=e^{-in\theta}\cdot\frac{e^{i(2n+1)\theta}-1}{e^{i\theta}-1}=\frac{e^{i(n+1)\theta}-e^{-in\theta}}{e^{i\theta}-1}$$
> 분자와 분모에 $e^{-i\theta/2}$를 곱해 반각을 대칭으로 맞춥니다.
> $$S=\frac{e^{i\left(n+\frac12\right)\theta}-e^{-i\left(n+\frac12\right)\theta}}{e^{i\theta/2}-e^{-i\theta/2}}=\frac{2i\sin\left(\left(n+\frac12\right)\theta\right)}{2i\sin(\theta/2)}=\frac{\sin\left(\left(n+\frac12\right)\theta\right)}{\sin(\theta/2)}$$
> 한편 같은 합을 켤레끼리 묶으면 $S=1+\displaystyle\sum_{k=1}^{n}\left(e^{ik\theta}+e^{-ik\theta}\right)=1+2\sum_{k=1}^{n}\cos k\theta$입니다. 두 표현이 같으므로 원식이 나옵니다. 검산합니다. $n=1$이면 좌변이 $1+2\cos\theta$이고, 우변은 $\dfrac{\sin(3\theta/2)}{\sin(\theta/2)}$인데 $\sin\dfrac{3\theta}2=\sin\dfrac\theta2\left(2\cos\theta+1\right)$이라 일치합니다. $\square$

## 스스로 점검

1. 복소수의 몫과 거듭제곱을 직교형식과 극형식 양쪽으로 계산하고 서로 검산하는가?
2. $n$제곱근을 빠짐없이 구하고 정$n$각형 배치와 실계수 인수분해로 이어 쓰는가?
3. 복소계수 이차방정식의 판별식에서 복소 제곱근을 절댓값 조건까지 써서 구하는가?
4. 거리 조건으로 주어진 자취를 원이나 직선의 방정식으로 정리하고 대입 검산을 하는가?
5. 드무아브르와 오일러 공식으로 $\sin n\theta$ 전개와 $\cos^n\theta$ 선형화를 양방향으로 다루는가?
6. 복소로그와 복소거듭제곱이 다가함수임을 알고 주값을 명시하는가?
7. 단위근의 합에서 삼각함수의 특수값과 급수의 닫힌 식을 뽑아내는가?

정답 요지: (1) 곱과 거듭제곱은 극형식이 빠르고, 결과는 직교형식으로 되돌려 확인합니다. (2) $w_k=r^{1/n}\operatorname{cis}\dfrac{\theta+2\pi k}{n}$로 $n$개를 모두 적고, 켤레쌍끼리 묶으면 실계수 이차식이 됩니다. (3) $x^2-y^2$, $2xy$, $x^2+y^2=\lvert D\rvert$의 세 식을 연립하고 $xy$의 부호로 분지를 정합니다. (4) 양변을 제곱해 정리한 뒤 완전제곱하며, 아폴로니우스 원은 두 거리의 비가 일정한 자취입니다. (5) $(\cos\theta+i\sin\theta)^n$의 실수부와 허수부를 비교하고, 역방향은 $\cos\theta=\dfrac{e^{i\theta}+e^{-i\theta}}{2}$의 거듭제곱을 켤레끼리 묶습니다. (6) $\log z=\ln\lvert z\rvert+i\arg z$와 $z^{w}=e^{w\log z}$는 다가이며 주값은 $\operatorname{Arg}$를 씁니다. (7) 단위근의 합이 $0$이라는 사실과 등비수열 합 공식이 특수값과 디리클레 핵을 함께 줍니다.

## 관련 강의

- [1. 복소수와 극형식](../1. 복소수와 극형식/index.md)
- [2. 복소함수와 오일러 공식](../2. 복소함수와 오일러 공식/index.md)
- [01. 복소수와 복소평면](../index.md)
