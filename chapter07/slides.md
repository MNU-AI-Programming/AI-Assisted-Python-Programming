---
marp: true
theme: default
paginate: true
---

# AI 활용 코딩

## Chapter 7. 리스트와 파일 처리

비전공자를 위한 생성형 AI 활용 프로그래밍

---

# 학습 목표

- 리스트가 필요한 이유를 설명할 수 있다.
- 리스트의 값을 읽고 수정할 수 있다.
- append()로 값을 추가할 수 있다.
- 반복문으로 리스트를 처리할 수 있다.
- CSV 파일을 저장하고 읽을 수 있다.

---

# 생각해 보기

- 학생 30명의 점수를 변수 30개에 저장한다면?
- 여러 이름을 한 번에 저장하려면?
- 프로그램 결과를 나중에도 보관하려면?

---

# 리스트란?

여러 개의 값을 하나로 묶어 저장하는 자료형입니다.

```python
students = ["김민수", "이서연", "박지훈"]
scores = [90, 85, 70]
```

---

# 리스트가 필요한 이유

변수를 따로 쓰면 불편합니다.

```python
student1 = "김민수"
student2 = "이서연"
student3 = "박지훈"
```

리스트를 사용하면 한 번에 저장할 수 있습니다.

```python
students = ["김민수", "이서연", "박지훈"]
```

---

# 리스트 값 읽기

리스트는 인덱스로 값을 읽습니다.

```python
students = ["김민수", "이서연", "박지훈"]

print(students[0])
print(students[1])
print(students[2])
```

인덱스는 0부터 시작합니다.

---

# 자주 하는 실수

```python
students = ["김민수", "이서연", "박지훈"]

print(students[3])
```

값이 3개이면 인덱스는 0, 1, 2만 가능합니다.

---

# 리스트 값 수정

```python
students = ["김민수", "이서연", "박지훈"]

students[1] = "최하늘"

print(students)
```

---

# 리스트에 값 추가

```python
students = ["김민수", "이서연"]

students.append("박지훈")

print(students)
```

---

# 빈 리스트에서 시작

```python
scores = []

scores.append(90)
scores.append(80)
scores.append(100)

print(scores)
```

---

# 반복문으로 리스트 출력

```python
students = ["김민수", "이서연", "박지훈"]

for name in students:
    print(name)
```

---

# 점수 합계와 평균

```python
scores = [90, 85, 70, 100]

total = 0

for score in scores:
    total = total + score

average = total / len(scores)

print(total)
print(average)
```

---

# 성적 관리 프로그램

```python
names = []
scores = []

for i in range(3):
    name = input("학생 이름: ")
    score = int(input("점수: "))

    names.append(name)
    scores.append(score)
```

---

# 성적 목록 출력

```python
for i in range(3):
    print(f"{names[i]}: {scores[i]}점")

average = sum(scores) / len(scores)
print(f"평균 점수: {average:.2f}")
```

---

# CSV 파일이란?

CSV는 쉼표로 구분된 값입니다.

```text
이름,점수
김민수,90
이서연,85
박지훈,70
```

엑셀과 Python에서 모두 사용할 수 있습니다.

---

# CSV 파일 저장

```python
with open("scores.csv", "w", encoding="utf-8") as file:
    file.write("이름,점수\n")

    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
```

---

# 줄바꿈 주의

```python
file.write("이름,점수\n")
```

`\n`은 줄바꿈을 의미합니다.

없으면 한 줄에 붙어서 저장될 수 있습니다.

---

# CSV 파일 읽기

```python
with open("scores.csv", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

---

# 한 줄씩 읽기

```python
with open("scores.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
```

---

# pandas로 CSV 확인

```python
import pandas as pd

df = pd.read_csv("scores.csv")

df
```

Colab에서 표 형태로 확인할 수 있습니다.

---

# AI Prompt 예시

```text
Python에서 리스트에 저장된 학생 이름과 점수를 CSV 파일로 저장하는 코드를 만들어 주세요.

Google Colab에서 실행 가능하게 작성하고,
한글이 깨지지 않도록 encoding="utf-8"을 사용해 주세요.
```

---

# AI 코드 검토 기준

- 리스트에 값이 제대로 추가되는가?
- 인덱스 범위를 벗어나지 않는가?
- 반복 횟수가 리스트 길이와 맞는가?
- encoding이 있는가?
- 줄바꿈이 들어 있는가?
- 저장한 파일을 다시 읽어 확인했는가?

---

# 실습

1. 리스트 만들기
2. 리스트 값 읽기
3. 리스트 값 수정하기
4. append() 사용하기
5. 성적 평균 구하기
6. CSV 저장하기
7. CSV 읽기

---

# 핵심 정리

- 리스트는 여러 값을 한 번에 저장합니다.
- 인덱스는 0부터 시작합니다.
- 반복문으로 리스트를 처리할 수 있습니다.
- CSV는 데이터를 저장하는 쉬운 파일 형식입니다.
- 저장한 파일은 반드시 다시 읽어 확인합니다.

---

# 과제

AI와 함께 성적 관리 프로그램을 만들어 봅시다.

- 학생 이름 입력
- 점수 입력
- 평균 계산
- CSV 저장
- CSV 읽기
