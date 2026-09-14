---
name: report-generation
description: Generate concise Markdown reports from structured findings with an executive summary, evidence table, risks, and recommended next steps. Use when a user asks to turn research or analysis into a decision-ready report.
license: MIT
metadata:
  author: example-org
  version: "0.1.0"
---

# Report generation

Use this skill when the user needs structured findings converted into a decision-ready Markdown report.

## Workflow

1. Identify the decision the report should support.
2. Separate observed evidence from interpretation and recommendations.
3. Start with a concise executive summary.
4. Organize findings in a table with clear source or evidence fields.
5. State material risks, limitations, and unresolved questions.
6. End with prioritized recommendations and concrete next steps.
7. Check that every factual claim is traceable to an input source.

## Output requirements

Use Markdown headings, short paragraphs, and tables where comparison helps. Avoid inventing facts. If evidence is incomplete, say so explicitly.

## Script

For a deterministic smoke test, run `scripts/smoke.py`.
