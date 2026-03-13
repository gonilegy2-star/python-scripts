import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.get("https://httpbin.org/get", headers=headers, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    
    print("Статус:", response.status_code)
    print("Мой IP:", data["origin"])
    
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("Данные сохранены в test.json")

except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)
except json.JSONDecodeError as e:
    print("Ошибка парсинга JSON:", e)
except Exception as e:
    print("Ошибка:", e)