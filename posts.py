import requests
import json

def получить_посты():
    print("Получаю посты...")
    
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout:
        print("Сервер не отвечает")
        return None
    
    except requests.exceptions.ConnectionError:
        print("Нет интернета")
        return None
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def обработать_посты(посты):
    результат = []
    
    for пост in посты:
        # берём только нужные поля
        чистый_пост = {
            "id": пост["id"],
            "заголовок": пост["title"],
            "текст": пост["body"],
            "автор_id": пост["userId"]
        }
        результат.append(чистый_пост)
    
    return результат

def сохранить(данные, имя_файла):
    with open(имя_файла, "w", encoding="utf-8") as f:
        json.dump(данные, f, ensure_ascii=False, indent=4)
    print(f"Сохранено в {имя_файла}")

def показать_статистику(посты):
    print("\n=============================")
    print(f"  Всего постов: {len(посты)}")
    print(f"  Первый пост:")
    print(f"  ID: {посты[0]['id']}")
    print(f"  Заголовок: {посты[0]['заголовок']}")
    print("=============================\n")

# запускаем
if __name__ == "__main__":
    посты = получить_посты()
    
    if посты:
        обработанные = обработать_посты(посты)
        показать_статистику(обработанные)
        сохранить(обработанные, "posts.json")
    else:
        print("Не удалось получить данные")