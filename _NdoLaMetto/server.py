import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
# SERVER = '<ip_here>
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "$$__DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION FROM] : {addr}")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            mes = conn.recv(msg_length).decode(FORMAT)

            if mes == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}]: {mes}")
            conn.send("Message sent from server".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[SERVER]: Listening on port {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[TOTAL CLIENT CONNECTED]: {threading.active_count() - 1}")


start()
