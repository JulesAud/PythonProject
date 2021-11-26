class Site:
    """
    Créer un site avec son nom, la ville ou il est, et si il s'agit du siège
    """

    def __init__(self, nom, ville, isSiege):
        """
        Constructeur de la classe Site
        :param nom: nom du siège (ex: Centre de Paris)
        :param ville: nom de la ville du site
        :param isSiege: boolean permettant d'identifier le siège qui est à true pour Paris
        """
        self.nom = nom
        self.localisation_ville = ville
        self.isSiege = isSiege

    def to_string(self):
        """
        Méthode
        :return: Return la version chaîne de caractère et linguistique de l'objet.
        """
        return f"[nom:{self.nom}; localisation:{self.localisation_ville}; siege:{self.isSiege}] "
