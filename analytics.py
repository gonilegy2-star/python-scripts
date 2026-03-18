import sqlite3

conn = sqlite3.connect("посты.db")
cursor = conn.cursor()

# 1. Общее количество постов
cursor.execute("SELECT COUNT(*) FROM посты")
всего = cursor.fetchone()[0]
print(f"Всего постов: {всего}")

# 2. Количество постов по каждому автору
print("\nПосты по авторам:")
cursor.execute("""
    SELECT автор_id, COUNT(*) as количество
    FROM посты
    GROUP BY автор_id
    ORDER BY количество DESC
""")
for строка in cursor.fetchall():
    print(f"  Автор #{строка[0]} — {строка[1]} постов")

# 3. Топ 5 самых длинных заголовков
print("\nТоп 5 длинных заголовков:")
cursor.execute("""
    SELECT заголовок, LENGTH(заголовок) as длина
    FROM посты
    ORDER BY длина DESC
    LIMIT 5
""")
for строка in cursor.fetchall():
    print(f"  {строка[1]} символов: {строка[0][:50]}...")

# 4. Самый активный автор
print("\nСамый активный автор:")
cursor.execute("""
    SELECT автор_id, COUNT(*) as количество
    FROM посты
    GROUP BY автор_id
    ORDER BY количество DESC
    LIMIT 1
""")
автор = cursor.fetchone()
print(f"  Автор #{автор[0]} — {автор[1]} постов")

# 5. Средняя длина текста поста
print("\nСредняя длина текста:")
cursor.execute("SELECT AVG(LENGTH(текст)) FROM посты")
средняя = cursor.fetchone()[0]
print(f"  {средняя:.0f} символов")

# 6. Посты с самым коротким текстом
print("\nТоп 3 поста с коротким текстом:")
cursor.execute("""
    SELECT автор_id, заголовок, LENGTH(текст) as длина
    FROM посты
    ORDER BY длина ASC
    LIMIT 3
""")
for строка in cursor.fetchall():
    print(f"  Автор #{строка[0]}: {строка[1][:40]}... ({строка[2]} симв)")

conn.close()
print("\nАналитика готова!")