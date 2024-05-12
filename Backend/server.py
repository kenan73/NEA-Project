import socket 
import threading #allows for concurrent processing

PORT = 5050 #Connects to the port in which the server listens for incoming connections
HEADER = 1024
SERVER = socket.gethostbyname(socket.gethostname()) #'gethostname' retrieves hostname of the machine, 'gethostbyname' translates a host name to IPv4 address format.
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #'AF_INET' Specifies the family address for the socket. 'SOCK_STREAM' specifies the internet protocol used.
server.bind(ADDR)

def handle_client(conn, addr):
    print('[NEW CONNECTION] {addr} connected.')
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            
        print(f'[{addr}] {msg}')
        
    conn.close()

        #To prevent brute force attacks, for every connection, they are only allowed three attempts to input username and password

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() -1}')

print("[STARTING] Server is starting...")
start()