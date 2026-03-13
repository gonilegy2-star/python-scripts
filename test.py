import requests

response = requests.get("https://httpbin.org/get")

print(response.status_code)  # код ответа (200 = всё ок)
print(response.text)         # текст страницы