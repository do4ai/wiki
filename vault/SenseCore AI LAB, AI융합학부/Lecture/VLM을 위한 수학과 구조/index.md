---
title: "VLM을 위한 수학과 구조"
source_kind: page
---
# VLM을 위한 수학과 구조
이 책은 [AI를 위한 수학](../AI를 위한 수학/index.md)의 8단계에서 다룬 VLM, 멀티모달 생성, grounding 주제를 별도 교재로 깊게 파기 위한 초안입니다. 목표는 VLM을 단순히 "이미지와 텍스트를 함께 넣는 모델"로 보는 수준을 넘어서, 이미지 표현이 토큰으로 바뀌고, 텍스트와 정렬되고, 생성 구조 안에서 결합되고, grounding과 평가 문제까지 이어지는 전체 흐름을 하나의 구조로 읽게 만드는 것입니다.

# 이 책의 목표
- 이미지를 feature map, patch, token으로 바꾸는 수학적 표현을 익힙니다.
- CLIP과 contrastive learning에서 출발해 shared embedding space를 이해합니다.
- projector, cross-attention, Q-Former, resampler 같은 연결 구조를 읽습니다.
- grounding, OCR, hallucination, faithfulness 같은 실제 품질 문제를 설명할 수 있게 합니다.
- VLM이 비디오, 생성, 에이전트 시스템으로 확장되는 방향을 구조 관점에서 정리합니다.

# 이 책이 필요한 이유
- `AI를 위한 수학` 본편은 큰 흐름과 핵심 수학을 잡는 데 초점을 둡니다.
- 하지만 VLM은 비전 인코더, 멀티모달 정렬, 생성 구조, 평가 체계까지 각각이 독립 교재가 될 정도로 넓습니다.
- 그래서 이 책은 본편을 반복하지 않고, VLM에만 필요한 구조와 수학을 한 층 더 깊게 이어서 다룹니다.

# 이 책을 읽는 방법
- 먼저 [AI를 위한 수학](../AI를 위한 수학/index.md)의 2, 5, 7, 8단계를 읽는 것이 좋습니다.
- 식이 나오면 먼저 "어떤 모달의 어떤 표현이 어디로 이동하는가"를 말로 읽습니다.
- 아키텍처 이름을 외우기보다 정보 흐름을 먼저 잡습니다.
- 같은 주제를 정렬, 생성, 평가 세 관점에서 반복해 읽습니다.
- 각 강의의 마지막 질문에 답할 수 있을 때 다음 강의로 넘어갑니다.

# 이 책의 읽는 순서
1. 이미지를 토큰으로 바꾸는 시야
2. 이미지와 텍스트를 같은 공간에 맞추기
3. VLM 아키텍처와 정보 흐름
4. Grounding, OCR, 멀티모달 정렬
5. 비디오, 생성, 에이전트로 확장

이 순서는 VLM을 구성 부품별로 쪼개기보다, 표현에서 정렬로, 정렬에서 결합으로, 결합에서 품질과 응용으로 흐르도록 배치했습니다.

# 각 단계에서 무엇을 배우는가
## 1단계. 이미지를 토큰으로 바꾸는 시야
- 이미지가 patch, feature map, token 시퀀스로 바뀌는 과정을 배웁니다.
- CNN과 ViT가 어떤 방식으로 시각 표현을 만드는지 비교합니다.
- projector, adapter, connector가 왜 필요한지 설명합니다.

## 2단계. 이미지와 텍스트를 같은 공간에 맞추기
- CLIP의 contrastive learning이 shared embedding space를 어떻게 만드는지 봅니다.
- temperature, negative sampling, retrieval 품질이 왜 중요한지 이해합니다.
- multimodal pretraining objective와 data mixture의 역할을 정리합니다.

## 3단계. VLM 아키텍처와 정보 흐름
- early fusion, late fusion, encoder-decoder 구조를 비교합니다.
- cross-attention, Q-Former, resampler가 어떤 연결 문제를 해결하는지 읽습니다.
- decoder-only VLM, visual prompt, prefix 방식이 어떻게 동작하는지 설명합니다.

## 4단계. Grounding, OCR, 멀티모달 정렬
- region reasoning, OCR, grounding이 실제 정답성과 어떻게 연결되는지 봅니다.
- hallucination과 faithfulness를 평가하는 관점을 정리합니다.
- multimodal instruction tuning과 alignment를 텍스트-only alignment와 비교합니다.

## 5단계. 비디오, 생성, 에이전트로 확장
- video token과 temporal modeling으로 시각 문맥이 시간축으로 늘어나는 방식을 설명합니다.
- multimodal RAG, tool use, agent loop가 왜 VLM 다음 단계인지 정리합니다.
- diffusion과 unified multimodal model이 생성 쪽으로 구조를 어떻게 넓히는지 봅니다.

# 모든 강의가 따르는 공통 순서
- 먼저 어떤 입력과 출력이 오가는지 문제를 세웁니다.
- 그다음 각 모듈이 어떤 표현을 주고받는지 정리합니다.
- 그다음 필요한 수식과 손실을 붙입니다.
- 마지막에 실제 사용 장면과 실패 사례를 연결합니다.

# 읽기 전에 기억할 약속
- 아키텍처 이름보다 정보 흐름이 먼저입니다.
- 이미지는 "큰 덩어리"가 아니라 시퀀스로 읽습니다.
- 좋은 정답은 유창함만이 아니라 grounding을 요구합니다.
- retrieval, OCR, generation, agent를 따로 떼지 말고 연결된 문제로 봅니다.
- 이 책의 목적은 모델 이름 암기가 아니라 구조를 읽는 습관입니다.

# 이 책을 마치면
이 책을 끝내면 어떤 VLM을 보더라도 `"vision encoder는 무엇을 내고, connector는 무엇을 바꾸고, language model은 어느 시점에 어떤 시각 정보를 읽는가"`를 먼저 묻는 습관이 생겨야 합니다. 더 나아가 contrastive alignment와 multimodal generation, grounding 평가와 hallucination 완화, 비디오와 에이전트 확장까지 하나의 수학적 흐름 안에서 연결할 수 있어야 합니다.

# 단계 목록
[01. 이미지를 토큰으로 바꾸는 시야](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야)
[02. 이미지와 텍스트를 같은 공간에 맞추기](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기)
[03. VLM 아키텍처와 정보 흐름](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름)
[04. Grounding, OCR, 멀티모달 정렬](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬)
[05. 비디오, 생성, 에이전트로 확장](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장)

## Page Tree

- [01. 이미지를 토큰으로 바꾸는 시야](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야)
  - [1. 패치, feature map, vision token](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/1-패치-feature-map-vision-token)
  - [2. CNN, ViT, vision encoder 비교](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/2-cnn-vit-vision-encoder-비교)
  - [3. projector, adapter, connector](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/3-projector-adapter-connector)
- [02. 이미지와 텍스트를 같은 공간에 맞추기](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기)
  - [4. CLIP, contrastive learning, shared embedding](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/4-clip-contrastive-learning-shared-embedding)
  - [5. hard negative, temperature, retrieval](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/5-hard-negative-temperature-retrieval)
  - [6. multimodal pretraining objective와 data mixture](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/6-multimodal-pretraining-objective와-data-mixture)
- [03. VLM 아키텍처와 정보 흐름](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름)
  - [7. early fusion, late fusion, encoder-decoder](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/7-early-fusion-late-fusion-encoder-decoder)
  - [8. cross-attention, Q-Former, resampler](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/8-cross-attention-q-former-resampler)
  - [9. decoder-only VLM, prefix tuning, visual prompt](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/9-decoder-only-vlm-prefix-tuning-visual-prompt)
- [04. Grounding, OCR, 멀티모달 정렬](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬)
  - [10. grounding, OCR, region reasoning](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/10-grounding-ocr-region-reasoning)
  - [11. hallucination, faithfulness, evaluation](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/11-hallucination-faithfulness-evaluation)
  - [12. instruction tuning, RLHF, multimodal alignment](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/12-instruction-tuning-rlhf-multimodal-alignment)
- [05. 비디오, 생성, 에이전트로 확장](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장)
  - [13. video token, temporal modeling, long context](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/13-video-token-temporal-modeling-long-context)
  - [14. multimodal RAG, tool use, agent loop](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/14-multimodal-rag-tool-use-agent-loop)
  - [15. diffusion, image generation, unified multimodal model](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/15-diffusion-image-generation-unified-multimodal-model)
