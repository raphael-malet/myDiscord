import tkinter as tk
from tkinter import *
import mysql.connector
import socket
import threading
from datetime import datetime
from datetime import date
import tkinter.scrolledtext

admin = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="mydiscord")
cursor = admin.cursor()
class Chat_page:

    def __init__(self, email):
        self.email = email
        self.continuer = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('10.10.1.143', 1025))
        self.liste_message = []
        self.longueur_liste = 0
        self.dernier_message = ''
        self.gui_done = False
        self.running = True
        affichage = threading.Thread(target=self.Fenetreloop)
        affichage.start()
        recois_message = threading.Thread(target=self.receive)
        recois_message.start()


    def Fenetreloop(self):
        fenetre = tk.Tk()
        fenetre.geometry('640x720')
        fenetre.title('My Discord')
        fenetre.configure(bg='#000000')
        fenetre.resizable(False,False)

        section_chanel_gauche = Frame()
        section_chanel_gauche.configure(bg='WHITE')
        section_chanel_gauche.pack(side=LEFT, fill=Y)

        afficher_email = Label(section_chanel_gauche, text=self.pseudoUtilisateur(), fg='WHITE', bg='BLACK')
        afficher_email.grid()

        liste_channel = Listbox(section_chanel_gauche, width=10, fg='BLACK', bg='RED', height=39)
        liste_channel.grid(pady=5)

        section_droite = Frame()
        section_droite.configure(bg='WHITE', width=500)
        section_droite.pack(side=RIGHT, fill=Y)

        section_droite_afficher_message = Frame(section_droite)
        section_droite_afficher_message.grid(rows=1)

        self.section_afficher_message = tkinter.scrolledtext.ScrolledText(section_droite, bg='GREY', width=50, height=34)
        self.section_afficher_message.grid(sticky=N)

        # Section Chat
        section_entrer_chat = Frame(section_droite)
        section_entrer_chat.configure(bg='GREY', width=500, height=100)
        section_entrer_chat.grid(row=2, )

        self.section_texte_chat = Entry(section_entrer_chat, bg='WHITE', width=40, fg='BLACK')
        self.section_texte_chat.grid(column=4, row=2)

        bouton_entrer_chat = Button(section_entrer_chat, text='Entrer',
                                    command=lambda: self.EnvoieMessage(self.section_texte_chat.get()))
        bouton_entrer_chat.grid(column=2, row=2)
        commande = "select message from public"
        cursor.execute(commande)
        cursor.fetchall()
        for message in cursor:
            self.section_afficher_message.insert('end',str(message))

        self.gui_done=True
        fenetre.mainloop()


    def pseudoUtilisateur(self):

        valeur = self.email
        commande = "select nom,prenom from utilisateurs where mail=%s"
        cursor.execute(commande, (valeur, ))
        pseudo = cursor.fetchall()
        for i in pseudo:
            for x in i:
                pseudo = x + ' '+i[1]
                return pseudo

    def receive(self):
        self.pseudo = self.pseudoUtilisateur()
        while self.running:
            try:
                self.message = self.client.recv(1024).decode('utf-8')
                if self.message == 'NICK':
                    self.client.send(self.pseudo.encode('utf-8'))
                else:
                    if self.gui_done:
                        print(self.message)
                        self.section_afficher_message.config(state='normal')
                        self.section_afficher_message.insert('end', self.message)
                        self.section_afficher_message.yview('end')
                        self.section_afficher_message.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print('error')
                self.client.close()
                break

    def EnvoieMessage(self, mess):
        heure = datetime.now()
        heure_actuel = heure.strftime("%H:%M:%S")
        aujourdhui = date.today()
        jour = aujourdhui.strftime("%d/%m/%Y")
        self.pseudo = self.pseudoUtilisateur()
        message = f'[{jour}] [{heure_actuel}] {self.pseudo}: {mess}\n'
        self.client.send(message.encode('utf-8'))
        self.section_afficher_message.insert(END, message)
        self.section_texte_chat.delete(0, END)
        valeur = message
        commande = "insert into public (message) values (%s)"
        cursor.execute(commande, valeur)
        admin.commit()
