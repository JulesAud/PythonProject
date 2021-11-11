class Site:
    """
    Créer un site avec son nom, la ville ou il est, et si il s'agit du siège
    """

    def __init__(self, nom, ville, isSiege):
        self.nom = nom
        self.localisation_ville = ville
        self.isSiege = isSiege

    def to_string(self):
        return f"[nom:{self.nom}; localisation:{self.localisation_ville}; siege:{self.siege}] "
