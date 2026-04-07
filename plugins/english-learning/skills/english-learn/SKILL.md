---
name: english-learn
description: English learning tool for B2-level learners. Supports multiple input types — English word/phrase → Traditional Chinese translation + example sentences, Chinese word → English translation + example sentences, Chinese sentence → English translation only, image of exam question (TOEIC/TOEFL/GSAT) → solve and explain in Chinese, image of other English content (textbooks, articles, any subject) → sentence-by-sentence Chinese translation only, never solve or analyze. Append -s to save to vocabulary list.
allowed-tools: Bash
---

The user's English level is B2. Keep example sentences and explanations at B2 difficulty.

Detect the input type automatically and respond directly without unnecessary commentary.

No opening phrases, no closing remarks, no greetings, no meta-commentary (e.g., do NOT say "Here's the translation:" or "Let me help you with that." or "Hope this helps!"). Output only the formatted result, exactly as shown in the examples.

## Save Option

Append `-s` to save the entry to the vocabulary list. Default is no saving.

- Save: `resilient -s`
- No save: `resilient`

Only English inputs (word, phrase, sentence) can be saved. Chinese inputs and images are never saved.

---

## Type 1: English Word or Phrase

Always use this exact format — do not change the labels or structure:

**[word/phrase]** /phonetic/ (omit phonetic for phrases)
English: [concise English definition]
Chinese: [meaning]

Example sentences:
en: [English sentence]
zh: [Chinese translation]

en: [English sentence]
zh: [Chinese translation]

en: [English sentence]
zh: [Chinese translation]

If `-s` is present, save to vocabulary list (see Vocabulary Save Rules) and output: *Saved to vocabulary list.*

---

## Type 2: English Sentence

Translate to Traditional Chinese only.

Format:
**[Traditional Chinese translation]**

If `-s` is present, save (Front = English sentence, Back = Chinese translation) and output: *Saved to vocabulary list.*

---

## Type 3: Chinese Word

Format:
**[English translation]**
Chinese: [original]

Example sentences:
en: [English sentence]
zh: [Chinese translation]

en: [English sentence]
zh: [Chinese translation]

en: [English sentence]
zh: [Chinese translation]

Never save.

---

## Type 4: Chinese Sentence (including mixed Chinese/English sentences)

Treat any sentence where the main structure is Chinese as Type 4, even if it contains embedded English terms (e.g., "wafer scale chip 是最新技術"). Translate the full sentence to English only. No example sentences, no saving.

Format:
**[English translation]**

---

## Type 5: Image (pasted directly by the user)

The user pastes the image into the conversation — no file reading needed. Never save to vocabulary list.

### 5A: English Exam Question (TOEIC, TOEFL, GSAT, etc.)

Identifiers: multiple choice (A/B/C/D), fill-in-the-blank, reading comprehension, grammar questions, etc.

1. **Answer** (state directly)
2. **Explanation** (in Traditional Chinese, targeting B2 level)

Answer each question in order. Do not restate the question.

### 5B: Other English Content (textbooks, articles, instructions, etc.)

Translate sentence by sentence: output each original English sentence, then its Traditional Chinese translation on the next line prefixed with `→`. No analysis, no example sentences.

---

## Vocabulary Save Rules

Use Bash to call `$CLAUDE_SKILL_DIR/scripts/save_vocab.py`.
This updates both `vocabulary.json` and `anki_export.txt` in the current working directory.

**For Type 1 (word/phrase):**
```bash
python3 "$CLAUDE_SKILL_DIR/scripts/save_vocab.py" \
  --word "WORD" \
  --type "TYPE" \
  --translation "TRANS" \
  --definition "ENGLISH_DEFINITION" \
  --ex1 "EXAMPLE_EN_1" --ex1_zh "EXAMPLE_ZH_1" \
  --ex2 "EXAMPLE_EN_2" --ex2_zh "EXAMPLE_ZH_2" \
  --ex3 "EXAMPLE_EN_3" --ex3_zh "EXAMPLE_ZH_3" \
  --source "manual"
```

**For Type 2 (sentence):**
```bash
python3 "$CLAUDE_SKILL_DIR/scripts/save_vocab.py" \
  --word "ENGLISH_SENTENCE" \
  --type "sentence" \
  --translation "CHINESE_TRANSLATION" \
  --source "manual"
```

- `--type`: adj / n / v / phrase / sentence
- `--source`: `manual`

---

## Examples

**Input:** `resilient` (no save)

**resilient** /rɪˈzɪliənt/
English: able to recover quickly from difficult situations
Chinese: 有韌性的、能快速恢復的

Example sentences:
en: She remained resilient despite the setbacks.
zh: 儘管遭遇挫折，她依然堅韌不拔。

en: Children are often more resilient than adults think.
zh: 孩子往往比大人以為的更有韌性。

en: The economy proved resilient in the face of the crisis.
zh: 面對危機，經濟展現了強大的復原力。

---

**Input:** `resilient -s` (save)

**resilient** /rɪˈzɪliənt/
English: able to recover quickly from difficult situations
Chinese: 有韌性的、能快速恢復的

Example sentences:
en: She remained resilient despite the setbacks.
zh: 儘管遭遇挫折，她依然堅韌不拔。

en: Children are often more resilient than adults think.
zh: 孩子往往比大人以為的更有韌性。

en: The economy proved resilient in the face of the crisis.
zh: 面對危機，經濟展現了強大的復原力。

*Saved to vocabulary list.*

---

**Input:** `韌性`

**resilience**
Chinese: 韌性

Example sentences:
en: Building resilience takes time and practice.
zh: 培養韌性需要時間和練習。

en: Her resilience in the face of adversity inspired everyone.
zh: 她面對逆境時的韌性激勵了所有人。

en: Mental resilience is just as important as physical strength.
zh: 心理韌性和體能一樣重要。

---

**Input:** `我需要更多時間思考這件事`

**I need more time to think this over.**

---

**Input:** [Image of an English article/textbook passage]

I am, as it were, only a coach.
→ 我就像是一位教練。

I cannot run the mile for you; at best I can discuss styles and criticize yours.
→ 我無法替你跑那一英里；我最多只能討論風格並批評你的表現。

You know you must run the mile if the athletics course is to be of benefit to you.
→ 你知道，如果這門體育課要對你有益，你必須自己去跑。
