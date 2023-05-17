import sqlite3

def get_database_connection():
    # Функция для получения подключения к базе данных
    conn = sqlite3.connect('server/data/data_sql.db')
    return conn

def setup_database():
    # Функция для настройки базы данных
    conn = get_database_connection()
    cursor = conn.cursor()

    # Создание таблицы domains, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY,
            name TEXT,
            ip_address TEXT
        )
    ''')

    # Закрываем соединение с базой данных
    conn.close()

