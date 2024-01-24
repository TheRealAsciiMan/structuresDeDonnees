import doctest

class stack():
    def __init__(self):
        self._data = []
    def push(self, v):
        """\
        Ajoute l' élément v en haut de la pile
        Parameters
        ----------
        v : int ou float
        
        >>> s1 = stack()
        >>> s1.push(2)
        >>> s1.push(33)
        >>> s1.push(44.4)
        >>> s1.push(5.55)
        """
        if is_int(v):
            self._data.append(int(v))
        elif is_float(v):
            self._data.append(float(v))
        #print(self)
    def __repr__(self):
        chaine = ""
        for i in self._data :
            if is_float(i) :
                chaine = f"║ {i:05} ║\n" + chaine
            #chaine = f"║ {i} ║\n" + chaine
            else :
                chaine = chaine + "║  {i}  ║\n"
        return chaine
    def pop(self):
        """\
        Sort l' élément du haut de la pile
        Returns
        ----------
        elem : float
        
        >>> s1 = stack()
        >>> s1.push(2)
        >>> s1.pop()
        2
        """
        if self._data :
            elem = self._data[-1]
            self._data = self._data[:-1]
            return elem
        else :
            raise RuntimeError("Empty stack")
    def is_empty(self) -> bool :
        """\
        Teste si la pile est vide
        Returns
        -------
        bool
        
        >>> s1 = stack()
        >>> s1.push(2)
        >>> s1.is_empty()
        False
        >>> s1.pop()
        2
        >>> s1.is_empty()
        True
        """
        return self._data == []

def calcul(une_pile, une_operande):
    """\
    Retire les 2 derniers éléments de la pile
    et leur applique l' opérande. 
    Le résultat est ajouté en haut de la pile
    
    Parameters
    ----------
    une_pile : stack
    une_operande : str
    
    >>> s1 = stack()
    >>> s1.push(2)
    >>> s1.push(33)
    >>> calcul(s1, '+')
    >>> s1.pop()
    35
    
    """
    try :
        y = une_pile.pop()
        x = une_pile.pop()
        #print(f"x: {x} et y : {y}")
    except :
        raise  ValueError('Not enough operand')
    if une_operande=='+':
        une_pile.push(x+y)
    elif une_operande=='-':
        une_pile.push(x-y)
    elif une_operande=='*':
        une_pile.push(x*y)
    elif une_operande=='/':
        une_pile.push(x/y)
    else :
        une_pile.push(x)
        une_pile.push(y)
        raise ValueError('Bad operator')

def is_float(chaine):
    """\
    Teste si la chaine de caractère peut être convertie en nombre décimal
    
    Parameters
    ----------
    chaine : str
    
    Returns
    -------
    bool
    
    >>> is_float("5")
    True
    >>> is_float("7.2")
    True
    >>> is_float("8.0")
    True
    >>> is_float("*")
    False
    """
    try :
        res = float(chaine)
    except :
        return False
    else :
        return True

def is_int(chaine):
    """\
    Teste si la chaine de caractère peut être convertie en nombre entier
    
    Parameters
    ----------
    chaine : str
    
    Returns
    -------
    bool
    
    >>> is_int("5")
    True
    >>> is_int("7.2")
    False
    >>> is_int("8.0")
    True
    >>> is_int("*")
    False
    """
    try :
        dec = float(chaine)
        ent = int(dec)
    except :
        return False
    else :
        if dec == ent :
            return True
        else:
            return False

def evaluation_lst(une_liste):
    """\
    Ajoute les éléments numériques d' une liste dans une pile
    et effectue les opérations correspondants aux éléments non numériques
    
    Parameters
    ----------
    une_liste : list
    
    Returns
    -------
    res : float
    
    >>> evaluation_lst(['1', '2', '+', '4', '*'])
    12
    """
    s = stack()
    for i in une_liste :
        #print(f"i : {i}")
        if is_int(i) or is_float(i):
            s.push(i)
            #print(s)
        elif i in ['+', '-', '*', '/'] :
            calcul(s, i)
            #print(s)
        else :
            raise  ValueError('Bad operator')
    res = s.pop()
    if not s.is_empty():
        raise ValueError('Some element still remain in the stack')
    else :
        return res

def evaluation(une_chaine):
    """\
    Ajoute les éléments numériques d' une chaine de caractères dans une pile
    et effectue les opérations correspondants aux éléments non numériques
    
    Parameters
    ----------
    une_chaine : str
    
    Returns
    -------
    res : int ou float
    
    >>> evaluation("3 5 *")
    15
    >>> evaluation("3 5 * 2 +")
    17
    >>> evaluation("8 1 1 + /")
    4
    >>> evaluation("8 1 -")
    7
    >>> evaluation("4 2.5 *")
    10
    >>> evaluation("0.5 2 /")
    0.25
    >>> evaluation("1    1   +     ")
    2
    >>> evaluation("*")
    Traceback (most recent call last):
        ...
    ValueError: Not enough operand
    >>> evaluation("1 1 + +")
    Traceback (most recent call last):
        ...
    ValueError: Not enough operand
    >>> evaluation("2 1 + 3 2 -")
    Traceback (most recent call last):
        ...
    ValueError: Some element still remain in the stack
    >>> evaluation("15 4 %")
    Traceback (most recent call last):
        ...
    ValueError: Bad operator
    >>> evaluation("BONJOUR")
    Traceback (most recent call last):
        ...
    ValueError: Bad operator

    """
    #une_chaine = une_chaine.strip()
    ma_liste = une_chaine.split(" ")
    ma_liste2 = []
    for i in ma_liste :
        if i!='' :
            ma_liste2.append(i)
    return evaluation_lst(ma_liste2)

if __name__=='__main__':
    doctest.testmod()
