from hashlib import sha256
import hashlib


class User:
    """
    Classe permettant d'identifier un user
    """
    _login = ""
    _hash = ''
    _last_name = ""
    _first_name = ""
    _workspace = ""
    _mail = ""

    #########################
    def set_login(self, login):
        """
        Setter pour le login du user
        :param login: login du user
        :return: void
        """
        self._login = login

    def get_login(self):
        """
        Getter de l'attribut login permettant d'obtenir le login du user
        :return: login du user
        """
        return self._login

    #########################
    def set_hash(self, password):
        """
        Setter permettant de hash le mot de passe via sha256
        :param password: password sous format string
        :return: void
        """
        if not isinstance(password, bytes):
            password = password.encode("ascii")
            self._hash = sha256(password).hexdigest()

    def get_hash(self):
        """
        Getter du hash du user
        :return: hash du mot de passe du user
        """
        return self._hash

    #########################
    def set_last_name(self, last_name):
        """
        Setter du nom du user
        :param last_name: nom du user
        :return: void
        """
        self._last_name = last_name

    def get_last_name(self):
        """
        Getter du nom du user
        :return: nom du user
        """
        return self._last_name

    #########################
    def set_first_name(self, first_name):
        """
        Setter du prénom du user
        :param first_name: prénom du user
        :return: void
        """
        self._first_name = first_name

    def get_first_name(self):
        """
        Getter du prénom du user
        :return: prénom du user
        """
        return self._first_name

    #########################
    def set_workspace(self, workspace):
        """
        Setter du site du user
        :param workspace: paramètre de type Site localisant le user
        :return: void
        """
        self._workspace = workspace

    def get_workspace(self):
        """
        Getter du Site localisant le user
        :return: Site localisant le user
        """
        return self._workspace

    #########################
    def set_mail(self, mail):
        """
        Setter du mail du user
        :param mail: mail du user
        :return: void
        """
        self._mail = mail

    def get_mail(self):
        """
        Getter du mail du user
        :return: mail du user
        """
        return self._mail

    def __init__(self, first_name, last_name, password, workspace, mail):
        """
        Constructeur de la classe permettant d'instancier un objet du type User
        :param first_name: prénom du user
        :param last_name: nom du user
        :param password: mot de passe créer aléatoirement
        :param workspace: paramètre du type Site localisant le user
        :param mail: mail du user
        """
        print("Password is :" + str(password))
        self.set_login(first_name[0].lower() + last_name.lower())
        self.set_hash(password)
        self._last_name = last_name  # nom de famille
        self._first_name = first_name  # prenom
        self._workspace = workspace
        self._mail = mail

    def to_string(self):
        """
        Méthode retournant sous langue française les informations du user
        :return: return les informations des attributs sous forme de liste de mot.
        """
        return f"[login: {self._login}; last_name:{self._last_name}; first_name:{self._first_name}; workspace:{self._workspace.to_string()}; mail:{self._mail}; hash :{self.get_hash()}]\n"
