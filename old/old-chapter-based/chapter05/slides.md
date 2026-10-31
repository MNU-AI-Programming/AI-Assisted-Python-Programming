---
marp: true
theme: default
paginate: true
---

# AI 활용 코딩

## Chapter 5. 반복문

비전공자를 위한 생성형 AI 활용 프로그래밍

---

# 학습 목표

- 반복문이 필요한 이유를 설명할 수 있다.
- for 반복문과 range()를 사용할 수 있다.
- while 반복문을 사용할 수 있다.
- 반복문과 조건문을 함께 사용할 수 있다.
- 구구단과 숫자 맞추기 게임을 만들 수 있다.

---

# 생각해 보기

- 같은 문장을 100번 출력해야 한다면?
- 구구단을 출력하려면?
- 정답을 맞힐 때까지 계속 질문하려면?

---

# 반복문이란?

같은 작업을 여러 번 실행할 때 사용하는 문법입니다.

```text
안녕하세요 5번 출력
1부터 10까지 출력
구구단 출력
정답을 맞힐 때까지 반복
```

---

# 반복문이 없는 코드

```python
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
```

---

# 반복문을 사용한 코드

```python
for i in range(5):
    print("안녕하세요")
```

같은 코드를 여러 번 쓰지 않아도 됩니다.

---

# for 반복문

정해진 횟수만큼 반복할 때 사용합니다.

```python
for 변수 in 반복범위:
    반복할 코드
```

---

# range() 함수

```python
for i in range(5):
    print(i)
```

결과

```text
0
1
2
3
4
```

---

# 1부터 5까지 출력

```python
for i in range(1, 6):
    print(i)
```

`range(1, 6)`은 1부터 5까지입니다.

---

# 자주 하는 실수

```python
for i in range(1, 5):
    print(i)
```

결과는 1부터 4까지입니다.

끝 숫자는 포함되지 않습니다.

---

# 합계 구하기

```python
total = 0

for i in range(1, 11):
    total = total + i

print(total)
```

결과

```text
55
```

---

# 구구단 2단

```python
dan = 2

for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")
```

---

# 입력받은 단 출력

```python
dan = int(input("출력할 단을 입력하세요: "))

for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")
```

---

# while 반복문

조건이 참인 동안 계속 반복합니다.

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

---

# while 문 주의

조건이 계속 참이면 끝나지 않습니다.

```python
count = count + 1
```

반복이 끝날 수 있도록 조건을 바꾸는 코드가 필요합니다.

---

# 무한 반복 예

```python
count = 1

while count <= 5:
    print(count)
```

`count`가 변하지 않으므로 계속 반복됩니다.

---

# 반복문 + 조건문

1부터 10까지 숫자 중 짝수만 출력합니다.

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

---

# 숫자 맞추기 게임

```python
answer = 7
guess = 0

while guess != answer:
    guess = int(input("숫자를 맞혀 보세요: "))

    if guess == answer:
        print("정답입니다!")
    else:
        print("틀렸습니다.")
```

---

# random 모듈

무작위 숫자를 만들 수 있습니다.

```python
import random

answer = random.randint(1, 10)
```

---

# random 숫자 맞추기

```python
import random

answer = random.randint(1, 10)
guess = 0

while guess != answer:
    guess = int(input("1부터 10 사이 숫자: "))

    if guess == answer:
        print("정답입니다!")
    elif guess < answer:
        print("더 큰 숫자입니다.")
    else:
        print("더 작은 숫자입니다.")
```

---

# break

반복문을 중간에 종료합니다.

```python
while True:
    number = int(input("종료하려면 0 입력: "))

    if number == 0:
        break

    print(number)
```

---

# AI Prompt 예시

```text
Python으로 구구단 프로그램을 만들어 주세요.

사용자가 원하는 단을 입력하면 해당 단을 출력하게 해 주세요.

for, range(), input(), int(), f-string을 사용해 주세요.
```

---

# AI 코드 검토 기준

- 반복 횟수가 맞는가?
- range() 범위가 올바른가?
- 들여쓰기가 맞는가?
- while 문이 무한 반복되지 않는가?
- break가 필요한 곳에 있는가?

---

# 실습

1. 문장 반복 출력
2. 숫자 출력
3. 합계 구하기
4. 구구단
5. while 반복
6. 짝수 출력
7. 숫자 맞추기 게임

---

# 핵심 정리

- 반복문은 같은 작업을 자동으로 반복합니다.
- for는 정해진 횟수 반복에 적합합니다.
- while은 조건이 참인 동안 반복합니다.
- while에서는 종료 조건이 중요합니다.
- break는 반복문을 중간에 끝냅니다.

---

# 과제

AI와 함께 반복문 프로그램을 만들어 봅시다.

예:

- 구구단 프로그램
- 숫자 맞추기 게임
- 합계 계산기
- 반복 메뉴 프로그램
