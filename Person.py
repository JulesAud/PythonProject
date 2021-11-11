import os

class Person:
    last_name = ""
    first_name = ""
    login = ""
    hash = ""
    workspace = ""
    mail = ""

    def random_char(self):
        return os.urandom(3)

    #########################
    def set_login(self, login):
        self.login = login

    def get_login(self):
        return self.login

    #########################
    def set_hash(self, password):
        self.hash = password.hash()

    def get_hash(self):
        return self.hash

    #########################
    def set_workspace(self, workspace):
        self.workspace = workspace

    def get_workspace(self):
        return self.workspace

    #########################                
    def set_mail(self, mail):
        self.mail = mail

    def get_mail(self):
        return self.mail

    def __init__(self, l_name, f_name, workspace):
        self.last_name = l_name#.toLowerCase()  # nom de famille
        self.first_name = f_name#.toLowerCase()  # prenom
        self.workspace = workspace
        self.login = self.first_name[0] + self.last_name
        self.hash = self.get_hash()
        self.mail = None

    def to_string(self):
        return f"[last_name:{self.last_name}; first_name:{self.first_name}; login:{self.login}; workspace:{self.workspace.to_string()}]"
