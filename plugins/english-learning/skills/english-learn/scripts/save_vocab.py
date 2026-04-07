#!/usr/bin/env python3
"""
Save vocabulary to vocabulary.json and sync to anki_export.txt.
Usage: python3 save_vocab.py --word WORD --type TYPE --translation TRANS
         --definition DEF
         --ex1 EN1 --ex1_zh ZH1
         --ex2 EN2 --ex2_zh ZH2
         --ex3 EN3 --ex3_zh ZH3
         --source SOURCE
"""

import argparse
import json
import os
import datetime

VOCAB_FILE = "vocabulary.json"
ANKI_FILE = "anki_export.txt"
ANKI_HEADER = "#separator:tab\n#html:true\n"


def load_vocab():
    if os.path.exists(VOCAB_FILE):
        with open(VOCAB_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"vocabulary": []}


def save_vocab(data):
    with open(VOCAB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_anki_back(v):
    parts = []
    parts.append(v["translation"])
    if v.get("definition"):
        parts.append(f"<i>{v['definition']}</i>")
    examples = v.get("examples", [])
    if examples:
        parts.append("")
        for i, ex in enumerate(examples, 1):
            en = ex.get("en", "")
            zh = ex.get("zh", "")
            if en:
                parts.append(f"{i}. {en}")
            if zh:
                parts.append(f"&nbsp;&nbsp;→ {zh}")
    return "<br>".join(parts)


def sync_anki(data):
    with open(ANKI_FILE, "w", encoding="utf-8") as f:
        f.write(ANKI_HEADER)
        for v in data["vocabulary"]:
            front = v["word"]
            back = build_anki_back(v)
            tags = "english"
            row = "\t".join([
                front.replace("\t", " "),
                back.replace("\t", " "),
                tags,
            ])
            f.write(row + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", required=True)
    parser.add_argument("--type", default="")
    parser.add_argument("--translation", required=True)
    parser.add_argument("--definition", default="")
    parser.add_argument("--ex1", default="")
    parser.add_argument("--ex1_zh", default="")
    parser.add_argument("--ex2", default="")
    parser.add_argument("--ex2_zh", default="")
    parser.add_argument("--ex3", default="")
    parser.add_argument("--ex3_zh", default="")
    parser.add_argument("--source", default="manual")
    args = parser.parse_args()

    examples = []
    for en, zh in [(args.ex1, args.ex1_zh), (args.ex2, args.ex2_zh), (args.ex3, args.ex3_zh)]:
        if en:
            examples.append({"en": en, "zh": zh})

    data = load_vocab()
    existing = {v["word"].lower() for v in data["vocabulary"]}

    if args.word.lower() in existing:
        print(f"已存在，跳過：{args.word}")
    else:
        entry = {
            "word": args.word,
            "type": args.type,
            "translation": args.translation,
            "definition": args.definition,
            "examples": examples,
            "source": args.source,
            "date": str(datetime.date.today()),
        }
        data["vocabulary"].append(entry)
        save_vocab(data)
        print(f"已記錄：{args.word}")

    sync_anki(data)
    print(f"已同步至 {ANKI_FILE}（共 {len(data['vocabulary'])} 筆）")


if __name__ == "__main__":
    main()
