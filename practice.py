import requests
import json
import time

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # save to file
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Success! Status: {response.status_code}")
        return data
    
    except requests.exceptions.Timeout:
        print("Server is not responding")
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.HTTPError as e:
        print(f"Server error: {e}")
    except json.JSONDecodeError:
        print("Server returned invalid JSON")
    except Exception as e:
        print(f"Unknown error: {e}")
    
    return None

result = get_data("https://httpbin.org/get")
if result:
    print("My IP:", result["origin"])