---
title: "05. 비디오, 생성, 에이전트로 확장"
source_kind: page
---
# 이 단계에서 배우는 것
- 이미지 VLM이 비디오 이해로 확장될 때 시간축 문제가 어떻게 생기는지 봅니다.
- multimodal RAG와 tool use가 왜 VLM 이후의 시스템 문제인지 정리합니다.
- diffusion과 unified multimodal model이 생성 방향에서 어떤 연결을 만드는지 설명합니다.

# 먼저 알고 갈 말
- temporal modeling: 시간 순서가 있는 시각 정보를 처리하는 방법입니다.
- long context: 매우 긴 토큰 시퀀스를 다루는 문맥 문제입니다.
- multimodal RAG: 외부 지식 검색을 이미지, 텍스트와 함께 결합하는 방식입니다.
- tool use: 모델이 외부 도구 호출을 포함해 문제를 푸는 방식입니다.
- unified model: 여러 모달과 여러 작업을 하나의 모델 안에서 처리하려는 접근입니다.

# 이 단계를 읽는 순서
1. 먼저 비디오 토큰과 시간축 문제를 봅니다.
2. 그다음 multimodal RAG와 agent loop를 이해합니다.
3. 마지막으로 diffusion과 통합 생성 모델 방향을 정리합니다.

# 각 강의가 맡는 역할
- 13. video token, temporal modeling, long context: 시간축이 추가될 때 생기는 구조 변화를 설명합니다.
- 14. multimodal RAG, tool use, agent loop: 시스템 관점에서 VLM의 다음 단계를 다룹니다.
- 15. diffusion, image generation, unified multimodal model: 생성 모델과 통합 모델 방향을 연결합니다.

# 이 단계를 마치면 할 수 있는 것
- 정적인 이미지 VLM과 비디오/에이전트 시스템의 차이를 구조적으로 설명할 수 있습니다.
- 검색과 도구 호출이 붙을 때 모델 문제가 시스템 문제로 확장된다는 점을 말할 수 있습니다.
- unified multimodal model이 왜 연구적으로 매력적이면서도 어려운지 정리할 수 있습니다.

# 강의 목록
[13. video token, temporal modeling, long context](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/13-video-token-temporal-modeling-long-context)
[14. multimodal RAG, tool use, agent loop](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/14-multimodal-rag-tool-use-agent-loop)
[15. diffusion, image generation, unified multimodal model](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/15-diffusion-image-generation-unified-multimodal-model)

## Page Tree

- [13. video token, temporal modeling, long context](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/13-video-token-temporal-modeling-long-context)
- [14. multimodal RAG, tool use, agent loop](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/14-multimodal-rag-tool-use-agent-loop)
- [15. diffusion, image generation, unified multimodal model](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/05-비디오-생성-에이전트로-확장/15-diffusion-image-generation-unified-multimodal-model)
