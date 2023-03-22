import mysql.connector
import hashlib

admin = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="mydiscord")
cursor = admin.cursor()


class Inscription:
    def __init__(self):
        pass

    def inscription(self, nom, prenom, email, mdp):
        try:
            self.nom = nom
            self.prenom = prenom
            self.mail = email
            self.mdp = mdp
            # Permet d'encoder les caractères spéciaux comme les accents et les symboles
            mdp_a_crypter = mdp.encode()
            # Définie le hachage en SHA-256
            hachage = hashlib.sha256(mdp_a_crypter)
            # Hache le mot de passe en hexadécimal
            mdp = hachage.hexdigest()
            valeur = nom, prenom, email, mdp
            commande = "insert into utilisateurs (nom,prenom,mail,mdp) values (%s,%s,%s,%s)"
            cursor.execute(commande, valeur)
            admin.commit()
            return True
        except:
            return False
