import string
import random

from User import *


class Remote_admin(User):
    """
    Classe illustrant le remote admin(administrateur distant) qui possède différentes d'actions,
    seulement sur le site dans lequel il se trouve.
    """
    _is_remote_admin = ""

    def _random_char(self):
        """
        Méthode retournant un mot de passe temporaire créer aléatoirement
        :return: retourne une chaîne de caractère contenant le mot de passe de l'utilisateur
        """
        size=8
        chars=string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = ''.join(random.choice(chars) for _ in range(size))
        return password

    def __init__(self, first_name, last_name, workspace, mail):
        """
        Constructeur de la classe Remote admin permettant d'un instancier un objet de ce type
        :param first_name: prénom du remote admin
        :param last_name: nom du remote admin
        :param workspace: paramètre de type Site permettant de localiser le remote admin
        :param mail: mail du remote admin
        """
        User.__init__(self, first_name, last_name, self._random_char(), workspace, mail)
        self._is_remote_admin = True

    def _set_is_remote_admin(self,remote_admin):
        """
        Setter du boolean pour identifier le remote admin
        :param remote_admin: boolean identifiant le statut de l'admin
        :return: void
        """
        self._is_remote_admin = remote_admin

    def _create_user(self, first_name, last_name, workspace, mail, annuaire):
        """
        Méthode permettant de créer un utilisateur seulement du site du remote admin
        :param first_name: prénom du user
        :param last_name: nom du user
        :param workspace: paramètre de type Site localisant l'utilisateur
        :param mail: mail du user
        :param annuaire: paramètre de type Annuaire contenant toutes les informations de tous les users
        :return: void
        """
        if self.get_workspace() == workspace:
            user = User(first_name, last_name, self._random_char(), workspace, mail)
            if(annuaire.research_login(user.get_login())):
                print("[Échec de Création] Impossible de créer l'utilisateur, ce dernier est déjà existant.")
            else:
                annuaire.add_person(user)
                print("Utilisateur créer et ajouter à l'annuaire")

    def _delete_user(self, login, annuaire):
        """
        Méthode permettant de supprimer un user du même Site que le remote admin identifier par le login
        :param login: login du user à supprimer
        :param annuaire: paramètre de type Annuaire contenant toutes les informations de tous les users
        :return: void
        """
        if (not annuaire):
            print("Vous ne pouvez pas supprimer des utilisateurs d'un annuaire vide")
        else:
            if(annuaire.research_login(login)):
                person = annuaire.return_index_from_list("login", login)
                annuaire.List_Persons.pop(person)
                print("Utilisateur supprimé avec succès !")
            else:
                print("Utilisateur non existant dans l'annuaire")

    def _show_user_list(self, workspace, annuaire):
        """
        Méthode permettant de lister les users selon le site du remote admin
        :param workspace: paramètre de type Site localisant la liste des users à afficher
        :param annuaire: paramètre de type Annuaire contenant toutes les informations de tous les users
        :return: void
        """
        print(annuaire.research_person('site', workspace))