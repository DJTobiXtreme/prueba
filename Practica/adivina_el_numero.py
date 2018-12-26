#falta esconder el input de numero_a_elegir
numero_a_elegir = int(input("Elige un numero entero del 1 al 10: "))

numero_participante = int(input("Intenta adivinar el numero: "))

while numero_a_elegir != numero_participante:
    numero_participante = int(input("Numero incorrecto, intenta de nuevo: "))

print("Felicidades has ganado")
