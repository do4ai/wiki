---
title: "문제집 - 03. 라플라스 변환"
---
# 문제집 - 03. 라플라스 변환

3단원의 두 강의(7강 라플라스 변환의 정의와 성질, 8강 역변환과 미분방정식 풀이)를 강의별로 묶은 문제집입니다. 각 문제는 문제·답·풀이 세 줄로 되어 있고, 본문 강의에 실린 드릴과 겹치지 않도록 모두 새로 지었으며 난이도를 한 단계 올렸습니다. 정의적분을 직접 계산하는 문항, 변환 규칙 두세 개를 겹쳐 써야 풀리는 문항, 불연속 강제항이 들어간 초기값 문제를 고르게 배치했으므로 계산 문항은 부분분수 계수를 다시 대입해 검산하고 유도 문항은 논리 전개를 스스로 다시 써 보는 것이 좋습니다. 변환 규약은 7강과 같이 $F(s)=\int_0^{\infty}f(t)e^{-st}\,dt$이고 표기는 KaTeX를 따릅니다.

## 7강. 라플라스 변환의 정의와 성질

> **문제 1.** (표준) 삼각 펄스 $f(t)=t$ $(0\le t<1)$, $f(t)=2-t$ $(1\le t<2)$, $f(t)=0$ $(t\ge2)$의 변환을 정의적분으로 직접 계산하고 수렴 영역을 말하십시오.
> **답.** $F(s)=\dfrac{(1-e^{-s})^{2}}{s^{2}}$이고 수렴 영역은 복소평면 전체입니다.
> **풀이.** 두 구간으로 나누어 각각 부분적분합니다. 앞 구간은
> $$\int_{0}^{1}te^{-st}\,dt=\left[-\frac{t}{s}e^{-st}\right]_{0}^{1}+\frac1s\int_{0}^{1}e^{-st}\,dt=-\frac{e^{-s}}{s}+\frac{1-e^{-s}}{s^{2}}$$
> 입니다. 뒤 구간은 $v=2-t$로 치환하면 $t=2-v$, $dt=-dv$이고 적분 구간이 $v:1\to0$이 되므로
> $$\int_{1}^{2}(2-t)e^{-st}\,dt=e^{-2s}\int_{0}^{1}ve^{sv}\,dv=e^{-2s}\left(\frac{e^{s}}{s}-\frac{e^{s}-1}{s^{2}}\right)=\frac{e^{-s}}{s}-\frac{e^{-s}-e^{-2s}}{s^{2}}$$
> 입니다. 두 결과를 더하면 $1/s$ 항이 상쇄되고 $F(s)=\dfrac{1-2e^{-s}+e^{-2s}}{s^{2}}=\dfrac{(1-e^{-s})^{2}}{s^{2}}$입니다. 검산합니다. 이 삼각 펄스는 폭 $1$인 사각 펄스 두 개의 합성곱이고 사각 펄스의 변환이 $(1-e^{-s})/s$이므로, 합성곱 정리에 따라 상은 그 제곱이어야 하며 실제로 일치합니다. $f$가 유계이고 유한 구간 밖에서 $0$이므로 적분이 유한 구간 적분이고 모든 $s$에서 수렴합니다. 곧 수렴 가로좌표는 $\sigma_c=-\infty$입니다. $\square$

> **문제 2.** (심화) $\mathcal{L}\left\{\dfrac{\sin t}{t}\right\}$를 $s$ 미분 규칙으로 구하고 수렴 가로좌표를 말하십시오.
> **답.** $G(s)=\arctan\dfrac1s$이고 수렴 가로좌표는 $\sigma_c=0$입니다.
> **풀이.** $g(t)=\dfrac{\sin t}{t}$로 두면 $tg(t)=\sin t$입니다. $s$ 미분 규칙 $\mathcal{L}\{tg(t)\}=-G'(s)$를 쓰면
> $$-G'(s)=\frac{1}{s^{2}+1}\;\Longrightarrow\;G(s)=-\arctan s+C$$
> 입니다. 상수 $C$는 무한대에서의 거동으로 정해집니다. $\lvert\sin t\rvert\le t$에서 $\lvert g(t)\rvert\le 1$이므로 다음 부등식이 성립합니다.
> $$\lvert G(s)\rvert\le\int_{0}^{\infty}e^{-\sigma t}\,dt=\frac1\sigma$$
> 따라서 $\sigma\to\infty$에서 $G(s)\to0$입니다. 같은 극한에서 $\arctan s\to\pi/2$이므로 $C=\pi/2$입니다. 그러므로
> $$G(s)=\frac{\pi}{2}-\arctan s=\arctan\frac1s\qquad(\sigma>0)$$
> 입니다. 수렴 가로좌표는 $g$가 유계이므로 $\sigma_c=0$입니다. 검산합니다. $s\to0^{+}$에서 $G\to\pi/2$이고 이는 디리클레 적분 $\int_{0}^{\infty}\frac{\sin t}{t}\,dt=\frac\pi2$와 같은 값이므로 결과가 맞습니다. $\square$

> **문제 3.** (심화) $f(t)=u(t-\pi)\,t\sin t$의 라플라스 변환을 구하십시오.
> **답.** $F(s)=-e^{-\pi s}\left(\dfrac{2s}{(s^{2}+1)^{2}}+\dfrac{\pi}{s^{2}+1}\right)$입니다.
> **풀이.** 제2이동정리는 피승수가 $t-\pi$의 함수일 때만 그대로 쓸 수 있으므로 $t\sin t$를 $\tau=t-\pi$의 식으로 고쳐 씁니다. $t=\tau+\pi$이고 $\sin t=\sin(\tau+\pi)=-\sin\tau$이므로
> $$t\sin t=-(\tau+\pi)\sin\tau=-\tau\sin\tau-\pi\sin\tau$$
> 입니다. 곧 $f(t)=u(t-\pi)\,h(t-\pi)$이고 $h(\tau)=-\tau\sin\tau-\pi\sin\tau$입니다. $s$ 미분 규칙에서 $\mathcal{L}\{\tau\sin\tau\}=\dfrac{2s}{(s^{2}+1)^{2}}$이므로
> $$H(s)=-\frac{2s}{(s^{2}+1)^{2}}-\frac{\pi}{s^{2}+1}$$
> 이고 제2이동정리로 $e^{-\pi s}$를 곱하면 최종 결과를 얻습니다.
> $$F(s)=e^{-\pi s}H(s)=-e^{-\pi s}\left(\frac{2s}{(s^{2}+1)^{2}}+\frac{\pi}{s^{2}+1}\right)$$
> $u(t-\pi)$를 붙이지 않고 $t\sin t$의 상에 그냥 $e^{-\pi s}$를 곱하면 틀린 답이 나오므로 재작성 단계를 건너뛰지 않아야 합니다. 같은 계산을 공식 $\mathcal{L}\{u(t-a)g(t)\}=e^{-as}\mathcal{L}\{g(t+a)\}$로 확인하면 $g(t+\pi)=-t\sin t-\pi\sin t$이므로 같은 상이 나옵니다. $\square$

> **문제 4.** (표준) 복소지수를 쓰지 않고 도함수 규칙만으로 $\mathcal{L}\{\sin\omega t\}$와 $\mathcal{L}\{\cos\omega t\}$를 동시에 유도하고, 적분 규칙으로 검산하십시오.
> **답.** $S(s)=\dfrac{\omega}{s^{2}+\omega^{2}}$, $C(s)=\dfrac{s}{s^{2}+\omega^{2}}$입니다.
> **풀이.** $S=\mathcal{L}\{\sin\omega t\}$, $C=\mathcal{L}\{\cos\omega t\}$로 둡니다. $(\sin\omega t)'=\omega\cos\omega t$이고 $\sin 0=0$이며, $(\cos\omega t)'=-\omega\sin\omega t$이고 $\cos 0=1$이므로 도함수 규칙 $\mathcal{L}\{f'\}=sF(s)-f(0)$이 두 관계를 줍니다.
> $$\omega C=sS,\qquad -\omega S=sC-1$$
> 첫 식에서 $C=sS/\omega$를 얻어 둘째 식에 넣으면 미지의 상이 하나로 줄어듭니다.
> $$-\omega S=\frac{s^{2}S}{\omega}-1\;\Longrightarrow\;(s^{2}+\omega^{2})S=\omega$$
> 따라서 $S=\dfrac{\omega}{s^{2}+\omega^{2}}$이고 이를 되돌려 넣으면 $C=\dfrac{s}{s^{2}+\omega^{2}}$입니다. 적분 규칙으로 검산합니다. $\int_{0}^{t}\cos\omega\tau\,d\tau=\dfrac{\sin\omega t}{\omega}$이므로 그 변환은 $\dfrac{1}{s^{2}+\omega^{2}}$이어야 하고, 규칙이 주는 값 $C(s)/s$도 같은 값입니다. 두 미지의 상을 연립방정식으로 한꺼번에 푸는 이 방식은 오일러 공식을 쓸 수 없는 상황에서도 통합니다. $\square$

> **문제 5.** (심화) $\mathcal{L}\{t^{2}e^{-t}\cos t\}$를 구하십시오.
> **답.** $\dfrac{2(s+1)\left[(s+1)^{2}-3\right]}{\left[(s+1)^{2}+1\right]^{3}}$입니다.
> **풀이.** 제1이동정리를 먼저 적용하면 지수 인자가 상의 평행이동으로 흡수됩니다. $w=s+1$로 두고 $F_0(s)=\mathcal{L}\{e^{-t}\cos t\}=\dfrac{w}{w^{2}+1}$로 씁니다. $s$에 대한 미분과 $w$에 대한 미분이 같으므로
> $$\frac{d}{dw}\frac{w}{w^{2}+1}=\frac{(w^{2}+1)-2w^{2}}{(w^{2}+1)^{2}}=\frac{1-w^{2}}{(w^{2}+1)^{2}}$$
> 입니다. 한 번 더 미분하면 몫의 미분법에서 분자가 $-2w(w^{2}+1)-4w(1-w^{2})=2w^{3}-6w$가 되므로 다음을 얻습니다.
> $$\frac{d^{2}}{dw^{2}}\frac{w}{w^{2}+1}=\frac{2w^{3}-6w}{(w^{2}+1)^{3}}$$
> $n=2$이므로 $s$ 미분 규칙은 $(-1)^{2}F_0''(s)$를 주고
> $$\mathcal{L}\{t^{2}e^{-t}\cos t\}=\frac{2w(w^{2}-3)}{(w^{2}+1)^{3}}\Big|_{w=s+1}$$
> 입니다. 검산합니다. $a=0$인 경우로 되돌리면 $\mathcal{L}\{t^{2}\cos t\}=\dfrac{2s(s^{2}-3)}{(s^{2}+1)^{3}}$이고 이는 표준 변환표의 값과 같습니다. 이동정리를 먼저 쓰고 미분을 뒤에 하면 계산이 훨씬 짧아집니다. $\square$

> **문제 6.** (심화) 반파 정류된 사인 $f(t)=\sin t$ $(0\le t<\pi)$, $f(t)=0$ $(\pi\le t<2\pi)$가 주기 $2\pi$로 반복될 때 변환을 구하십시오.
> **답.** $F(s)=\dfrac{1}{(1-e^{-\pi s})(s^{2}+1)}$입니다.
> **풀이.** 한 주기 적분을 먼저 계산합니다. 부정적분이 $\dfrac{e^{-st}(-s\sin t-\cos t)}{s^{2}+1}$이므로
> $$\int_{0}^{\pi}e^{-st}\sin t\,dt=\frac{e^{-\pi s}\cdot 1-(-1)}{s^{2}+1}=\frac{1+e^{-\pi s}}{s^{2}+1}$$
> 입니다. 주기함수 공식에 $T=2\pi$를 넣으면
> $$F(s)=\frac{1}{1-e^{-2\pi s}}\cdot\frac{1+e^{-\pi s}}{s^{2}+1}$$
> 입니다. 분모를 $1-e^{-2\pi s}=(1-e^{-\pi s})(1+e^{-\pi s})$로 인수분해하면 $1+e^{-\pi s}$가 약분됩니다.
> $$F(s)=\frac{1}{(1-e^{-\pi s})(s^{2}+1)}$$
> 검산합니다. 반파 정류에 반주기 지연한 것을 더하면 $\lvert\sin t\rvert$가 되고, 그 상은 $F(s)(1+e^{-\pi s})=\dfrac{1+e^{-\pi s}}{(1-e^{-\pi s})(s^{2}+1)}$이며 이는 전파 정류 사인의 알려진 변환과 같습니다. $\square$

> **문제 7.** (심화) $F(s)=\dfrac{2s+3}{s(s+1)(s+4)}$에 대해 $f(0^{+})$, $f'(0^{+})$, $\lim_{t\to\infty}f(t)$를 상에서 읽고 역변환으로 검산하십시오.
> **답.** $f(0^{+})=0$, $f'(0^{+})=2$, $\lim_{t\to\infty}f(t)=\dfrac34$입니다.
> **풀이.** 먼저 $s$를 곱해 정리합니다.
> $$sF(s)=\frac{2s+3}{(s+1)(s+4)}$$
> 분모의 차수가 분자보다 높으므로 $s\to\infty$에서 이 값은 $0$이고, 초기값 정리에 따라 $f(0^{+})=0$입니다. 도함수의 상은 $\mathcal{L}\{f'\}=sF(s)-f(0^{+})=sF(s)$이므로 같은 정리를 한 번 더 적용하면
> $$f'(0^{+})=\lim_{s\to\infty}s\cdot sF(s)=\lim_{s\to\infty}\frac{s(2s+3)}{(s+1)(s+4)}=2$$
> 입니다. 최종값은 $sF(s)$의 극이 $-1$과 $-4$로 모두 좌반평면에 있으므로 정리를 쓸 수 있고 $\lim_{s\to0}\dfrac{2s+3}{(s+1)(s+4)}=\dfrac34$입니다. 검산합니다. 단순근 분해에서 계수는 $s=0$에서 $\dfrac{3}{1\cdot4}=\dfrac34$, $s=-1$에서 $\dfrac{1}{(-1)(3)}=-\dfrac13$, $s=-4$에서 $\dfrac{-5}{(-4)(-3)}=-\dfrac{5}{12}$이므로
> $$f(t)=\frac34-\frac13e^{-t}-\frac{5}{12}e^{-4t}$$
> 입니다. 실제로 $f(0)=\frac{9-4-5}{12}=0$이고 $f'(t)=\frac13e^{-t}+\frac53e^{-4t}$에서 $f'(0)=2$이며 $t\to\infty$에서 $f\to\frac34$입니다. 세 값이 모두 일치합니다. $\square$

## 8강. 역변환과 미분방정식 풀이

> **문제 8.** (표준) $\mathcal{L}^{-1}\left\{\dfrac{2s^{2}+3}{s(s+1)^{2}}\right\}$을 구하고 양 끝값으로 검산하십시오.
> **답.** $f(t)=3-e^{-t}-5te^{-t}$입니다.
> **풀이.** 중근이 있으므로 그 인수에 대해 항을 두 개 세웁니다. 분해를 $\dfrac{A}{s}+\dfrac{B}{s+1}+\dfrac{C}{(s+1)^{2}}$로 두고 분모를 곱하면
> $$2s^{2}+3=A(s+1)^{2}+Bs(s+1)+Cs$$
> 입니다. $s=0$을 넣으면 $A=3$이고, $s=-1$을 넣으면 $5=-C$이므로 $C=-5$입니다. $s^{2}$의 계수를 비교하면 $2=A+B$이므로 $B=-1$입니다. 곧 분해가 다음과 같습니다.
> $$F(s)=\frac{3}{s}-\frac{1}{s+1}-\frac{5}{(s+1)^{2}}$$
> 중근 항의 역변환 규칙 $\mathcal{L}^{-1}\{(s-p)^{-j}\}=\dfrac{t^{j-1}}{(j-1)!}e^{pt}$를 각 항에 적용하면 $3$, $-e^{-t}$, $-5te^{-t}$이므로 위 결과를 얻습니다. 검산합니다. 초기값 정리는 $\lim_{s\to\infty}sF(s)=\lim\dfrac{2s^{2}+3}{(s+1)^{2}}=2$를 주고 실제로 $f(0)=3-1-0=2$입니다. 최종값 정리는 $sF(s)$의 극이 $-1$뿐이라 쓸 수 있고 $\lim_{s\to0}\dfrac{2s^{2}+3}{(s+1)^{2}}=3$이며, $t\to\infty$에서 지수항이 사라져 $f\to3$입니다. $\square$

> **문제 9.** (심화) 합성곱 정리만으로 $\mathcal{L}^{-1}\left\{\dfrac{1}{(s^{2}+\omega^{2})^{2}}\right\}$을 구하십시오.
> **답.** $\dfrac{\sin\omega t-\omega t\cos\omega t}{2\omega^{3}}$입니다.
> **풀이.** 상을 $\dfrac{1}{s^{2}+\omega^{2}}\cdot\dfrac{1}{s^{2}+\omega^{2}}$로 보면 두 인자의 역변환이 모두 $\dfrac{\sin\omega t}{\omega}$입니다. 합성곱 정리에 따라
> $$f(t)=\frac{1}{\omega^{2}}\int_{0}^{t}\sin\omega\tau\,\sin\omega(t-\tau)\,d\tau$$
> 입니다. 곱을 합으로 바꾸는 공식 $\sin A\sin B=\tfrac12\left[\cos(A-B)-\cos(A+B)\right]$에서 $A=\omega\tau$, $B=\omega t-\omega\tau$이므로 $A-B=2\omega\tau-\omega t$이고 $A+B=\omega t$입니다. 따라서
> $$\int_{0}^{t}\sin\omega\tau\sin\omega(t-\tau)\,d\tau
> =\frac12\left[\frac{\sin(2\omega\tau-\omega t)}{2\omega}\right]_{0}^{t}-\frac{t\cos\omega t}{2}
> =\frac{\sin\omega t}{2\omega}-\frac{t\cos\omega t}{2}$$
> 입니다. 앞의 대괄호는 $\sin\omega t$와 $-\sin\omega t$의 차이므로 $2\sin\omega t$가 되고 그 절반을 $2\omega$로 나눈 값이 남습니다. $1/\omega^{2}$을 곱해 정리하면 답이 됩니다. 검산합니다. $s$ 미분 규칙에서 $\mathcal{L}\{t\cos\omega t\}=\dfrac{s^{2}-\omega^{2}}{(s^{2}+\omega^{2})^{2}}$이므로
> $$\mathcal{L}\left\{\frac{\sin\omega t-\omega t\cos\omega t}{2\omega^{3}}\right\}
> =\frac{1}{2\omega^{3}}\left[\frac{\omega}{s^{2}+\omega^{2}}-\frac{\omega(s^{2}-\omega^{2})}{(s^{2}+\omega^{2})^{2}}\right]
> =\frac{1}{2\omega^{2}}\cdot\frac{2\omega^{2}}{(s^{2}+\omega^{2})^{2}}$$
> 이고 이는 원래 상과 같습니다. $\square$

> **문제 10.** (심화) $y''+3y'+2y=u(t-1)+\delta(t-2)$, $y(0)=0$, $y'(0)=1$을 푸십시오.
> **답.** $y(t)=e^{-t}-e^{-2t}+u(t-1)\left[\tfrac12-e^{-(t-1)}+\tfrac12e^{-2(t-1)}\right]+u(t-2)\left[e^{-(t-2)}-e^{-2(t-2)}\right]$입니다.
> **풀이.** 도함수 규칙에서 $\mathcal{L}\{y''\}=s^{2}Y-1$이고 $\mathcal{L}\{3y'\}=3sY$이므로 변환하면
> $$(s^{2}+3s+2)Y-1=\frac{e^{-s}}{s}+e^{-2s}$$
> 입니다. 좌변의 이차식이 $(s+1)(s+2)$로 인수분해되므로 $Y$를 세 조각으로 정리합니다.
> $$Y=\frac{1}{(s+1)(s+2)}+\frac{e^{-s}}{s(s+1)(s+2)}+\frac{e^{-2s}}{(s+1)(s+2)}$$
> 첫 조각은 초기속도가, 둘째는 계단 입력이, 셋째는 충격 입력이 만든 몫입니다. 지수인자를 떼고 남은 두 상을 각각 되돌립니다. 단순근 분해에서 $\dfrac{1}{(s+1)(s+2)}$의 계수는 $s=-1$에서 $1$, $s=-2$에서 $-1$이므로 역변환이 $e^{-t}-e^{-2t}$입니다. 또 $\dfrac{1}{s(s+1)(s+2)}$의 계수는 $s=0$에서 $\tfrac12$, $s=-1$에서 $-1$, $s=-2$에서 $\tfrac12$이므로 역변환이 $\tfrac12-e^{-t}+\tfrac12e^{-2t}$입니다. 제2이동정리로 각각 $1$과 $2$만큼 지연시켜 더하면 위 답이 됩니다. 검산합니다. $t<1$에서 $y=e^{-t}-e^{-2t}$이므로 $y(0)=0$이고 $y'(0)=-1+2=1$로 초기조건을 만족합니다. $t\to\infty$에서 지수항이 모두 사라지고 계단 입력이 만든 $\tfrac12$만 남는데, 이는 정상상태 $2y=1$과 일치합니다. 델타 입력은 $t=2$에서 $y'$을 $1$만큼 도약시키고 그 뒤로는 감쇠 항만 더합니다. $\square$

> **문제 11.** (심화) 적분방정식 $y(t)=t+\displaystyle\int_{0}^{t}y(\tau)\sin(t-\tau)\,d\tau$를 라플라스 변환으로 푸십시오.
> **답.** $y(t)=t+\dfrac{t^{3}}{6}$입니다.
> **풀이.** 우변의 적분이 $y*\sin$ 꼴의 합성곱이므로 변환하면 곱이 됩니다.
> $$Y(s)=\frac{1}{s^{2}}+Y(s)\cdot\frac{1}{s^{2}+1}$$
> 입니다. $Y$를 좌변으로 모으면 괄호 안이 하나의 분수로 합쳐집니다.
> $$Y\left(1-\frac{1}{s^{2}+1}\right)=\frac{1}{s^{2}}
> \;\Longrightarrow\;
> Y\cdot\frac{s^{2}}{s^{2}+1}=\frac{1}{s^{2}}$$
> 양변에 $\dfrac{s^{2}+1}{s^{2}}$을 곱하면 상이 두 항의 합으로 정리됩니다.
> $$Y=\frac{s^{2}+1}{s^{4}}=\frac{1}{s^{2}}+\frac{1}{s^{4}}$$
> $\mathcal{L}^{-1}\{1/s^{2}\}=t$이고 $\mathcal{L}^{-1}\{1/s^{4}\}=t^{3}/3!$이므로 $y=t+t^{3}/6$입니다. 검산합니다. 구한 $y$를 우변에 넣으면 합성곱 부분의 상이 $\left(\dfrac{1}{s^{2}}+\dfrac{1}{s^{4}}\right)\dfrac{1}{s^{2}+1}=\dfrac{s^{2}+1}{s^{4}}\cdot\dfrac{1}{s^{2}+1}=\dfrac{1}{s^{4}}$이므로 그 값은 $t^{3}/6$이고, 여기에 $t$를 더하면 정확히 $y$가 됩니다. 미지함수가 적분 안에 갇힌 방정식도 합성곱 구조만 알아보면 대수방정식으로 내려옵니다. $\square$

> **문제 12.** (심화) $x'=-2x+y+1$, $y'=x-2y$, $x(0)=y(0)=0$을 푸십시오.
> **답.** $x(t)=\dfrac23-\dfrac12e^{-t}-\dfrac16e^{-3t}$, $y(t)=\dfrac13-\dfrac12e^{-t}+\dfrac16e^{-3t}$입니다.
> **풀이.** 두 식을 변환하면 초기값이 모두 $0$이므로
> $$(s+2)X-Y=\frac1s,\qquad -X+(s+2)Y=0$$
> 입니다. 둘째 식에서 $X=(s+2)Y$이고 이를 첫째 식에 넣으면 다음이 됩니다.
> $$\left[(s+2)^{2}-1\right]Y=\frac1s$$
> $(s+2)^{2}-1=(s+1)(s+3)$이므로 두 상이 모두 단순근 세 개의 유리함수가 됩니다.
> $$Y=\frac{1}{s(s+1)(s+3)},\qquad X=\frac{s+2}{s(s+1)(s+3)}$$
> $Y$의 계수는 $s=0$에서 $\dfrac{1}{1\cdot3}=\dfrac13$, $s=-1$에서 $\dfrac{1}{(-1)(2)}=-\dfrac12$, $s=-3$에서 $\dfrac{1}{(-3)(-2)}=\dfrac16$입니다. $X$의 계수는 $s=0$에서 $\dfrac{2}{1\cdot3}=\dfrac23$, $s=-1$에서 $\dfrac{1}{(-1)(2)}=-\dfrac12$, $s=-3$에서 $\dfrac{-1}{(-3)(-2)}=-\dfrac16$입니다. 검산합니다. $x(0)=\frac23-\frac12-\frac16=0$이고 $y(0)=\frac13-\frac12+\frac16=0$입니다. 또 $t\to\infty$에서 $x\to\frac23$, $y\to\frac13$인데, 정상상태 조건 $-2x+y+1=0$과 $x-2y=0$을 풀면 $x=2y$이고 $y=\frac13$이므로 값이 일치합니다. $\square$

> **문제 13.** (심화) 유수정리로 $\mathcal{L}^{-1}\left\{\dfrac{s}{(s^{2}+\omega^{2})^{2}}\right\}$을 구하십시오.
> **답.** $\dfrac{t\sin\omega t}{2\omega}$입니다.
> **풀이.** 상은 $s=\pm i\omega$에 2위 극을 가집니다. $m=2$인 유수 공식은 $\lim_{s\to p}\dfrac{d}{ds}\left[(s-p)^{2}F(s)e^{st}\right]$이므로 $p=i\omega$에서 괄호 안이 $\dfrac{se^{st}}{(s+i\omega)^{2}}$입니다. 미분하면
> $$\frac{d}{ds}\frac{se^{st}}{(s+i\omega)^{2}}=\frac{\left[(1+st)(s+i\omega)-2s\right]e^{st}}{(s+i\omega)^{3}}$$
> 입니다. $s=i\omega$를 대입하면 분자의 대괄호는 $(1+i\omega t)(2i\omega)-2i\omega=-2\omega^{2}t$이고 분모는 $(2i\omega)^{3}=-8i\omega^{3}$이므로 유수는 $\dfrac{t}{4i\omega}e^{i\omega t}$입니다. $F$의 계수가 실수이므로 $s=-i\omega$에서의 유수는 그 켤레인 $-\dfrac{t}{4i\omega}e^{-i\omega t}$입니다. 두 유수를 더하면
> $$f(t)=\frac{t}{4i\omega}\left(e^{i\omega t}-e^{-i\omega t}\right)=\frac{t}{4i\omega}\cdot 2i\sin\omega t=\frac{t\sin\omega t}{2\omega}$$
> 입니다. 검산합니다. $s$ 미분 규칙에서 $\mathcal{L}\{t\sin\omega t\}=\dfrac{2\omega s}{(s^{2}+\omega^{2})^{2}}$이므로 양변을 $2\omega$로 나누면 원래 상이 나옵니다. 2위 극이 $t$가 곱해진 항을 만든다는 규칙이 실수 극에서만이 아니라 허수축 위의 극에서도 그대로 성립합니다. $\square$

> **문제 14.** (심화) 전달함수가 $H_1(s)=\dfrac{1}{s^{2}+2s+2}$인 계와 $H_2(s)=\dfrac{1}{s^{2}+2}$인 계에 단위계단을 넣습니다. 각각 최종값 정리를 적용할 수 있는지 판정하고 실제 응답과 비교하십시오.
> **답.** 첫 계는 적용 가능하며 최종값이 $\dfrac12$이고, 둘째 계는 적용할 수 없으며 응답에 극한이 없습니다.
> **풀이.** 첫 계는 $Y_1=\dfrac{1}{s(s^{2}+2s+2)}$이므로 $sY_1$의 극이 $-1\pm i$로 모두 좌반평면에 있고 정리를 쓸 수 있습니다. 값은 $\lim_{s\to0}\dfrac{1}{s^{2}+2s+2}=\dfrac12$입니다. 실제 역변환을 구하면 분해는
> $$\frac{1}{s(s^{2}+2s+2)}=\frac{1/2}{s}-\frac12\cdot\frac{(s+1)+1}{(s+1)^{2}+1}$$
> 이므로 $y_1(t)=\tfrac12-\tfrac12e^{-t}\cos t-\tfrac12e^{-t}\sin t$이고 $t\to\infty$에서 $\tfrac12$로 수렴하므로 정리와 일치합니다. 둘째 계는 $Y_2=\dfrac{1}{s(s^{2}+2)}$이고 $sY_2$의 극이 $\pm i\sqrt2$로 허수축 위에 있어 조건이 깨집니다. 공식을 그대로 쓰면 $\lim_{s\to0}\dfrac{1}{s^{2}+2}=\dfrac12$이라는 값이 나오지만 이는 잘못된 결론입니다. 실제로 $\dfrac{1}{s(s^{2}+2)}=\dfrac{1/2}{s}-\dfrac12\cdot\dfrac{s}{s^{2}+2}$이므로
> $$y_2(t)=\tfrac12\left(1-\cos\sqrt2\,t\right)$$
> 이고 이 함수는 $0$과 $1$ 사이를 영원히 진동해 극한을 갖지 않습니다. 공식이 준 $\tfrac12$은 진동의 시간평균일 뿐입니다. 최종값 정리는 계산 전에 반드시 극의 위치를 확인해야 하는 정리입니다. $\square$

## 관련 강의

- [7. 라플라스 변환의 정의와 성질](../7. 라플라스 변환의 정의와 성질/index.md)
- [8. 역변환과 미분방정식 풀이](../8. 역변환과 미분방정식 풀이/index.md)
- [03. 라플라스 변환](../index.md)
