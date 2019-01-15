from time import sleep
import random

def main():
    happy_phrase = ["Soy feliz", "Estoy comiendo en mostaza", "Me gusta la carne aunque sea mala"]
    furniture = ["Cama", "Mesa", "Mesa ratona", "Mesa de luz"]
    drinks = ["Coca", "Sprite", "Fanta"]
    hate_phrase = ["Sorete", "Mala persona", "Sos caca"]
    foods = ["Hamburguesa", "Milanesa", "Patynesa"]
    absurd_phrase = ["Demasiado humeda el agua", "Calentito el fuego", "Hielo refrescantemente pegajoso"]
    animals = ["Caballo", "Rana", "Leon"]
    motivacional = ["El unico fracaso es no intentarlo", "Tu puedes", "Se un hombre"]
    animals_sounds = ["Miaw", "Woof", "Meehh"]
    sad_phrase = ["Sin dinero", "DSP limit reached", "Solo"]
    while True:

        sleep(1)
        print(furniture[random.randrange(0, 3)])
        sleep(1)
        print(drinks[random.randrange(0, 2)])
        sleep(1)
        print(hate_phrase[random.randrange(0, 2)])
        sleep(1)
        print(foods[random.randrange(0, 2)])
        sleep(1)
        print(absurd_phrase[random.randrange(0, 2)])
        sleep(1)
        print(animals[random.randrange(0, 2)])
        sleep(1)
        print(motivacional[random.randrange(0, 2)])
        sleep(1)
        print(animals_sounds[random.randrange(0, 2)])
        sleep(1)
        print(sad_phrase[random.randrange(0, 2)])
        sleep(1)
        print(happy_phrase[random.randrange(0, 2)])

if __name__ == '__main__':
    main()