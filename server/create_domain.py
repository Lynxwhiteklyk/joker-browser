import sqlite3

def get_database_connection():
    # Функция для получения подключения к базе данных
    conn = sqlite3.connect('data/data_sql.db')
    return conn

def create_domain(name, ip_address):
    # Функция для создания нового домена и сохранения его в базе данных
    conn = get_database_connection()
    cursor = conn.cursor()

    # Выполнение SQL-запроса для создания нового домена
    cursor.execute("INSERT INTO domains (name, ip_address) VALUES (?, ?)", (name, ip_address))

    # Сохранение изменений в базе данных
    conn.commit()

    # Закрываем соединение с базой данных
    conn.close()

    print("Домен успешно создан!")

# Пример использования функции create_domain
domain_name = input("Введите имя домена: ")
ip_address = input("Введите IP-адрес: ")

create_domain(domain_name, ip_address)

