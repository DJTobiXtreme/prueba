def devuelve_pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares


print(devuelve_pares([1, 5, 3, 56, 77, 3]))

