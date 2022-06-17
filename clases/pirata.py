from clases.personaje import personaje

class pirata(personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.fuerza = 15
        self.velocidad = 3
        self.salud = 100
    
    def atacar(self, valorAtaque, ninja):
        ninja.salud -= valorAtaque
        print(f"Salud: {ninja.salud}")