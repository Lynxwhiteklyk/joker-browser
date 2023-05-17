from flask import Flask, render_template
from protocol_joker import JokerProtocol
from server import handle_common_request
from sql_config import setup_database
from domains import DomainManager
from search_db import search_data

app = Flask(__name__)

# Создание экземпляров классов и настройка базы данных
data_file = 'server/data/data_sql.db'
joker_protocol = JokerProtocol()
domain_manager = DomainManager(data_file)
setup_database()

@app.route('/')
def index():
    return render_template('hosts/search.html')

@app.route('/joker/<path:url>')
def handle_joker_url(url):
    try:
        path = joker_protocol.parse_url(url)
        # Обработка пути в протоколе Joker
        # ...

        return "Joker response"
    except ValueError as e:
        return str(e), 400

@app.route('/common')
def handle_common():
    return handle_common_request()

@app.route('/search')
def handle_search():
    return search_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)

