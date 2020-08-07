import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 25565))
s.listen(5)

HEADERSIZE = 10

while True:
    clientsocket, address = s.accept()
    print("connection from {0} has been established!".format(address))
    msg = "Connection established"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))
    
    while True:
        msg = input("Input message to send to clients: ")
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))