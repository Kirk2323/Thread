import socket

#10.128.2.27
host,port =('10.128.2.27', 2048)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Le serveur se lance")
server_socket.bind((host,port))
server_socket.listen(1)
print("Le serveur est en attente de connexion")
socket.connect, add_client = server_socket.accept()
print(f"Le client {add_client[0]} est connecté")






