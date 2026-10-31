# Week 15. 최종 프로젝트 발표와 재현성

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/practice.ipynb)

## 학습 목표

- 실행 순서·절대 경로·난수·버전·데이터 변경 등 재현성을 깨뜨리는 원인을 알고 막는다.
- 환경·데이터 지문·난수 시드를 기록하는 재현성 셀과 질문→결론·한계→AI 활용 구조로 최종 노트북을 완성한다.
- README와 5분 발표를 준비하고, 결론마다 근거와 한계를 제시한다.
- AI가 쓴 결론 문장을 근거로 검증하고, AI 활용을 구체적이고 정직하게 공개한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 최종 프로젝트 점검과 5분 발표 (예시 미니 프로젝트 포함)
- **산출물**: 최종 Colab 노트북, README, 발표 자료, AI 활용 기록, 성찰 보고서

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 재현성 점검 | 30분 | 재현성 셀, 다시 시작 및 모두 실행, README |
| 발표 준비 | 20분 | 5분 발표 구성과 리허설 |
| 최종 발표 | 60분 | 1인(팀) 5분 발표 + 2분 질의 |
| 마무리 | 10분 | 동료 평가, 한 학기 정리 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 4~7 | 1~2. 재현성과 재현성 셀 | 깨지는 이유, 버전·시드·데이터 지문 |
| 8~10 | 3. 예시 미니 프로젝트 | 노트북 구조, 결론과 한계 |
| 11~13 | 4. README와 5분 발표 | README 구성, 발표 구성과 팁 |
| 14~15 | 5. AI 결론 검증과 공개 | 과장·인과 주장 판정, 공개 문장 |
| 16~19 | 6. 최종 점검 | 과제 안내, 신뢰구간, 제출 체크리스트, 동료 평가 |

## 사용하는 데이터

- [`cafe_sales.csv`](../../datasets/cafe_sales.csv)
- [`weather_daily.csv`](../../datasets/weather_daily.csv)
- [`students.csv`](../../datasets/students.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 환경과 데이터 지문 기록 | 2 |
| 2 | 결과표를 Markdown으로 | 2 |
| 3 | 시드가 있는 부트스트랩 신뢰구간 | 3 |
| 4 | README 생성기와 내 프로젝트 README (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
