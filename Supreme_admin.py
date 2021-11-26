from Remote_admin import *


class Supreme_admin(Remote_admin):
    __is_supreme_admin = ""

    def __init__(self,first_name, last_name, password, workplace, mail):
        user = User(first_name, last_name, password, workplace, mail)
        Remote_admin.__init__(self, first_name, last_name, password, workplace, mail)
        self.__is_supreme_admin = True

    def create_user(self, first_name, last_name, workspace, mail, annuaire):
        user = User(first_name, last_name, self._random_char(), workspace, mail)
        if annuaire.research_login(user.login):
            print("[Échec de Création] Impossible de créer l'utilisateur, ce dernier est déjà existant.")
        else:
            annuaire.add_person(user.login)
            print("Utilisateur créer et ajouter à l'annuaire.")

    def create_remote_admin(self, first_name, last_name, workspace, mail, annuaire):
        password = self._random_char()
        remote_admin = Remote_admin(first_name, last_name, password, workspace, mail)
        print(f"login : {remote_admin.get_login()}, password : {password}")
        if annuaire.research_login(remote_admin.get_login()):
            print("Impossible de créer le remote admin, ce dernier est déjà existant dans l'annuaire.")
        else:
            annuaire.add_person(remote_admin)
            print("Remote admin créer avec succès.")

    def delete_remote_admin(self, login, annuaire):
        if annuaire:
            if annuaire.research_login(login):
                person = annuaire.person_from_unique_attribute('login', login)
                annuaire.pop(person)
                print("Utilisateur supprimé avec succès !")
            else:
                print("Utilisateur non existant dans l'annuaire")
        else:
            print("Erreur l'annuaire est vide")

    def set_is_supreme_admin(self,supreme_admin):
        self.__is_supreme_admin = supreme_admin




