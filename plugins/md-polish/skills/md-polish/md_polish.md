# md-polish — English Rules

Target: English or English-dominant Markdown files.

## Process

1. Scan the file for all issues.
2. Apply all fixes in-place using Edit tool.
3. Output only "Done" — nothing else.

## Scope — what to fix

- **Typos**: spelling mistakes, repeated words, wrong characters
- **Punctuation**: use half-width marks only (,.;:!?()-""). Fix wrong dashes (em-dash → —, en-dash → –, hyphen → -). Remove space before punctuation.
- **Consistency**: heading capitalization (match existing style), list marker (unify to `-`), code fence language tags
- **Whitespace**: trailing spaces, collapse multiple blank lines to one, missing blank line before/after headings and fenced code blocks
- **Horizontal rules**: remove `---`, `***`, `___` decorative dividers (and their surrounding blank lines)
- **LaTeX**: wrap bare math tokens missing `$` — single-letter variables (`i`, `n`, `k`, `x`), expressions (`i+1`, `O(n)`, `x^2`, `x_i`). Only when clearly math, not English words or code.
- **Display math**: `$$` opening and `$$` closing must each be on their own line, not sharing a line with other content. `$...$` inline math is exempt.
  - Wrong: `$$Q = \begin{pmatrix}...$$` (`$$` on same line as content)
  - Correct:
    ```
    $$
    Q = \begin{pmatrix}...
    $$
    ```

## Hard limits

- Do NOT rewrite, rephrase, or restructure sentences
- Do NOT change meaning, tone, or technical content
- Do NOT add, remove, or reorder sections
- Do NOT touch code inside fenced code blocks
- Do NOT change URLs, file paths, or variable names
- Skip ambiguous fixes silently.
