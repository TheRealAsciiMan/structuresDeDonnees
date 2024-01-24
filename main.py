class queue():
    def __init__(self):
        self._data = []

    def __repr__(self):
        chaine = ""
        for i in self._data:
            chaine = f"║ {i:05} ║\n" + chaine
            # chaine = f"║ {i} ║\n" + chaine
        chaine = chaine + "╚═══════╝\n"
        return chaine

    def ajout(self, v):
        """Ajoute un élément à la file
        >>> q = queue()
        >>> q.ajout(2)
        >>> q.ajout(33)
        >>> q.ajout(444)
        """
        self._data.append(v)

    def retire(self):
        """Retire un élément à la file
        >>> q = queue()
        >>> q.ajout(2)
        >>> q.ajout(33)
        >>> q.retire()
        2
        """
        if self._data:
            elem = self._data[0]
            self._data = self._data[1:]
            return elem

    def premier(self):
        """Récupère le 1er élément à la file
        >>> q = queue()
        >>> q.ajout(2)
        >>> q.ajout(33)
        >>> q.premier()
        2
        """
        if self._data:
            elem = self._data[0]
            return elem

    def file_vide(self):
        """Teste si la file est vide
        >>> q = queue()
        >>> q.file_vide()
        True
        >>> q.ajout(2)
        >>> q.file_vide()
        False
        """
        return self._data == []

    def taille(self):
        """Retourne la taille de la file
        >>> q = queue()
        >>> q.taille()
        0
        >>> q.ajout(2)
        >>> q.taille()
        1
        >>> q.ajout(33)
        >>> q.taille()
        2
        """
        return len(self._data)
