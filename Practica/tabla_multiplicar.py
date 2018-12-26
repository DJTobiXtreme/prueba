numero_elegido = int(input("Que numero necesitas multiplicar: "))

for multiplo in range (10,0,-1):
    if multiplo % 1 == 0:
        print("{} x {} = {}".format(numero_elegido, multiplo, numero_elegido * multiplo))
