import socket

host,port =('10.128.2.27', 2048)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

data =client_socket.recv(1024).decode()
print("Le client vient de se connecter")