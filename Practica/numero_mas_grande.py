lista_numeros = [1, 55, 3, 2, 66666484]
numero_grande = lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_grande:
        numero_grande = numero


print(numero_grande)