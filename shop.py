import sqlite3

def создать_базу():
    conn = sqlite3.connect("магазин.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS товары (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            название TEXT    NOT NULL,
            категория TEXT,
            цена     REAL,
            остаток  INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS клиенты (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            имя     TEXT NOT NULL,
            город   TEXT,
            email   TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS заказы (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            клиент_id   INTEGER,
            товар_id    INTEGER,
            количество  INTEGER,
            дата        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            статус      TEXT DEFAULT 'новый'
        )
    """)

    conn.commit()
    return conn

def заполнить_данными(conn):
    cursor = conn.cursor()

    товары = [
        ("iPhone 15",      "Телефоны",    90000, 15),
        ("Samsung S24",    "Телефоны",    80000, 20),
        ("MacBook Pro",    "Ноутбуки",   150000,  8),
        ("Dell XPS",       "Ноутбуки",   120000, 12),
        ("AirPods Pro",    "Аксессуары",  25000, 30),
        ("iPad Air",       "Планшеты",    70000, 10),
        ("Samsung Tab",    "Планшеты",    45000, 18),
        ("Зарядка Apple",  "Аксессуары",   3000, 50),
        ("Чехол iPhone",   "Аксессуары",   1500, 100),
        ("Xiaomi 14",      "Телефоны",    60000, 25),
    ]

    cursor.executemany("""
        INSERT INTO товары (название, категория, цена, остаток)
        VALUES (?, ?, ?, ?)
    """, товары)

    клиенты = [
        ("Данил",   "Москва",  "danil@mail.ru"),
        ("Иван",    "Питер",   "ivan@mail.ru"),
        ("Мария",   "Казань",  "maria@mail.ru"),
        ("Алексей", "Москва",  "alex@mail.ru"),
        ("Ольга",   "Питер",   "olga@mail.ru"),
        ("Дмитрий", "Москва",  "dima@mail.ru"),
        ("Анна",    "Казань",  "anna@mail.ru"),
        ("Сергей",  "Москва",  "sergey@mail.ru"),
    ]

    cursor.executemany("""
        INSERT INTO клиенты (имя, город, email)
        VALUES (?, ?, ?)
    """, клиенты)

    заказы = [
        (1, 1,  1, "доставлен"),
        (1, 5,  2, "доставлен"),
        (2, 3,  1, "в пути"),
        (2, 8,  3, "доставлен"),
        (3, 2,  1, "новый"),
        (3, 9,  2, "доставлен"),
        (4, 4,  1, "доставлен"),
        (4, 6,  1, "в пути"),
        (5, 10, 1, "доставлен"),
        (5, 5,  1, "новый"),
        (6, 1,  2, "доставлен"),
        (6, 7,  1, "в пути"),
        (7, 3,  1, "доставлен"),
        (8, 2,  1, "новый"),
        (8, 8,  5, "доставлен"),
    ]

    cursor.executemany("""
        INSERT INTO заказы (клиент_id, товар_id, количество, статус)
        VALUES (?, ?, ?, ?)
    """, заказы)

    conn.commit()
    print("База заполнена данными!")

conn = создать_базу()
заполнить_данными(conn)
conn.close()