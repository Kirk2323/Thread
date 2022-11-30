import socket
import os
import psutil
import platform

host,port =('127.0.0.1', 2089)

client_socket = socket.socket()
client_socket.connect(("localhost", port))

#ce qui est reçu
msg =""
#ce qui est envoyé
data=""
#liste pour manier les OS
w = []
print("Le client vient de se connecter")
a=0

while msg != "1" and data != "1" and msg != "7" and data != "7":
    msg = input("Voulez vous :"
                   "\n1. Fermer la connexion : "
                   "\n2. Avoir l'adresse IP locale :"
                   "\n3. Connaître l'os :"
                   "\n4. Obtenir l'usage du CPU :"
                   "\n5. Avoir le nom du poste :"
                   "\n6. Obtenir la quantité de RAM :")

    if msg == "1":
        print("Vous allez être déconnecté")
        # Ajouter un moyen de se déco
    else:
        client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    print(data)

client_socket.close()





