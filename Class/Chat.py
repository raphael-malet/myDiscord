import socket
import threading
from datetime import datetime
from datetime import date

class Chat():
    def __init__(self,pseudo):
        self.pseudo=pseudo
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def EnvoieMessage(self):
        self.client.connect(('10.10.3.160', 1025))
        heure = datetime.now()
        heure_actuel = heure.strftime("%H:%M:%S")
        aujourdhui = date.today()
        jour = aujourdhui.strftime("%d/%m/%Y")
        while True:
            message = f'[{jour}] [{heure_actuel}] {self.pseudo}: {input("")}'
            self.client.send(message.encode('utf-8'))