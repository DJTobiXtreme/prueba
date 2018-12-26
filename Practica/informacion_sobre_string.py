frase_usuario = input("Escribe una frase: ")

n_espacios = 0
n_puntos = 0
n_comas = 0

for caracter in frase_usuario:
    if caracter is " ":
        n_espacios += 1
    elif caracter is ".":
        n_puntos += 1
    elif caracter is ",":
        n_comas += 1

print("Espacios: {}".format(n_espacios))
print("Puntos: {}".format(n_espacios))
print("Comas: {}".format(n_espacios))