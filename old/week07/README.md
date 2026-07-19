# Week 7. Class와 객체지향 프로그래밍 기초

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/week07/practice.ipynb)

---

## 1. 이번 주 학습 맥락

관련 데이터와 기능을 하나의 객체로 묶으면 구조가 명확해지지만 단순한 문제에 과도한 class를 만들지 않도록 판단해야 합니다.

**문제 상황:** Student class에 이름·전공·점수와 학점 판정·요약 메서드를 구현합니다.

## 2. 관련 학습성과

CLO5, CLO8

## 3. 학습 목표

- class·객체·속성·메서드를 설명한다.
- __init__()과 self로 객체를 초기화한다.
- 객체 리스트를 분석한다.

## 4. 선수 지식 확인

- 이전 주 핵심 개념을 설명할 수 있는가?
- 오늘 문제의 입력·처리·출력을 구분할 수 있는가?
- AI가 생성한 코드에서 무엇을 검증해야 하는가?

## 5. 핵심 개념

### 1. class

객체의 데이터와 행동을 정의하는 설계도입니다.

### 2. 객체

class를 바탕으로 생성된 실제 데이터 단위입니다.

### 3. 속성

객체가 보유하는 데이터입니다.

### 4. 메서드

객체가 수행하는 행동입니다.

## 6. 주요 코드 예제

```python
class Student:
    def __init__(self,name:str,major:str,score:int)->None:
        self.name=name; self.major=major; self.score=score
    def get_grade(self)->str:
        if self.score>=90:return "A"
        if self.score>=80:return "B"
        if self.score>=70:return "C"
        return "F"
    def summary(self)->str:
        return f"{self.name}({self.major}) - {self.score}점, {self.get_grade()}"

student=Student("김민수","경영학과",85)
print(student.summary())
```

### 예상 확인 사항

- 새 Colab 런타임에서 실행되는가?
- 변수·함수·데이터 열이 요구사항과 일치하는가?
- 경계값에서 결과가 바뀌는가?
- 각 단계의 역할을 설명할 수 있는가?

## 7. AI 협업 코딩 절차

```text
문제 정의 → 입력·처리·출력 → Prompt → AI 코드 검토 → 실행
→ 정상·경계·예외 테스트 → 오류 수정 → 리팩토링 → 기록
```

## 8. 복사해서 사용할 수 있는 Prompt

```text
당신은 대학 Python 강사이자 코드 리뷰어입니다.

주제: Class와 객체지향 프로그래밍 기초
문제 상황: Student class에 이름·전공·점수와 학점 판정·요약 메서드를 구현합니다.

먼저 입력, 처리, 출력을 표로 정리해 주세요.
Google Colab에서 실행 가능한 Python 코드 초안을 작성해 주세요.
의미 있는 변수명과 함수명, 핵심 주석을 사용해 주세요.
정상·경계·예외 테스트와 예상 결과를 제안해 주세요.
```

## 9. Google Colab 실습 안내

1. Open in Colab 버튼을 누릅니다.
2. `파일 > 드라이브에 사본 저장`을 선택합니다.
3. 기본 예제를 순서대로 실행합니다.
4. TODO 셀을 직접 수정합니다.
5. 디버깅 셀의 오류 원인을 기록합니다.
6. 테스트 셀을 통과시킵니다.
7. AI 활용 로그를 작성합니다.

## 10. 오류와 점검 방법

| 점검 항목 | 확인 방법 |
|---|---|
| 변수·함수 이름 | 정의와 호출 철자 확인 |
| 자료형 | `type()`과 변환 함수 확인 |
| 조건 논리 | 경계값 전·해당·후 테스트 |
| 파일·데이터 열 | 실제 경로와 `columns` 확인 |
| 결과 검증 | assert 또는 수동 계산과 비교 |
| AI 답변 | 실행·테스트 후 수용 여부 결정 |

## 11. 테스트 케이스

- 정상 대표 입력
- 조건이 바뀌는 경계값
- 빈 입력 또는 빈 데이터
- 범위를 벗어난 입력
- 예상 자료형과 다른 입력

## 12. 응용 실습

- 데이터를 자신의 전공 또는 관심 주제로 변경
- AI 제안 코드와 직접 작성한 코드 비교
- 출력 형식 또는 함수 구조 개선
- 새 테스트 케이스 추가

## 13. 스스로 설명하기

1. 오늘 코드의 입력·처리·출력은 무엇인가?
2. AI 초안에서 직접 수정한 부분은 무엇인가?
3. 어떤 테스트가 오류 발견에 도움을 주었는가?
4. Prompt를 어떻게 개선할 것인가?

## 14. 과제 또는 프로젝트 연결

**Student class와 객체 리스트 리팩토링**

Colab 링크, Prompt, 최종 코드, 테스트 결과, 직접 수정한 부분, 오류 해결 과정을 제출합니다.

## 15. 핵심 요약

- AI는 초안을 제안하지만 정확성 판단은 학습자의 책임입니다.
- 실행과 테스트 없이 AI 코드를 신뢰하지 않습니다.
- 수정 이유를 설명할 수 있어야 합니다.
- Prompt와 수정 과정을 학습 결과로 기록합니다.

## 16. 다음 주 예고

Week 8에서는 class·파일·테스트를 결합한 중간 프로젝트를 수행합니다.
