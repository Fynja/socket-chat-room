import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 25565))
s.listen(5)

HEADERSIZE = 10


def threaded_client(connection):
    i = 0
    
    connection.send(bytes("welcome to the Server!", "utf-8"))
    while True:
        i += 1
        time.sleep(1)
        msg = "you've been connected to the server for {0} secconds".format(i)
        connection.send(bytes(msg, "utf-8"))




#while True:
   # clientsocket, address = s.accept()
    #print("connection from {0} has been established!".format(address))
   # msg = "Connection established"
  #  msg = f'{len(msg):<{HEADERSIZE}}' + msg
 #   clientsocket.send(bytes(msg, "utf-8"))

#    thread1 = threading.Thread(target=threaded_client)


ThreadCount = 0
while True:
    Client, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    threading.start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
s.close()