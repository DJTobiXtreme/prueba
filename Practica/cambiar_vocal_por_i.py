input_usuario = ""
vocales = ["a", "e", "o", "u", "A", "E", "I" "O", "U"]

while input_usuario != "FIN":
    input_usuario = input("Di algo. escribe FIN para finalizar: ")
    for letra in input_usuario:
        if letra in vocales:
            input_usuario = input_usuario.replace(letra, "i",1)
    if input_usuario != "FIN":
         print(input_usuario)

print("Has terminado")
