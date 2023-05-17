import sqlite3

def get_database_connection():
    # Функция для получения подключения к базе данных
    conn = sqlite3.connect('server/data/data_sql.db')
    return conn

def search_data(query):
    # Функция для выполнения поиска данных в базе данных
    conn = get_database_connection()
    cursor = conn.cursor()

    # Выполнение SQL-запроса для поиска данных
    cursor.execute("SELECT * FROM domains WHERE name LIKE ? OR ip_address LIKE ?", ('%' + query + '%', '%' + query + '%'))
    result = cursor.fetchall()

    # Закрываем соединение с базой данных
    conn.close()

    return result


