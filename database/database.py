import sqlite3
import requests
import json

def создать_базу():
    conn = sqlite3.connect("посты.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS посты (
            id        INTEGER PRIMARY KEY,
            заголовок TEXT,
            текст     TEXT,
            автор_id  INTEGER,
            добавлен  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    return conn

def загрузить_данные_из_api(conn):
    print("Загружаю посты из API...")
    
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            timeout=10
        )
        response.raise_for_status()
        посты = response.json()
        
        cursor = conn.cursor()
        
        for пост in посты:
            cursor.execute("""
                INSERT OR IGNORE INTO посты (id, заголовок, текст, автор_id)
                VALUES (?, ?, ?, ?)
            """, (
                пост["id"],
                пост["title"],
                пост["body"],
                пост["userId"]
            ))
        
        conn.commit()
        print(f"Загружено постов: {len(посты)}")
        
    except Exception as e:
        print(f"Ошибка: {e}")

def найти_посты(conn, автор_id):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT * FROM посты 
        WHERE автор_id = ?
        ORDER BY id
    """, (автор_id,))
    
    return cursor.fetchall()

def статистика(conn):
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM посты")
    всего = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT автор_id) FROM посты")
    авторов = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT автор_id, COUNT(*) as количество 
        FROM посты 
        GROUP BY автор_id 
        ORDER BY количество DESC 
        LIMIT 3
    """)
    топ_авторы = cursor.fetchall()
    
    print("\n========== СТАТИСТИКА ==========")
    print(f"Всего постов: {всего}")
    print(f"Всего авторов: {авторов}")
    print("Топ 3 автора:")
    for автор in топ_авторы:
        print(f"  Автор #{автор[0]} — {автор[1]} постов")
    print("================================\n")

# запускаем
conn = создать_базу()
загрузить_данные_из_api(conn)
статистика(conn)

# ищем посты конкретного автора
посты_автора = найти_посты(conn, 1)
print(f"Посты автора #1 ({len(посты_автора)} штук):")
for пост in посты_автора[:3]:
    print(f"  #{пост['id']}: {пост['заголовок'][:50]}...")

conn.close()