import random
import time
import os
class Caballo(object):
    def __init__(self, name):
        self.name = name
        self.posicion = 0

    def corre(self):
        p = random.randint(1, 5)
        self.posicion = self.posicion + p
    
    def dibuja(self):
        x = ("-" * self.posicion) + f"[{self.name}]"
        print(x)

pista = [Caballo("Yatasto"), Caballo("Pingo"), Caballo("Reina"), Caballo("Reina")]

termino = False
while not termino:
    i = 0
    os.system("cls")
    while i < len(pista):
        pista[i].corre()
        pista[i].dibuja()
        if pista[i].posicion > 100:
            termino = True
        i = i + 1
    time.sleep(0.5)



