# AI활용코딩연습(ZBE135)

> **AI-Assisted Python Coding** · 이영호 교수 · 국립목포대학교 컴퓨터학부
> 문의: [youngho@ce.mokpo.ac.kr](mailto:youngho@ce.mokpo.ac.kr)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![Marp](https://img.shields.io/badge/Slides-Marp-0288D1)](https://marp.app/)
[![Course](https://img.shields.io/badge/Course-15%20Weeks-2E7D32)](course/15-week-plan.md)

생성형 AI를 **정답 생성기가 아니라 학습 파트너**로 활용하며 Python 문제 해결과 데이터 분석을 익히는 15주 교과목입니다. 학생은 매주 AI가 제안한 코드를 **읽고, 실행하고, 검증하고, 고치고, 기록**합니다. Python 핵심 문법에서 출발해 파일·예외·클래스, NumPy·pandas, 데이터 정제·탐색·시각화, AI 디버깅·테스트·리팩토링을 거쳐 **재현 가능한 데이터 분석 프로젝트**를 완성합니다.

본 교과목은 국립목포대학교 AI부트캠프사업단 과정이며, `AI활용프로그래밍`을 이수했거나 Python 기초 문법을 아는 학생을 대상으로 합니다.

## 교과목 개요

| 항목 | 내용 |
|---|---|
| 교과목 | AI활용코딩연습(ZBE135) |
| 운영 | 15주, **주 2시간** (도입 20분 · 안내 실습 45분 · 독립/짝 실습 35분 · 공유·점검 20분) |
| 선수 학습 | `AI활용프로그래밍` 이수 또는 Python 기초 |
| 실습 환경 | Google Colab, GitHub, 생성형 AI (ChatGPT, Gemini, Claude 등) |
| 주차별 자료 | Marp 슬라이드, 실습 노트북, 과제 노트북(3~4문제, 자동 확인 포함) |
| 평가 | 실습 참여, 주차별 과제, 중간 실기, 최종 프로젝트, 참여·동료 평가 |

## 학습 목표

1. Python의 자료형·제어문·자료구조·함수로 문제를 해결하고, 파일·예외·클래스로 프로그램을 구조화한다.
2. NumPy와 pandas로 데이터를 읽고 정제·변환·집계하며, 질문에서 출발하는 탐색적 분석을 수행한다.
3. matplotlib으로 메시지가 분명한 시각화를 만들고 근거와 한계를 함께 설명한다.
4. AI가 만든 코드를 **정상·경계·오류 사례와 테스트**로 검증하고, 디버깅·리팩토링하며 수정 근거를 기록한다.
5. 재현 가능한 분석 노트북·README·발표로 결과를 공유하고, AI 활용을 정직하게 공개한다.

## 수업 시작하기

**학생**

1. 해당 주차의 **안내(README)** 를 읽고 슬라이드를 봅니다.
2. **실습 노트북**을 Colab에서 열어 위에서 아래로 실행합니다. (예상 → 실행 → 비교 → 변경)
3. **과제 노트북**을 *드라이브에 사본 저장*한 뒤 `# TODO`를 채우고 자동 확인(✅)을 통과시킵니다.
4. 문제별 **AI 활용 기록**과 **성찰**을 작성하고, *다시 시작 및 모두 실행* 후 제출합니다.

**교수자**

1. [15주 운영 계획](course/15-week-plan.md)과 [교수자 운영 가이드](instructor/operation-guide.md)를 확인합니다.
2. 과제 모범답안은 [`instructor/solutions/`](instructor/solutions/)에 있습니다. (학생 배포 금지)
3. 자료를 고친 뒤에는 `python scripts/validate.py --execute`로 전체 노트북을 검증합니다.

## 15주 강의자료

| 주차 | 주제 | 핵심 실습 | 자료 | 실습 | 과제 |
|---:|---|---|---|---|---|
| 1 | AI 협업 코딩과 Colab 시작 | 수강 준비 진단, 자기소개 카드 | [안내](weeks/week01/README.md) · [슬라이드](weeks/week01/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week01/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week01/assignment.ipynb) · [안내](weeks/week01/assignment.md) |
| 2 | 입력 · 계산 · 문자열 | 여행 경비 계산기, 정산 검증 | [안내](weeks/week02/README.md) · [슬라이드](weeks/week02/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/assignment.ipynb) · [안내](weeks/week02/assignment.md) |
| 3 | 조건문과 반복문 | 장학 기준 판정기, 경계값 표 | [안내](weeks/week03/README.md) · [슬라이드](weeks/week03/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/assignment.ipynb) · [안내](weeks/week03/assignment.md) |
| 4 | 리스트 · 튜플 · 집합 · 딕셔너리 | 학생 성적 레코드 분석 | [안내](weeks/week04/README.md) · [슬라이드](weeks/week04/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/assignment.ipynb) · [안내](weeks/week04/assignment.md) |
| 5 | 함수 · 모듈 · 테스트 가능한 코드 | 성적 계산 모듈 | [안내](weeks/week05/README.md) · [슬라이드](weeks/week05/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/assignment.ipynb) · [안내](weeks/week05/assignment.md) |
| 6 | 파일 · CSV · 예외 처리 | 오류에 견고한 성적 파일 처리기 | [안내](weeks/week06/README.md) · [슬라이드](weeks/week06/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/assignment.ipynb) · [안내](weeks/week06/assignment.md) |
| 7 | 클래스와 객체지향 설계 | 도서 대출 관리 시스템 | [안내](weeks/week07/README.md) · [슬라이드](weeks/week07/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/assignment.ipynb) · [안내](weeks/week07/assignment.md) |
| 8 | **중간 실기**: Python 문제 해결 | 모의 실기 → 성적 분석 미니 프로젝트 | [안내](weeks/week08/README.md) · [슬라이드](weeks/week08/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week08/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week08/assignment.ipynb) · [안내](weeks/week08/assignment.md) |
| 9 | NumPy와 배열 사고 | 1년치 기온 데이터 분석 | [안내](weeks/week09/README.md) · [슬라이드](weeks/week09/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/assignment.ipynb) · [안내](weeks/week09/assignment.md) |
| 10 | pandas로 데이터 불러오기와 탐색 | 성적 데이터 탐색 보고 | [안내](weeks/week10/README.md) · [슬라이드](weeks/week10/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/assignment.ipynb) · [안내](weeks/week10/assignment.md) |
| 11 | 데이터 정제 · 변환 · 집계 | 설문 데이터 정제 파이프라인 | [안내](weeks/week11/README.md) · [슬라이드](weeks/week11/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/assignment.ipynb) · [안내](weeks/week11/assignment.md) |
| 12 | 탐색적 데이터 분석과 프로젝트 기획 | 카페 판매 EDA, 프로젝트 제안서 | [안내](weeks/week12/README.md) · [슬라이드](weeks/week12/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/assignment.ipynb) · [안내](weeks/week12/assignment.md) |
| 13 | matplotlib 데이터 시각화 | 카페 판매 대시보드 | [안내](weeks/week13/README.md) · [슬라이드](weeks/week13/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/assignment.ipynb) · [안내](weeks/week13/assignment.md) |
| 14 | AI 디버깅 · 테스트 · 리팩토링 | 결함 있는 분석 코드 진단 | [안내](weeks/week14/README.md) · [슬라이드](weeks/week14/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/assignment.ipynb) · [안내](weeks/week14/assignment.md) |
| 15 | **최종 프로젝트 발표**와 재현성 | 재현성 점검, 5분 발표 | [안내](weeks/week15/README.md) · [슬라이드](weeks/week15/slides.md) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/practice.ipynb) | [Colab](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/assignment.ipynb) · [안내](weeks/week15/assignment.md) |

각 주차 폴더의 `slides.pdf`는 `slides.md`를 Marp로 변환한 파일입니다.

## 매주 같은 흐름

모든 실습 노트북은 같은 단계로 진행합니다.

| 단계 | 활동 |
|---|---|
| **Level 1 따라하기** | 짧은 코드의 결과를 예상한 뒤 실행하고 비교 |
| **Level 2 바꾸기** | 값·조건·기준을 바꾸고 결과 변화를 설명 |
| **Level 3 적용하기** | 여러 개념을 조합한 미니 프로젝트, 정상·경계 사례 검증 |
| **Level 4 AI와 함께** | AI가 만든 코드의 결함을 테스트로 찾고, 프롬프트를 개선하고, 기록 |

과제 노트북은 문제마다 **자동 확인 셀**(✅/❌/⏳)이 있어 스스로 검증할 수 있고, 마지막 문제는 항상 **AI 협업 + 기록**입니다.

## 평가

| 항목 | 비율 | 근거 |
|---|---:|---|
| 실습 참여 | 15% | 실습 노트북 실행·변경 기록 |
| 주차별 과제 | 25% | [주차별 과제 루브릭](rubrics/weekly-assignment-rubric.md) |
| 중간 실기 (8주) | 20% | [중간 실기 안내](projects/midterm-project.md) · [루브릭](rubrics/midterm-rubric.md) |
| 최종 프로젝트 (12~15주) | 35% | [최종 프로젝트 안내](projects/final-project.md) · [루브릭](rubrics/final-project-rubric.md) |
| 참여·동료 평가 | 5% | 질문, 코드 리뷰, 발표 동료 평가 |

비율은 학기별 운영 상황에 따라 조정될 수 있으며, 수업 첫 주에 공지합니다.

## 데이터셋

모든 데이터는 수업을 위해 만든 **가상 데이터**입니다. [`scripts/make_datasets.py`](scripts/make_datasets.py)로 언제든 같은 파일을 다시 만들 수 있습니다.

| 파일 | 내용 | 주로 쓰는 주차 |
|---|---|---|
| [`students.csv`](datasets/students.csv) | 학생 80명 성적·출석 (과제 결측 3명) | 6, 8, 10 |
| [`students_raw.csv`](datasets/students_raw.csv) | 일부러 오류를 넣은 성적 파일 18행 | 6 |
| [`survey_raw.csv`](datasets/survey_raw.csv) | 표기가 제각각인 설문 156행 (중복·결측·이상값) | 11 |
| [`departments.csv`](datasets/departments.csv) | 학과 → 단과대학 | 11 |
| [`weather_daily.csv`](datasets/weather_daily.csv) | 2025년 일별 기온·강수·습도 (결측 3일) | 9, 12~15 |
| [`cafe_sales.csv`](datasets/cafe_sales.csv) | 캠퍼스 카페 1학기 판매 3,019행 | 12~15 |

자세한 설명은 [데이터셋 안내](datasets/README.md)를 참고하세요. Colab에서는 노트북의 `get_data()`가 GitHub에서 파일을 자동으로 내려받습니다.

## 생성형 AI 활용 원칙

1. AI가 만든 코드는 **직접 실행하고 한 줄씩 설명할 수 있을 때만** 제출합니다.
2. 사용한 프롬프트, 채택한 제안, 직접 고친 부분과 이유를 [AI 활용 기록](templates/ai-use-log.md)에 남깁니다.
3. 정상 사례뿐 아니라 **경계값과 오류 사례**로 검증합니다. AI가 만든 테스트에는 **내 테스트를 하나 이상** 더합니다.
4. AI의 설명과 결론은 **실행 결과와 근거**로 확인합니다. (상관을 인과로 말하는 문장, 과장된 수치에 주의)
5. 개인정보, 비밀번호, API 키, 다른 사람의 과제를 프롬프트에 넣지 않습니다.
6. 중간 실기처럼 AI 사용 범위가 정해진 평가는 공지를 따릅니다. 사용 자체는 감점 대상이 아니지만, **사용을 숨기는 것은 부정행위**입니다.

## 저장소 구조

```text
AI-Assisted-Python-Programming/
├── weeks/week01~week15/     # README, slides.md(.pdf), practice.ipynb, assignment.ipynb, assignment.md
├── instructor/              # 교수자 운영 가이드, solutions/ (과제 모범답안)
├── course/                  # 15주 운영 계획
├── projects/                # 중간 실기, 최종 프로젝트 안내
├── rubrics/                 # 주차별 과제·중간 실기·최종 프로젝트 루브릭
├── templates/               # AI 활용 기록, 최종 프로젝트 노트북·README·제안서 템플릿
├── datasets/                # 수업용 가상 데이터
├── scripts/                 # 데이터 생성, 노트북 검증, 슬라이드 변환
├── 2026_여름학기/           # 2026년 여름학기 공지·과제
├── 2026_가을학기/           # 2026년 가을학기 공지·과제
├── old/                     # 이전 버전 강의자료 (개편 전 주차 자료, Chapter 기반 자료)
├── requirements.txt
└── SUMMARY.md
```

## 로컬 실행과 검증

대부분의 실습은 Colab에서 바로 실행됩니다. 로컬에서 실행하려면:

```bash
git clone https://github.com/MNU-AI-Programming/AI-Assisted-Python-Programming.git
cd AI-Assisted-Python-Programming
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

```bash
python scripts/validate.py --execute               # 전체 노트북 실행 검증
python scripts/validate.py --execute --weeks 3 4   # 일부 주차만
bash scripts/build_slides.sh                       # 모든 slides.md → slides.pdf (Marp CLI 필요)
```

`validate.py`는 실습 노트북이 끝까지 실행되는지, 모범답안의 자동 확인이 모두 통과하는지, 학생용 과제 노트북에 미작성(`NotImplementedError`) 외의 오류가 없는지 확인합니다.

## 이전 자료

- 개편 전 주차 자료와 영상 대본은 [`old/`](old/)에, 그보다 이전의 Chapter 기반 자료는 [`old/old-chapter-based/`](old/old-chapter-based/)에 보존되어 있습니다.
- 2026년 여름·가을학기 집중과정 공지와 과제는 [`2026_여름학기/`](2026_여름학기/), [`2026_가을학기/`](2026_가을학기/)에 있습니다.

## 라이선스 및 이용

이 저장소의 자료는 국립목포대학교 「AI활용코딩연습(ZBE135)」 수업을 위해 제작되었습니다. 외부에서 활용·수정·재배포할 때는 출처를 밝혀 주세요.

---

**담당 교수:** 이영호 · 국립목포대학교 컴퓨터학부
**GitHub:** [MNU-AI-Programming/AI-Assisted-Python-Programming](https://github.com/MNU-AI-Programming/AI-Assisted-Python-Programming)
