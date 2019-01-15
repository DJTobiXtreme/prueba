dic_colores = {"amarillo": "yellow", "rojo": "red", "azul": "blue", "verde": "green"}
salir = True

while salir == True:
    color = input("Que numero quieres traducir? F/finalizar: ")
    if color in dic_colores:
        print(dic_colores[color])
    elif color == "F":
        salir = False

print("Has finalizado")