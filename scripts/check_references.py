#!/usr/bin/env python3
from pathlib import Path
import re
import sys

skill = Path(sys.argv[1])
text = (skill / "SKILL.md").read_text(encoding="utf-8")
errors = []
for match in re.finditer(r"(?<![\w/])((?:scripts|references|assets)/[^\s)]+)", text):
    ref = match.group(1).rstrip(".,`\"")
    target = skill / ref
    if ".." in Path(ref).parts or not target.exists():
        errors.append(f"{skill / 'SKILL.md'}: missing or escaping resource {ref}")
if errors:
    print("Reference check: FAIL")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)
print(f"Reference check: PASS ({skill.name})")
