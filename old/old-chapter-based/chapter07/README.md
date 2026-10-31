# Chapter 7. 리스트와 파일 처리

[![Open Chapter 7 In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/chapter07/practice.ipynb)

> 지금까지는 하나의 값이나 몇 개의 변수만 다루었습니다.  
> 이번 장에서는 여러 개의 데이터를 한 번에 저장하는 **리스트(list)**와 데이터를 파일로 저장하고 다시 읽는 기초 방법을 배웁니다.

---


---

## 💻 Google Colab 실습 바로 열기

아래 버튼을 클릭하면 이 장의 실습 노트북이 Google Colab에서 열립니다.

[![Open Chapter 7 In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/chapter07/practice.ipynb)

> GitHub에 업로드한 뒤 `MNU-AI-Programming`를 교수자 GitHub 아이디로 변경해야 버튼이 정상 동작합니다.

---

## 🎯 학습 목표

이번 장을 학습하면 다음을 할 수 있습니다.

- 리스트가 필요한 이유를 설명할 수 있다.
- 여러 개의 값을 리스트에 저장할 수 있다.
- 리스트의 값을 읽고 수정할 수 있다.
- `append()`를 사용하여 리스트에 값을 추가할 수 있다.
- 반복문으로 리스트의 값을 하나씩 처리할 수 있다.
- 간단한 성적 관리 프로그램을 만들 수 있다.
- CSV 파일의 개념을 이해할 수 있다.
- Google Colab에서 CSV 파일을 저장하고 읽을 수 있다.
- AI에게 리스트와 파일 처리 코드를 요청하고 검토할 수 있다.

---

## 🤔 생각해 보기

다음 질문에 대해 생각해 봅시다.

1. 학생 30명의 점수를 변수 30개에 따로 저장해야 한다면 불편하지 않을까요?
2. 여러 개의 이름을 한 번에 저장하려면 어떻게 해야 할까요?
3. 성적 데이터를 프로그램이 끝난 뒤에도 보관하려면 어떻게 해야 할까요?
4. AI가 만든 파일 저장 코드가 제대로 저장되는지 어떻게 확인할 수 있을까요?

---

## 7.1 리스트란?

리스트는 여러 개의 값을 하나로 묶어 저장하는 자료형입니다.

예를 들어 학생 이름 3개를 저장한다고 해 봅시다.

변수를 따로 사용하면 다음과 같습니다.

```python
student1 = "김민수"
student2 = "이서연"
student3 = "박지훈"
```

학생 수가 많아지면 변수가 너무 많아집니다.

리스트를 사용하면 다음과 같이 한 번에 저장할 수 있습니다.

```python
students = ["김민수", "이서연", "박지훈"]
```

---

### 리스트의 기본 형태

```python
리스트이름 = [값1, 값2, 값3]
```

예:

```python
scores = [90, 85, 70, 100]
names = ["김민수", "이서연", "박지훈"]
```

리스트는 숫자, 문자열 등 여러 값을 저장할 수 있습니다.

---

## 7.2 리스트 값 읽기

리스트 안의 값을 읽으려면 위치 번호를 사용합니다.

이 위치 번호를 **인덱스(index)**라고 합니다.

중요한 점은 Python의 인덱스가 0부터 시작한다는 것입니다.

```python
students = ["김민수", "이서연", "박지훈"]

print(students[0])
print(students[1])
print(students[2])
```

실행 결과:

```text
김민수
이서연
박지훈
```

---

## ⚠️ 자주 하는 실수 1: 인덱스는 0부터 시작

리스트에 값이 3개 있을 때 사용할 수 있는 인덱스는 0, 1, 2입니다.

```python
students = ["김민수", "이서연", "박지훈"]

print(students[3])
```

위 코드는 오류가 발생합니다.

`students[3]`은 네 번째 값을 의미하지만, 리스트에는 세 개의 값만 있기 때문입니다.

---

## 7.3 리스트 값 수정하기

리스트의 값은 수정할 수 있습니다.

```python
students = ["김민수", "이서연", "박지훈"]

students[1] = "최하늘"

print(students)
```

실행 결과:

```text
['김민수', '최하늘', '박지훈']
```

---

## 7.4 리스트에 값 추가하기

리스트에 값을 추가할 때는 `append()`를 사용합니다.

```python
students = ["김민수", "이서연"]

students.append("박지훈")

print(students)
```

실행 결과:

```text
['김민수', '이서연', '박지훈']
```

---

### 빈 리스트에서 시작하기

빈 리스트를 만든 후 값을 하나씩 추가할 수도 있습니다.

```python
scores = []

scores.append(90)
scores.append(80)
scores.append(100)

print(scores)
```

---

## 🤖 AI Prompt 실습 1

ChatGPT에게 다음 Prompt를 입력해 봅시다.

```text
당신은 Python 프로그래밍 강사입니다.

저는 프로그래밍을 처음 배우는 비전공 대학생입니다.

Python의 리스트(list)를 쉽게 설명해 주세요.

학생 이름을 저장하는 리스트 예제를 만들어 주세요.

인덱스가 0부터 시작한다는 점도 설명해 주세요.

각 줄에 초보자도 이해할 수 있는 주석을 달아 주세요.
```

AI가 만든 코드를 Google Colab에서 실행해 봅시다.

---

## 7.5 반복문으로 리스트 처리하기

리스트와 반복문을 함께 사용하면 리스트 안의 값을 하나씩 처리할 수 있습니다.

```python
students = ["김민수", "이서연", "박지훈"]

for name in students:
    print(name)
```

실행 결과:

```text
김민수
이서연
박지훈
```

---

### 점수 리스트 출력하기

```python
scores = [90, 85, 70, 100]

for score in scores:
    print(score)
```

---

### 점수 합계와 평균 구하기

```python
scores = [90, 85, 70, 100]

total = 0

for score in scores:
    total = total + score

average = total / len(scores)

print(f"합계: {total}")
print(f"평균: {average:.2f}")
```

`len()`은 리스트 안에 값이 몇 개 있는지 알려주는 함수입니다.

---

## 7.6 성적 관리 프로그램 만들기

학생 이름과 점수를 리스트에 저장하고 평균을 계산하는 프로그램을 만들어 봅시다.

```python
names = []
scores = []

for i in range(3):
    name = input("학생 이름을 입력하세요: ")
    score = int(input("점수를 입력하세요: "))

    names.append(name)
    scores.append(score)

print("===== 성적 목록 =====")

for i in range(3):
    print(f"{names[i]}: {scores[i]}점")

average = sum(scores) / len(scores)

print(f"평균 점수: {average:.2f}")
```

---

### 코드 이해하기

```python
names = []
scores = []
```

학생 이름과 점수를 저장할 빈 리스트를 만듭니다.

```python
names.append(name)
scores.append(score)
```

입력받은 이름과 점수를 리스트에 추가합니다.

```python
sum(scores) / len(scores)
```

점수 합계를 점수 개수로 나누어 평균을 구합니다.

---

## 7.7 CSV 파일이란?

CSV는 Comma-Separated Values의 약자입니다.

우리말로는 “쉼표로 구분된 값”이라는 뜻입니다.

예를 들어 다음과 같은 데이터가 있다고 해 봅시다.

```text
이름,점수
김민수,90
이서연,85
박지훈,70
```

이처럼 쉼표로 데이터를 구분한 파일을 CSV 파일이라고 합니다.

CSV 파일은 엑셀에서도 열 수 있고, Python에서도 쉽게 다룰 수 있습니다.

---

## 7.8 Colab에서 CSV 파일 저장하기

Python에서는 `open()` 함수를 사용하여 파일을 만들 수 있습니다.

```python
names = ["김민수", "이서연", "박지훈"]
scores = [90, 85, 70]

with open("scores.csv", "w", encoding="utf-8") as file:
    file.write("이름,점수\n")

    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
```

위 코드를 실행하면 `scores.csv` 파일이 만들어집니다.

---

### with open()의 의미

```python
with open("scores.csv", "w", encoding="utf-8") as file:
```

이 코드는 `scores.csv` 파일을 쓰기 모드로 여는 코드입니다.

- `"scores.csv"`: 파일 이름
- `"w"`: write, 쓰기 모드
- `encoding="utf-8"`: 한글이 깨지지 않도록 설정
- `file.write()`: 파일에 글을 쓰는 함수

---

## ⚠️ 자주 하는 실수 2: 줄바꿈 `\n` 빠뜨리기

파일에 여러 줄을 저장하려면 줄바꿈이 필요합니다.

```python
file.write("이름,점수\n")
```

여기서 `\n`은 줄을 바꾸라는 뜻입니다.

`\n`이 없으면 모든 내용이 한 줄에 붙어서 저장될 수 있습니다.

---

## 7.9 CSV 파일 읽기

저장한 CSV 파일을 다시 읽어 봅시다.

```python
with open("scores.csv", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

이 코드는 파일 전체 내용을 읽어 화면에 출력합니다.

---

### 한 줄씩 읽기

```python
with open("scores.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
```

`strip()`은 줄 끝의 줄바꿈 문자 등을 제거합니다.

---

## 7.10 pandas로 CSV 읽기

Google Colab에서는 `pandas`라는 도구를 사용하여 CSV 파일을 표처럼 읽을 수 있습니다.

```python
import pandas as pd

df = pd.read_csv("scores.csv")

df
```

Colab에서는 표 형태로 결과가 보입니다.

> 이 교재에서는 pandas를 깊게 배우지는 않습니다.  
> 다만 CSV 파일을 표처럼 확인하는 용도로 간단히 사용합니다.

---

## 🤖 AI Prompt 실습 2

ChatGPT에게 다음 Prompt를 입력해 봅시다.

```text
Python에서 리스트에 저장된 학생 이름과 점수를 CSV 파일로 저장하는 코드를 만들어 주세요.

Google Colab에서 실행할 수 있게 작성해 주세요.

파일 이름은 scores.csv로 해 주세요.

한글이 깨지지 않도록 encoding="utf-8"을 사용해 주세요.

각 줄에 초보자도 이해할 수 있는 주석을 달아 주세요.
```

AI가 만든 코드를 실행하고, 파일이 생성되었는지 확인해 봅시다.

---

## 7.11 AI가 만든 리스트·파일 코드 검토하기

AI가 만든 리스트와 파일 처리 코드는 반드시 확인해야 합니다.

확인할 점은 다음과 같습니다.

1. 리스트에 값이 제대로 추가되는가?
2. 인덱스 범위를 벗어나지 않는가?
3. 반복 횟수가 리스트 길이와 맞는가?
4. 파일 이름이 올바른가?
5. 파일 저장 모드가 적절한가?
6. 한글 저장을 위해 `encoding="utf-8"`을 사용했는가?
7. 줄바꿈 `\n`이 들어 있는가?
8. 저장한 파일을 다시 읽어서 확인했는가?

---

### AI에게 코드 검토 요청하기

다음 Prompt를 사용할 수 있습니다.

```text
아래 Python 코드가 Google Colab에서 올바르게 실행되는지 검토해 주세요.

특히 리스트 인덱스, 반복문, CSV 저장, encoding, 줄바꿈 문제가 있는지 확인해 주세요.

필요하면 초보자도 이해하기 쉬운 코드로 수정해 주세요.

코드:
여기에 코드를 붙여 넣기
```

---

## 💻 Google Colab 실습 안내

이번 장의 실습 노트북은 `practice.ipynb`입니다.

실습 내용은 다음과 같습니다.

1. 리스트 만들기
2. 리스트 값 읽기
3. 리스트 값 수정하기
4. 리스트에 값 추가하기
5. 반복문으로 리스트 출력하기
6. 점수 합계와 평균 구하기
7. 성적 관리 프로그램 만들기
8. CSV 파일 저장하기
9. CSV 파일 읽기
10. pandas로 CSV 확인하기
11. AI가 만든 파일 처리 코드 검토하기

---

## ✍️ 스스로 해보기

다음 프로그램을 만들어 봅시다.

1. 좋아하는 음식 5개를 리스트에 저장하고 출력하기
2. 친구 이름 3개를 입력받아 리스트에 저장하기
3. 점수 5개를 입력받아 평균 구하기
4. 학생 이름과 점수를 입력받아 성적 목록 출력하기
5. 성적 목록을 CSV 파일로 저장하기
6. 저장된 CSV 파일을 다시 읽어 출력하기
7. AI에게 리스트와 파일 처리 프로그램을 요청하고 직접 수정하기

---

## 7.12 Chapter 7 요약

이번 장에서는 다음을 배웠습니다.

- 리스트는 여러 개의 값을 하나로 묶어 저장하는 자료형입니다.
- 리스트의 인덱스는 0부터 시작합니다.
- `append()`를 사용하면 리스트에 값을 추가할 수 있습니다.
- 반복문을 사용하면 리스트 안의 값을 하나씩 처리할 수 있습니다.
- `sum()`과 `len()`을 사용하여 합계와 평균을 구할 수 있습니다.
- CSV 파일은 쉼표로 데이터를 구분한 파일입니다.
- `open()`과 `write()`를 사용하여 파일을 저장할 수 있습니다.
- `read()`와 `readlines()`를 사용하여 파일을 읽을 수 있습니다.
- `pandas`를 사용하면 CSV 파일을 표처럼 확인할 수 있습니다.
- AI가 만든 파일 처리 코드는 저장 결과를 반드시 직접 확인해야 합니다.

---

## 📚 핵심 문장

> 리스트는 여러 데이터를 한 번에 저장하는 도구이고,  
> 파일 처리는 프로그램의 결과를 저장하고 다시 사용하는 방법입니다.

---

## 다음 장 예고

Chapter 8에서는 지금까지 배운 내용을 활용하여 AI와 함께 나만의 프로젝트를 만듭니다.
