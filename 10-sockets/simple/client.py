from socket import socket, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5030))

message = input("Type a message for the server: ")
message_bytes = message.encode('utf-8')

client_socket.send(message_bytes)

