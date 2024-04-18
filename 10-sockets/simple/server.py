from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5030))

server_socket.listen()
print("Server started on port 5030")

while True:
    connection, address = server_socket.accept()
    print("Connection incoming from:", address)

    data = connection.recv(1024)
    message = data.decode('utf-8')
    print(message)



