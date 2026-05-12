import requests
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"

data = {
    "contents": [
        {"parts": [{"text": "Объясни что такое API одним абзацем простыми словами"}]}
    ]
}

response = requests.post(url, json=data)
result = response.json()

print(result)