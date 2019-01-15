valor_a_sustituir = [1, 2, "hola","adios"]
string_a_cambiar = "Hola, numero {}, numero {}, {}, {}"

for valor in valor_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("{}", str(valor), 1)

print(string_a_cambiar)