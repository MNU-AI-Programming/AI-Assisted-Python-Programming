---
marp: true
theme: default
paginate: true
---

# AI 활용 코딩

## Chapter 3. 입력과 계산

비전공자를 위한 생성형 AI 활용 프로그래밍

---

# 학습 목표

- input() 함수로 사용자 입력을 받을 수 있다.
- 문자열을 숫자로 변환할 수 있다.
- 산술 연산자를 사용할 수 있다.
- f-string으로 계산 결과를 출력할 수 있다.
- BMI 계산기와 간단한 계산기를 만들 수 있다.

---

# 생각해 보기

- 프로그램이 사용자에게 질문할 수 있다면?
- 키와 몸무게를 입력하면 BMI를 계산할 수 있을까?
- 사용자가 입력한 20은 숫자일까, 문자일까?

---

# input() 함수

사용자에게 값을 입력받을 때 사용합니다.

```python
name = input("이름을 입력하세요: ")
print(name)
```

---

# 입력값 사용하기

```python
name = input("이름을 입력하세요: ")
print("안녕하세요,", name, "님!")
```

---

# input()의 결과

`input()`으로 입력받은 값은 기본적으로 문자열입니다.

```python
age = input("나이를 입력하세요: ")
print(type(age))
```

---

# 숫자로 변환하기

정수 변환

```python
age = int(input("나이를 입력하세요: "))
```

실수 변환

```python
height = float(input("키를 입력하세요: "))
```

---

# int()와 float()

| 함수 | 의미 | 예시 |
|---|---|---|
| int() | 정수로 변환 | 20 |
| float() | 실수로 변환 | 175.5 |

---

# 자주 하는 실수

잘못된 코드

```python
num = input("숫자: ")
print(num + 10)
```

올바른 코드

```python
num = int(input("숫자: "))
print(num + 10)
```

---

# 산술 연산자

| 연산자 | 의미 |
|---|---|
| + | 더하기 |
| - | 빼기 |
| * | 곱하기 |
| / | 나누기 |
| // | 몫 |
| % | 나머지 |
| ** | 거듭제곱 |

---

# 계산 예제

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

# f-string으로 출력하기

```python
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
```

---

# 소수점 자리 조절

```python
result = 10 / 3
print(f"결과: {result:.2f}")
```

결과

```text
결과: 3.33
```

---

# BMI 계산식

```text
BMI = 몸무게(kg) / (키(m) * 키(m))
```

---

# BMI 계산기

```python
height = float(input("키를 m 단위로 입력하세요: "))
weight = float(input("몸무게를 kg 단위로 입력하세요: "))

bmi = weight / (height * height)

print(f"당신의 BMI는 {bmi:.2f}입니다.")
```

---

# 키 단위 주의

BMI 계산에서는 키를 m 단위로 사용합니다.

- 175cm → 1.75m
- 160cm → 1.60m

---

# cm 단위 입력 처리

```python
height_cm = float(input("키를 cm 단위로 입력하세요: "))
height_m = height_cm / 100
```

---

# 간단한 계산기

```python
a = float(input("첫 번째 숫자: "))
b = float(input("두 번째 숫자: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
```

---

# AI Prompt 예시

```text
Python으로 간단한 계산기 프로그램을 만들어 주세요.

두 숫자를 입력받아 사칙연산 결과를 출력하게 해 주세요.

초보자도 이해할 수 있도록 주석을 달아 주세요.
```

---

# AI 코드 검토 기준

- 입력값을 숫자로 변환했는가?
- 계산식이 맞는가?
- 출력 결과가 이해하기 쉬운가?
- 오류가 발생하지 않는가?
- 입력 단위가 명확한가?

---

# 실습

1. 이름 입력받기
2. 나이 입력받기
3. 숫자 변환하기
4. 산술 연산자 실습
5. BMI 계산기
6. 간단한 계산기

---

# 핵심 정리

- input()은 사용자 입력을 받습니다.
- input()의 결과는 문자열입니다.
- 계산하려면 int() 또는 float()으로 변환합니다.
- 산술 연산자로 계산합니다.
- f-string으로 결과를 보기 좋게 출력합니다.

---

# 과제

AI와 함께 생활 계산기 프로그램을 만들어 봅시다.

예:

- BMI 계산기
- 여행 경비 계산기
- 카페 주문 금액 계산기
- 용돈 계산기
