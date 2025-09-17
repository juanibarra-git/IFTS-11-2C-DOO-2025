from abc import ABC, abstractmethod

class Animal(Animal):
    def __init__(self, name):
        self.name = name
        self.posicion = 0

        @abstractmethod
        def caminar(self):
            pass

class Perro1(Animal):
    def __init__(self, name, velocidad):
        super().__init__(name)
        self.velocidad = velocidad

    def caminar(self):
        self.posicion = self.posicion + self.velocidad

class Perro2(Animal):

    def hablar(self):
        print("Hola")

    def caminar(self):
        self.posicion = self.posicion