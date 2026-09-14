#!/usr/bin/env python3
"""Repository-specific checks beyond skills-ref."""
from pathlib import Path
import re
import sys

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".agents/skills")
errors = []
seen = set()

for skill_dir in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{skill_dir}: missing exact uppercase SKILL.md")
        continue
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"{skill_file}: invalid frontmatter delimiters")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill_file}: exceeds 500-line progressive-disclosure budget")
    match = re.search(r"^name:\s*([^\s]+)\s*$", text, re.MULTILINE)
    if not match:
        errors.append(f"{skill_file}: missing name")
    else:
        name = match.group(1)
        if name != skill_dir.name:
            errors.append(f"{skill_file}: name {name!r} does not match directory {skill_dir.name!r}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{skill_file}: name must use ASCII lowercase letters, digits, and single hyphens")
        if name in seen:
            errors.append(f"duplicate skill name: {name}")
        seen.add(name)
    for token in ("scripts/", "references/", "assets/"):
        for line in text.splitlines():
            if token in line and "scripts/smoke.py" not in line and line.strip().startswith("/"):
                errors.append(f"{skill_file}: absolute resource path is not allowed")

if errors:
    print("Skill policy check: FAIL")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)
print(f"Skill policy check: PASS ({len(seen)} skills)")
