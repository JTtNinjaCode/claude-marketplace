# Claude Marketplace

A personal collection of Claude Code skill plugins.

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| english-learn | `/english-learn [input] [-s]` | English learning assistant — translate words/phrases/sentences, solve exam questions, and process images. Add `-s` to save to vocabulary list. |
| english-quiz | `/english-quiz` | Fill-in-the-blank quiz pulled from your local `vocabulary.json`. 3 questions per round with instant feedback. |

## Installation

```bash
/plugin install <path-or-url>
```

## Adding a New Skill

Create a new directory under `skills/` with a `SKILL.md` inside:

```
skills/
  <skill-name>/
    SKILL.md
```

## License

MIT
