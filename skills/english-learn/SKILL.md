---
name: english-learn
description: 英文學習工具（使用者程度 B2）。支援多種輸入：英文單字/片語→繁中翻譯+造句、中文→英文翻譯+造句、圖片→內容擷取+翻譯+難字造句、英文考題（多益/托福/學測等）→解題+解析。輸入單字或片語時自動記錄至當前目錄的單字表。
allowed-tools: Read Bash
---

使用者英文程度為 B2，造句與解說的難度請對應 B2，但難字分析要找出 B2 以上的詞彙。

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

完成後，將此單字/片語記錄至單字表（見「單字表記錄規則」）。

---

## 類型二：中文單字

格式：
**[英文翻譯]**
中文：[原文]

造句：
1. [句子] → [中文]
2. [句子] → [中文]
3. [句子] → [中文]

完成後，將此單字記錄至單字表（見「單字表記錄規則」）。

---

## 類型二B：中文句子

只翻譯，不造句，不記錄單字表。

格式：
**[英文翻譯]**

---

## 類型三：圖片輸入

用 Read 工具讀取圖片。

1. **內容摘要**（繁中，2-3句）
2. **全文翻譯**（如果是文章/段落）
3. **難字列表**（挑出 B2+ 的單字或片語，5-10個）

格式：
| 單字/片語 | 音標 | 繁中意思 | 例句 |
|-----------|------|----------|------|
| [word] | /.../ | [意思] | [例句] |

完成後，將所有難字記錄至單字表（見「單字表記錄規則」）。

---

## 類型四：英文考題（多益、托福、學測、指考等）

1. **題目重述**（確認讀懂題目）
2. **答案**（直接給答案）
3. **解析**（說明為什麼，用繁中解釋，針對 B2 程度）
4. **關鍵字彙**（考題中出現的重要單字，附繁中意思）

如果是整份題目，逐題作答。

---

## 單字表記錄規則

單字表位置：當前目錄的 `vocabulary.json`

用 Bash 工具讀取並更新此檔案。若檔案不存在則建立。

JSON 結構：
```json
{
  "vocabulary": [
    {
      "word": "resilient",
      "type": "adj",
      "translation": "有韌性的",
      "example": "She remained resilient despite the setbacks.",
      "source": "manual",
      "date": "2026-04-06"
    }
  ]
}
```

`source` 填入來源：`manual`（使用者直接輸入）或 `image`（圖片擷取）或 `exam`（考題）。

新增時避免重複（比對 `word` 欄位，忽略大小寫）。

更新指令範例（用 Python inline，避免 jq 依賴問題）：
```bash
python3 -c "
import json, os, datetime
path = 'vocabulary.json'
data = json.load(open(path)) if os.path.exists(path) else {'vocabulary': []}
existing = {v['word'].lower() for v in data['vocabulary']}
new_word = {'word': 'WORD', 'type': 'TYPE', 'translation': 'TRANS', 'example': 'EXAMPLE', 'source': 'SOURCE', 'date': str(datetime.date.today())}
if new_word['word'].lower() not in existing:
    data['vocabulary'].append(new_word)
    json.dump(data, open(path, 'w'), ensure_ascii=False, indent=2)
    print('已記錄：' + new_word['word'])
else:
    print('已存在，跳過：' + new_word['word'])
"
```

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

**輸入：** `give it a shot`

**give it a shot**
繁中：試試看、嘗試一下

造句：
1. I've never cooked Thai food before, but I'll give it a shot.
   → 我從沒做過泰國菜，但我來試試看。
2. You should give it a shot — you might surprise yourself.
   → 你應該試試看，說不定會讓自己驚喜。
3. He decided to give it a shot even though the odds were slim.
   → 儘管機率不大，他還是決定試一試。

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
