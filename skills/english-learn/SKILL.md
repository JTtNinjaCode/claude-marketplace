---
name: english-learn
description: 英文學習工具（使用者程度 B2）。支援多種輸入：英文單字/片語→繁中翻譯+造句、中文單字→英文翻譯+造句、中文句子→英文翻譯、圖片→判斷是否為考題再決定處理方式。輸入單字或片語時自動記錄至當前目錄的單字表。
allowed-tools: Bash
---

使用者英文程度為 B2，造句與解說的難度請對應 B2。

根據輸入類型自動判斷，直接給結果，不要多餘說明。

---

## 類型一：英文單字或片語

格式：
**[單字/片語]** /音標/（片語不需音標）
繁中：[意思]

造句：
1. [句子] → [中文]
2. [句子] → [中文]
3. [句子] → [中文]

完成後記錄至單字表（見「單字表記錄規則」）。

---

## 類型一B：英文句子

翻譯成繁中，完成後記錄至單字表（Front = 英文句子，Back = 繁中翻譯）。

格式：
**[繁中翻譯]**

---

## 類型二：中文單字

格式：
**[英文翻譯]**
中文：[原文]

造句：
1. [句子] → [中文]
2. [句子] → [中文]
3. [句子] → [中文]

不記錄單字表。

---

## 類型三：中文句子

只翻譯成英文，不造句，不記錄。

格式：
**[英文翻譯]**

---

## 類型四：圖片（使用者直接貼上）

圖片由使用者直接貼入對話，不需讀取檔案。

判斷圖片內容：

### 4A：英文考題（多益、托福、學測、指考、各科英文題目等）

辨識標誌：有選項（A/B/C/D）、填空題、閱讀測驗、語法題等。

1. **答案**（直接給）
2. **解析**（繁中，針對 B2，說明為什麼）

逐題作答，不需重述題目。

### 4B：其他英文內容（教科書、文章、說明文字等）

只翻譯成繁體中文，不分析，不造句，不記錄單字表。

---

## 單字表記錄規則

用 Bash 呼叫 `$CLAUDE_SKILL_DIR/scripts/save_vocab.py`，
同時更新當前目錄的 `vocabulary.json` 和 `anki_export.txt`。

```bash
python3 "$CLAUDE_SKILL_DIR/scripts/save_vocab.py" \
  --word "WORD" \
  --type "TYPE" \
  --translation "TRANS" \
  --example "EXAMPLE" \
  --source "SOURCE"
```

- `--type`：adj / n / v / phrase 等
- `--example`：第一句造句
- `--source`：`manual`（直接輸入）

---

## 範例

**輸入：** `resilient`

**resilient** /rɪˈzɪliənt/
繁中：有韌性的、能快速恢復的

造句：
1. She remained resilient despite the setbacks.
   → 儘管遭遇挫折，她依然堅韌不拔。
2. Children are often more resilient than adults think.
   → 孩子往往比大人以為的更有韌性。
3. The economy proved resilient in the face of the crisis.
   → 面對危機，經濟展現了強大的復原力。

*已記錄至單字表。*

---

**輸入：** `韌性`

**resilience**
中文：韌性

造句：
1. Building resilience takes time and practice.
   → 培養韌性需要時間和練習。
2. Her resilience in the face of adversity inspired everyone.
   → 她面對逆境時的韌性激勵了所有人。
3. Mental resilience is just as important as physical strength.
   → 心理韌性和體能一樣重要。

*已記錄至單字表。*

---

**輸入：** `我需要更多時間思考這件事`（中文句子）

**I need more time to think this over.**

---

**輸入：** 圖片（教科書段落）

（直接輸出繁中翻譯）

---

**輸入：** 圖片（多益考題）

Q1. 答案：(B)
解析：...（繁中說明）

Q2. 答案：(A)
解析：...
