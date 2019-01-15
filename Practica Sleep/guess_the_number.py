from time import sleep
import random

def main():
    while True:
        number_to_guess = random.randint(1, 10)
        print("Adivina un numero del 1 al 10: ")
        user_number = int(input("Elige tu numero: "))
        print("A ver que tal te fue")
        sleep(3)
        if number_to_guess == user_number:
            print("Felicidades has adivinado")
        elif 0 < user_number < 11:
            print("Has fallado, el numero era el {}".format(number_to_guess))
        else:
            print("Tonto, debes elegir un numero del 1 al 10")
        sleep(1.5)

if __name__ == '__main__':
    main()
