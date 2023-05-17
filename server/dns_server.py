import socket

DNS_PORT = 8616

def handle_dns_request(data):
    # Обработка запроса DNS-сервера
    # ...

    # Пример: Возвращение фиктивного IP-адреса для всех запросов
    response = b'\xC0\x0C\x00\x01\x00\x01\x00\x00\x00\x00\x00\x04\x7F\x00\x00\x01'
    return response

def start_dns_server():
    # Создание UDP-сокета для DNS-сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', DNS_PORT))

    print('DNS server started on port', DNS_PORT)

    while True:
        data, addr = server_socket.recvfrom(1024)
        response = handle_dns_request(data)
        server_socket.sendto(response, addr)

if __name__ == '__main__':
    start_dns_server()

