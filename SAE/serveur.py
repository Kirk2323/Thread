import socket,os, sys, platform, psutil


class Server:
    def __init__(self):
        self.__host, self.__port =('0.0.0.0', 2047)
        self.__server_socket = None
        self.__conn = None
        self.__addr = None


    def start(self):
        print("Le serveur se lance")
        self.__server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__server_socket.bind((self.__host,self.__port))
        self.connexion()

    def connexion(self):
        self.__server_socket.listen(1)
        print(f"Le serveur {self.__host} est en attente de connexion")
        self.__conn, self.__addr = self.__server_socket.accept()
        self.message()

    def message(self):
        while True :
            msg = ""
            data = ""

            while msg != "1" and data != "1" and msg != "7" and data != "7":
                data = self.__conn.recv(1024).decode()
                print(data)
                # if data=="1":
                    #FAIRE UN MOYEN DE SE DECONNECTER
                if data == "2":
                    message = f"\nVoici l'adresse IP du pc : {socket.gethostbyname(socket.gethostname())}\n"
                    self.__conn.send(message.encode())
                elif data == "3":
                    message = f"\nNom de l'os : {platform.system()} | Version du système : {platform.release()}\n"
                    self.__conn.send(message.encode())
                elif data == "4":
                    message = f'\nL"usage du CPU est : {psutil.cpu_percent(4)}\n'
                    self.__conn.send(message.encode())
                elif data == "5":
                    message = f"\nLe nom du pc est : {socket.gethostname()} \n"
                    self.__conn.send(message.encode())
                elif data =="6":
                    vm = round(psutil.virtual_memory()[3] / 1000000000, 2)
                    message = f'\nMémoire RAM utilisé: {psutil.virtual_memory()[2]} % | RAM Utilisé (GB): {vm}\n'
                    self.__conn.send(message.encode())
                #A MODIFIER AUSSI AVEC LE DEF COMMANDE
                elif data== "quit":
                    message = "Vous venez de quitter l'invite de commande, retour de la liste des commandes via numéro :"
                    self.__conn.send(message.encode())

                else:
                    message = os.system(data)
                    self.__conn.send(msg.encode())
            self.__conn.close()

serv = Server()
serv.start()

