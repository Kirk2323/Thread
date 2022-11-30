import socket
import os
import sys
import psutil
import platform

host,port =('127.0.0.1', 2089)
print("Le serveur se lance")

server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen(1)

print(f"Le serveur {host} est en attente de connexion")






while True :
    conn, address = server_socket.accept()
    msg = ""
    data = ""

    while msg != "1" and data != "1" and msg != "7" and data != "7":
        data = conn.recv(1024).decode()
        print(data)
        # if data=="1":
            #FAIRE UN MOYEN DE SE DECONNECTER
        if data == "2" :
            message = f"\nVoici l'adresse IP du pc : {socket.gethostbyname(socket.gethostname())}\n"
            conn.send(message.encode())
        elif data == "3":
            message = f"\nNom de l'os : {platform.system()} | Version du système : {platform.release()}\n"
            conn.send(message.encode())
        elif data == "4":
            message = f'\nL"usage du CPU est : {psutil.cpu_percent(4)}\n'
            conn.send(message.encode())
        elif data == "5":
            message = f"\nLe nom du pc est : {socket.gethostname()} \n"
            conn.send(message.encode())
        elif data =='6':
            vm = round(psutil.virtual_memory()[3] / 1000000000, 2)
            message = f'\nMémoire RAM utilisé: {psutil.virtual_memory()[2]} % | RAM Utilisé (GB): {vm}\n'
            conn.send(message.encode())
        else:
            msg='Votre commande n"existe pas, merci de rentrer un chiffre valide.'
            conn.send(msg.encode())
    conn.close()

