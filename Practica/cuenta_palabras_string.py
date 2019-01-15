frase_usuario = "Hola Hola como estas amigo amigo amigo"
largo_hola = 0
largo_como = 0
largo_estas = 0
largo_amigo = 0

for palabra in frase_usuario.split():
    if "Hola" == palabra:
        largo_hola += 1
    if "como" == palabra:
        largo_como += 1
    if "estas" == palabra:
        largo_estas += 1
    if "amigo" == palabra:
        largo_amigo += 1


print("Hola: {}".format(largo_hola))
print("como: {}".format(largo_como))
print("estas: {}".format(largo_estas))
print("amigo: {}".format(largo_amigo))
