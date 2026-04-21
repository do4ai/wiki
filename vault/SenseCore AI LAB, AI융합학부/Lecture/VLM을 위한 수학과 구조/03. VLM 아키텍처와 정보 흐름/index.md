---
title: "03. VLM 아키텍처와 정보 흐름"
source_kind: page
---
# 이 단계에서 배우는 것
- VLM에서 정보가 언제 결합되는지에 따라 구조가 어떻게 갈리는지 봅니다.
- cross-attention, Q-Former, resampler가 해결하는 연결 문제를 읽습니다.
- decoder-only VLM과 visual prompt 계열 설계를 비교합니다.

# 먼저 알고 갈 말
- early fusion: 비교적 이른 층부터 모달을 함께 섞는 방식입니다.
- late fusion: 각 모달을 별도로 처리한 뒤 늦게 결합하는 방식입니다.
- cross-attention: 한 모달의 query가 다른 모달의 key/value를 읽는 attention입니다.
- Q-Former: 시각 정보를 언어모델에 전달하기 위한 질의 기반 압축 구조입니다.
- visual prompt: 이미지 정보를 프롬프트처럼 언어모델 앞단에 주입하는 방식입니다.

# 이 단계를 읽는 순서
1. 먼저 fusion 설계 지형을 봅니다.
2. 그다음 cross-attention과 Q-Former 계열 연결기를 이해합니다.
3. 마지막으로 decoder-only VLM과 prompt 기반 설계를 비교합니다.

# 각 강의가 맡는 역할
- 7. early fusion, late fusion, encoder-decoder: VLM 구조 지형도를 설명합니다.
- 8. cross-attention, Q-Former, resampler: 대표 연결기들의 목적을 비교합니다.
- 9. decoder-only VLM, prefix tuning, visual prompt: 최근 경량 결합 방식을 정리합니다.

# 이 단계를 마치면 할 수 있는 것
- 새로운 VLM 논문을 볼 때 먼저 fusion point를 찾을 수 있습니다.
- connector가 단순 선형층인지, 질의 기반 모듈인지, prompt 주입형인지 구별할 수 있습니다.
- encoder-decoder와 decoder-only 접근의 장단점을 과제 기준으로 설명할 수 있습니다.

# 강의 목록
[7. early fusion, late fusion, encoder-decoder](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/7-early-fusion-late-fusion-encoder-decoder)
[8. cross-attention, Q-Former, resampler](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/8-cross-attention-q-former-resampler)
[9. decoder-only VLM, prefix tuning, visual prompt](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/9-decoder-only-vlm-prefix-tuning-visual-prompt)

## Page Tree

- [7. early fusion, late fusion, encoder-decoder](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/7-early-fusion-late-fusion-encoder-decoder)
- [8. cross-attention, Q-Former, resampler](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/8-cross-attention-q-former-resampler)
- [9. decoder-only VLM, prefix tuning, visual prompt](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/03-vlm-아키텍처와-정보-흐름/9-decoder-only-vlm-prefix-tuning-visual-prompt)
