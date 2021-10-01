import socket

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "$$__DISCONNECT"
# SERVER = "<ip_here">
SERVER = "10.0.0.13"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def sendMessageToServer(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))


sendMessageToServer("Hello World!")
sendMessageToServer("Hello World 2!")
sendMessageToServer("Hello World 3!")
sendMessageToServer(DISCONNECT_MESSAGE)
