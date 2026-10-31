# Week 05. 함수 · 모듈 · 테스트 가능한 코드

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/practice.ipynb)

## 학습 목표

- 매개변수·기본값·키워드 인자·여러 값 반환·docstring·타입 힌트로 읽기 쉬운 함수를 만든다.
- print 대신 return, 전역 대신 매개변수를 쓰는 순수 함수로 설계하고, 잘못된 입력은 `raise ValueError`로 알린다.
- 정상·경계·잘못된 입력을 포함한 `test_` 함수를 작성하고, `%%writefile`로 모듈을 만들어 `import`한다.
- AI 코드의 가변 기본값 버그를 찾고, AI가 만든 테스트에 나만의 경계값 테스트를 추가한다.

## 이번 주 실습과 산출물

- **핵심 실습**: 재사용 가능한 성적 계산 모듈 (`grade_utils.py`)
- **산출물**: 입력·처리·출력을 분리한 함수 모음과 테스트

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 함수로 나누는 이유, print vs return, 순수 함수 |
| 안내 실습 | 45분 | 함수 구성 요소, 범위, raise, 테스트 함수와 실행기 |
| 독립·짝 실습 | 35분 | 성적 계산 모듈 작성·import·테스트 |
| 공유·점검 | 20분 | 가변 기본값 버그 재현과 수정, 과제 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~8 | 1. Level 1 함수의 구성 요소 | 기본값·키워드 인자·여러 값 반환, print vs return |
| 9~10 | 2. 범위와 순수 함수 | UnboundLocalError 재현, 순수 함수로 바꾸기 |
| 11~13 | 3. 테스트와 잘못된 입력 | raise ValueError, test_ 함수, 테스트 실행기 |
| 14 | 4. Level 2 바꾸기 | 과제 가중치 추가와 하위 호환 확인 |
| 15~18 | 5. Level 3 성적 계산 모듈 | %%writefile, import, reload, 모듈 테스트 |
| 19~21 | 6. Level 4 가변 기본값 | AI 코드 버그 재현, None 기본값으로 수정 |

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 가중 평균과 입력 검증 | 2 |
| 2 | 비밀번호 강도 검사 | 2 |
| 3 | 텍스트 통계 함수 | 3 |
| 4 | 테스트로 AI 버그 잡기 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
