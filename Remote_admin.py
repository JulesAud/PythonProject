import os
from User import *


class Remote_admin(User):
    _is_remote_admin = ""

    def __init__(self, first_name, last_name, password, workspace, mail):
        User.__init__(first_name, last_name, password, workspace, mail)
        self._is_remote_admin = True

    def _set_is_remote_admin(self,remote_admin):
        self._is_remote_admin = remote_admin

    def random_char(self):
        return os.urandom(3)

    def create_user(self, first_name, last_name, workspace, mail, annuaire):
        user = User(first_name, last_name, self.random_char(), workspace, mail)
        if(user in annuaire):
            print("[Échec de Création] Impossible de créer l'utilisateur, ce dernier est déjà existant.")
        else:
            annuaire.add_person(user)
            print("Utilisateur créer et ajouter à l'annuaire")

