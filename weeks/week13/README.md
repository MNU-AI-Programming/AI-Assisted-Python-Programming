# Week 13. matplotlib 데이터 시각화

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/practice.ipynb)

## 학습 목표

- `fig, ax = plt.subplots()` 객체지향 방식으로 선·막대·히스토그램·상자·산점도를 그린다.
- 추세·비교·분포·관계·구성 질문에 맞는 차트를 고른다.
- 결론형 제목, 단위, 강조 색, 값 표시로 메시지가 분명한 차트를 만들고 나쁜 차트를 고친다.
- 2×2 대시보드를 저장하고, AI 차트 코드를 체크리스트와 그래프 객체 자동 점검으로 검증한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 캠퍼스 카페 판매 대시보드
- **산출물**: 메시지가 분명한 차트 3종 이상과 2×2 대시보드 PNG

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | Figure·Axes 구조, 질문별 차트 선택 |
| 안내 실습 | 45분 | 차트 6종, 메시지가 분명한 차트 |
| 독립·짝 실습 | 35분 | 나쁜 차트 고치기, 2×2 대시보드 저장 |
| 공유·점검 | 20분 | AI 차트 코드 자동 점검, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~6 | 1. matplotlib 기본 구조 | Figure·Axes, 한글 폰트 |
| 7~11 | 2. 질문별 차트 6종 | 추세·비교·분포·관계 |
| 12~13 | 3. 메시지가 분명한 차트 | 결론형 제목, 강조, bar_label, 기간 강조 |
| 14~15 | 4. 나쁜 차트 고치기 · Level 2 | 0부터, 순서, 색, 제목 |
| 16~17 | 5. Level 3 카페 대시보드 | subplots(2, 2), 히트맵, savefig |
| 18~21 | 6. Level 4 AI 차트 점검 | audit_chart, 그래프 객체 검사, 체크리스트 |

## 사용하는 데이터

- [`cafe_sales.csv`](../../datasets/cafe_sales.csv)
- [`weather_daily.csv`](../../datasets/weather_daily.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 강조가 있는 메뉴 매출 가로 막대 | 2 |
| 2 | 일 매출 추세와 이동평균 | 2 |
| 3 | 기온과 아이스 비율 산점도 + 추세선 | 3 |
| 4 | 2×2 대시보드 저장 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
