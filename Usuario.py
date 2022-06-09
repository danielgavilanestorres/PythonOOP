from typing_extensions import Self

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.saldoCuenta = 0
    def hacerDeposito(self, valorDeposito):
        self.saldoCuenta += valorDeposito
    def hacerRetiro(self, valorRetiro):
        self.saldoCuenta -= valorRetiro
    def mostrarBalance(self):
        usuario = self.nombre
        total = self.saldoCuenta
        print(f"El Usuario {usuario}, Balance: ${self.saldoCuenta}")
    def trasnferirDinero(self, Usuario, valor):
        self.saldoCuenta -= valor
        Usuario.saldoCuenta += valor

daniel = Usuario("Daniel", "danielgavilanestorres@gmail.com")
patricia = Usuario("Patricia", "patty@gmail.com")
angeles = Usuario("Angeles", "angeles@gmail.com")

daniel.hacerDeposito(100)
daniel.hacerDeposito(150.25)
daniel.hacerDeposito(25)
daniel.hacerRetiro(75.60)
daniel.mostrarBalance()
print("\n")

patricia.hacerDeposito(500)
patricia.hacerDeposito(150)
patricia.hacerRetiro(30)
patricia.hacerRetiro(24.60)
patricia.mostrarBalance()
print("\n")

angeles.hacerRetiro(1000.58)
angeles.hacerRetiro(254.90)
angeles.hacerRetiro(125.89)
angeles.hacerRetiro(89.74)
angeles.mostrarBalance()

print("\n")
daniel.trasnferirDinero(patricia, 50)
daniel.mostrarBalance()
patricia.mostrarBalance()