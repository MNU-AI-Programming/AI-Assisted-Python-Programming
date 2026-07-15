# 데이터 사전

## scores.csv
| 열 | 자료형 | 범위/단위 | 설명 |
|---|---|---|---|
| name | str | - | 가상 학생 이름 |
| major | str | - | 전공 |
| score | int | 0~100점 | 시험 점수 |
| attendance | int | 0~100점 | 출석 환산 점수 |
| assignment | int | 0~100점 | 과제 점수 |

분석 예시: 전체 평균, 학과별 평균, 총점 파생변수, 점수 분포.

## expenses.csv
date는 YYYY-MM-DD, amount는 원 단위입니다. 범주별 합계와 날짜별 변화를 분석할 수 있습니다.

## books.csv
pages는 쪽 수, rating은 1~5점, genre는 도서 장르입니다.

## travel.csv
transport, food, lodging, activity는 모두 원 단위입니다.

## survey.csv
satisfaction, difficulty, interest는 1~5 척도이고 study_hours는 시간입니다.
