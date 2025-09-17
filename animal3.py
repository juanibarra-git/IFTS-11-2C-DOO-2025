from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, velocidad):
        self.name = name
        self.posicion = 0
        self.velocidad = velocidad

    def caminar(self, tiempo):
        self.posicion = self.velocidad * tiempo


class Perro(Animal):
    def __init__(self, name):
        super().__init__(name, 2)

class Gato(Animal):
    def __init__(self, name):
        super().__init__(name, 1)

p = Perro("Victor")
g = Gato("Pedro")

p.caminar(10)
g.caminar(10)

print(p.posicion, g.posicion)