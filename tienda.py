from ctypes.util import find_library


class Tienda:
    nombre = None

    def __init__(self, nombre):
        self.nombre = nombre
        self.producto = []
    
    def agregarProducto(self, nuevoProducto):
        self.producto.append(nuevoProducto)

    def venderProducto(self, idProducto):
        for pro in range(0, len(self.producto)):
            if self.producto[pro].idPro == idProducto:
                print(f"Producto Vendido: {self.producto[pro].nombre}")
                self.producto.remove(self.producto[pro])
                break
            else:
                print("Producto Inexistente")
    
    def inflacionTienda(self):
        sumaProductos = 0
        for pro in range(0, len(self.producto)):
            sumaProductos += self.producto[pro].precio
        return (sumaProductos / len(self.producto))
    
    def liquidacionTienda(self):
        print("LIQUIDACION DE TIENDA - Todos los Productos 10%")
        final = len(self.producto)
        inicio = 0
        while final > inicio:
            respuesta = input(f"Producto {self.producto[inicio].nombre} - (S/N): ")
            if respuesta == "S":
                print(f"Nuevo Precio: {self.producto[inicio].precio}")
                self.producto.remove(self.producto[inicio])
                final = len(self.producto)
                inicio = 0
            else:
                inicio += 1

    def verProductos(self):
        print("PRODUCTOS EXISTENTES")
        for pro in range(0, len(self.producto)):
            print(f"Producto: {self.producto[pro].nombre}, Precio: {self.producto[pro].precio}")
