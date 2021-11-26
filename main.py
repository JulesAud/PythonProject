from Remote_admin import Remote_admin
from Site import *
from Person import *

site_paris = Site("Centre de Paris", "Paris", True)
site_rennes = Site("Centre de Rennes", "Rennes", False)
site_strasbourg = Site("Centre de Strasbourg", "Strasbourg", False)
site_grenoble = Site("Centre de Grenoble", "Grenoble", False)
#annuaire = []

def inscription(admin,annuaire):
    nom_de_famille = str(input("Saisissez votre nom de famille: "))
    prenom = str(input("Saisissez votre prenom: "))
    mail = str(input("Saisissez votre mail: "))
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

    if admin.isinstance(Remote_admin):
            admin._create_user(prenom,nom_de_famille,workspace,mail,annuaire)
    print(annuaire)

def connexion():
    pass

def modification():
    pass

def suppression():
    pass


def menu():
    choix = int(input(
        "Bienvenu chez Team_Net\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

    while choix < 0 or choix > 1:
        choix = int(input("\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\nVotre choix: "))

    if choix == 0:
        print("\nInscription")
        print("-----------")
        inscription()


    elif choix == 1:
        print("\nConnexion")
        print("-----------")
        # connexion()

    elif choix == 2:
        print("\nTeam_Net vous remerci pour votre visite\nA bientôt")

menu()