# Week 03. 조건문과 반복문으로 흐름 제어

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/practice.ipynb)

## 학습 목표

- `if / elif / else`와 비교·논리 연산자로 여러 조건을 판정하고, 조건의 순서를 올바르게 정한다.
- `for`, `range`, `enumerate`, `while`, `break`, `continue`로 반복을 제어한다.
- 누적·개수 세기·최댓값·모으기 패턴을 조합해 여러 데이터를 요약한다.
- 경계값 표(경계·바로 아래·범위 끝·잘못된 입력)로 AI가 만든 판정 코드를 검증한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 장학 기준 판정기
- **산출물**: 여러 조건과 반복을 적용한 판정 프로그램과 경계값 테스트

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 조건 순서, 연쇄 비교, 반복 패턴 4가지 |
| 안내 실습 | 45분 | 조건 순서 실험, 중첩 조건 평평하게, break·continue·while |
| 독립·짝 실습 | 35분 | 체감 온도·구구단 바꾸기, 장학 기준 판정기 |
| 공유·점검 | 20분 | AI 학점 함수 경계값 검증 결과 공유, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~9 | 1. Level 1 조건문 | 조건 순서 예상, truthiness, early return |
| 10~14 | 2. Level 1 반복문 | range·enumerate, 반복 패턴, break·continue, while |
| 15 | 3. Level 2 바꾸기 | 경계 온도 바꾸기, 구구단 변형 |
| 16~18 | 4. Level 3 장학 기준 판정기 | 판정 함수, 경계값 검증, 여러 학생 요약 |
| 19~21 | 5. Level 4 경계값 표 | AI 학점 함수의 `>`/`>=` 버그 찾고 고치기 |

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 학점 판정과 경계값 | 2 |
| 2 | 목포대학 게임 | 2 |
| 3 | 장학 판정과 집계 | 3 |
| 4 | 저축 목표 계산기 – 무한 반복 막기 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
