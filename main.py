"""
# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""

"""
from hashlib import sha512
import getpass
from Person import Person

def inscription():
    fichier_csv = open("users.csv","r")
    id = str(input("Saisissez votre id: "))
    mdp = getpass.getpass('Sasissez votre mdp: ')
    mdp_encode = mdp.encode()
    mdp_hash = sha512(mdp_encode).hexdigest()
    
    lesId = []
    lesMdp = []
    for i in fichier_csv:
        Id,Mdp = i.split(";")
        Mdp = Mdp.strip()
        lesId.append(Id)
        lesMdp.append(Mdp)
    lesDonnees = dict(zip(lesId,lesMdp))
    #print(lesDonnees)
    
    if id == "" or mdp == "":
        print("L'id ou le mdp est vide\n")
        y_n_inscription()
        
    elif id in lesId:
        print("Id existant\n")
        y_n_inscription()
        
    else:
        fichier_csv = open("users.csv","a")
        fichier_csv.write(id+";"+mdp_hash+"\n")
        print("Inscrit avec succes\nVous pouvez maintenant vous connecter\n")
        fichier_csv.close()
        print("Connexion")
        print("-----------")
        connexion()

def connexion():
    fichier_csv = open("users.csv","r")
    id = str(input("Saisissez votre id: "))
    mdp = getpass.getpass('Sasissez votre mdp: ')
    mdp_encode = mdp.encode()
    mdp_hash = sha512(mdp_encode).hexdigest()
    
    
    if not len(id or mdp)<1:
        lesId = []
        lesMdp = []
        for i in fichier_csv:
            Id,Mdp = i.split(";")
            Mdp = Mdp.strip()
            lesId.append(Id)
            lesMdp.append(Mdp)
        lesDonnees = dict(zip(lesId,lesMdp))
        
        try:
            if lesDonnees[id]:
                try:
                    if mdp_hash == lesDonnees[id]:
                        choix2 = int(input("Connexion réussi\nBonjour "+id+"\n\n- Saisir 0 pour modifier le mdp\n- Saisir 1 pour quitter le système\nVotre choix: "))
                        
                        while choix2<0 or choix2>1:
                            choix2 = int(input("\n- Saisir 0 pour modifier le mdp\n- Saisir 1 pour quitter le système\nVotre choix: "))

                        if choix2 == 0:
                            print("Choix 0")

                        elif choix2 == 1:
                            print("\nTeam_Net vous remerci pour votre visite\nA bientôt")
                    
                    else:
                        print("L'id ou le mdp est incorrect")
                        y_n_connexion()
                        
                except:
                    print("L'd ou le mdp est incorrect")
                    y_n_connexion()
            else:
                print("L'id n'existe pas dans nos registre\nVeuillez vous inscrire d'abord")
                y_n_connexion()
        except:
            print("L'id n'existe pas dans nos registre\nVeuillez vous inscrire d'abord")
            y_n_connexion()
    
    else:
        print("Les champs sont vides")
        y_n_connexion()

def menu():
    choix = int(input("Bienvenu chez Team_Net\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

    while choix<0 or choix>2:
        choix = int(input("\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

    if choix == 0:
        print("\nInscription")
        print("-----------")
        inscription()


    elif choix == 1:
        print("\nConnexion")
        print("-----------")
        connexion()
        
    elif choix == 2:
        print("\nTeam_Net vous remerci pour votre visite\nA bientôt")
        

def y_n_connexion():
    y_n = str(input("\n\n- Saisir y pour réessayer\n- Saisir n pour affichier le menu\nVotre choix: "))
    if y_n == 'y':
        print("\n")
        connexion()
        print("\n")

    elif y_n == 'n':
        print("\n")
        menu()
        print("\n")
        


def y_n_inscription():
    y_n = str(input("\n\n- Saisir y pour réessayer\n- Saisir n pour affichier le menu\nVotre choix: "))
    if y_n == 'y':
        print("\n")
        inscription()
        print("\n")

    elif y_n == 'n':
        print("\n")
        menu()
        print("\n")                    


try:
    fichier_csv = open("users.csv","r")
except:
    fichier_csv = open("users.csv","w+")


menu()"""

from Site import *
from Person import *

#site_rennes = Site("Centre de Rennes", "Rennes", False)
#site_strasbourg = Site("Centre de Strasbourg", "Strasbourg", False)
#site_grenoble = Site("Centre de Grenoble", "Grenoble", False)
'''site_paris = Site("Centre de Paris", "Paris", True)

nom_de_famille = input("Saisissez votre nom de famille: ")
prenom = input("Saisissez votre prenom: ")
workspace = site_paris

creation_personne = Person(nom_de_famille, prenom, workspace)
print(personne.to_string())'''





def menu():
    choix = int(input("Bienvenu chez Team_Net\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

    while choix<0 or choix>1:
        choix = int(input("\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\nVotre choix: "))

    if choix == 0:
        print("\nInscription")
        print("-----------")
        inscription()


    elif choix == 1:
        print("\nConnexion")
        print("-----------")
        connexion()
        
    elif choix == 2:
        print("\nTeam_Net vous remerci pour votre visite\nA bientôt")
        
        
        
        
def inscription():
  

    nom_de_famille = str(input("Saisissez votre nom de famille: "))
    prenom = str(input("Saisissez votre prenom: "))
    site = str(input("Saisissez p(paris), r(rennes), s(strasbourg), g(grenoble) pour le lieu du site: "))
    if site == 'p':
        workspace = site_paris
        
    elif site == 'r':
        workspace = site_rennes
    
    elif site == 's':
        workspace = site_strasbourg
        
    elif site == 'g':
        workspace = site_grenoble
        
    else:
        print("Vous n'avaez pas sisi la bonne lettre")

    creation_personne = Person(nom_de_famille, prenom, workspace)
    
    fichier_csv = open("users.csv","a")
    fichier_csv.write(creation_personne.to_string()+"\n")
    print("Inscrit avec succes")
    fichier_csv.close()
    



try:
    fichier_csv = open("users.csv","r")
except:
    fichier_csv = open("users.csv","w+")

menu()


site_paris = Site("Centre de Paris", "Paris", True)
site_rennes = Site("Centre de Rennes", "Rennes", False)
site_strasbourg = Site("Centre de Strasbourg", "Strasbourg", False)
site_grenoble = Site("Centre de Grenoble", "Grenoble", False)