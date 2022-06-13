class Mascota:
    def __init__(self, nombre, tipo, golosinas, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.sonido = sonido
        self.energia = 25
        self.salud = 25

    def dormir(self):
        self.energia += 25
        print("Durmiendo!! Energia: ", self.energia)
        return self
    def comer(self):
        self.energia += 5
        self.salud += 10
        print(f"Comiendo!! Energia: {self.energia} - Salud: {self.salud}")
        return self
    def jugar(self):
        self.salud += 5
        print("Jugando!!", self.salud)
        return self
    def sonidoM(self):
        print(self.sonido)
        return self

class MascotaHerencia(Mascota):
    def __init__(self, nombre, tipo, golosinas, sonido, juguete):
        super().__init__(nombre, tipo, golosinas, sonido)
        self.juguete = juguete
    def juguetes(self):
        print(self.juguete)

