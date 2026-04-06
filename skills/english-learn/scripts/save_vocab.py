#!/usr/bin/env python3
"""
Save vocabulary to vocabulary.json and sync to anki_export.txt.
Usage: python3 save_vocab.py --word WORD --type TYPE --translation TRANS --example EXAMPLE --source SOURCE
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


def sync_anki(data):
    with open(ANKI_FILE, "w", encoding="utf-8") as f:
        f.write(ANKI_HEADER)
        for v in data["vocabulary"]:
            front = v["word"]
            back = v["translation"]
            if v.get("example"):
                back += "<br><i>" + v["example"] + "</i>"
            tags = "english"
            # tab-separated, escape tabs in fields just in case
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
    parser.add_argument("--example", default="")
    parser.add_argument("--source", default="manual")
    args = parser.parse_args()

    data = load_vocab()
    existing = {v["word"].lower() for v in data["vocabulary"]}

    if args.word.lower() in existing:
        print(f"已存在，跳過：{args.word}")
    else:
        entry = {
            "word": args.word,
            "type": args.type,
            "translation": args.translation,
            "example": args.example,
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
