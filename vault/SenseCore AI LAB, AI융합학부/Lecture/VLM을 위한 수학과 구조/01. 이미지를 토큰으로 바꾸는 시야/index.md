---
title: "01. VLM의 시각 표현과 토큰화"
source_kind: page
---
이 단계는 `AI를 위한 수학`에서 다루지 않은 VLM 고유 시각 병목을 여는 출발 단계입니다. 여기서는 이미지 일반론을 다시 설명하는 것이 아니라, VLM에서 왜 고해상도 입력과 token budget, connector 병목이 핵심 문제가 되는지에 집중합니다.

# 이 단계에서 배우는 것
- VLM이 vision token을 만들 때 어디서 정보가 사라지는지 배운다.
- backbone 선택이 OCR, grounding, document 이해에 어떤 차이를 만드는지 읽는다.
- resolution, stride, pooling이 token budget과 faithfulness에 어떤 영향을 주는지 본다.
- projector와 connector가 왜 단순 연결층이 아니라 핵심 병목인지 이해한다.

# 먼저 알고 갈 말
- 이 단계는 CNN과 ViT 입문이 아니라, `VLM용 시각 표현`을 읽는 단계입니다.
- 토큰 예산: 한 번에 모델이 처리하는 토큰 수와 계산량의 한계입니다.
- backbone: 상위 VLM이 기대는 기본 vision encoder입니다.
- connector: vision 쪽 표현을 language 쪽 표현과 이어 주는 다리입니다.

# 이 단계를 읽는 순서
- 1강에서는 시각 입력이 VLM용 token으로 바뀌는 병목을 만든다.
- 2강에서는 ViT 계열 backbone과 positional structure를 VLM 과제 관점에서 읽는다.
- 3강에서는 해상도, stride, pooling이 OCR와 grounding을 어떻게 바꾸는지 본다.
- 4강에서는 projector, adapter, connector를 VLM의 첫 구조 선택으로 정리한다.
- 5강에서는 backbone pretraining과 domain transfer가 실제 VLM 품질에 미치는 영향을 본다.

# 각 강의가 맡는 역할
- 1. pixel, patch, feature map, vision token: VLM용 시각 토큰화의 출발점.
- 2. CNN, ViT, positional structure: backbone inductive bias가 VLM 품질에 미치는 영향.
- 3. resolution, stride, pooling, token budget: OCR와 grounding을 좌우하는 토큰 예산 문제.
- 4. projector, adapter, connector: vision과 language를 잇는 첫 병목 읽기.
- 5. vision backbone pretraining과 transfer: VLM의 domain transfer와 backbone 전략 이해.

# 이 단계를 읽을 때 기억할 점
- 이 단계는 vision 일반론이 아니라 VLM 특화 시각 표현론입니다.
- 좋은 backbone은 단순 정확도뿐 아니라 downstream OCR와 grounding 품질과도 연결됩니다.
- connector는 사소한 부품이 아니라 전체 VLM 표현 품질을 좌우하는 병목이 될 수 있습니다.

# 이 단계를 마치면 할 수 있는 것
- 어떤 vision encoder가 어떤 형태의 토큰을 내고 무엇을 잃는지 설명할 수 있다.
- token budget과 resolution trade-off를 VLM 과제 기준으로 말할 수 있다.
- projector와 connector가 왜 VLM에서 첫 병목인지 구조 관점에서 설명할 수 있다.

# 문제 해설과 강의 목록
- 이 단계의 연습문제 해설은 맨 아래 해설 페이지에 모아 둡니다.

[1. pixel, patch, feature map, vision token](1. pixel, patch, feature map, vision token/index.md)
[2. CNN, ViT, positional structure](2. CNN, ViT, positional structure/index.md)
[3. resolution, stride, pooling, token budget](3. resolution, stride, pooling, token budget/index.md)
[4. projector, adapter, connector](4. projector, adapter, connector/index.md)
[5. vision backbone pretraining과 transfer](5. vision backbone pretraining과 transfer/index.md)
[문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야](문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야/index.md)

## Page Tree

- [1. pixel, patch, feature map, vision token](1. pixel, patch, feature map, vision token/index.md)
- [2. CNN, ViT, positional structure](2. CNN, ViT, positional structure/index.md)
- [3. resolution, stride, pooling, token budget](3. resolution, stride, pooling, token budget/index.md)
- [4. projector, adapter, connector](4. projector, adapter, connector/index.md)
- [5. vision backbone pretraining과 transfer](5. vision backbone pretraining과 transfer/index.md)
- [문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야](문제 해설 - 01. 이미지를 토큰으로 바꾸는 시야/index.md)
