#!/usr/bin/env python3
from pathlib import Path

skill = Path(__file__).parents[1]
text = (skill / "SKILL.md").read_text(encoding="utf-8")
assert "name: data-cleaning" in text
assert "description:" in text
assert "scripts/smoke.py" in text
print("data-cleaning smoke test: PASS")
