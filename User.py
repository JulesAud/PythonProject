from Person import *
from Person import Person


class User:
    login = ""
    hash = ""

    def set_login(self, login):
        self.login = login

    def get_login(self):
        return self.login

    def set_hash(self, password):
        self.hash = password.hash()

    def get_hash(self):
        return self.hash

    def __init__(self, first_name, last_name, password, workspace, mail):
        self.set_login(first_name[0] + last_name)
        self.set_hash(password)
        person = Person(last_name, first_name, workspace, mail)