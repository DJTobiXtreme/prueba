lista_usuario = []
numero_agregado = ""
suma_numeros = 0
cantidad_numeros = 0

while numero_agregado != "FIN":
    numero_agregado = input("Que numero quieres en tu lista: ")
    if numero_agregado.isdigit():
        lista_usuario.append(int(numero_agregado))
        suma_numeros += int(numero_agregado)
        cantidad_numeros += 1
        print("Numero agregado")

print(lista_usuario)

print("La media es de {}".format(suma_numeros / cantidad_numeros))