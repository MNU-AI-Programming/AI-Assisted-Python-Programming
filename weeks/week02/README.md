# Week 02. 입력 · 계산 · 문자열

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/practice.ipynb)

## 학습 목표

- 산술 연산자 `//`, `%`, `**`와 연산 우선순위로 생활 문제를 계산한다.
- 실수 비교와 반올림의 함정을 이해하고, 돈 계산에서 올림·내림 규칙을 명시한다.
- 문자열 인덱싱·슬라이싱과 `strip`, `split`, `replace`, `join` 등으로 입력을 가공한다.
- 입력 → 처리 → 출력으로 나눈 프로그램을 만들고, AI 정산 코드를 불변 조건으로 검증한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 여행 경비 계산기와 정산 규칙 검증
- **산출물**: 입력과 계산을 분리한 생활 문제 계산기

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 연산자와 우선순위, 실수의 함정, 문자열 메서드 |
| 안내 실습 | 45분 | 단위 변환, 반올림 실험, 학번 슬라이싱, 입력 정리 |
| 독립·짝 실습 | 35분 | 시간 변환기, 여행 경비 계산기 |
| 공유·점검 | 20분 | AI 정산 코드 검증 결과 공유, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~10 | 1. Level 1 산술 연산 | 우선순위 예상, divmod, 실수 비교, 올림·내림 |
| 11~14 | 2. Level 1 문자열 다루기 | 슬라이싱, 메서드, 금액 문자열 변환 |
| 15 | 3. Level 2 바꾸기 | 시간 변환기, 이메일 정리 |
| 16~17 | 4. Level 3 여행 경비 계산기 | 입력 → 처리 → 출력, 검증 |
| 18~21 | 5. Level 4 AI 정산 코드 검증 | 반올림 버그 발견, 규칙 명시, 불변 조건 |

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 초를 `HH:MM:SS`로 바꾸기 | 2 |
| 2 | 학번 분석하기 | 2 |
| 3 | 영수증 문자열 만들기 | 3 |
| 4 | 정확한 정산 함수 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
