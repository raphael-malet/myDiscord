import tkinter as tk
from tkinter import *
import mysql.connector
import socket
import threading
from datetime import datetime
from datetime import date
import tkinter.scrolledtext
import tkinter.messagebox
from tkinter.simpledialog import askstring

# Connexion a la base de données
admin = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="mydiscord")
cursor = admin.cursor()


class Chat_page:

    def __init__(self, email):
        self.email = email
        self.continuer = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connexion au serveur
        self.port = 1025
        self.client.connect(('127.0.0.1', self.port))
        self.longueur_liste = 0
        self.gui = False
        self.en_cours = True
        self.channel = 'public'

        recois_message = threading.Thread(target=self.ReceptionMessage)
        recois_message.start()

        # Définition des paramètres de la fenêtre
        self.fenetre = tk.Tk()
        self.fenetre.geometry('900x720')
        self.fenetre.title('My Discord')
        self.fenetre.configure(bg='#000000')
        self.fenetre.resizable(False, False)

        section_chanel_gauche = Frame()
        section_chanel_gauche.configure(bg='BLACK')
        section_chanel_gauche.pack(side=LEFT, fill=Y)
        # Section pour afficher le nom de l'utilisateur
        afficher_email = Label(section_chanel_gauche, text=self.pseudoUtilisateur(), fg='WHITE', bg='BLACK')
        afficher_email.grid()

        # Section pour afficher la liste des channels
        self.liste_channel = Frame(section_chanel_gauche, width=10)
        self.liste_channel.config(bg='BLACK', height=500)
        self.liste_channel.grid(sticky=EW)

        # bouton accéder serveur
        section_droite = Frame()
        section_droite.configure(bg='BLACK', width=500)
        section_droite.pack(side=RIGHT, fill=Y)

        section_droite_afficher_message = Frame(section_droite)
        section_droite_afficher_message.grid(rows=1)

        # Section afficher les messages du chat
        self.section_afficher_message = tkinter.scrolledtext.ScrolledText(section_droite, bg='GREY',
                                                                          height=34)
        self.section_afficher_message.grid(sticky=EW)

        # Section Chat
        section_entrer_chat = Frame(section_droite)
        section_entrer_chat.configure(bg='BLACK', width=500, height=100)
        section_entrer_chat.grid(row=2, )
        # Section pour entrer le texte à envoyer
        self.section_texte_chat = Entry(section_entrer_chat, bg='WHITE', width=85, fg='BLACK')
        self.section_texte_chat.grid(column=4, row=2)
        # Bouton Envoyer message
        bouton_entrer_chat = Button(section_entrer_chat, text='Entrer',
                                    command=lambda: self.EnvoieMessage(self.section_texte_chat.get()))
        bouton_entrer_chat.grid(column=2, row=2)

        section_gauche_bas = Frame(section_chanel_gauche)
        section_gauche_bas.config(bg='WHITE')
        section_gauche_bas.grid(sticky=N, pady=10)

        # Bouton déconnexion
        bouton_deconnexion = Button(section_gauche_bas, font=('', 11, "bold"), text='Déconnexion', bg="RED",
                                    command=lambda: self.Deconnexion())
        bouton_deconnexion.grid(column=0, row=4, sticky=EW)

        # Bouton Liste Serveur
        bouton_liste_serveur = Button(section_gauche_bas, font=('', 11, "bold"), text='Liste Serveur', bg="BLUE",
                                      command=lambda: self.ListeServeur())
        bouton_liste_serveur.grid(column=0, row=3, sticky=EW)
        # Affichage de l'historique des messages
        commande = "select message from public"
        cursor.execute(commande)
        for message in cursor:
            self.section_afficher_message.insert('end', str(message)[2:-3] + "\n")
        # Bouton pour créer des channels
        bouton_creer_serveur = Button(section_gauche_bas, font=('', 11, "bold"), text='Créer un Channel', bg='GREEN',
                                      command=lambda: self.creation_channel())
        bouton_creer_serveur.grid(column=0, row=2, sticky=EW)

        afficher_bouton_serveur = threading.Thread(target=self.afficher_bouton_serveur)
        afficher_bouton_serveur.start()

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
                        self.section_afficher_message.config(state='normal')
                        self.section_afficher_message.insert('end', self.message)
                        self.section_afficher_message.yview('end')
                        self.section_afficher_message.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print('Connexion Perdu !')
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
        commande = "insert into " + self.channel + " (message) value (%s)"
        cursor.execute(commande, (message_db,))
        admin.commit()

    def ListeServeur(self):
        # Affiche une pop-up avec les nom et port des channels
        liste_serveur = []
        str_liste_serveur = ''
        commande = "select nom,port from channel"
        cursor.execute(commande)
        for port in cursor:
            liste_serveur.append(port)
        for i in liste_serveur:
            str_liste_serveur += str(i)[2:-1] + '\n'
        tkinter.messagebox.showinfo("Liste des serveurs", str_liste_serveur)

    def Deconnexion(self):
        # Déconnecte l'utilisateur du serveur et de sa session
        self.client.close()
        self.fenetre.destroy()
        import main

    def afficher_bouton_serveur(self):
        # Affiche les boutons des channels
        commande = 'select nom from channel'
        cursor.execute(commande)
        i = 0
        for nom in cursor:
            bouton_channel = Button(self.liste_channel, text=nom, bg='WHITE',
                                    command=lambda bouton=nom: self.afficher_channel(bouton))
            bouton_channel.grid(column=0, row=i, sticky=EW, ipadx=43, pady=3)
            i += 1

    def afficher_channel(self, nom):
        # Affiche le contenu du channel sélectionné et son historique
        self.section_afficher_message.config(state='normal')
        self.section_afficher_message.delete(1.0, END)
        self.section_afficher_message.config(state='disabled')
        nom_channel = str(nom)[2:-3]
        self.channel = nom_channel
        commande = "select message from " + nom_channel
        cursor.execute(commande)
        for i in cursor:
            self.section_afficher_message.config(state='normal')
            self.section_afficher_message.insert('end', str(i)[2:-3] + "\n")
            self.section_afficher_message.yview('end')
            self.section_afficher_message.config(state='disabled')

    def creation_channel(self):
        commande1 = 'select max(port) from channel'
        cursor.execute(commande1)
        for port in cursor:
            port = str(port)[1:-2]
            port = int(port)
            port += 1
            # Ouvre une pop-up qui demande le nom du channel
        channel = askstring('Création de channel', 'Entrer le nom de votre channel')
        valeur = channel, port
        # Créer le channel avec le nom choisi
        commande2 = 'insert into channel (nom, port) values (%s,%s)'
        cursor.execute(commande2, valeur)
        admin.commit()
        # Créer une table pour l'historique des messages du channel créer
        commande3 = 'create table ' + channel + '(id int primary key auto_increment, message text not null)'
        cursor.execute(commande3)
        admin.commit()
        # Actualise la liste des channels
        self.afficher_bouton_serveur()
