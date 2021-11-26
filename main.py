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
    choix_home_page_user = int(input("Pour vous déconnecter saisissez 0: "))

    while choix_home_page_user != 0:
        print("Cette action n'est pas supporté")
        choix_home_page_user = int(input("Pour vous déconnecter saisissez 0: "))

    menu(annuaire)


def home_page_remote_admin(user, annuaire):
    print("Bonjour remote admin : " + user.to_string())
    choix_home_page_remote_admin = int(input("Vos actions :\n" +
                                             "\t -Saisissez 0 pour afficher la liste des utilisateurs présent dans votre lieu de travail\n" +
                                             "\t -Saisissez 1 pour créer un utilisateur dans votre site\n" +
                                             "\t -Saisissez 2 pour effacer un utilisateur présent dans votre site\n" +
                                             "\t -Saisissez 3 pour vous déconnecter\n" +
                                             "Votre choix : "))

    while choix_home_page_remote_admin not in [0,1,2,3]:
        print("Cette action n'est pas supportée")
        choix_home_page_remote_admin = int(input("Vos actions :\n" +
                                                 "\t -Saisissez 0 pour afficher la liste des utilisateurs présent dans votre lieu de travail\n" +
                                                 "\t -Saisissez 1 pour créer un utilisateur dans votre site\n" +
                                                 "\t -Saisissez 2 pour effacer un utilisateur présent dans votre site\n"
                                                 "\t -Saisissez 3 pour vous déconnecter\n" +
                                                 "Votre choix : "))

    if choix_home_page_remote_admin == 0:
        print(annuaire.research_person('site', user.get_workspace()))

    elif choix_home_page_remote_admin == 1:
        inscription(user, annuaire)

    elif choix_home_page_remote_admin == 2:
        login = str(input("Veuillez renseigner le login de l'utilisateur que vous souhaitez supprimer : "))
        user._delete_user(login, annuaire)

    elif choix_home_page_remote_admin == 3:
        print("Au revoir et à bientôt...")
        menu(annuaire)
    home_page_remote_admin(user, annuaire)

def home_page_supreme_admin(user, annuaire):
    print("Bonjour supreme admin : " + user.to_string())
    choix_home_page_supreme_admin = int(input("Vos actions :\n" +
                                             "\t -Saisissez 0 pour afficher la liste de tous les utilisateurs\n" +
                                             "\t -Saisissez 1 pour créer un utilisateur dans un site\n" +
                                             "\t -Saisissez 2 pour effacer un utilisateur\n" +
                                             "\t -Saisissez 3 pour créer un remote admin\n" +
                                             "\t -Saisissez 4 pour supprimer un remote admin\n" +
                                             "\t -Saisissez 5 pour vous déconnecter\n" +
                                             "Votre choix : "))

    while choix_home_page_supreme_admin not in [0,1,2,3,4,5]:
        print("Cette action n'est pas supportée")
        choix_home_page_supreme_admin = int(input("Vos actions :\n" +
                                             "\t -Saisissez 0 pour afficher la liste de tous les utilisateurs\n" +
                                             "\t -Saisissez 1 pour créer un utilisateur dans un site\n" +
                                             "\t -Saisissez 2 pour effacer un utilisateur\n" +
                                             "\t -Saisissez 3 pour créer un remote admin\n" +
                                             "\t -Saisissez 4 pour supprimer un remote admin\n" +
                                             "\t -Saisissez 5 pour vous déconnecter\n" +
                                             "Votre choix : "))

    if choix_home_page_supreme_admin == 0:
        print(annuaire.to_string())

    elif choix_home_page_supreme_admin == 1:
        inscription(user, annuaire)

    elif choix_home_page_supreme_admin == 2:
        login = str(input("Veuillez renseigner le login de l'utilisateur que vous souhaitez supprimer : "))
        user._delete_user(login, annuaire)

    elif choix_home_page_supreme_admin == 3:
        inscription_remote_admin(user, annuaire)

    elif choix_home_page_supreme_admin == 4:
        login = str(input("Veuillez renseigner le login de l'utilisateur que vous souhaitez supprimer : "))
        user.delete_remote_admin(login, annuaire)

    elif choix_home_page_supreme_admin == 5:
        print("Au revoir et à bientôt...")
        menu(annuaire)
    home_page_supreme_admin(user, annuaire)

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
            print("Le siège saisi n'est pas correct veuillez recommencez la saisie")
            pass

        admin.create_user(prenom, nom_de_famille, workspace, mail, annuaire)

    else:
        if isinstance(admin, Remote_admin):
            admin._create_user(prenom, nom_de_famille, admin.get_workspace(), mail, annuaire)
            print(annuaire)


def inscription_remote_admin(admin, annuaire):
    nom_de_famille = str(input("Saisissez le nom de famille: "))
    prenom = str(input("Saisissez le prénom: "))
    mail = str(input("Saisissez le mail: "))
    workspace = ""

    site = str(input("Saisissez \"Paris\", \"Rennes\", \"Strasbourg\" ou \"Grenoble\" pour le lieu du site: "))
    if site.lower() == 'paris':
        workspace = site_paris

    elif site.lower() == 'rennes':
        workspace = site_rennes

    elif site.lower() == 'strasbourg':
        workspace = site_strasbourg

    elif site.lower() == 'grenoble':
        workspace = site_grenoble

    admin.create_remote_admin(prenom, nom_de_famille, workspace, mail, annuaire)
    print("Remote admin créé avec succès\n")


def connexion(annuaire):
    login = str(input("Veuillez saisir votre login : "))
    password = str(input("Veuillez saisir votre mot de passe : "))

    if annuaire.research_login(login):
        user = annuaire.person_from_unique_attribute('login', login)
        hash = sha256(password.encode("ascii")).hexdigest()

        if user.get_hash() == hash:
            print("Connexion réussi ! Bienvenue")

            if isinstance(user, Supreme_admin):
                home_page_supreme_admin(user, annuaire)

            elif isinstance(user, Remote_admin):
                home_page_remote_admin(user, annuaire)

            elif isinstance(user, User):
                home_page_user(user)

        else:
            print("Votre mot de passe contient une erreur veuillez réssayer !")

    else:
        print("Votre login est incorrect veuillez ressayer !")

    pass

def menu(annuaire):

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



################## MAIN ##########################
# Création des variables et des instances de départ afin de ne pas partir d'un annuaire vide est pouvoir tester
supreme_admin = Supreme_admin("admin", "supreme", site_paris, "toto")
annuaire = Annuaire()

annuaire.add_person(supreme_admin)
print(annuaire.to_string())

menu(annuaire)
