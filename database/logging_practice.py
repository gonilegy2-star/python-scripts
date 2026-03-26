import logging
import requests
import json
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("отчёт.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def получить_курсы():
    logger.info("Получение курсов валют")
    try:
        r = requests.get("https://open.er-api.com/v6/latest/USD", timeout=10)
        r.raise_for_status()
        данные = r.json()
        курсы = {
            "EUR": данные["rates"]["EUR"],
            "RUB": данные["rates"]["RUB"],
            "GBP": данные["rates"]["GBP"],
        }
        logger.info(f"Курсы получены: EUR={курсы['EUR']}, RUB={курсы['RUB']}")
        return {"статус": "успех", "данные": курсы}
    except Exception as e:
        logger.error(f"Ошибка курсов: {e}")
        return {"статус": "ошибка", "данные": None}

def получить_посты():
    logger.info("Получение постов")
    try:
        r = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            timeout=10
        )
        r.raise_for_status()
        посты = r.json()[:5]
        обработанные = [
            {"id": п["id"], "заголовок": п["title"][:50], "автор": п["userId"]}
            for п in посты
        ]
        logger.info(f"Постов получено и обработано: {len(обработанные)}")
        return {"статус": "успех", "данные": обработанные}
    except Exception as e:
        logger.error(f"Ошибка постов: {e}")
        return {"статус": "ошибка", "данные": None}

def сохранить_отчёт(отчёт):
    имя_файла = f"отчёт_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    logger.info(f"Сохраняю отчёт в {имя_файла}")
    
    try:
        with open(имя_файла, "w", encoding="utf-8") as f:
            json.dump(отчёт, f, ensure_ascii=False, indent=4)
        logger.info(f"Отчёт сохранён: {имя_файла}")
        return имя_файла
    
    except Exception as e:
        logger.error(f"Ошибка сохранения: {e}")
        return None

def main():
    logger.info("=" * 50)
    logger.info("ПРОГРАММА ЗАПУЩЕНА")
    
    начало = datetime.now()
    
    # выполняем задачи
    курсы = получить_курсы()
    посты = получить_посты()
    
    конец = datetime.now()
    время = (конец - начало).total_seconds()
    
    # собираем отчёт
    отчёт = {
        "мета": {
            "дата":           начало.strftime("%Y-%m-%d %H:%M:%S"),
            "время_работы":   f"{время:.2f} сек",
            "успешных_задач": sum(1 for х in [курсы, посты]
                                  if х["статус"] == "успех"),
            "всего_задач":    2
        },
        "курсы_валют": курсы,
        "посты":       посты
    }
    
    # сохраняем
    файл = сохранить_отчёт(отчёт)
    
    logger.info(f"Время работы: {время:.2f} сек")
    logger.info("ПРОГРАММА ЗАВЕРШЕНА")
    logger.info("=" * 50)
    
    return отчёт

main()
