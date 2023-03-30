from tkinter import *
import tkinter as tk
from Class.Inscription import Inscription
from Class.Connexion import Connexion
from chat_page import Chat_page


class Main:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.geometry('600x700')
        self.fenetre.title('My Discord')
        self.fenetre.configure(bg='#000000')
        nom = StringVar()
        prenom = StringVar()
        email_connection = StringVar()
        email = StringVar()
        mdp = StringVar()
        mdp_connection = StringVar()
        self.text = StringVar()

        # Section inscription
        section_entrer = LabelFrame(self.fenetre, bg='BLAcK', text='Connexion', font=('', 25), fg='WHITE')
        section_entrer.pack(expand=1, ipady=10)

        self.section_confirmation = Label(section_entrer, fg='RED', bg='BLACK', text='')
        self.section_confirmation.grid()

        # Section email
        email_text = Label(section_entrer, text='Email', bg='BLACK', fg='WHITE', anchor=W, width=30)
        email_text.grid()
        email_entrer = Entry(section_entrer, bg='WHITE', fg='BLACK', width=30, textvariable=email_connection)
        email_entrer.grid()

        # Section mdp
        mdp_text = Label(section_entrer, text='Mot de passe', bg='BLACK', fg='WHITE', anchor=W, width=30)
        mdp_text.grid(pady=10)
        mdp_entrer = Entry(section_entrer, bg='WHITE', fg='BLACK', width=30, textvariable=mdp_connection, show='*')
        mdp_entrer.grid()

        # Section bouton de connexion
        bouton_connexion = Button(section_entrer, text='Connexion',
                                  command=lambda: self.login(email_connection.get(), mdp_connection.get()))
        bouton_connexion.grid(pady=10)

        # Section inscription
        section_entrer_2 = LabelFrame(self.fenetre, bg='BLACK', text='Inscription', font=('', 25), fg='WHITE')
        section_entrer_2.pack(expand=1, ipady=10)

        self.section_confirmation_inscription = Label(section_entrer_2, bg='BLACK', text='', fg='RED')
        self.section_confirmation_inscription.grid()

        # Section entrer nom
        nom_txt = Label(section_entrer_2, text='Nom', bg='BLACK', fg='WHITE', anchor=W, width=30)
        nom_txt.grid(pady=10)
        nom_entrer = Entry(section_entrer_2, bg='WHITE', fg='BLACK', width=30, textvariable=nom)
        nom_entrer.grid()
        # Section entrer prénom
        prenom_txt = Label(section_entrer_2, text='Prénom', bg='BLACK', fg='WHITE', anchor=W, width=30)
        prenom_txt.grid(pady=10)
        prenom_entrer = Entry(section_entrer_2, bg='WHITE', fg='BLACK', width=30, textvariable=prenom)
        prenom_entrer.grid()
        # Section entrer email
        email_txt = Label(section_entrer_2, text='Email', bg='BLACK', fg='WHITE', anchor=W, width=30)
        email_txt.grid(pady=10)
        email_entrer = Entry(section_entrer_2, bg='WHITE', fg='BLACK', width=30, textvariable=email)
        email_entrer.grid()
        # Section entrer mdp
        mdp_txt = Label(section_entrer_2, text='Mot de passe', bg='BLACK', fg='WHITE', anchor=W, width=30)
        mdp_txt.grid(pady=10)
        mdp_entrer = Entry(section_entrer_2, bg='WHITE', fg='BLACK', width=30, textvariable=mdp, show='*')
        mdp_entrer.grid()
        # Section bouton inscription
        inscription_bouton = Button(section_entrer_2, text='Inscription',
                                    command=lambda: self.register(nom_entrer.get(), prenom_entrer.get(),
                                                                  email_entrer.get(), mdp_entrer.get()))
        inscription_bouton.grid(pady=10)

        self.fenetre.mainloop()

    def login(self, email, mdp):
        if not Connexion.connexion(self, email, mdp):
            self.section_confirmation.config(text='Mot de passe ou Email incorrect')
        else:
            self.fenetre.destroy()
            Chat_page(email)

    def register(self, nom, prenom, email, mdp):
        # Vérifie si l'email est déjà utilisé
        if not Inscription.inscription(self, nom, prenom, email, mdp):
            self.section_confirmation_inscription.config(text='Email déjà utilisé', fg="RED")
            # Si l'email n'existe pas créer le compte
        else:
            self.section_confirmation_inscription.config(text='Votre compte a été crée', fg="GREEN")


Main()
