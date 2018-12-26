frase_usuario = input("Escribe una frase: ")

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

vocales_lista = []

for letra in frase_usuario:
    if letra in vocales:
        vocales_lista.append(letra)

print(vocales_lista)