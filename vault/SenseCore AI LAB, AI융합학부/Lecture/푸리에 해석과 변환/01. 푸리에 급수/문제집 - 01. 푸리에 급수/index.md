---
title: "문제집 - 01. 푸리에 급수"
---
# 문제집 - 01. 푸리에 급수

1단원의 세 강의(1강 주기함수와 삼각함수계의 직교성, 2강 푸리에 계수와 수렴 정리, 3강 복소 푸리에 급수와 스펙트럼)를 강의별로 묶은 문제집입니다. 각 문제는 문제·답·풀이 세 줄로 되어 있고, 본문 강의에 실린 드릴과 겹치지 않도록 모두 새로 지었으며 난이도를 한 단계 올렸습니다. 규약은 본문과 같습니다. 기준 구간은 $[-L,L]$이고 주기는 $2L$이며, 실계수는 $a_n=\tfrac1L\int_{-L}^{L}f(x)\cos\tfrac{n\pi x}{L}dx$와 $b_n=\tfrac1L\int_{-L}^{L}f(x)\sin\tfrac{n\pi x}{L}dx$로, 복소 계수는 $c_n=\tfrac{1}{2L}\int_{-L}^{L}f(x)e^{-in\pi x/L}dx$로 계산합니다. 상수항은 급수에서 $a_0/2$로 씁니다. 별도 언급이 없으면 $L=\pi$입니다. 계산 문항은 적분을 끝까지 손으로 밀어 값을 확인하고, 증명 문항은 논리 전개를 스스로 다시 써 보는 것이 좋습니다.

## 1강. 주기함수와 삼각함수계의 직교성

> **문제 1.** (표준) $L=\pi$에서 $f(x)=3\cos 2x-4\sin 5x$의 노름 $\lVert f\rVert$를 구하십시오.
> **답.** $5\sqrt{\pi}$입니다.
> **풀이.** 노름의 제곱을 전개하면 교차항 $-24\int_{-\pi}^{\pi}\cos2x\sin5x\,dx$가 나오는데, 코사인과 사인의 혼합 내적은 직교성에 의해 0이므로 사라집니다.
> $$\lVert f\rVert^{2}=9\lVert\cos2x\rVert^{2}+16\lVert\sin5x\rVert^{2}=9\pi+16\pi=25\pi$$
> 두 노름 제곱이 모두 $L=\pi$이므로 위 값이 나오고 $\lVert f\rVert=5\sqrt\pi$입니다. 직교 성분의 노름이 성분별 제곱합으로 계산된다는 점에서 이 계산은 함수 공간의 피타고라스 정리입니다.

> **문제 2.** (표준) $\displaystyle\int_{-\pi}^{\pi}\sin^{2}(2x)\cos(4x)\,dx$를 구하십시오.
> **답.** $-\dfrac{\pi}{2}$입니다.
> **풀이.** 배각공식으로 $\sin^{2}2x=\tfrac{1-\cos4x}{2}$이므로 피적분함수를 다음처럼 쪼갤 수 있습니다.
> $$\sin^{2}(2x)\cos(4x)=\frac{\cos4x}{2}-\frac{\cos^{2}4x}{2}$$
> 첫 항의 적분은 $\int_{-\pi}^{\pi}\cos4x\,dx=0$이고, 둘째 항은 $m=n=4$인 코사인 곱이므로 직교성 정리에 의해 $\int_{-\pi}^{\pi}\cos^{2}4x\,dx=\pi$입니다. 따라서 값은 $0-\tfrac12\cdot\pi=-\tfrac\pi2$입니다. 제곱 항을 배각으로 낮추면 삼각함수계의 직교성만으로 적분이 끝난다는 점이 요령입니다.

> **문제 3.** (표준) $\cos^{4}x$를 삼각다항식으로 전개해 푸리에 계수를 모두 적고 $\displaystyle\int_{-\pi}^{\pi}\cos^{4}x\,dx$를 구하십시오.
> **답.** $\cos^{4}x=\tfrac38+\tfrac12\cos2x+\tfrac18\cos4x$이므로 $a_0=\tfrac34$, $a_2=\tfrac12$, $a_4=\tfrac18$이고 적분값은 $\tfrac{3\pi}{4}$입니다.
> **풀이.** $\cos^{2}x=\tfrac{1+\cos2x}{2}$를 제곱하고 다시 $\cos^{2}2x=\tfrac{1+\cos4x}{2}$를 넣습니다.
> $$\cos^{4}x=\frac{1+2\cos2x+\cos^{2}2x}{4}=\frac{3}{8}+\frac{\cos2x}{2}+\frac{\cos4x}{8}$$
> 유한 삼각다항식의 푸리에 급수는 자기 자신이므로 상수항 $a_0/2=\tfrac38$에서 $a_0=\tfrac34$이고 나머지 계수는 전개식의 계수 그대로입니다. 적분은 코사인 항이 모두 사라지므로 $\tfrac38\cdot2\pi=\tfrac{3\pi}{4}$입니다. 파르세발 등식으로 검산하면 좌변은 $\tfrac{(3/4)^2}{2}+(\tfrac12)^2+(\tfrac18)^2=\tfrac{35}{64}$이고, 우변은 $\tfrac1\pi\int_{-\pi}^{\pi}\cos^{8}x\,dx=\tfrac1\pi\cdot\tfrac{35\pi}{64}=\tfrac{35}{64}$로 일치합니다.

> **문제 4.** (심화) $f(x)=\cos\dfrac{2\pi x}{3}+\sin\dfrac{\pi x}{2}$의 기본주기를 구하십시오.
> **답.** $12$입니다.
> **풀이.** $T$가 주기라고 두고 덧셈정리로 $f(x+T)$를 펼칩니다.
> $$f(x+T)=\cos\tfrac{2\pi T}{3}\cos\tfrac{2\pi x}{3}-\sin\tfrac{2\pi T}{3}\sin\tfrac{2\pi x}{3}+\cos\tfrac{\pi T}{2}\sin\tfrac{\pi x}{2}+\sin\tfrac{\pi T}{2}\cos\tfrac{\pi x}{2}$$
> 네 함수 $\cos\tfrac{2\pi x}{3}$, $\sin\tfrac{2\pi x}{3}$, $\cos\tfrac{\pi x}{2}$, $\sin\tfrac{\pi x}{2}$는 서로 다른 진동수를 가지므로 일차독립입니다. 따라서 $f(x+T)=f(x)$가 모든 $x$에서 성립하려면 계수가 항별로 일치해야 하고, 이는 $\cos\tfrac{2\pi T}{3}=1$과 $\sin\tfrac{2\pi T}{3}=0$, 그리고 $\cos\tfrac{\pi T}{2}=1$과 $\sin\tfrac{\pi T}{2}=0$을 뜻합니다. 앞 조건은 $T$가 3의 배수임을, 뒤 조건은 $T$가 4의 배수임을 줍니다. 두 조건을 함께 만족하는 최소 양수는 $12$이므로 기본주기는 12입니다. $T=6$을 넣으면 사인 항의 부호가 뒤집혀 실제로 주기가 아님을 바로 확인할 수 있습니다. $\square$

> **문제 5.** (심화) 자연수 $m,n\ge0$에 대해 $\displaystyle\int_{0}^{L}\sin\frac{(2m+1)\pi x}{2L}\sin\frac{(2n+1)\pi x}{2L}\,dx=\frac{L}{2}\delta_{mn}$임을 증명하십시오.
> **답.** 반구간 $[0,L]$에서 홀수 반파장 사인계도 서로 직교하며 노름 제곱은 $L/2$입니다.
> **풀이.** 곱-합 공식 $\sin A\sin B=\tfrac12[\cos(A-B)-\cos(A+B)]$를 적용합니다. 두 각의 차는 $\tfrac{(m-n)\pi x}{L}$이고 합은 $\tfrac{(m+n+1)\pi x}{L}$이므로
> $$\int_{0}^{L}\sin\tfrac{(2m+1)\pi x}{2L}\sin\tfrac{(2n+1)\pi x}{2L}dx=\frac12\int_{0}^{L}\cos\frac{(m-n)\pi x}{L}dx-\frac12\int_{0}^{L}\cos\frac{(m+n+1)\pi x}{L}dx$$
> 입니다. 0이 아닌 정수 $k$에 대해 $\int_{0}^{L}\cos\tfrac{k\pi x}{L}dx=\tfrac{L}{k\pi}\sin k\pi=0$이고, $k=0$이면 값이 $L$입니다. $m\ne n$이면 $m-n\ne0$이고 $m+n+1\ge1$이므로 두 적분이 함께 0이 되어 전체가 0입니다. $m=n$이면 첫 적분만 $k=0$에 해당해 $L$이 되고 둘째 적분은 $k=2m+1\ne0$이라 0이므로 값은 $L/2$입니다. 이 계는 $x=0$에서 0이고 $x=L$에서 도함수가 0인 경계조건에 맞는 전개에 쓰입니다. $\square$

> **문제 6.** (심화) $L=\pi$에서 $\langle x^{3},\sin nx\rangle$을 끝까지 계산하고 $f(x)=x^{3}$을 $\sin x$와 $\sin2x$의 일차결합으로 최적 근사하십시오.
> **답.** $\langle x^{3},\sin nx\rangle=2\pi(-1)^{n}\left(\dfrac{6}{n^{3}}-\dfrac{\pi^{2}}{n}\right)$이고 최적 근사는 $2(\pi^{2}-6)\sin x+\left(\tfrac32-\pi^{2}\right)\sin2x$입니다.
> **풀이.** $x^{3}\sin nx$는 짝함수이므로 $\langle x^{3},\sin nx\rangle=2\int_{0}^{\pi}x^{3}\sin nx\,dx$입니다. 부분적분을 세 단계로 밀면 먼저 $\int_{0}^{\pi}x\sin nx\,dx=-\tfrac{\pi(-1)^{n}}{n}$이고, 이를 써서 $\int_{0}^{\pi}x^{2}\cos nx\,dx=-\tfrac2n\int_{0}^{\pi}x\sin nx\,dx=\tfrac{2\pi(-1)^{n}}{n^{2}}$입니다. 마지막으로
> $$\int_{0}^{\pi}x^{3}\sin nx\,dx=\left[-\frac{x^{3}\cos nx}{n}\right]_{0}^{\pi}+\frac3n\int_{0}^{\pi}x^{2}\cos nx\,dx=-\frac{\pi^{3}(-1)^{n}}{n}+\frac{6\pi(-1)^{n}}{n^{3}}$$
> 이므로 두 배 하면 답의 식이 됩니다. 사영 계수는 노름 제곱 $\pi$로 나눈 $c_n=2(-1)^{n}\left(\tfrac{6}{n^{3}}-\tfrac{\pi^{2}}{n}\right)$이고, $n=1$에서 $2(\pi^{2}-6)\approx7.739$, $n=2$에서 $2\left(\tfrac68-\tfrac{\pi^{2}}{2}\right)=\tfrac32-\pi^{2}\approx-8.370$입니다. 계수가 $1/n$ 규모로만 줄어드는 이유는 주기 확장한 $x^{3}$이 $x=\pm\pi$에서 도약하기 때문입니다.

> **문제 7.** (심화) $[-1,1]$의 내적에서 $1,x,x^{2}$을 그람-슈미트 방식으로 직교화하고 각 함수의 노름 제곱을 구하십시오.
> **답.** 직교계는 $1$, $x$, $x^{2}-\tfrac13$이고 노름 제곱은 각각 $2$, $\tfrac23$, $\tfrac{8}{45}$입니다.
> **풀이.** $\langle1,x\rangle=\int_{-1}^{1}x\,dx=0$이므로 처음 두 함수는 이미 직교합니다. 세 번째 함수에서 앞의 두 방향 성분을 뺍니다. $\langle x^{2},1\rangle=\int_{-1}^{1}x^{2}dx=\tfrac23$이고 $\lVert1\rVert^{2}=2$이므로 상수 방향 성분은 $\tfrac13$이며, $\langle x^{2},x\rangle=\int_{-1}^{1}x^{3}dx=0$이므로 $x$ 방향 성분은 없습니다. 따라서 $p_2(x)=x^{2}-\tfrac13$입니다. 노름 제곱은
> $$\lVert p_2\rVert^{2}=\int_{-1}^{1}\left(x^{4}-\tfrac23x^{2}+\tfrac19\right)dx=\frac25-\frac49+\frac29=\frac25-\frac29=\frac{8}{45}$$
> 입니다. 이 결과는 르장드르 다항식의 처음 세 항과 상수배만큼만 다르며, 삼각함수계가 아닌 다항식계에서도 직교화가 같은 사영 계산으로 이루어짐을 보여 줍니다. $\square$

## 2강. 푸리에 계수와 수렴 정리

> **문제 8.** (표준) $f(x)=x(L-x)$를 $[0,L]$에서 사인 급수로 전개하십시오.
> **답.** $b_n=\dfrac{4L^{2}\bigl(1-(-1)^{n}\bigr)}{n^{3}\pi^{3}}$이므로 홀수 $n$에서 $\dfrac{8L^{2}}{n^{3}\pi^{3}}$이고 짝수 $n$에서 0입니다.
> **풀이.** $k=n\pi/L$이라 두면 $kL=n\pi$이므로 $\cos kL=(-1)^{n}$이고 $\sin kL=0$입니다. 부분적분으로 $\int_{0}^{L}x\sin kx\,dx=-\tfrac{L(-1)^{n}}{k}$이고 $\int_{0}^{L}x\cos kx\,dx=-\tfrac{1-(-1)^{n}}{k^{2}}$이며, 이를 다시 써서 $\int_{0}^{L}x^{2}\sin kx\,dx=-\tfrac{L^{2}(-1)^{n}}{k}-\tfrac{2(1-(-1)^{n})}{k^{3}}$입니다. 따라서
> $$\int_{0}^{L}\bigl(Lx-x^{2}\bigr)\sin kx\,dx=-\frac{L^{2}(-1)^{n}}{k}+\frac{L^{2}(-1)^{n}}{k}+\frac{2\bigl(1-(-1)^{n}\bigr)}{k^{3}}=\frac{2\bigl(1-(-1)^{n}\bigr)}{k^{3}}$$
> 이고 $b_n=\tfrac2L$을 곱하면 답이 됩니다. 계수가 $1/n^{3}$으로 빠르게 줄어드는 까닭은 홀 확장한 함수가 연속이고 양 끝에서 값이 0이라 도약이 생기지 않기 때문입니다. 이 전개는 양 끝이 고정된 막대의 초기 온도분포를 다룰 때 그대로 쓰입니다.

> **문제 9.** (표준) 주기 $2\pi$이고 한 주기에서 $f(x)=x$ $(0<x<2\pi)$인 함수의 푸리에 급수를 구하고, $x=0$에서의 수렴값을 말한 뒤 파르세발 등식으로 $\sum1/n^{2}$을 구하십시오.
> **답.** $f(x)\sim\pi-2\sum_{n\ge1}\tfrac{\sin nx}{n}$이고 $x=0$에서 급수는 $\pi$로 수렴하며 $\sum1/n^{2}=\pi^{2}/6$입니다.
> **풀이.** 한 주기 적분 구간을 $[0,2\pi]$로 잡습니다. $a_0=\tfrac1\pi\int_{0}^{2\pi}x\,dx=2\pi$이고, 부분적분에서 경계항의 $\sin2n\pi$가 0이므로 $a_n=0$입니다.
> $$b_n=\frac1\pi\int_{0}^{2\pi}x\sin nx\,dx=\frac1\pi\left(\left[-\frac{x\cos nx}{n}\right]_{0}^{2\pi}+\frac1n\int_{0}^{2\pi}\cos nx\,dx\right)=-\frac2n$$
> 상수항이 $a_0/2=\pi$이므로 위 급수가 나옵니다. $x=0$은 도약점이고 $f(0^{+})=0$, $f(0^{-})=f(2\pi^{-})=2\pi$이므로 수렴값은 평균 $\pi$이며, 실제로 급수의 사인 항이 모두 0이라 값이 $\pi$입니다. 파르세발 등식의 우변은 $\tfrac1\pi\int_{0}^{2\pi}x^{2}dx=\tfrac{8\pi^{2}}{3}$이고 좌변은 $\tfrac{(2\pi)^{2}}{2}+\sum\tfrac{4}{n^{2}}=2\pi^{2}+4\sum\tfrac1{n^{2}}$입니다. 두 값을 같게 놓으면 $4\sum n^{-2}=\tfrac{2\pi^{2}}{3}$이므로 $\sum n^{-2}=\tfrac{\pi^{2}}{6}$입니다.

> **문제 10.** (심화) 반파 정류 사인, 곧 주기 $2\pi$이고 한 주기에서 $f(x)=\sin x$ $(0\le x\le\pi)$, $f(x)=0$ $(-\pi<x<0)$인 함수의 푸리에 급수를 구하십시오.
> **답.** $f(x)=\dfrac{1}{\pi}+\dfrac{\sin x}{2}-\dfrac{2}{\pi}\displaystyle\sum_{m=1}^{\infty}\frac{\cos 2mx}{4m^{2}-1}$입니다.
> **풀이.** 대칭성이 없으므로 코사인과 사인을 모두 계산합니다. $a_0=\tfrac1\pi\int_{0}^{\pi}\sin x\,dx=\tfrac2\pi$입니다. $n\ne1$에서 곱-합 공식 $\sin x\cos nx=\tfrac12[\sin((n+1)x)-\sin((n-1)x)]$과 $\int_{0}^{\pi}\sin kx\,dx=\tfrac{1-(-1)^{k}}{k}$를 쓰면
> $$a_n=\frac1\pi\int_{0}^{\pi}\sin x\cos nx\,dx=\frac{1+(-1)^{n}}{\pi\bigl(1-n^{2}\bigr)}$$
> 이므로 홀수 $n$에서는 0이고 $n=2m$에서 $a_{2m}=-\tfrac{2}{\pi(4m^{2}-1)}$입니다. $n=1$은 따로 계산해 $a_1=\tfrac{1}{2\pi}\int_{0}^{\pi}\sin2x\,dx=0$입니다. 사인 계수는 $b_1=\tfrac1\pi\int_{0}^{\pi}\sin^{2}x\,dx=\tfrac12$이고 $n\ge2$에서는 다음처럼 두 항이 함께 사라집니다.
> $$b_n=\frac{1}{2\pi}\int_{0}^{\pi}\Bigl[\cos\bigl((n-1)x\bigr)-\cos\bigl((n+1)x\bigr)\Bigr]dx=\frac{1}{2\pi}\left[\frac{\sin\bigl((n-1)\pi\bigr)}{n-1}-\frac{\sin\bigl((n+1)\pi\bigr)}{n+1}\right]=0$$
> 검산으로 $x=0$을 넣으면 $\tfrac1\pi-\tfrac2\pi\sum_m\tfrac{1}{4m^{2}-1}$이고 망원급수로 $\sum_m\tfrac{1}{4m^{2}-1}=\tfrac12$이므로 값이 0이 되어 $f(0)=0$과 맞습니다.

> **문제 11.** (심화) 전파 정류 사인 $f(x)=\lvert\sin x\rvert$의 푸리에 급수를 구하고 홀수 조파가 사라지는 이유를 설명하십시오.
> **답.** $\lvert\sin x\rvert=\dfrac{2}{\pi}-\dfrac{4}{\pi}\displaystyle\sum_{m=1}^{\infty}\frac{\cos2mx}{4m^{2}-1}$이며 기본주기가 $\pi$이므로 $2\pi$ 기준의 홀수 조파가 존재하지 않습니다.
> **풀이.** $f$가 짝함수이므로 $b_n=0$입니다. $a_0=\tfrac2\pi\int_{0}^{\pi}\sin x\,dx=\tfrac4\pi$이고, 문제 10에서 계산한 적분을 절반 구간의 두 배로 다시 쓰면 다음과 같습니다.
> $$a_n=\frac2\pi\int_{0}^{\pi}\sin x\cos nx\,dx=\frac{2}{\pi}\cdot\frac{1+(-1)^{n}}{1-n^{2}}$$
> 홀수 $n$에서는 분자가 0이고 $n=2m$에서 $a_{2m}=-\tfrac{4}{\pi(4m^{2}-1)}$이므로 위 급수를 얻습니다. 홀수 조파가 없는 구조적 이유는 $\lvert\sin(x+\pi)\rvert=\lvert\sin x\rvert$, 곧 기본주기가 $\pi$라는 사실입니다. 주기가 절반이면 $2\pi$를 기준으로 볼 때 짝수 번째 조파만 남습니다. 검산으로 $x=\pi/2$를 넣으면 $\sum_m\tfrac{(-1)^{m}}{4m^{2}-1}=\tfrac12-\tfrac\pi4$이므로 급수의 값은 $\tfrac2\pi-\tfrac4\pi\left(\tfrac12-\tfrac\pi4\right)=1$이 되어 $\lvert\sin(\pi/2)\rvert=1$과 맞습니다.

> **문제 12.** (심화) 문제 11의 결과에 파르세발 등식을 적용해 $\displaystyle\sum_{m=1}^{\infty}\frac{1}{\bigl(4m^{2}-1\bigr)^{2}}$을 구하십시오.
> **답.** $\dfrac{\pi^{2}-8}{16}$입니다.
> **풀이.** 우변은 $\tfrac1\pi\int_{-\pi}^{\pi}\sin^{2}x\,dx=\tfrac1\pi\cdot\pi=1$입니다. 좌변은 $a_0=\tfrac4\pi$와 $a_{2m}=-\tfrac{4}{\pi(4m^{2}-1)}$을 넣으면
> $$\frac{a_0^{2}}{2}+\sum_{m=1}^{\infty}a_{2m}^{2}=\frac{8}{\pi^{2}}+\frac{16}{\pi^{2}}\sum_{m=1}^{\infty}\frac{1}{\bigl(4m^{2}-1\bigr)^{2}}$$
> 입니다. 두 값을 같게 놓고 정리하면 $\sum_m(4m^{2}-1)^{-2}=\tfrac{\pi^{2}-8}{16}$입니다. 수치로 확인하면 $\tfrac{9.8696-8}{16}\approx0.11685$이고, 직접 몇 항을 더하면 $\tfrac19+\tfrac1{225}+\tfrac1{1225}+\cdots\approx0.1168$로 일치합니다. 같은 상수를 문제 10의 반파 정류 사인에 파르세발을 적용해도 얻을 수 있으므로 두 계산이 서로 검산이 됩니다.

> **문제 13.** (심화) 사각파의 부분합 $S_{2M-1}(x)=\dfrac{4}{\pi}\displaystyle\sum_{k=0}^{M-1}\frac{\sin\bigl((2k+1)x\bigr)}{2k+1}$에 대해 $S_{2M-1}'(x)=\dfrac{2\sin(2Mx)}{\pi\sin x}$임을 보이고 $x>0$에서 첫 극대점의 위치와 그 점의 값의 극한을 구하십시오.
> **답.** 첫 극대점은 $x=\dfrac{\pi}{2M}$이고 값의 극한은 $\dfrac{2}{\pi}\displaystyle\int_{0}^{\pi}\frac{\sin u}{u}du\approx1.1790$입니다.
> **풀이.** 항별로 미분하면 $S_{2M-1}'(x)=\tfrac4\pi\sum_{k=0}^{M-1}\cos((2k+1)x)$입니다. 이 합에 $2\sin x$를 곱하면 곱-합 공식에 의해 각 항이 두 사인의 차가 되어 망원으로 접힙니다.
> $$2\sin x\sum_{k=0}^{M-1}\cos\bigl((2k+1)x\bigr)=\sum_{k=0}^{M-1}\Bigl[\sin\bigl((2k+2)x\bigr)-\sin(2kx)\Bigr]=\sin(2Mx)$$
> 따라서 합은 $\tfrac{\sin2Mx}{2\sin x}$이고 도함수는 $\tfrac{2\sin2Mx}{\pi\sin x}$입니다. $0<x<\pi/(2M)$에서 분자와 분모가 모두 양수이므로 $S$는 증가하고, $x=\pi/(2M)$에서 분자가 처음 0이 되므로 이 점이 첫 극대점입니다. 그 점의 값은
> $$S_{2M-1}\!\left(\frac{\pi}{2M}\right)=\int_{0}^{\pi/2M}\frac{2\sin2Mt}{\pi\sin t}dt=\frac{2}{\pi}\int_{0}^{\pi}\frac{\sin u}{2M\sin\frac{u}{2M}}du$$
> 이고, $M\to\infty$에서 $2M\sin\tfrac{u}{2M}\to u$이므로 극한은 $\tfrac2\pi\int_{0}^{\pi}\tfrac{\sin u}{u}du\approx1.1790$입니다. 극대점의 위치는 0으로 가지만 높이는 1로 내려오지 않으므로 균등수렴이 깨지며, 이것이 깁스 현상의 정량적 내용입니다. $\square$

> **문제 14.** (심화) $L=\pi$인 문제 8의 사인 급수에 파르세발 등식을 적용해 $\sum_{n\ \text{홀수}}1/n^{6}$과 $\sum_{n\ge1}1/n^{6}$을 구하십시오.
> **답.** $\displaystyle\sum_{n\ \text{홀수}}\frac{1}{n^{6}}=\frac{\pi^{6}}{960}$이고 $\displaystyle\sum_{n\ge1}\frac{1}{n^{6}}=\frac{\pi^{6}}{945}$입니다.
> **풀이.** $L=\pi$이면 문제 8에서 홀수 $n$의 계수가 $b_n=\tfrac{8}{n^{3}\pi}$입니다. 홀 확장한 함수를 $g$라 하면 파르세발 등식의 우변은
> $$\frac1\pi\int_{-\pi}^{\pi}g^{2}dx=\frac2\pi\int_{0}^{\pi}\bigl(\pi x-x^{2}\bigr)^{2}dx=\frac2\pi\left(\frac{\pi^{5}}{3}-\frac{\pi^{5}}{2}+\frac{\pi^{5}}{5}\right)=\frac{2}{\pi}\cdot\frac{\pi^{5}}{30}=\frac{\pi^{4}}{15}$$
> 입니다. 좌변은 $\sum_{n\ \text{홀수}}\tfrac{64}{n^{6}\pi^{2}}$이므로 $\sum_{n\ \text{홀수}}n^{-6}=\tfrac{\pi^{6}}{960}$입니다. 이제 짝수 항을 분리합니다. $\sum_{n\ge1}n^{-6}=\sum_{n\ \text{홀수}}n^{-6}+\sum_{m\ge1}(2m)^{-6}$이고 마지막 합이 전체의 $\tfrac1{64}$이므로 $\tfrac{63}{64}\sum n^{-6}=\tfrac{\pi^{6}}{960}$이 되어 $\sum n^{-6}=\tfrac{\pi^{6}}{945}$입니다. 같은 분리를 2강에서 얻은 $\sum_{n\ \text{홀수}}n^{-4}=\tfrac{\pi^{4}}{96}$에 적용하면 $\tfrac{15}{16}\sum n^{-4}=\tfrac{\pi^{4}}{96}$에서 $\sum n^{-4}=\tfrac{\pi^{4}}{90}$이 나옵니다. $\square$

## 3강. 복소 푸리에 급수와 스펙트럼

> **문제 15.** (표준) $f(x)=\sin^{4}x$의 복소 계수를 모두 구하고 진폭 스펙트럼과 위상 스펙트럼을 적으십시오.
> **답.** $c_0=\tfrac38$, $c_{\pm2}=-\tfrac14$, $c_{\pm4}=\tfrac1{16}$이고 진폭은 $A_2=\tfrac12$, $A_4=\tfrac18$이며 위상은 $\varphi_2=\pi$, $\varphi_4=0$입니다.
> **풀이.** $\sin^{2}x=\tfrac{1-\cos2x}{2}$를 제곱하고 $\cos^{2}2x=\tfrac{1+\cos4x}{2}$를 넣습니다.
> $$\sin^{4}x=\frac{1-2\cos2x+\cos^{2}2x}{4}=\frac{3}{8}-\frac{\cos2x}{2}+\frac{\cos4x}{8}$$
> 유한 삼각다항식이므로 $c_0=\tfrac{a_0}{2}=\tfrac38$이고 $b_n=0$이므로 $c_{\pm n}=\tfrac{a_n}{2}$입니다. 곧 $c_{\pm2}=-\tfrac14$, $c_{\pm4}=\tfrac1{16}$입니다. 진폭은 $A_n=2\lvert c_n\rvert$이므로 $A_2=\tfrac12$, $A_4=\tfrac18$이고, $c_2$가 음의 실수이므로 위상은 $\pi$이며 $c_4$는 양의 실수이므로 위상은 0입니다. 홀수 조파가 하나도 없는 까닭은 $\sin^{4}x$의 기본주기가 $\pi$이기 때문입니다.

> **문제 16.** (표준) $f(x)=3\cos\left(x-\tfrac\pi4\right)+2\sin3x$의 복소 계수와 평균 전력을 구하십시오.
> **답.** $c_1=\tfrac32e^{-i\pi/4}$, $c_{-1}=\tfrac32e^{i\pi/4}$, $c_3=-i$, $c_{-3}=i$이고 평균 전력은 $\tfrac{13}{2}$입니다.
> **풀이.** 조파 형태 $A_n\cos(nx+\varphi_n)$과 $c_n=\tfrac{A_n}{2}e^{i\varphi_n}$의 대응을 그대로 씁니다. 첫 항은 $A_1=3$, $\varphi_1=-\tfrac\pi4$이므로 $c_1=\tfrac32e^{-i\pi/4}$입니다. 둘째 항은 $2\sin3x=2\cos\left(3x-\tfrac\pi2\right)$이므로 $A_3=2$, $\varphi_3=-\tfrac\pi2$이고 $c_3=e^{-i\pi/2}=-i$입니다. 실수 신호이므로 $c_{-n}=\overline{c_n}$이며 나머지 계수는 0입니다. 실계수로 검산하면 $3\cos\left(x-\tfrac\pi4\right)=\tfrac{3}{\sqrt2}\cos x+\tfrac{3}{\sqrt2}\sin x$이므로 다음이 성립합니다.
> $$c_1=\frac{a_1-ib_1}{2}=\frac{3}{2\sqrt2}(1-i)=\frac32e^{-i\pi/4}$$
> 평균 전력은 $\sum\lvert c_n\rvert^{2}=2\cdot\tfrac94+2\cdot1=\tfrac{13}{2}$이고, 조파 형태로 계산한 $\tfrac12(A_1^{2}+A_3^{2})=\tfrac12(9+4)=\tfrac{13}{2}$과 일치합니다.

> **문제 17.** (심화) $L=\pi$이고 한 주기에서 $f(x)=1$ $(\lvert x\rvert<d)$, $f(x)=0$ $(d<\lvert x\rvert<\pi)$인 펄스열의 복소 계수를 구하십시오. 여기서 $0<d<\pi$입니다.
> **답.** $c_0=\dfrac{d}{\pi}$이고 $n\ne0$에서 $c_n=\dfrac{\sin(nd)}{n\pi}$입니다.
> **풀이.** 정의에 넣으면 적분 구간이 $[-d,d]$로 줄어듭니다.
> $$c_n=\frac{1}{2\pi}\int_{-d}^{d}e^{-inx}dx=\frac{1}{2\pi}\left[\frac{e^{-inx}}{-in}\right]_{-d}^{d}=\frac{e^{ind}-e^{-ind}}{2\pi in}=\frac{\sin(nd)}{n\pi}$$
> 입니다. $n=0$이면 피적분함수가 1이므로 $c_0=\tfrac{2d}{2\pi}=\tfrac{d}{\pi}$이고, 이는 위 식의 $n\to0$ 극한과도 맞습니다. 계수가 모두 실수인 까닭은 $f$가 실 짝함수라 사인 성분이 없기 때문이며, 실계수로는 $a_n=2c_n=\tfrac{2\sin nd}{n\pi}$입니다. 계수열이 $\operatorname{sinc}$ 모양을 정수 지점에서 뽑은 값이라는 점이 중요합니다. $d$를 좁히면 $\sin(nd)$의 첫 영점이 멀어져 스펙트럼이 넓게 퍼지며, 이 경향이 2단원의 사각펄스 변환으로 이어집니다.

> **문제 18.** (심화) 문제 17의 결과에 복소 파르세발 등식을 적용해 $\displaystyle\sum_{n=1}^{\infty}\frac{\sin^{2}(nd)}{n^{2}}$을 구하십시오.
> **답.** $\dfrac{d(\pi-d)}{2}$입니다.
> **풀이.** 좌변은 $\tfrac{1}{2\pi}\int_{-\pi}^{\pi}\lvert f\rvert^{2}dx=\tfrac{2d}{2\pi}=\tfrac{d}{\pi}$입니다. 우변은 $\lvert c_n\rvert^{2}$을 모든 정수에 대해 더한 것이고 $\lvert c_{-n}\rvert=\lvert c_n\rvert$이므로
> $$\frac{d}{\pi}=\frac{d^{2}}{\pi^{2}}+\frac{2}{\pi^{2}}\sum_{n=1}^{\infty}\frac{\sin^{2}(nd)}{n^{2}}$$
> 입니다. 정리하면 $\sum_{n\ge1}\tfrac{\sin^{2}(nd)}{n^{2}}=\tfrac{\pi^{2}}{2}\left(\tfrac{d}{\pi}-\tfrac{d^{2}}{\pi^{2}}\right)=\tfrac{d(\pi-d)}{2}$입니다. $d=\tfrac\pi2$를 넣으면 좌변은 홀수 $n$에서만 살아남아 $\sum_{n\ \text{홀수}}n^{-2}$이고 우변은 $\tfrac{\pi^{2}}{8}$이므로 이미 알려진 값과 맞습니다. 한 문제에서 $d$를 매개변수로 남기면 무한히 많은 수치급수를 한꺼번에 얻습니다. $\square$

> **문제 19.** (심화) $g(x)=f(x-x_0)$의 복소 계수가 $c_n(g)=e^{-in\pi x_0/L}c_n(f)$임을 보이고 두 신호의 스펙트럼을 비교하십시오.
> **답.** 진폭 스펙트럼은 완전히 같고 위상 스펙트럼만 $n$에 비례해 기울어집니다.
> **풀이.** 정의에 넣고 $u=x-x_0$으로 치환합니다. 피적분함수가 주기 $2L$을 가지므로 적분 구간을 한 주기만큼 옮겨도 값이 변하지 않고
> $$c_n(g)=\frac{1}{2L}\int_{-L}^{L}f(x-x_0)e^{-in\pi x/L}dx=\frac{1}{2L}\int_{-L}^{L}f(u)e^{-in\pi(u+x_0)/L}du=e^{-in\pi x_0/L}c_n(f)$$
> 입니다. $\lvert e^{-in\pi x_0/L}\rvert=1$이므로 $\lvert c_n(g)\rvert=\lvert c_n(f)\rvert$이고 진폭 $A_n$과 평균 전력이 모두 보존됩니다. 반면 위상은 $\arg c_n(g)=\arg c_n(f)-\tfrac{n\pi x_0}{L}$이므로 조파 번호에 비례해 일정한 기울기로 기울어집니다. 위상 스펙트럼이 $n$의 일차함수만큼 어긋나 있으면 두 신호는 모양이 같고 시간만 밀린 관계라고 판정할 수 있습니다.

> **문제 20.** (심화) 실수 신호 $f$가 반주기 대칭 $f(x+L)=-f(x)$를 만족하면 짝수 조파의 계수가 모두 0임을 증명하십시오.
> **답.** $c_n=(-1)^{n+1}c_n$이 되어 $n$이 짝수이면 $c_n=0$입니다.
> **풀이.** $f$의 주기가 $2L$이므로 계수 적분은 어느 한 주기에서 계산해도 같은 값을 줍니다. 적분 변수를 $L$만큼 옮기면
> $$c_n=\frac{1}{2L}\int_{-L}^{L}f(x+L)e^{-in\pi(x+L)/L}dx=e^{-in\pi}\cdot\frac{1}{2L}\int_{-L}^{L}\bigl(-f(x)\bigr)e^{-in\pi x/L}dx=(-1)^{n+1}c_n$$
> 입니다. $n$이 짝수이면 $(-1)^{n+1}=-1$이므로 $c_n=-c_n$, 곧 $c_n=0$입니다. $n$이 홀수이면 항등식이 되어 아무 제약이 없습니다. 사각파와 삼각파에 홀수 조파만 나타났던 사실이 이 정리의 사례이며, 거꾸로 짝수 조파가 하나라도 있으면 그 신호는 반주기 대칭이 아닙니다. $\square$

> **문제 21.** (심화) 주기 $2\pi$이고 연속이며 조각매끄러운 함수 $f$가 $\int_{-\pi}^{\pi}f(x)\,dx=0$을 만족하면 $\int_{-\pi}^{\pi}\lvert f\rvert^{2}dx\le\int_{-\pi}^{\pi}\lvert f'\rvert^{2}dx$임을 증명하고 등호 조건을 밝히십시오.
> **답.** 등호는 $f(x)=c_1e^{ix}+c_{-1}e^{-ix}$ 꼴, 곧 기본 조파만 남을 때 성립합니다.
> **풀이.** 먼저 도함수의 복소 계수를 구합니다. 부분적분에서 경계항 $\bigl[f(x)e^{-inx}\bigr]_{-\pi}^{\pi}$은 $f$와 지수가 모두 주기 $2\pi$를 가지므로 사라지고
> $$c_n(f')=\frac{1}{2\pi}\int_{-\pi}^{\pi}f'(x)e^{-inx}dx=in\,c_n(f)$$
> 입니다. 가정에서 $c_0=\tfrac{1}{2\pi}\int_{-\pi}^{\pi}f\,dx=0$입니다. 복소 파르세발 등식을 두 함수에 각각 적용합니다.
> $$\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert f\rvert^{2}dx=\sum_{n\ne0}\lvert c_n\rvert^{2}$$
> $$\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert f'\rvert^{2}dx=\sum_{n\ne0}n^{2}\lvert c_n\rvert^{2}$$
> $n\ne0$인 정수에서 $n^{2}\ge1$이므로 항별 비교로 두 번째 합이 첫 번째 합 이상이고, 양변에 $2\pi$를 곱하면 주장하는 부등식이 됩니다. 등호는 $n^{2}>1$인 모든 항의 계수가 0일 때, 곧 $\lvert n\rvert\ge2$에서 $c_n=0$일 때만 성립하므로 $f$는 기본 조파 $c_1e^{ix}+c_{-1}e^{-ix}$뿐입니다. 이 부등식을 비르팅거 부등식이라고 하며, 평균이 0인 진동은 도함수의 에너지가 자신의 에너지보다 작을 수 없다는 뜻입니다. $\square$

## 관련 강의

- [1. 주기함수와 삼각함수계의 직교성](../1. 주기함수와 삼각함수계의 직교성/index.md)
- [2. 푸리에 계수와 수렴 정리](../2. 푸리에 계수와 수렴 정리/index.md)
- [3. 복소 푸리에 급수와 스펙트럼](../3. 복소 푸리에 급수와 스펙트럼/index.md)
- [01. 푸리에 급수](../index.md)
