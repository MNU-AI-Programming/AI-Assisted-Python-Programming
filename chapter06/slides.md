---
marp: true
theme: default
paginate: true
---

# AI 활용 코딩

## Chapter 6. 함수와 AI 활용

비전공자를 위한 생성형 AI 활용 프로그래밍

---

# 학습 목표

- 함수가 필요한 이유를 설명할 수 있다.
- def로 함수를 만들 수 있다.
- 매개변수와 인자를 이해할 수 있다.
- return을 사용할 수 있다.
- AI에게 함수 생성, 디버깅, 리팩토링을 요청할 수 있다.

---

# 생각해 보기

- 같은 계산을 여러 번 해야 한다면?
- BMI 계산기를 다시 사용하려면?
- 긴 코드를 보기 쉽게 정리하려면?
- AI가 만든 코드를 개선하려면?

---

# 함수란?

특정 작업을 수행하는 코드를 하나의 이름으로 묶은 것입니다.

이미 사용한 함수:

```python
print()
input()
int()
float()
type()
range()
```

---

# 함수가 필요한 이유

- 같은 코드를 반복해서 쓰지 않아도 됨
- 코드가 짧고 깔끔해짐
- 프로그램 구조를 이해하기 쉬움
- 오류 수정이 쉬움
- AI에게 개선 요청하기 쉬움

---

# 함수 만들기

```python
def hello():
    print("안녕하세요")
    print("AI 활용 코딩 수업입니다")

hello()
```

---

# 함수 정의와 호출

함수 정의

```python
def hello():
    print("안녕하세요")
```

함수 호출

```python
hello()
```

함수는 호출해야 실행됩니다.

---

# 자주 하는 실수

함수를 정의만 하고 호출하지 않는 경우

```python
def hello():
    print("안녕하세요")
```

실행하려면:

```python
hello()
```

---

# 매개변수

함수에 값을 전달할 수 있습니다.

```python
def hello(name):
    print(f"안녕하세요, {name}님!")

hello("홍길동")
```

---

# 매개변수와 인자

```python
def hello(name):
```

`name`은 매개변수입니다.

```python
hello("홍길동")
```

`"홍길동"`은 인자입니다.

---

# 여러 매개변수

```python
def introduce(name, major):
    print(f"이름: {name}")
    print(f"학과: {major}")

introduce("홍길동", "교양학부")
```

---

# return

함수의 결과를 돌려줍니다.

```python
def add(a, b):
    result = a + b
    return result

answer = add(3, 5)
print(answer)
```

---

# print()와 return

`print()`는 화면에 출력합니다.

`return`은 결과를 함수 밖으로 돌려줍니다.

```python
def add(a, b):
    return a + b
```

---

# 계산기 함수

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(10, 2))
print(subtract(10, 2))
```

---

# BMI 계산 함수

```python
def calculate_bmi(height_cm, weight):
    height_m = height_cm / 100
    bmi = weight / (height_m * height_m)
    return bmi

bmi = calculate_bmi(175, 70)
print(f"BMI: {bmi:.2f}")
```

---

# AI에게 함수 요청하기

좋은 요청에는 다음을 포함합니다.

1. 함수 이름
2. 입력값
3. 처리 과정
4. 반환값
5. 사용 예시
6. 주석 여부

---

# 좋은 Prompt 예시

```text
Python 함수를 만들어 주세요.

함수 이름: calculate_total
입력값: price, quantity
기능: 가격과 수량을 곱해 총 금액 계산
반환값: 총 금액
초보자용 주석 포함
```

---

# 디버깅

오류를 찾고 수정하는 과정입니다.

오류가 생기면 AI에게 다음을 알려줍니다.

- 코드
- 오류 메시지
- 하려던 작업
- 실행 환경

---

# 오류 예시

```python
def add(a, b):
    return a + b

result = add(3)
print(result)
```

인자가 하나 부족합니다.

---

# 리팩토링

기능은 유지하면서 코드를 더 읽기 좋게 개선하는 것입니다.

반복되는 코드를 함수로 바꾸는 것도 리팩토링입니다.

---

# 리팩토링 전

```python
price1 = 3000
quantity1 = 2
total1 = price1 * quantity1
print(total1)

price2 = 5000
quantity2 = 3
total2 = price2 * quantity2
print(total2)
```

---

# 리팩토링 후

```python
def calculate_total(price, quantity):
    return price * quantity

print(calculate_total(3000, 2))
print(calculate_total(5000, 3))
```

---

# AI 코드 검토 기준

- 함수 이름이 적절한가?
- 매개변수가 필요한 만큼 있는가?
- return이 필요한 곳에 있는가?
- 함수가 한 가지 역할에 집중하는가?
- 예제 실행 결과가 올바른가?
- 초보자가 이해하기 쉬운가?

---

# 실습

1. 간단한 함수 만들기
2. 매개변수 사용
3. return 사용
4. 계산기 함수
5. BMI 함수
6. 디버깅
7. 리팩토링

---

# 핵심 정리

- 함수는 코드를 이름으로 묶는 도구입니다.
- def로 함수를 만듭니다.
- 함수는 호출해야 실행됩니다.
- return은 결과를 돌려줍니다.
- AI를 활용해 함수 생성, 디버깅, 리팩토링을 할 수 있습니다.

---

# 과제

AI와 함께 함수를 사용하는 프로그램을 만들어 봅시다.

예:

- BMI 계산 함수
- 총 금액 계산 함수
- 원의 넓이 계산 함수
- 학점 판정 함수
