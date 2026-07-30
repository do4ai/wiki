---
title: "문제집 - 02. 푸리에 변환"
---
# 문제집 - 02. 푸리에 변환

2단원의 세 강의(4강 푸리에 변환의 정의와 성질, 5강 합성곱 정리와 파르세발 정리, 6강 샘플링 정리와 DFT·FFT 개관)를 강의별로 묶은 문제집입니다. 각 문제는 문제·답·풀이 세 줄로 되어 있고, 본문 강의에 실린 드릴과 겹치지 않도록 모두 새로 지었으며 난이도를 한 단계 올렸습니다. 규약은 본문과 같습니다. 변환은 $\hat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt$이고 역변환은 $f(t)=\tfrac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\omega)e^{i\omega t}\,d\omega$이므로 계수 $1/2\pi$는 역변환에만 붙습니다. 변수는 각주파수 $\omega$이며 보통진동수 $\nu$와는 $\omega=2\pi\nu$로 오갑니다. 계산 문항은 적분과 수치를 손으로 끝까지 밀어 검산하고, 증명 문항은 논리 전개를 스스로 다시 써 보는 것이 좋습니다.

## 4강. 푸리에 변환의 정의와 성질

> **문제 1.** (표준) $a>0$에 대해 삼각펄스 $f(t)=1-\dfrac{\lvert t\rvert}{a}$ $(\lvert t\rvert\le a)$, $f(t)=0$ $(\lvert t\rvert>a)$의 변환을 정의에 따라 직접 계산하십시오.
> **답.** $\hat f(\omega)=\dfrac{4\sin^{2}(a\omega/2)}{a\omega^{2}}=a\operatorname{sinc}^{2}\!\left(\dfrac{a\omega}{2}\right)$입니다.
> **풀이.** $f$가 실 짝함수이므로 $e^{-i\omega t}$의 사인 부분이 홀함수가 되어 사라지고 코사인 부분만 두 배로 남습니다.
> $$\hat f(\omega)=2\int_{0}^{a}\left(1-\frac{t}{a}\right)\cos\omega t\,dt=2\left[\frac{\sin a\omega}{\omega}-\frac1a\left(\frac{a\sin a\omega}{\omega}-\frac{1-\cos a\omega}{\omega^{2}}\right)\right]=\frac{2\bigl(1-\cos a\omega\bigr)}{a\omega^{2}}$$
> 여기서 $\int_{0}^{a}t\cos\omega t\,dt=\tfrac{a\sin a\omega}{\omega}-\tfrac{1-\cos a\omega}{\omega^{2}}$를 썼습니다. 반각공식 $1-\cos\theta=2\sin^{2}(\theta/2)$를 넣으면 답의 형태가 됩니다. 검산하면 $\omega\to0$에서 값이 $a$이고, 이는 밑변 $2a$와 높이 1인 삼각형의 넓이와 같아 $\hat f(0)=\int f\,dt$라는 성질과 맞습니다. 고주파 감쇠가 $1/\omega^{2}$인 이유는 삼각펄스가 연속이고 도함수만 도약하기 때문입니다.

> **문제 2.** (표준) $a>0$에 대해 $\mathcal{F}\bigl[t\,e^{-a\lvert t\rvert}\bigr]$을 구하십시오.
> **답.** $\dfrac{-4ai\omega}{\bigl(a^{2}+\omega^{2}\bigr)^{2}}$입니다.
> **풀이.** 4강의 $t$ 곱 규칙 $\mathcal{F}[tg]=i\hat g'(\omega)$를 씁니다. $g(t)=e^{-a\lvert t\rvert}$의 변환은 $\hat g(\omega)=\tfrac{2a}{a^{2}+\omega^{2}}$이므로
> $$\hat g'(\omega)=\frac{-4a\omega}{\bigl(a^{2}+\omega^{2}\bigr)^{2}}$$
> $$\mathcal{F}\bigl[te^{-a\lvert t\rvert}\bigr]=i\hat g'(\omega)=\frac{-4ai\omega}{\bigl(a^{2}+\omega^{2}\bigr)^{2}}$$
> 입니다. 결과가 순허수이고 $\omega$에 대해 홀함수인 점을 확인합니다. $te^{-a\lvert t\rvert}$이 실 홀함수이므로 4강의 대칭성 표에 따라 변환이 순허수 홀함수여야 하며, 계산 결과가 정확히 그 조건을 만족합니다. $\omega=0$에서 값이 0인 것도 홀함수의 전체 적분이 0이라는 사실과 일치합니다.

> **문제 3.** (표준) $a>0$, $b$가 실수일 때 $\mathcal{F}\bigl[e^{-at^{2}}\cos bt\bigr]$을 구하십시오.
> **답.** $\dfrac12\sqrt{\dfrac{\pi}{a}}\left(e^{-(\omega-b)^{2}/4a}+e^{-(\omega+b)^{2}/4a}\right)$입니다.
> **풀이.** 4강 예제 4에서 $\mathcal{F}\bigl[e^{-at^{2}}\bigr]=\sqrt{\pi/a}\,e^{-\omega^{2}/4a}$입니다. 코사인을 복소지수 두 개로 쪼개면 각각이 변조에 해당하므로 변조 규칙 $\mathcal{F}[e^{i\omega_0t}f]=\hat f(\omega-\omega_0)$과 선형성을 함께 씁니다.
> $$\mathcal{F}\bigl[e^{-at^{2}}\cos bt\bigr]=\frac12\mathcal{F}\bigl[e^{-at^{2}}e^{ibt}\bigr]+\frac12\mathcal{F}\bigl[e^{-at^{2}}e^{-ibt}\bigr]=\frac12\hat g(\omega-b)+\frac12\hat g(\omega+b)$$
> 여기에 $\hat g$를 대입하면 답이 됩니다. 하나였던 가우스 봉우리가 $\pm b$ 두 자리로 갈라졌고 각 봉우리의 높이는 절반이 되었습니다. 변조는 스펙트럼을 옮길 뿐 모양과 폭을 바꾸지 않으므로 두 봉우리의 폭은 원래 봉우리와 같습니다.

> **문제 4.** (심화) $\mathcal{F}\bigl[t^{2}e^{-t^{2}/2}\bigr]$을 구하십시오.
> **답.** $\sqrt{2\pi}\,\bigl(1-\omega^{2}\bigr)e^{-\omega^{2}/2}$입니다.
> **풀이.** $g(t)=e^{-t^{2}/2}$의 변환은 $a=\tfrac12$을 넣어 $\hat g(\omega)=\sqrt{2\pi}\,e^{-\omega^{2}/2}$입니다. $t$ 곱 규칙을 두 번 적용하면 $\mathcal{F}[t^{2}g]=i^{2}\hat g''(\omega)=-\hat g''(\omega)$입니다. 두 번 미분합니다.
> $$\hat g'(\omega)=-\sqrt{2\pi}\,\omega e^{-\omega^{2}/2}$$
> $$\hat g''(\omega)=\sqrt{2\pi}\,\bigl(\omega^{2}-1\bigr)e^{-\omega^{2}/2}$$
> 부호를 뒤집으면 답이 됩니다. 검산으로 $\omega=0$을 넣으면 $\sqrt{2\pi}$인데, 정의에서 이 값은 $\int_{-\infty}^{\infty}t^{2}e^{-t^{2}/2}dt$이고 이는 표준정규분포의 분산 1에 정규화 상수 $\sqrt{2\pi}$를 곱한 값이므로 일치합니다. 시간 영역에서 $t^{2}$을 곱하면 주파수 영역에서 가우스 함수에 이차 인자가 붙어 $\lvert\omega\rvert=1$에서 부호가 바뀌는 마디가 생깁니다.

> **문제 5.** (심화) $a>0$일 때 역변환을 이용해 $\displaystyle\int_{0}^{\infty}\frac{\cos\omega t}{a^{2}+\omega^{2}}\,d\omega=\frac{\pi}{2a}e^{-a\lvert t\rvert}$임을 보이십시오.
> **답.** $e^{-a\lvert t\rvert}$의 역변환 적분에서 허수부가 홀함수로 사라지고 코사인 적분만 남기 때문입니다.
> **풀이.** 4강 예제 3에서 $\mathcal{F}\bigl[e^{-a\lvert t\rvert}\bigr]=\tfrac{2a}{a^{2}+\omega^{2}}$입니다. 역변환 공식을 그대로 적으면
> $$e^{-a\lvert t\rvert}=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{2a}{a^{2}+\omega^{2}}\bigl(\cos\omega t+i\sin\omega t\bigr)d\omega=\frac{a}{\pi}\int_{-\infty}^{\infty}\frac{\cos\omega t}{a^{2}+\omega^{2}}d\omega$$
> 입니다. 사인 항은 짝함수와 홀함수의 곱이라 대칭구간 적분이 0이고, 남은 피적분함수는 짝함수이므로 절반 구간의 두 배로 씁니다. 곧 $e^{-a\lvert t\rvert}=\tfrac{2a}{\pi}\int_{0}^{\infty}\tfrac{\cos\omega t}{a^{2}+\omega^{2}}d\omega$이고 정리하면 주장하는 식입니다. $t=0$을 넣으면 $\int_{0}^{\infty}\tfrac{d\omega}{a^{2}+\omega^{2}}=\tfrac{\pi}{2a}$로 아크탄젠트 적분과 맞습니다. $\square$

> **문제 6.** (심화) 사각펄스 $p(t)=1$ $(\lvert t\rvert\le a)$, $p(t)=0$ $(\lvert t\rvert>a)$에 대해 주파수 폭 $\Delta\omega$가 정의되지 않음을 보이고 그 원인을 설명하십시오.
> **답.** $\int\omega^{2}\lvert\hat p(\omega)\rvert^{2}d\omega$가 발산하므로 $\Delta\omega$는 유한한 값을 갖지 않습니다.
> **풀이.** $\hat p(\omega)=\tfrac{2\sin(a\omega)}{\omega}$이므로 분자의 피적분함수는 다음처럼 진동하는 유계 함수가 됩니다.
> $$\int_{-\infty}^{\infty}\omega^{2}\lvert\hat p(\omega)\rvert^{2}d\omega=\int_{-\infty}^{\infty}4\sin^{2}(a\omega)\,d\omega=\infty$$
> 평균값이 2인 함수를 실직선 전체에서 적분하므로 값이 무한대입니다. 분모 $\int\lvert\hat p\rvert^{2}d\omega=2\pi\int\lvert p\rvert^{2}dt=4\pi a$는 유한하므로 비는 발산하고 $\Delta\omega=\infty$입니다. 원인은 $p$의 도약 불연속입니다. 4강의 미분 규칙에서 $\int\omega^{2}\lvert\hat p\rvert^{2}d\omega=2\pi\int\lvert p'\rvert^{2}dt$인데 도약이 있으면 도함수가 델타를 포함해 에너지가 무한합니다. 불확정성 부등식 $\Delta t\,\Delta\omega\ge\tfrac12$은 자명하게 성립하지만 아무 정보도 주지 않으며, 등호를 주는 함수는 가우스뿐이라는 사실과 어긋나지 않습니다.

> **문제 7.** (심화) 실함수 $f$를 짝 부분 $f_e$와 홀 부분 $f_o$로 나눌 때 $\operatorname{Re}\hat f=\widehat{f_e}$이고 $i\operatorname{Im}\hat f=\widehat{f_o}$임을 증명하십시오.
> **답.** 짝 부분의 변환이 실 짝함수이고 홀 부분의 변환이 순허수 홀함수이므로 두 성분이 실수부와 허수부로 정확히 갈립니다.
> **풀이.** $f_e(t)=\tfrac{f(t)+f(-t)}{2}$, $f_o(t)=\tfrac{f(t)-f(-t)}{2}$로 두면 $f=f_e+f_o$이고 두 함수 모두 실함수입니다. 선형성에 의해 $\hat f=\widehat{f_e}+\widehat{f_o}$입니다. 4강의 대칭성 표에서 실 짝함수의 변환은
> $$\widehat{f_e}(\omega)=2\int_{0}^{\infty}f_e(t)\cos\omega t\,dt$$
> $$\widehat{f_o}(\omega)=-2i\int_{0}^{\infty}f_o(t)\sin\omega t\,dt$$
> 이므로 앞의 것은 실수 값이고 뒤의 것은 순허수 값입니다. 복소수의 실수부와 허수부 분해는 유일하므로 $\operatorname{Re}\hat f=\widehat{f_e}$이고 $i\operatorname{Im}\hat f=\widehat{f_o}$입니다. 이 분해가 실함수의 에르미트 대칭 $\hat f(-\omega)=\overline{\hat f(\omega)}$을 다시 설명해 줍니다. 실수부는 짝함수, 허수부는 홀함수이기 때문입니다. $\square$

## 5강. 합성곱 정리와 파르세발 정리

> **문제 8.** (표준) $p(t)=1$ $(0\le t\le T)$, 그 밖에서 0인 사각펄스와 $h(t)=e^{-at}u(t)$의 합성곱을 구간별로 구하십시오. $a>0$입니다.
> **답.** $t<0$에서 0, $0\le t\le T$에서 $\dfrac{1-e^{-at}}{a}$, $t>T$에서 $\dfrac{e^{-a(t-T)}-e^{-at}}{a}$입니다.
> **풀이.** $(p*h)(t)=\int p(\tau)h(t-\tau)\,d\tau$에서 피적분함수가 0이 아니려면 $0\le\tau\le T$이고 동시에 $\tau\le t$여야 합니다. 따라서 적분 구간은 $[0,\min(t,T)]$이고 $t<0$이면 비어 있어 값이 0입니다.
> $$(p*h)(t)=\int_{0}^{\min(t,T)}e^{-a(t-\tau)}d\tau=e^{-at}\cdot\frac{e^{a\min(t,T)}-1}{a}$$
> $0\le t\le T$이면 $\min(t,T)=t$이므로 $\tfrac{1-e^{-at}}{a}$이고, $t>T$이면 $\min(t,T)=T$이므로 $\tfrac{e^{-a(t-T)}-e^{-at}}{a}$입니다. 두 식이 $t=T$에서 모두 $\tfrac{1-e^{-aT}}{a}$를 주므로 결과는 연속입니다. 계단 입력을 저역통과 시스템에 넣으면 지수적으로 차오르다가 입력이 끊긴 뒤 지수적으로 빠지는 응답이 나온다는 사실을 이 계산이 보여 줍니다.

> **문제 9.** (표준) $f(t)=e^{-at}u(t)$의 자기상관 $R_f$를 정의로 구하고 위너-킨친 관계로 검산하십시오. $a>0$입니다.
> **답.** $R_f(t)=\dfrac{e^{-a\lvert t\rvert}}{2a}$입니다.
> **풀이.** $t\ge0$에서 $R_f(t)=\int_{0}^{\infty}e^{-a\tau}e^{-a(t+\tau)}d\tau=e^{-at}\int_{0}^{\infty}e^{-2a\tau}d\tau=\tfrac{e^{-at}}{2a}$입니다. 실함수의 자기상관은 짝함수이므로 $t<0$에서는 $\lvert t\rvert$로 바꾸어 쓰면 됩니다. 검산합니다. $\hat f(\omega)=\tfrac{1}{a+i\omega}$이므로 에너지 스펙트럼 밀도는
> $$S_f(\omega)=\lvert\hat f(\omega)\rvert^{2}=\frac{1}{a^{2}+\omega^{2}}=\frac{1}{2a}\cdot\frac{2a}{a^{2}+\omega^{2}}$$
> 이고, 4강에서 $\tfrac{2a}{a^{2}+\omega^{2}}$의 역변환이 $e^{-a\lvert t\rvert}$이므로 $S_f$의 역변환은 $\tfrac{e^{-a\lvert t\rvert}}{2a}$입니다. 두 계산이 일치합니다. 또 $R_f(0)=\tfrac{1}{2a}$이고 직접 구한 에너지 $\int_{0}^{\infty}e^{-2at}dt=\tfrac{1}{2a}$와 같으므로 자기상관의 최댓값이 에너지라는 성질도 확인됩니다.

> **문제 10.** (표준) 최고 각주파수가 $\omega_{\max}$인 신호 $f$에 $\cos\omega_0 t$를 곱한 신호의 스펙트럼을 구하고, 두 조각이 겹치지 않을 조건을 구하십시오.
> **답.** $\mathcal{F}[f\cos\omega_0t]=\tfrac12\hat f(\omega-\omega_0)+\tfrac12\hat f(\omega+\omega_0)$이고 겹치지 않을 조건은 $\omega_0>\omega_{\max}$입니다.
> **풀이.** 5강의 곱의 변환 공식과 $\mathcal{F}[\cos\omega_0t]=\pi\delta(\omega-\omega_0)+\pi\delta(\omega+\omega_0)$을 함께 씁니다. 델타와의 합성곱이 평행이동이므로
> $$\mathcal{F}[f\cos\omega_0t]=\frac{1}{2\pi}\Bigl(\hat f*\bigl[\pi\delta(\cdot-\omega_0)+\pi\delta(\cdot+\omega_0)\bigr]\Bigr)(\omega)=\frac{\hat f(\omega-\omega_0)+\hat f(\omega+\omega_0)}{2}$$
> 입니다. 4강의 변조 규칙을 두 복소지수에 각각 적용해도 같은 결과가 나오므로 두 경로가 서로 검산이 됩니다. 옮겨진 두 조각은 각각 $[\omega_0-\omega_{\max},\omega_0+\omega_{\max}]$와 $[-\omega_0-\omega_{\max},-\omega_0+\omega_{\max}]$에 놓입니다. 두 구간이 만나지 않으려면 $-\omega_0+\omega_{\max}<\omega_0-\omega_{\max}$, 곧 $\omega_0>\omega_{\max}$여야 합니다. 진폭 변조에서 반송파 진동수를 신호 대역보다 높게 잡는 이유가 이 조건입니다.

> **문제 11.** (심화) 플랑셰렐 정리로 $\displaystyle\int_{-\infty}^{\infty}\frac{\omega^{2}}{\bigl(a^{2}+\omega^{2}\bigr)^{2}}\,d\omega$를 구하십시오. $a>0$입니다.
> **답.** $\dfrac{\pi}{2a}$입니다.
> **풀이.** $f(t)=e^{-a\lvert t\rvert}$은 연속이고 조각매끄러우므로 미분 규칙 $\mathcal{F}[f']=i\omega\hat f$를 쓸 수 있습니다. $f'(t)=-a\operatorname{sgn}(t)e^{-a\lvert t\rvert}$이므로 시간 영역의 에너지는 $\int\lvert f'\rvert^{2}dt=a^{2}\int e^{-2a\lvert t\rvert}dt=a^{2}\cdot\tfrac1a=a$입니다. 한편 $\lvert\mathcal{F}[f']\rvert^{2}=\omega^{2}\lvert\hat f\rvert^{2}$이므로
> $$a=\frac{1}{2\pi}\int_{-\infty}^{\infty}\omega^{2}\cdot\frac{4a^{2}}{\bigl(a^{2}+\omega^{2}\bigr)^{2}}d\omega$$
> 이 등식을 적분에 대해 풀면 다음을 얻습니다.
> $$\int_{-\infty}^{\infty}\frac{\omega^{2}}{\bigl(a^{2}+\omega^{2}\bigr)^{2}}d\omega=\frac{2\pi a}{4a^{2}}=\frac{\pi}{2a}$$
> 검산으로 $a=1$을 넣으면 $\tfrac\pi2$인데, 5강에서 얻은 $\int\tfrac{d\omega}{(1+\omega^{2})^{2}}=\tfrac\pi2$와 더하면 $\int\tfrac{d\omega}{1+\omega^{2}}=\pi$가 되어 아크탄젠트 적분과 맞습니다. 미분을 한 번 취해 얻는 새 변환쌍이 새 이상적분을 준다는 점이 요령입니다. $\square$

> **문제 12.** (심화) $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^{3}\omega}{\omega^{3}}\,d\omega$를 합성곱 정리와 역변환 공식으로 구하십시오.
> **답.** $\dfrac{3\pi}{4}$입니다.
> **풀이.** $p(t)=1$ $(\lvert t\rvert\le1)$인 사각펄스의 변환은 $\hat p(\omega)=\tfrac{2\sin\omega}{\omega}$입니다. 합성곱 정리를 두 번 쓰면 $\mathcal{F}[p*p*p]=\hat p^{3}=\tfrac{8\sin^{3}\omega}{\omega^{3}}$입니다. 역변환 공식에 $t=0$을 넣으면 좌변이 $(p*p*p)(0)$이고 우변이 문제의 적분에 상수를 곱한 것이 됩니다.
> $$(p*p*p)(0)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{8\sin^{3}\omega}{\omega^{3}}d\omega$$
> 좌변을 직접 계산합니다. 5강 예제 1에서 $(p*p)(\tau)=2-\lvert\tau\rvert$ $(\lvert\tau\rvert\le2)$이므로 $(p*p*p)(0)=\int_{-1}^{1}(2-\lvert\tau\rvert)d\tau=2\int_{0}^{1}(2-\tau)d\tau=3$입니다. 따라서 $\int\tfrac{8\sin^{3}\omega}{\omega^{3}}d\omega=6\pi$이고 8로 나누면 $\tfrac{3\pi}{4}$입니다. $p*p*p$가 연속함수라서 역변환이 $t=0$에서 함수값을 그대로 준다는 점이 이 계산의 전제입니다. $\square$

> **문제 13.** (심화) 실수 $x$에 대해 $\displaystyle\int_{-\infty}^{\infty}\frac{dt}{\bigl(1+t^{2}\bigr)\bigl(1+(x-t)^{2}\bigr)}$를 구하십시오.
> **답.** $\dfrac{2\pi}{4+x^{2}}$입니다.
> **풀이.** 주어진 적분은 $f(t)=\tfrac{1}{1+t^{2}}$의 자기 합성곱 $(f*f)(x)$입니다. 4강에서 $\hat f(\omega)=\pi e^{-\lvert\omega\rvert}$이므로 합성곱 정리에 의해 $\mathcal{F}[f*f]=\pi^{2}e^{-2\lvert\omega\rvert}$입니다. 역변환으로 되돌립니다.
> $$(f*f)(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\pi^{2}e^{-2\lvert\omega\rvert}e^{i\omega x}d\omega=\pi\int_{0}^{\infty}e^{-2\omega}\cos\omega x\,d\omega=\pi\cdot\frac{2}{4+x^{2}}$$
> 여기서 허수부는 홀함수라 사라졌고 $\int_{0}^{\infty}e^{-c\omega}\cos b\omega\,d\omega=\tfrac{c}{c^{2}+b^{2}}$를 썼습니다. 검산으로 $x=0$을 넣으면 $\tfrac{\pi}{2}$이고, 이는 5강에서 파르세발 정리로 얻은 $\int\tfrac{dt}{(1+t^{2})^{2}}=\tfrac\pi2$와 같습니다. 폭이 1인 두 로런츠 함수의 합성곱이 폭 2인 로런츠 함수라는 결과이며, 지수 스펙트럼의 곱이 지수의 합으로 나타나는 구조가 그 이유입니다. $\square$

> **문제 14.** (심화) $\mathcal{F}\bigl[\operatorname{sgn}(t)\bigr]=\dfrac{2}{i\omega}$임을 감쇠 인자의 극한으로 유도하십시오.
> **답.** $e^{-a\lvert t\rvert}\operatorname{sgn}(t)$의 변환에서 $a\to0^{+}$ 극한을 취하면 됩니다.
> **풀이.** $\operatorname{sgn}$은 절대적분가능하지 않으므로 정의 적분이 통상적 의미로 수렴하지 않습니다. 그래서 $a>0$인 감쇠 인자를 곱한 $f_a(t)=e^{-a\lvert t\rvert}\operatorname{sgn}(t)$를 먼저 변환합니다. 이 함수는 $L^{1}$에 속하고 두 조각으로 나누어 계산됩니다.
> $$\hat f_a(\omega)=\int_{0}^{\infty}e^{-(a+i\omega)t}dt-\int_{-\infty}^{0}e^{(a-i\omega)t}dt=\frac{1}{a+i\omega}-\frac{1}{a-i\omega}=\frac{-2i\omega}{a^{2}+\omega^{2}}$$
> 이제 $a\to0^{+}$을 취하면 $\omega\ne0$인 모든 점에서 $\hat f_a(\omega)\to\tfrac{-2i}{\omega}=\tfrac{2}{i\omega}$입니다. 결과가 순허수 홀함수인 점은 $\operatorname{sgn}$이 실 홀함수라는 사실과 맞습니다. 이 결과를 $u(t)=\tfrac12+\tfrac12\operatorname{sgn}(t)$에 넣으면 5강에서 쓴 $\mathcal{F}[u]=\pi\delta(\omega)+\tfrac{1}{i\omega}$가 그대로 나옵니다. $\square$

## 6강. 샘플링 정리와 DFT·FFT 개관

> **문제 15.** (표준) $\nu_s=1000\ \mathrm{Hz}$로 표본화할 때 $300$, $700$, $1300$, $1800\ \mathrm{Hz}$ 성분이 각각 어느 진동수로 관측되는지 구하고, 서로 구별되지 않는 성분을 찾으십시오.
> **답.** 차례로 $300$, $300$, $300$, $200\ \mathrm{Hz}$이며 앞의 세 성분이 서로 구별되지 않습니다.
> **풀이.** 나이퀴스트 진동수는 $500\ \mathrm{Hz}$이고 접힘 공식은 $\nu_{\text{alias}}=\min_k\lvert\nu_0-k\nu_s\rvert$입니다. $300$은 이미 관측 대역 안이라 그대로입니다. $700$은 $\lvert700-1000\rvert=300$, $1300$은 $\lvert1300-1000\rvert=300$, $1800$은 $\lvert1800-2000\rvert=200$이 최소입니다. 표본열로 확인하면 $\cos\bigl(2\pi\cdot700\cdot\tfrac{n}{1000}\bigr)=\cos\bigl(2\pi\cdot0.7n\bigr)$이고 $0.7n$과 $-0.3n$은 정수만큼 차이가 나므로 코사인 값이 같습니다. 곧 $300$, $700$, $1300\ \mathrm{Hz}$ 세 성분은 완전히 같은 표본열을 만들며 표본만 보고는 구별할 방법이 없습니다. 이 성분들을 살리려면 표본화 진동수를 올리거나 표본화 전에 저역통과 필터로 잘라야 합니다.

> **문제 16.** (표준) $\mathbf{x}=(0,1,0,-1)$의 4점 DFT를 구하고 이산 파르세발 등식을 확인하십시오.
> **답.** $\mathbf{X}=(0,-2i,0,2i)$이고 양변이 모두 $2$입니다.
> **풀이.** $W_4=e^{-2\pi i/4}=-i$이므로 $W_4^{2}=-1$, $W_4^{3}=i$입니다. 지표 1과 3만 값을 가지므로
> $$X_k=\sum_{n=0}^{3}x_nW_4^{nk}=W_4^{k}-W_4^{3k}$$
> $$X_0=0,\quad X_1=-i-i=-2i,\quad X_2=-1+1=0,\quad X_3=i+i=2i$$
> 입니다. 입력이 실수열이므로 $X_3=\overline{X_1}$인 에르미트 대칭이 성립합니다. 이 수열은 $x_n=\sin(2\pi n/4)$이므로 실 홀함수에 해당하고, 4강의 대칭성 표대로 변환이 순허수가 되었습니다. 파르세발 등식의 좌변은 $0+1+0+1=2$이고 우변은 $\tfrac14(0+4+0+4)=2$이므로 일치합니다.

> **문제 17.** (심화) $\mathbf{x}=(1,2,3)$과 $\mathbf{h}=(1,-1,2)$의 선형 합성곱과 3점 순환 합성곱을 각각 구하고 두 결과의 관계를 설명하십시오.
> **답.** 선형 합성곱은 $(1,1,3,1,6)$이고 순환 합성곱은 $(2,7,3)$이며, 뒤의 두 항이 앞으로 되돌아와 더해진 것입니다.
> **풀이.** 선형 합성곱은 $y_n=\sum_m x_mh_{n-m}$입니다. 차례로 $y_0=1$, $y_1=-1+2=1$, $y_2=2-2+3=3$, $y_3=4-3=1$, $y_4=6$이므로 길이 $3+3-1=5$인 수열 $(1,1,3,1,6)$을 얻습니다. 순환 합성곱은 지표를 3으로 나눈 나머지로 읽으므로
> $$z_0=x_0h_0+x_1h_2+x_2h_1=1+4-3=2,\quad z_1=x_0h_1+x_1h_0+x_2h_2=-1+2+6=7,\quad z_2=x_0h_2+x_1h_1+x_2h_0=2-2+3=3$$
> 입니다. 두 결과를 비교하면 $z_0=y_0+y_3=1+1=2$이고 $z_1=y_1+y_4=1+6=7$이며 $z_2=y_2=3$입니다. 곧 길이 3을 넘어간 꼬리 $y_3,y_4$가 머리 자리로 되돌아와 더해졌고, 이것이 순환 겹침입니다. 0을 덧붙여 길이를 5 이상으로 늘리면 되돌아올 자리가 없어져 두 연산이 일치합니다.

> **문제 18.** (심화) $g(t)=\dfrac{\sin\pi t}{\pi t}$와 $f(t)=g(t)^{2}$의 대역폭을 각각 구하고 두 신호를 표본화할 때 필요한 최소 표본화 진동수를 비교하십시오.
> **답.** $g$는 $B=0.5\ \mathrm{Hz}$이고 $f$는 $B=1\ \mathrm{Hz}$이므로 최소 표본화 진동수가 $1\ \mathrm{Hz}$에서 $2\ \mathrm{Hz}$로 두 배가 됩니다.
> **풀이.** 4강의 쌍대성 결과를 스케일링해 $\hat g(\omega)=1$ $(\lvert\omega\rvert<\pi)$, $\hat g(\omega)=0$ $(\lvert\omega\rvert>\pi)$을 얻습니다. 곧 $\omega_{\max}=\pi$이고 $B=\omega_{\max}/2\pi=0.5$입니다. 제곱은 시간 영역의 곱이므로 5강의 공식에 따라 주파수 영역에서 합성곱이 됩니다.
> $$\hat f(\omega)=\frac{1}{2\pi}\bigl(\hat g*\hat g\bigr)(\omega)=1-\frac{\lvert\omega\rvert}{2\pi}\quad(\lvert\omega\rvert\le2\pi),\qquad \hat f(\omega)=0\quad(\lvert\omega\rvert>2\pi)$$
> 폭 $2\pi$인 사각형을 자기 자신과 합성곱하면 밑변이 $4\pi$이고 꼭짓값이 $2\pi$인 삼각형이 되며, 여기에 $\tfrac{1}{2\pi}$를 곱한 결과입니다. 따라서 $f$의 최고 진동수는 $B=1$이고 표본화 조건은 $\nu_s>2$입니다. 검산으로 $\hat f(0)=1$인데 이는 $\int g^{2}dt=1$과 같습니다. 신호를 제곱하면 대역폭이 두 배가 되므로 비선형 처리를 거친 뒤에는 표본화 진동수를 다시 따져야 합니다. $\square$

> **문제 19.** (심화) DFT 행렬에 대해 $\bigl(F_N^{2}\mathbf{x}\bigr)_k=N\,x_{(-k)\bmod N}$임을 보이고 $F_N^{4}=N^{2}I$를 유도하십시오.
> **답.** DFT를 두 번 적용하면 수열이 $N$배가 되면서 지표가 뒤집히고, 네 번 적용하면 원래 수열의 $N^{2}$배가 됩니다.
> **풀이.** 정의를 두 번 넣고 합의 순서를 바꿉니다.
> $$\bigl(F_N^{2}\mathbf{x}\bigr)_k=\sum_{n=0}^{N-1}\left(\sum_{m=0}^{N-1}x_mW_N^{mn}\right)W_N^{nk}=\sum_{m=0}^{N-1}x_m\sum_{n=0}^{N-1}W_N^{n(m+k)}$$
> 안쪽 합은 1의 $N$제곱근의 거듭제곱을 모두 더한 것이므로 $m+k\equiv0\pmod N$일 때만 $N$이고 나머지에서는 0입니다. 따라서 살아남는 항은 $m=(-k)\bmod N$ 하나뿐이고 값은 $Nx_{(-k)\bmod N}$입니다. 이 연산을 다시 두 번 적용하면 지표가 두 번 뒤집혀 제자리로 돌아오고 배수만 곱해지므로 $F_N^{4}=N^{2}I$입니다. 곧 $\tfrac{1}{\sqrt N}F_N$은 네 제곱이 항등원인 유니터리 행렬이며 고윳값은 1의 네 제곱근 중 하나뿐입니다. 예제로 $\mathbf{x}=(1,2,3,4)$를 두 번 변환하면 $4\cdot(1,4,3,2)$가 되어 첫 성분만 제자리에 있고 나머지가 역순으로 배열됩니다. $\square$

> **문제 20.** (심화) $N=4096$일 때 정의대로 계산하는 DFT와 기수 2 FFT의 복소 곱셈 횟수를 비교하고 단계 수와 단계당 버터플라이 개수를 구하십시오.
> **답.** 각각 약 $1.68\times10^{7}$번과 $24{,}576$번이며 약 $683$배 차이가 납니다. 단계는 $12$개이고 단계마다 버터플라이가 $2048$개입니다.
> **풀이.** 정의대로 계산하면 출력 하나에 $N$번의 복소 곱셈이 들고 출력이 $N$개이므로 $N^{2}=4096^{2}=16{,}777{,}216$번입니다. 기수 2 FFT는 절반 크기 문제 두 개로 나누는 구조이므로 단계 수가 $\log_2N=12$이고, 각 단계에서 버터플라이가 $N/2=2048$개이며 버터플라이마다 회전인자 곱셈이 한 번 듭니다.
> $$\frac{N}{2}\log_2N=2048\times12=24{,}576$$
> $$\frac{N^{2}}{\frac{N}{2}\log_2N}=\frac{2N}{\log_2N}=\frac{8192}{12}\approx682.7$$
> 곧 약 683배 빠릅니다. 절감의 원천은 $E_k$와 $O_k$를 한 번 계산해 $X_k$와 $X_{k+N/2}$ 두 출력을 함께 얻는 재사용입니다. 이 절감이 있어야 길이 $N$ 두 수열의 합성곱을 $O(N^{2})$ 대신 $O(N\log N)$으로 계산하는 전략이 실제 이득이 됩니다.

> **문제 21.** (심화) $\nu_s=16\ \mathrm{Hz}$로 $N=16$개의 표본을 뽑을 때 $3\ \mathrm{Hz}$ 정현파에는 누출이 없고 $3.5\ \mathrm{Hz}$ 정현파에는 누출이 생기는 이유를 지표 계산으로 설명하십시오.
> **답.** 관측 구간에 신호의 주기가 정수 번 들어가는지가 갈림길이며, 그 조건은 $\nu_0N/\nu_s$가 정수인 것입니다.
> **풀이.** 관측 시간은 $NT=N/\nu_s=1$초이고 DFT 지표 간격은 $\nu_s/N=1\ \mathrm{Hz}$입니다. 따라서 지표 $k$는 $k\ \mathrm{Hz}$에 대응합니다.
> $$\frac{\nu_0N}{\nu_s}=\nu_0\cdot NT,\qquad \nu_0=3\ \Longrightarrow\ k=3,\qquad \nu_0=3.5\ \Longrightarrow\ k=3.5$$
> $3\ \mathrm{Hz}$ 성분은 관측 구간에 정확히 3주기가 들어가므로 사각창 변환인 sinc의 영점이 다른 모든 지표에 정확히 놓입니다. 그래서 에너지가 $k=3$ 하나에만 나타나고 누출이 보이지 않으며, 이를 정합 표본화라고 합니다. $3.5\ \mathrm{Hz}$ 성분은 지표 3과 4 사이에 놓여 어느 영점과도 맞지 않으므로 모든 지표에 값이 번지고, 부엽이 $1/\lvert\omega\rvert$로만 잦아들어 멀리까지 영향을 줍니다. 대응은 관측 시간을 늘려 지표 간격을 좁히거나 부엽이 낮은 창함수를 쓰는 것이며, 뒤의 선택은 주엽이 넓어지는 대가를 치릅니다.

## 관련 강의

- [4. 푸리에 변환의 정의와 성질](../4. 푸리에 변환의 정의와 성질/index.md)
- [5. 합성곱 정리와 파르세발 정리](../5. 합성곱 정리와 파르세발 정리/index.md)
- [6. 샘플링 정리와 DFT·FFT 개관](../6. 샘플링 정리와 DFT·FFT 개관/index.md)
- [02. 푸리에 변환](../index.md)
