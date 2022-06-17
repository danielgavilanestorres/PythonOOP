from clases.personaje import personaje

class ninja(personaje):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.fuerza = 15
        self.velocidad = 5
        self.salud = 100
    
    def atacar(self, valorAtaque, pirata):
        pirata.salud -= valorAtaque
        print(f"Salud: {pirata.salud}")
