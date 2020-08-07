import socket
import _thread

IP = input("Server IP: ")
PORT = 25565

rcvesock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rcvesock.connect((IP, PORT))

def receive():
    HEADERSIZE = 10
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



_thread.start_new_thread(receive, ())

while True:
    msgtosend = input()
    print("\nYou said: ", msgtosend, " but not really")