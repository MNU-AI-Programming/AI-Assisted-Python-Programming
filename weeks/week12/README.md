# Week 12. 탐색적 데이터 분석과 프로젝트 기획

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/practice.ipynb)

## 학습 목표

- 질문 → 데이터 이해 → 단변량 → 이변량·그룹 비교 → 발견 정리의 EDA 절차로 분석한다.
- 한 행의 의미와 집계 단위(건수·수량·매출)를 구분하고, 날짜·시각 파생 변수를 만든다.
- 그룹마다 일수가 다를 때 일평균으로 비교하고, 두 데이터를 합쳐 관계를 보되 상관과 인과를 구분한다.
- AI의 분석 문장을 계산으로 검증하고, 최종 프로젝트 연구 질문과 제안서를 작성한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 캠퍼스 카페 판매 EDA (`cafe_sales.csv` + `weather_daily.csv`)
- **산출물**: 발견 정리표와 최종 프로젝트 제안서 초안

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | EDA 절차, 한 행의 의미, 집계 단위 |
| 안내 실습 | 45분 | 파생 변수, 메뉴·요일·시간대·시험 기간 비교 |
| 독립·짝 실습 | 35분 | 기온과 판매 합쳐 보기, AI 해석 검증 |
| 공유·점검 | 20분 | 연구 질문 다듬기, 제안서 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~7 | 1. EDA 절차와 데이터 이해 | 오늘의 질문, 한 행의 의미, 집계 단위 |
| 8 | 2. 파생 변수 | .dt, pd.cut, 순서 있는 Categorical |
| 9~11 | 3. 단변량·그룹 비교 | 메뉴 세 기준, 요일×시간대 일평균, 시험 기간 |
| 12~15 | 4. Level 3 두 데이터 합치기 | 기온과 아이스 비율·매출, 상관 ≠ 인과, 발견 정리 |
| 16~17 | 5. Level 4 AI 해석 검증 | 과장·합계 비교·인과 주장 검증 |
| 18~21 | 6. 최종 프로젝트 기획 | 좋은 연구 질문, 데이터 후보, 제안서 |

## 사용하는 데이터

- [`cafe_sales.csv`](../../datasets/cafe_sales.csv)
- [`weather_daily.csv`](../../datasets/weather_daily.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 시간 파생 변수 만들기 | 2 |
| 2 | 요일 × 시간대 일평균 매출표 | 2 |
| 3 | 메뉴 매출 비중과 상위 80% 메뉴 | 3 |
| 4 | 기온 구간 분석 (AI 협업) + 프로젝트 제안서 | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
