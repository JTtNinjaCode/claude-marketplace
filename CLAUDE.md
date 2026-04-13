# Plugin Development Rules

## Versioning

Every plugin modification requires a version bump in `.claude-plugin/marketplace.json`.

Do **not** put `version` in `plugins/<name>/.claude-plugin/plugin.json` — per official docs, only one place is needed. This repo uses `marketplace.json` as the single source of truth.

- Bug fix or rule tweak → patch bump (1.0.0 → 1.0.1)
- New rule or behavior → minor bump (1.0.0 → 1.1.0)
- Breaking change → major bump (1.0.0 → 2.0.0)

This applies to all plugins in this repo: `terse`, `english-learning`, `commit-convention`.

## Git Workflow

Push directly to `main`. No feature branches or PRs.

## README Maintenance

When adding or modifying a plugin/skill, always check if `README.md` needs updating — especially the Plugins table (plugin list, descriptions).
