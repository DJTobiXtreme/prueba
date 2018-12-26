lista_compras = []

indice_lista = 0

input_usuario = input("Que quieres agregar a la lista de compras? (escribe FIN para salir): ")

while input_usuario != "FIN":
    lista_compras.append(input_usuario)
    input_usuario = input("Que quieres agregar a la lista de compras? (escribe FIN para salir): ")

for item in lista_compras:
    print("Tengo que comprar {}".format(item))

if len(lista_compras) == 0:
    print("No escribiste nada")
else:
    print("Esta es tu mega lista")
