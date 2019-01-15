numeros = [3, 2, 3, 5, 3, 15]

for indice in range(len(numeros)):
    if numeros[indice] % 3 == 0 and numeros[indice] % 5 == 0:
        numeros[indice] = "Bazinga"
    elif numeros[indice] % 3 != 0 and numeros[indice] % 5 != 0:
        None
    else:
        valor_a_sustituir = ""
        if numeros[indice] % 3 == 0:
            valor_a_sustituir += "Fizz"
        if numeros[indice] % 5 == 0:
            valor_a_sustituir += "Buzz"
        numeros[indice] = valor_a_sustituir

print(numeros)
