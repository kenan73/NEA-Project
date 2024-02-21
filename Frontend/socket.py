import socket 
import threading #allows for concurrent processing

PORT = 5050 #Connects to the port in which the server listens for incoming connections

HEADER = 64
SERVER = socket.gethostbyame(socket.gethostname()) #'gethostname' retreives hostname of the machine, 'gethostbyname' translates a host name to IPv4 address format.
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.sock_STREAM) #'AF_INET' Specifies the family address for the socket. 'SOCK_STREAM' specifies the internet protocol used.
server.bind(ADDR)

def handle_client(conn, addr):
    print('[NEW CONNECTION] {addr} connected.')
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f'[{addr}] {msg}')

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() -1}')

print("[STARTING] server is starting...")
start()