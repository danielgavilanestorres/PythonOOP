import mascota
class Ninja:
    def __init__(self, nombre, apellido, premio, comidaMascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premio = premio
        self.comidaMascota = comidaMascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self
    def alimentar(self):
        self.mascota.comer()
        return self
    def banar(self):
        self.mascota.sonidoM()

premioM = ["Galletas", "Pan"]
comidaM = ["Croquetas", "Pollo", "Leche"]

panchita = mascota.Mascota("Panchita", "Gato", ["Galleta", "Otro"], "Miua")
perroHerencia = mascota.MascotaHerencia("Suco", "Perro", ["Huesos", "Pan"], "Guuaa", "Pelota")

daniel = Ninja("Daniel", "Gavilanes", premioM, comidaM, panchita)

daniel.alimentar().caminar().banar()

xavier = Ninja("xavier", "Lopez", premioM, comidaM, perroHerencia)
xavier.mascota.juguetes()
