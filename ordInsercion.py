def ordInsercion(lista):
    for i in range (1, len(lista)):
        ver = (lista[i])
        for j in range (0, i):
            if lista[i] < lista[j]:
                temp = lista[j]
                lista[i] = temp
                lista[j] = ver
            ver = lista[i]
            
    return lista

print(ordInsercion([6, 5, 3, 1, 8, 7, 2, 4]))
print(ordInsercion([0, 7, 8, 5, 9, 10, 1, 4, 2]))
