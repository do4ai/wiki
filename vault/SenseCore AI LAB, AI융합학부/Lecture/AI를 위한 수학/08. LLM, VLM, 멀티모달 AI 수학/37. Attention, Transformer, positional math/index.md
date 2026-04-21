---
title: "37. Attention, Transformer, positional math"
source_kind: page
source_path: ssot/pages/31ee313f58b980d68c5ad8ed9d5aeff8__SenseCore AI LAB, AI융합학부/children/lecture/32be313f58b980078dbbeed4f006f95b__Lecture/children/math/32be313f58b981e7b26fea2d45e6fa7f__AI를 위한 수학/children/32be313f58b9810b873aef61d2e45e6d__08. 신경망과 현대 AI 수학/children/32ce313f58b981a3b3c8f735fc4a761e__37. Attention, Transformer, positional math
notion_id: 32ce313f58b981a3b3c8f735fc4a761e
notion_url: https://www.notion.so/32ce313f58b981a3b3c8f735fc4a761e
parent_notion_id: 32be313f58b9810b873aef61d2e45e6d
---
attention은 문장을 읽을 때 "지금 이 토큰을 이해하려면 다른 토큰 중 무엇을 얼마나 참고해야 하는가?"를 계산하는 장치입니다. Transformer는 이 attention을 중심으로 문맥을 반복해서 섞고 가공하는 구조입니다. 이 강의에서는 attention의 직관만 소개하는 데서 멈추지 않고, 행렬 차원, scaled dot-product attention의 계산 순서, multi-head attention의 이유, positional encoding과 causal mask의 필요성, 그리고 Transformer 블록이 실제로 어떤 흐름으로 계산되는지까지 한 단계 더 깊게 다룹니다.

# 먼저 알아둘 말
- 토큰: 문장이나 데이터를 잘게 나눈 입력 단위다.
- 임베딩: 토큰을 숫자 벡터로 바꾼 표현이다.
- query: 지금 토큰이 찾고 싶은 정보의 기준이다.
- key: 각 토큰이 제공할 수 있는 정보의 표지다.
- value: 실제로 전달할 내용이다.
- attention weight: 어떤 토큰을 얼마나 참고할지 나타내는 가중치다.
- softmax: 점수들을 합이 1인 가중치로 바꾸는 함수다.
- positional encoding: 순서 정보를 벡터에 더하는 장치다.
- self-attention: 같은 입력 안의 토큰들끼리 서로를 참고하는 attention이다.
- cross-attention: 한 시퀀스의 query가 다른 시퀀스의 key, value를 참고하는 attention이다.
- causal mask: 미래 토큰을 보지 못하게 가리는 마스크다.
- head: attention을 여러 개의 관점으로 병렬 계산하는 한 갈래다.
- residual connection: 이전 표현을 다음 계산 결과에 더하는 연결 방식이다.
- layer normalization: 층 내부 표현의 스케일을 안정화하는 정규화다.
- MLP: attention으로 섞인 정보를 위치별로 다시 비선형 가공하는 층이다.

# 이 강의에서 답할 질문
- attention은 왜 RNN 이후의 핵심 구조가 되었는가?
- query, key, value는 각각 어떤 역할을 하는가?
- attention 식은 행렬 관점에서 어떻게 읽어야 하는가?
- 왜 점수를 `sqrt(d_k)`로 나누는가?
- multi-head attention은 head를 하나만 쓰는 것보다 무엇이 좋은가?
- positional encoding과 causal mask는 각각 어떤 문제를 해결하는가?
- Transformer 블록은 실제로 어떤 계산 순서로 흘러가는가?

# 먼저 떠올릴 장면
- "철수가 영희를 도왔다. 그는 기뻤다."라는 문장에서 "그는"이 누구인지 이해하려면 앞에 나온 단어들을 다시 봐야 합니다.
- 그런데 문맥 이해는 단순히 한 단어만 되짚는 일로 끝나지 않습니다. 주어-동사 관계, 수식어 연결, 부정 범위, 멀리 떨어진 참조까지 함께 봐야 합니다.
- attention은 이 "필요한 곳을 선택적으로 다시 보는 과정"을 수치화한 장치입니다.
- Transformer는 이 계산을 한 번만 하는 것이 아니라 여러 층에서 반복해 표현을 더 정교하게 만듭니다.

# 이 강의의 큰 그림
이 강의는 다음 순서로 읽는 것이 좋습니다.

1. 먼저 왜 문맥 이해에 "다시 보기"가 필요한지 직관을 잡습니다.
2. 그다음 입력 행렬에서 query, key, value가 어떻게 만들어지는지 봅니다.
3. 이어서 scaled dot-product attention을 행렬 계산 순서대로 해석합니다.
4. 그 뒤 multi-head attention, positional encoding, causal mask가 왜 필요한지 설명합니다.
5. 마지막으로 Transformer 블록과 decoder-only LLM 구조까지 연결합니다.

# 먼저 문제를 세우기
전통적인 순차 모델은 토큰을 왼쪽에서 오른쪽으로 하나씩 처리합니다. 이 방식은 자연스럽지만 두 가지 한계가 있습니다.

1. 멀리 떨어진 토큰 관계를 잡기가 어렵습니다.
2. 순차 계산이 강해서 병렬화가 어렵습니다.

예를 들어 문장 앞부분의 주어와 한참 뒤에 있는 동사를 연결하거나, 앞 문장에 나온 대명사 참조를 유지하려면 긴 경로를 따라 정보가 전달되어야 합니다. attention은 이런 문제를 "현재 토큰이 다른 모든 토큰을 직접 참고할 수 있게 하자"는 방식으로 바꿉니다. 그래서 정보 경로가 짧아지고, 모든 토큰 쌍의 관련성을 한 번에 계산할 수 있습니다.

# 입력을 행렬로 보기
길이가

$$
n
$$

인 시퀀스가 있고, 각 토큰 임베딩 차원이

$$
d_{\text{model}}
$$

이라고 합시다. 입력 전체를 행렬

$$
X \in \mathbb{R}^{n \times d_{\text{model}}}
$$

로 적을 수 있습니다. 이때 한 행은 한 토큰의 표현입니다.

Transformer는 이 입력에서 세 가지 다른 선형 변환을 만듭니다.

$$
Q = XW_Q,\qquad K = XW_K,\qquad V = XW_V
$$

여기서 보통

$$
W_Q, W_K \in \mathbb{R}^{d_{\text{model}} \times d_k}, \qquad
W_V \in \mathbb{R}^{d_{\text{model}} \times d_v}
$$

입니다. 따라서

$$
Q, K \in \mathbb{R}^{n \times d_k}, \qquad
V \in \mathbb{R}^{n \times d_v}
$$

가 됩니다.

이 식은 단순한 기호 장난이 아닙니다. 같은 입력

$$
X
$$

를 세 번 다르게 투영해서, "찾는 기준", "비교 기준", "전달 내용"을 분리한 것입니다.

## query, key, value의 역할
이 셋은 보통 다음처럼 이해하면 됩니다.

| 구성요소 | 질문 형태 | 역할 |
| --- | --- | --- |
| query | "나는 지금 어떤 정보를 찾고 있나?" | 현재 토큰의 관심사 |
| key | "나는 어떤 정보로 검색될 수 있나?" | 각 토큰의 검색 표지 |
| value | "실제로 전달할 내용은 무엇인가?" | 가져올 실제 정보 |

토큰은 한편으로는 남을 참고하는 주체이고, 다른 한편으로는 남에게 참고되는 대상입니다. 또 비교 기준과 실제 전달 내용이 같을 필요도 없습니다. 그래서 셋을 분리하는 것이 더 표현력이 높습니다.

# attention 식을 행렬 계산으로 읽기
scaled dot-product attention은 보통 다음 식으로 씁니다.

$$
\mathrm{Attention}(Q, K, V)
=
\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

이 식은 반드시 계산 순서대로 읽어야 이해됩니다.

## 1. 점수 행렬 만들기
먼저

$$
S = QK^\top
$$

를 계산합니다. 그러면

$$
S \in \mathbb{R}^{n \times n}
$$

이 됩니다. 이 행렬의

$$
(i,j)
$$

원소는 `i`번째 토큰이 `j`번째 토큰을 얼마나 참고하고 싶은지를 나타내는 원시 점수입니다.

즉,

$$
S_{ij} = q_i \cdot k_j
$$

입니다. 내적이 크면 현재 토큰의 관심사와 상대 토큰의 key가 잘 맞는다는 뜻입니다.

## 2. 스케일 안정화
그다음

$$
\frac{S}{\sqrt{d_k}}
$$

를 계산합니다. 왜 나누는가가 중요합니다.

차원

$$
d_k
$$

가 커지면 내적값의 분산도 커져 softmax 입력이 지나치게 커질 수 있습니다. 그러면 softmax가 너무 뾰족해져 거의 one-hot처럼 변하고, gradient가 불안정해질 수 있습니다. 따라서

$$
\sqrt{d_k}
$$

로 나누어 점수의 스케일을 안정화합니다.

이 단계는 단순한 수학 장식이 아니라 학습 안정성을 위한 핵심 장치입니다.

## 3. softmax로 가중치 만들기
이제 행별로 softmax를 적용해

$$
A = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)
$$

를 만듭니다. 그러면

$$
A \in \mathbb{R}^{n \times n}
$$

이고, 각 행의 합은 1입니다.

즉 `i`번째 행은 `i`번째 토큰이 다른 토큰들을 어떤 비율로 참고하는지를 나타냅니다.

## 4. value의 가중합
마지막으로

$$
H = AV
$$

를 계산합니다. 여기서

$$
H \in \mathbb{R}^{n \times d_v}
$$

입니다. `i`번째 출력 벡터는 모든 토큰의 value를 attention weight로 가중합한 결과입니다.

즉 현재 토큰 표현은 자기 자신만의 정보가 아니라, 문맥 전체를 참고해 다시 만든 표현이 됩니다.

# attention을 표로 보는 작은 예
문장 `"철수 / 가 / 웃었다 / 그는 / 기뻤다"`를 생각해 봅시다. `"그는"`을 처리할 때의 attention을 아주 단순화하면 다음 같은 그림을 떠올릴 수 있습니다.

| 현재 토큰 | 강하게 보는 대상 | 이유 |
| --- | --- | --- |
| 그는 | 철수 | 대명사 참조 후보 |
| 그는 | 웃었다 | 감정 상태의 원인 추론 |
| 그는 | 기뻤다 | 현재 서술과의 직접 연결 |

실제 모델은 이런 이유를 언어로 쓰지 않습니다. 대신 query-key 내적으로 점수를 만들고, softmax를 통해 비율을 정합니다. 하지만 직관은 결국 "필요한 곳에 더 큰 비중을 둔다"는 말로 요약할 수 있습니다.

# self-attention은 무엇을 잘하는가
self-attention의 장점은 세 가지 관점에서 이해할 수 있습니다.

## 1. 긴 거리 관계를 직접 연결한다
RNN류 모델에서는 멀리 떨어진 토큰 관계가 많은 단계를 거쳐 전달됩니다. self-attention에서는 멀리 있는 토큰도 한 번의 attention 계산으로 직접 참고할 수 있습니다.

## 2. 병렬 계산이 쉽다
모든 토큰 쌍의 점수를 행렬 곱으로 한 번에 계산할 수 있으므로 GPU 병렬화에 유리합니다.

## 3. 토큰별로 다른 문맥을 만들 수 있다
같은 입력 문장이라도 각 토큰은 서로 다른 attention 분포를 가질 수 있습니다. 즉 문맥 표현이 위치마다 다르게 재구성됩니다.

반대로 비용도 있습니다. 시퀀스 길이가

$$
n
$$

일 때 점수 행렬이

$$
n \times n
$$

이므로 계산량과 메모리 사용이 길이 제곱에 비례해 커집니다. 긴 문맥 처리에서 attention 최적화가 중요한 이유가 여기에 있습니다.

# multi-head attention은 왜 필요한가
head를 하나만 쓰면 attention은 한 종류의 관련성만 강하게 포착할 수 있습니다. 하지만 실제 문맥에는 다양한 관계가 동시에 있습니다.

- 대명사 참조
- 주어-동사 일치
- 수식어 연결
- 문장 구조
- 장거리 의존성

그래서 Transformer는 attention을 여러 head로 나눠 병렬로 계산합니다.

$$
\mathrm{head}_i
=
\mathrm{Attention}(XW_Q^{(i)}, XW_K^{(i)}, XW_V^{(i)})
$$

그리고 이들을 이어 붙여

$$
\mathrm{MHA}(X)
=
\mathrm{Concat}(\mathrm{head}_1, \dots, \mathrm{head}_h)W_O
$$

로 만듭니다.

이 구조의 직관은 "문맥을 하나의 렌즈로만 보지 말고 여러 렌즈로 보자"입니다. 어떤 head는 가까운 토큰 관계를 보고, 어떤 head는 장거리 참조를 보고, 또 어떤 head는 구문 구조를 더 잘 포착할 수 있습니다. 물론 실제로 모든 head가 완벽히 분업되는 것은 아니지만, 표현력을 높이는 핵심 장치라는 점은 분명합니다.

# positional encoding이 왜 필요한가
attention은 토큰들 사이의 관계를 비교하는 연산이지만, 입력 순서를 저절로 기억하지는 않습니다. 극단적으로 말하면 순서 정보가 전혀 없는 상태에서는 `"개가 사람을 물었다"`와 `"사람이 개를 물었다"`가 비슷한 토큰 집합처럼 보일 수 있습니다.

따라서 위치 정보를 따로 넣어 주어야 합니다. 초기 Transformer에서는 사인, 코사인 기반 positional encoding을 사용했습니다.

$$
\mathrm{PE}(pos, 2i)
=
\sin\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

$$
\mathrm{PE}(pos, 2i+1)
=
\cos\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

이 벡터를 토큰 임베딩에 더해 위치를 알려 줍니다.

이 방식을 직관적으로 보면:

1. 각 차원이 서로 다른 주기의 파동을 가집니다.
2. 위치마다 고유한 패턴이 만들어집니다.
3. 상대적 위치 차이도 어느 정도 선형적으로 표현할 수 있습니다.

현대 모델에서는 학습형 위치 임베딩, 상대 위치 방식, 회전형 위치 표현 등 다양한 방식이 쓰이지만, 핵심은 같습니다. attention이 내용 관계만으로는 부족하므로 순서 정보를 별도로 공급해야 한다는 점입니다.

# causal mask는 왜 중요한가
언어모델은 다음 토큰을 예측해야 하므로 현재 위치가 미래 토큰을 미리 보면 안 됩니다. 예를 들어 `"나는 오늘"` 다음 토큰을 예측할 때 정답 문장 전체를 이미 보고 있으면 학습이 너무 쉬워지고, 생성 시점의 제약과 맞지 않게 됩니다.

그래서 decoder self-attention에는 causal mask를 씁니다. 미래 위치의 점수에

$$
-\infty
$$

에 가까운 값을 더해 softmax 후 가중치가 0이 되게 합니다.

즉 현재 위치 `t`는 오직 `1`부터 `t`까지의 토큰만 볼 수 있습니다. 이 제약이 있어야 autoregressive language model이 성립합니다.

# Transformer 블록을 실제 계산 순서로 보기
Transformer 블록은 attention 하나로 끝나지 않습니다. 현대 구현에서는 보통 다음과 같은 pre-norm 형태를 자주 봅니다.

$$
U = X + \mathrm{MHA}(\mathrm{LN}(X))
$$

$$
Y = U + \mathrm{MLP}(\mathrm{LN}(U))
$$

이 식을 단계별로 읽어 보면 다음과 같습니다.

## 1. layer normalization
입력 표현의 스케일을 안정화합니다. 깊은 층에서도 학습이 흔들리지 않게 돕습니다.

## 2. multi-head self-attention
각 토큰이 문맥 전체를 참고해 새 표현을 만듭니다.

## 3. residual addition
원래 입력을 더해 정보 손실을 줄이고 gradient 흐름을 돕습니다.

## 4. 두 번째 normalization
attention 이후 표현을 다시 안정화합니다.

## 5. MLP
attention으로 섞인 표현을 위치별로 비선형 가공합니다. attention이 "어디를 볼까"를 정하는 장치라면, MLP는 "본 정보를 어떻게 변환할까"를 담당합니다.

## 6. residual addition
다시 원래 경로를 보존하며 층을 깊게 쌓을 수 있게 합니다.

따라서 Transformer 블록은 단순한 attention 덩어리가 아니라:

1. 문맥을 섞는 단계
2. 그 결과를 비선형 변환하는 단계

를 residual 구조 안에서 반복하는 시스템입니다.

# encoder, decoder, decoder-only의 차이
Transformer라는 말은 원래 하나의 고정 구조를 뜻하기보다 attention 중심 설계 원리를 뜻합니다.

## encoder
- 입력 전체를 양방향 self-attention으로 읽습니다.
- 분류, 인코딩, 이해 과제에 적합합니다.

## decoder
- masked self-attention으로 과거만 봅니다.
- 필요하면 encoder 출력에 cross-attention도 붙습니다.
- 생성 과제에 적합합니다.

## decoder-only LLM
- 현대 LLM의 핵심 구조입니다.
- masked self-attention과 MLP 블록을 반복해 다음 토큰을 예측합니다.
- GPT 계열을 이해할 때 가장 먼저 떠올려야 하는 구조입니다.

즉 오늘 배운 attention과 Transformer 블록은 곧바로 LLM 구조로 이어집니다.

# attention을 이해할 때 자주 생기는 오해
## 오해 1. attention weight가 곧 설명 가능성이다
attention weight는 참고 비율을 보여 주지만, 그것만으로 모델의 완전한 추론 과정을 설명한다고 보기는 어렵습니다. 이후 MLP, residual, 여러 층의 상호작용도 함께 작동합니다.

## 오해 2. query, key, value는 단어 사전처럼 고정된 의미다
이들은 입력마다 달라지는 동적 표현입니다. 같은 단어라도 문맥에 따라 query, key, value가 달라집니다.

## 오해 3. positional encoding만 있으면 순서를 완전히 해결한다
위치 정보는 중요하지만, 실제 순서 이해는 attention, MLP, 층 반복 전체가 함께 만들어 냅니다.

# 예제
1. 관련 토큰에 더 큰 가중치
문제: 현재 토큰의 query가 어떤 이전 토큰의 key와 매우 비슷하다면 어떤 일이 일어나는가?
풀이: 그 이전 토큰에 대한 attention weight가 커지고, 그 토큰의 value가 더 크게 반영된다.
해설: attention은 "관련성이 큰 곳을 더 본다"는 직관을 수치로 구현한 것이다.

2. `sqrt(d_k)`로 나누는 이유
문제: query-key 점수를 그냥 softmax에 넣지 않고 차원 크기의 제곱근으로 나누는 이유는 무엇인가?
풀이: 차원이 커질수록 내적값이 커져 softmax가 지나치게 뾰족해지고 학습이 불안정해질 수 있기 때문이다.
해설: scaled dot-product attention의 "scaled"는 바로 이 안정화 장치를 뜻한다.

3. multi-head attention의 필요성
문제: head를 하나만 쓰는 대신 여러 개를 병렬로 쓰는 이유는 무엇인가?
풀이: 서로 다른 종류의 문맥 관계를 여러 관점에서 동시에 포착하기 위해서다.
해설: 대명사 참조, 구문 구조, 장거리 의존성처럼 다양한 관계를 한 렌즈만으로 보기 어렵다.

4. causal mask의 역할
문제: 언어모델 학습에서 미래 토큰을 가리는 이유는 무엇인가?
풀이: 현재 위치가 미래 정답을 미리 보면 autoregressive 생성 문제와 맞지 않기 때문이다.
해설: mask는 "현재는 과거만 볼 수 있다"는 생성 규칙을 강제한다.

5. positional encoding의 필요성
문제: positional encoding이 없다면 어떤 문장 차이를 놓치기 쉬운가?
풀이: 같은 단어들이라도 순서만 다른 문장을 잘 구분하기 어려워진다.
해설: attention은 내용 비교는 잘하지만 위치 정보는 별도로 주어야 한다.

# 핵심 정리
- attention은 현재 토큰이 다른 토큰을 어떤 비율로 참고할지 계산하는 장치다.
- query, key, value는 찾기 기준, 비교 표지, 전달 내용을 분리한 표현이다.
- scaled dot-product attention은 점수 행렬, 스케일 안정화, softmax, value 가중합의 순서로 읽어야 한다.
- multi-head attention은 여러 종류의 문맥 관계를 병렬로 포착하게 한다.
- positional encoding은 순서를, causal mask는 미래 차단을 담당한다.
- Transformer 블록은 attention과 MLP를 residual 구조 안에서 반복한다.
- decoder-only Transformer는 곧 현대 LLM의 기본 뼈대다.

# 스스로 점검
## 연습 문제
1. query, key, value를 각각 자연어와 행렬 관점에서 설명하라.
2. attention 식을 계산 순서대로 읽으며 각 단계의 역할과 출력 차원을 설명하라.
3. `sqrt(d_k)`로 나누지 않으면 어떤 학습 문제가 생길 수 있는지 설명하라.
4. multi-head attention이 head 하나보다 왜 더 표현력이 높은지 설명하라.
5. positional encoding과 causal mask가 각각 해결하는 문제를 구분해 설명하라.
6. Transformer 블록에서 attention과 MLP가 맡는 역할을 비교하라.

## 복습 질문
1. self-attention은 왜 긴 거리 의존성에 유리한가?
2. attention weight 행렬의 각 행은 무엇을 뜻하는가?
3. decoder-only LLM에서 미래 토큰을 보면 안 되는 이유는 무엇인가?
4. residual connection은 왜 깊은 구조에서 중요한가?

## 체크포인트
1. `Q`, `K`, `V`, `A`, `H`의 의미와 차원을 말할 수 있다.
2. scaled dot-product attention을 식이 아니라 계산 흐름으로 설명할 수 있다.
3. multi-head attention의 이유를 직관과 구조 양쪽에서 말할 수 있다.
4. positional encoding과 causal mask의 차이를 설명할 수 있다.
5. Transformer 블록이 `LN -> Attention -> Add -> LN -> MLP -> Add` 흐름으로 작동함을 설명할 수 있다.
