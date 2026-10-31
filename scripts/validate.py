"""강의자료 검증 스크립트.

    python scripts/validate.py              # 구조만 검사
    python scripts/validate.py --execute    # 노트북까지 실행해 검사
    python scripts/validate.py --execute --weeks 3 4

검사 내용
1. 주차마다 README.md, slides.md, practice.ipynb, assignment.md, assignment.ipynb가 있는지
2. 교수자용 모범답안(instructor/solutions/weekNN_solution.ipynb)이 있는지
3. (--execute) 실습 노트북이 오류 없이 끝까지 실행되는지
4. (--execute) 모범답안 노트북의 모든 자동 확인이 통과하는지
5. (--execute) 학생용 과제 노트북은 '미작성(NotImplementedError)' 외의 오류가 없는지
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEK_FILES = ["README.md", "slides.md", "practice.ipynb", "assignment.md", "assignment.ipynb"]


def outputs_text(nb) -> str:
    chunks = []
    for cell in nb.cells:
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                chunks.append(out.get("text", ""))
            elif out.get("output_type") == "error":
                chunks.append(f"{out.get('ename')}: {out.get('evalue')}")
            else:
                chunks.append(str(out.get("data", {}).get("text/plain", "")))
    return "\n".join(chunks)


def execute(path: Path, allow_errors: bool = False, timeout: int = 300):
    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3",
                            allow_errors=allow_errors,
                            resources={"metadata": {"path": str(path.parent)}})
    # 노트북이 실행 중에 만든 파일(모듈, 결과 CSV, 그림 등)은 검증 후 지운다.
    before = {p for p in path.parent.rglob("*")}
    try:
        client.execute()
    finally:
        for p in sorted(set(path.parent.rglob("*")) - before, reverse=True):
            if p.is_dir():
                p.rmdir() if not any(p.iterdir()) else None
            else:
                p.unlink()
    return nb


def check_week(n: int, run: bool) -> list[str]:
    problems = []
    week = ROOT / "weeks" / f"week{n:02d}"
    for name in WEEK_FILES:
        if not (week / name).exists():
            problems.append(f"week{n:02d}: {name} 없음")
    sol = ROOT / "instructor" / "solutions" / f"week{n:02d}_solution.ipynb"
    if not sol.exists():
        problems.append(f"week{n:02d}: 모범답안 없음")
    if not run or problems:
        return problems

    try:
        execute(week / "practice.ipynb")
    except Exception as exc:  # noqa: BLE001
        problems.append(f"week{n:02d}: practice 실행 오류 - {str(exc).strip().splitlines()[-1]}")

    try:
        nb = execute(sol)
        text = outputs_text(nb)
        for mark in ("❌", "⏳"):
            if mark in text:
                bad = [line for line in text.splitlines() if mark in line]
                problems.append(f"week{n:02d}: 모범답안 확인 실패 {bad[:3]}")
                break
        if "✅" not in text:
            problems.append(f"week{n:02d}: 모범답안에서 통과 표시를 찾지 못함")
    except Exception as exc:  # noqa: BLE001
        problems.append(f"week{n:02d}: 모범답안 실행 오류 - {str(exc).strip().splitlines()[-1]}")

    try:
        nb = execute(week / "assignment.ipynb", allow_errors=True)
        for cell in nb.cells:
            for out in cell.get("outputs", []):
                if out.get("output_type") == "error" and out.get("ename") != "NotImplementedError":
                    problems.append(f"week{n:02d}: 과제 노트북 예상 밖 오류 {out.get('ename')}: {out.get('evalue')}")
    except Exception as exc:  # noqa: BLE001
        problems.append(f"week{n:02d}: 과제 노트북 실행 오류 - {exc}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="노트북을 실제로 실행")
    parser.add_argument("--weeks", type=int, nargs="*", default=list(range(1, 16)))
    args = parser.parse_args()

    all_problems = []
    for n in args.weeks:
        problems = check_week(n, args.execute)
        status = "OK" if not problems else "문제 있음"
        print(f"week{n:02d}: {status}")
        for p in problems:
            print("   -", p)
        all_problems += problems
    print("\n총 문제:", len(all_problems))
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
