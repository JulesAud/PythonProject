class Site:
    """
    Créer un site avec son nom, la ville ou il est, et si il s'agit du siège
    """

    def __init__(self, nom, ville, isSiege):
        self.nom = nom
        self.localisation_ville = ville
        self.siege = isSiege

    def get_name(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_ville(self):
        return self.localisation_ville

    def set_ville(self, ville):
        self.localisation_ville = ville

    def isSiege(self):
        return self.siege

    def set_isSiege(self, isSiege):
        self.siege = isSiege
