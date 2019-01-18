class Favourite_animal:
    def __init__(self, species, color, region, food_type, favourite_animals_list):
        self.species = species
        self.color = color
        self.region = region
        self.food_type = food_type
        favourite_animals_list.append(self)

favourite_animals_list = []
exits = ""
while exits != "S":
    Favourite_animal(input("Especie: "), input("Color: "), input("Region: "),
                     input("Es carnivoro, omnivoro u hervivoro?: "), favourite_animals_list)
    exits = input("Pulsa S para salir de lo  contrario N: ")

for item in favourite_animals_list:
    print("Especie {}, Color {}, Region {}, Tipo de comida {}".format(item.species,
         item.color,
         item.region,
         item.food_type))
