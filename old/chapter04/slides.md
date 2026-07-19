---
marp: true
theme: default
paginate: true
---

# AI 활용 코딩

## Chapter 4. 조건문

비전공자를 위한 생성형 AI 활용 프로그래밍

---

# 학습 목표

- 조건문이 필요한 이유를 설명할 수 있다.
- if, elif, else를 사용할 수 있다.
- 비교 연산자를 사용할 수 있다.
- 논리 연산자 기초를 이해할 수 있다.
- 학점 계산기와 로그인 프로그램을 만들 수 있다.

---

# 생각해 보기

- 점수가 90점 이상이면 A학점을 주려면?
- 비밀번호가 맞을 때만 로그인하려면?
- 프로그램이 스스로 판단하려면?

---

# 조건문이란?

조건에 따라 실행할 코드를 선택하는 문법입니다.

```text
비가 오면 우산을 가져간다.
점수가 60점 이상이면 합격이다.
```

---

# if 문

```python
score = 80

if score >= 60:
    print("합격입니다.")
```

조건이 참이면 들여쓰기 된 코드가 실행됩니다.

---

# if 문의 구조

```python
if 조건:
    실행할 코드
```

주의할 점

- 조건 뒤에 콜론 `:`
- 실행할 코드는 들여쓰기

---

# 자주 하는 실수

잘못된 코드

```python
if score >= 60
    print("합격입니다.")
```

올바른 코드

```python
if score >= 60:
    print("합격입니다.")
```

---

# 비교 연산자

| 연산자 | 의미 |
|---|---|
| > | 크다 |
| < | 작다 |
| >= | 크거나 같다 |
| <= | 작거나 같다 |
| == | 같다 |
| != | 같지 않다 |

---

# 비교 연산 결과

```python
score = 75

print(score >= 60)
print(score < 60)
print(score == 75)
```

결과는 `True` 또는 `False`입니다.

---

# else 문

```python
score = 50

if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
```

조건이 거짓이면 else가 실행됩니다.

---

# elif 문

여러 조건을 처리할 때 사용합니다.

```python
score = 85

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
else:
    print("C 이하")
```

---

# 조건 순서가 중요하다

잘못된 예

```python
score = 95

if score >= 60:
    print("D")
elif score >= 90:
    print("A")
```

95점도 60점 이상이므로 D가 출력됩니다.

---

# 논리 연산자

| 연산자 | 의미 |
|---|---|
| and | 두 조건이 모두 참 |
| or | 둘 중 하나라도 참 |
| not | 참과 거짓 반대 |

---

# and 예제

```python
age = 20
has_ticket = True

if age >= 19 and has_ticket == True:
    print("입장 가능")
else:
    print("입장 불가")
```

---

# 학점 계산기

```python
score = int(input("점수를 입력하세요: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"학점은 {grade}입니다.")
```

---

# 학점 계산기 검토

- 점수를 숫자로 변환했는가?
- 조건 순서가 올바른가?
- 경계값이 잘 처리되는가?
- 출력 결과가 이해하기 쉬운가?

---

# 로그인 프로그램

```python
user_id = input("아이디: ")
password = input("비밀번호: ")

if user_id == "admin" and password == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")
```

---

# = 와 ==

| 기호 | 의미 |
|---|---|
| = | 값을 저장 |
| == | 같은지 비교 |

```python
password = "1234"
password == "1234"
```

---

# AI Prompt 예시

```text
Python으로 학점 계산기 프로그램을 만들어 주세요.

90점 이상 A, 80점 이상 B, 70점 이상 C,
60점 이상 D, 그 외 F로 출력하게 해 주세요.

초보자도 이해할 수 있도록 주석을 달아 주세요.
```

---

# AI 코드 검토 기준

- 조건식이 맞는가?
- 콜론이 있는가?
- 들여쓰기가 맞는가?
- 조건 순서가 맞는가?
- = 와 ==를 혼동하지 않았는가?
- 경계값을 테스트했는가?

---

# 실습

1. 합격/불합격 출력
2. 비교 연산자 확인
3. if-else 사용
4. elif 사용
5. 학점 계산기
6. 로그인 프로그램
7. AI 코드 검토

---

# 핵심 정리

- 조건문은 프로그램이 판단하게 합니다.
- if, elif, else를 사용합니다.
- 조건문에는 콜론과 들여쓰기가 필요합니다.
- 비교 연산자는 True/False를 만듭니다.
- 조건 순서가 중요합니다.

---

# 과제

AI와 함께 조건 판단 프로그램을 만들어 봅시다.

예:

- 학점 계산기
- 성인 판별기
- 로그인 프로그램
- 날씨 메시지 프로그램
