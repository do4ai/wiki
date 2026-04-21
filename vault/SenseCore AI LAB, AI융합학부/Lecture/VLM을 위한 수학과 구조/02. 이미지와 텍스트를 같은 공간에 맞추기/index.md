---
title: "02. 이미지와 텍스트를 같은 공간에 맞추기"
source_kind: page
---
# 이 단계에서 배우는 것
- CLIP과 contrastive learning이 shared embedding space를 어떻게 만드는지 봅니다.
- retrieval 품질과 temperature, negative sampling의 역할을 설명합니다.
- multimodal pretraining objective와 data mixture가 왜 성능을 좌우하는지 정리합니다.

# 먼저 알고 갈 말
- shared embedding: 이미지와 텍스트를 함께 놓는 공통 표현 공간입니다.
- positive pair: 서로 대응되는 이미지-텍스트 쌍입니다.
- negative pair: 대응되지 않는 쌍입니다.
- temperature: contrastive loss의 분포 sharpness를 조절하는 값입니다.
- retrieval: 한 모달에서 다른 모달의 대응 항목을 찾아오는 문제입니다.

# 이 단계를 읽는 순서
1. 먼저 CLIP의 기본 loss와 shared space를 이해합니다.
2. 그다음 retrieval 품질을 좌우하는 negative와 temperature를 봅니다.
3. 마지막으로 대규모 pretraining objective와 데이터 혼합 전략을 정리합니다.

# 각 강의가 맡는 역할
- 4. CLIP, contrastive learning, shared embedding: 이미지와 텍스트 정렬의 기준점을 세웁니다.
- 5. hard negative, temperature, retrieval: 정렬 성능을 좌우하는 학습 세부를 설명합니다.
- 6. multimodal pretraining objective와 data mixture: 실제 대규모 멀티모달 사전학습 설계를 다룹니다.

# 이 단계를 마치면 할 수 있는 것
- CLIP류 모델의 목적함수를 말로 읽을 수 있습니다.
- retrieval 성능과 contrastive training 안정성이 왜 이어지는지 설명할 수 있습니다.
- 데이터 설계가 아키텍처만큼 중요하다는 점을 구체적으로 말할 수 있습니다.

# 강의 목록
[4. CLIP, contrastive learning, shared embedding](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/4-clip-contrastive-learning-shared-embedding)
[5. hard negative, temperature, retrieval](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/5-hard-negative-temperature-retrieval)
[6. multimodal pretraining objective와 data mixture](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/6-multimodal-pretraining-objective와-data-mixture)

## Page Tree

- [4. CLIP, contrastive learning, shared embedding](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/4-clip-contrastive-learning-shared-embedding)
- [5. hard negative, temperature, retrieval](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/5-hard-negative-temperature-retrieval)
- [6. multimodal pretraining objective와 data mixture](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/02-이미지와-텍스트를-같은-공간에-맞추기/6-multimodal-pretraining-objective와-data-mixture)
