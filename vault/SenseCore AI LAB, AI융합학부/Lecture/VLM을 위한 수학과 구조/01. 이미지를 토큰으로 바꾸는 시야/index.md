---
title: "01. 이미지를 토큰으로 바꾸는 시야"
source_kind: page
---
# 이 단계에서 배우는 것
- 이미지를 patch와 feature map, token 시퀀스로 바꾸는 관점을 잡습니다.
- CNN과 ViT가 어떤 방식으로 시각 표현을 만드는지 비교합니다.
- projector, adapter, connector가 왜 VLM의 첫 관문인지 설명합니다.

# 먼저 알고 갈 말
- pixel: 원본 이미지의 가장 작은 값 단위입니다.
- patch: 이미지를 일정 크기 블록으로 나눈 단위입니다.
- feature map: 인코더가 추출한 중간 표현입니다.
- vision token: language model과 결합하기 좋도록 만든 시각 토큰 표현입니다.
- connector: vision encoder와 language model 사이를 이어 주는 모듈입니다.

# 이 단계를 읽는 순서
1. 패치와 토큰 표현을 먼저 이해합니다.
2. 그다음 CNN과 ViT의 표현 방식을 비교합니다.
3. 마지막으로 projector와 adapter가 왜 필요한지 봅니다.

# 각 강의가 맡는 역할
- 1. 패치, feature map, vision token: 이미지가 시퀀스로 읽히는 기본 관점을 설명합니다.
- 2. CNN, ViT, vision encoder 비교: 시각 인코더의 대표 구조를 비교합니다.
- 3. projector, adapter, connector: 시각 표현을 언어모델 입력에 맞추는 연결 문제를 다룹니다.

# 이 단계를 마치면 할 수 있는 것
- 이미지 표현이 language model 쪽 토큰과 어떻게 연결될 수 있는지 설명할 수 있습니다.
- vision encoder의 출력이 단순 벡터 하나가 아니라 시퀀스라는 사실을 자연스럽게 읽을 수 있습니다.
- connector가 없는 VLM 설계가 왜 곧바로 성립하지 않는지 말할 수 있습니다.

# 강의 목록
[1. 패치, feature map, vision token](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/1-패치-feature-map-vision-token)
[2. CNN, ViT, vision encoder 비교](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/2-cnn-vit-vision-encoder-비교)
[3. projector, adapter, connector](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/3-projector-adapter-connector)

## Page Tree

- [1. 패치, feature map, vision token](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/1-패치-feature-map-vision-token)
- [2. CNN, ViT, vision encoder 비교](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/2-cnn-vit-vision-encoder-비교)
- [3. projector, adapter, connector](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/01-이미지를-토큰으로-바꾸는-시야/3-projector-adapter-connector)
