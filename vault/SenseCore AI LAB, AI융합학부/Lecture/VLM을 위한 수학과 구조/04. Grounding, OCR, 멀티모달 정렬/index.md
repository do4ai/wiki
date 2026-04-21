---
title: "04. Grounding, OCR, 멀티모달 정렬"
source_kind: page
---
# 이 단계에서 배우는 것
- VLM이 실제 이미지를 제대로 보고 있는지 평가하는 기준을 잡습니다.
- OCR과 region reasoning이 왜 단순 캡셔닝보다 어려운지 설명합니다.
- instruction tuning, preference alignment를 멀티모달 환경에서 다시 읽습니다.

# 먼저 알고 갈 말
- grounding: 출력이 실제 시각 입력과 연결되어 있는 성질입니다.
- OCR: 이미지 안의 텍스트를 읽는 문제입니다.
- region reasoning: 특정 영역이나 객체 관계를 기준으로 추론하는 문제입니다.
- faithfulness: 모델 답변이 입력 근거를 충실히 반영하는 정도입니다.
- multimodal alignment: 사람 선호와 시각 근거를 함께 반영하도록 맞추는 과정입니다.

# 이 단계를 읽는 순서
1. 먼저 grounding과 OCR 문제를 정리합니다.
2. 그다음 hallucination과 evaluation 관점을 봅니다.
3. 마지막으로 instruction tuning과 alignment를 멀티모달로 확장합니다.

# 각 강의가 맡는 역할
- 10. grounding, OCR, region reasoning: 정답성과 근거성의 출발점을 설명합니다.
- 11. hallucination, faithfulness, evaluation: 실패 유형과 평가 프레임을 정리합니다.
- 12. instruction tuning, RLHF, multimodal alignment: 정렬 과정을 멀티모달 환경에 맞춰 읽습니다.

# 이 단계를 마치면 할 수 있는 것
- 유창하지만 틀린 답과 실제로 grounded한 답을 구별하는 관점을 가질 수 있습니다.
- OCR과 region reasoning이 vision encoder만의 문제가 아니라 결합 구조 문제이기도 하다는 점을 설명할 수 있습니다.
- 텍스트-only alignment와 multimodal alignment의 차이를 말할 수 있습니다.

# 강의 목록
[10. grounding, OCR, region reasoning](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/10-grounding-ocr-region-reasoning)
[11. hallucination, faithfulness, evaluation](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/11-hallucination-faithfulness-evaluation)
[12. instruction tuning, RLHF, multimodal alignment](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/12-instruction-tuning-rlhf-multimodal-alignment)

## Page Tree

- [10. grounding, OCR, region reasoning](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/10-grounding-ocr-region-reasoning)
- [11. hallucination, faithfulness, evaluation](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/11-hallucination-faithfulness-evaluation)
- [12. instruction tuning, RLHF, multimodal alignment](https://wiki.do4ai.com/home/lecture/vlm을-위한-수학과-구조/04-grounding-ocr-멀티모달-정렬/12-instruction-tuning-rlhf-multimodal-alignment)
