# Week 07. 클래스와 객체지향 설계

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/practice.ipynb)

## 학습 목표

- 딕셔너리+함수 방식의 한계를 보고, 상태와 동작을 묶는 클래스가 필요한 이유를 설명한다.
- `class`, `__init__`, `self`, 메서드, `__str__`/`__repr__`, `@property`로 클래스를 만든다.
- 책임을 나눈 여러 클래스가 협력하는 시스템을 만들고, 시나리오 테스트로 상태 변화를 검증한다.
- 상속·다형성·`@dataclass`를 활용하고, AI 코드의 클래스 변수 공유 버그를 찾아 고친다.

## 이번 주 실습과 산출물

- **핵심 실습**: 도서 대출 관리 시스템 (`Book`, `Member`, `Library`)
- **산출물**: 상태와 동작을 함께 관리하는 클래스와 시나리오 테스트

## 2시간 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입·개념 | 20분 | 왜 클래스인가, 클래스·객체·self |
| 안내 실습 | 45분 | Book 클래스, 특별 메서드, 도서 대출 시스템 |
| 독립·짝 실습 | 35분 | 시나리오 테스트, 상속·dataclass |
| 공유·점검 | 20분 | 클래스 변수 공유 버그, 과제·중간 실기 안내 |

## 이번 주 파일

| 파일 | 설명 | 바로 열기 |
|---|---|---|
| [`slides.md`](slides.md) | Marp 강의 슬라이드 | [PDF](slides.pdf) |
| [`practice.ipynb`](practice.ipynb) | 수업 시간 실습 노트북 | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/practice.ipynb) |
| [`assignment.ipynb`](assignment.ipynb) | 과제 노트북(자동 확인 포함) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/assignment.ipynb) |
| [`assignment.md`](assignment.md) | 과제 안내와 채점 기준 | |

## 슬라이드–노트북 연결

| 슬라이드 | 노트북 구간 | 학생 활동 |
|---|---|---|
| 5~6 | 1. 왜 클래스인가? | 딕셔너리 방식의 문제 재현 |
| 7~10 | 2. Level 1 클래스의 기본 | __init__, self, __str__, @property |
| 11 | 3. Level 2 바꾸기 | 누적 대출 횟수 추가 |
| 12~16 | 4. Level 3 도서 대출 시스템 | 책임 나누기, 대출·반납·연체, 시나리오 테스트 |
| 17~18 | 5. 상속과 dataclass | EBook 오버라이딩, LoanRecord |
| 19~21 | 6. Level 4 클래스 변수 | 공유 리스트 버그 재현과 수정 |

## 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 은행 계좌 클래스 | 2 |
| 2 | 도형 상속과 다형성 | 2 |
| 3 | 할 일 목록 클래스 | 3 |
| 4 | 스터디룸 예약 시스템 (AI 협업) | 3 |

자세한 내용은 [과제 안내](assignment.md)를 확인하세요.
