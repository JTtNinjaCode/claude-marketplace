---
name: english-quiz
description: Fill-in-the-blank vocabulary quiz pulled from vocabulary.json in the current directory. 3 questions per round with instant grading. Question types include English-to-Chinese blanks, Chinese-to-English blanks, and English sentence translation blanks. Best used alongside english-learn.
allowed-tools: Read Bash
---

The user's English level is B2. Give 3 questions per round, grade immediately, then ask if they want to continue.

## Flow

1. Read `vocabulary.json` from the current directory using Bash
2. If the file does not exist or has fewer than 3 entries, prompt the user to add words with `/english-learn -s`
3. Randomly pick 3 entries, assign each a random question type
4. Present all 3 questions, wait for answers
5. Grade immediately with brief feedback
6. Ask if they want another round

## Question Types (all fill-in-the-blank)

### Type A: English → Chinese blank
Show an English sentence, give a partial Chinese translation with a key word blanked out.

```
Q1. Fill in the correct Chinese word:
"She remained resilient despite the setbacks."
→ 她儘管遭遇挫折，依然______不拔。
```

### Type B: Chinese → English blank
Show a Chinese sentence, give a partial English translation with the target word blanked out.

```
Q2. Fill in the correct English word or phrase:
「我們應該試試看這個新方法。」
→ We should ________ this new approach.
```

### Type C: English sentence → Chinese translation blank
Show an English sentence (may be new, not limited to the stored example), give a partial Chinese translation with 1–2 key words blanked out.

```
Q3. Read the sentence and fill in the missing Chinese words:
"The project was put on hold due to budget constraints."
→ 這個計畫因為預算______而被______。
```

Only blank out words that genuinely test comprehension. Do not blank out function words or overly simple words.

## Question Format

```
📝 Round N
──────────────────
Q1. [type description]
[question content]

Q2. [type description]
[question content]

Q3. [type description]
[question content]
──────────────────
```

## Grading Format

Keep it fast and clear. Only explain when the answer is wrong. If the answer is correct and the word has common, high-frequency synonyms that are actually used in everyday English, mention 1–2 briefly. Skip obscure or overly formal synonyms.

```
✅ Q1. Correct! resilient can also be expressed as tough (informal) or adaptable (emphasizing flexibility).
❌ Q2. Your answer: insist — Correct answer: persist
   → persist means to continue doing something despite difficulty.
     insist means to firmly demand or maintain a position. Different meaning.
   Synonyms: persevere (stronger tone), keep at it (informal)
✅ Q3. Correct!
```

If there is nothing worth noting for a correct answer, just say "Correct!"

After grading:
```
Continue to the next round? Type anything to go on.
```
