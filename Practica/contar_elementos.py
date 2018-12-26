
lista_usuario = []

numero_agregar = ""
largo_lista = 0


while numero_agregar != "FIN":
    numero_agregar = input("Que numeros quieres agregar a la lista, FIN para terminar: ")
    if numero_agregar.isdigit():
        lista_usuario.append(int(numero_agregar))
        largo_lista += 1
        print("Numero agregado")

if largo_lista > 0:
    print(lista_usuario)

print("El largo de la lista es {}".format(largo_lista))