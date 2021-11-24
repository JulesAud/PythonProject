from hashlib import sha512
import getpass
from Person import Person


def inscription():
    fichier_csv = open("users.csv", "r")
    id = str(input("Saisissez votre id: "))
    mdp = getpass.getpass('Sasissez votre mdp: ')
    mdp_encode = mdp.encode()
    mdp_hash = sha512(mdp_encode).hexdigest()

    lesId = []
    lesMdp = []
    for i in fichier_csv:
        Id, Mdp = i.split(";")
        Mdp = Mdp.strip()
        lesId.append(Id)
        lesMdp.append(Mdp)
    lesDonnees = dict(zip(lesId, lesMdp))
    # print(lesDonnees)

    if id == "" or mdp == "":
        print("L'id ou le mdp est vide\n")
        y_n_inscription()

    elif id in lesId:
        print("Id existant\n")
        y_n_inscription()

    else:
        fichier_csv = open("users.csv", "a")
        fichier_csv.write(id + ";" + mdp_hash + "\n")
        print("Inscrit avec succes\nVous pouvez maintenant vous connecter\n")
        fichier_csv.close()
        print("Connexion")
        print("-----------")
        connexion()


def connexion():
    fichier_csv = open("users.csv", "r")
    id = str(input("Saisissez votre id: "))
    mdp = getpass.getpass('Sasissez votre mdp: ')
    mdp_encode = mdp.encode()
    mdp_hash = sha512(mdp_encode).hexdigest()

    if not len(id or mdp) < 1:
        lesId = []
        lesMdp = []
        for i in fichier_csv:
            Id, Mdp = i.split(";")
            Mdp = Mdp.strip()
            lesId.append(Id)
            lesMdp.append(Mdp)
        lesDonnees = dict(zip(lesId, lesMdp))

        try:
            if lesDonnees[id]:
                try:
                    if mdp_hash == lesDonnees[id]:
                        choix2 = int(input(
                            "Connexion réussi\nBonjour " + id + "\n\n- Saisir 0 pour modifier le mdp\n- Saisir 1 pour quitter le système\nVotre choix: "))

                        while choix2 < 0 or choix2 > 1:
                            choix2 = int(input(
                                "\n- Saisir 0 pour modifier le mdp\n- Saisir 1 pour quitter le système\nVotre choix: "))

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
    choix = int(input(
        "Bienvenu chez Team_Net\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

    while choix < 0 or choix > 2:
        choix = int(input(
            "\n- Saisir 0 pour s'inscrire\n- Saisir 1 pour se connecter\n- Saisir 2 pour quitter le système\nVotre choix: "))

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
    fichier_csv = open("users.csv", "r")
except:
    fichier_csv = open("users.csv", "w+")

menu()