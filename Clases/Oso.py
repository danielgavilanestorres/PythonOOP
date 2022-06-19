from Clases.Animal import Animal

class Oso(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.salud = 30
        self.felicidad = 30
    
    def alimentar(self):
        self.salud += 25
        self.felicidad += 25