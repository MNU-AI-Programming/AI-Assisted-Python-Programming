# Week 04. 리스트 · 튜플 · 집합 · 딕셔너리

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/practice.ipynb)

## 학습 목표

- 네 가지 자료구조의 특징(순서·변경·중복)을 비교하고 상황에 맞는 자료구조를 고른다.
- 리스트 컴프리헨션, 언패킹, `sorted(key=...)`로 데이터를 간결하게 다룬다.
- 딕셔너리로 개수 세기와 그룹 묶기 패턴을 구현해 학생 레코드를 학과별로 요약한다.
- AI 코드에서 반복 중 삭제, 없는 키 접근, 원본 변경, 동점 처리 문제를 테스트로 찾아낸다.

## 이번 주 실습과 산출물

- **핵심 실습**: 학생 성적 레코드 분석
- **산출물**: 구조화된 학생 데이터와 학과별 요약 통계

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 자료구조 비교, 복사와 참조, 정렬 key |
| 안내 실습 | 45분 | 리스트·튜플·집합·딕셔너리, 개수 세기·그룹 묶기 |
| 독립·짝 실습 | 35분 | 학생 성적 레코드 분석 (총점, 학과별 요약, 상위 3명) |
| 공유·점검 | 20분 | AI 코드 함정 3가지 재현과 수정 공유, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~9 | 1. Level 1 리스트 | sort vs sorted, 복사와 참조, 컴프리헨션 |
| 10~11 | 2~3. 튜플 · 집합 | 언패킹, 중복 제거, 집합 연산 |
| 12~15 | 4. 딕셔너리 | get, 개수 세기, 그룹 묶기, 정렬 key |
| 16 | 5. Level 2 바꾸기 | 컴프리헨션 조건 바꾸기, 평균 순 정렬 |
| 17~19 | 6. Level 3 성적 레코드 분석 | 총점 계산, 학과별 요약, 검증 |
| 20~22 | 7. Level 4 AI 코드 함정 | 반복 중 삭제, 없는 키, 원본 변경 |

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 단어 빈도 세기 | 2 |
| 2 | 두 수강반 비교 | 2 |
| 3 | 학과별 성적 요약 | 3 |
| 4 | 순위와 필터 – 원본을 지켜라 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
