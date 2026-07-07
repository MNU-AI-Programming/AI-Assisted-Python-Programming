#!/usr/bin/env python3
"""
Update Google Colab links in this repository.

Usage:
    python tools/update_colab_links.py YOUR_GITHUB_ID
    python tools/update_colab_links.py YOUR_GITHUB_ID --repo AI-Programming-with-GenAI

This script replaces the placeholder GITHUB_ID in Markdown and Jupyter Notebook files.
"""

from pathlib import Path
import argparse
import json

def update_text_file(path: Path, github_id: str, repo_name: str):
    text = path.read_text(encoding="utf-8")
    old_text = text
    text = text.replace("GITHUB_ID/AI-Programming-with-GenAI", f"{github_id}/{repo_name}")
    text = text.replace("USERNAME/AI-Programming-with-GenAI", f"{github_id}/{repo_name}")
    text = text.replace("GITHUB_ID", github_id)
    if text != old_text:
        path.write_text(text, encoding="utf-8")
        return True
    return False

def update_notebook(path: Path, github_id: str, repo_name: str):
    nb = json.loads(path.read_text(encoding="utf-8"))
    old = json.dumps(nb, ensure_ascii=False)
    for cell in nb.get("cells", []):
        if isinstance(cell.get("source"), list):
            cell["source"] = [
                s.replace("GITHUB_ID/AI-Programming-with-GenAI", f"{github_id}/{repo_name}")
                 .replace("USERNAME/AI-Programming-with-GenAI", f"{github_id}/{repo_name}")
                 .replace("GITHUB_ID", github_id)
                for s in cell["source"]
            ]
    new = json.dumps(nb, ensure_ascii=False)
    if new != old:
        path.write_text(json.dumps(nb, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("github_id", help="Your GitHub username or organization name")
    parser.add_argument("--repo", default="AI-Programming-with-GenAI", help="Repository name")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    changed = []

    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.suffix.lower() in [".md", ".txt", ""] and path.is_file():
            try:
                if update_text_file(path, args.github_id, args.repo):
                    changed.append(path.relative_to(root))
            except UnicodeDecodeError:
                pass
        elif path.suffix.lower() == ".ipynb" and path.is_file():
            if update_notebook(path, args.github_id, args.repo):
                changed.append(path.relative_to(root))

    print("Updated Colab links.")
    for p in changed:
        print("-", p)

if __name__ == "__main__":
    main()
