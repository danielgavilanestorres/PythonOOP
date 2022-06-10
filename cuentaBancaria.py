from lib2to3.pgen2.token import SLASHEQUAL
from typing_extensions import Self

class CuentaBancaria:
    def __init__(self, interes, saldo = 0):
        self.interes = interes / 100
        self.saldo = saldo
    def deposito(self, valorDeposito):
        self.saldo += valorDeposito
        return self
    def retiro(self, valorRetiro):
        if valorRetiro > self.saldo:
            print("Fondos Insuficientes: cobrando una tarifa de $5")
            self.saldo -= 5
        else:
            self.saldo -= valorRetiro
        return self
    def mostrarInfo(self):
        print("Balance: ", self.saldo)
    def generarInteres(self):
        if self.saldo > 0:
            self.interes = self.saldo * self.interes
            self.saldo += self.interes
        return self
    @classmethod
    def instanciasSaldo(cls, cuenta):
        cuenta.mostrarInfo()


cuenta1 = CuentaBancaria(3)
cuenta1.deposito(49).deposito(100).deposito(25).retiro(10).generarInteres().mostrarInfo()
CuentaBancaria.instanciasSaldo(cuenta1)

cuenta2 = CuentaBancaria(5, 100)
cuenta2.deposito(10).deposito(10).retiro(50).retiro(25).retiro(15).retiro(40).generarInteres().mostrarInfo()
CuentaBancaria.instanciasSaldo(cuenta2)


