# Week 06 과제 — 파일 · CSV · 예외 처리

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week06/assignment.ipynb)

## 과제 구성 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | 안전한 정수 변환 | 2 |
| 2 | 메모 파일 다루기 | 2 |
| 3 | CSV 학과별 평균 | 3 |
| 4 | 검증 보고서 만들기 (AI 협업) | 3 |

### 문제 1. 안전한 정수 변환 (2점)

`safe_int(text, default, low, high)`가 변환 실패나 범위 밖이면 기본값을 돌려주도록 `try/except ValueError`로 작성합니다.

### 문제 2. 메모 파일 다루기 (2점)

덮어쓰기·이어 쓰기·내용 있는 줄 세기 함수를 만들고, 없는 파일은 `FileNotFoundError`를 처리해 0을 돌려줍니다.

### 문제 3. CSV 학과별 평균 (3점)

`csv.DictReader`로 `students.csv`를 읽어 학과별 평균을 구하고, 빈 칸·숫자가 아닌 값은 건너뜁니다.

### 문제 4. 검증 보고서 만들기 (AI 협업) (3점)

수강 신청 CSV를 규칙 순서대로 검증해 정상 행을 돌려주고, 줄 번호와 이유가 담긴 오류 보고서 CSV를 저장합니다.

## 제출 방법

1. Colab에서 `assignment.ipynb`를 열고 **파일 → 드라이브에 사본 저장**을 누릅니다.
2. 파일 이름을 `week06_학번_이름.ipynb`로 바꿉니다.
3. `# TODO` 부분을 채우고 각 문제 아래 **자동 확인 셀**이 ✅인지 확인합니다.
4. 문제별 **AI 활용 기록**과 마지막 **성찰**을 작성합니다. AI를 쓰지 않았다면 "사용 안 함"이라고 씁니다.
5. **런타임 → 다시 시작 및 모두 실행** 후 오류가 없으면 `.ipynb` 파일을 LMS에 제출합니다.

## 채점 기준

문제별 배점은 다음 비율로 나누어 채점합니다. 자세한 기준은 [주차별 과제 루브릭](../../rubrics/weekly-assignment-rubric.md)을 따릅니다.

| 기준 | 비율 | 확인 내용 |
|---|---:|---|
| 기능 | 50% | 자동 확인 통과, 요구사항 충족 |
| 검증 | 20% | 정상·경계·오류 사례를 직접 확인했는지 |
| 이해 | 15% | 코드와 수정 이유를 자신의 말로 설명했는지 |
| AI 활용 기록·성찰 | 15% | 프롬프트, 채택·수정 내용, 성찰의 구체성 |

> 자동 확인은 최소 기준입니다. 자동 확인만 통과하도록 결과값을 직접 써 넣는(하드코딩) 코드는 기능 점수를 받지 못합니다.
