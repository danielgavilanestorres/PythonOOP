from operator import truediv

class Producto:
    
    def __init__(self, idPro, nombre, precio, categoria):
        self.idPro = idPro
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def printInfo(self):
        print(self)
        print(f"Producto: {self.nombre} - Categoría: {self.categoria} - Precio: {self.precio}")
    
    def actualizarPrecio(self, cambioPorcentaje, estaElevado):
        if estaElevado == True:
            self.precio = self.precio + (self.precio * (cambioPorcentaje/100))
        else:
            self.precio = self.precio - (self.precio * (cambioPorcentaje/100))
        return self.precio
    

