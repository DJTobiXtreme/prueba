
numero_inicial = 10

print(numero_inicial)
print("Par")
while numero_inicial > 1:
    numero_inicial -= 1
    print(numero_inicial)
    if numero_inicial / 2 is float(3):
        print("Par")
    else:
        print("Impar")
