import threading
import socket


class Server:
    def __init__(self):
        self.host = '127.0.0.1' #ip local, server local
        self.port = 1025 #port utiliser pour le serveurs

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.nicknames = []
        self.receive()

    #fonction qui permet d'envoyer messsage a tous les client sur le serveurs
    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    #fonction qui regarde si le client est toujours sur le serveurs
    def handle(self ,client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)

            except:
                #on enleve e client de la liste pour dire au chat qu'il est partit
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                break

    #fonction qui recois les message
    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'connected with (str{address})')
            #envoie Nick pour avoir les noms d'utilisateurs pour l'ajouter a la liste des users
            client.send("NICK".encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            self.nicknames.append(nickname)
            self.clients.append(client)
            print(f'Nickame if the {nickname} !')
            #envoie un message dans le chat pour dire qui a rejoins le chat
            self.broadcast(f'{nickname} a rejoint le chat !\n'.encode('utf-8'))
            #client.send('connected to the server'.encode("utf-8"))
            thread = threading.Thread(target=self.handle, args=(client,))
            print('le serveur est en route...')
            thread.start()




