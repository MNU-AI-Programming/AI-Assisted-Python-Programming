---
marp: true
theme: default
paginate: true
size: 16:9
header: "AI활용코딩연습 · Week 13"
footer: "국립목포대학교 컴퓨터학부 · 이영호"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
  section { font-family: "Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif; font-size: 25px; padding: 56px 64px; color: #1d2733; }
  h1 { color: #1f4e79; font-size: 1.45em; border-bottom: 3px solid #d6e4f2; padding-bottom: 6px; }
  h2 { color: #2e75b6; font-size: 1.1em; }
  strong { color: #c0392b; }
  code { font-size: 0.86em; }
  pre { font-size: 0.74em; line-height: 1.35; }
  table { font-size: 0.78em; }
  blockquote { border-left: 6px solid #2e75b6; background: #eef4fb; padding: 8px 18px; color: #1d2733; font-size: 0.92em; }
  header, footer { color: #8a99a8; font-size: 0.55em; }
  section.lead { justify-content: center; text-align: center; }
  section.lead h1 { font-size: 2.1em; border: none; }
  section.lead h2 { font-size: 1.3em; color: #2e75b6; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Week 13
## matplotlib 데이터 시각화

AI활용코딩연습(ZBE135)
이영호 교수 · 국립목포대학교 컴퓨터학부

---

# 지난주 돌아보기

| 발견 | 근거 |
|---|---|
| 아메리카노 · 라떼가 매출의 40% 이상 | 메뉴별 매출 비중 |
| 평일 점심, 특히 12시가 가장 바쁨 | 요일 × 시간대 일평균 |
| 기온↑ → 아이스 비율↑ (26% → 81%) | 상관 0.85 |
| 시험 주간 주문 증가 | 평일 비교 (10일) |

오늘: 이 발견을 **한눈에 전달되는 그래프**로

---

# 오늘의 목표

1. `fig, ax = plt.subplots()` **객체지향 방식**
2. **질문에 맞는 차트** 고르기 (추세 · 비교 · 분포 · 관계 · 구성)
3. 결론형 제목, 단위, 강조 색, 주석 → **메시지가 분명한 차트**
4. 나쁜 차트 고치기, **2×2 대시보드** 저장
5. AI 차트 코드를 **체크리스트 + 자동 점검**으로 검증

---

# 수업 흐름

| 구간 | 시간 | 활동 |
|---|---:|---|
| 도입 · 개념 | 20분 | Figure · Axes, 차트 선택 |
| 안내 실습 | 45분 | 차트 6종, 메시지 있는 차트 |
| 독립 · 짝 실습 | 35분 | 나쁜 차트 고치기, 대시보드 |
| 공유 · 점검 | 20분 | AI 차트 점검, 과제 안내 |

[이번 주 Colab 실습 열기](https://colab.research.google.com/github/MNU-AI-Programming/AI-Assisted-Python-Programming/blob/main/weeks/week13/practice.ipynb)

---

# Figure와 Axes

```text
Figure (종이 한 장)
 └── Axes (그래프 한 칸)
      ├── ax.set_title / set_xlabel / set_ylabel
      ├── ax.plot / bar / barh / hist / scatter / boxplot
      └── ax.legend
```

```python
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y, marker="o", label="값")
ax.set_title("제목"); ax.set_xlabel("x (단위)"); ax.set_ylabel("y (단위)")
ax.legend()
plt.show()
```

---

# 한글 폰트

```python
try:
    import koreanize_matplotlib
except ModuleNotFoundError:
    %pip install -q koreanize-matplotlib
    import koreanize_matplotlib
```

- Colab 기본 폰트에는 한글이 없어 □□□로 보인다
- `koreanize-matplotlib`가 나눔고딕을 설정해 준다

---

# 질문에 맞는 차트

| 질문 | 차트 | 메서드 |
|---|---|---|
| 시간에 따라? (추세) | 선 | `ax.plot` |
| 무엇이 더 큰가? (비교) | 막대, 항목 많으면 **가로 + 정렬** | `ax.bar`, `ax.barh` |
| 어떻게 퍼져 있나? (분포) | 히스토그램 | `ax.hist` |
| 그룹별 분포 | 상자 그림 | `ax.boxplot` |
| 관계가 있나? (관계) | 산점도 | `ax.scatter` |
| 전체 중 비율 (구성) | 정렬 막대 (파이는 2~3항목만) | `ax.barh` |

---

# ① 추세: 선 + 이동평균

```python
daily["ma7"] = daily["revenue"].rolling(7).mean()
fig, ax = plt.subplots(figsize=(9, 3.5))
ax.plot(daily["date"], daily["revenue"] / 1000, color="#BBBBBB", linewidth=1, label="일 매출")
ax.plot(daily["date"], daily["ma7"] / 1000, color="#1f4e79", linewidth=2.5, label="7일 이동평균")
ax.set_ylabel("매출 (천 원)")
ax.legend(loc="upper left")
```

원자료는 **연하게**, 추세는 **진하게**

---

# ② ③ 비교: 막대와 가로 막대

```python
by_wd = daily.groupby("weekday")["revenue"].mean().reindex(list("월화수목금토"))
ax.bar(by_wd.index, by_wd.values / 1000)          # 순서가 의미 있으면 그 순서로

menu = cafe.groupby("menu")["revenue"].sum().sort_values()
ax.barh(menu.index, menu.values / 10000)          # 항목이 많으면 가로 + 정렬
```

- 이름이 긴 항목 → **가로 막대**
- 순서가 없는 항목 → **크기순 정렬**

---

# ④ ⑤ 분포: 히스토그램과 상자 그림

```python
ax.hist(cafe["hour"], bins=range(8, 21), edgecolor="white")
ax.boxplot([daily.loc[daily["weekday"] == d, "revenue"] for d in order],
           tick_labels=order)          # matplotlib 3.9 이전: labels=
```

| 상자 그림 | 의미 |
|---|---|
| 상자 | 가운데 50% (Q1~Q3) |
| 가운데 선 | 중앙값 |
| 수염 · 점 | 일반 범위 · 이상값 후보 |

---

# ⑥ 관계: 산점도 + 추세선

```python
ax.scatter(daily["avg_temp"], daily["ice_ratio"] * 100, s=18, alpha=0.7)
slope, intercept = np.polyfit(daily["avg_temp"], daily["ice_ratio"] * 100, 1)
xs = np.linspace(daily["avg_temp"].min(), daily["avg_temp"].max(), 50)
ax.plot(xs, slope * xs + intercept, linestyle="--")
```

기온 1℃ 오를 때 아이스 비율 약 **2.9%p** — 상관이지 인과는 아니다

---

# 메시지가 분명한 차트

| 원칙 | 방법 |
|---|---|
| 제목 = 결론 | "메뉴별 매출" → "아메리카노가 매출의 4분의 1" |
| 축에 단위 | "매출 (만 원)", "평균기온 (℃)" |
| 하나만 강조 | 강조할 것만 진한 색, 나머지 회색 |
| 숫자 직접 표시 | `ax.bar_label`, `ax.annotate` |
| 군더더기 제거 | `ax.spines[["top", "right"]].set_visible(False)` |

---

# 강조 예

```python
share = menu / menu.sum() * 100
colors = ["#BBBBBB"] * (len(share) - 1) + ["#C0392B"]
bars = ax.barh(share.index, share.values, color=colors)
ax.bar_label(bars, fmt="%.1f%%", padding=3)
ax.set_title("아메리카노가 매출의 약 4분의 1을 차지한다",
             loc="left", fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)
```

```python
ax.axvspan(시작, 끝, color="#F4D03F", alpha=0.3)    # 기간 강조
ax.annotate("중간고사", xy=(x, y), xytext=(5, -5), textcoords="offset points")
```

---

# 나쁜 차트: 무엇이 문제인가?

```python
wd_mean = daily.groupby("weekday")["revenue"].mean()     # 가나다순
ax.bar(wd_mean.index, wd_mean.values,
       color=plt.cm.rainbow(np.linspace(0, 1, 6)))
ax.set_ylim(60000, 175000)
ax.set_title("data")
```

| 문제 | 고치기 |
|---|---|
| y축이 60,000부터 → 토요일이 거의 0처럼 | **막대는 0부터** |
| 금목수월토화 순서 | `reindex(["월", …])` |
| 무지개 색 | 한 색 + 강조 하나 |
| 제목 "data", 레이블 없음 | 결론형 제목, 단위 |

---

# 실습 1 · 2 (Level 1 → Level 2)

**Level 1 따라하기**
- Figure · Axes 구조, 차트 6종
- 결론형 제목 · 강조 · `bar_label` · 기간 강조

**Level 2 바꾸기**
- 나쁜 차트의 네 가지 문제를 모두 고치기
- 토요일만 강조해 "토요일 매출은 평일의 절반 이하" 메시지

---

# 실습 3 (Level 3): 대시보드

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("캠퍼스 카페 2025년 1학기 판매 요약", fontweight="bold")
axes[0, 0].plot(...)      # 추세
axes[0, 1].barh(...)      # 메뉴 비교
axes[1, 0].imshow(...)    # 요일 × 시간대 히트맵
axes[1, 1].scatter(...)   # 기온과 아이스 비율
fig.tight_layout()
fig.savefig("figures/cafe_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
```

`savefig`는 `show`보다 **먼저** · 날짜 겹침은 `DateFormatter("%m/%d")`

---

# 히트맵: 두 기준을 색으로

```python
heat = pivot.reindex(order).div(days_per_wd, axis=0) / 1000
im = ax.imshow(heat.values, cmap="Blues", aspect="auto")
ax.set_xticks(range(heat.shape[1]), heat.columns)
ax.set_yticks(range(heat.shape[0]), heat.index)
for i in range(heat.shape[0]):
    for j in range(heat.shape[1]):
        ax.text(j, i, f"{heat.values[i, j]:.0f}", ha="center", va="center")
fig.colorbar(im, ax=ax)
```

색만으로는 정확한 값을 읽기 어렵다 → **숫자를 함께**

---

# AI 차트 코드 점검: 자동으로

```python
def audit_chart(ax, kind="bar"):
    problems = []
    title = " ".join(ax.get_title(loc=l) for l in ("left", "center", "right")).strip()
    if not title or title.lower() in {"data", "chart", "plot"}:
        problems.append("제목이 없거나 의미 없음")
    if not ax.get_xlabel() and not ax.get_ylabel():
        problems.append("축 레이블 없음")
    if kind == "bar" and ax.get_ylim()[0] > 0:
        problems.append("막대 그래프의 y축이 0에서 시작하지 않음")
    if len({tuple(p.get_facecolor()) for p in ax.patches}) > 3:
        problems.append("색이 너무 많음")
    return problems
```

AI 차트: 4가지 문제 → 고친 차트: **문제 없음**

---

# 그래프도 테스트할 수 있다

| 확인 | 코드 |
|---|---|
| 제목 | `ax.get_title(loc="left")` |
| 축 레이블 | `ax.get_xlabel()`, `ax.get_ylabel()` |
| 막대 개수 · 길이 · 색 | `ax.patches`, `p.get_width()`, `p.get_facecolor()` |
| 선 데이터 | `ax.lines[0].get_ydata()` |
| 산점도 점 | `ax.collections[0].get_offsets()` |
| 축 범위 | `ax.get_ylim()` |

이번 주 과제의 자동 확인이 바로 이 방법

---

# AI에게 차트를 요청할 때

```text
daily(열: date, revenue(원), weekday('월'~'토'))로 요일별 일평균 매출 막대 그래프.
- fig, ax = plt.subplots() 객체지향 방식
- x축은 월~토 순서, y축은 천 원 단위, 0부터
- 제목은 결론 문장, 축에 단위
- 토요일만 빨간색, 나머지는 회색
- 한글 폰트는 koreanize_matplotlib
```

**차트 종류 · 순서 · 단위 · 강조 · 0 시작**을 명시

---

# 시각화 체크리스트

- [ ] 질문에 맞는 차트 종류인가?
- [ ] 제목이 결론을 말하는가? 축에 단위가 있는가?
- [ ] 막대는 0부터 시작하는가? 순서가 의미 있는가?
- [ ] 색은 의미가 있을 때만 쓰였는가?
- [ ] 그래프의 숫자가 표의 값과 일치하는가?
- [ ] 글자가 겹치지 않는가? 한글이 보이는가?

---

# 이번 주 과제 (10점)

| 문제 | 내용 | 배점 |
|---|---|---:|
| 1 | `plot_menu_share` 정렬 · 강조 · 값 표시 가로 막대 | 2 |
| 2 | `plot_trend` 일 매출 + 이동평균, 범례 | 2 |
| 3 | `plot_temp_ice` 산점도 + 추세선 + 기울기 | 3 |
| 4 | `make_dashboard` 2×2 대시보드 PNG 저장 (AI 협업) | 3 |

자동 확인이 **그래프 객체**(제목 · 막대 · 선 · 점)를 검사한다

---

# 자기 점검

1. 추세 · 비교 · 분포 · 관계에 맞는 차트는?
2. 막대 그래프의 y축을 0부터 시작해야 하는 이유는?
3. 항목이 11개인 비교 그래프를 가로 막대로 그리는 이유는?
4. "결론형 제목"의 예를 하나 들면?
5. `savefig`를 `show`보다 먼저 호출하는 이유는?

---

# 정리와 다음 주

| 오늘 | 핵심 |
|---|---|
| 구조 | `fig, ax = plt.subplots()` |
| 선택 | 추세 → 선, 비교 → 막대, 분포 → 히스토그램 · 상자, 관계 → 산점도 |
| 메시지 | 결론형 제목, 단위, 강조 하나, 값 표시 |
| 대시보드 | `subplots(2, 2)`, `suptitle`, `savefig(dpi=150)` |
| AI | 체크리스트 + 그래프 객체 자동 점검 |

**다음 주 · Week 14** AI 디버깅 · 테스트 · 리팩토링
