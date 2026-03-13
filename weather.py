import json
from datetime import datetime

def save_to_history(weather):
    history = []
    
    # Read existing history from file
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        pass  # File doesn't exist yet - start with empty list
    
    # Add request timestamp
    weather["request_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add new entry
    history.append(weather)
    
    # Save back to file
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
    
    print(f"History now contains {len(history)} requests")