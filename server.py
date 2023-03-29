import threading
import socket


host = '127.0.0.1' #ip local, server local
port = 1025 #port utiliser pour le serveurs

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []

#fonction qui permet d'envoyer messsage a tous les client sur le serveurs
def broadcast(message):
    for client in clients:
        client.send(message)

#fonction qui regarde si le client est toujours sur le serveurs
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            #on enleve e client de la liste pour dire au chat qu'il est partit
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

#fonction qui recois les message
def receive():
    while True:
        client, address = server.accept()
        print(f'connected with (str{address})')
        #envoie Nick pour avoir les noms d'utilisateurs pour l'ajouter a la liste des users
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickame if the {nickname} !')
        #envoie un message dans le chat pour dire qui a rejoins le chat
        broadcast(f'{nickname} a rejoint le chat !\n'.encode('utf-8'))
        #client.send('connected to the server'.encode("utf-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('le serveur est en route...')
receive()