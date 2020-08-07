import socket
import threading



USERN = input("username: ")
IP = input("Server IP: ")
PORT = 25565
HEADERSIZE = 10
rcvesock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rcvesock.connect((IP, PORT))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S_IP = "0.0.0.0"
S_PORT = 25565

def estabsend():
    s.bind((S_IP, S_PORT))
    print("Listening for connections...")
    s.listen(5)
    clientsocket, address = s.accept()
    print("connection from {0} has been established!".format(address))
    msg = USERN + " has connected"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))


def send(serversocket):
    msg = input()
    msg = USERN + " says: " + msg
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    serversocket.send(bytes(msg, "utf-8"))

def receive():
    full_msg = ''
    new_msg = True
    msglen = 0
    while True:
        msg = rcvesock.recv(16)
        print(msg)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False        
        full_msg += msg.decode("utf-8")
        if len(full_msg)-HEADERSIZE == msglen:
            print("\nServer says: ", full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''



threading._start_new_thread(receive, ())
estabsend()
while True:
    send(s)