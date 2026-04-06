# English Learning Plugin

A Claude Code plugin for B2-level English learners. Supports vocabulary lookup, translation, exam solving, and spaced-repetition export to Anki.

## Skills

### `english-learn`

Detects input type automatically and responds accordingly.

| Input | Behavior |
|-------|----------|
| English word (`resilient`) | Phonetic + Chinese translation + 3 example sentences |
| English phrase (`give it a shot`) | Chinese translation + 3 example sentences |
| English sentence | Chinese translation only |
| Chinese word (`韌性`) | English translation + 3 example sentences |
| Chinese sentence | English translation only |
| Image — exam question (TOEIC, TOEFL, etc.) | Answer + explanation in Chinese |
| Image — other content | Chinese translation only |

Append `-s` to save the entry to `vocabulary.json` and `anki_export.txt`:
```
/english-learn resilient -s
```

### `english-quiz`

Fill-in-the-blank quiz from your saved `vocabulary.json`. 3 questions per round with instant grading.

```
/english-quiz
```

## Anki Export

Every time a word is saved with `-s`, `anki_export.txt` is updated in the current directory. Import it directly into Anki via **File → Import**.

Format: tab-separated, UTF-8, HTML enabled.
- **Front**: English word / phrase / sentence
- **Back**: Traditional Chinese meaning
- **Tags**: `english`

## Files Generated

| File | Description |
|------|-------------|
| `vocabulary.json` | Full vocabulary data with metadata |
| `anki_export.txt` | Anki-ready import file |
