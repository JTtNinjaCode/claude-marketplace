---
name: md-polish
description: Polish a Markdown file by fixing typos, punctuation, LaTeX formatting, and consistency — without rewriting content. Auto-detects Traditional Chinese vs English and applies language-appropriate rules. Use this skill whenever the user wants to proofread, clean up, fix typos, fix punctuation, or polish a .md file, even if they don't say "polish". Usage: /md-polish <file-path>
allowed-tools: Read, Edit, Bash
---

## Step 1 — Read the target file

Read the file provided by the user.

## Step 2 — Detect dominant language

Inspect prose text (ignore code blocks, URLs, headings). If Chinese characters make up more than 30% of prose characters, classify as **Traditional Chinese**; otherwise **English**.

## Step 3 — Load rule file

- Traditional Chinese → read `$CLAUDE_SKILL_DIR/md_polish_zh.md`
- English → read `$CLAUDE_SKILL_DIR/md_polish.md`

Follow the rules in that file exactly for the remainder of the process.
