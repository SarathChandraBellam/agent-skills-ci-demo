---
name: data-cleaning
description: Clean small tabular datasets by normalizing headers, trimming text, removing blank rows, and reporting duplicate records. Use when a user asks to tidy or prepare CSV data for analysis.
license: MIT
metadata:
  author: example-org
  version: "0.1.0"
---

# Data cleaning

Use this skill when the task is to prepare a small CSV or table for downstream analysis.

## Workflow

1. Inspect the input columns and identify the likely header row.
2. Normalize headers to lowercase `snake_case` without losing meaning.
3. Trim leading and trailing whitespace from text cells.
4. Remove rows that are completely blank.
5. Preserve values unless the user explicitly requests coercion or deduplication.
6. Report duplicate rows separately before removing them.
7. Write the cleaned result and a short summary of changes.

## Output requirements

Return the cleaned file, the row and column counts before and after cleaning, and any assumptions made. Keep the original file unchanged.

## Script

For a deterministic smoke test, run `scripts/smoke.py`.
