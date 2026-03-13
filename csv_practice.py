import csv
import json

def load_data(file):
    data = []
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                "name": row["имя"],
                "age": int(row["возраст"]),
                "city": row["город"],
                "balance": int(row["баланс"]),
                "active": row["активен"] == "yes"
            })
    return data

def save_to_csv(data, file):
    if not data:
        print("No data to save")
        return
    
    with open(file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} records to {file}")

def analyze(data):
    print("\n========== ANALYSIS ==========")
    print(f"Total records: {len(data)}")
    print(f"Active: {sum(1 for p in data if p['active'])}")
    print(f"Average age: {sum(p['age'] for p in data) / len(data):.1f}")
    print(f"Average balance: {sum(p['balance'] for p in data) / len(data):.0f}")
    
    # top 3 by balance
    top3 = sorted(data, key=lambda x: x["balance"], reverse=True)[:3]
    print("\nTop 3 by balance:")
    for i, p in enumerate(top3, 1):
        print(f"  {i}. {p['name']} — {p['balance']}")
    print("============================\n")

# run
people = load_data("data.csv")
analyze(people)

# save only active users to new CSV
active = [p for p in people if p["active"]]
save_to_csv(active, "active.csv")

# save to JSON
with open("people.json", "w", encoding="utf-8") as f:
    json.dump(people, f, ensure_ascii=False, indent=4)
print("Also saved to people.json")