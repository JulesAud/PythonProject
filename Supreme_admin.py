from Remote_admin import *


class Supreme_admin(Remote_admin):
    """
    Classe instanciant le supreme administrateur qui possède tous les droits sur le logiciel.
    Différentes méthodes de création et de suppression sont à sa portée. Il hérite directement de remote admin,
    il possède donc les mêmes actions que ce dernier et d'autres en plus
    """

    __is_supreme_admin = ""

    # boolean qui permet de connaitre le statut du supreme admin

    def __init__(self, first_name, last_name, workplace, mail):
        """
        Constructeur de la classe Supreme admin qui va instancier un nouvel objet de ce type.
        Nous faisons appel au constructeur de la classe mère afin de créer l'objet
        :param first_name: prénom du supreme admin qui peut correspondre à n'importe quoi
        :param last_name: nom du supreme admin qui peut correspondre lui aussi à n'importe quoi.
        :param workplace: paramètre de type Site il permet de localiser le user en question selon son site
        :param mail: mail du user
        """

        Remote_admin.__init__(self, first_name, last_name, workplace, mail)
        self.__is_supreme_admin = True
        print(" User created : " + self.to_string())

    def create_user(self, first_name, last_name, workspace, mail, annuaire):
        """
        Méthode permettant de créer un nouvel user (sans rôle particulier ex: un salarié) peut importe son site.
        Ne retourne rien par défaut.
        :param first_name: prénom du user en question à créer
        :param last_name: nom du user à créer
        :param workspace: paramètre de type Site précisant le site de l'utilisateur
        :param mail: paramètre précisant le mail de l'utilisateur
        :param annuaire: annuaire du type Annuaire contenant toutes les informations
        :return: void
        """
        user = User(first_name, last_name, self._random_char(), workspace, mail)
        if annuaire.research_login(user.get_login()):
            print("[Échec de Création] Impossible de créer l'utilisateur, ce dernier est déjà existant.")
        else:
            annuaire.add_person(user)
            print("Utilisateur créer et ajouter à l'annuaire.")

    def create_remote_admin(self, first_name, last_name, workspace, mail, annuaire):
        """
        Méthode permettant de créer un remote admin pouvant être créer seulement via le supreme admin
        :param first_name: prénom du remote admin
        :param last_name: nom du remote admin
        :param workspace: paramètre de type Site du remote admin
        :param mail: mail du remote admin
        :param annuaire: annuaire du type Annuaire contenant toutes les informations
        :return: void
        """
        password = self._random_char()
        remote_admin = Remote_admin(first_name, last_name, workspace, mail)
        print(f"login : {remote_admin.get_login()}, password : {password}")
        if annuaire.research_login(remote_admin.get_login()):
            print("Impossible de créer le remote admin, ce dernier est déjà existant dans l'annuaire.")
        else:
            annuaire.add_person(remote_admin)
            print("Remote admin créer avec succès.")

    def delete_remote_admin(self, login, annuaire):
        """
        Méthode de suppression du remote admin. Cette méthode permet de supprimer un remote admin. Identifié par son login.
        :param login: login du remote admoin à supprimer
        :param annuaire: annuaire du type Annuaire contenant toutes les informations
        :return: void
        """
        if annuaire:
            if annuaire.research_login(login):
                count = annuaire.return_index_from_list('login', login)
                annuaire.List_Persons.pop(count)
                print("Utilisateur supprimé avec succès !")
            else:
                print("Utilisateur non existant dans l'annuaire")
        else:
            print("Erreur l'annuaire est vide")

    def set_is_supreme_admin(self, supreme_admin):
        """
        Setter de l'attribut is_supreme_admin
        :param supreme_admin: boolean de set
        :return: void
        """
        self.__is_supreme_admin = supreme_admin
