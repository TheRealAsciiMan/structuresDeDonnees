class EmptyStackError(Exception):
    def __init__(self, message="Erreur de pile vide"):
        self.message = message
        super().__init__(self.message)

class Stack():
    def __init__(self):
        self.pile = []
    def is_empty(self):
        return self.pile == []
    def pop(self):
        if self.pile:
            elem = self.pile[-1]
            self.pile = self.pile[:-1]
            return elem
        else:
            raise EmptyStackError("Erreur de pile vide")
    def push(self, elem):
        self.pile.append(float(elem))
        return self.pile
    def __str__(self):
        string = ""
        for elem in self.pile :
                string = f"║ {elem:05} ║\n" + string
        return string

def calcul(pile, ope):
    lst_operateurs = ["+", "-", "*", "/"]
    if ope in "+":
        i = 0
    if ope is "-":
        i = 1
    if ope is "*":
        i = 2
    if ope is "/":
        i = 3
    v1 = pile.pop()
    v2 = pile.pop()
    result = eval(f"{v2}+{lst_operateurs[i]}+{v1}")
    pile.push(result)
    return pile

def evaluation_lst(liste):
    pile = Stack()
    for elem in liste:
        if isinstance(elem, str):
            calcul(pile, elem)
        else:
            pile.push(elem)
    return pile.pop()

