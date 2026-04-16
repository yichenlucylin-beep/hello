import requests

url = "https://uselessfacts.jsph.pl/random.json?language=zh"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    fact = data["text"]
    print("取得的事實資料：")
    print(fact)
else:
    print("API 連線失敗")
