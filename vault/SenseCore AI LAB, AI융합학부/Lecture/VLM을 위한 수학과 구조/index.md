---
title: "VLM을 위한 수학과 구조"
source_kind: page
---
# VLM을 위한 수학과 구조
이 책은 [AI를 위한 수학](../AI를 위한 수학/index.md)을 이미 읽고 온 학습자를 위한 `VLM 특화 심화 교재`입니다. 따라서 여기서는 Transformer의 일반론, 텍스트-only alignment의 일반론, CLIP의 가장 기초 개념을 처음부터 다시 가르치지 않습니다. 대신 VLM에서만 본격적으로 어려워지는 시각 토큰화, connector 설계, OCR와 grounding, multimodal tuning, faithfulness 평가, video/audio/agent 확장을 순서대로 다룹니다.

# 이 책의 목표
- VLM에서만 중요한 시각 표현과 token budget 문제를 구조적으로 읽습니다.
- image-text alignment를 `VLM용 pretraining 데이터와 목적함수` 관점에서 다시 해석합니다.
- connector, resampler, Q-Former, decoder-only VLM 같은 대표 설계를 비교합니다.
- OCR, document understanding, region grounding, faithfulness를 핵심 난제로 정리합니다.
- multimodal tuning, evaluation, RAG/agent, frontier 논문 독해까지 VLM 중심으로 연결합니다.

# 이 책의 선수 지식
- [AI를 위한 수학 02단계](../AI를 위한 수학/02. 벡터와 행렬의 시작/index.md): 벡터, 행렬, 투영, 저랭크 근사를 이미 안다고 가정합니다.
- [AI를 위한 수학 05단계](../AI를 위한 수학/05. 최적화와 정보이론/index.md): cross-entropy, KL, 최적화 기본기는 다시 풀지 않습니다.
- [AI를 위한 수학 07단계](../AI를 위한 수학/07. 딥러닝과 생성모델/index.md): 신경망, self-supervised learning, diffusion의 일반론은 선수지식입니다.
- [AI를 위한 수학 08단계](../AI를 위한 수학/08. LLM, VLM, 멀티모달 AI 수학/index.md): Transformer, pretraining, alignment, CLIP의 큰 그림을 이미 읽었다고 가정합니다.

# 이 책에서 의도적으로 반복하지 않는 것
- Transformer의 가장 기본적인 attention 유도
- LLM pretraining과 tokenization의 일반론
- text-only SFT, RLHF, DPO의 보편 개론
- CLIP의 입문 수준 설명

이 책은 이런 공통 기반을 다시 길게 반복하지 않고, `그 공통 기반이 VLM에서 어떻게 달라지는가`에 집중합니다.

# 이 책을 읽는 방법
- 처음부터 끝까지 순서대로 읽습니다. 뒤 단계는 앞 단계의 용어와 병목을 이미 안다고 가정합니다.
- 공통 개념이 나오면 여기서 새로 외우기보다 `AI를 위한 수학`에서 어디까지 배웠는지 먼저 떠올립니다.
- 각 강의는 "입력은 무엇인가, vision token은 어디서 줄어드는가, language side는 어디서 읽는가"를 기준으로 읽습니다.
- OCR, grounding, evaluation처럼 실제 실패 사례가 나오면 반드시 구조와 데이터 문제로 다시 연결합니다.
- 막히면 뒤로 가기보다 바로 앞 단계의 VLM 전용 병목을 다시 확인합니다.

# 이 책의 읽는 순서
1. VLM의 시각 표현과 토큰화
2. 멀티모달 정렬과 데이터 설계
3. Connector와 VLM 아키텍처
4. Grounding, OCR, structured visual reasoning
5. 멀티모달 tuning, preference, safety
6. 평가, faithfulness, hallucination 완화
7. 비디오, 음성, RAG, 에이전트 시스템
8. Frontier VLM과 최신 논문 독해

이 순서는 단순 역사 순서가 아니라, `시각 표현 -> 정렬 데이터 -> connector 구조 -> grounded reasoning -> tuning과 safety -> trust 평가 -> 시스템 확장 -> frontier`로 병목을 따라가도록 배치했습니다.

# 각 단계에서 무엇을 배우는가
## 1단계. VLM의 시각 표현과 토큰화
- generic vision backbone 소개가 아니라 `VLM에서 왜 token budget이 곧 성능 병목인지`를 배웁니다.
- high-resolution 입력, connector 병목, backbone transfer를 VLM 과제와 바로 연결합니다.

## 2단계. 멀티모달 정렬과 데이터 설계
- CLIP 기본 개념을 다시 처음부터 가르치지 않고, `VLM용 pretraining pipeline` 안에서 정렬을 다시 읽습니다.
- interleaved data, OCR-heavy data, curated mixture가 왜 중요한지 정리합니다.

## 3단계. Connector와 VLM 아키텍처
- generic Transformer 설명보다 `vision token을 LM이 어떻게 읽게 만드는가`에 집중합니다.
- connector, resampler, Q-Former, decoder-only VLM family를 비교합니다.

## 4단계. Grounding, OCR, structured visual reasoning
- VLM 고유 난제인 OCR, document/chart understanding, spatial reference, counting을 묶습니다.
- grounded reasoning과 hallucination failure를 구조적 문제로 읽습니다.

## 5단계. 멀티모달 tuning, preference, safety
- text-only alignment 일반론이 아니라 `멀티모달 instruction data와 visual evidence가 들어간 정렬`을 다룹니다.
- refusal, jailbreak, safety policy를 이미지 입력까지 포함한 문제로 봅니다.

## 6단계. 평가, faithfulness, hallucination 완화
- benchmark 점수만이 아니라 faithfulness, verifier, abstention, human evaluation을 중심에 둡니다.
- `잘 맞는 모델`과 `믿을 수 있는 모델`의 차이를 다룹니다.

## 7단계. 비디오, 음성, RAG, 에이전트 시스템
- 단순 모달 추가가 아니라 video/audio/RAG/tool use가 붙으면서 시스템 문제가 어떻게 커지는지 봅니다.
- GUI agent와 serving, cost, latency를 함께 읽습니다.

## 8단계. Frontier VLM과 최신 논문 독해
- multimodal diffusion, unified model, MoE, world model 같은 VLM frontier를 정리합니다.
- open-source VLM 생태계와 실험 설계를 `재현성`과 `제품 적용 가능성` 기준으로 읽습니다.
- 최신 논문을 읽을 때 무엇이 진짜 novelty이고 무엇이 포장인지 구분하는 기준을 익힙니다.

# 모든 강의가 따르는 공통 순서
- 먼저 어떤 입력과 출력 문제를 다루는지 세웁니다.
- 그다음 필요한 표현과 모듈을 쉬운 말로 정리합니다.
- 그다음 손실, attention, 토큰 흐름 같은 핵심 수식을 붙입니다.
- 마지막에 실제 사용 장면, 실패 사례, 다음 단계 연결로 마무리합니다.

이 책은 이 순서를 지키면서 진행하므로, 위에서 아래로 읽기만 해도 `공통 AI 수학` 위에 `VLM 특화 난제`가 층층이 쌓이도록 구성합니다.

# 읽기 전에 기억할 약속
- 이 책은 독립 입문서가 아니라 VLM 특화 심화 교재입니다.
- 공통 개념은 짧게 상기하고, VLM 고유 병목을 오래 봅니다.
- 구조 이름보다 정보 흐름과 failure mode가 먼저입니다.
- 높은 점수보다 grounded answer와 faithfulness를 더 중요하게 봅니다.
- 이 책의 목적은 유행 모델 나열이 아니라 VLM 설계를 읽는 습관을 만드는 것입니다.

# 이 책을 마치면
이 책을 끝내면 어떤 VLM 논문이나 제품을 보더라도, `generic Transformer 설명`이 아니라 `시각 표현이 어디서 압축되고, connector가 어떤 병목을 만들고, OCR와 grounding이 왜 어렵고, safety와 evaluation이 어디서 실패하는지`를 순서대로 설명할 수 있어야 합니다. 더 나아가 이미지 VLM에서 비디오, 음성, RAG, agent, unified model까지 어떤 추가 난제가 붙는지도 연결해서 볼 수 있어야 합니다.

# 단계 목록
[01. VLM의 시각 표현과 토큰화](01. 이미지를 토큰으로 바꾸는 시야/index.md)
[02. 멀티모달 정렬과 데이터 설계](02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
[03. Connector와 VLM 아키텍처](03. VLM 아키텍처와 정보 흐름/index.md)
[04. Grounding, OCR, structured visual reasoning](04. Grounding, OCR, region reasoning/index.md)
[05. 멀티모달 tuning, preference, safety](05. 멀티모달 생성과 instruction tuning/index.md)
[06. 평가, faithfulness, hallucination 완화](06. 평가, 신뢰성, hallucination 완화/index.md)
[07. 비디오, 음성, RAG, 에이전트 시스템](07. 비디오, 음성, 에이전트로 확장/index.md)
[08. Frontier VLM과 최신 논문 독해](08. Frontier VLM과 최신 논문 독해/index.md)

## Page Tree

- [01. VLM의 시각 표현과 토큰화](01. 이미지를 토큰으로 바꾸는 시야/index.md)
  - [1. pixel, patch, feature map, vision token](01. 이미지를 토큰으로 바꾸는 시야/1. pixel, patch, feature map, vision token/index.md)
  - [2. CNN, ViT, positional structure](01. 이미지를 토큰으로 바꾸는 시야/2. CNN, ViT, positional structure/index.md)
  - [3. resolution, stride, pooling, token budget](01. 이미지를 토큰으로 바꾸는 시야/3. resolution, stride, pooling, token budget/index.md)
  - [4. projector, adapter, connector](01. 이미지를 토큰으로 바꾸는 시야/4. projector, adapter, connector/index.md)
  - [5. vision backbone pretraining과 transfer](01. 이미지를 토큰으로 바꾸는 시야/5. vision backbone pretraining과 transfer/index.md)
  - [문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야](01. 이미지를 토큰으로 바꾸는 시야/문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야/index.md)
- [02. 멀티모달 정렬과 데이터 설계](02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
  - [06. image-text pair, shared embedding, cosine similarity](02. 이미지와 텍스트를 같은 공간에 맞추기/06. image-text pair, shared embedding, cosine similarity/index.md)
  - [07. CLIP objective, in-batch negative, temperature](02. 이미지와 텍스트를 같은 공간에 맞추기/07. CLIP objective, in-batch negative, temperature/index.md)
  - [08. hard negative, retrieval, ranking](02. 이미지와 텍스트를 같은 공간에 맞추기/08. hard negative, retrieval, ranking/index.md)
  - [09. captioning, matching, contrastive objective 조합](02. 이미지와 텍스트를 같은 공간에 맞추기/09. captioning, matching, contrastive objective 조합/index.md)
  - [10. data mixture, web-scale data, curriculum](02. 이미지와 텍스트를 같은 공간에 맞추기/10. data mixture, web-scale data, curriculum/index.md)
  - [문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기](02. 이미지와 텍스트를 같은 공간에 맞추기/문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
- [03. Connector와 VLM 아키텍처](03. VLM 아키텍처와 정보 흐름/index.md)
  - [11. encoder-decoder, decoder-only, fusion map](03. VLM 아키텍처와 정보 흐름/11. encoder-decoder, decoder-only, fusion map/index.md)
  - [12. cross-attention, perceiver resampler, Q-Former](03. VLM 아키텍처와 정보 흐름/12. cross-attention, perceiver resampler, Q-Former/index.md)
  - [13. prefix tuning, visual prompt, frozen LM](03. VLM 아키텍처와 정보 흐름/13. prefix tuning, visual prompt, frozen LM/index.md)
  - [14. token compression, memory, long context](03. VLM 아키텍처와 정보 흐름/14. token compression, memory, long context/index.md)
  - [15. representative VLM families 비교](03. VLM 아키텍처와 정보 흐름/15. representative VLM families 비교/index.md)
  - [문제 해설 - 03. VLM 아키텍처와 정보 흐름](03. VLM 아키텍처와 정보 흐름/문제 해설 - 03. VLM 아키텍처와 정보 흐름/index.md)
- [04. Grounding, OCR, structured visual reasoning](04. Grounding, OCR, region reasoning/index.md)
  - [16. OCR, document understanding, chart understanding](04. Grounding, OCR, region reasoning/16. OCR, document understanding, chart understanding/index.md)
  - [17. box, mask, region token, spatial reference](04. Grounding, OCR, region reasoning/17. box, mask, region token, spatial reference/index.md)
  - [18. referring expression, region reasoning, counting](04. Grounding, OCR, region reasoning/18. referring expression, region reasoning, counting/index.md)
  - [19. multimodal chain-of-thought와 visual reasoning](04. Grounding, OCR, region reasoning/19. multimodal chain-of-thought와 visual reasoning/index.md)
  - [20. grounding failure와 hallucination의 구조](04. Grounding, OCR, region reasoning/20. grounding failure와 hallucination의 구조/index.md)
  - [문제 해설 - 04. Grounding, OCR, region reasoning](04. Grounding, OCR, region reasoning/문제 해설 - 04. Grounding, OCR, region reasoning/index.md)
- [05. 멀티모달 tuning, preference, safety](05. 멀티모달 생성과 instruction tuning/index.md)
  - [21. captioning, VQA, conditional generation](05. 멀티모달 생성과 instruction tuning/21. captioning, VQA, conditional generation/index.md)
  - [22. supervised fine-tuning과 multimodal instruction data](05. 멀티모달 생성과 instruction tuning/22. supervised fine-tuning과 multimodal instruction data/index.md)
  - [23. preference learning, reward model, RLHF](05. 멀티모달 생성과 instruction tuning/23. preference learning, reward model, RLHF/index.md)
  - [24. DPO, rejection sampling, policy alignment](05. 멀티모달 생성과 instruction tuning/24. DPO, rejection sampling, policy alignment/index.md)
  - [25. safety policy, refusal, jailbreak 대응](05. 멀티모달 생성과 instruction tuning/25. safety policy, refusal, jailbreak 대응/index.md)
  - [문제 해설 - 05. 멀티모달 생성과 instruction tuning](05. 멀티모달 생성과 instruction tuning/문제 해설 - 05. 멀티모달 생성과 instruction tuning/index.md)
- [06. 평가, faithfulness, hallucination 완화](06. 평가, 신뢰성, hallucination 완화/index.md)
  - [26. benchmark, leaderboard, evaluation protocol](06. 평가, 신뢰성, hallucination 완화/26. benchmark, leaderboard, evaluation protocol/index.md)
  - [27. hallucination taxonomy와 faithfulness](06. 평가, 신뢰성, hallucination 완화/27. hallucination taxonomy와 faithfulness/index.md)
  - [28. calibration, uncertainty, abstention](06. 평가, 신뢰성, hallucination 완화/28. calibration, uncertainty, abstention/index.md)
  - [29. data filtering, verifier, retrieval grounding](06. 평가, 신뢰성, hallucination 완화/29. data filtering, verifier, retrieval grounding/index.md)
  - [30. human evaluation과 product metric](06. 평가, 신뢰성, hallucination 완화/30. human evaluation과 product metric/index.md)
  - [문제 해설 - 06. 평가, 신뢰성, hallucination 완화](06. 평가, 신뢰성, hallucination 완화/문제 해설 - 06. 평가, 신뢰성, hallucination 완화/index.md)
- [07. 비디오, 음성, RAG, 에이전트 시스템](07. 비디오, 음성, 에이전트로 확장/index.md)
  - [31. video token, frame sampling, temporal modeling](07. 비디오, 음성, 에이전트로 확장/31. video token, frame sampling, temporal modeling/index.md)
  - [32. speech, audio, spoken dialogue extension](07. 비디오, 음성, 에이전트로 확장/32. speech, audio, spoken dialogue extension/index.md)
  - [33. multimodal RAG, memory, tool use](07. 비디오, 음성, 에이전트로 확장/33. multimodal RAG, memory, tool use/index.md)
  - [34. GUI agent, robotics, embodied reasoning](07. 비디오, 음성, 에이전트로 확장/34. GUI agent, robotics, embodied reasoning/index.md)
  - [35. latency, serving, cost optimization](07. 비디오, 음성, 에이전트로 확장/35. latency, serving, cost optimization/index.md)
  - [문제 해설 - 07. 비디오, 음성, 에이전트로 확장](07. 비디오, 음성, 에이전트로 확장/문제 해설 - 07. 비디오, 음성, 에이전트로 확장/index.md)
- [08. Frontier VLM과 최신 논문 독해](08. Frontier VLM과 최신 논문 독해/index.md)
  - [36. multimodal diffusion과 unified model](08. Frontier VLM과 최신 논문 독해/36. multimodal diffusion과 unified model/index.md)
  - [37. mixture-of-experts, adaptive compute, token routing](08. Frontier VLM과 최신 논문 독해/37. mixture-of-experts, adaptive compute, token routing/index.md)
  - [38. world model, simulation, action-conditioned model](08. Frontier VLM과 최신 논문 독해/38. world model, simulation, action-conditioned model/index.md)
  - [39. open-source VLM ecosystem과 실험 설계](08. Frontier VLM과 최신 논문 독해/39. open-source VLM ecosystem과 실험 설계/index.md)
  - [40. 최신 VLM 논문 독해 프레임워크](08. Frontier VLM과 최신 논문 독해/40. 최신 VLM 논문 독해 프레임워크/index.md)
  - [문제 해설 - 08. Frontier VLM과 최신 논문 독해](08. Frontier VLM과 최신 논문 독해/문제 해설 - 08. Frontier VLM과 최신 논문 독해/index.md)
