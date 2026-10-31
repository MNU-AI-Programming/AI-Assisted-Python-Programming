# Week 11. 데이터 정제 · 변환 · 집계

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/practice.ipynb)

## 학습 목표

- 지저분한 데이터의 중복·표기 불일치·단위 혼재·결측·이상값을 진단해 정제 계획 표로 정리한다.
- `.str` 메서드와 정규식, `replace`/`map`, `to_numeric`, `to_datetime`, `where`/`clip`으로 데이터를 정제한다.
- 정제 단계를 파이프라인 함수로 묶고 정제 전후 비교표와 테스트로 검증한다.
- `groupby().agg()`, `pivot_table`, `crosstab`, `merge`, `cut`으로 집계하고, AI 정제 코드의 순서·결측 처리 문제를 찾는다.

## 이번 주 실습과 산출물

- **핵심 실습**: 설문 데이터 정제 파이프라인 (`survey_raw.csv` + `departments.csv`)
- **산출물**: 정제 함수, 정제 전후 비교표, 학과·단과대학·학년별 집계표

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 지저분한 데이터 진단과 정제 계획 표 |
| 안내 실습 | 45분 | 정제 도구와 파이프라인 함수, 전후 비교 |
| 독립·짝 실습 | 35분 | groupby·pivot_table·merge·cut 집계 |
| 공유·점검 | 20분 | AI 정제 코드의 순서·결측 처리 문제, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~7 | 1. 진단 | value_counts·unique·duplicated, 정제 계획 표 |
| 8~11 | 2. 정제 도구 | .str·정규식, replace vs map, to_numeric·to_datetime, where vs clip |
| 12 | 3. Level 2 바꾸기 | map 누락 찾기, 상한 바꾸기, where·clip 비교 |
| 13~15 | 4. Level 3 정제 파이프라인 | clean_survey, 전후 비교표, 테스트 |
| 16~19 | 5. 집계 | agg, pivot_table·crosstab, merge(validate), cut |
| 20~22 | 6. Level 4 AI 정제 코드 | 정제 순서, 열 성격에 맞는 결측 처리 |

## 사용하는 데이터

- [`survey_raw.csv`](../../datasets/survey_raw.csv)
- [`departments.csv`](../../datasets/departments.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 학과명 표준화 | 2 |
| 2 | 코딩 시간 숫자 변환과 이상값 | 2 |
| 3 | 설문 정제 파이프라인 | 3 |
| 4 | 단과대학 요약과 피벗 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
