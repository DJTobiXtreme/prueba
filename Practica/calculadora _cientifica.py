operacion_elegida = input("Elige el tipo de operacion (SUMA/RESTA/MULTIPLICACION/DIVISION)").upper()

#falta hacer funcinar el while

operaciones = ["SUMA","RESTA","MULTIPLICACION","DIVISION"]

while operacion_elegida != "SUMA" or "RESTA" or "MULTIPLICACION" or "DIVISION":
    print("No has elegido ninguna operacion")
    input("Elige operacion")

if operacion_elegida == "SUMA":
    print("Elegiste {}".format(operacion_elegida))
    primer_numero = float(input("Elige el primer numero: "))
    segundo_numero = float(input("Elige el segundo numero: "))
    resultado = primer_numero + segundo_numero
    print("Tu resultado es {}".format(resultado))
elif operacion_elegida == "MULTIPLICACION":
    print("Elegiste {}".format(operacion_elegida))
    primer_numero = float(input("Elige el primer numero: "))
    segundo_numero = float(input("Elige el segundo numero: "))
    resultado = primer_numero * segundo_numero
    print("Tu resultado es {}".format(resultado))
elif operacion_elegida == "RESTA":
    print("Elegiste {}".format(operacion_elegida))
    primer_numero = float(input("Elige el primer numero: "))
    segundo_numero = float(input("Elige el segundo numero: "))
    resultado = primer_numero - segundo_numero
    print("Tu resultado es {}".format(resultado))
elif operacion_elegida == "DIVISION":
    print("Elegiste {}".format(operacion_elegida))
    primer_numero = float(input("Elige el primer numero: "))
    segundo_numero = float(input("Elige el segundo numero: "))
    resultado = primer_numero / segundo_numero
    print("Tu resultado es {}".format(resultado))
else:
    print("La operacion elegida no es valida")