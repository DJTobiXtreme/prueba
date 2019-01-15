string_a_cambiar = "Aurora boreal"
vocales = ["a", "e", "o", "u", "A", "E", "I" "O", "U"]
posicion_vocal = 1

for letra in string_a_cambiar:
    if letra in vocales:
        string_a_cambiar = string_a_cambiar.replace(letra, (str(posicion_vocal)), 1)
        posicion_vocal = int(posicion_vocal)
        posicion_vocal +=1

print(string_a_cambiar)
