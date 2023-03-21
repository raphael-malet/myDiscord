import tkinter as tk
from tkinter import *
import mysql.connector

admin = mysql.connector.connect(host="localhost", user="root", password="vatefaireencule", database="mydiscord")
cursor = admin.cursor()

class Chat_page:

    def __init__(self, email):
        self.email = email
        fenetre = tk.Tk()
        fenetre.geometry('600x700')
        fenetre.title('My Discord')
        fenetre.configure(bg='#000000')

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

        section_entrer_chat = Frame(section_droite)
        section_entrer_chat.configure(bg='GREY', width=500, height=100)
        section_entrer_chat.pack(side=BOTTOM, fill=X)

        section_texte_chat = Entry(section_entrer_chat, bg='WHITE', width=40, fg='BLACK')
        section_texte_chat.grid()

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



Chat_page('abab')
