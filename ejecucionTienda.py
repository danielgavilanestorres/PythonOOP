from tienda import Tienda
from producto import Producto

tienda1 = Tienda("AlCosto")
producto1 = Producto(1, "Avena", 3.90, "Harina")
producto2 = Producto(2, "Aceite", 2.70, "Comestible")
producto3 = Producto(3, "Leche", 1.00, "Comestible")

producto2.actualizarPrecio(5, True)

tienda1.agregarProducto(producto1)
tienda1.agregarProducto(producto2)
tienda1.agregarProducto(producto3)
tienda1.verProductos()

tienda1.venderProducto(producto1.idPro)
tienda1.verProductos()

print(f"Inflacion Tienda: {tienda1.inflacionTienda()}")

tienda1.liquidacionTienda()
tienda1.verProductos()




