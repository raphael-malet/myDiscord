import threading
import socket

host = '10.10.6.22' #ip local, server local
port = 1025

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname}  quitte le chat !".encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()

        print(f'connected with (str{address})')
        client.send("NICK".encode('utf-8'))

        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickame if the {nickname} !')

        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))

        client.send('connected to the server'.encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('le serveur est en route...')
receive()