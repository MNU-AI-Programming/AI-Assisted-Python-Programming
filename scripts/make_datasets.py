"""수업용 가상 데이터셋 생성 스크립트.

모든 데이터는 수업을 위해 만든 가상 데이터입니다. 실제 개인·기관 정보가 아닙니다.
시드를 고정했기 때문에 몇 번을 실행해도 같은 파일이 만들어집니다.

    python scripts/make_datasets.py
"""

from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datasets"
OUT.mkdir(exist_ok=True)

SURNAMES = list("김이박최정강조윤장임한오서신권황안송류전")
GIVEN = ["민준", "서연", "지호", "하은", "도윤", "지우", "예준", "수아", "시우", "서윤",
         "주원", "지민", "하준", "채원", "건우", "다은", "우진", "유진", "현우", "소율",
         "준서", "윤서", "태윤", "가은", "은호", "나연", "승민", "예린", "재원", "수빈"]

DEPARTMENTS = [
    ("컴퓨터공학과", "공과대학", "공학관"),
    ("정보보안학과", "공과대학", "공학관"),
    ("전자공학과", "공과대학", "제2공학관"),
    ("경영학과", "경영대학", "경영관"),
    ("간호학과", "간호대학", "보건관"),
]


def write_csv(name: str, header: list[str], rows: list[list]) -> None:
    path = OUT / name
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"{name}: {len(rows)}행")


def make_names(rng: np.random.Generator, n: int) -> list[str]:
    names: set[str] = set()
    while len(names) < n:
        names.add(rng.choice(SURNAMES) + rng.choice(GIVEN))
    return sorted(names, key=lambda _: rng.random())


# ---------------------------------------------------------------- students
def make_students() -> None:
    rng = np.random.default_rng(2026)
    n = 80
    names = make_names(rng, n)
    dept_weights = np.array([0.32, 0.18, 0.18, 0.17, 0.15])
    rows = []
    for i in range(n):
        dept = DEPARTMENTS[rng.choice(len(DEPARTMENTS), p=dept_weights)][0]
        year = int(rng.choice([1, 2, 3, 4], p=[0.15, 0.35, 0.3, 0.2]))
        ability = rng.normal(72, 12)
        midterm = int(np.clip(round(ability + rng.normal(0, 8)), 20, 100))
        final = int(np.clip(round(ability + rng.normal(2, 9)), 15, 100))
        assignment = int(np.clip(round(ability + rng.normal(8, 7)), 30, 100))
        attendance = int(np.clip(round(16 - abs(rng.normal(0, 2.2))), 6, 16))
        sid = f"2026{(i * 37) % 900 + 100:03d}{i % 10}"
        rows.append([sid, names[i], dept, year, midterm, final, assignment, attendance])
    # 과제 미제출(결측) 3명
    for idx in (11, 42, 67):
        rows[idx][6] = ""
    write_csv("students.csv",
              ["student_id", "name", "department", "year", "midterm", "final",
               "assignment", "attendance"], rows)


def make_students_raw() -> None:
    """6주차 파일·예외 처리 실습용: 일부 행에 일부러 오류를 넣은 성적 파일."""
    rows = [
        ["20261011", "김민준", "컴퓨터공학과", "2", "78", "85", "90", "15"],
        ["20261012", "이서연", "정보보안학과", "3", "92", "88", "95", "16"],
        ["20261013", "박지호", "전자공학과", "1", "65", "70", "", "14"],
        ["20261014", "", "경영학과", "2", "80", "75", "82", "16"],
        ["20261015", "정도윤", "컴퓨터공학과", "4", "abc", "77", "88", "13"],
        ["20261016", "강지우", "간호학과", "3", "88", "120", "91", "16"],
        ["20261017", "조예준", "컴퓨터공학과", "2", "71", "68", "75", "12"],
        ["20261018", "윤수아", "정보보안학과", "1", "-5", "60", "70", "15"],
        ["20261012", "이서연", "정보보안학과", "3", "92", "88", "95", "16"],
        ["20261019", "장시우", "전자공학과", "2", "84", "90", "86", "16"],
        ["20261020", "임서윤", "경영학과", "5", "77", "81", "79", "14"],
        ["20261021", "한주원", "간호학과", "3", "95", "93", "97", "16"],
        ["20261022", "오지민", "컴퓨터공학과", "2", " 82 ", "79", "85", "15"],
        ["20261023", "서하준", "정보보안학과", "4", "58", "62", "70", "9"],
        ["20261024", "신채원", "전자공학과", "1", "90", "", "92", "16"],
        ["20261025", "권건우", "경영학과", "2", "73", "76", "80", "20"],
        ["20261026", "황다은", "간호학과", "3", "86", "84", "89", "16"],
        ["20261027", "안우진", "컴퓨터공학과", "1", "69", "72", "74", "14"],
    ]
    write_csv("students_raw.csv",
              ["student_id", "name", "department", "year", "midterm", "final",
               "assignment", "attendance"], rows)


def make_departments() -> None:
    rows = [[d, c, b] for d, c, b in DEPARTMENTS]
    write_csv("departments.csv", ["department", "college", "building"], rows)


# ------------------------------------------------------------------ survey
def make_survey() -> None:
    rng = np.random.default_rng(11)
    n = 150
    dept_variants = {
        "컴퓨터공학과": ["컴퓨터공학과", "컴퓨터공학과", "컴공", " 컴퓨터공학과", "컴퓨터 공학과"],
        "정보보안학과": ["정보보안학과", "정보보안학과", "정보보안", "보안학과"],
        "전자공학과": ["전자공학과", "전자공학과", "전자공", "전자공학과 "],
        "경영학과": ["경영학과", "경영학과", "경영"],
        "간호학과": ["간호학과", "간호학과", "간호"],
    }
    yes_variants = ["예", "예", "Y", "yes", "사용함"]
    no_variants = ["아니오", "아니오", "N", "no", "사용안함"]
    start = datetime(2025, 9, 1, 9, 0)
    rows = []
    for i in range(n):
        dept = rng.choice(list(dept_variants))
        dept_text = rng.choice(dept_variants[dept])
        grade = int(rng.choice([1, 2, 3, 4], p=[0.2, 0.35, 0.3, 0.15]))
        grade_text = rng.choice([str(grade), str(grade), f"{grade}학년", f" {grade} "])
        uses_ai = rng.random() < (0.55 + 0.08 * grade)
        ai_text = rng.choice(yes_variants if uses_ai else no_variants)
        hours = max(0.0, round(rng.gamma(2.0, 0.9 + (0.4 if dept == "컴퓨터공학과" else 0)) * 2) / 2)
        r = rng.random()
        if r < 0.06:
            hours_text = ""
        elif r < 0.18:
            hours_text = f"{hours:g}시간"
        elif r < 0.22:
            hours_text = f"약 {hours:g}"
        else:
            hours_text = f"{hours:g}"
        sat = int(np.clip(round(3 + (0.6 if uses_ai else -0.3) + rng.normal(0, 0.9)), 1, 5))
        r = rng.random()
        if r < 0.05:
            sat_text = ""
        elif r < 0.12:
            sat_text = f"{sat}점"
        else:
            sat_text = str(sat)
        ts = start + timedelta(minutes=int(rng.integers(0, 60 * 24 * 14)))
        fmt = rng.choice(["%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M", "%Y/%m/%d %H:%M", "%Y.%m.%d %H:%M"])
        comments = ["", "", "", "실습이 더 많았으면 좋겠어요", "AI 답이 틀릴 때가 있어요",
                    "과제가 어려웠어요", "좋아요", "오류 메시지 읽는 법이 도움됨"]
        rows.append([f"R{i + 1:03d}", ts.strftime(fmt), dept_text, grade_text,
                     hours_text, ai_text, sat_text, rng.choice(comments)])
    # 이상값과 중복 응답
    rows[17][4] = "30"
    rows[88][4] = "25"
    rows[120][4] = "-1"
    for src in (5, 23, 60, 61, 99, 140):
        rows.append(list(rows[src]))
    order = rng.permutation(len(rows))
    rows = [rows[k] for k in order]
    write_csv("survey_raw.csv",
              ["response_id", "submitted_at", "department", "grade", "coding_hours",
               "uses_ai", "satisfaction", "comment"], rows)


# ----------------------------------------------------------------- weather
def make_weather() -> list[float]:
    rng = np.random.default_rng(7)
    days = [date(2025, 1, 1) + timedelta(days=k) for k in range(365)]
    rows = []
    temps = []
    for k, d in enumerate(days):
        seasonal = 14.5 - 11.5 * np.cos(2 * np.pi * (k - 18) / 365)
        avg = round(seasonal + rng.normal(0, 2.0), 1)
        spread = abs(rng.normal(7.5, 1.5))
        tmax = round(avg + spread / 2, 1)
        tmin = round(avg - spread / 2, 1)
        rainy_season = 1.0 + (2.5 if 170 <= k <= 215 else 0)
        rain = round(rng.gamma(0.9, 9) * rainy_season, 1) if rng.random() < 0.28 else 0.0
        humidity = int(np.clip(round(62 + 12 * np.sin(2 * np.pi * (k - 100) / 365)
                                     + (12 if rain > 0 else 0) + rng.normal(0, 6)), 25, 99))
        temps.append(avg)
        rows.append([d.isoformat(), avg, tmax, tmin, rain, humidity])
    for idx in (45, 200, 301):  # 관측 누락
        rows[idx][1] = ""
    write_csv("weather_daily.csv",
              ["date", "avg_temp", "max_temp", "min_temp", "precipitation_mm", "humidity"], rows)
    return temps


# -------------------------------------------------------------------- cafe
def make_cafe(temps: list[float]) -> None:
    rng = np.random.default_rng(3)
    menu = [  # 이름, 분류, 가격, 기본 인기, 아이스 가능
        ("아메리카노", "커피", 2500, 30, True),
        ("카페라떼", "커피", 3200, 18, True),
        ("바닐라라떼", "커피", 3700, 10, True),
        ("콜드브루", "커피", 3500, 6, False),
        ("녹차라떼", "논커피", 3500, 6, True),
        ("유자차", "논커피", 3000, 6, True),
        ("레몬에이드", "논커피", 3800, 5, False),
        ("초코라떼", "논커피", 3500, 5, True),
        ("크루아상", "디저트", 2800, 6, False),
        ("베이글", "디저트", 3000, 7, False),
        ("치즈케이크", "디저트", 4500, 3, False),
    ]
    names = [m[0] for m in menu]
    base = np.array([m[3] for m in menu], dtype=float)
    start = date(2025, 3, 3)
    end = date(2025, 6, 20)
    exam_weeks = {(date(2025, 4, 21) + timedelta(days=k)) for k in range(5)} | \
                 {(date(2025, 6, 16) + timedelta(days=k)) for k in range(5)}
    hours = np.arange(8, 20)
    hour_w = np.array([5, 9, 7, 6, 14, 12, 7, 6, 6, 5, 3, 2], dtype=float)
    hour_w /= hour_w.sum()
    rows = []
    oid = 1
    d = start
    while d <= end:
        temp = temps[(d - date(2025, 1, 1)).days]
        wd = d.weekday()
        if wd == 6:
            d += timedelta(days=1)
            continue
        n_orders = rng.poisson(14 if wd == 5 else 34)
        if d in exam_weeks:
            n_orders = int(n_orders * 1.35)
        ice_prob = float(np.clip(0.15 + (temp - 8) * 0.035, 0.08, 0.9))
        weights = base.copy()
        weights[names.index("레몬에이드")] *= 1 + max(0, temp - 15) * 0.12
        weights[names.index("콜드브루")] *= 1 + max(0, temp - 15) * 0.08
        weights[names.index("유자차")] *= max(0.25, 1.6 - temp * 0.05)
        weights /= weights.sum()
        for _ in range(n_orders):
            k = rng.choice(len(menu), p=weights)
            name, cat, price, _, ice_ok = menu[k]
            if cat == "디저트":
                temp_type = "-"
            elif name in ("콜드브루", "레몬에이드"):
                temp_type = "ICE"
            else:
                temp_type = "ICE" if (ice_ok and rng.random() < ice_prob) else "HOT"
            add = 300 if temp_type == "ICE" and cat != "디저트" and name not in ("콜드브루", "레몬에이드") else 0
            qty = int(rng.choice([1, 1, 1, 1, 1, 2, 2, 3]))
            h = int(rng.choice(hours, p=hour_w))
            m = int(rng.integers(0, 60))
            pay = rng.choice(["카드", "모바일", "현금"], p=[0.55, 0.38, 0.07])
            rows.append([f"O{oid:05d}", d.isoformat(), f"{h:02d}:{m:02d}", name, cat,
                         temp_type, price + add, qty, pay])
            oid += 1
        d += timedelta(days=1)
    rows.sort(key=lambda r: (r[1], r[2]))
    for i, r in enumerate(rows, 1):
        r[0] = f"O{i:05d}"
    write_csv("cafe_sales.csv",
              ["order_id", "date", "time", "menu", "category", "temp_type",
               "unit_price", "qty", "payment"], rows)


if __name__ == "__main__":
    make_students()
    make_students_raw()
    make_departments()
    make_survey()
    temps = make_weather()
    make_cafe(temps)
