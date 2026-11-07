#!/usr/bin/env python3
"""Sync Workato Labs (github.com/workato-devs) knowledge into the KB.

Only MIT-licensed repositories are copied, with their license and source commit recorded.

  recipe-skills         -> kb/patterns/workato-labs/   (skills, patterns, templates, lint-rules)
  recipe-lint (docs)    -> kb/patterns/workato-labs/lint/  (rule reference, rule authoring)
  dewy-resort           -> kb/examples/labs/dewy-resort/   (*.recipe.json)
  (workato-platform-cli docs/examples are NOT imported: they are synthetic snippets that use
   non-existent structures/providers and fail validation; importing them would teach wrong JSON.)

Repositories without a license (for example dewy-bank, AgentOrch) are intentionally NOT copied.

Usage: python3 kb/patterns/sync_labs.py
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATTERNS = ROOT / "kb" / "patterns" / "workato-labs"
EXAMPLES = ROOT / "kb" / "examples" / "labs"
GH = "https://github.com/workato-devs/{}.git"


def clone(repo: str, dest: Path) -> str:
    subprocess.run(["git", "clone", "-q", "--depth", "1", GH.format(repo), str(dest)], check=True)
    return subprocess.run(["git", "-C", str(dest), "log", "-1", "--format=%H %cs"],
                          check=True, capture_output=True, text=True).stdout.strip()


def license_ok(repo_dir: Path) -> Path | None:
    for name in ("LICENSE", "LICENSE.md", "LICENSE.txt"):
        p = repo_dir / name
        if p.exists() and "Permission is hereby granted, free of charge" in p.read_text():
            return p
    return None


def is_recipe(p: Path) -> bool:
    try:
        d = json.loads(p.read_text())
    except Exception:
        return False
    return isinstance(d, dict) and isinstance(d.get("code"), dict) and d["code"].get("keyword") == "trigger"


def main() -> None:
    sources = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for repo in ("recipe-skills", "recipe-lint", "dewy-resort"):
            d = tmp / repo
            rev = clone(repo, d)
            lic = license_ok(d)
            if not lic:
                print(f"skip {repo}: no MIT license found", file=sys.stderr)
                continue
            sources.append((repo, rev))

            if repo == "recipe-skills":
                if PATTERNS.exists():
                    shutil.rmtree(PATTERNS)
                shutil.copytree(d / "skills", PATTERNS / "skills")
                for f in ("README.md", "AGENTS.md"):
                    if (d / f).exists():
                        shutil.copy2(d / f, PATTERNS / f)
                if (d / "docs").exists():
                    shutil.copytree(d / "docs", PATTERNS / "docs")
                shutil.copy2(lic, PATTERNS / "LICENSE.md")
            elif repo == "recipe-lint":
                out = PATTERNS / "lint"
                out.mkdir(parents=True, exist_ok=True)
                for f in ("rule-reference.md", "rule-authoring.md"):
                    if (d / "docs" / f).exists():
                        shutil.copy2(d / "docs" / f, out / f)
                shutil.copy2(lic, out / "LICENSE.md")
            else:
                name = "dewy-resort" if repo == "dewy-resort" else "platform-cli"
                out = EXAMPLES / name
                if out.exists():
                    shutil.rmtree(out)
                n = 0
                for p in d.rglob("*.json"):
                    if "node_modules" in p.parts or "fixtures" in p.parts or not is_recipe(p):
                        continue
                    rel = p.relative_to(d)
                    target = out / rel
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(p, target)
                    n += 1
                shutil.copy2(lic, out / "LICENSE.md")
                print(f"{repo}: {n} recipes", file=sys.stderr)

    stamp = dt.datetime.now(dt.timezone.utc).date().isoformat()
    lines = ["# Sources", "", f"Synced {stamp} by `kb/patterns/sync_labs.py`. Content is © Workato, MIT License "
             "(see each folder's LICENSE.md). Unmodified copies; do not edit, re-sync instead.", ""]
    lines += [f"- `workato-devs/{r}` @ {rev}" for r, rev in sources]
    PATTERNS.mkdir(parents=True, exist_ok=True)
    (PATTERNS / "SOURCES.md").write_text("\n".join(lines) + "\n")
    print("done:", ", ".join(r for r, _ in sources), file=sys.stderr)


if __name__ == "__main__":
    main()
