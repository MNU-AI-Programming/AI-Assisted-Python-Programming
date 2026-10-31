# Week 10. pandas로 데이터 불러오기와 탐색

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/practice.ipynb)

## 학습 목표

- `Series`와 `DataFrame`의 구조(값·인덱스·열·자료형)를 설명한다.
- `read_csv`와 `head`·`info`·`describe`·`isna`·`value_counts`로 데이터의 구조와 품질을 탐색한다.
- 열 선택, `loc`/`iloc`, 조건 필터, 다중 정렬, 새 열 만들기로 질문에 답한다.
- 8주차 결과를 pandas로 재현해 대조하고, AI 코드의 `and` 오류·체인 인덱싱·count/size 혼동을 찾아낸다.

## 이번 주 실습과 산출물

- **핵심 실습**: 성적 데이터 탐색 보고 (질문 5개)
- **산출물**: 데이터 구조·품질·기초통계 탐색 결과와 8주차 결과 대조

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | DataFrame 구조, 탐색 5종 세트, 8주차와 비교 |
| 안내 실습 | 45분 | 읽기·탐색·선택·필터·정렬·새 열 |
| 독립·짝 실습 | 35분 | 성적 데이터 탐색 보고 (질문 5개) |
| 공유·점검 | 20분 | pandas 함정 2가지와 체크리스트, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~7 | 1~2. Series·DataFrame, 읽기와 첫 탐색 | 구조 확인, info로 결측 찾기 |
| 8~12 | 3. 선택·필터·정렬·새 열 | loc/iloc, & | 필터, 다중 정렬, pd.cut |
| 13 | 4. Level 2 바꾸기 | 조건·정렬 기준 바꾸기, 향상 점수 열 |
| 14~17 | 5. Level 3 탐색 보고 | 질문 5개, groupby 맛보기, 상관과 결측 |
| 18~20 | 6. Level 4 pandas 함정 | and 오류, 체인 인덱싱, 체크리스트 |

## 사용하는 데이터

- [`students.csv`](../../datasets/students.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 데이터 개요 함수 | 2 |
| 2 | 조건 필터와 정렬 | 2 |
| 3 | 총점·등급 열 추가 | 3 |
| 4 | 학과별 탐색 보고 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
