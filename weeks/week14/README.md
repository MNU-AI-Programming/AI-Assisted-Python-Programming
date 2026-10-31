# Week 14. AI 디버깅 · 테스트 · 리팩토링

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/practice.ipynb)

## 학습 목표

- 재현 → 범위 좁히기 → 가설 → 확인 → 수정 → 회귀 테스트의 디버깅 절차를 따르고 트레이스백을 읽는다.
- 손으로 답을 알 수 있는 작은 데이터로 오류 없는 조용한 버그를 찾아낸다.
- 기대 결과를 먼저 적는 테스트로 수정과 리팩토링의 안전을 확인하고, 이름·상수·함수 추출·중복 제거로 코드를 다듬는다.
- AI에게 최소 재현·기대/실제 결과로 디버깅을 요청하고, 테스트만 통과시키는 가짜 수정을 검증으로 걸러 낸다.

## 이번 주 실습과 산출물

- **핵심 실습**: 결함 있는 주간 보고서 코드 진단과 리팩토링
- **산출물**: 버그 보고서, 회귀 테스트, 리팩토링 전후 결과 동일 확인

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 디버깅 6단계, 트레이스백, 조용한 버그 |
| 안내 실습 | 45분 | 결함 있는 주간 보고서: 작은 데이터·테스트 팩토리·수정 |
| 독립·짝 실습 | 35분 | 리팩토링, AI 디버깅과 가짜 수정 검증 |
| 공유·점검 | 20분 | 최종 프로젝트 릴리스 후보 점검표, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~6 | 1. 디버깅 절차와 트레이스백 | 트레이스백 아래에서 위로 읽기 |
| 7 | 2. 흔한 조용한 버그 | 초기화 위치 버그 재현, 중간값 출력 |
| 8~11 | 3. Level 3 결함 있는 분석 코드 | 작은 데이터, 테스트 팩토리, 버그 4개 수정 |
| 12~14 | 4. 리팩토링 | 함수 추출·상수·중복 제거, 결과 동일 assert |
| 15~17 | 5. Level 4 AI 디버깅 | 좋은 질문, 가짜 수정과 두 번째 테스트 데이터 |
| 18 | 6. 최종 프로젝트 점검 | 릴리스 후보 체크리스트 |

## 사용하는 데이터

- [`cafe_sales.csv`](../../datasets/cafe_sales.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 버그 3개 찾아 고치기 + 버그 보고서 | 2 |
| 2 | 버그를 잡는 테스트 만들기 | 3 |
| 3 | 결과는 그대로, 코드는 깔끔하게 | 3 |
| 4 | AI와 함께 pandas 버그 고치기 | 2 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
