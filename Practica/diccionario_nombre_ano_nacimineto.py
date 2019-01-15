agenda = dict()


salir = False

while salir == False:
    entrada = input("Que quieres hacer? A/Agregar, C/Consultar y S/Finalizar: ")
    if entrada == "A":
        nombre = input("Nombre: ")
        ano = input("Ano de nacimiento: ")
        agenda[nombre] = ano
    elif entrada == "C":
        nombre = input("Que persona deseas buscar: ")
        print("Ano de nacimiento de {}: {}".format(nombre, agenda[nombre]))
    elif entrada == "S":
        salir = True

print("Has finalizado")