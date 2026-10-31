# Week 09. NumPy와 배열 사고

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/practice.ipynb)

## 학습 목표

- 반복문 대신 배열 전체에 연산하는 벡터화와 브로드캐스팅을 이해하고 활용한다.
- 인덱싱·슬라이싱·불리언 마스크·`np.where`/`np.select`로 원하는 값을 고른다.
- `axis`를 정확히 지정해 행/열 방향으로 집계하고, `nan` 함수와 보간으로 결측값을 다룬다.
- 1년치 기온 데이터를 월별 요약·이동평균·잔차 z-점수로 분석하고, AI 코드의 axis 혼동을 shape와 작은 예제로 검증한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 1년치 기온 데이터 분석 (`weather_daily.csv`)
- **산출물**: 배열 기반 기초 통계, 월별 요약, 이동평균과 이상값 탐지

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 리스트 vs 배열, shape, 브로드캐스팅, axis |
| 안내 실습 | 45분 | 생성·연산·인덱싱·마스크·집계·NaN |
| 독립·짝 실습 | 35분 | 기온 데이터 월별 요약, 이동평균, 이상값 탐지 |
| 공유·점검 | 20분 | axis 혼동 사례와 검증 방법 공유, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5 | 1. 왜 NumPy인가? | 리스트와 배열 속도·연산 비교 |
| 6~8 | 2. 배열 만들기와 연산 | 생성, 2차원 배열, 브로드캐스팅 |
| 9~11 | 3. 인덱싱과 마스크 | [행, 열], 마스크, where·select |
| 12~14 | 4. 집계와 axis, NaN | axis 예상하기, nan 함수 |
| 15 | 5. Level 2 바꾸기 | 가중치·조건·argmin 바꾸기 |
| 16~19 | 6. Level 3 기온 데이터 | genfromtxt, 월별 요약, 보간·이동평균, 잔차 z-점수 |
| 20~22 | 7. Level 4 axis 혼동 | shape 확인과 손계산 예제 |

## 사용하는 데이터

- [`weather_daily.csv`](../../datasets/weather_daily.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 점수 행렬 요약 | 2 |
| 2 | 정규화 두 가지 | 2 |
| 3 | IQR 이상값 탐지 | 3 |
| 4 | 이동평균과 연속 상승 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
