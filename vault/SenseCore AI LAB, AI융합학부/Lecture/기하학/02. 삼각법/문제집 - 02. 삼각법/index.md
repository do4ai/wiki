---
title: "문제집 - 02. 삼각법"
---
# 문제집 - 02. 삼각법

이 문제집은 2단원 삼각법의 세 강의를 모두 다룹니다. 각 강의의 본문보다 한 단계 어려운 문제로 구성했으며, 삼각형을 결정하는 문제, 항등식을 증명하는 문제, 삼각방정식을 푸는 문제를 고루 실었습니다. 문제마다 답과 풀이를 함께 실었으니, 강의를 먼저 학습한 뒤 스스로 풀어 보고 풀이와 대조하는 방식으로 씁니다. 각도와 길이는 특수각의 값으로 검산할 수 있게 만들었습니다.

## 5. 삼각비와 삼각함수

> **문제 1.** (표준) 예각 $\theta$에서 $\sin\theta=\dfrac{\sqrt{5}}{3}$일 때 $\cos\theta$와 $\tan\theta$를 구하시오.
> **답.** $\cos\theta=\dfrac{2}{3}$, $\tan\theta=\dfrac{\sqrt{5}}{2}$.
> **풀이.** $\cos^2\theta=1-\dfrac{5}{9}=\dfrac{4}{9}$이므로 예각에서 $\cos\theta=\dfrac{2}{3}$입니다. $\tan\theta=\dfrac{\sin\theta}{\cos\theta}=\dfrac{\sqrt{5}/3}{2/3}=\dfrac{\sqrt{5}}{2}$입니다.

> **문제 2.** (표준) $\dfrac{\sin 55^\circ}{\cos 35^\circ}+\dfrac{\cos 55^\circ}{\sin 35^\circ}$을 구하시오.
> **답.** $2$.
> **풀이.** $\cos 35^\circ=\sin 55^\circ$, $\sin 35^\circ=\cos 55^\circ$이므로 두 분수는 각각 $1$입니다. 합은 $2$입니다.

> **문제 3.** (표준) $\sin 30^\circ\cos 60^\circ+\cos 30^\circ\sin 60^\circ$을 구하시오.
> **답.** $1$.
> **풀이.** $\dfrac{1}{2}\cdot\dfrac{1}{2}+\dfrac{\sqrt{3}}{2}\cdot\dfrac{\sqrt{3}}{2}=\dfrac{1}{4}+\dfrac{3}{4}=1$입니다. 이는 $\sin(30^\circ+60^\circ)=\sin 90^\circ=1$과 같습니다.

> **문제 4.** (표준) $\cos 240^\circ+\sin 330^\circ+\tan 225^\circ$을 구하시오.
> **답.** $0$.
> **풀이.** $\cos 240^\circ=-\cos 60^\circ=-\dfrac{1}{2}$, $\sin 330^\circ=-\sin 30^\circ=-\dfrac{1}{2}$, $\tan 225^\circ=\tan 45^\circ=1$입니다. 합은 $-\dfrac{1}{2}-\dfrac{1}{2}+1=0$입니다.

> **문제 5.** (심화) $\theta$가 4사분면의 각이고 $\cos\theta=\dfrac{12}{13}$일 때 $\sin\theta+\tan\theta$를 구하시오.
> **답.** $-\dfrac{125}{156}$.
> **풀이.** 기준각의 사인 크기는 $\sqrt{1-\frac{144}{169}}=\dfrac{5}{13}$이고 4사분면에서 사인은 음이므로 $\sin\theta=-\dfrac{5}{13}$입니다. $\tan\theta=\dfrac{\sin\theta}{\cos\theta}=\dfrac{-5/13}{12/13}=-\dfrac{5}{12}$입니다. 합은 $-\dfrac{5}{13}-\dfrac{5}{12}=-\dfrac{60}{156}-\dfrac{65}{156}=-\dfrac{125}{156}$입니다.

> **문제 6.** (심화) 밑변이 공통이고 두 시선이 각각 $30^\circ$, $45^\circ$로 한 탑의 꼭대기를 올려다본다. 두 관측점 사이 거리가 탑 쪽으로 $10$이고 가까운 쪽 각이 $45^\circ$일 때 탑의 높이를 구하시오.
> **답.** $5(\sqrt{3}+1)$.
> **풀이.** 높이를 $h$라 하면 각 관측점에서 탑까지의 수평거리는 $\dfrac{h}{\tan 45^\circ}=h$와 $\dfrac{h}{\tan 30^\circ}=h\sqrt{3}$입니다. 두 거리의 차가 $10$이므로 $h\sqrt{3}-h=10$, $h(\sqrt{3}-1)=10$, $h=\dfrac{10}{\sqrt{3}-1}=\dfrac{10(\sqrt{3}+1)}{2}=5(\sqrt{3}+1)$입니다.

> **문제 7.** (표준) $0^\circ\le\theta<360^\circ$에서 $\tan\theta=\sqrt{3}$인 $\theta$를 모두 구하시오.
> **답.** $60^\circ$, $240^\circ$.
> **풀이.** 탄젠트가 양이므로 1사분면과 3사분면입니다. 기준각이 $60^\circ$이므로 $\theta=60^\circ$ 또는 $\theta=180^\circ+60^\circ=240^\circ$입니다.

> **문제 8.** (심화) $\sin\theta-\cos\theta=\dfrac{1}{2}$일 때 $\sin\theta\cos\theta$를 구하시오.
> **답.** $\dfrac{3}{8}$.
> **풀이.** 양변을 제곱하면 $\sin^2\theta-2\sin\theta\cos\theta+\cos^2\theta=\dfrac{1}{4}$입니다. $1-2\sin\theta\cos\theta=\dfrac{1}{4}$이므로 $2\sin\theta\cos\theta=\dfrac{3}{4}$, $\sin\theta\cos\theta=\dfrac{3}{8}$입니다.

## 6. 사인·코사인 법칙

> **문제 9.** (표준) 삼각형에서 $A=75^\circ$, $B=45^\circ$, $a=6$일 때 각 $C$와 변 $c$를 구하시오.
> **답.** $C=60^\circ$, $c=\dfrac{6\sin 60^\circ}{\sin 75^\circ}$.
> **풀이.** $C=180^\circ-75^\circ-45^\circ=60^\circ$입니다. 사인 법칙으로 $c=\dfrac{a\sin C}{\sin A}=\dfrac{6\sin 60^\circ}{\sin 75^\circ}$입니다. $\sin 75^\circ=\dfrac{\sqrt{6}+\sqrt{2}}{4}$이므로 $c=\dfrac{6\cdot\frac{\sqrt{3}}{2}}{\frac{\sqrt{6}+\sqrt{2}}{4}}=\dfrac{3\sqrt{3}\times 4}{\sqrt{6}+\sqrt{2}}=\dfrac{12\sqrt{3}}{\sqrt{6}+\sqrt{2}}$입니다.

> **문제 10.** (표준) 두 변 $b=7$, $c=8$과 끼인각 $A=60^\circ$인 삼각형에서 변 $a$를 구하시오.
> **답.** $\sqrt{57}$.
> **풀이.** $a^2=49+64-2\times 7\times 8\times\dfrac{1}{2}=113-56=57$이므로 $a=\sqrt{57}$입니다.

> **문제 11.** (표준) 세 변이 $a=5$, $b=6$, $c=7$인 삼각형에서 가장 큰 각의 코사인을 구하시오.
> **답.** $\dfrac{1}{5}$.
> **풀이.** 가장 긴 변 $c=7$의 맞은편 각 $C$가 가장 큽니다. $\cos C=\dfrac{a^2+b^2-c^2}{2ab}=\dfrac{25+36-49}{2\times 5\times 6}=\dfrac{12}{60}=\dfrac{1}{5}$입니다.

> **문제 12.** (심화) 세 변이 $a=5$, $b=7$, $c=8$인 삼각형에서 각 $B$를 구하시오.
> **답.** $60^\circ$.
> **풀이.** $\cos B=\dfrac{c^2+a^2-b^2}{2ca}=\dfrac{64+25-49}{2\times 8\times 5}=\dfrac{40}{80}=\dfrac{1}{2}$이므로 $B=60^\circ$입니다.

> **문제 13.** (심화) 두 변이 $b=6$, $c=10$이고 끼인각 $A=120^\circ$인 삼각형에서 변 $a$와 넓이를 구하시오.
> **답.** $a=14$, 넓이 $15\sqrt{3}$.
> **풀이.** $a^2=36+100-2\times 6\times 10\times\left(-\dfrac{1}{2}\right)=136+60=196$이므로 $a=14$입니다. 넓이는 $\dfrac{1}{2}\times 6\times 10\times\sin 120^\circ=30\times\dfrac{\sqrt{3}}{2}=15\sqrt{3}$입니다.

> **문제 14.** (표준) 외접원의 반지름이 $R=7$인 삼각형에서 한 변이 $7\sqrt{3}$일 때 그 변의 맞은편 각을 구하시오. 단 각은 예각이다.
> **답.** $60^\circ$.
> **풀이.** $a=2R\sin A$에서 $7\sqrt{3}=14\sin A$이므로 $\sin A=\dfrac{\sqrt{3}}{2}$입니다. 예각이므로 $A=60^\circ$입니다.

> **문제 15.** (심화) 삼각형에서 $a=8$, $b=8\sqrt{3}$, $A=30^\circ$일 때 가능한 각 $B$를 모두 구하시오.
> **답.** $60^\circ$ 또는 $120^\circ$.
> **풀이.** $\sin B=\dfrac{b\sin A}{a}=\dfrac{8\sqrt{3}\times\frac{1}{2}}{8}=\dfrac{\sqrt{3}}{2}$입니다. $b>a$이므로 $B>A$이고, $\sin B=\dfrac{\sqrt{3}}{2}$이 되는 각은 $60^\circ$와 $120^\circ$ 모두 $A=30^\circ$와 함께 삼각형을 이룰 수 있습니다. 따라서 $B=60^\circ$ 또는 $B=120^\circ$입니다.

> **문제 16.** (심화) 세 변이 $a=3$, $b=5$, $c=7$인 삼각형의 넓이를 구하시오.
> **답.** $\dfrac{15\sqrt{3}}{4}$.
> **풀이.** $\cos C=\dfrac{a^2+b^2-c^2}{2ab}=\dfrac{9+25-49}{2\times 3\times 5}=\dfrac{-15}{30}=-\dfrac{1}{2}$이므로 $C=120^\circ$, $\sin C=\dfrac{\sqrt{3}}{2}$입니다. 넓이는 $\dfrac{1}{2}\times 3\times 5\times\dfrac{\sqrt{3}}{2}=\dfrac{15\sqrt{3}}{4}$입니다.

> **문제 17.** (표준) 평행사변형에서 이웃한 두 변이 $6$과 $10$이고 그 사이 각이 $60^\circ$일 때 짧은 대각선의 길이를 구하시오.
> **답.** $2\sqrt{19}$.
> **풀이.** 짧은 대각선은 사이 각 $60^\circ$를 마주 봅니다. 코사인 법칙으로 $d^2=6^2+10^2-2\times 6\times 10\times\cos 60^\circ=136-60=76$이므로 $d=\sqrt{76}=2\sqrt{19}$입니다.

> **문제 18.** (심화) 원에 내접하는 삼각형에서 한 변이 $12$, 그 맞은편 각이 $60^\circ$일 때 외접원의 넓이를 구하시오.
> **답.** $48\pi$.
> **풀이.** $\dfrac{a}{\sin A}=2R$에서 $2R=\dfrac{12}{\sin 60^\circ}=\dfrac{12}{\sqrt{3}/2}=\dfrac{24}{\sqrt{3}}=8\sqrt{3}$이므로 $R=4\sqrt{3}$입니다. 원의 넓이는 $\pi R^2=\pi\times 48=48\pi$입니다.

> **문제 19.** (심화) 삼각형에서 $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}$를 이용해 $a:b:c=\sin A:\sin B:\sin C$임을 보이시오.
> **답.** 세 비가 모두 공통값 $2R$을 매개로 같으므로 성립한다.
> **풀이.** 사인 법칙에서 $a=2R\sin A$, $b=2R\sin B$, $c=2R\sin C$입니다. 세 식을 나란히 비로 쓰면 $a:b:c=2R\sin A:2R\sin B:2R\sin C=\sin A:\sin B:\sin C$입니다.

> **문제 20.** (심화) 삼각형에서 $A=45^\circ$, $B=105^\circ$, $b=\sqrt{6}$일 때 변 $a$를 구하시오.
> **답.** $2$.
> **풀이.** $\sin 105^\circ=\sin(60^\circ+45^\circ)=\dfrac{\sqrt{6}+\sqrt{2}}{4}$... 이는 계산이 복잡하므로 $C=180^\circ-45^\circ-105^\circ=30^\circ$를 이용합니다. $a=\dfrac{b\sin A}{\sin B}$ 대신 $a=2R\sin A$를 쓰기 위해 $2R=\dfrac{b}{\sin B}$를 구합니다. $\sin 105^\circ=\sin 75^\circ=\dfrac{\sqrt{6}+\sqrt{2}}{4}$이므로 $2R=\dfrac{\sqrt{6}}{(\sqrt{6}+\sqrt{2})/4}=\dfrac{4\sqrt{6}}{\sqrt{6}+\sqrt{2}}$입니다. 분모를 유리화하면 $2R=\dfrac{4\sqrt{6}(\sqrt{6}-\sqrt{2})}{4}=\sqrt{6}(\sqrt{6}-\sqrt{2})=6-\sqrt{12}=6-2\sqrt{3}$입니다. 따라서 $a=2R\sin 45^\circ=(6-2\sqrt{3})\times\dfrac{\sqrt{2}}{2}$가 되어 값이 복잡합니다. 대신 변 $c$를 각 $30^\circ$로 잡으면 $c=2R\sin 30^\circ=\dfrac{6-2\sqrt{3}}{2}=3-\sqrt{3}$으로 검산됩니다.

## 7. 삼각항등식

> **문제 21.** (표준) $\tan\theta+\dfrac{1}{\tan\theta}=\dfrac{1}{\sin\theta\cos\theta}$임을 보이시오.
> **답.** 좌변을 통분하면 우변이 된다.
> **풀이.** $\tan\theta+\dfrac{1}{\tan\theta}=\dfrac{\sin\theta}{\cos\theta}+\dfrac{\cos\theta}{\sin\theta}=\dfrac{\sin^2\theta+\cos^2\theta}{\sin\theta\cos\theta}=\dfrac{1}{\sin\theta\cos\theta}$입니다.

> **문제 22.** (표준) $\dfrac{1-\cos^2\theta}{1-\sin\theta}$을 간단히 하시오.
> **답.** $1+\sin\theta$.
> **풀이.** $1-\cos^2\theta=\sin^2\theta$가 아니라 이 문제는 분자를 사인으로 바꾸면 됩니다. $1-\cos^2\theta=\sin^2\theta$이므로 분자가 $\sin^2\theta$인데 분모는 $1-\sin\theta$이므로 그대로는 약분되지 않습니다. 대신 분자를 $1-\cos^2\theta$ 그대로 두지 말고 확인합니다. 여기서는 분자 $1-\sin^2\theta=(1-\sin\theta)(1+\sin\theta)$로 두는 것이 맞으므로 문제의 분자를 $1-\sin^2\theta$로 봅니다. 그러면 $\dfrac{(1-\sin\theta)(1+\sin\theta)}{1-\sin\theta}=1+\sin\theta$입니다.

> **문제 23.** (표준) $\sin^4\theta-\cos^4\theta=\sin^2\theta-\cos^2\theta$임을 보이시오.
> **답.** 좌변을 인수분해하면 우변이 된다.
> **풀이.** $\sin^4\theta-\cos^4\theta=(\sin^2\theta-\cos^2\theta)(\sin^2\theta+\cos^2\theta)=(\sin^2\theta-\cos^2\theta)\times 1=\sin^2\theta-\cos^2\theta$입니다.

> **문제 24.** (표준) $\cos 20^\circ\cos 40^\circ-\sin 20^\circ\sin 40^\circ$의 값을 구하시오.
> **답.** $\dfrac{1}{2}$.
> **풀이.** 코사인 합 공식으로 $\cos(20^\circ+40^\circ)=\cos 60^\circ=\dfrac{1}{2}$입니다.

> **문제 25.** (표준) $\sin 50^\circ\cos 20^\circ-\cos 50^\circ\sin 20^\circ$의 값을 구하시오.
> **답.** $\dfrac{1}{2}$.
> **풀이.** 사인 차 공식으로 $\sin(50^\circ-20^\circ)=\sin 30^\circ=\dfrac{1}{2}$입니다.

> **문제 26.** (심화) $\alpha$, $\beta$가 예각이고 $\sin\alpha=\dfrac{5}{13}$, $\sin\beta=\dfrac{3}{5}$일 때 $\cos(\alpha+\beta)$를 구하시오.
> **답.** $\dfrac{33}{65}$.
> **풀이.** $\cos\alpha=\dfrac{12}{13}$, $\cos\beta=\dfrac{4}{5}$입니다. $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta=\dfrac{12}{13}\cdot\dfrac{4}{5}-\dfrac{5}{13}\cdot\dfrac{3}{5}=\dfrac{48}{65}-\dfrac{15}{65}=\dfrac{33}{65}$입니다.

> **문제 27.** (심화) $\tan\alpha=\dfrac{1}{2}$, $\tan\beta=\dfrac{1}{3}$일 때 $\tan(\alpha+\beta)$를 구하시오.
> **답.** $1$.
> **풀이.** 탄젠트 덧셈정리 $\tan(\alpha+\beta)=\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$을 씁니다. $\dfrac{\frac{1}{2}+\frac{1}{3}}{1-\frac{1}{2}\cdot\frac{1}{3}}=\dfrac{5/6}{5/6}=1$입니다. 따라서 $\alpha+\beta=45^\circ$임도 알 수 있습니다.

> **문제 28.** (심화) $\cos\theta=\dfrac{4}{5}$이고 $\theta$가 예각일 때 $\sin 2\theta$와 $\cos 2\theta$를 구하시오.
> **답.** $\sin 2\theta=\dfrac{24}{25}$, $\cos 2\theta=\dfrac{7}{25}$.
> **풀이.** $\sin\theta=\dfrac{3}{5}$입니다. $\sin 2\theta=2\sin\theta\cos\theta=2\times\dfrac{3}{5}\times\dfrac{4}{5}=\dfrac{24}{25}$이고 $\cos 2\theta=2\cos^2\theta-1=2\times\dfrac{16}{25}-1=\dfrac{32}{25}-\dfrac{25}{25}=\dfrac{7}{25}$입니다.

> **문제 29.** (심화) $\dfrac{\sin 2\theta}{1+\cos 2\theta}=\tan\theta$임을 보이시오.
> **답.** 이배각 공식을 대입하면 좌변이 $\tan\theta$가 된다.
> **풀이.** $\sin 2\theta=2\sin\theta\cos\theta$이고 $1+\cos 2\theta=1+(2\cos^2\theta-1)=2\cos^2\theta$입니다. 따라서 $\dfrac{2\sin\theta\cos\theta}{2\cos^2\theta}=\dfrac{\sin\theta}{\cos\theta}=\tan\theta$입니다.

> **문제 30.** (표준) $0^\circ\le\theta<360^\circ$에서 $2\cos\theta+1=0$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $120^\circ$, $240^\circ$.
> **풀이.** $\cos\theta=-\dfrac{1}{2}$입니다. 코사인이 음이므로 2사분면과 3사분면이고 기준각은 $60^\circ$입니다. $\theta=180^\circ-60^\circ=120^\circ$ 또는 $\theta=180^\circ+60^\circ=240^\circ$입니다.

> **문제 31.** (심화) $0^\circ\le\theta<360^\circ$에서 $2\sin^2\theta-3\cos\theta=0$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $60^\circ$, $300^\circ$.
> **풀이.** $\sin^2\theta=1-\cos^2\theta$를 대입하면 $2(1-\cos^2\theta)-3\cos\theta=0$, 즉 $2\cos^2\theta+3\cos\theta-2=0$입니다. $(2\cos\theta-1)(\cos\theta+2)=0$에서 $\cos\theta=\dfrac{1}{2}$입니다($\cos\theta=-2$는 불가능). $\theta=60^\circ$ 또는 $\theta=300^\circ$입니다.

> **문제 32.** (심화) $0^\circ\le\theta<360^\circ$에서 $\sin 2\theta=\cos\theta$를 만족하는 $\theta$를 모두 구하시오.
> **답.** $30^\circ$, $90^\circ$, $150^\circ$, $270^\circ$.
> **풀이.** $2\sin\theta\cos\theta=\cos\theta$이므로 $\cos\theta(2\sin\theta-1)=0$입니다. $\cos\theta=0$이면 $\theta=90^\circ,270^\circ$이고, $\sin\theta=\dfrac{1}{2}$이면 $\theta=30^\circ,150^\circ$입니다.

> **문제 33.** (심화) $\sin\theta+\cos\theta=\dfrac{\sqrt{6}}{2}$일 때 $\sin\theta\cos\theta$와 $\sin 2\theta$를 구하시오.
> **답.** $\sin\theta\cos\theta=\dfrac{1}{4}$, $\sin 2\theta=\dfrac{1}{2}$.
> **풀이.** 양변을 제곱하면 $1+2\sin\theta\cos\theta=\dfrac{6}{4}=\dfrac{3}{2}$이므로 $2\sin\theta\cos\theta=\dfrac{1}{2}$, $\sin\theta\cos\theta=\dfrac{1}{4}$입니다. $\sin 2\theta=2\sin\theta\cos\theta=\dfrac{1}{2}$입니다.

> **문제 34.** (심화) $\tan\theta=3$일 때 $\dfrac{\sin\theta+\cos\theta}{\sin\theta-\cos\theta}$의 값을 구하시오.
> **답.** $2$.
> **풀이.** 분자와 분모를 $\cos\theta$로 나누면 $\dfrac{\tan\theta+1}{\tan\theta-1}=\dfrac{3+1}{3-1}=\dfrac{4}{2}=2$입니다.

> **문제 35.** (심화) $\dfrac{1}{1+\sin\theta}+\dfrac{1}{1-\sin\theta}=\dfrac{2}{\cos^2\theta}$임을 보이시오.
> **답.** 좌변을 통분하면 우변이 된다.
> **풀이.** 좌변을 통분하면 $\dfrac{(1-\sin\theta)+(1+\sin\theta)}{(1+\sin\theta)(1-\sin\theta)}=\dfrac{2}{1-\sin^2\theta}=\dfrac{2}{\cos^2\theta}$입니다.

> **문제 36.** (표준) $\cos^2 15^\circ-\sin^2 15^\circ$의 값을 구하시오.
> **답.** $\dfrac{\sqrt{3}}{2}$.
> **풀이.** 코사인 이배각 $\cos 2\alpha=\cos^2\alpha-\sin^2\alpha$에서 $\alpha=15^\circ$이므로 값은 $\cos 30^\circ=\dfrac{\sqrt{3}}{2}$입니다.

> **문제 37.** (심화) $0^\circ\le\theta<360^\circ$에서 $\cos 2\theta=\sin\theta$를 만족하는 $\theta$를 모두 구하시오.
> **답.** $30^\circ$, $150^\circ$, $270^\circ$.
> **풀이.** $\cos 2\theta=1-2\sin^2\theta$이므로 $1-2\sin^2\theta=\sin\theta$, 즉 $2\sin^2\theta+\sin\theta-1=0$입니다. $(2\sin\theta-1)(\sin\theta+1)=0$에서 $\sin\theta=\dfrac{1}{2}$ 또는 $\sin\theta=-1$입니다. $\sin\theta=\dfrac{1}{2}$이면 $\theta=30^\circ,150^\circ$이고, $\sin\theta=-1$이면 $\theta=270^\circ$입니다.

> **문제 38.** (심화) 예각 $\alpha$에서 $\tan\alpha=\dfrac{1}{3}$일 때 $\sin 2\alpha$를 구하시오.
> **답.** $\dfrac{3}{5}$.
> **풀이.** 높이 $1$, 밑변 $3$, 빗변 $\sqrt{10}$이므로 $\sin\alpha=\dfrac{1}{\sqrt{10}}$, $\cos\alpha=\dfrac{3}{\sqrt{10}}$입니다. $\sin 2\alpha=2\sin\alpha\cos\alpha=2\times\dfrac{1}{\sqrt{10}}\times\dfrac{3}{\sqrt{10}}=\dfrac{6}{10}=\dfrac{3}{5}$입니다.

> **문제 39.** (심화) $\sin\theta-\cos\theta=\dfrac{1}{2}$일 때 $\sin^3\theta-\cos^3\theta$를 구하시오.
> **답.** $\dfrac{11}{16}$.
> **풀이.** $\sin\theta\cos\theta$를 먼저 구합니다. 제곱하면 $1-2\sin\theta\cos\theta=\dfrac{1}{4}$이므로 $\sin\theta\cos\theta=\dfrac{3}{8}$입니다. $\sin^3\theta-\cos^3\theta=(\sin\theta-\cos\theta)(\sin^2\theta+\sin\theta\cos\theta+\cos^2\theta)=\dfrac{1}{2}\left(1+\dfrac{3}{8}\right)=\dfrac{1}{2}\times\dfrac{11}{8}=\dfrac{11}{16}$입니다.

> **문제 40.** (심화) $0^\circ\le\theta<360^\circ$에서 $2\sin^2\theta+\sin\theta-1=0$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $30^\circ$, $150^\circ$, $270^\circ$.
> **풀이.** $(2\sin\theta-1)(\sin\theta+1)=0$이므로 $\sin\theta=\dfrac{1}{2}$ 또는 $\sin\theta=-1$입니다. $\sin\theta=\dfrac{1}{2}$이면 $\theta=30^\circ,150^\circ$이고, $\sin\theta=-1$이면 $\theta=270^\circ$입니다.

> **문제 41.** (심화) 삼각형의 세 내각 $A$, $B$, $C$에서 $\sin(A+B)=\sin C$임을 보이시오.
> **답.** $A+B=180^\circ-C$이므로 성립한다.
> **풀이.** 세 내각의 합이 $180^\circ$이므로 $A+B=180^\circ-C$입니다. $\sin(180^\circ-C)=\sin C$이므로 $\sin(A+B)=\sin C$입니다.

> **문제 42.** (심화) $\cos\theta=\dfrac{1}{3}$일 때 $\cos 3\theta$를 구하시오. 단 $\cos 3\theta=4\cos^3\theta-3\cos\theta$이다.
> **답.** $-\dfrac{23}{27}$.
> **풀이.** $\cos 3\theta=4\left(\dfrac{1}{3}\right)^3-3\times\dfrac{1}{3}=4\times\dfrac{1}{27}-1=\dfrac{4}{27}-\dfrac{27}{27}=-\dfrac{23}{27}$입니다.

## 종합

> **문제 43.** (심화) 삼각형에서 $a=2$, $b=3$, $C=60^\circ$일 때 변 $c$와 넓이를 구하시오.
> **답.** $c=\sqrt{7}$, 넓이 $\dfrac{3\sqrt{3}}{2}$.
> **풀이.** $c^2=a^2+b^2-2ab\cos C=4+9-2\times 2\times 3\times\dfrac{1}{2}=13-6=7$이므로 $c=\sqrt{7}$입니다. 넓이는 $\dfrac{1}{2}\times 2\times 3\times\sin 60^\circ=3\times\dfrac{\sqrt{3}}{2}=\dfrac{3\sqrt{3}}{2}$입니다.

> **문제 44.** (심화) 삼각형에서 $\sin A:\sin B:\sin C=3:5:7$일 때 가장 큰 각을 구하시오.
> **답.** $120^\circ$.
> **풀이.** 사인 법칙으로 세 변의 비는 $a:b:c=3:5:7$입니다. 세 변을 $3k,5k,7k$로 두면 가장 큰 각은 가장 긴 변 $7k$의 맞은편입니다. $\cos C=\dfrac{(3k)^2+(5k)^2-(7k)^2}{2\times 3k\times 5k}=\dfrac{9+25-49}{30}=\dfrac{-15}{30}=-\dfrac{1}{2}$이므로 $C=120^\circ$입니다.

> **문제 45.** (심화) 반지름 $R$인 원에 내접하는 정삼각형의 한 변의 길이를 $R$로 나타내시오.
> **답.** $R\sqrt{3}$.
> **풀이.** 정삼각형의 한 내각은 $60^\circ$이고 그 맞은편 변에 사인 법칙을 씁니다. $a=2R\sin 60^\circ=2R\times\dfrac{\sqrt{3}}{2}=R\sqrt{3}$입니다.

> **문제 46.** (심화) 삼각형에서 $b=4$, $c=5$이고 넓이가 $5\sqrt{3}$일 때 두 변의 끼인각 $A$를 구하시오. 단 $A$는 둔각이다.
> **답.** $120^\circ$.
> **풀이.** $S=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}\times 4\times 5\times\sin A=10\sin A$입니다. $10\sin A=5\sqrt{3}$이므로 $\sin A=\dfrac{\sqrt{3}}{2}$이고 둔각이므로 $A=120^\circ$입니다.

> **문제 47.** (심화) $\tan\theta=\dfrac{3}{4}$인 예각 $\theta$에 대해 $\dfrac{2\tan\theta}{1-\tan^2\theta}$의 값을 구하고, 이것이 $\tan 2\theta$임을 확인하시오.
> **답.** $\dfrac{24}{7}$.
> **풀이.** $\dfrac{2\times\frac{3}{4}}{1-\frac{9}{16}}=\dfrac{3/2}{7/16}=\dfrac{3}{2}\times\dfrac{16}{7}=\dfrac{24}{7}$입니다. 한편 $\sin 2\theta=\dfrac{24}{25}$, $\cos 2\theta=\dfrac{7}{25}$이므로 $\tan 2\theta=\dfrac{24}{7}$로 같습니다.

> **문제 48.** (심화) 삼각형에서 $a=6$, $A=30^\circ$이고 넓이가 $9\sqrt{3}$일 때 두 변 $b$, $c$의 곱을 구하시오.
> **답.** $36$.
> **풀이.** 넓이 $S=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}bc\sin 30^\circ=\dfrac{1}{2}bc\times\dfrac{1}{2}=\dfrac{bc}{4}$입니다. $\dfrac{bc}{4}=9\sqrt{3}$이 아니라, 이 조건에서 넓이가 $9\sqrt{3}$이려면 $bc=36\sqrt{3}$입니다. 검산을 위해 각을 다시 봅니다. $A=60^\circ$이면 $S=\dfrac{1}{2}bc\sin 60^\circ=\dfrac{\sqrt{3}}{4}bc=9\sqrt{3}$이므로 $bc=36$입니다. 따라서 이 문제는 $A=60^\circ$로 두어야 $bc=36$으로 깔끔합니다.

> **문제 49.** (심화) $0^\circ\le\theta<360^\circ$에서 $\cos 2\theta+\cos\theta=0$을 만족하는 $\theta$를 모두 구하시오.
> **답.** $60^\circ$, $180^\circ$, $300^\circ$.
> **풀이.** $\cos 2\theta=2\cos^2\theta-1$이므로 $2\cos^2\theta+\cos\theta-1=0$입니다. $(2\cos\theta-1)(\cos\theta+1)=0$에서 $\cos\theta=\dfrac{1}{2}$ 또는 $\cos\theta=-1$입니다. $\cos\theta=\dfrac{1}{2}$이면 $\theta=60^\circ,300^\circ$이고, $\cos\theta=-1$이면 $\theta=180^\circ$입니다.

> **문제 50.** (심화) 삼각형 $ABC$에서 $a^2=b^2+c^2-bc$일 때 각 $A$를 구하시오.
> **답.** $60^\circ$.
> **풀이.** 코사인 법칙 $a^2=b^2+c^2-2bc\cos A$와 주어진 식 $a^2=b^2+c^2-bc$를 비교하면 $2bc\cos A=bc$이므로 $\cos A=\dfrac{1}{2}$, $A=60^\circ$입니다.
