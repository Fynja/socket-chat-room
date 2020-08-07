import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 25565))
s.listen(5)


def threaded_client(connection, info):
    i = 0
    HEADERSIZE = 10
    requestclientconnection(info)

    while True:
       # i += 10
       # time.sleep(10)
      #  msg = "you've been connected to the server for {0} secconds".format(i)
      #  print(msg)
       # msg = f'{len(msg):<{HEADERSIZE}}' + msg
       # print(msg)
       # connection.send(bytes(msg, "utf-8"))

        data = connection.recv(16)
        reply = f'{len(data):<{HEADERSIZE}}' + data
        if not data:
            break
        connection.sendall(bytes(reply,"utf-8"))
    connection.close()

def requestclientconnection(info):
    while True:
        try:
            r.connect((info[0], info[1]))
            print("Connection succesful")
        except:
            print("couldn't connect..")
        
def receive(rcvesock):
    full_msg = ''
    new_msg = True
    msglen = 0
    HEADERSIZE = 10
    while True:
        msg = rcvesock.recv(16)
        print(msg)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False        
        full_msg += msg.decode("utf-8")
        if len(full_msg)-HEADERSIZE == msglen:
            print("\n", full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''



ThreadCount = 0
while True:
    Client, info = s.accept()
    print('Connected to: ' + info[0] + ':' + str(info[1]))
    threading._start_new_thread(threaded_client, (Client, ), info)
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    threading._start_new_thread(requestclientconnection, (Client, ), info)
    threading._start_new_thread(receive, (Client, ))

s.close()