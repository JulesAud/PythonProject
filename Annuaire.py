class Annuaire:
    """
    Créer un annuaire qui permet de sauvegarder une nouvelle personne
    et qui permet de faire une recherche sur toutes les personnes
    enregistrer dans l'annuaire en fonction d'un attribut.
    """
    List_Persons = []

    def __init__(self):
        pass

    def add_person(self, person):
        """Ajoute une personne à l'annuaire.
        :param person: Person
        """
        self.List_Persons.append(person)

    def research_login(self, login):
        """
        Recherhcer si un login existe déjà dans l'annuaire.
        :param login: valeur login à chercher
        :return: True si le login existe, False si non.
        """
        for p in self.List_Persons:
            if p.get_login() == login:
                return True
        else:
            return False

    def person_from_unique_attribute(self, attribut, valeur):
        """
        Recherche si un login ou un mail existe, si oui retourne la personne à qui celui-ci appartient.
        :param attribut: 'login' ou 'mail' -> attribut a chercher.
        :param valeur: la valeur de l'attribut que tu cherches.
        :return: retourne soit un objet Person si il a été trouvé, sinon retourne None.
        """
        if 'login' == attribut:
            for p in self.List_Persons:
                if p.get_login() == valeur:
                    return p
            else:
                return None
        elif 'mail' == attribut:
            for p in self.List_Persons:
                if p.get_mail() == valeur:
                    return p
            else:
                return None
        else:
            print("l'attibut n'existe pas ou n'est pas utilisé dans cette fonction. Les attributs disponibles sont 'login' et 'mail'")

    def research_person(self, attribut, valeur):
        """
        Rechercher parmis toutes les personnes de l'annuaire les personnes répondant aux critère
        mis dans 'attribut' et 'valeur'.
        :param attribut: String parmis (first_name, last_name, login, mail, site).
        :param valeur: String ou Site dans le cas où l'attribut est 'site'.
        :return: String avec une liste écrite des personnes répondant au critère ou un message
        donnant les différents attributs.
        """
        sortie = "Résultat:\n"
        if 'first_name' == attribut:
            for p in self.List_Persons:
                if p.first_name.startswith(valeur):
                    sortie += f"- Nom: {p.last_name}, Prénom: {p.first_name}, Login: {p.login}, Mail: {p.mail}, " \
                              f"Workspace: {p.workspace.nom}\n"
            return sortie
        elif 'last_name' == attribut:
            for p in self.List_Persons:
                if p.last_name.startswith(valeur):
                    sortie += f"- Nom: {p.last_name}, Prénom: {p.first_name}, Login: {p.login}, Mail: {p.mail}, " \
                              f"Workspace: {p.workspace.nom}\n"
            return sortie
        elif 'login' == attribut:
            for p in self.List_Persons:
                if p.login.startswith(valeur):
                    sortie += f"- Nom: {p.last_name}, Prénom: {p.first_name}, Login: {p.login}, Mail: {p.mail}, " \
                              f"Workspace: {p.workspace.nom}\n"
            return sortie
        elif 'mail' == attribut:
            for p in self.List_Persons:
                if p.mail.startswith(valeur):
                    sortie += f"- Nom: {p.last_name}, Prénom: {p.first_name}, Login: {p.login}, Mail: {p.mail}, " \
                              f"Workspace: {p.workspace.nom}\n"
            return sortie
        elif 'site' == attribut:
            for p in self.List_Persons:
                if p.workspace == valeur:
                    sortie += f"- Nom: {p.last_name}, Prénom: {p.first_name}, Login: {p.login}, Mail: {p.mail}, " \
                              f"Workspace: {p.workspace.nom}\n"
            return sortie
        else:
            return "L'attribut n'existe pas. Voici les attributs: (first_name, last_name, login, mail, site)."

    def to_string(self):
        sortie = ""
        for p in self.List_Persons:
            sortie += f"- Nom: {p.last_name}, Prénom: {p.first_name}, Login: {p.login}, Mail: {p.mail}, " \
                      f"Workspace: {p.workspace.nom}\n"
        return sortie
