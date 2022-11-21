import socket
import os
import sys

#10.128.2.27
host,port =('127.0.0.1', 2049)
print("Le serveur se lance")

server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen(1)

while True:
    conn,address = server_socket.accept()
    msg=""
    data=""
    while msg != "exit" and msg != "bye" and data != "bye" and data != "exit":
        data = conn.recv(1024).decode()
        print(data)
        msg=input("serveur -->")
        conn.send(msg.encode())
    rep = input("continuer (y/n)")
    if rep =="n":
        break
server_socket.close()

#print("Le serveur se lance")
#server_socket.bind((host,port))
#server_socket.listen(1)
#print("Le serveur est en attente de connexion")
#socket.connect, add_client = server_socket.accept()
#print(f"Le client {add_client[0]} est connecté sur le port {add_client[1]} ")


# make a thread that listens for messages to this client & print them
#t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
#t.daemon = True
# start the thread
#t.start()






