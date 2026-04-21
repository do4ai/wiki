---
title: "02. 멀티모달 정렬과 데이터 설계"
source_kind: page
---
이 단계는 CLIP 입문을 반복하는 단계가 아니라, `VLM용 multimodal pretraining이 어떤 정렬 전략과 데이터 설계 위에 서 있는지`를 읽는 단계입니다. 여기서는 shared embedding의 일반론보다, 어떤 데이터와 어떤 objective 조합이 실제 VLM 성격을 바꾸는지를 봅니다.

# 이 단계에서 배우는 것
- VLM pretraining에서 alignment가 어떤 역할을 맡는지 배운다.
- cosine similarity와 contrastive loss를 `VLM 출발점`으로 다시 읽는다.
- retrieval과 hard negative가 세밀한 시각 구분에 왜 중요한지 이해한다.
- matching, captioning, contrastive objective의 조합이 assistant형 VLM을 어떻게 만드는지 본다.
- OCR-heavy, document-heavy, web-scale data mixture가 모델 성격을 어떻게 바꾸는지 정리한다.

# 먼저 알고 갈 말
- 이 단계는 CLIP 기본 소개를 짧게 상기한 뒤, VLM용 사전학습으로 바로 넘어갑니다.
- 정렬: 서로 다른 모달이 같은 의미를 가리키게 만드는 과정입니다.
- shared embedding: 이미지와 텍스트를 함께 놓는 공통 벡터 공간입니다.
- negative pair: 서로 대응되지 않는 샘플 쌍입니다.
- curriculum: 학습 순서와 데이터 비율을 설계하는 방식입니다.

# 이 단계를 읽는 순서
- 6강에서는 공통 표현 공간을 VLM 출발점으로 다시 정리한다.
- 7강에서는 CLIP objective와 temperature를 VLM pretraining 기준으로 읽는다.
- 8강에서는 hard negative와 retrieval를 세밀한 구분 문제와 연결한다.
- 9강에서는 여러 objective를 섞어 assistant형 VLM을 만드는 구조를 읽는다.
- 10강에서는 web-scale data와 task-specific data mixture를 비교한다.

# 각 강의가 맡는 역할
- 06. image-text pair, shared embedding, cosine similarity: 정렬 문제의 기본 좌표계 세우기.
- 07. CLIP objective, in-batch negative, temperature: contrastive learning 핵심 계산 읽기.
- 08. hard negative, retrieval, ranking: 정렬 품질과 검색 성능 연결.
- 09. captioning, matching, contrastive objective 조합: 실제 사전학습 설계 읽기.
- 10. data mixture, web-scale data, curriculum: 데이터 설계와 스케줄링 이해.

# 이 단계를 읽을 때 기억할 점
- 이 단계는 공통 alignment 이론보다 `VLM용 data design`에 더 무게를 둡니다.
- loss만 좋다고 끝나지 않고, negative의 질과 데이터 혼합 방식이 함께 중요합니다.
- 이후 generation 단계도 여기서 배운 alignment 품질과 데이터 편향의 영향을 크게 받습니다.

# 이 단계를 마치면 할 수 있는 것
- CLIP류 objective를 VLM 사전학습 출발점으로 설명할 수 있다.
- retrieval 성능과 fine-grained embedding 품질의 관계를 말할 수 있다.
- 여러 pretraining objective와 data mixture가 왜 함께 쓰이는지 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[06. image-text pair, shared embedding, cosine similarity](06. image-text pair, shared embedding, cosine similarity/index.md)
[07. CLIP objective, in-batch negative, temperature](07. CLIP objective, in-batch negative, temperature/index.md)
[08. hard negative, retrieval, ranking](08. hard negative, retrieval, ranking/index.md)
[09. captioning, matching, contrastive objective 조합](09. captioning, matching, contrastive objective 조합/index.md)
[10. data mixture, web-scale data, curriculum](10. data mixture, web-scale data, curriculum/index.md)
[문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기](문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)

## Page Tree

- [06. image-text pair, shared embedding, cosine similarity](06. image-text pair, shared embedding, cosine similarity/index.md)
- [07. CLIP objective, in-batch negative, temperature](07. CLIP objective, in-batch negative, temperature/index.md)
- [08. hard negative, retrieval, ranking](08. hard negative, retrieval, ranking/index.md)
- [09. captioning, matching, contrastive objective 조합](09. captioning, matching, contrastive objective 조합/index.md)
- [10. data mixture, web-scale data, curriculum](10. data mixture, web-scale data, curriculum/index.md)
- [문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기](문제 해설 - 02. 이미지와 텍스트를 같은 공간에 맞추기/index.md)
