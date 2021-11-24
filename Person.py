from User import *


class Person:
    __last_name = ""
    __first_name = ""
    __workspace = ""
    __mail = ""

    #########################
    def set_workspace(self, workspace):
        self.__workspace = workspace

    def get_workspace(self):
        return self.__workspace

    #########################
    def set_mail(self, mail):
        self.__mail = mail

    def get_mail(self):
        return self.__mail

    def __init__(self, l_name, f_name, workspace, mail):
        self.__last_name = l_name.lower()  # nom de famille
        self.__first_name = f_name.lower()  # prenom
        self.__workspace = workspace
        self.__mail = mail

    def to_string(self):
        return f"[last_name:{self.__last_name}; first_name:{self.__first_name}; workspace:{self.__workspace.to_string()}]"
