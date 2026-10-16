import socket


def server():
    server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_soket.bind(server_address)

    server_soket.listen(10)
    history = []
    while True:
        client_socket, client_address = server_soket.accept()
        print(f'Connection from {client_address} ')

        message = client_socket.recv(4024).decode()
        print(f'Пользователь с адресом: {client_address} отправил сообщение: {message}')


        history.append(message)
        client_socket.send('\n'.join(history).encode())

        client_socket.close()


if __name__ == '__main__':
    server()