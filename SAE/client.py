import socket, os, csv

class Client:

    def __init__(self):
        self.__dico = {}
        f = open('fichier.csv', 'r')
        obj = csv.reader(f)
        for lignes in obj:
            self.__a = lignes[0]
            self.__dico[lignes[0]] = lignes[1]


    def start(self):
        self.__client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__client_socket.connect((str(self.__a), int(self.__dico.get(self.__a))))
        print("Le client vient de se connecter")
        self.message()



    def message(self):
        # ce qui est reçu
        msg = ""
        # ce qui est envoyé
        data = ""
        while msg != "1" and data != "1" and msg != "8" and data != "8":
            msg = input("Voulez vous :"
                           "\n1. Fermer la connexion : "
                           "\n2. Avoir l'adresse IP locale :"
                           "\n3. Connaître l'os :"
                           "\n4. Obtenir l'usage du CPU :"
                           "\n5. Avoir le nom du poste :"
                           "\n6. Obtenir la quantité de RAM :"
                            "\n7. Utiliser l'invite de commande Windows")
            if msg == "1":
                print("Vous allez être déconnecté")
                # Ajouter un moyen de se déco
            elif msg =="7":
                self.commande()
            else:
                self.__client_socket.send(msg.encode())
            data = self.__client_socket.recv(1024).decode()
            print(data)
        self.__client_socket.close()

#Tout refaire ATTENTION NE FONCTIONNE MEME SI YA DE L'IDEE
    def commande(self):
        msg = "quit"
        while msg != quit:
            msg = input("Vous pouvez saisir votre commande :")
            self.__client_socket.send(msg.encode())
            data = self.__client_socket.recv(1024).decode()
            print(data)
        else:
            self.message()


