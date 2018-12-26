frase_usuario = input("Escribe una frase: ")

mayusculas = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

n_mayusculas = 0

for letra in frase_usuario:
    if letra in mayusculas:
        n_mayusculas += 1

print(n_mayusculas)