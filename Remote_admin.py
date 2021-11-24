import os
from User import *


class Remote_admin(User):
    _is_remote_admin = ""

    def __init__(self, first_name, last_name, password, workspace, mail):
        User.__init__(first_name, last_name, password, workspace, mail)
        self._is_remote_admin = True

    def _set_is_remote_admin(self,remote_admin):
        self._is_remote_admin = remote_admin

    def _random_char(self):
        password = os.urandom(3)
        print(password)
        return password

    def _create_user(self, first_name, last_name, workspace, mail, annuaire):
        if self.workspace == workspace:
            user = User(first_name, last_name, self.random_char(), workspace, mail)
            if(user in annuaire):
                print("[Échec de Création] Impossible de créer l'utilisateur, ce dernier est déjà existant.")
            else:
                annuaire.add_person(user.login)
                print("Utilisateur créer et ajouter à l'annuaire")

    def _delete_user(self, login, annuaire):
        if (not annuaire):
            print("Vous ne pouvez pas supprimer des utilisateurs d'un annuaire vide")
        else:
            if(login in annuaire):
                annuaire.pop(login)
                print("Utilisateur supprimé avec succès !")
            else:
                print("Utilisateur non existant dans l'annuaire")

    def _show_user_list(self, annuaire):
        for x in annuaire:
            print("User: "+ x)




