import requests
import json
import os
import time
from datetime import datetime

API_URL = "https://uselessfacts.jsph.pl/random.json?language=zh"
DATA_FILE = "facts.json"
INTERVAL_SECONDS = 10  # 每 10 秒執行一次（示範用）


def load_facts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_facts(facts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)


def fetch_fact():
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            return response.json()["text"]
    except Exception:
        pass
    return None


def main_loop():
    print("自動事實收集器已啟動，按 Ctrl+C 可停止")

    while True:
        facts = load_facts()
        new_fact = fetch_fact()
        timestamp = datetime.now().isoformat(timespec="seconds")

        if new_fact is None:
            print(f"[{timestamp}] API 連線失敗")
        elif new_fact in facts:
            print(f"[{timestamp}] 重複資料，略過")
        else:
            facts.append(new_fact)
            save_facts(facts)
            print(f"[{timestamp}] 新增事實：{new_fact}")

        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main_loop()
