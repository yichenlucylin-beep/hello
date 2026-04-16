import requests
import json
import os

API_URL = "https://uselessfacts.jsph.pl/random.json?language=zh"
DATA_FILE = "facts.json"


def load_facts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_facts(facts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)


def fetch_fact():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["text"]
    else:
        return None


def main():
    facts = load_facts()
    new_fact = fetch_fact()

    if new_fact is None:
        print("API 連線失敗")
        return

    if new_fact in facts:
        print("這則事實已經存在資料庫中：")
        print(new_fact)
    else:
        facts.append(new_fact)
        save_facts(facts)
        print("新增一則事實並存入資料庫：")
        print(new_fact)


if __name__ == "__main__":
    main()
