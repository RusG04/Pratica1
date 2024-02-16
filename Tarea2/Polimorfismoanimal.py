from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print ("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

perro1 = Perro()
gato2 = Gato()

print("El perro hace") ,perro1.hacer_sonido()
print("El gato hace") ,gato2.hacer_sonido()

