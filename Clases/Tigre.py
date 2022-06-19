from Clases.Animal import Animal

class Tigre(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.salud = 25
        self.felicidad = 25
    
    def alimentar(self):
        self.salud += 5
        self.felicidad += 5
