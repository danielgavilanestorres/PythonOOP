from Clases.Animal import Animal

class Leon(Animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre)
        self.peso = peso
        self.salud = 20
        self.felicidad = 20
    
    def alimentar(self):
        self.salud += 15
        self.felicidad += 20
        return self
