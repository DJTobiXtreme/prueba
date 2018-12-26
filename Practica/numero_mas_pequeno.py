numeros_usuario = []
numero_elegido = ""

while len(numeros_usuario) < 10 :
    while not numero_elegido.isdigit():
        numero_elegido = input("Dime un numero: ")
    numeros_usuario.append(int(numero_elegido))
    numero_elegido = ""
    print("Numero anadido!")

print(numeros_usuario)

numero_grande = numeros_usuario [0]

for numero in numeros_usuario :
    if numero < numero_grande:
        numero_grande = numero

print("El numero mas pequeno es {}".format(numero_grande))