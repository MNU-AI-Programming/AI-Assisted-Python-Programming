# 데이터셋 안내

본 저장소의 데이터셋은 수업용 가상 데이터이며 실제 개인을 나타내지 않습니다.

| 파일 | 주요 용도 |
|---|---|
| scores.csv | 성적·출석·과제 분석 |
| expenses.csv | 날짜·범주별 지출 분석 |
| books.csv | 도서 분량·평점·장르 분석 |
| travel.csv | 도시별 여행 경비 분석 |
| survey.csv | 만족도·난이도·학습시간 분석 |

```python
import pandas as pd
url = "https://raw.githubusercontent.com/MNU-AI-Programming/AI-Assisted-Python-Programming/main/datasets/scores.csv"
df = pd.read_csv(url)
```
