# Chapter 7 과제
## AI와 함께 성적 관리 프로그램 만들기

---

## 과제 목표

이번 과제의 목표는 리스트와 파일 처리를 활용하여 여러 명의 학생 성적을 저장하고, 평균을 계산하며, CSV 파일로 저장하는 프로그램을 만드는 것입니다.

---

## 과제 설명

ChatGPT를 활용하여 **성적 관리 프로그램**을 작성하세요.

프로그램은 다음 기능을 포함해야 합니다.

1. 학생 이름을 입력받기
2. 학생 점수를 입력받기
3. 이름과 점수를 리스트에 저장하기
4. 성적 목록 출력하기
5. 평균 점수 계산하기
6. CSV 파일로 저장하기
7. 저장한 CSV 파일을 다시 읽어 확인하기

---

## 필수 조건

다음 조건을 모두 만족해야 합니다.

1. Google Colab에서 작성하고 실행할 것
2. 리스트를 2개 이상 사용할 것
3. `append()`를 사용할 것
4. 반복문을 사용할 것
5. `sum()`과 `len()`을 사용하여 평균을 계산할 것
6. CSV 파일로 저장할 것
7. `encoding="utf-8"`을 사용할 것
8. 저장한 파일을 다시 읽어 출력할 것
9. ChatGPT에 사용한 Prompt를 기록할 것
10. AI가 만든 코드를 직접 수정하거나 개선할 것

---

## 추천 Prompt

```text
당신은 Python 프로그래밍 강사입니다.

저는 프로그래밍을 처음 배우는 대학생입니다.

Google Colab에서 실행할 수 있는 성적 관리 프로그램을 만들고 싶습니다.

학생 3명의 이름과 점수를 입력받고,
이름은 names 리스트에, 점수는 scores 리스트에 저장해 주세요.

성적 목록을 출력하고,
평균 점수를 계산해 주세요.

마지막으로 scores.csv 파일에 이름과 점수를 저장하고,
저장한 파일을 다시 읽어 출력하게 해 주세요.

리스트, append(), for 반복문, sum(), len(), open(), write(), read()를 사용해 주세요.

한글이 깨지지 않도록 encoding="utf-8"을 사용해 주세요.

각 줄에 초보자도 이해할 수 있는 주석을 달아 주세요.
```

---

## 제출물

다음 내용을 제출합니다.

1. Google Colab 링크
2. 사용한 AI Prompt
3. 최종 Python 코드
4. 실행 결과
5. 생성된 CSV 파일 내용
6. 직접 수정한 부분 설명
7. AI를 활용해 수정하거나 개선한 과정
8. 느낀 점 3줄 이상

---

## 제출 형식 예시

```markdown
# Chapter 7 과제

## 1. 사용한 Prompt

...

## 2. 최종 코드

```python
names = []
scores = []

for i in range(3):
    name = input("학생 이름을 입력하세요: ")
    score = int(input("점수를 입력하세요: "))

    names.append(name)
    scores.append(score)

print("===== 성적 목록 =====")

for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}점")

average = sum(scores) / len(scores)
print(f"평균 점수: {average:.2f}")

with open("scores.csv", "w", encoding="utf-8") as file:
    file.write("이름,점수\n")

    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")

with open("scores.csv", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

## 3. 실행 결과

...

## 4. CSV 파일 내용

...

## 5. 수정한 부분

AI가 만든 코드에 평균 점수 출력 형식을 소수점 둘째 자리로 바꾸었습니다.

## 6. 느낀 점

...
```

---

## 평가 기준

| 평가 항목 | 배점 |
|---|---:|
| Colab 실행 여부 | 10 |
| 리스트 사용 | 15 |
| append()와 반복문 사용 | 15 |
| 평균 계산 | 15 |
| CSV 저장 | 15 |
| CSV 다시 읽기 | 10 |
| AI Prompt 기록 | 10 |
| 수정 내용 및 느낀 점 | 10 |
| 합계 | 100 |

---

## 주의사항

파일을 저장한 뒤에는 반드시 다시 읽어서 내용이 제대로 저장되었는지 확인하세요.  
AI가 만든 코드가 Colab에서 실제로 파일을 생성하는지 직접 확인해야 합니다.
