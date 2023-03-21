import socket
import threading
from datetime import datetime
from datetime import date

class Chat():
    def __init__(self,pseudo):
        self.pseudo=pseudo
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def RecoisMessage(self):
        self.client.connect(('10.10.3.160', 1025))
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.client.send(self.pseudo.encode('utf-8'))
                else:
                    print(message)
            except:
                print('error occured!')
                self.client.close()
                break

    def EnvoieMessage(self):
        heure = datetime.now()
        heure_actuel = heure.strftime("%H:%M:%S")
        aujourdhui = date.today()
        jour = aujourdhui.strftime("%d/%m/%Y")
        while True:
            message = f'[{jour}] [{heure_actuel}] {self.pseudo}: {input("")}'
            self.client.send(message.encode('utf-8'))

    receive_thread = threading.Thread(target=RecoisMessage)
    receive_thread.start()

    write_thread = threading.Thread(target=EnvoieMessage)
    write_thread.start()