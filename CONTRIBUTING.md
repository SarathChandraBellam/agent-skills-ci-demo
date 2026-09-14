# Contributing

Add skills under `.agents/skills/<skill-name>/`.

Each skill must contain an exact uppercase `SKILL.md` with YAML frontmatter containing `name` and `description`. The `name` must match the directory name and use ASCII lowercase letters, digits, and single hyphens. Keep the activated instructions concise and put detailed material in `references/`.

Pull requests must pass the Skill CI workflow. Do not add secrets to skills or workflows. Bundled scripts are treated as executable code and must include a deterministic smoke test.
