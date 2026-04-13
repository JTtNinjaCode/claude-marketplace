# JTtNinja Claude Marketplace

A personal Claude Code plugin marketplace — skills, MCP servers, and tools for everyday use.

## Plugins

| Plugin | Description |
|--------|-------------|
| [commit-convention](./plugins/commit-convention/) | Enforces conventional commit format — validates messages, suggests types, and blocks non-conforming commits |
| [english-learning](./plugins/english-learning/) | English learning skills for B2-level learners — vocabulary lookup, translation, exam solving, Anki export |
| [md-polish](./plugins/md-polish/) | Polishes Markdown files — fixes typos, punctuation, LaTeX formatting, and consistency. Auto-detects Traditional Chinese vs English |
| [terse](./plugins/terse/) | Terse communication mode — drops filler and pleasantries, keeps grammar and full technical accuracy. Always active via SessionStart hook |

## Installation

Add this marketplace to Claude Code:

```
/plugin marketplace add JTtNinjaCode/claude-marketplace
```

Then install a plugin:

```
/plugin install english-learning@jtt-ninja-marketplace
```

## Structure

```
claude-marketplace/
├── .claude-plugin/
│   └── marketplace.json       # Marketplace index
├── plugins/
│   ├── english-learning/      # Plugin directory
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── skills/            # Skill definitions
│   │   └── README.md
│   └── terse/                 # Plugin directory
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── hooks/             # SessionStart hook
│           └── terse.py
├── LICENSE
└── README.md
```

Each plugin can contain skills, MCP servers, hooks, agents, and more.

## License

MIT
