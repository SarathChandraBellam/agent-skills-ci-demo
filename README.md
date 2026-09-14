# Agent Skills CI Demo

A small reference repository for publishing Agent Skills with GitHub Actions.

## Included sample skills

- `data-cleaning`: a CSV-cleaning workflow with a bundled smoke test.
- `report-generation`: a Markdown-report workflow with a bundled smoke test.

## GitHub Actions

- `ci-pr.yml` runs on pull requests, discovers changed skills, runs the pinned `skills-ref` specification validator, applies repository policy checks, checks resource references, runs smoke tests, and executes a deterministic regression smoke suite.
- `ci-main.yml` is the intended main-branch integrity entry point.
- `eval.yml` runs the deterministic regression suite nightly and on manual dispatch.

The workflows use read-only permissions, concurrency cancellation, matrix validation, short-lived PR artifacts, and a pinned revision of `skills-ref`. Third-party Actions are referenced by full commit SHA.

## Local checks

```bash
python3 scripts/check_skill_policy.py .agents/skills
python3 scripts/check_references.py .agents/skills/data-cleaning
python3 scripts/check_references.py .agents/skills/report-generation
python3 .agents/skills/data-cleaning/scripts/smoke.py
python3 .agents/skills/report-generation/scripts/smoke.py
python3 evals/runner.py
```

## Extension points

For a production repository, add task fixtures under `evals/tasks/`, deterministic outcome verifiers, paired with-skill/no-skill trials, model-judge diagnostics, trace retention, and a protected release workflow. Keep model credentials out of pull-request jobs.
