from Clases.Leon import Leon
from Clases.Tigre import Tigre
from Clases.Oso import Oso
from Clases.Animal import Animal

class Zoo:
    def __init__(self, nombreZoo):
        self.nombreZoo = nombreZoo
        self.animales = []
    
    def agregarAnimal(self, animal):
        self.animales.append(animal)
        return self

    def imprimirInfoZoo(self):
        for animal in self.animales:
            animal.mostrarInfo()
        return self

zoo1 = Zoo("Sierra Bella")
zoo1.agregarAnimal(Leon("Leonidas",10)).agregarAnimal(Tigre("Tiger")).agregarAnimal(Oso("Baloo")).imprimirInfoZoo()

