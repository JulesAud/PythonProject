import random
import string
import os

class Person:
    last_name = ""
    first_name = ""
    login = ""
    password = ""
    hash = ""
    localisation = ""

    def __init__(self, l_name, f_name, localisation):
        self.last_name = l_name.toLowerCase()  # nom de famille
        self.first_name = f_name.toLowerCase()  # prenom
        self.localisation = localisation
        self.login = self.first_name[0] + self.last_name

    def random_char(self):
        return os.urandom(5)

    def get_login(self):
        return self.login

    def set_password(self):
        self.password = self.random_char()

    def get_password(self):
        return self.password

    def set_hash(self):
        self.hash = self.get_password().hash()

    def get_hash(self):
        return self.hash

    # def to_string(self):
    #   return "The student is "+ self.ge
