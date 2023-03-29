import tkinter as tk
from tkinter import *
import mysql.connector
import socket
import threading
from datetime import datetime
from datetime import date
import tkinter.scrolledtext
import tkinter.messagebox

# Connexion a la base de données
admin = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="mydiscord")
cursor = admin.cursor()


class Chat_page:

    def __init__(self, email):
        self.email = email
        self.continuer = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connexion au serveur
        self.client.connect(('10.10.1.7', 1025))
        self.longueur_liste = 0
        self.gui = False
        self.en_cours = True


        recois_message = threading.Thread(target=self.ReceptionMessage)
        recois_message.start()

        # Définition des paramètres de la fenêtre
        self.fenetre = tk.Tk()
        self.fenetre.geometry('640x720')
        self.fenetre.title('My Discord')
        self.fenetre.configure(bg='#000000')
        self.fenetre.resizable(False, False)

        section_chanel_gauche = Frame()
        section_chanel_gauche.configure(bg='WHITE')
        section_chanel_gauche.pack(side=LEFT, fill=Y)
        # Section pour afficher le nom de l'utilisateur
        afficher_email = Label(section_chanel_gauche, text=self.pseudoUtilisateur(), fg='WHITE', bg='BLACK')
        afficher_email.grid()
        # Section pour afficher la liste des channels
        liste_channel = Frame(section_chanel_gauche, width=10)
        liste_channel.config(bg='RED', height=500)
        liste_channel.grid(sticky=EW)

        #bouton accéder serveur

        section_droite = Frame()
        section_droite.configure(bg='WHITE', width=500)
        section_droite.pack(side=RIGHT, fill=Y)

        section_droite_afficher_message = Frame(section_droite)
        section_droite_afficher_message.grid(rows=1)

        # Section afficher les messages du chat
        self.section_afficher_message = tkinter.scrolledtext.ScrolledText(section_droite, bg='GREY', width=50,
                                                                          height=34)
        self.section_afficher_message.grid(sticky=N)

        # Section Chat
        section_entrer_chat = Frame(section_droite)
        section_entrer_chat.configure(bg='GREY', width=500, height=100)
        section_entrer_chat.grid(row=2, )
        # Section pour entrer le texte à envoyer
        self.section_texte_chat = Entry(section_entrer_chat, bg='WHITE', width=40, fg='BLACK')
        self.section_texte_chat.grid(column=4, row=2)
        # Bouton Envoyer message
        bouton_entrer_chat = Button(section_entrer_chat, text='Entrer',
                                    command=lambda: self.EnvoieMessage(self.section_texte_chat.get()))
        bouton_entrer_chat.grid(column=2, row=2)



        # Bouton déconnexion
        bouton_deconnexion = Button(section_chanel_gauche, text='Déconnexion', bg="RED",
                                    command=lambda: self.Deconnexion())
        bouton_deconnexion.grid(column=0, row=2)


        # Bouton Liste Serveur
        bouton_liste_serveur = Button(section_chanel_gauche, text='Liste Serveur',bg="BLUE",
                                    command=lambda: self.ListeServeur())
        bouton_liste_serveur.grid(column=0, row=3)
        # Affichage de l'historique des messages
        commande = "select message from public"
        cursor.execute(commande)
        for message in cursor:
            self.section_afficher_message.insert('end', str(message)[2:-3] + "\n")

        bouton_creer_serveur = Button(section_chanel_gauche, text='creer channel', bg='RED')
        bouton_creer_serveur.grid(column=0, row=4)

        # Variable pour indiquer que la fenêtre a été créer
        self.gui = True
        self.fenetre.mainloop()

    def pseudoUtilisateur(self):
        # Récupère le nom et prénom pour en faire un pseudo
        valeur = self.email
        commande = "select nom,prenom from utilisateurs where mail=%s"
        cursor.execute(commande, (valeur,))
        pseudo = cursor.fetchall()
        for i in pseudo:
            for x in i:
                pseudo = x + ' ' + i[1]
                return pseudo

    def ReceptionMessage(self):
        self.pseudo = self.pseudoUtilisateur()
        while self.en_cours:
            # Affiche les messages reçus dans myDiscord
            try:
                self.message = self.client.recv(1024).decode('utf-8')
                if self.message == 'NICK':
                    self.client.send(self.pseudo.encode('utf-8'))
                else:
                    if self.gui:
                        print(self.message)
                        self.section_afficher_message.config(state='normal')
                        self.section_afficher_message.insert('end', self.message)
                        self.section_afficher_message.yview('end')
                        self.section_afficher_message.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print('Erreur')
                self.client.close()
                break

    def EnvoieMessage(self, mess):
        # Date et Heure des messages
        heure = datetime.now()
        heure_actuel = heure.strftime("%H:%M:%S")
        aujourdhui = date.today()
        jour = aujourdhui.strftime("%d/%m/%Y")
        # Récupère le pseudo de l'utilisateur
        self.pseudo = self.pseudoUtilisateur()
        # Envoie le message sur myDiscord
        message = f'[{jour}] [{heure_actuel}] {self.pseudo}: {mess}\n'
        self.client.send(message.encode('utf-8'))
        self.section_afficher_message.insert(END, message)
        self.section_texte_chat.delete(0, END)
        # Ajout des messages dans la database pour l'historique
        message_db = f'[{jour}] [{heure_actuel}] {self.pseudo}: {mess}'
        commande = "insert into public (message) value (%s)"
        cursor.execute(commande, (message_db,))
        admin.commit()

    def ListeServeur(self):
        liste_serveur = []
        str_liste_serveur = ''
        commande = "select nom,port from channel"
        cursor.execute(commande)
        for port in cursor:
            liste_serveur.append(port)
        for i in liste_serveur:
            str_liste_serveur += str(i)[2:-1]+'\n'
        tkinter.messagebox.showinfo("Liste des serveurs", str_liste_serveur)

    def Deconnexion(self):
        self.client.close()
        self.fenetre.destroy()
        import main

