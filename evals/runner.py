#!/usr/bin/env python3
"""Small no-network smoke evaluator for sample skills."""
from pathlib import Path
import json

ROOT = Path(__file__).parents[1]
checks = []
for skill in sorted((ROOT / ".agents/skills").iterdir()):
    if not skill.is_dir():
        continue
    path = skill / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    checks.append({
        "task_id": f"smoke-{skill.name}",
        "skill": skill.name,
        "passed": text.startswith("---\n") and f"name: {skill.name}" in text and "description:" in text,
    })
summary = {"suite": "regression-smoke", "tasks": len(checks), "passed": sum(x["passed"] for x in checks), "results": checks}
print(json.dumps(summary, indent=2))
if summary["passed"] != summary["tasks"]:
    raise SystemExit(1)
