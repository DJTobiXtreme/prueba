from time import sleep
import random

def main(sleep_seconds):
    words_list = ["Bajo", "Guitarra", "Bateria", "Piano", "Violin", "Viola", "Violonchelo", "Contrabajo"]
    while True:
        sleep(sleep_seconds)
        ramdom_number = random.randrange(0, 7)
        ramdom_number2 = random.randrange(0, 7)
        ramdom_number3 = random.randrange(0, 7)
        print(words_list[ramdom_number], words_list[ramdom_number2], words_list[ramdom_number3])


if __name__ == '__main__':
    main(3)

