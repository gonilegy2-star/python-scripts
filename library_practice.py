import sqlite3

# Создаем файл базы
conn = sqlite3.connect('my_library.db')
cursor = conn.cursor()

# Включаем поддержку внешних ключей (важно для связей!)
cursor.execute("PRAGMA foreign_keys = ON")

# Создаем таблицу авторов
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT
)
''')

# Создаем таблицу книг со связью
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    year INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (id)
)
''')
conn.commit()

# Добавляем авторов
authors_data = [
    ('Лев Толстой', 'Россия'),
    ('Джордж Оруэлл', 'Великобритания'),
    ('Рэй Брэдбери', 'США')
]
cursor.executemany("INSERT INTO authors (name, country) VALUES (?, ?)", authors_data)

# Добавляем книги (author_id 1 — это Толстой, и так далее)
books_data = [
    ('Война и мир', 1, 1869),
    ('Анна Каренина', 1, 1877),
    ('1984', 2, 1949),
    ('451 градус по Фаренгейту', 3, 1953)
]
cursor.executemany("INSERT INTO books (title, author_id, year) VALUES (?, ?, ?)", books_data)
conn.commit()

query = '''
SELECT b.title, a.name, a.country
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.year > 1900
ORDER BY b.year ASC
'''

cursor.execute(query)
for row in cursor.fetchall():
    print(f"Книга: {row[0]} | Автор: {row[1]} ({row[2]})")

conn.close()