valor_a_sustituir = [1, 2, "hola","adios"]
string_a_cambiar = "HolA, amazon, papu"

for valor in string_a_cambiar:
    if valor == "a":
        string_a_cambiar = string_a_cambiar.replace(valor, "VACA")
    elif valor == "A":
        string_a_cambiar = string_a_cambiar.replace(valor, "VACA")


print(string_a_cambiar)