# Python Scripts 🐍

Мои Python скрипты — учебный проект для изучения Python с нуля.

## Структура проекта
```
python-scripts/
├── api/                    # HTTP запросы и работа с API
│   ├── currency.py         # Курсы валют в реальном времени
│   ├── posts.py            # Получение постов из API
│   ├── async_api.py        # Асинхронные запросы к нескольким API
│   └── weather.py          # Погода через API
├── database/               # Работа с базой данных SQLite
│   ├── database.py         # Основы SQLite
│   ├── analytics.py        # Аналитические SQL запросы
│   ├── sql_to_json.py      # SQL запросы → экспорт в JSON
│   └── finance_manager.py  # Менеджер финансов
├── basics/                 # Основы Python
│   ├── calculator.py       # Калькулятор
│   ├── csv_practice.py     # Чтение и фильтрация CSV
│   └── budget.py           # Работа с бюджетом
├── bot/                    # Боты
│   └── bot.py              # Мини бот в терминале
├── main.py                 # Точка входа
├── requirements.txt        # Зависимости
└── .env.example            # Пример переменных окружения
```

## Что изучено

- Функции, условия, циклы
- Списки и словари
- Работа с файлами
- HTTP запросы (requests, aiohttp)
- Обработка ошибок (try/except)
- JSON — чтение и запись
- Async Python (asyncio, aiohttp)
- ENV переменные (python-dotenv)
- База данных SQLite
- CSV файлы
- Git и GitHub
- Мини бот в терминале

## Установка

1. Клонируй репозиторий:
```
git clone https://github.com/gonilegy2-star/python-scripts.git
```

2. Установи библиотеки:
```
py -m pip install -r requirements.txt
```

3. Создай `.env` файл по примеру `.env.example`

## Запуск
```
py main.py
```

## Технологии

- Python 3.14
- requests
- aiohttp
- python-dotenv
- SQLite3