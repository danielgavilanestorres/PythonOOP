class jugador:

    def __init__(self):
        raise RuntimeError
    
    @classmethod
    def jugadorNinja(cls, nombre, edad, genero, ninja):
        jugador = cls.__new__(cls)
        jugador.nombre = nombre
        jugador.edad = edad
        jugador.genero = genero
        jugador.ninjas = ninja
        return jugador

    @classmethod
    def jugadorPirata(cls, nombre, edad, genero, pirata):
        jugador = cls.__new__(cls)
        jugador.nombre = nombre
        jugador.edad = edad
        jugador.genero = genero
        jugador.piratas = pirata
        return jugador

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}\n Edad: {self.edad}\n Genero: {self.genero}\n ")
    
