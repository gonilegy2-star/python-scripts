import sqlite3

# Подключаемся к базе (файл создастся автоматически в папке с проектом)
conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

# Создаем таблицу категорий и таблицу расходов
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    amount REAL,
    date TEXT,
    FOREIGN KEY (category_id) REFERENCES categories (id)
)
''')

conn.commit()
print("База данных готова!")

# 1. Добавляем категории
# Используем executemany для добавления списка кортежей
categories = [('Продукты',), ('Транспорт',), ('Кино',)]
cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

# 2. Добавляем расходы
# category_id 1 — это Продукты, 2 — Транспорт и т.д.
expenses = [
    (1, 500.50, '2026-03-16'),
    (2, 100.00, '2026-03-16'),
    (1, 1200.00, '2026-03-16'),
    (3, 600.00, '2026-03-16')
]
cursor.executemany("INSERT INTO expenses (category_id, amount, date) VALUES (?, ?, ?)", expenses)

# КРИТИЧЕСКИ ВАЖНО: сохранить изменения
conn.commit()
print("Данные успешно добавлены!")

print("\n--- СТАТИСТИКА ТРАТ ---")

query = '''
SELECT 
    c.name, 
    SUM(e.amount),
    COUNT(e.id)
FROM categories c
JOIN expenses e ON c.id = e.category_id
GROUP BY c.name
HAVING SUM(e.amount) > 1000
ORDER BY SUM(e.amount) DESC;
'''

cursor.execute(query)
for row in cursor.fetchall():
    print(f"На {row[0]} потрачено {row[1]} руб. (Операций: {row[2]})")

# Закрываем соединение в самом конце
conn.close()