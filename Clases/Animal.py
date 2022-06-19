class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = None
        self.salud = None
        self.felicidad = None
    
    def alimentar(self):
        self.salud += 10
        self.felicidad += 10
    
    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}, Salud: {self.salud}, Felicidad: {self.felicidad}")
        return self
    

