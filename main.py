import sys

from Remote_admin import Remote_admin
from Supreme_admin import *
from Site import *
from Annuaire import *

site_paris = Site("Centre de Paris", "Paris", True)
site_rennes = Site("Centre de Rennes", "Rennes", False)
site_strasbourg = Site("Centre de Strasbourg", "Strasbourg", False)
site_grenoble = Site("Centre de Grenoble", "Grenoble", False)


# annuaire = []

def home_page_user(user):
    print("Bonjour utilisateur : " + user.to_string())
    choix_home_page_user = int(input("Pour vous déconnecter saisissez 0"))

    while choix_home_page_user != 0:
        print("Cette action n'est pas supporté")
        choix_home_page_user = int(input("Pour vous déconnecter saisissez 0"))

    menu()


def home_page_remote_admin(user, annuaire):
    print("Bonjour remote admin : " + user.to_string())
    choix_home_page_remote_admin = int(input("Vos actions :\n" +
                                             "\t -Saisissez 0 pour afficher la liste des utilisateurs présent dans votre lieu de travail\n" +
                                             "\t -Saisissez 1 pour créer un utilisateur dans votre site\n"+
                                             "\t -Saisissez 2 pour effacer un utilisateur présent dans votre site\n"+
                                             "\t -Saisissez 3 pour vous déconnecter\n"+
                                             "Votre choix : "))

    while choix_home_page_remote_admin != 0 or choix_home_page_remote_admin != 1 or choix_home_page_remote_admin != 2 or choix_home_page_remote_admin != 3:
        print("Cette action n'est pas supportée")
        choix_home_page_remote_admin = int(input("Vos actions :\n" +
                                                 "\t -Saisissez 0 pour afficher la liste des utilisateurs présent dans votre lieu de travail\n" +
                                                 "\t -Saisissez 1 pour créer un utilisateur dans votre site\n" +
                                                 "\t -Saisissez 2 pour effacer un utilisateur présent dans votre site\n"
                                                 "\t -Saisissez 3 pour vous déconnecter\n"+
                                                 "Votre choix : "))

        if choix_home_page_remote_admin == 0:
            user._show_user_list(annuaire)

        elif choix_home_page_remote_admin == 1:
            inscription(user, annuaire)

        elif choix_home_page_remote_admin == 2:
            

        elif choix_home_page_remote_admin == 3:
            print("Au revoir et à bientôt...")
            menu()






def home_page_supreme_admin(user, annuaire):
    pass


def inscription(admin, annuaire):
    nom_de_famille = str(input("Saisissez le nom de famille: "))
    prenom = str(input("Saisissez le prénom: "))
    mail = str(input("Saisissez le mail: "))
    workspace = ""

    if isinstance(admin, Supreme_admin):
        site = str(input("Saisissez \"Paris\", \"Rennes\", \"Strasbourg\" ou \"Grenoble\" pour le lieu du site: "))
        if site.lower() == 'paris':
            workspace = site_paris

        elif site.lower() == 'rennes':
            workspace = site_rennes

        elif site.lower() == 'strasbourg':
            workspace = site_strasbourg

        elif site.lower() == 'grenoble':
            workspace = site_grenoble

        else:
            print("Le siège saisi n'est pas correct veuillez recommencez la saisi")
            pass

        admin.create_user(prenom, nom_de_famille, workspace, mail, annuaire)

    else:
        if isinstance(admin, Remote_admin):
            admin._create_user(prenom, nom_de_famille, admin.get_workspace(), mail, annuaire)
            print(annuaire)


def connexion(annuaire):
    login = str(input("Veuillez saisir votre login : "))
    password = str(input("Veuillez saisir votre mot de passe : "))

    if annuaire.research_login(login):
        user = annuaire.person_from_unique_attribute('login', login)
        hash = password.hash()

        if user.get_hash() == hash:
            print("Connexion réussi ! Bienvenue")

            if isinstance(user, User):
                home_page_user(user)

            elif isinstance(user, Remote_admin):
                home_page_remote_admin(user, annuaire)

            elif isinstance(user, Supreme_admin):
                home_page_supreme_admin(user, annuaire)

        else:
            print("Votre mot de passe contient une erreur veuillez réssayer !")

    else:
        print("Votre login est incorrect veuillez ressayer !")

    pass


def modification():
    pass


def suppression():
    pass


def menu():
    # Création des variables et des instances de départ afin de ne pas partir d'un annuaire vide est pouvoir tester
    supreme_admin = Supreme_admin()
    annuaire = Annuaire()

    choix = int(input(
        "Bienvenue chez Team_Net\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

    while choix != 2:
        if choix == 1:
            print("\nConnexion")
            print("-----------")
            connexion(annuaire)
        else:
            choix = int(input("\n- Bienvenue chez Team_Net\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le "
                              "système\nVotre choix: "))

    print("\nTeam_Net vous remercie pour votre visite.\nÀ bientôt")
    sys.exit()


menu()
