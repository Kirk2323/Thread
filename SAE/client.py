import socket
import os
host,port =('127.0.0.1', 2047)

client_socket = socket.socket()
client_socket.connect(("localhost", port))
#ce qui est reçu
msg =""
#ce qui est envoyé
data=""

#liste pour manier les OS
w = []

print("Le client vient de se connecter")

a = int(input("Voulez vous :"
              "\n1. Fermer la connexion"
              "\n2. Envoyer un message "
              "\n3. Connaître l'os du serveur"))

if a == 1:
    client_socket.close()
    print("La connexion vient d'être fermée")

if a == 2:
    print("Vous pouvez désormais envoyer un message")
    while msg != "exit" and msg != "bye" and data != "bye" and data != "exit":
        msg = input("-->")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print(data)
    client_socket.close()

if a == 3:
    r = os.name
    w.append(r)
    if "nt" in w:
        print("L'os du serveur est Windows.")
        #permet de retirer l'os de la liste au cas où l'utilisateur change d'os entre temps
        w.pop(0)
    if "posix" in w:
        print("L'os du serveur est Linux.")
        # permet de retirer l'os de la liste au cas où l'utilisateur change d'os entre temps
        w.pop(0)

while a != 1 and a!= 2 and a!=3 :
    a = int(input("Merci de choisir un chiffre valable (1 ou 2) \n"))
    if a == 1:
        print("La connexion vient d'être fermée")
    if a == 2:
        print("Vous pouvez désormais envoyer un message")
    if a == 3:
        r = os.name
        w.append(r)
        if "nt" in w:
            print("L'os du serveur est Windows.")
            # permet de retirer l'os de la liste au cas où l'utilisateur change d'os entre temps
            w.pop(0)
        if "posix" in w:
            print("L'os du serveur est Linux.")
            # permet de retirer l'os de la liste au cas où l'utilisateur change d'os entre temps
            w.pop(0)













