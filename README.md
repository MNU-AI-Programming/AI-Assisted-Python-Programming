# AI 활용 Python 프로그래밍
## AI-Assisted Python Programming — 15주 정규학기 패키지

> 이영호 교수 | 국립목포대학교 컴퓨터학부  
> Google Colab · GitHub · 생성형 AI를 활용한 15주 실습 중심 교과목

본 패키지는 기존 8개 Chapter의 입문 흐름을 정규학기 수준으로 확장합니다. Python 핵심 문법에서 시작해 함수, 파일, 클래스, NumPy, pandas, matplotlib, AI 디버깅·리팩토링을 거쳐 재현 가능한 데이터 분석 프로젝트로 마무리합니다.

## 빠른 시작

1. `course/15-week-plan.md`에서 운영·평가 계획을 확인합니다.
2. `weeks/week01`부터 해당 주차의 `README.md`와 `practice.ipynb`를 사용합니다.
3. 학생은 Colab에서 실습 후 `assignment.md` 형식으로 제출합니다.
4. 교수자는 `instructor/operation-guide.md`와 `instructor/quiz-answer-key.md`를 사용합니다.
5. 배포 전 `python scripts/validate_package.py --execute`로 전체 노트북을 점검합니다.

## 수업 기본값

| 항목 | 운영안 |
|---|---|
| 기간 | 15주 정규학기 |
| 기본 수업 | 주 2시간, 이론+안내 실습+독립 실습+피드백 |
| 확장 수업 | 주 3시간: 확장 과제·동료 코드 리뷰·프로젝트 클리닉 추가 |
| 선수 과목 | 교양필수 `AI 활용 프로그래밍` 이수 또는 Python 기초 |
| 환경 | Google Colab, GitHub, 생성형 AI |
| 핵심 평가 | 주차별 실습, 중간 실기, 최종 데이터 분석 프로젝트 |

## 저장소 구조

```text
AI-Assisted-Python-Programming/
├── README.md
├── SUMMARY.md
├── requirements.txt
├── course/                 # 15주 계획·평가·교과목 성과
├── weeks/week01~week15/    # 주차별 README·Colab·슬라이드·과제·퀴즈
├── assets/diagrams/        # 주차별 개념 순서도 SVG 15종
├── datasets/               # 수업용 가상 CSV 4종
├── projects/               # 중간·최종 프로젝트 안내
├── rubrics/                # 실습·중간·최종 평가표
├── templates/              # 학생 제출·AI 활용 기록 템플릿
├── instructor/             # 운영 가이드·퀴즈 정답
├── scripts/                # 패키지/노트북 검증
└── .github/workflows/      # 자동 검증
```

## 주차별 Colab

| 주차 | 주제 | 실행 |
|---:|---|---|
| 1 | AI 협업 코딩과 Colab 시작 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week01/practice.ipynb) |
| 2 | 입력·계산·문자열 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week02/practice.ipynb) |
| 3 | 조건문과 반복문으로 흐름 제어 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week03/practice.ipynb) |
| 4 | 리스트·튜플·집합·딕셔너리 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week04/practice.ipynb) |
| 5 | 함수·모듈·테스트 가능한 코드 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week05/practice.ipynb) |
| 6 | 파일·CSV·예외 처리 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/practice.ipynb) |
| 7 | 클래스와 객체지향 설계 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week07/practice.ipynb) |
| 8 | 중간 실기: Python 문제 해결 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week08/practice.ipynb) |
| 9 | NumPy와 배열 사고 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week09/practice.ipynb) |
| 10 | pandas로 데이터 불러오기와 탐색 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week10/practice.ipynb) |
| 11 | 데이터 정제·변환·집계 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week11/practice.ipynb) |
| 12 | 탐색적 데이터 분석과 프로젝트 기획 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week12/practice.ipynb) |
| 13 | matplotlib 데이터 시각화 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/practice.ipynb) |
| 14 | AI 디버깅·테스트·리팩토링 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week14/practice.ipynb) |
| 15 | 최종 프로젝트 발표와 재현성 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week15/practice.ipynb) |

## 학생 제출 원칙

- AI가 만든 코드는 반드시 직접 실행하고 설명합니다.
- 사용한 Prompt, 채택한 제안, 직접 수정한 부분과 이유를 기록합니다.
- 정상 사례와 경계·오류 사례를 함께 검증합니다.
- 개인정보, API 키, 타인의 결과물을 저장소에 올리지 않습니다.

## 기존 8개 Chapter 저장소와 통합

`MIGRATION.md`에 기존 부트캠프 자료를 보존하면서 이 15주 패키지를 병합하는 순서를 제시했습니다. 이 압축 파일은 GitHub를 직접 변경하지 않는 독립형 초안입니다.
