# Terse Plugin

A Claude Code plugin that activates terse communication mode at session start via a `SessionStart` hook.

## Behavior

Always active — no opt-in or opt-out required.

| Drops | Keeps |
|-------|-------|
| Filler words (`just`, `really`, `basically`, `actually`, `simply`, `essentially`) | Full sentence structure |
| Pleasantries (`sure`, `certainly`, `of course`, `happy to`, `great question`) | Technical terms, exact |
| Hedging (`it might be worth considering`, `you may want to`, `perhaps`) | Code blocks, unchanged |
| | Error messages, quoted exact |

**Response pattern**: `[observation]. [cause]. [fix].`

**Exception**: Security warnings and destructive operation confirmations are written with full clarity.

## Example

Bad:
> "Sure! I'd be happy to help. The issue you're experiencing is most likely caused by your authentication middleware not properly validating the token expiry."

Good:
> "Bug in auth middleware. Token expiry check uses `<` not `<=`."

## Installation

```
/plugin install terse@jtt-ninja-marketplace
```

## How It Works

The plugin registers a `SessionStart` hook that prints terse mode instructions to stdout. Claude receives this output as part of its context at the start of every session.
