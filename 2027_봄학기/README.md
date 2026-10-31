# AI활용코딩연습(ZBE135) · 2027년 봄학기

> 생성형 AI와 함께 배우는 Python 문제 해결·데이터 분석 **5일 집중과정**
> 이영호 교수 · 국립목포대학교 컴퓨터학부
> 문의: [youngho@ce.mokpo.ac.kr](mailto:youngho@ce.mokpo.ac.kr)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Course%20Repository-181717?logo=github)](https://github.com/MNU-AI-Programming/AI-Assisted-Python-Programming)
[![Credits](https://img.shields.io/badge/Credit-1%20학점-2E7D32)](#수업-일정)

> **이 문서 하나로 수업을 따라갈 수 있습니다.** 매일 수업 전에 [수업 일정](#수업-일정)과 [일차별 자료 바로가기](#일차별-자료-바로가기)를 확인하고, 과제는 [과제 안내](#과제-안내)를 따르세요.

## 교과목 소개

**AI활용코딩연습(ZBE135)** 은 생성형 AI를 단순한 정답 생성기가 아니라 코드를 함께 설계하고 검증하는 **학습 파트너**로 활용하는 1학점 집중수업입니다.

하루 3시간씩 5일 동안, 하루에 **3개 주제(주차 자료 3개)** 를 다룹니다. Python 핵심 문법에서 출발해 자료구조·함수·파일·클래스, NumPy·pandas, 데이터 정제·탐색·시각화, AI 디버깅·테스트·리팩토링을 거쳐 마지막 날 **데이터 분석 미니 프로젝트를 발표**합니다. 모든 과정에서 AI가 제안한 코드를 직접 읽고 실행하며, 오류와 한계를 확인하고 수정 근거를 기록합니다.

## 교과목 개요

| 항목 | 내용 |
|---|---|
| 교과목명 | AI활용코딩연습(ZBE135) |
| 영문명 | AI-Assisted Python Coding |
| 학점·시수 | 1학점 · 총 15시간 |
| 운영 기간 | **2027년 __월 __일(_) ~ __월 __일(_)**, 5일 (확정 후 공지) |
| 수업 시간 | 매일 **__:__ ~ __:__** · 1일 3시간 (확정 후 공지) |
| 강의실 | (확정 후 공지) |
| 담당 교수 | 이영호 교수 · 국립목포대학교 컴퓨터학부 |
| 선수 학습 | `AI활용프로그래밍` 이수 또는 Python 기초 문법 이해 |
| 실습 환경 | Google Colab, GitHub, 생성형 AI (ChatGPT, Gemini, Claude 등) |
| 최종 결과물 | 실행 가능한 데이터 분석 Colab 노트북, README, 5분 발표, AI 활용 기록 |

## 학습 목표

수강생은 수업을 마친 뒤 다음을 수행할 수 있습니다.

1. Python의 조건문, 반복문, 자료구조와 함수를 조합해 문제를 해결합니다.
2. 파일·CSV·예외 처리와 클래스를 활용해 오류에 견고한 프로그램을 만듭니다.
3. NumPy와 pandas로 데이터를 불러오고 정제·변환·집계·탐색합니다.
4. matplotlib으로 메시지가 분명한 그래프를 만들고 근거와 한계를 설명합니다.
5. 생성형 AI가 제안한 코드를 정상·경계·오류 사례와 테스트로 검증하고 개선합니다.
6. 다른 사람이 다시 실행할 수 있는 분석 노트북과 발표로 결과를 공유합니다.

## 첫 수업 전에 준비하세요

- [ ] Google 계정으로 [Google Colab](https://colab.research.google.com/)에 접속해 새 노트북을 만들고 `print("hello")`를 실행해 봅니다.
- [ ] [GitHub](https://github.com/) 계정을 만들고 [수업 저장소](https://github.com/MNU-AI-Programming/AI-Assisted-Python-Programming)에 접속해 봅니다.
- [ ] 생성형 AI 서비스 하나 이상에 로그인할 수 있는지 확인합니다.
- [ ] 노트북(PC)을 충전하고 인터넷 연결을 확인합니다.
- [ ] [1주차 안내](../weeks/week01/README.md)와 [1주차 슬라이드](../weeks/week01/slides.pdf)를 미리 훑어봅니다.

## 수업 일정

하루 3차시이며, **1차시 = 주차 자료 1개**입니다. 8주차(중간 실기) 자료는 이번 집중과정에서 [과제 1](assignments/assignment01_python_problem_solving.md)로 대신합니다.

| 일차 | 날짜 | 1차시 | 2차시 | 3차시 | 주요 실습·산출물 |
|---:|---|---|---|---|---|
| 1일차 | __월 __일(_) | [1주. AI 협업 코딩과 Colab](../weeks/week01/README.md) | [2주. 입력·계산·문자열](../weeks/week02/README.md) | [3주. 조건문과 반복문](../weeks/week03/README.md) | 수강 준비 진단, 여행 경비 계산기, 장학 기준 판정기 |
| 2일차 | __월 __일(_) | [4주. 리스트·튜플·집합·딕셔너리](../weeks/week04/README.md) | [5주. 함수·모듈·테스트](../weeks/week05/README.md) | [6주. 파일·CSV·예외 처리](../weeks/week06/README.md) | 성적 레코드 분석, 성적 계산 모듈, 오류에 견고한 CSV 처리 · **과제 1 배부** |
| 3일차 | __월 __일(_) | [7주. 클래스와 객체지향](../weeks/week07/README.md) | [9주. NumPy와 배열 사고](../weeks/week09/README.md) | [10주. pandas 불러오기·탐색](../weeks/week10/README.md) | 도서 대출 시스템, 기온 데이터 분석, 성적 데이터 탐색 · **과제 2 배부** |
| 4일차 | __월 __일(_) | [11주. 데이터 정제·변환·집계](../weeks/week11/README.md) | [12주. EDA와 프로젝트 기획](../weeks/week12/README.md) | [13주. matplotlib 시각화](../weeks/week13/README.md) | 설문 정제, 카페 판매 EDA, 대시보드 · **과제 1 마감**, 과제 2 연구 질문 점검 |
| 5일차 | __월 __일(_) | [14주. AI 디버깅·테스트·리팩토링](../weeks/week14/README.md) | [15주. 재현성](../weeks/week15/README.md) + **과제 3 실기** | **최종 발표** (과제 2) | 결함 진단·리팩토링, 재현성 점검, 5분 발표 · **과제 2·3 마감** |

## 매일 이렇게 공부하세요

집중과정은 하루에 2시간 분량의 주차 자료 3개를 다루기 때문에, **수업 전 10분 예습**과 **수업 후 복습**이 중요합니다.

| 언제 | 할 일 | 자료 |
|---|---|---|
| 수업 전 (10~20분) | 그날 3개 주차의 **안내(README)** 에서 학습 목표를 읽고, 슬라이드를 훑어봅니다. | 주차 `README.md`, `slides.pdf` |
| 수업 중 | 실습 노트북을 Colab으로 열고 **Level 1~3** 셀을 교수자와 함께 실행합니다. 실행 전에 결과를 **예상**하고, 값을 바꿔 봅니다. | 주차 `practice.ipynb` |
| 수업 끝나기 전 | 당일 실습 노트북 3개를 교수자에게 **뷰어로 공유**합니다 (출석·참여 점수). | |
| 수업 후 | 실습 노트북의 **Level 4(AI와 함께)** 와 남은 셀을 마저 실행합니다. 주차 **연습 과제**로 실력을 확인합니다 (선택, 자동 확인 ✅). | `practice.ipynb`, `assignment.ipynb` |
| 과제 기간 | 종합 과제 1·2·3을 수행하고 AI 활용 기록을 남깁니다. | [과제 안내](#과제-안내) |

> 💡 주차별 `assignment.ipynb`(연습 과제)는 **제출하지 않아도 되는** 자율 연습입니다. 하지만 자동 확인(✅/❌/⏳)으로 스스로 점검할 수 있고, 종합 과제와 같은 유형이 나오므로 꼭 풀어 보길 권합니다.

## 일차별 자료 바로가기

각 링크의 **실습**은 수업 중에 함께 실행하는 노트북, **연습 과제**는 자동 확인이 있는 자율 연습 노트북입니다. Colab에서 열린 뒤 **파일 → Drive에 사본 저장**을 하고 작업하세요.

### 1일차: Python 핵심 문법

| 주제 | 안내 | 슬라이드 | 실습 | 연습 과제 |
|---|---|---|---|---|
| 1주. AI 협업 코딩과 Colab 시작 | [README](../weeks/week01/README.md) | [PDF](../weeks/week01/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week01/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week01/assignment.ipynb) |
| 2주. 입력 · 계산 · 문자열 | [README](../weeks/week02/README.md) | [PDF](../weeks/week02/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/assignment.ipynb) |
| 3주. 조건문과 반복문 | [README](../weeks/week03/README.md) | [PDF](../weeks/week03/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/assignment.ipynb) |

### 2일차: 구조화된 Python 프로그램

| 주제 | 안내 | 슬라이드 | 실습 | 연습 과제 |
|---|---|---|---|---|
| 4주. 리스트 · 튜플 · 집합 · 딕셔너리 | [README](../weeks/week04/README.md) | [PDF](../weeks/week04/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/assignment.ipynb) |
| 5주. 함수 · 모듈 · 테스트 | [README](../weeks/week05/README.md) | [PDF](../weeks/week05/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/assignment.ipynb) |
| 6주. 파일 · CSV · 예외 처리 | [README](../weeks/week06/README.md) | [PDF](../weeks/week06/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/assignment.ipynb) |

### 3일차: 객체와 데이터 처리

| 주제 | 안내 | 슬라이드 | 실습 | 연습 과제 |
|---|---|---|---|---|
| 7주. 클래스와 객체지향 설계 | [README](../weeks/week07/README.md) | [PDF](../weeks/week07/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/assignment.ipynb) |
| 9주. NumPy와 배열 사고 | [README](../weeks/week09/README.md) | [PDF](../weeks/week09/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/assignment.ipynb) |
| 10주. pandas 불러오기 · 탐색 | [README](../weeks/week10/README.md) | [PDF](../weeks/week10/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/assignment.ipynb) |

### 4일차: 데이터 분석과 시각화

| 주제 | 안내 | 슬라이드 | 실습 | 연습 과제 |
|---|---|---|---|---|
| 11주. 데이터 정제 · 변환 · 집계 | [README](../weeks/week11/README.md) | [PDF](../weeks/week11/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/assignment.ipynb) |
| 12주. EDA와 프로젝트 기획 | [README](../weeks/week12/README.md) | [PDF](../weeks/week12/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/assignment.ipynb) |
| 13주. matplotlib 시각화 | [README](../weeks/week13/README.md) | [PDF](../weeks/week13/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/assignment.ipynb) |

### 5일차: AI 코드 검증과 최종 발표

| 주제 | 안내 | 슬라이드 | 실습 | 연습 과제 |
|---|---|---|---|---|
| 14주. AI 디버깅 · 테스트 · 리팩토링 | [README](../weeks/week14/README.md) | [PDF](../weeks/week14/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/practice.ipynb) | (과제 3으로 진행) |
| 15주. 최종 프로젝트 발표와 재현성 | [README](../weeks/week15/README.md) | [PDF](../weeks/week15/slides.pdf) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/assignment.ipynb) |

최종 발표 준비 자료: [최종 프로젝트 노트북 템플릿](../templates/final_project_template.ipynb) · [README 템플릿](../templates/project-readme-template.md) · [AI 활용 기록지](../templates/ai-use-log.md)

## 과제 안내

종합 과제 3개로 학습성과를 평가합니다. 모든 과제는 Colab 노트북을 담당 교수에게 **뷰어로 공유**해 제출합니다.

| 과제 | 주제 | 배부 | 제출 마감 | 배점 | 상세 안내 |
|---|---|---|---|---:|---|
| 과제 1 | Python 성적 분석 미니 프로젝트 | 2일차 수업 후 | **4일차 수업 시작 전** | 25점 | [과제 1 안내](assignments/assignment01_python_problem_solving.md) |
| 과제 2 | AI 활용 데이터 분석 미니 프로젝트 (최종 발표) | 3일차 수업 후 | **5일차 23:59** (발표는 5일차 3차시) | 30점 | [과제 2 안내](assignments/assignment02_ai_data_analysis.md) |
| 과제 3 | AI 코드 디버깅·테스트·리팩토링 실기 | 5일차 2차시 | **5일차 23:59** | 15점 | [과제 3 안내](assignments/assignment03_ai_debugging_refactoring.md) |

정확한 날짜·시각은 운영 기간이 확정되면 이 표에 적고 LMS에도 공지합니다.

### 과제 공통 제출 원칙

- 노트북은 **런타임 → 다시 시작 및 모두 실행** 후 오류 없이 끝까지 실행되어야 합니다.
- 코드 셀만 나열하지 말고 문제, 방법, 실행 결과와 해석을 Markdown 셀에 설명합니다.
- AI를 사용했다면 프롬프트, 채택·거절한 제안, 직접 수정한 코드와 검증 결과를 기록합니다. **AI 사용 자체는 감점 대상이 아니며, 숨기는 것이 문제입니다.**
- 결과값을 직접 써 넣어(하드코딩) 자동 확인만 통과시키는 코드는 점수를 받지 못합니다.
- 개인정보, API 키, 다른 학생의 코드나 과제를 AI와 GitHub에 입력하지 않습니다.
- 파일 이름은 `학번_이름_assignment01.ipynb`, `학번_이름_assignment02.ipynb`, `학번_이름_assignment03.ipynb` 형식을 사용합니다.

### Google Colab 과제 제출 방법

파일을 따로 업로드하지 않고, 완성한 Colab 노트북을 담당 교수에게 공유하면 제출이 완료됩니다.

1. 과제 링크로 연 노트북에서 **파일 → Drive에 사본 저장**을 선택합니다.
2. 노트북 이름을 과제별 형식에 맞게 바꿉니다. (예: `20271234_김목포_assignment01.ipynb`)
3. **런타임 → 다시 시작 및 모두 실행**으로 전체 코드와 출력 결과를 확인합니다.
4. Colab 오른쪽 위의 **공유** 버튼을 누릅니다.
5. 사용자 추가란에 담당 교수 이메일 **`youngho@ce.mokpo.ac.kr`** 을 입력합니다.
6. 권한을 **뷰어**로 설정하고 **알림 보내기**를 선택한 뒤 공유합니다.
7. 공유 창의 사용자 목록에 `youngho@ce.mokpo.ac.kr`이 표시되는지 확인합니다.

> **중요:** 일반 액세스는 `제한됨`으로 유지하고 담당 교수에게만 공유합니다. 마감 시각까지 공유가 완료되어야 하며, 마감 후에는 교수자의 허가 없이 노트북을 수정하지 않습니다.

## 매일 수업 운영

1일 3시간을 3차시로 나누고, 차시마다 주차 자료 하나를 다룹니다. (시각은 수업 시작 기준)

| 시간 | 단계 | 활동 |
|---|---|---|
| 0:00~0:05 | 오늘의 목표 | 3개 주제와 산출물 안내, 전날 질문 정리 |
| 0:05~0:58 | **1차시** | 핵심 개념 15분 → 실습 노트북 Level 1~3 함께 실행 35분 → 정리 |
| 0:58~1:05 | 휴식 | 7분 |
| 1:05~1:58 | **2차시** | 핵심 개념 15분 → 실습 35분 → 정리 |
| 1:58~2:05 | 휴식 | 7분 |
| 2:05~2:50 | **3차시** | 핵심 개념 15분 → 실습 30분 |
| 2:50~3:00 | 제출 점검 | AI 사례 공유, 당일 실습 노트북 3개 공유 확인, 다음 날 안내 |

5일차는 1차시(14주) → 2차시(15주 재현성 + 과제 3 실기) → 3차시(최종 발표: 1인 5분 + 질의 2분) 순서로 진행합니다. 발표 인원이 많으면 발표 시간을 조정해 공지합니다.

## 평가 안내

| 평가 항목 | 비율 | 평가 내용 |
|---|---:|---|
| 출석·수업 참여 | 20% | 출석, 당일 실습 노트북 공유, 질문, 동료 피드백 |
| 과제 1 | 25% | Python 문제 해결, 함수·자료구조·파일·예외·클래스, 테스트, 기술 메모 |
| 과제 2 | 30% | 데이터 정제·분석·시각화, 근거 있는 결론, 재현성, 발표 |
| 과제 3 | 15% | 결함 원인 분석, 테스트 설계, 디버깅과 리팩토링 |
| AI 활용·검증 기록 | 10% | 프롬프트, 채택·거절 판단, 직접 수정, 테스트 근거 |
| **합계** | **100%** |  |

출석과 이수에 관한 세부 기준은 국립목포대학교 및 사업단의 관련 규정을 따릅니다.

## 생성형 AI 활용 원칙

1. AI가 만든 코드는 **직접 실행하고 한 줄씩 설명할 수 있을 때만** 제출합니다.
2. 사용한 프롬프트, 채택한 제안, 직접 고친 부분과 이유를 [AI 활용 기록지](../templates/ai-use-log.md)에 남깁니다.
3. 정상 사례뿐 아니라 **경계값과 오류 사례**로 검증합니다. AI가 만든 테스트에는 **내 테스트를 하나 이상** 더합니다.
4. AI의 설명과 결론은 **실행 결과와 근거**로 확인합니다. (상관을 인과로 말하는 문장, 과장된 수치에 주의)
5. 개인정보, 비밀번호, API 키, 다른 사람의 과제를 프롬프트에 넣지 않습니다.
6. 최종 결과에 대한 책임은 AI가 아니라 제출자에게 있습니다.

좋은 프롬프트는 **역할·맥락 / 요구사항 / 제약 조건 / 출력 형식** 네 요소와 **검증 조건**을 갖춥니다. ([1주차 슬라이드](../weeks/week01/slides.pdf) 참고)

## 데이터셋

모든 데이터는 수업을 위해 만든 **가상 데이터**입니다. 노트북의 `get_data()`가 GitHub에서 자동으로 내려받으므로 따로 업로드할 필요가 없습니다.

| 파일 | 내용 | 사용 |
|---|---|---|
| [`students.csv`](../datasets/students.csv) | 학생 80명 성적·출석 | 6·10주 실습, **과제 1** |
| [`students_raw.csv`](../datasets/students_raw.csv) | 오류를 넣은 성적 파일 | 6주 실습 |
| [`survey_raw.csv`](../datasets/survey_raw.csv) · [`departments.csv`](../datasets/departments.csv) | 정제 전 설문, 학과 정보 | 11주 실습, 과제 2 선택지 |
| [`weather_daily.csv`](../datasets/weather_daily.csv) | 2025년 일별 기상 | 9·12·13주 실습, 과제 2 선택지 |
| [`cafe_sales.csv`](../datasets/cafe_sales.csv) | 캠퍼스 카페 1학기 판매 | 12~15주 실습, 과제 2 선택지 |

자세한 설명은 [데이터셋 안내](../datasets/README.md)를 확인합니다.

## 자주 묻는 질문

**Q. 셀을 실행했더니 `NameError`가 나요.**
위쪽 셀을 실행하지 않았을 가능성이 큽니다. **런타임 → 다시 시작 및 모두 실행**으로 처음부터 실행해 보세요.

**Q. 그래프의 한글이 □□로 보여요.**
노트북 첫 셀의 `koreanize_matplotlib` 설치 셀을 실행했는지 확인하세요. 설치 직후 한 번 더 실행하면 대부분 해결됩니다.

**Q. 연습 과제의 자동 확인에 ⏳가 나와요.**
`# TODO` 부분을 아직 작성하지 않았다는 뜻입니다. ❌는 실행은 되지만 결과가 틀렸다는 뜻이고, ✅가 나와야 통과입니다.

**Q. 데이터 파일을 찾을 수 없다고 나와요.**
데이터는 첫 실행 때 GitHub에서 내려받습니다. 인터넷 연결을 확인하고 해당 셀을 다시 실행하세요. 계속 안 되면 [datasets 폴더](../datasets/)에서 파일을 내려받아 Colab 왼쪽 **파일** 탭에 올리면 됩니다.

**Q. AI가 준 코드를 그대로 내도 되나요?**
직접 실행해 검증하고, 한 줄씩 설명할 수 있으며, AI 활용 기록을 남겼다면 됩니다. 설명할 수 없는 코드는 내지 마세요.

**Q. 수업을 하루 빠졌어요.**
그날 3개 주차의 `README.md` → `slides.pdf` → `practice.ipynb` 순서로 따라 하면 수업 내용을 거의 그대로 복습할 수 있습니다. 질문은 이메일로 보내 주세요.

## 관련 문서

- [과제 1: Python 성적 분석 미니 프로젝트](assignments/assignment01_python_problem_solving.md)
- [과제 2: AI 활용 데이터 분석 미니 프로젝트](assignments/assignment02_ai_data_analysis.md)
- [과제 3: AI 코드 디버깅·테스트·리팩토링 실기](assignments/assignment03_ai_debugging_refactoring.md)
- [전체 15주 수업 운영계획](../course/15-week-plan.md) (정규 학기 기준)
- [최종 프로젝트 루브릭](../rubrics/final-project-rubric.md)
- [AI 활용 기록지](../templates/ai-use-log.md)
- [저장소 첫 화면](../README.md)

---

**담당 교수:** 이영호 · 국립목포대학교 컴퓨터학부
**GitHub:** [MNU-AI-Programming/AI-Assisted-Python-Programming](https://github.com/MNU-AI-Programming/AI-Assisted-Python-Programming)
