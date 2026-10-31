#!/usr/bin/env bash
# 모든 주차의 slides.md를 slides.pdf로 변환한다.
# 필요: Node.js, Marp CLI (npm i -g @marp-team/marp-cli)  또는 npx 사용
#   bash scripts/build_slides.sh          # 전체
#   bash scripts/build_slides.sh 3 4      # 일부 주차
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MARP="marp"
command -v marp >/dev/null 2>&1 || MARP="npx --yes @marp-team/marp-cli"
weeks=("$@")
if [ ${#weeks[@]} -eq 0 ]; then weeks=($(seq 1 15)); fi
for n in "${weeks[@]}"; do
  w=$(printf "week%02d" "$n")
  echo "▶ $w"
  $MARP -c "$ROOT/scripts/marp.config.js" "$ROOT/weeks/$w/slides.md" --pdf -o "$ROOT/weeks/$w/slides.pdf" </dev/null
done
