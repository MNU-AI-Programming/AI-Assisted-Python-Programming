# GitHub 사용법

> GitHub는 코드와 문서를 저장하고 공유하는 온라인 저장소입니다.  
> 이 교재에서는 GitHub를 강의자료, 실습 코드, 과제 안내를 제공하는 공간으로 사용합니다.

---

## 1. GitHub란?

GitHub는 다음을 할 수 있는 서비스입니다.

- 코드 저장
- 문서 공유
- 버전 관리
- 협업
- 과제 제출
- 프로젝트 공개

이 수업에서는 GitHub를 어렵게 사용하지 않습니다.  
학생은 주로 자료를 읽고, 실습 파일을 열고, 과제 링크를 제출하는 용도로 사용합니다.

---

## 2. 저장소 구조 이해하기

이 교재 저장소는 다음과 같은 구조입니다.

```text
AI-Programming-with-GenAI/
├── README.md
├── SUMMARY.md
├── chapter01/
├── chapter02/
├── ...
└── chapter08/
```

각 Chapter 폴더에는 다음 파일이 있습니다.

```text
README.md       # 교재 본문
practice.ipynb  # Google Colab 실습
slides.md       # 강의 슬라이드
assignment.md   # 과제 안내
quiz.md         # 퀴즈
```

---

## 3. GitHub에서 교재 읽기

1. 저장소 접속
2. `README.md` 읽기
3. `SUMMARY.md`에서 목차 확인
4. 원하는 Chapter 폴더 선택
5. `README.md` 클릭

---

## 4. 실습 파일 열기

실습 파일은 각 Chapter의 `practice.ipynb`입니다.

GitHub에서 파일을 볼 수 있지만, 실행은 Google Colab에서 해야 합니다.

실습 방법:

1. Chapter 폴더로 이동
2. `practice.ipynb` 클릭
3. README의 Open in Colab 버튼 클릭
4. Colab에서 실행

---

## 5. 과제 제출 방법

수업 운영 방식에 따라 제출 방법은 달라질 수 있습니다.

일반적으로 다음 중 하나를 사용합니다.

- LMS에 Colab 링크 제출
- GitHub 저장소 링크 제출
- PDF 또는 Markdown 보고서 제출
- 실행 결과 캡처 제출

---

## 6. GitHub 계정 만들기

1. GitHub 접속
2. Sign up 클릭
3. 이메일 입력
4. 사용자 이름 설정
5. 비밀번호 설정
6. 이메일 인증

사용자 이름은 가능하면 수업용으로 알아보기 쉽게 만듭니다.

예:

```text
mnu-ai-coding-gildong
```

---

## 7. 내 저장소 만들기

과제나 프로젝트를 GitHub에 정리하려면 자신의 저장소를 만들 수 있습니다.

1. 오른쪽 위 `+` 클릭
2. `New repository` 선택
3. Repository name 입력
4. Public 또는 Private 선택
5. `Add a README file` 체크
6. Create repository 클릭

---

## 8. README 작성하기

프로젝트 저장소에는 README를 작성하는 것이 좋습니다.

예:

```markdown
# 용돈 관리 프로그램

## 프로젝트 소개
수입과 지출을 입력받아 잔액을 계산하는 프로그램입니다.

## 사용한 기술
- Python
- Google Colab
- ChatGPT

## 주요 기능
- 수입 입력
- 지출 입력
- 잔액 계산

## 사용한 AI Prompt
...
```

---

## 9. GitHub 사용 시 주의사항

- 비밀번호나 개인정보를 올리지 않습니다.
- 다른 학생의 코드를 그대로 복사하지 않습니다.
- AI가 만든 코드도 자신의 이해와 수정 과정을 기록합니다.
- 과제 제출용 저장소가 공개되어도 되는지 교수자 지침을 확인합니다.
