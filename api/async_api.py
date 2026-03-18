import asyncio
import aiohttp
import json
import time
from datetime import datetime

semaphore = asyncio.Semaphore(3)

async def get_currencies(session):
    async with semaphore:
        try:
            async with session.get(
                "https://open.er-api.com/v6/latest/USD",
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                data = await response.json()
                return {
                    "type": "currencies",
                    "data": {
                        "EUR": data["rates"]["EUR"],
                        "RUB": data["rates"]["RUB"],
                        "GBP": data["rates"]["GBP"],
                    }
                }
        except Exception as e:
            return {"type": "currencies", "data": None, "error": str(e)}

async def get_post(session, post_id):
    async with semaphore:
        try:
            async with session.get(
                f"https://jsonplaceholder.typicode.com/posts/{post_id}",
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                data = await response.json()
                return {
                    "type": f"post_{post_id}",
                    "data": {
                        "id": data["id"],
                        "title": data["title"],
                        "text": data["body"][:50] + "..."
                    }
                }
        except Exception as e:
            return {"type": f"post_{post_id}", "data": None, "error": str(e)}

async def get_weather(session, city, lat, lon):
    async with semaphore:
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            async with session.get(
                url,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                data = await response.json()
                weather = data["current_weather"]
                return {
                    "type": f"weather_{city}",
                    "data": {
                        "city": city,
                        "temperature": weather["temperature"],
                        "windspeed": weather["windspeed"]
                    }
                }
        except Exception as e:
            return {"type": f"weather_{city}", "data": None, "error": str(e)}

async def main():
    print("=" * 40)
    print("Running all requests concurrently...")
    print("=" * 40)
    
    start = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [
            get_currencies(session),
            get_post(session, 1),
            get_post(session, 2),
            get_post(session, 3),
            get_weather(session, "Moscow", 55.75, 37.62),
            get_weather(session, "London", 51.50, -0.12),
            get_weather(session, "Tokyo", 35.68, 139.69),
        ]
        
        results = await asyncio.gather(*tasks)
    
    elapsed = time.time() - start
    
    summary = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_seconds": round(elapsed, 2),
        "data": {}
    }
    
    for result in results:
        result_type = result["type"]
        summary["data"][result_type] = result.get("data")
    
    with open("async_result.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=4)
    
    print(f"\nAll requests took: {elapsed:.1f} sec")
    print(f"Successful: {sum(1 for r in results if r.get('data'))}")
    
    print("\n--- Currencies ---")
    currencies = summary["data"].get("currencies")
    if currencies:
        for currency, rate in currencies.items():
            print(f"  1 USD = {rate} {currency}")
    
    print("\n--- Weather ---")
    for key, value in summary["data"].items():
        if key.startswith("weather_") and value:
            print(f"  {value['city']}: {value['temperature']}°C, wind {value['windspeed']} km/h")
    
    print("\n--- Posts ---")
    for key, value in summary["data"].items():
        if key.startswith("post_") and value:
            print(f"  #{value['id']}: {value['title'][:40]}...")
    
    print(f"\nSaved to async_result.json")

asyncio.run(main())