# Plugin Development Rules

## Versioning

Every plugin modification requires a version bump in `plugins/<name>/.claude-plugin/plugin.json`.

- Bug fix or rule tweak → patch bump (1.0.0 → 1.0.1)
- New rule or behavior → minor bump (1.0.0 → 1.1.0)
- Breaking change → major bump (1.0.0 → 2.0.0)

This applies to all plugins in this repo: `terse`, `english-learning`, `commit-convention`.
