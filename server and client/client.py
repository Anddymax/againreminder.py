import socket
import threading
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
def handle_client(conn, addr):
    print(f"NEW CONNECTION {addr} connected.")
def start():
    server.listen()
    while True:
        conn, addr=server.accept()
        thread = threading.Thread(target=handle_client,args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threating.activeCount()-1} ")
print("[SRARTING] server is starting.....")
start()
