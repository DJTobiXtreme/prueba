lista_mixta = [12312, "Hello", "ITS ME", 123123, "ATR PAPU"]
lista_enteros = []
lista_strings = []

for elemento in lista_mixta:
    if type(elemento) is not str:
        lista_enteros.append(elemento)
    else:
        lista_strings.append(elemento)

print("La lista de enteros es {}".format(lista_enteros))
print("La lista de strings es {}".format(lista_strings))
