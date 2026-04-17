---
name: cmdref
description: Quick Linux command reference. Given a command name (text) or a screenshot of a command/error, shows the most common usage patterns with concise examples in English. Use this skill whenever the user asks "how to use X", "what flags does X take", "how do I X with Y", "I forgot how X works", pastes a bare command name, or uploads a screenshot of a terminal, man page, or error involving a command — even if they don't say /cmdref explicitly. Usage: /cmdref <command> or /cmdref <image>
---

## Step 1 — Identify the command

- If input is **text**: the command name is the argument (e.g., `/linux-help grep` → command = `grep`).
- If input is **image**: read the image visually and extract the primary command name. If the image shows an error or output rather than a clear command name, ask the user which command they want help with.

## Step 2 — Generate the reference

Do NOT run `man`. Use your training knowledge to produce the following in **English**:

### Output format (strict)

```
## <command>

<one-line description of what the command does>

### Common syntax

<syntax line 1>
<syntax line 2>
...

### Common options

| Option | Description |
|--------|-------------|
| ...    | ...         |

### Examples

# <scenario description>
$ <example command>

# <scenario description>
$ <example command>

...(3–6 examples covering the most common use cases)
```

### Rules

- Options table: list only the 5–8 most useful flags, not all of them.
- Examples must be concrete — use real paths/filenames/values, not placeholders.
- If the command has dangerous options (e.g., `rm -rf /`, `dd` overwriting a disk), add a ⚠️ warning line.
- Output language: English only. Commands stay as-is.
- No preamble or closing remarks — start directly with `## <command>`.
