class User:
    _login = ""
    _hash = ""
    _last_name = ""
    _first_name = ""
    _workspace = ""
    _mail = ""

    #########################
    def set_login(self, login):
        self._login = login

    def get_login(self):
        return self._login

    #########################
    def set_hash(self, password):
        self._hash = password.hash()

    def get_hash(self):
        return self._hash

    #########################
    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    #########################
    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    #########################
    def set_workspace(self, workspace):
        self._workspace = workspace

    def get_workspace(self):
        return self._workspace

    #########################
    def set_mail(self, mail):
        self._mail = mail

    def get_mail(self):
        return self._mail

    def __init__(self, first_name, last_name, password, workspace, mail):
        self.set_login(first_name[0].lower() + last_name.lower())
        self.set_hash(password)
        self._last_name = last_name  # nom de famille
        self._first_name = first_name  # prenom
        self._workspace = workspace
        self._mail = mail

    def to_string(self):
        return f"[login: {self._login}; last_name:{self._last_name}; first_name:{self._first_name}; workspace:{self._workspace.to_string()}; mail:{self._mail }]\n"