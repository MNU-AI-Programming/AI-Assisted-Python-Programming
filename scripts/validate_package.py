#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"README.md", "practice.ipynb", "slides.md", "assignment.md", "quiz.md"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="15개 노트북을 실제 실행합니다.")
    args = parser.parse_args()
    errors = []

    for number in range(1, 16):
        week = ROOT / "weeks" / f"week{number:02d}"
        missing = REQUIRED - {p.name for p in week.iterdir()} if week.exists() else REQUIRED
        if missing:
            errors.append(f"week{number:02d}: 누락 {sorted(missing)}")
            continue
        notebook_path = week / "practice.ipynb"
        try:
            notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
            if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
                raise ValueError("유효한 nbformat 4 노트북이 아닙니다.")
            notebook_source = "\n".join(
                "".join(cell.get("source", [])) for cell in notebook["cells"]
            )
            for level in range(1, 5):
                if f"Level {level}" not in notebook_source:
                    raise ValueError(f"Level {level} 단계가 노트북에 없습니다.")

            slides_text = (week / "slides.md").read_text(encoding="utf-8")
            slide_count = slides_text.count("\n---\n")
            if slide_count != 15:
                raise ValueError(f"슬라이드 수가 15장이 아닙니다: {slide_count}장")
            diagram_path = ROOT / "assets" / "diagrams" / f"week{number:02d}-flow.svg"
            if not diagram_path.exists():
                raise ValueError("주차별 개념 순서도 SVG가 없습니다.")
            ET.parse(diagram_path)
            relative_diagram = f"../../assets/diagrams/week{number:02d}-flow.svg"
            if relative_diagram not in slides_text:
                raise ValueError("슬라이드에 개념 순서도 경로가 없습니다.")
            code_blocks = re.findall(r"```python\n(.*?)\n```", slides_text, flags=re.DOTALL)
            if len(code_blocks) < 3:
                raise ValueError("슬라이드에 Level 1~3 Python 코드가 모두 없습니다.")
            notebook_code = "\n".join(
                "".join(cell.get("source", []))
                for cell in notebook["cells"]
                if cell.get("cell_type") == "code"
            )
            for block in code_blocks[:3]:
                snippet = "\n".join(
                    line for line in block.splitlines()
                    if not line.startswith("# ...")
                ).strip()
                if snippet and snippet not in notebook_code:
                    raise ValueError("슬라이드 코드가 Colab 노트북과 일치하지 않습니다.")
            if args.execute:
                source = "\n\n".join(
                    "".join(cell.get("source", []))
                    for cell in notebook["cells"]
                    if cell.get("cell_type") == "code"
                )
                env = os.environ.copy()
                env.setdefault("MPLBACKEND", "Agg")
                result = subprocess.run(
                    [sys.executable, "-c", source],
                    cwd=week,
                    env=env,
                    text=True,
                    capture_output=True,
                    timeout=120,
                )
                if result.returncode:
                    raise RuntimeError(result.stderr[-1500:])
        except Exception as exc:
            errors.append(f"week{number:02d}: {type(exc).__name__}: {exc}")

    if errors:
        print("검증 실패")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("검증 통과: 15개 주차 파일과 노트북" + (" 실행" if args.execute else " 형식"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
