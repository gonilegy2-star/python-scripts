import requests
import json
from datetime import datetime

def get_exchange_rates():
    print("Fetching exchange rates...")
    
    try:
        response = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        if data["result"] != "success":
            print("API returned an error")
            return None
        
        return data
    
    except requests.exceptions.Timeout:
        print("Server is not responding")
        return None
    
    except requests.exceptions.ConnectionError:
        print("No internet connection")
        return None
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_exchange_rates(data):
    rates_data = {
        "date": data["time_last_update_utc"],
        "base_currency": "USD",
        "rates": {
            "RUB": data["rates"]["RUB"],
            "EUR": data["rates"]["EUR"],
            "UAH": data["rates"]["UAH"],
            "GBP": data["rates"]["GBP"],
            "JPY": data["rates"]["JPY"],
        }
    }
    
    with open("exchange_rates.json", "w", encoding="utf-8") as f:
        json.dump(rates_data, f, ensure_ascii=False, indent=4)
    
    return rates_data

def display_rates(rates):
    print("\n=============================")
    print(f"  Exchange rates to USD")
    print(f"  {rates['date']}")
    print("=============================")
    for currency, rate in rates["rates"].items():
        print(f"  1 USD = {rate} {currency}")
    print("=============================\n")

data = get_exchange_rates()

if data:
    rates = save_exchange_rates(data)
    display_rates(rates)
    print("Data saved to exchange_rates.json")
else:
    print("Failed to retrieve data")