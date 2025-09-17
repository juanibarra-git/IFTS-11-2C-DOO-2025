import random

class Caballo(object):
    def __init__(self, name):
        self.name = name
        self.posicion = 0


    def corre(self):
        random.randit(1, 5)
        self.posicion = self.posicion + p
    
    def dibuja(self):
        x = (" " * self.posicion) + f"[{self.name}]"
        print(x)



