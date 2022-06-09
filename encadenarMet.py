from typing_extensions import Self

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.saldoCuenta = 0
    def hacerDeposito(self, valorDeposito):
        self.saldoCuenta += valorDeposito
        return self
    def hacerRetiro(self, valorRetiro):
        self.saldoCuenta -= valorRetiro
        return self
    def mostrarBalance(self):
        usuario = self.nombre
        total = self.saldoCuenta
        print(f"El Usuario {usuario}, Balance: ${self.saldoCuenta}")
        return self
    def trasnferirDinero(self, Usuario, valor):
        self.saldoCuenta -= valor
        Usuario.saldoCuenta += valor
        return self

daniel = Usuario("Daniel", "danielgavilanestorres@gmail.com")
patricia = Usuario("Patricia", "patty@gmail.com")
angeles = Usuario("Angeles", "angeles@gmail.com")

daniel.hacerDeposito(100).hacerDeposito(150.25).hacerDeposito(25).hacerRetiro(75.60).mostrarBalance()
print("\n")

patricia.hacerDeposito(500).hacerDeposito(150).hacerRetiro(30).hacerRetiro(24.60).mostrarBalance()
print("\n")

angeles.hacerRetiro(1000.58).hacerRetiro(254.90).hacerRetiro(125.89).hacerRetiro(89.74).mostrarBalance()

print("\n")
daniel.trasnferirDinero(patricia, 50).mostrarBalance()
patricia.mostrarBalance()