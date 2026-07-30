---
title: "문제집 - 05. 해석함수의 대역 이론"
---
# 문제집 - 05. 해석함수의 대역 이론

5단원의 두 강의(10강 리우빌 정리와 대수학의 기본정리, 11강 등각사상과 뫼비우스 변환)를 강의별로 묶어 정리한 문제집입니다. 각 문제는 문제·답·풀이 세 줄로 되어 있으며, 본문 강의의 드릴보다 한 단계 어렵게 구성했습니다. 10강 몫은 코시 부등식으로 성장 조건을 다항식 차수로 번역하는 문항, 리우빌 정리를 보조함수 $e^{f}$나 $1/g$에 옮겨 적용하는 문항, 최대 절대값 원리와 슈바르츠 보조정리를 자기사상으로 옮겨 쓰는 문항, 항등정리로 함수방정식을 푸는 문항으로 구성했습니다. 11강 몫은 자기사상군을 직접 결정하는 문항, 여러 기본 사상을 이어 붙여 원하는 영역까지 옮기는 조립 문항, 등각사상을 디리클레 문제와 면적 배율로 읽는 문항으로 구성했습니다. 증명 문항은 가정이 어디서 쓰였는지 표시하며 다시 써 보는 것이 좋습니다. 표기는 KaTeX를 따릅니다.

## 10강. 리우빌 정리와 대수학의 기본정리

> **문제 1.** (표준) 전해석함수 $f$가 모든 $z$에서 $\lvert f(z)\rvert\le 3\lvert z\rvert^{5/2}$을 만족할 때 $f$의 꼴을 결정하십시오.
> **답.** $f(z)=a_1z+a_2z^{2}$ 꼴입니다.
> **풀이.** 코시 부등식을 원 $\lvert z\rvert=R$에 적용합니다. 그 원 위에서 $\lvert f\rvert\le 3R^{5/2}$이므로 각 $n$에 대해 다음이 성립합니다.
> $$\bigl\lvert f^{(n)}(0)\bigr\rvert\le\frac{n!\cdot 3R^{5/2}}{R^{n}}=3\,n!\,R^{5/2-n}$$
> $n\ge3$이면 지수 $\tfrac52-n$이 음수이므로 우변이 $R\to\infty$에서 $0$으로 갑니다. 좌변은 $R$과 무관한 고정된 수이므로 다음이 성립합니다.
> $$f^{(3)}(0)=f^{(4)}(0)=\cdots=0$$
> 테일러 정리에 의해 $f$는 이차 이하 다항식입니다. 가정에 $z=0$을 넣으면 $\lvert f(0)\rvert\le0$이라 상수항도 $0$입니다. 따라서 $f(z)=a_1z+a_2z^{2}$입니다. 지수 $\tfrac52$가 정수가 아니어도 결론이 정수 차수로 떨어진다는 점이 이 문항의 핵심입니다. 실제로 $f(z)=z^{2}$은 가정을 만족하고 $f(z)=z^{3}$은 만족하지 않습니다. $n=2$에서는 상계가 $6R^{1/2}$로 발산하므로 이차항을 억누를 수 없고, 그 지점에서 정확히 차수가 갈립니다.

> **문제 2.** (표준) $p(z)=z^{4}+6z+3$의 근이 모두 $\lvert z\rvert<2$ 안에 있음을 보이십시오.
> **답.** $\lvert z\rvert\ge2$에서 $\lvert p(z)\rvert\ge1>0$이므로 그 영역에는 근이 없습니다.
> **풀이.** 삼각부등식을 최고차항 쪽으로 씁니다. $\lvert z\rvert=t\ge2$이면 다음이 성립합니다.
> $$\lvert p(z)\rvert\ge\lvert z\rvert^{4}-6\lvert z\rvert-3=t^{4}-6t-3$$
> 우변을 $t$의 함수 $q(t)=t^{4}-6t-3$으로 보고 증가 여부를 확인합니다.
> $$q'(t)=4t^{3}-6\ge 4\cdot 8-6=26>0\quad(t\ge2),\qquad q(2)=16-12-3=1>0$$
> 곧 $q$는 $t\ge2$에서 증가하며 시작값이 이미 양수이므로 그 구간 전체에서 양수입니다. 따라서 $\lvert z\rvert\ge2$에는 근이 없습니다. 한편 대수학의 기본정리와 인수분해 따름정리에 의해 $p$는 중복을 허용해 정확히 네 개의 근을 가지므로, 그 네 개가 모두 $\lvert z\rvert<2$ 안에 있습니다. 반지름을 줄여 보면 한계가 드러납니다. $t=1$에서는 $1-6-3<0$이라 같은 추정이 아무 정보를 주지 않으며, 실제로 $p(-1)=-2$이고 $p(0)=3$이므로 구간 $(-1,0)$에 실근이 하나 있습니다.

> **문제 3.** (심화) 전해석함수 $f,g$가 모든 $z$에서 $\lvert f(z)\rvert\le\lvert g(z)\rvert$를 만족하고 $g\not\equiv0$이면 $\lvert c\rvert\le1$인 상수 $c$가 있어 $f=cg$임을 보이십시오.
> **답.** $h=f/g$가 유계인 전해석함수로 확장되므로 리우빌 정리에 의해 상수입니다.
> **풀이.** $g$가 항등적으로 $0$이 아니므로 그 영점 집합 $Z$는 고립점만으로 이루어집니다. $\mathbb{C}\setminus Z$에서 다음 함수가 해석적입니다.
> $$h(z)=\frac{f(z)}{g(z)},\qquad \lvert h(z)\rvert=\frac{\lvert f(z)\rvert}{\lvert g(z)\rvert}\le1$$
> 각 $z_0\in Z$는 $h$의 고립특이점인데 그 근방에서 $h$가 유계이므로, 리만의 제거가능특이점 정리에 의해 $h$는 $z_0$까지 해석적으로 확장됩니다. 확장된 $h$는 전해석함수이고 연속성에 의해 전평면에서 $\lvert h\rvert\le1$입니다. 리우빌 정리에서 $h\equiv c$이고 $\lvert c\rvert\le1$입니다. 마지막으로 $f=cg$가 $\mathbb{C}\setminus Z$에서 성립하고 양변이 연속이므로 $Z$ 위에서도 성립합니다. $Z$ 위에서는 가정 자체가 $\lvert f\rvert\le\lvert g\rvert=0$을 주므로 $f=0=cg$로 직접 확인할 수도 있습니다. 가정 $g\not\equiv0$이 없으면 결론이 무너집니다. $g\equiv0$이면 $f\equiv0$이 되어 상수 $c$가 정해지지 않습니다. $\square$

> **문제 4.** (표준) $f$가 $\overline{\mathbb{D}}$에서 연속이고 $\mathbb{D}$에서 해석적이며 $\lvert z\rvert=1$에서 $\lvert f(z)-3\rvert\le1$일 때, $f$가 $\mathbb{D}$에서 영점을 갖지 않음을 보이고 $\lvert f(0)\rvert$의 범위를 구하십시오.
> **답.** $\mathbb{D}$에서 $\lvert f\rvert\ge2>0$이므로 영점이 없고 $2\le\lvert f(0)\rvert\le4$입니다.
> **풀이.** $g(z)=f(z)-3$으로 두면 $g$도 $\overline{\mathbb{D}}$에서 연속, $\mathbb{D}$에서 해석적입니다. 경계 최대값 따름정리를 $g$에 적용합니다.
> $$\max_{\overline{\mathbb{D}}}\lvert g\rvert=\max_{\lvert z\rvert=1}\lvert g\rvert\le1$$
> 곧 닫힌 원판 전체에서 $\lvert f(z)-3\rvert\le1$입니다. 여기에 삼각부등식을 양쪽 방향으로 씁니다.
> $$3-\lvert f(z)-3\rvert\le\lvert f(z)\rvert\le 3+\lvert f(z)-3\rvert\quad\Longrightarrow\quad 2\le\lvert f(z)\rvert\le4$$
> 왼쪽 부등식에서 $\lvert f\rvert\ge2>0$이므로 $f$는 어디서도 $0$이 되지 않고, 오른쪽 부등식을 $z=0$에 적용하면 $2\le\lvert f(0)\rvert\le4$입니다. 두 끝값은 실제로 달성됩니다. $f\equiv2$와 $f\equiv4$가 모두 조건을 만족합니다. 이 문항은 최대값 정리를 $f$가 아니라 $f-3$처럼 이동한 함수에 적용하는 것이 요령임을 보여 줍니다. 평균값 성질로도 같은 결론에 이릅니다. $f(0)$이 경계값들의 평균이므로 원판 $\lvert w-3\rvert\le1$ 안에 놓이기 때문입니다.

> **문제 5.** (심화) $f:\mathbb{D}\to\mathbb{D}$가 해석적이고 $f\!\left(\tfrac12\right)=0$이면 $\lvert f(0)\rvert\le\tfrac12$임을 보이십시오.
> **답.** 원점을 $\tfrac12$로 옮기는 자기사상을 합성해 슈바르츠 보조정리를 적용합니다.
> **풀이.** $a=\tfrac12$에 대응하는 단위원판의 자기사상을 잡습니다.
> $$\psi(z)=\frac{z-\tfrac12}{1-\tfrac12 z},\qquad \psi\!\left(\tfrac12\right)=0,\qquad \psi^{-1}(w)=\frac{w+\tfrac12}{1+\tfrac12 w}$$
> $g=f\circ\psi^{-1}$로 두면 $g$는 $\mathbb{D}$를 $\mathbb{D}$로 보내는 해석함수이고 $g(0)=f\!\left(\psi^{-1}(0)\right)=f\!\left(\tfrac12\right)=0$입니다. 슈바르츠 보조정리에서 모든 $w\in\mathbb{D}$에 대해 $\lvert g(w)\rvert\le\lvert w\rvert$입니다. 이제 $f(0)=g(\psi(0))$이고 $\psi(0)=-\tfrac12$이므로 다음을 얻습니다.
> $$\lvert f(0)\rvert=\bigl\lvert g(-\tfrac12)\bigr\rvert\le\bigl\lvert-\tfrac12\bigr\rvert=\frac12$$
> 등호는 $g$가 회전일 때, 곧 $f=e^{i\theta}\psi$일 때 성립합니다. 실제로 $f=\psi$를 넣어 확인합니다.
> $$f(0)=\psi(0)=\frac{0-\tfrac12}{1-0}=-\frac12,\qquad \lvert f(0)\rvert=\frac12$$
> 곧 상계 $\tfrac12$은 개선할 수 없는 최선의 값입니다. 슈바르츠 보조정리는 원점을 고정하는 경우만 다루지만, 자기사상으로 원점을 원하는 점으로 옮기면 임의의 두 점 사이의 관계로 확장된다는 것이 이 논법의 요점입니다. $\square$

> **문제 6.** (표준) 전해석함수 $f$가 모든 $z$에서 $f(z)^{2}=z^{2}$을 만족하면 $f(z)=z$이거나 $f(z)=-z$임을 보이십시오.
> **답.** $(f-z)(f+z)\equiv0$에서 영점의 고립성과 항등정리로 둘 중 하나가 항등적으로 $0$입니다.
> **풀이.** 가정을 인수분해합니다.
> $$f(z)^{2}-z^{2}=\bigl(f(z)-z\bigr)\bigl(f(z)+z\bigr)=0\qquad(\forall z\in\mathbb{C})$$
> $F=f-z$와 $G=f+z$는 둘 다 전해석함수입니다. $F\equiv0$이면 $f(z)=z$이므로 $F\not\equiv0$인 경우만 봅니다. 그러면 $F$의 영점은 모두 고립되어 있으므로 어떤 점 $z_0$과 반지름 $r>0$을 잡아 $0<\lvert z-z_0\rvert<r$에서 $F\ne0$이 되게 할 수 있습니다. 그 뚫린 원판의 모든 점에서 곱이 $0$이므로 $G=0$이어야 하고, $G$가 연속이므로 원판 전체에서 $G\equiv0$입니다.
> $$0<\lvert z-z_0\rvert<r\ \Rightarrow\ F(z)\ne0\ \Rightarrow\ G(z)=0$$
> 영점 집합이 원판을 통째로 포함하면 집적점을 가지므로 항등정리에 의해 $G\equiv0$이 전평면에서 성립하고 $f(z)=-z$입니다. 곧 두 경우뿐입니다. 실함수에서는 이런 결론이 나오지 않습니다. $f(x)=\lvert x\rvert$는 $f(x)^{2}=x^{2}$을 만족하지만 $x$도 $-x$도 아니며, 해석성이 없어 조각별로 부호를 바꿀 수 있기 때문입니다. $\square$

> **문제 7.** (심화) $u$가 평면 전체에서 조화이고 위로 유계이면 $u$가 상수임을 보이십시오.
> **답.** $e^{u+iv}$가 유계인 전해석함수가 되므로 리우빌 정리를 씁니다.
> **풀이.** 평면은 단순연결이므로 $u$의 조화켤레 $v$가 존재하고 $f=u+iv$가 전해석함수입니다. 여기서 $g=e^{f}$를 만듭니다. $g$도 전해석함수이고 절대값은 실수부만으로 정해집니다.
> $$\lvert g(z)\rvert=e^{\operatorname{Re}f(z)}=e^{u(z)}\le e^{M}$$
> 가정에서 $u\le M$이므로 $g$는 유계입니다. 리우빌 정리에서 $g$는 상수이고, 지수함수는 영점을 갖지 않으므로 $g\ne0$입니다. 상수함수를 미분해 다음을 얻습니다.
> $$g'(z)=f'(z)e^{f(z)}\equiv0,\qquad e^{f(z)}\ne0\quad\Longrightarrow\quad f'\equiv0$$
> 따라서 $f$가 상수이고 그 실수부인 $u$도 상수입니다. 조건을 아래로 유계로 바꾸어도 $-u$에 같은 논법을 적용하면 됩니다. 실해석의 감각과는 어긋나는 결론입니다. 두 변수 실함수 가운데 유계이면서 상수가 아닌 매끄러운 함수는 얼마든지 있지만, 조화라는 조건이 붙는 순간 복소해석의 경직성이 그대로 옮겨 옵니다. $\square$

## 11강. 등각사상과 뫼비우스 변환

> **문제 8.** (표준) 단위원 $\lvert z\rvert=1$을 자기 자신으로 보내고 $T\!\left(\tfrac12\right)=0$인 뫼비우스 변환을 모두 구하십시오.
> **답.** $T(z)=e^{i\theta}\dfrac{z-\tfrac12}{1-\tfrac12 z}$($\theta$는 실수)입니다.
> **풀이.** $T$는 $\hat{\mathbb{C}}$의 전단사이고 단위원을 단위원으로 보내므로, 원의 여집합의 두 연결성분인 $\mathbb{D}$와 그 외부를 각각 통째로 보냅니다. $\tfrac12\in\mathbb{D}$의 상이 $0\in\mathbb{D}$이므로 $T$는 $\mathbb{D}$를 $\mathbb{D}$로 보내며, 곧 $T\in\operatorname{Aut}(\mathbb{D})$입니다. 단위원판의 등각 자기사상은 모두 다음 꼴입니다.
> $$\psi_{a,\theta}(z)=e^{i\theta}\frac{z-a}{1-\bar a z},\qquad a\in\mathbb{D},\ \theta\in\mathbb{R}$$
> 이 사상이 $a$를 $0$으로 보내므로 $a=\tfrac12$이고, $a$가 실수이므로 $\bar a=\tfrac12$입니다. 이 꼴이 실제로 단위원을 보존하는지 확인합니다. $\lvert z\rvert=1$이면 $z\bar z=1$이므로 분모를 다음처럼 다시 씁니다.
> $$\lvert 1-\bar a z\rvert=\lvert z\rvert\,\lvert \bar z-\bar a\rvert=\lvert\overline{z-a}\rvert=\lvert z-a\rvert$$
> 곧 분자와 분모의 절대값이 같아 $\lvert T(z)\rvert=1$입니다. 회전 인자 $e^{i\theta}$는 단위원을 그대로 두므로 답은 한 개의 실매개변수 $\theta$를 가진 족입니다. 조건을 하나 더 붙이면 유일해집니다. $\theta=0$일 때의 도함수를 계산해 봅니다.
> $$\psi'(z)=\frac{1-\lvert a\rvert^{2}}{(1-\bar a z)^{2}},\qquad \psi'\!\left(\tfrac12\right)=\frac{3/4}{(3/4)^{2}}=\frac43>0$$
> 곧 $T'\!\left(\tfrac12\right)>0$을 요구하면 $\theta=0$인 하나만 남습니다.

> **문제 9.** (표준) $T(z)=\dfrac{z-i}{z+i}$가 단위원 $\lvert z\rvert=1$과 단위원판 $\mathbb{D}$를 각각 어디로 보내는지 구하십시오.
> **답.** 단위원은 허축으로 가고 $\mathbb{D}$는 좌반평면 $\{\operatorname{Re}w<0\}$으로 갑니다.
> **풀이.** 극점 $z=-i$가 단위원 위에 있으므로 상은 무한원점을 포함하고 따라서 직선입니다. 직선은 두 점으로 정해지므로 원 위의 편한 점을 넣습니다.
> $$T(1)=\frac{1-i}{1+i}=\frac{(1-i)^{2}}{2}=-i,\qquad T(-1)=\frac{-1-i}{-1+i}=\frac{(-1-i)^{2}}{2}=i,\qquad T(i)=0$$
> 여기서 $(1-i)^{2}=-2i$이고 $(-1-i)^{2}=2i$이며 분모의 유리화에 쓴 $(1+i)(1-i)=2$와 $(-1+i)(-1-i)=2$를 이용했습니다. 세 상 $-i$, $i$, $0$이 모두 허축 위에 있으므로 단위원의 상은 허축입니다. 다음으로 여집합의 어느 성분이 어디로 가는지는 시험점 하나로 결정됩니다.
> $$T(0)=\frac{0-i}{0+i}=-1,\qquad \operatorname{Re}(-1)=-1<0$$
> 곧 $\mathbb{D}$의 상은 좌반평면입니다. 자연히 $\mathbb{D}$의 외부는 우반평면으로 갑니다. 케일리 변환 $\varphi(z)=\dfrac{z-i}{z+i}$와 식이 같지만 정의역이 다르다는 점에 주의해야 합니다. 같은 식이 상반평면 위에서는 상반평면을 단위원판으로 보내고, 단위원판 위에서는 단위원판을 좌반평면으로 보냅니다.

> **문제 10.** (표준) 띠 $S=\left\{z:\lvert\operatorname{Im}z\rvert<\dfrac{\pi}{2}\right\}$를 단위원판으로 보내는 등각사상을 구하십시오.
> **답.** $w=\dfrac{e^{z}-1}{e^{z}+1}=\tanh\dfrac z2$입니다.
> **풀이.** 두 단계로 조립합니다. 먼저 $\zeta=e^{z}$을 봅니다. $z=x+iy$이면 절대값과 편각이 각각 다음을 훑습니다.
> $$\lvert\zeta\rvert=e^{x}\in(0,\infty),\qquad \arg\zeta=y\in\left(-\frac\pi2,\frac\pi2\right)$$
> 곧 상은 우반평면 $\{\operatorname{Re}\zeta>0\}$입니다. 세로 폭이 $\pi$이라 $2\pi$ 이하이므로 단사입니다. 다음으로 우반평면을 단위원판으로 보내는 뫼비우스 변환을 씁니다.
> $$w=\frac{\zeta-1}{\zeta+1}$$
> 이 사상은 $\zeta=1$을 $0$으로 보내고, 허축 위의 점 $\zeta=iy$에서는 $\lvert iy-1\rvert=\lvert iy+1\rvert=\sqrt{y^{2}+1}$이라 상의 절대값이 $1$이므로 허축을 단위원으로 보냅니다. 시험점 $\zeta=1$의 상이 원판 안이므로 우반평면 전체가 $\mathbb{D}$로 갑니다. 두 사상을 합성하고 분자와 분모를 $e^{z/2}$로 나눕니다.
> $$w=\frac{e^{z}-1}{e^{z}+1}=\frac{e^{z/2}-e^{-z/2}}{e^{z/2}+e^{-z/2}}=\tanh\frac z2$$ 각 단계에서 도함수가 $0$이 되지 않으므로 합성도 등각입니다. 띠의 폭을 $\pi$보다 넓게 잡으면 $e^{z}$이 단사가 아니게 되어 이 조립이 무너집니다.

> **문제 11.** (심화) 반원판 $\Omega=\{z:\lvert z\rvert<1,\ \operatorname{Im}z>0\}$을 단위원판으로 보내는 등각사상을 조립하십시오.
> **답.** $\zeta=\dfrac{1+z}{1-z}$, $\eta=\zeta^{2}$, $w=\dfrac{\eta-i}{\eta+i}$를 이어 붙인 $w=\dfrac{\left(\frac{1+z}{1-z}\right)^{2}-i}{\left(\frac{1+z}{1-z}\right)^{2}+i}$입니다.
> **풀이.** 세 단계로 나눕니다. 첫째, $\zeta=\dfrac{1+z}{1-z}$은 두 가지 성질을 동시에 가집니다. 경계 $z=e^{i\phi}$의 상을 계산하면 순허수입니다.
> $$\frac{1+e^{i\phi}}{1-e^{i\phi}}=\frac{e^{-i\phi/2}+e^{i\phi/2}}{e^{-i\phi/2}-e^{i\phi/2}}=\frac{2\cos(\phi/2)}{-2i\sin(\phi/2)}=i\cot\frac\phi2$$
> 시험점 $\zeta(0)=1$이 우반평면에 있으므로 $\mathbb{D}$는 우반평면으로 갑니다. 한편 계수가 모두 실수이고 $ad-bc=1\cdot1-1\cdot(-1)=2>0$이므로 상반평면은 상반평면으로 갑니다. 두 성질을 겹치면 $\Omega=\mathbb{D}\cap\mathbb{H}$의 상은 우반평면과 상반평면의 교집합, 곧 제1사분면입니다. 둘째, $\eta=\zeta^{2}$이 편각을 두 배로 늘려 제1사분면을 상반평면으로 전단사로 보냅니다. 셋째, 케일리 변환 $w=\dfrac{\eta-i}{\eta+i}$가 상반평면을 단위원판으로 보냅니다. 시험점으로 확인합니다. $z=\dfrac i2$이면 다음과 같습니다.
> $$\zeta=\frac{1+\tfrac i2}{1-\tfrac i2}=\frac{\left(1+\tfrac i2\right)^{2}}{\tfrac54}=0.6+0.8i,\qquad \eta=\zeta^{2}=-0.28+0.96i$$
> $\zeta$는 제1사분면, $\eta$는 상반평면에 있습니다. 마지막 단계의 절대값을 계산합니다.
> $$\lvert w\rvert=\frac{\lvert\eta-i\rvert}{\lvert\eta+i\rvert}=\frac{\lvert-0.28-0.04i\rvert}{\lvert-0.28+1.96i\rvert}\approx\frac{0.283}{1.980}\approx0.143<1$$
> 곧 상이 원판 안에 있습니다. 각 단계의 도함수가 정의역 안에서 $0$이 되지 않으므로 합성이 등각입니다. $\zeta^{2}$의 도함수가 $0$이 되는 점은 $\zeta=0$인데 제1사분면에는 없습니다. $\square$

> **문제 12.** (심화) 상반평면의 자기사상 가운데 점 $i$를 고정하는 것 전체를 구하십시오.
> **답.** $T(z)=\dfrac{z\cos\alpha+\sin\alpha}{-z\sin\alpha+\cos\alpha}$($\alpha$는 실수) 전체입니다.
> **풀이.** 케일리 변환 $\varphi(z)=\dfrac{z-i}{z+i}$는 $\mathbb{H}$를 $\mathbb{D}$로 보내고 $\varphi(i)=0$입니다. 따라서 켤레를 취해 문제를 원판으로 옮깁니다.
> $$T\in\operatorname{Aut}(\mathbb{H}),\ T(i)=i\quad\Longleftrightarrow\quad \varphi\circ T\circ\varphi^{-1}\in\operatorname{Aut}(\mathbb{D}),\ (\varphi\circ T\circ\varphi^{-1})(0)=0$$
> 원점을 고정하는 단위원판의 자기사상은 회전 $w\mapsto e^{i\theta}w$뿐이므로, 찾는 사상은 $T=\varphi^{-1}\circ\left(e^{i\theta}\,\cdot\right)\circ\varphi$의 꼴 전부입니다. 이를 실계수로 정리한 결과가 위 답이며 $\theta=-2\alpha$에 대응합니다. 답이 맞는지 직접 확인합니다.
> $$T(i)=\frac{i\cos\alpha+\sin\alpha}{-i\sin\alpha+\cos\alpha}=\frac{i(\cos\alpha-i\sin\alpha)}{\cos\alpha-i\sin\alpha}=\frac{i\,e^{-i\alpha}}{e^{-i\alpha}}=i$$
> 또한 계수가 실수이고 $ad-bc=\cos^{2}\alpha+\sin^{2}\alpha=1>0$이므로 $T$는 상반평면을 자기 자신으로 보냅니다. 이 부분군은 회전군과 동형이며 원 하나만큼의 자유도를 가집니다. 리만 사상 정리에서 정규화 조건 $f(z_0)=0$과 $f'(z_0)>0$이 필요한 이유가 정확히 이 자유도를 없애기 위함입니다. $\square$

> **문제 13.** (심화) 상반평면에서 조화이고 실축 위의 경계값이 $-1<x<1$에서 $1$, 나머지에서 $0$인 함수를 구하십시오.
> **답.** $u(z)=\dfrac1\pi\Bigl(\arg(z-1)-\arg(z+1)\Bigr)$입니다.
> **풀이.** 상반평면의 디리클레 문제에서 계단 모양 경계값은 편각함수의 차로 만듭니다. 실수 $a$에 대해 $z\mapsto\log(z-a)$가 상반평면에서 해석적이므로 그 허수부가 조화입니다.
> $$\log(z-a)=\ln\lvert z-a\rvert+i\arg(z-a),\qquad u(z)=\frac1\pi\operatorname{Im}\log\frac{z-1}{z+1}$$
> 조화함수의 차도 조화이므로 위 $u$는 상반평면에서 조화입니다. 편각의 범위를 $0\le\arg\le\pi$로 두고 경계값을 세 구간으로 나누어 확인합니다.
> $$x>1:\ \frac1\pi(0-0)=0,\qquad -1<x<1:\ \frac1\pi(\pi-0)=1,\qquad x<-1:\ \frac1\pi(\pi-\pi)=0$$
> 세 값이 모두 요구와 맞습니다. 대칭점에서 검산합니다.
> $$\arg(i-1)=\frac{3\pi}{4},\qquad \arg(i+1)=\frac{\pi}{4},\qquad u(i)=\frac1\pi\left(\frac{3\pi}{4}-\frac{\pi}{4}\right)=\frac12$$ 경계에서 값 $1$을 갖는 구간이 전체 실축의 어느 쪽으로도 치우치지 않은 상황이므로 대칭축 위에서 $\tfrac12$이 나오는 것이 자연스럽습니다. 값이 항상 $0$과 $1$ 사이에 있다는 사실은 조화함수의 최대·최소가 경계에서 달성된다는 성질과 맞물립니다. 다른 영역의 같은 문제는 그 영역을 상반평면으로 보내는 등각사상 $\varphi$를 찾아 $u\circ\varphi$로 옮기면 됩니다. $\square$

> **문제 14.** (심화) 해석함수 $f=u+iv$를 실이변수 사상으로 볼 때 그 야코비 행렬식이 $\lvert f'\rvert^{2}$임을 보이고, 이것이 등각사상의 면적 배율과 어떻게 이어지는지 밝히십시오.
> **답.** 코시-리만 방정식을 대입하면 행렬식이 $u_x^{2}+v_x^{2}=\lvert f'\rvert^{2}$이 되며, 이는 국소 면적이 $\lvert f'\rvert^{2}$배가 된다는 뜻입니다.
> **풀이.** $(x,y)\mapsto(u,v)$로 보면 야코비 행렬식은 다음과 같습니다.
> $$J_f=\det\begin{pmatrix}u_x&u_y\\ v_x&v_y\end{pmatrix}=u_xv_y-u_yv_x$$
> 코시-리만 방정식 $u_x=v_y$, $u_y=-v_x$를 대입하고 도함수의 절대값과 비교합니다.
> $$J_f=u_x\cdot u_x-(-v_x)\cdot v_x=u_x^{2}+v_x^{2},\qquad f'=u_x+iv_x\ \Longrightarrow\ \lvert f'\rvert^{2}=u_x^{2}+v_x^{2}$$
> 두 값이 같습니다. 기하적 해석은 두 갈래로 갈립니다. 길이 쪽은 이미 등각성 논의에서 확인한 대로 접벡터가 $\lvert f'(z_0)\rvert$배로 늘어나므로, 면적은 두 방향에서 동시에 늘어나 $\lvert f'(z_0)\rvert^{2}$배가 됩니다. 부호 쪽은 $J_f\ge0$이라는 사실이 말해 줍니다. 해석함수는 방향을 뒤집지 않으며, 이것이 켤레 $\bar z$처럼 각의 크기만 보존하고 방향을 뒤집는 사상과 구분되는 지점입니다. 실제로 $z\mapsto\bar z$의 야코비 행렬식은 $-1$입니다. $J_f=0$인 점은 $f'(z_0)=0$인 점과 같고, 그 점에서 등각성이 깨지며 각이 배수화됩니다. 응용으로 상의 면적을 적분으로 계산할 수 있습니다. $f(z)=z^{2}$에서 $\lvert z\rvert<1$의 상 면적을 겹침까지 세어 구합니다.
> $$\iint_{\lvert z\rvert<1}\lvert f'(z)\rvert^{2}\,dA=\iint_{\lvert z\rvert<1}4\lvert z\rvert^{2}dA=4\int_0^{2\pi}\!\!\int_0^{1}r^{2}\cdot r\,dr\,d\theta=4\cdot2\pi\cdot\frac14=2\pi$$
> 상 자체는 단위원판 $\lvert w\rvert<1$이고 면적이 $\pi$이므로, 값 $2\pi$는 $z^{2}$이 그 원판을 두 겹으로 덮는다는 사실과 일치합니다. $\square$

## 스스로 점검

1. 코시 부등식에서 성장 조건을 다항식 차수로 번역하는 절차를 재현하는가?
2. 리우빌 정리를 쓸 때 $f$가 아니라 $1/g$나 $e^{f}$ 같은 보조함수를 만들 줄 아는가?
3. 근의 위치를 삼각부등식만으로 가두는 추정을 세우고 그 한계를 아는가?
4. 최대 절대값 원리를 이동한 함수 $f-c$에 적용해 하계를 얻는가?
5. 슈바르츠 보조정리를 자기사상으로 옮겨 원점이 아닌 점에 적용하는가?
6. 항등정리와 영점의 고립성으로 함수방정식의 해를 분류하는가?
7. 뫼비우스 변환이 일반원의 한쪽을 통째로 보낸다는 성질을 시험점으로 확정하는가?
8. 지수사상, 거듭제곱사상, 케일리 변환을 이어 붙여 원하는 영역을 원판까지 옮기는가?
9. 등각사상이 조화성을 보존한다는 사실로 디리클레 문제를 옮겨 푸는가?

정답 요지: (1) 원 위의 상계를 $R$의 식으로 쓰고 $\lvert f^{(n)}(0)\rvert\le n!M(R)/R^{n}$에서 $R\to\infty$를 보내 높은 차수 계수를 $0$으로 만듭니다. (2) 유계성을 직접 얻기 어려우면 $\lvert e^{f}\rvert=e^{\operatorname{Re}f}$나 $\lvert 1/g\rvert\le1/\delta$처럼 절대값이 통제되는 함수를 만듭니다. (3) $\lvert p\rvert\ge\lvert z\rvert^{n}-(\text{나머지})$가 양수가 되는 반지름을 찾으며, 반지름이 작으면 추정이 무의미해집니다. (4) $f-c$에 경계 최대값을 적용하면 $\lvert f-c\rvert\le M$이 되고 역삼각부등식이 $\lvert f\rvert\ge\lvert c\rvert-M$을 줍니다. (5) $a$를 $0$으로 보내는 자기사상 $\psi_a$를 합성해 $f\circ\psi_a^{-1}$이 원점을 고정하게 만듭니다. (6) 곱이 항등적으로 $0$이면 한 인수의 영점 집합이 열린 집합을 포함하므로 항등정리로 그 인수가 항등적으로 $0$입니다. (7) 경계 일반원의 상을 세 점으로 정한 뒤 내부의 시험점 하나를 넣어 어느 쪽인지 확정합니다. (8) $e^{z}$로 띠를 반평면으로, $z^{n}$으로 부채꼴을 반평면으로 옮기고 마지막에 케일리 변환으로 원판에 넣습니다. (9) 표준 영역의 해 $U$를 미리 구해 두고 $u=U\circ\varphi$로 되돌리며, 경계는 경계로 가므로 경계조건도 함께 옮겨집니다.

## 관련 강의

- [10. 리우빌 정리와 대수학의 기본정리](../10. 리우빌 정리와 대수학의 기본정리/index.md)
- [11. 등각사상과 뫼비우스 변환](../11. 등각사상과 뫼비우스 변환/index.md)
- [05. 해석함수의 대역 이론](../index.md)
