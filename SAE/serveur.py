import socket
import os
import sys

host,port =('127.0.0.1', 2047)
print("Le serveur se lance")

server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen(1)

print(f"Le serveur {host} est en attente de connexion")

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









