---
title: "문제집 - 04. 변환의 응용"
---
# 문제집 - 04. 변환의 응용

4단원의 두 강의(9강 신호 처리와 필터링, 10강 열방정식과 파동방정식 풀이)를 강의별로 묶은 문제집입니다. 각 문제는 문제·답·풀이 세 줄로 되어 있고, 본문 강의에 실린 드릴과 겹치지 않도록 모두 새로 지었으며 난이도를 한 단계 올렸습니다. 필터 쪽은 전달함수와 창함수, 정합필터처럼 성질 두세 개를 겹쳐 써야 풀리는 문항을 모았고, 편미분방정식 쪽은 혼합 경계조건과 반사, 열핵의 적분 계산처럼 손으로 끝까지 밀어야 하는 문항을 모았습니다. 수치 답은 어림한 자리까지 함께 적었으므로 계산기로 다시 확인하는 것이 좋습니다. 푸리에 변환 규약은 9강과 같이 $\hat f(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt$이고 $1/2\pi$는 역변환에만 붙이며, 표기는 KaTeX를 따릅니다.

## 9강. 신호 처리와 필터링

> **문제 1.** (표준) 초기 정지 상태의 시스템이 $y''+3y'+2y=x'+x$로 주어질 때 전달함수와 임펄스 응답을 구하고 차단주파수를 말하십시오.
> **답.** $H(s)=\dfrac{1}{s+2}$이고 $h(t)=e^{-2t}$ (단 $t\ge0$)이며 차단주파수는 $\omega_c=2\ \mathrm{rad/s}$입니다.
> **풀이.** 초기값이 모두 $0$이므로 양변을 라플라스 변환하면 $(s^{2}+3s+2)Y=(s+1)X$입니다. 따라서 전달함수는 두 다항식의 비이며 분자와 분모에 공통 인수가 있습니다.
> $$H(s)=\frac{s+1}{s^{2}+3s+2}=\frac{s+1}{(s+1)(s+2)}=\frac{1}{s+2}$$
> 곧 $s=-1$의 극이 같은 자리의 영점과 상쇄되어 1계 저역통과 계로 내려갑니다. 역변환하면 $h(t)=e^{-2t}u(t)$이고, 허수축에서 평가한 주파수 응답과 그 크기는 다음과 같습니다.
> $$H(\omega)=\frac{1}{2+i\omega},\qquad \lvert H(\omega)\rvert=\frac{1}{\sqrt{4+\omega^{2}}}$$
> 크기가 최대값 $1/2$의 $1/\sqrt2$가 되는 조건은 $4+\omega^{2}=8$이므로 $\omega_c=2$입니다. 이 상쇄는 계산상의 편의일 뿐이며, 초기조건이 $0$이 아니면 $e^{-t}$ 항이 살아나 상태변수가 하나 더 있다는 사실이 드러납니다. $\square$

> **문제 2.** (심화) 이상 저역통과 필터의 임펄스 응답 $h(t)=\dfrac{\sin\omega_ct}{\pi t}$에 대해 $\int_{-\infty}^{\infty}h(t)^{2}\,dt$를 구하고, 이 값이 유한한데도 계가 유계입력 유계출력 안정이 아닌 이유를 설명하십시오.
> **답.** $\displaystyle\int h^{2}=\frac{\omega_c}{\pi}$로 유한하지만 안정성 조건은 $\int\lvert h\rvert<\infty$이므로 두 조건은 다릅니다.
> **풀이.** 파르세발 정리를 쓰면 시간 영역 적분을 주파수 영역에서 계산할 수 있습니다.
> $$\int_{-\infty}^{\infty}h(t)^{2}\,dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}\lvert H(\omega)\rvert^{2}\,d\omega=\frac{1}{2\pi}\int_{-\omega_c}^{\omega_c}1\,d\omega=\frac{\omega_c}{\pi}$$
> 곧 $h$는 제곱적분가능하며 에너지가 유한합니다. 그러나 안정성이 요구하는 것은 절댓값의 적분입니다. $\lvert\sin\omega_ct\rvert$의 한 주기 평균이 $2/\pi$이므로 충분히 큰 $t$에서
> $$\int_{1}^{\infty}\frac{\lvert\sin\omega_ct\rvert}{\pi t}\,dt\ \ge\ \frac{2}{\pi^{2}}\int_{1}^{\infty}\frac{dt}{t}=\infty$$
> 입니다. 같은 사정을 제곱 쪽에서 보면 감쇠가 한 차수 빨라져 적분이 살아납니다.
> $$\int_{1}^{\infty}\frac{\sin^{2}\omega_ct}{\pi^{2}t^{2}}\,dt\ \le\ \frac{1}{\pi^{2}}\int_{1}^{\infty}\frac{dt}{t^{2}}=\frac{1}{\pi^{2}}<\infty$$
> 곧 절댓값은 $1/t$ 규모라 발산하고 제곱은 $1/t^{2}$ 규모라 수렴한다는 것이 두 결과의 차이입니다. 유계입력 유계출력 안정은 $\int\lvert h\rvert<\infty$를 요구하므로 이 필터는 에너지가 유한해도 불안정합니다. 실제로 부호가 $h$와 맞도록 $\pm1$을 오가는 유계 입력을 넣으면 출력이 무한히 커집니다. $\square$

> **문제 3.** (심화) 시간상수가 같은 1계 RC 저역통과 두 단을 서로 부하를 주지 않게 이어 붙였습니다. $R=1\ \mathrm{k\Omega}$, $C=0.1\ \mu\mathrm{F}$일 때 전체의 차단주파수를 구하고 한 단일 때와 비교하십시오.
> **답.** 약 $1024\ \mathrm{Hz}$이며 한 단일 때의 $1592\ \mathrm{Hz}$보다 낮습니다.
> **풀이.** 두 단이 서로 부하를 주지 않으므로 전달함수는 곱이 되고 크기의 제곱도 곱이 됩니다.
> $$\lvert H(\omega)\rvert^{2}=\frac{1}{\left[1+(\omega RC)^{2}\right]^{2}}$$
> 차단주파수는 이 값이 $1/2$이 되는 진동수이므로 $x=\omega RC$로 두면 $(1+x^{2})^{2}=2$, 곧 $x^{2}=\sqrt2-1$입니다. 따라서
> $$x=\sqrt{\sqrt2-1}\approx0.6436\;\Longrightarrow\;\omega_c=\frac{0.6436}{RC}$$
> 입니다. 여기에 $RC=10^{3}\times10^{-7}=10^{-4}$초를 넣고 보통진동수로 바꿉니다.
> $$\nu_{c,1}=\frac{1}{2\pi RC}\approx1591.5\ \mathrm{Hz},\qquad
> \nu_{c,2}=0.6436\times1591.5\approx1024.3\ \mathrm{Hz}$$ 각 단이 자기 차단주파수에서 이미 $-3$ 데시벨을 깎으므로 두 단을 지나면 $-6$ 데시벨이 되고, 그래서 $-3$ 데시벨 점이 더 낮은 진동수로 밀립니다. 대신 고주파 감쇠는 십진구간당 $-40$ 데시벨로 두 배 가팔라집니다. 단을 이어 붙일수록 차단은 날카로워지지만 통과대역이 좁아진다는 것이 다단 필터 설계의 기본 상충입니다. $\square$

> **문제 4.** (심화) $x(t)=\cos\omega_0t$를 폭 $T$의 사각창으로 $\lvert t\rvert\le T/2$에서만 잘라 냈을 때의 스펙트럼을 구하고, 첫 사이드로브의 크기를 데시벨로 구하십시오.
> **답.** $\hat x(\omega)=\dfrac{T}{2}\left[\operatorname{sinc}\dfrac{(\omega-\omega_0)T}{2}+\operatorname{sinc}\dfrac{(\omega+\omega_0)T}{2}\right]$이고 첫 사이드로브는 약 $-13.3\ \mathrm{dB}$입니다.
> **풀이.** 코사인을 복소지수의 합으로 쓰고 항별로 적분합니다. 한 항은
> $$\int_{-T/2}^{T/2}e^{-i(\omega-\omega_0)t}\,dt=\frac{2\sin\left[(\omega-\omega_0)T/2\right]}{\omega-\omega_0}=T\operatorname{sinc}\frac{(\omega-\omega_0)T}{2}$$
> 이고 다른 항은 $\omega_0$의 부호만 바뀝니다. 두 항에 $1/2$을 곱해 더하면 위 결과입니다. 자르기 전의 스펙트럼은 $\pm\omega_0$에 놓인 두 개의 델타였는데, 창을 곱한 뒤에는 주엽과 사이드로브로 번집니다. 영점은 sinc의 인수가 $\pi$의 정수배가 되는 자리이므로 다음 위치에 놓입니다.
> $$\omega=\omega_0\pm\frac{2\pi k}{T}\quad(k=1,2,\dots),\qquad \text{주엽의 폭}=\frac{4\pi}{T}$$
> 이 번짐이 스펙트럼 누설입니다. 사이드로브의 극값은 $\dfrac{d}{du}\dfrac{\sin u}{u}=0$, 곧 $\tan u=u$의 해에서 나오고 첫 해는 $u_1\approx4.4934$입니다. 그 자리의 크기는
> $$\left\lvert\frac{\sin u_1}{u_1}\right\rvert\approx\frac{0.9761}{4.4934}\approx0.2172
> \;\Longrightarrow\;20\log_{10}0.2172\approx-13.26\ \mathrm{dB}$$
> 입니다. 사각창의 사이드로브는 창을 아무리 길게 잡아도 이 $-13.3$ 데시벨에서 내려가지 않고 폭만 좁아집니다. 약한 성분이 강한 성분의 사이드로브에 묻히는 것을 막으려면 창의 양 끝을 부드럽게 깎은 해닝 창이나 해밍 창을 써야 하며, 그 대가로 주엽이 넓어져 가까운 두 진동수를 구분하기 어려워집니다. $\square$

> **문제 5.** (심화) 신호 $s(t)$가 $[0,T]$ 밖에서 $0$이고 에너지가 $E=\int_{0}^{T}s(t)^{2}\,dt$입니다. 자기상관이 $\frac{N_0}{2}\delta(\tau)$인 백색잡음이 더해진 입력을 필터 $h$에 통과시켜 $t=T$에서 표본화할 때 신호 대 잡음비를 최대로 만드는 $h$를 구하십시오.
> **답.** $h(\tau)=s(T-\tau)$이며 그때 최대값은 $\dfrac{2E}{N_0}$입니다.
> **풀이.** 출력의 신호 성분과 잡음 전력은 각각 다음과 같습니다.
> $$y_s(T)=\int_{0}^{T}h(\tau)s(T-\tau)\,d\tau,\qquad
> \sigma^{2}=\frac{N_0}{2}\int_{0}^{T}h(\tau)^{2}\,d\tau$$
> 잡음 전력 식은 자기상관이 델타이므로 이중적분 중 $\tau_1=\tau_2$인 부분만 남아서 나옵니다. 이제 코시-슈바르츠 부등식을 신호 성분에 적용합니다.
> $$\left(\int_{0}^{T}h(\tau)s(T-\tau)\,d\tau\right)^{2}
> \le\int_{0}^{T}h(\tau)^{2}\,d\tau\cdot\int_{0}^{T}s(T-\tau)^{2}\,d\tau
> =E\int_{0}^{T}h(\tau)^{2}\,d\tau$$
> 마지막 등호는 $\tau\mapsto T-\tau$가 적분 구간을 그대로 옮기므로 성립합니다. 두 식을 합치면
> $$\mathrm{SNR}=\frac{y_s(T)^{2}}{\sigma^{2}}\le\frac{E\int h^{2}}{\frac{N_0}{2}\int h^{2}}=\frac{2E}{N_0}$$
> 이고 $\int h^{2}$이 약분되므로 상한은 필터의 크기와 무관합니다. 등호는 코시-슈바르츠의 등호 조건, 곧 $h(\tau)=c\,s(T-\tau)$일 때만 성립하며 이 필터를 정합필터라고 합니다. 뒤집어 지연시킨 신호 자신이 필터가 되므로 출력은 입력과 신호의 상관이 됩니다. 최대값이 파형의 모양이 아니라 에너지 $E$로만 정해진다는 점이 핵심이며, 잡음 속에서 신호를 찾을 때는 파형을 바꾸지 말고 에너지를 키워야 합니다. $s(t)=A$ (단 $0\le t\le T$)이면 $E=A^{2}T$이고 정합필터는 폭 $T$의 적분기이며 최대 신호 대 잡음비는 $2A^{2}T/N_0$입니다. $\square$

> **문제 6.** (심화) $y'+ay=\cos\omega_0t$, $y(0)=0$, $a>0$을 라플라스 변환으로 풀고 정상상태 항의 진폭과 위상이 주파수 응답 $H(\omega_0)$과 일치함을 확인하십시오.
> **답.** $y(t)=\dfrac{-a}{a^{2}+\omega_0^{2}}e^{-at}+\dfrac{a\cos\omega_0t+\omega_0\sin\omega_0t}{a^{2}+\omega_0^{2}}$이며 정상상태 진폭은 $\dfrac{1}{\sqrt{a^{2}+\omega_0^{2}}}$입니다.
> **풀이.** 변환하면 $(s+a)Y=\dfrac{s}{s^{2}+\omega_0^{2}}$이므로 상이 다음과 같습니다.
> $$Y(s)=\frac{s}{(s+a)(s^{2}+\omega_0^{2})}=\frac{A}{s+a}+\frac{Bs+C}{s^{2}+\omega_0^{2}}$$
> $s=-a$를 대입하면 $A=\dfrac{-a}{a^{2}+\omega_0^{2}}$입니다. $s^{2}$의 계수 비교에서 $A+B=0$이므로 $B=\dfrac{a}{a^{2}+\omega_0^{2}}$이고, 상수항 비교 $A\omega_0^{2}+Ca=0$에서 $C=\dfrac{\omega_0^{2}}{a^{2}+\omega_0^{2}}$입니다. $s$의 계수는 $Ba+C=1$로 분자와 맞으므로 분해가 옳습니다. 각 항을 되돌리면 위 답이 됩니다. 이제 정상상태 항만 봅니다. $a\cos\omega_0t+\omega_0\sin\omega_0t$는 진폭 $\sqrt{a^{2}+\omega_0^{2}}$의 하나의 정현파이므로
> $$y_{\mathrm{ss}}(t)=\frac{1}{\sqrt{a^{2}+\omega_0^{2}}}\cos\left(\omega_0t-\arctan\frac{\omega_0}{a}\right)$$
> 입니다. 한편 이 계의 주파수 응답은 $H(\omega)=\dfrac{1}{a+i\omega}$이므로 크기가 $\dfrac{1}{\sqrt{a^{2}+\omega_0^{2}}}$이고 위상이 $-\arctan(\omega_0/a)$입니다. 두 결과가 정확히 일치합니다. 곧 크기 응답과 위상 응답은 과도항이 사라진 뒤의 응답을 읽는 도구이며, 극이 좌반평면에 있어 $e^{-at}$ 항이 잦아드는 계에서만 뜻을 가집니다. $\square$

> **문제 7.** (표준) 임펄스 응답이 $h(t)=\delta(t)+2\delta(t-T)+\delta(t-2T)$인 필터의 크기 응답과 위상 응답을 구하고 완전히 지워지는 진동수를 말하십시오.
> **답.** $\lvert H(\omega)\rvert=4\cos^{2}\dfrac{\omega T}{2}$, $\arg H(\omega)=-\omega T$이며 $\nu=\dfrac{1}{2T}$의 홀수배가 지워집니다.
> **풀이.** 각 델타의 변환이 지연 인자이므로 $H(\omega)=1+2e^{-i\omega T}+e^{-2i\omega T}$입니다. 중앙 항을 밖으로 빼내면 구조가 드러납니다.
> $$H(\omega)=e^{-i\omega T}\left(e^{i\omega T}+2+e^{-i\omega T}\right)=e^{-i\omega T}\left(2+2\cos\omega T\right)=4e^{-i\omega T}\cos^{2}\frac{\omega T}{2}$$
> 괄호 안이 실수이고 음이 아니므로 크기는 $4\cos^{2}(\omega T/2)$이고 위상은 $-\omega T$입니다. 위상이 $\omega$에 정확히 비례하므로 이 필터는 선형위상이며 모든 성분을 똑같이 $T$만큼 지연시킵니다. 임펄스 응답의 계수 배열 $1,2,1$이 중앙에 대해 대칭이라는 점이 선형위상의 근거입니다. 크기가 $0$이 되는 조건은 코사인의 영점이므로 다음과 같습니다.
> $$\frac{\omega T}{2}=\frac\pi2+k\pi\;\Longrightarrow\;\omega=\frac{(2k+1)\pi}{T},\qquad \nu=\frac{2k+1}{2T}$$
> 표본 간격이 $T$인 이산 구현에서는 이 자리가 나이퀴스트 진동수에 해당하므로, 이 필터는 표본마다 부호가 뒤집히는 성분을 완전히 지웁니다. $\omega=0$에서 크기가 $4$이므로 평균을 보존하려면 전체를 $1/4$로 나누어 씁니다. $\square$

## 10강. 열방정식과 파동방정식 풀이

> **문제 8.** (심화) 한쪽은 온도가 고정되고 다른 쪽은 단열된 막대에서 $u_t=u_{xx}$ (단 $0<x<1$), $u(0,t)=0$, $u_x(1,t)=0$, $u(x,0)=1$을 푸십시오.
> **답.** $u(x,t)=\displaystyle\sum_{n=1}^{\infty}\frac{4}{(2n-1)\pi}\sin\frac{(2n-1)\pi x}{2}\,e^{-\left(\frac{(2n-1)\pi}{2}\right)^{2}t}$입니다.
> **풀이.** $X''+\lambda X=0$에 $X(0)=0$과 $X'(1)=0$을 부과합니다. $\lambda=\mu^{2}>0$에서 $X=A\cos\mu x+B\sin\mu x$이고 $X(0)=0$이 $A=0$을 줍니다. 이어서 $X'(1)=B\mu\cos\mu=0$이므로 비자명 해가 되려면 $\cos\mu=0$, 곧 다음이 성립해야 합니다.
> $$\mu_n=\frac{(2n-1)\pi}{2},\qquad \lambda_n=\mu_n^{2},\qquad X_n(x)=\sin\mu_nx$$
> 고유값이 $n\pi$의 정수배가 아니라 반정수배로 나오는 것이 혼합 경계조건의 특징입니다. 직교성을 확인하면 $2\mu_n=(2n-1)\pi$이므로 $\int_{0}^{1}\sin^{2}\mu_nx\,dx=\frac12-\frac{\sin 2\mu_n}{4\mu_n}=\frac12$이고, 따라서 계수 공식은 $b_n=2\int_{0}^{1}f(x)\sin\mu_nx\,dx$입니다. $f=1$을 넣으면 $\cos\mu_n=0$이므로
> $$b_n=2\left[\frac{-\cos\mu_nx}{\mu_n}\right]_{0}^{1}=\frac{2}{\mu_n}=\frac{4}{(2n-1)\pi}$$
> 입니다. 시간 부분은 $T_n=e^{-\lambda_nt}$이므로 중첩하면 위 급수가 됩니다.
> $$u(x,t)=\sum_{n=1}^{\infty}\frac{4}{(2n-1)\pi}\sin\mu_nx\,e^{-\mu_n^{2}t},\qquad \mu_n=\frac{(2n-1)\pi}{2}$$
> 검산합니다. $t=0$에서 급수는 $\sum\frac{4}{(2n-1)\pi}\sin\frac{(2n-1)\pi x}{2}$이고 $x=1$을 넣으면 $\sin\frac{(2n-1)\pi}{2}=(-1)^{n-1}$이므로 $\frac4\pi\left(1-\frac13+\frac15-\cdots\right)=\frac4\pi\cdot\frac\pi4=1$로 초기조건과 맞습니다. 또 모든 항이 $x=0$에서 $0$이고 $x=1$에서 미분이 $0$이므로 경계조건도 만족합니다. $\square$

> **문제 9.** (표준) 옆면으로 열을 잃는 막대의 방정식 $u_t=u_{xx}-2u$ (단 $0<x<\pi$)를 $u(0,t)=u(\pi,t)=0$, $u(x,0)=3\sin x-\sin 3x$ 아래에서 푸십시오.
> **답.** $u(x,t)=3e^{-3t}\sin x-e^{-11t}\sin 3x$입니다.
> **풀이.** 손실항은 치환 하나로 걷어 낼 수 있습니다. $u=e^{-2t}v$로 두면 $u_t=e^{-2t}(v_t-2v)$이고 $u_{xx}=e^{-2t}v_{xx}$이므로 방정식이 $v_t=v_{xx}$로 돌아옵니다. 경계조건은 그대로 동차이고 초기조건도 그대로이므로 $v$는 표준 문제의 해입니다.
> $$v(x,t)=3e^{-t}\sin x-e^{-9t}\sin 3x$$
> 초기조건이 이미 고유함수 두 개의 결합이라 급수 전개가 필요하지 않고 감쇠율만 $n^{2}$으로 붙습니다. 여기에 $e^{-2t}$를 곱해 되돌립니다.
> $$u(x,t)=e^{-2t}v(x,t)=3e^{-3t}\sin x-e^{-11t}\sin 3x$$
> 직접 확인해도 같습니다. $u=e^{-\beta t}\sin nx$를 대입하면 $-\beta=-n^{2}-2$이므로 $\beta=n^{2}+2$이고, $n=1$에서 $3$, $n=3$에서 $11$입니다. 검산합니다. $t=0$에서 $u=3\sin x-\sin 3x$로 초기조건을 만족하고 두 항 모두 $x=0,\pi$에서 $0$입니다. 손실항은 모든 모드에 같은 크기 $2$를 더하므로 모드 사이의 상대적 감쇠 순서를 바꾸지 않고 전체를 균일하게 빨리 식힙니다. $\square$

> **문제 10.** (심화) 길이 $L$의 줄을 중앙에서 높이 $h$만큼 당겼다 놓았을 때, 곧 $f(x)=\dfrac{2hx}{L}$ $(0\le x\le L/2)$, $f(x)=\dfrac{2h(L-x)}{L}$ $(L/2\le x\le L)$, $g=0$일 때의 해를 구하고 어떤 배음이 빠지는지 말하십시오.
> **답.** $u(x,t)=\displaystyle\sum_{n=1}^{\infty}\frac{8h}{n^{2}\pi^{2}}\sin\frac{n\pi}{2}\,\sin\frac{n\pi x}{L}\cos\frac{n\pi ct}{L}$이며 짝수 배음이 모두 빠집니다.
> **풀이.** $g=0$이므로 $B_n=0$이고 $A_n$만 구하면 됩니다. $\mu=n\pi/L$로 두고 앞 구간을 부분적분하면
> $$I_1=\int_{0}^{L/2}\frac{2hx}{L}\sin\mu x\,dx
> =\frac{2h}{L}\left(\frac{\sin(n\pi/2)}{\mu^{2}}-\frac{L\cos(n\pi/2)}{2\mu}\right)$$
> 입니다. 뒤 구간은 $w=L-x$로 치환합니다. $\sin\mu(L-w)=-(-1)^{n}\sin\mu w$이므로 적분이 $I_2=-(-1)^{n}I_1$이 되고, 두 조각의 합은 $I_1\left(1-(-1)^{n}\right)$입니다. 짝수 $n$에서는 이 인자가 $0$이므로 계수가 사라지고, 홀수 $n$에서는 $\cos(n\pi/2)=0$이라 둘째 항도 사라져 계산이 짧아집니다. 따라서
> $$A_n=\frac{2}{L}\cdot 2I_1=\frac{8h}{n^{2}\pi^{2}}\sin\frac{n\pi}{2}$$
> 이고, 이 식은 $\sin(n\pi/2)$가 짝수 $n$에서 $0$이므로 두 경우를 한꺼번에 담습니다. 시간 부분은 $\omega_n=n\pi c/L$의 코사인이므로 위 급수를 얻습니다. 검산합니다. 앞의 세 홀수 계수를 계산하면 다음과 같습니다.
> $$A_1=\frac{8h}{\pi^{2}}\approx0.811h,\qquad
> A_3=-\frac{8h}{9\pi^{2}}\approx-0.090h,\qquad
> A_5=\frac{8h}{25\pi^{2}}\approx0.032h$$
> 계수가 $n^{2}$에 반비례해 줄어들므로 기본음이 압도적이고 높은 배음은 음색만 조금 바꿉니다. 짝수 배음이 빠지는 이유는 $n$이 짝수인 고유함수가 $x=L/2$에 절점을 갖는데 그 지점이 바로 줄을 당긴 자리이기 때문입니다. 절점을 직접 건드리는 위치에서 뜯으면 그 모드는 여기되지 않습니다. 기타에서 뜯는 위치를 바꾸면 음색이 달라지는 것이 같은 원리입니다. $\square$

> **문제 11.** (심화) 양 끝이 고정된 줄에서 $g=0$일 때 푸리에 급수 해가 달랑베르 공식과 일치함을 보이십시오.
> **답.** 급수를 곱의 합 공식으로 풀면 $f$의 홀·주기 확장 $\tilde f$에 대한 $\tfrac12\left[\tilde f(x-ct)+\tilde f(x+ct)\right]$가 됩니다. $\square$
> **풀이.** 급수 해는 $u=\sum_{n\ge1}A_n\sin\frac{n\pi x}{L}\cos\frac{n\pi ct}{L}$입니다. 각 항에 $\sin A\cos B=\tfrac12\left[\sin(A+B)+\sin(A-B)\right]$를 적용하고 합의 순서를 바꾸면
> $$u(x,t)=\frac12\sum_{n\ge1}A_n\sin\frac{n\pi(x+ct)}{L}+\frac12\sum_{n\ge1}A_n\sin\frac{n\pi(x-ct)}{L}$$
> 입니다. 여기서 $\tilde f(\xi)=\sum_{n\ge1}A_n\sin\frac{n\pi\xi}{L}$로 정의하면 위 식이 곧 $\tfrac12\left[\tilde f(x+ct)+\tilde f(x-ct)\right]$입니다. 이 $\tilde f$는 사인만으로 이루어진 급수이므로 $\tilde f(-\xi)=-\tilde f(\xi)$인 홀함수이고 주기가 $2L$입니다. 또 $0\le\xi\le L$에서는 $f$의 사인 급수이므로 $\tilde f=f$입니다. 곧 급수 해는 초기 변위를 홀함수로 주기 $2L$까지 확장한 뒤 달랑베르 공식을 그대로 쓴 것과 같습니다. 확장의 뜻도 분명합니다. $x=0$에서 $\tilde f$가 홀함수라 $u(0,t)=0$이 자동으로 성립하고, 왼쪽으로 나간 진행파는 부호가 뒤집힌 채 되돌아옵니다. 고정단 반사가 부호를 바꾼다는 물리가 홀함수 확장으로 나타납니다. 검산합니다. $L=\pi$, $c=1$, $f=\sin x$이면 급수 해는 $\sin x\cos t$이고 달랑베르 공식은 $\tfrac12\left[\sin(x+t)+\sin(x-t)\right]=\sin x\cos t$로 같습니다. $\square$

> **문제 12.** (심화) 무한 막대에서 초기분포가 $f(x)=T_0$ $(x<0)$, $f(x)=0$ $(x>0)$일 때 해를 열핵으로 구하십시오.
> **답.** $u(x,t)=\dfrac{T_0}{2}\operatorname{erfc}\!\left(\dfrac{x}{2\sqrt{\alpha t}}\right)$입니다.
> **풀이.** 해는 초기분포와 열핵의 합성곱이고 초기분포가 음의 반직선에서만 $T_0$이므로 적분 구간이 잘립니다.
> $$u(x,t)=\int_{-\infty}^{0}\frac{T_0}{\sqrt{4\pi\alpha t}}\,e^{-(x-s)^{2}/(4\alpha t)}\,ds$$
> $v=\dfrac{x-s}{\sqrt{4\alpha t}}$로 치환하면 $ds=-\sqrt{4\alpha t}\,dv$이고, $s=-\infty$가 $v=+\infty$에, $s=0$이 $v=z=\dfrac{x}{2\sqrt{\alpha t}}$에 대응합니다. 부호가 두 번 뒤집혀 적분이 정방향으로 정리됩니다.
> $$u(x,t)=\frac{T_0\sqrt{4\alpha t}}{\sqrt{4\pi\alpha t}}\int_{z}^{\infty}e^{-v^{2}}\,dv
> =\frac{T_0}{\sqrt\pi}\int_{z}^{\infty}e^{-v^{2}}\,dv=\frac{T_0}{2}\operatorname{erfc}(z)$$
> 마지막 등호는 $\operatorname{erfc}z=\frac{2}{\sqrt\pi}\int_z^{\infty}e^{-v^{2}}dv$라는 정의입니다. 검산합니다. $x=0$에서 $\operatorname{erfc}0=1$이므로 $u=T_0/2$이고, 이는 양쪽 값의 평균이라는 대칭성과 맞습니다. $x>0$을 고정하고 $t\to0^{+}$이면 $z\to\infty$이고 $\operatorname{erfc}\infty=0$이므로 초기조건도 맞습니다. 온도가 $T_0/4$까지 오른 지점은 $\operatorname{erfc}z=0.5$인 $z\approx0.477$에서 $x\approx0.95\sqrt{\alpha t}$이므로 계단이 뭉개지는 폭은 시간의 제곱근에 비례합니다. 10강의 반무한 막대 문제에서는 경계를 계속 $T_0$으로 붙잡았기 때문에 답이 $T_0\operatorname{erfc}$였고, 여기서는 붙잡지 않아 절반이 됩니다. $\square$

> **문제 13.** (심화) 반무한 막대 $x>0$의 표면 온도가 $u(0,t)=T_0\cos\omega t$로 진동할 때의 정상상태 해를 구하고, $\alpha=10^{-6}\ \mathrm{m^{2}/s}$인 흙에서 연주기 변동의 감쇠 깊이를 구하십시오.
> **답.** $u(x,t)=T_0e^{-kx}\cos(\omega t-kx)$이고 $k=\sqrt{\dfrac{\omega}{2\alpha}}$이며 감쇠 깊이는 약 $3.2\ \mathrm{m}$입니다.
> **풀이.** 정상상태에서는 모든 점이 같은 진동수로 흔들리므로 $u=\operatorname{Re}\left[T_0e^{i\omega t}\phi(x)\right]$로 두고 $\phi$를 찾습니다. 대입하면 $i\omega\phi=\alpha\phi''$이므로
> $$\phi''=\frac{i\omega}{\alpha}\phi\;\Longrightarrow\;\phi=e^{\pm qx},\qquad q=\sqrt{\frac{i\omega}{\alpha}}=(1+i)\sqrt{\frac{\omega}{2\alpha}}$$
> 입니다. 가운데 등호는 $\sqrt i=\dfrac{1+i}{\sqrt2}$이기 때문입니다. 깊이 들어갈수록 유계여야 하므로 커지는 쪽을 버리고 $\phi=e^{-qx}$를 택합니다. $k=\sqrt{\omega/(2\alpha)}$로 두면 $\phi=e^{-kx}e^{-ikx}$이고 $\phi(0)=1$이라 표면 조건도 맞으므로
> $$u(x,t)=\operatorname{Re}\left[T_0e^{i\omega t}e^{-kx}e^{-ikx}\right]=T_0e^{-kx}\cos(\omega t-kx)$$
> 입니다. 진폭은 깊이에 따라 지수적으로 줄고 위상은 $kx$만큼 늦어지므로, 이 해를 열파라고 부릅니다. 수치를 넣습니다. 주기가 $T=3.156\times10^{7}$초이므로 $\omega=2\pi/T\approx1.99\times10^{-7}\ \mathrm{rad/s}$이고
> $$k=\sqrt{\frac{1.99\times10^{-7}}{2\times10^{-6}}}\approx0.316\ \mathrm{m^{-1}},\qquad \frac1k\approx3.2\ \mathrm{m}$$
> 입니다. 곧 깊이 $3.2\ \mathrm{m}$에서 연중 온도차가 표면의 $1/e$, 약 $37$퍼센트로 줄어듭니다. 같은 깊이에서 위상은 $kx=1$라디안 늦어지고, 1라디안을 날수로 바꾸면 다음과 같습니다.
> $$\frac{T}{2\pi}=\frac{3.156\times10^{7}}{6.283}\ \text{초}\approx5.02\times10^{6}\ \text{초}\approx58\ \text{일}$$
> 그 깊이에서는 가장 추운 때가 지표보다 약 두 달 늦게 찾아옵니다. 감쇠 깊이가 $\sqrt{\alpha/\omega}$ 규모이므로 주기가 짧은 하루 변동은 훨씬 얕은 곳에서 사라집니다. $\square$

> **문제 14.** (심화) 끝이 고정된 반무한 줄 $x>0$에서 $c=1$, $u(0,t)=0$, $u_t(x,0)=0$이고 초기 변위 $f$가 $1<x<2$에서만 $0$이 아닙니다. $u(0.5,t)$가 $0$이 아닌 시간 구간을 모두 구하십시오.
> **답.** 직접파가 $0.5<t<1.5$에, 반사파가 $1.5<t<2.5$에 나타나며 반사파의 부호는 반대입니다.
> **풀이.** $f$를 원점에 대해 홀함수로 확장한 $\tilde f$를 쓰면 고정단 조건이 자동으로 성립하고, 해는 무한 줄의 달랑베르 공식과 같습니다.
> $$u(x,t)=\frac{\tilde f(x-t)+\tilde f(x+t)}{2},\qquad \tilde f(-\xi)=-\tilde f(\xi)$$
> $x=0.5$를 넣고 두 항을 따로 봅니다. 첫 항의 인수는 $0.5+t$이고 이 값이 $(1,2)$에 들어가는 조건은 $0.5<t<1.5$입니다. 그 구간에서 $u=\tfrac12f(0.5+t)$로 원래 부호를 그대로 가집니다. 둘째 항의 인수는 $0.5-t$이며 $t>0.5$에서 음수이므로 홀함수 성질로 $\tilde f(0.5-t)=-f(t-0.5)$입니다. 이 값이 $0$이 아닐 조건은 $t-0.5\in(1,2)$, 곧 $1.5<t<2.5$입니다.
> $$u(0.5,t)=\begin{cases}\tfrac12f(0.5+t), & 0.5<t<1.5\\[2pt] -\tfrac12f(t-0.5), & 1.5<t<2.5\\[2pt] 0, & \text{그 밖}\end{cases}$$
> 두 구간이 겹치지 않으므로 관측점은 먼저 왼쪽으로 달리는 펄스를 보고, 그 펄스가 원점에서 되튄 뒤 다시 지나가는 것을 봅니다. 부호가 뒤집힌 것은 고정단 반사의 특징이며, 끝이 자유롭다면 짝함수로 확장해 부호가 그대로 유지됩니다. 시간 간격도 확인됩니다. 초기 자료의 왼쪽 끝 $x=1$이 관측점까지 오는 데 $0.5$가 걸리고, 원점에서 되튀어 돌아오는 데 다시 $1$이 더 걸려 반사파의 시작이 $1.5$입니다. $\square$

## 관련 강의

- [9. 신호 처리와 필터링](../9. 신호 처리와 필터링/index.md)
- [10. 열방정식과 파동방정식 풀이](../10. 열방정식과 파동방정식 풀이/index.md)
- [04. 변환의 응용](../index.md)
