# Week 06. 파일 · CSV · 예외 처리

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/practice.ipynb)

## 학습 목표

- `with open`과 `pathlib`으로 텍스트 파일을 안전하게 쓰고 읽으며, 파일 모드와 인코딩을 올바르게 지정한다.
- `csv.DictReader`/`csv.DictWriter`로 CSV를 읽고 쓰며, 읽은 값이 문자열이라는 점을 처리한다.
- `try/except/else/finally`로 예상 가능한 오류만 처리하고, `raise`로 오류 이유를 전달한다.
- 오류가 섞인 파일을 행 단위로 검증해 정상 데이터와 줄 번호가 있는 오류 보고서로 나누고, 결과를 재검증한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 오류에 견고한 성적 파일 처리기 (`students_raw.csv`)
- **산출물**: 정상 행 CSV, 오류 보고서 CSV, 재검증 결과

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 지저분한 실제 데이터, 파일 모드, 예외 처리 구조 |
| 안내 실습 | 45분 | 텍스트 파일, CSV 읽고 쓰기, try/except/raise |
| 독립·짝 실습 | 35분 | 검증 규칙에 따른 성적 파일 처리기와 오류 보고서 |
| 공유·점검 | 20분 | `except: pass`가 숨긴 버그 사례 공유, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~8 | 0~1. 데이터 준비 · 텍스트 파일 | 파일 모드 실험, pathlib |
| 9~10 | 2. CSV 읽고 쓰기 | DictReader 문자열 함정, DictWriter 저장 |
| 11~13 | 3. 예외 처리 | try/except/else/finally, 오류 종류별 처리, raise |
| 14 | 4. Level 2 바꾸기 | 범위 검사 추가, 파일 모드 비교 |
| 15~18 | 5. Level 3 성적 파일 처리기 | 행 검증, 정상/오류 분리, 보고서, 재검증 |
| 19~21 | 6. Level 4 except: pass | 숨은 오타 버그 재현, 예외 처리 원칙 |

## 사용하는 데이터

- [`students_raw.csv`](../../datasets/students_raw.csv)
- [`students.csv`](../../datasets/students.csv)

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 안전한 정수 변환 | 2 |
| 2 | 메모 파일 다루기 | 2 |
| 3 | CSV 학과별 평균 | 3 |
| 4 | 검증 보고서 만들기 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
