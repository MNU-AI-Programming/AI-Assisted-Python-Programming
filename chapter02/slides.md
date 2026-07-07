---
marp: true
theme: default
paginate: true
---

# AI 활용 코딩

## Chapter 2. Python 시작하기

비전공자를 위한 생성형 AI 활용 프로그래밍

---

# 학습 목표

- Google Colab에서 Python 코드를 실행할 수 있다.
- print() 함수로 문장을 출력할 수 있다.
- 변수를 사용하여 데이터를 저장할 수 있다.
- 자료형을 구분할 수 있다.
- 문자열과 f-string을 사용할 수 있다.

---

# Python이란?

Python은 전 세계에서 많이 사용하는 프로그래밍 언어입니다.

- 데이터 분석
- 인공지능
- 웹 개발
- 업무 자동화
- 교육
- 과학 계산

---

# Python 코드 예시

```python
print("안녕하세요")
```

사람이 읽기 쉬운 문법을 가지고 있습니다.

---

# Google Colab에서 실행하기

1. 코드 셀 클릭
2. Python 코드 입력
3. 실행 버튼 클릭
4. 결과 확인

---

# print() 함수

화면에 내용을 출력하는 함수입니다.

```python
print("안녕하세요")
print("AI 활용 코딩")
```

---

# 여러 줄 출력하기

```python
print("이름: 홍길동")
print("학과: 교양학부")
print("관심 분야: 인공지능")
```

---

# 자주 하는 실수

잘못된 코드

```python
print(안녕하세요)
```

올바른 코드

```python
print("안녕하세요")
```

문자열에는 따옴표가 필요합니다.

---

# 변수란?

변수는 데이터를 저장하는 이름표입니다.

```python
name = "홍길동"
print(name)
```

---

# 변수는 왜 필요한가?

같은 값을 여러 번 사용할 수 있습니다.

```python
name = "홍길동"

print(name)
print("안녕하세요,", name, "님")
```

---

# 변수 이름 규칙

- 영어, 숫자, 밑줄 사용 가능
- 숫자로 시작할 수 없음
- 공백 사용 불가
- 의미 있는 이름 사용 권장

예:

```python
student_name = "홍길동"
```

---

# 자료형이란?

자료형은 데이터의 종류입니다.

| 자료형 | 의미 | 예시 |
|---|---|---|
| int | 정수 | 10 |
| float | 실수 | 3.14 |
| str | 문자열 | "Hello" |
| bool | 참/거짓 | True |

---

# type() 함수

자료형을 확인할 때 사용합니다.

```python
print(type(10))
print(type(3.14))
print(type("Hello"))
print(type(True))
```

---

# 숫자와 문자열

```python
print(10 + 5)
print("10" + "5")
```

결과

```text
15
105
```

숫자 10과 문자열 "10"은 다릅니다.

---

# 문자열

문자열은 글자나 문장입니다.

```python
message = "안녕하세요"
print(message)
```

---

# 문자열 연결

```python
first = "AI"
second = "Coding"

print(first + " " + second)
```

결과

```text
AI Coding
```

---

# f-string

문자열 안에 변수 값을 넣을 때 사용합니다.

```python
name = "홍길동"
age = 20

print(f"안녕하세요. 저는 {name}입니다.")
print(f"제 나이는 {age}살입니다.")
```

---

# AI Prompt 예시

```text
Python의 f-string을 프로그래밍 초보자도 이해할 수 있도록 설명해 주세요.

이름, 나이, 학과를 출력하는 예제를 만들어 주세요.
```

---

# AI가 만든 코드 수정하기

AI가 만든 코드를 그대로 사용하지 말고 자신의 정보에 맞게 수정합니다.

```python
name = "김하늘"
age = 19
print(f"안녕하세요. 저는 {name}입니다.")
```

---

# 실습

1. 문장 출력하기
2. 여러 줄 출력하기
3. 변수 사용하기
4. 자료형 확인하기
5. f-string 자기소개 만들기
6. AI 코드 수정하기

---

# 핵심 정리

- print()는 화면 출력 함수입니다.
- 변수는 값을 저장하는 이름표입니다.
- 자료형은 데이터의 종류입니다.
- 문자열은 따옴표로 감쌉니다.
- f-string은 문장 안에 변수 값을 넣을 때 유용합니다.

---

# 과제

AI와 함께 나의 프로필 카드 프로그램을 만들어 봅시다.

- 이름
- 학과
- 나이
- 관심 분야
- 이번 학기 목표

을 변수와 f-string으로 출력합니다.
