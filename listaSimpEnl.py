# Primer Elemento: Nodo
from typing import List

class Nodo:
    def __init__(self, valorNodo):
        self.valorNodo = valorNodo
        self.siguiente = None

# Segundo Elemento: Lista
class Lista:
    def __init__(self):
        self.cabeza = None
    
    def agNodoInicio(self, valorNodoLista):
        nuevoNodo = Nodo(valorNodoLista)
        cabezaActual = self.cabeza
        nuevoNodo.siguiente = cabezaActual
        self.cabeza = nuevoNodo
        return self

    def agNodoFinal(self, valorNodoLista):
        if (self.cabeza == None):
            self.agNodoInicio(valorNodoLista)
            return self
        nuevoNodo = Nodo(valorNodoLista)
        puntero = self.cabeza
        while (puntero.siguiente != None):
            puntero = puntero.siguiente
        puntero.siguiente = nuevoNodo
        return self

    def imprimirLista(self):
        puntero = self.cabeza
        while (puntero != None):
            print(puntero.valorNodo)
            puntero = puntero.siguiente
        return self


miLista = Lista()
miLista.agNodoInicio("son").agNodoInicio("las listas").agNodoFinal("Excelentes").imprimirLista()

