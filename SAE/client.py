import socket
import os
import psutil
import platform

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
a=0

while a!=1:
    a = int(input("Voulez vous :"
                  "\n1. Fermer la connexion : "
                  "\n2. Avoir l'adresse IP locale :"
                  "\n3. Connaître l'os :"
                  "\n4. Obtenir l'usage du CPU :"
                  "\n5. Avoir le nom du poste :"
                  "\n6. Obtenir la quantité de RAM :"))
    if a == 1:
        print("\nLa connexion vient d'être fermée")

    if a == 2:
        print(f"\nVoici l'adresse IP du pc : {socket.gethostbyname(socket.gethostname())}\n")

    if a == 3:
        print(f"\nNom de l'os :", platform.system())
        print(f"Version du système :{platform.release()}\n")

    if a == 4:
        print(f'\nL"usage du CPU est : {psutil.cpu_percent(4)}\n')

    if a==5:
        print(f"\nLe nom du pc est : {socket.gethostname()} \n" )

    if a ==6:
        # Getting % usage of virtual_memory ( 3rd field)
        print(f'\nMémoire RAM utilisé: {psutil.virtual_memory()[2]} %')
        # Getting usage of virtual_memory in GB ( 4th field)
        vm = round(psutil.virtual_memory()[3] / 1000000000,2)
        print(f'RAM Utilisé (GB): {vm}\n')



while a != 1 and a!= 2 and a!=3 and a!=4 and a!=5 :
    a = int(input("Merci de choisir un chiffre valable (1 ou 2) \n"))
    if a == 1:
        print("La connexion vient d'être fermée")
        socket.connect.close()
    if a == 2:
        print(f"Voici l'adresse IP du pc : {socket.gethostbyname(socket.gethostname())}\n")
    if a == 3:
        print(f"\nNom de l'os :", platform.system())
        print(f"Version du système :{platform.release()}\n")
    if a == 4:
        print(f'\nL"usage du CPU est : {psutil.cpu_percent(3)}\n')

    if a==5:
        print(f"\nLe nom du pc est : {socket.gethostname()} \n" )

    if a ==6:
        # Getting % usage of virtual_memory ( 3rd field)
        print(f'\nMémoire RAM utilisé: {psutil.virtual_memory()[2]} %')
        # Getting usage of virtual_memory in GB ( 4th field)
        vm = round(psutil.virtual_memory()[3] / 1000000000,2)
        print(f'RAM Utilisé (GB): {vm}\n')










