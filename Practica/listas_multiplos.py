lista_usuario = [13, 1, 10, 70, 30, 50, 55, 13, 132312]
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []
resagados = []

for numero in lista_usuario:
    if numero % 3 == 0 or numero % 2 == 0 or numero % 5 == 0 or numero % 7 == 0:
        if numero % 2 == 0:
            multiplos_dos.append(str(numero))
        if numero % 3 == 0:
            multiplos_tres.append(str(numero))
        if numero % 5 == 0:
            multiplos_cinco.append(str(numero))
        if numero % 7 == 0:
            multiplos_siete.append(str(numero))
    else:
        resagados.append(str(numero))




print(multiplos_dos)
print(multiplos_tres)
print(multiplos_cinco)
print(multiplos_siete)
print(resagados)