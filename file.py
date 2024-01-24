class File:
    """
    Classe représentant une file ou une queue
    """
    def __init__(self):
        """
        Constructeur qui crée une liste correspondant aux données de la file
        """
        self.data = []

    def __repr__(self):
        """
        Méthode servant à représenter la file en parcourant ses éléments
        """
        chaine = ""
        for elem in self.data:
            chaine = f"| {elem:05} |\n" + chaine
        chaine += "\-------/\n"
        return chaine

    def ajout(self, value):
        """
        Permet d'ajouter une valeur à la file
        """
        self.data.append(value)

    def retire(self):
        """
        Permet de récupérer le premier élément de la liste et de le supprimer
        """
        if self.data:
            prem = self.data[0]
            self.data = self.data[1:]
            return prem

    def premier(self):
        """
        Permet de récupérer le premier élément de la liste et de le conserver
        """
        if self.data:
            return self.data[0]

    def file_vide(self):
        """
        Teste si la file est vide ou non
        """
        return self.data == []

    def taille(self):
        """
        Revoie la longueur de la liste
        """
        return len(self.data)