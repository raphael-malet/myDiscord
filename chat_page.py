import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from Class.Chat import Chat
import socket
import threading
from datetime import datetime
from datetime import date
import tkinter.scrolledtext
import time

admin = mysql.connector.connect(host="localhost", user="root", password="vatefaireencule", database="mydiscord")
cursor = admin.cursor()

class Chat_page:

    def __init__(self, email):
        self.email = email
        self.continuer = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.liste_message = []
        self.longueur_liste = 0
        self.dernier_message = ''

        fenetre = tk.Tk()
        fenetre.geometry('600x720')
        fenetre.title('My Discord')
        fenetre.configure(bg='#000000')
        try:
            self.client.connect(('10.10.6.22', 1025))
        except:
            tk.messagebox.showwarning("Test","Test")

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

        self.section_afficher_message =tkinter.scrolledtext.ScrolledText(section_droite, bg='GREY', width=50)
        self.section_afficher_message.grid(sticky=N)


        # Section Chat
        section_entrer_chat = Frame(section_droite)
        section_entrer_chat.configure(bg='GREY', width=500, height=100)
        section_entrer_chat.grid(row=2, )


        self.section_texte_chat = Entry(section_entrer_chat, bg='WHITE', width=40, fg='BLACK')
        self.section_texte_chat.grid(column=4,row=2)

        bouton_entrer_chat = Button(section_entrer_chat, text='Entrer',command=lambda : self.EnvoieMessage(self.section_texte_chat.get()))
        bouton_entrer_chat.grid(column=2,row=2)

        afficher_fenetre = threading.Thread(target=self.lancerfenetre, args=fenetre)
        afficher_fenetre.start()

        recois_message = threading.Thread(target=self.recoisMessage)
        recois_message.start()

        #afficher_message_recus = threading.Thread(target=self.afficher_message_dans_listebox)
        #afficher_message_recus.start()

        envoie_message = threading.Thread(target=self.EnvoieMessage)
        envoie_message.start()

    def lancerfenetre(self, fenetre):
        fenetre = fenetre
        self.afficher_message_dans_listebox()
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

    def recoisMessage(self):
        self.pseudo = self.pseudoUtilisateur()
        while True:
            #try:
            self.message = self.client.recv(1024).decode('utf-8')
            if message == 'NICK':
                self.client.send(self.pseudo.encode('utf-8'))
            else:
                try:
                    if bool(self.message):
                        self.liste_message.append(message)
                        print(self.liste_message)
                        self.dernier_message = message
                        print(self.dernier_message)
                        self.section_afficher_message.insert(END, self.message)
                except:
                    pass
            #except:
             #   print('error occured!')
              #  self.client.close()
               # break

    def EnvoieMessage(self, mess):
        heure = datetime.now()
        heure_actuel = heure.strftime("%H:%M:%S")
        aujourdhui = date.today()
        jour = aujourdhui.strftime("%d/%m/%Y")
        self.pseudo = self.pseudoUtilisateur()
        message = f'[{jour}] [{heure_actuel}] {self.pseudo}: {mess}'
        self.client.send(message.encode('utf-8'))
        self.section_afficher_message.insert(END, message)
        self.section_texte_chat.delete(0, END)


    def afficher_message_dans_listebox(self):
        if self.longueur_liste != len(self.liste_message):
            mess = self.dernier_message
            print(type(mess))
            self.section_afficher_message.insert(END, mess)
            self.longueur_liste = len(self.liste_message)












