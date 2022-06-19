from typing import List

def listaOrdenadaSeleccion(lista):
    inicio = 0
    while (inicio < len(lista)):
        min = lista[inicio]
        veces = 0
        for eMenor in range(inicio, len(lista)):
            if (min > lista[eMenor]):
                min = lista[eMenor]
                posicionMenor = eMenor
                veces += 1
        if veces >= 1:
            temp = lista[inicio]
            lista[inicio] = min
            lista[posicionMenor] = temp
        
        inicio += 1
    return lista


print(listaOrdenadaSeleccion([9, 2, 3, 5, 2, 0, 6]))
print(listaOrdenadaSeleccion([30, 8, 7, 40, 69, 5, 2]))
print(listaOrdenadaSeleccion([1, 2, 3]))
print(listaOrdenadaSeleccion([3, 2, 1]))

# 0 2 2 3 5 6 9
