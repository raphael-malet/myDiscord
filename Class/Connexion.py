import mysql.connector
import hashlib
admin = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="mydiscord")
cursor = admin.cursor()
class Connexion:
    def __init__(self):
        pass

    def connexion(self, email, mdp):
            self.email = email
            self.mdp = mdp
            valide = True
            # Permet d'encoder les caractères spéciaux comme les accents et les symboles
            mdp_a_crypter = mdp.encode()
            # Définie le hachage en SHA-256
            hachage = hashlib.sha256(mdp_a_crypter)
            # Hache le mot de passe en hexadécimal
            mdp_digest = hachage.hexdigest()
            valeur = email,mdp_digest
            # Vérifie si le mail et mdp sont corrects pour connecter l'utilisateur
            commande ="select * from utilisateurs where mail=%s and mdp=%s"
            cursor.execute(commande, valeur)
            existe = cursor.fetchone()
            if existe is None:
                valide = False

            if valide:
                return True
            else:
                return False
