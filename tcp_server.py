import socket




def server():
    server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_soket.bind(server_address)

    server_soket.listen(5)
    print(f"Server is started and wait for connection...")

    while True:
        client_socket, client_address = server_soket.accept()
        print(f'Connection from {client_address} ')

        data =client_socket.recv(1024).decode()
        print(f'Received {data}')

        response = f"Сервер получил: {data}"
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == '__main__':
    server()