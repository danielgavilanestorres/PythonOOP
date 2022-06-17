class personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fuerza = 0
        self.velocidad = 0
        self.salud = 0
    def mostrarEstado(self):
        print(f"Nombre: {self.nombre}, Fuerza: {self.fuerza}, Velocidad: {self.velocidad}, Salud: {self.salud}")