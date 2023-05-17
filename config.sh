#!/bin/bash

# Настройки сервера
SERVER_PORT=443
DNS_PORT=8616

# Настройки базы данных
DB_HOST="localhost"
DB_PORT=3306
DB_NAME="joker_browser"
DB_USER="username"
DB_PASSWORD="password"

# Настройки путей к файлам
DATA_DOMAINS="server/data_domains.csv"
DATA_SQL="server/data_sql.db"

# Экспорт переменных окружения
export SERVER_PORT
export DNS_PORT
export DB_HOST
export DB_PORT
export DB_NAME
export DB_USER
export DB_PASSWORD
export DATA_DOMAINS
export DATA_SQL

echo '1. Запустить Joker'
echo '2. Создать домен'
read -p "Введите номер категрии: " input

if [ "$input" == "1" ]; then
  	# Запуск сервера и DNS-сервера
	python server/main.py &
	python server/dns_server.py &
	python browser/app.py &
elif [ "$input" == "2" ]; then
	cd server
	python create_domain.py
	cd -
else
	exit 0
fi

