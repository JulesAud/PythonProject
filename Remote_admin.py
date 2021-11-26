import string
import random

from User import *


class Remote_admin(User):
    _is_remote_admin = ""

    def _random_char(self):
        size=8
        chars=string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = ''.join(random.choice(chars) for _ in range(size))
        return password

    def __init__(self, first_name, last_name, workspace, mail):
        User.__init__(self, first_name, last_name, self._random_char(), workspace, mail)
        self._is_remote_admin = True

    def _set_is_remote_admin(self,remote_admin):
        self._is_remote_admin = remote_admin

    def _create_user(self, first_name, last_name, workspace, mail, annuaire):
        if self.get_workspace() == workspace:
            user = User(first_name, last_name, self._random_char(), workspace, mail)
            if(annuaire.research_login(user.get_login())):
                print("[Échec de Création] Impossible de créer l'utilisateur, ce dernier est déjà existant.")
            else:
                annuaire.add_person(user.get_login())
                print("Utilisateur créer et ajouter à l'annuaire")

    def _delete_user(self, login, annuaire):
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
        print(annuaire.research_person('site', workspace))

    #def get_workspace(self):





