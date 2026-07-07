# Chapter 6. 함수와 AI 활용

[![Open Chapter 6 In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Programming-with-GenAI/blob/main/chapter06/practice.ipynb)

> 함수는 자주 사용하는 코드를 하나의 이름으로 묶어 다시 사용할 수 있게 해 줍니다.  
> 이번 장에서는 함수를 만들고, AI를 활용하여 코드를 함수로 정리하고, 오류를 찾고, 더 읽기 좋은 코드로 개선하는 방법을 배웁니다.

---


---

## 💻 Google Colab 실습 바로 열기

아래 버튼을 클릭하면 이 장의 실습 노트북이 Google Colab에서 열립니다.

[![Open Chapter 6 In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Programming-with-GenAI/blob/main/chapter06/practice.ipynb)

> GitHub에 업로드한 뒤 `MNU-AI-Programming`를 교수자 GitHub 아이디로 변경해야 버튼이 정상 동작합니다.

---

## 🎯 학습 목표

이번 장을 학습하면 다음을 할 수 있습니다.

- 함수가 필요한 이유를 설명할 수 있다.
- `def`를 사용하여 함수를 만들 수 있다.
- 매개변수와 인자의 의미를 이해할 수 있다.
- `return`을 사용하여 함수의 결과를 돌려줄 수 있다.
- 반복되는 코드를 함수로 정리할 수 있다.
- AI에게 함수 생성, 코드 설명, 오류 수정, 리팩토링을 요청할 수 있다.
- AI가 만든 함수 코드를 검토하고 수정할 수 있다.

---

## 🤔 생각해 보기

다음 질문에 대해 생각해 봅시다.

1. 같은 계산을 여러 번 해야 한다면 매번 코드를 다시 써야 할까요?
2. BMI 계산기를 여러 번 사용하려면 어떻게 하면 좋을까요?
3. 코드가 길어졌을 때 보기 쉽게 정리하려면 어떻게 해야 할까요?
4. AI가 만든 코드를 더 읽기 좋게 바꾸려면 어떻게 요청해야 할까요?

---

## 6.1 함수란?

함수는 특정 작업을 수행하는 코드를 하나의 이름으로 묶은 것입니다.

우리는 이미 Python에서 여러 함수를 사용했습니다.

예를 들어 다음은 모두 함수입니다.

```python
print()
input()
int()
float()
type()
range()
```

이 함수들은 누군가 미리 만들어 둔 기능입니다.

이번 장에서는 우리가 직접 함수를 만들어 보겠습니다.

---

### 함수는 왜 필요할까요?

함수를 사용하면 다음과 같은 장점이 있습니다.

- 같은 코드를 반복해서 쓰지 않아도 됩니다.
- 코드가 더 짧고 깔끔해집니다.
- 프로그램의 구조를 이해하기 쉬워집니다.
- 오류를 찾고 수정하기 쉬워집니다.
- AI에게 코드 개선을 요청하기 쉬워집니다.

---

## 6.2 함수 만들기

Python에서 함수를 만들 때는 `def`를 사용합니다.

기본 구조는 다음과 같습니다.

```python
def 함수이름():
    실행할 코드
```

예를 들어 인사하는 함수를 만들어 봅시다.

```python
def hello():
    print("안녕하세요")
    print("AI 활용 코딩 수업입니다")

hello()
```

실행 결과:

```text
안녕하세요
AI 활용 코딩 수업입니다
```

---

### 함수 정의와 함수 호출

함수를 만드는 것을 **함수 정의**라고 합니다.

```python
def hello():
    print("안녕하세요")
```

함수를 실행하는 것을 **함수 호출**이라고 합니다.

```python
hello()
```

함수는 정의만 해서는 실행되지 않습니다.  
반드시 호출해야 실행됩니다.

---

## ⚠️ 자주 하는 실수 1: 함수를 정의만 하고 호출하지 않기

```python
def hello():
    print("안녕하세요")
```

위 코드는 함수를 정의한 것뿐입니다.  
실행 결과가 나타나지 않습니다.

함수를 실행하려면 아래처럼 호출해야 합니다.

```python
hello()
```

---

## ⚠️ 자주 하는 실수 2: 들여쓰기 실수

잘못된 코드:

```python
def hello():
print("안녕하세요")
```

올바른 코드:

```python
def hello():
    print("안녕하세요")
```

함수 안에서 실행할 코드는 반드시 들여쓰기 해야 합니다.

---

## 🤖 AI Prompt 실습 1

ChatGPT에게 다음 Prompt를 입력해 봅시다.

```text
당신은 Python 프로그래밍 강사입니다.

저는 프로그래밍을 처음 배우는 비전공 대학생입니다.

Python의 함수가 무엇인지 쉽게 설명해 주세요.

def를 사용하여 인사말을 출력하는 함수를 만드는 예제를 작성해 주세요.

각 줄에 초보자도 이해할 수 있는 주석을 달아 주세요.
```

AI가 만든 코드를 Google Colab에서 실행해 봅시다.

---

## 6.3 매개변수와 인자

함수에 값을 전달할 수 있습니다.

예를 들어 이름을 받아 인사하는 함수를 만들어 봅시다.

```python
def hello(name):
    print(f"안녕하세요, {name}님!")

hello("홍길동")
hello("김민수")
```

실행 결과:

```text
안녕하세요, 홍길동님!
안녕하세요, 김민수님!
```

---

### 매개변수와 인자의 차이

```python
def hello(name):
```

여기서 `name`은 **매개변수**입니다.  
함수가 값을 받을 자리를 의미합니다.

```python
hello("홍길동")
```

여기서 `"홍길동"`은 **인자**입니다.  
함수를 호출할 때 실제로 전달하는 값입니다.

---

### 여러 개의 매개변수 사용하기

```python
def introduce(name, major):
    print(f"이름: {name}")
    print(f"학과: {major}")

introduce("홍길동", "교양학부")
```

---

## 6.4 return 사용하기

함수는 계산한 결과를 돌려줄 수 있습니다.

이때 `return`을 사용합니다.

```python
def add(a, b):
    result = a + b
    return result

answer = add(3, 5)
print(answer)
```

실행 결과:

```text
8
```

---

### print()와 return의 차이

초보자가 가장 많이 헷갈리는 부분입니다.

`print()`는 화면에 출력합니다.

```python
def add(a, b):
    print(a + b)

add(3, 5)
```

`return`은 결과를 함수 밖으로 돌려줍니다.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

`return`을 사용하면 결과를 다른 계산에 다시 사용할 수 있습니다.

---

## 6.5 함수로 계산기 만들기

더하기, 빼기, 곱하기, 나누기 함수를 만들어 봅시다.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

x = 10
y = 2

print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")
```

---

## 6.6 BMI 계산 함수를 만들기

Chapter 3에서 만들었던 BMI 계산기를 함수로 바꿔 봅시다.

```python
def calculate_bmi(height_cm, weight):
    height_m = height_cm / 100
    bmi = weight / (height_m * height_m)
    return bmi

height = float(input("키를 cm 단위로 입력하세요: "))
weight = float(input("몸무게를 kg 단위로 입력하세요: "))

bmi = calculate_bmi(height, weight)

print(f"당신의 BMI는 {bmi:.2f}입니다.")
```

---

### 함수로 만들면 좋은 점

BMI 계산식을 함수로 만들면 나중에 다시 사용할 수 있습니다.

```python
bmi1 = calculate_bmi(175, 70)
bmi2 = calculate_bmi(160, 55)

print(f"첫 번째 BMI: {bmi1:.2f}")
print(f"두 번째 BMI: {bmi2:.2f}")
```

---

## 🤖 AI Prompt 실습 2

ChatGPT에게 다음 Prompt를 입력해 봅시다.

```text
Python으로 BMI를 계산하는 함수를 만들고 싶습니다.

함수 이름은 calculate_bmi로 해 주세요.

키는 cm 단위, 몸무게는 kg 단위로 입력받고,
함수 안에서 키를 m 단위로 변환한 뒤 BMI를 계산하게 해 주세요.

return을 사용해 결과를 돌려주고,
함수 사용 예제도 함께 작성해 주세요.

초보자도 이해할 수 있도록 주석을 달아 주세요.
```

AI가 만든 코드를 실행하고, 함수 이름이나 출력 문장을 직접 수정해 봅시다.

---

## 6.7 AI에게 함수 만들기 요청하기

AI에게 함수를 만들어 달라고 할 때는 다음을 구체적으로 알려주는 것이 좋습니다.

1. 함수 이름
2. 입력값
3. 처리 과정
4. 반환값
5. 사용 예시
6. 주석 여부

---

### 좋은 Prompt 예시

```text
Python 함수를 만들어 주세요.

함수 이름: calculate_total
입력값: price, quantity
기능: 가격과 수량을 곱해 총 금액 계산
반환값: 총 금액
사용 예시: calculate_total(3000, 2)의 결과는 6000
초보자용 주석 포함
```

---

## 6.8 디버깅이란?

디버깅은 코드의 오류를 찾고 수정하는 과정입니다.

프로그래밍을 하다 보면 오류는 자연스럽게 발생합니다.

중요한 것은 오류를 두려워하지 않고, 오류 메시지를 읽고 해결하는 것입니다.

---

### 오류가 있는 코드 예시

```python
def add(a, b):
    return a + b

result = add(3)
print(result)
```

이 코드는 오류가 발생합니다.  
`add()` 함수는 두 개의 값을 받아야 하는데 하나만 전달했기 때문입니다.

---

### AI에게 오류 해결 요청하기

오류가 발생하면 다음 정보를 AI에게 함께 전달해야 합니다.

1. 내가 작성한 코드
2. 오류 메시지
3. 내가 하려던 작업
4. 실행 환경

---

### 디버깅 Prompt 예시

```text
아래 Python 코드를 Google Colab에서 실행했더니 오류가 발생했습니다.

제가 하려던 작업은 두 숫자를 더하는 함수를 실행하는 것입니다.

오류의 원인을 초보자도 이해할 수 있도록 설명하고,
수정된 코드를 제시해 주세요.

코드:
def add(a, b):
    return a + b

result = add(3)
print(result)

오류 메시지:
여기에 오류 메시지를 붙여 넣기
```

---

## 6.9 리팩토링이란?

리팩토링은 코드의 기능은 유지하면서 코드를 더 읽기 좋고 관리하기 쉽게 개선하는 것입니다.

예를 들어 반복되는 코드를 함수로 바꾸는 것도 리팩토링입니다.

---

### 리팩토링 전 코드

```python
price1 = 3000
quantity1 = 2
total1 = price1 * quantity1
print(f"총 금액: {total1}원")

price2 = 5000
quantity2 = 3
total2 = price2 * quantity2
print(f"총 금액: {total2}원")
```

---

### 리팩토링 후 코드

```python
def calculate_total(price, quantity):
    return price * quantity

total1 = calculate_total(3000, 2)
total2 = calculate_total(5000, 3)

print(f"총 금액: {total1}원")
print(f"총 금액: {total2}원")
```

함수를 사용하면 코드가 더 깔끔해지고 재사용하기 쉬워집니다.

---

## 🤖 AI Prompt 실습 3

ChatGPT에게 다음 Prompt를 입력해 봅시다.

```text
아래 Python 코드를 함수로 리팩토링해 주세요.

기능은 그대로 유지하고,
반복되는 부분을 함수로 묶어 주세요.

초보자도 이해할 수 있도록 변경 전과 변경 후의 차이를 설명해 주세요.

코드:
price1 = 3000
quantity1 = 2
total1 = price1 * quantity1
print(f"총 금액: {total1}원")

price2 = 5000
quantity2 = 3
total2 = price2 * quantity2
print(f"총 금액: {total2}원")
```

---

## 6.10 AI가 만든 함수 코드 검토하기

AI가 만든 함수 코드는 반드시 확인해야 합니다.

확인할 점은 다음과 같습니다.

1. 함수 이름이 기능을 잘 설명하는가?
2. 매개변수가 필요한 만큼 있는가?
3. `return`이 필요한 곳에 사용되었는가?
4. 함수가 한 가지 역할에 집중하는가?
5. 예제 실행 결과가 올바른가?
6. 불필요하게 어려운 코드가 들어가 있지 않은가?
7. 초보자가 이해할 수 있는 주석이 있는가?

---

### AI에게 코드 검토 요청하기

다음 Prompt를 사용할 수 있습니다.

```text
아래 Python 함수가 초보자용 수업에 적합한지 검토해 주세요.

함수 이름, 매개변수, return 사용, 코드 난이도, 주석을 중심으로 확인해 주세요.

필요하면 더 쉬운 코드로 수정해 주세요.

코드:
여기에 코드를 붙여 넣기
```

---

## 💻 Google Colab 실습 안내

이번 장의 실습 노트북은 `practice.ipynb`입니다.

실습 내용은 다음과 같습니다.

1. 간단한 함수 만들기
2. 함수 호출하기
3. 매개변수 사용하기
4. 여러 매개변수 사용하기
5. `return` 사용하기
6. 계산기 함수 만들기
7. BMI 계산 함수 만들기
8. AI에게 함수 생성 요청하기
9. 오류가 있는 함수 디버깅하기
10. 반복 코드를 함수로 리팩토링하기
11. 나만의 함수 만들기

---

## ✍️ 스스로 해보기

다음 프로그램을 만들어 봅시다.

1. 이름을 받아 인사하는 함수 만들기
2. 두 숫자를 더하는 함수 만들기
3. 원의 넓이를 계산하는 함수 만들기
4. 가격과 수량을 받아 총 금액을 계산하는 함수 만들기
5. BMI 계산 함수를 만들고 여러 사람의 BMI 계산하기
6. AI에게 함수를 만들어 달라고 요청한 후 더 쉽게 수정하기
7. 오류가 있는 함수 코드를 AI와 함께 수정하기

---

## 6.11 Chapter 6 요약

이번 장에서는 다음을 배웠습니다.

- 함수는 특정 작업을 수행하는 코드를 하나의 이름으로 묶은 것입니다.
- `def`를 사용하여 함수를 정의합니다.
- 함수는 정의만 해서는 실행되지 않고 호출해야 실행됩니다.
- 매개변수는 함수가 값을 받을 자리입니다.
- 인자는 함수를 호출할 때 전달하는 실제 값입니다.
- `return`은 함수의 결과를 밖으로 돌려줍니다.
- 함수를 사용하면 코드를 재사용하고 정리하기 쉽습니다.
- 디버깅은 오류를 찾고 수정하는 과정입니다.
- 리팩토링은 기능은 유지하면서 코드를 더 좋게 개선하는 과정입니다.
- AI는 함수 생성, 코드 설명, 디버깅, 리팩토링에 활용할 수 있습니다.

---

## 📚 핵심 문장

> 함수는 자주 사용하는 코드를 하나의 이름으로 묶어 다시 사용할 수 있게 해 주는 도구입니다.  
> AI를 사용할 때도 함수 단위로 요청하면 더 좋은 코드를 얻을 수 있습니다.

---

## 다음 장 예고

Chapter 7에서는 리스트와 파일 처리를 배웁니다.  
여러 개의 데이터를 저장하고, 간단한 성적 관리 프로그램을 만들어 봅니다.
