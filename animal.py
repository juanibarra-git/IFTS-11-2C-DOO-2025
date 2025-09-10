from adc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        print("WOW WOW")


class Gato(Animal):
    def hablar(self):
        print("MIAU")