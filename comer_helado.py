apetece_helado_input = input("quieres comer helado? (SI/NO)").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("No se lo que dices, solo puedes poner si o no, lo considerare un no")
    apetece_helado = False

tiene_dinero_input = input("tienes dinero? (SI/NO)").upper()
esta_tu_tia_input = input("esta tu tia? (SI/NO)").upper()

if tiene_dinero_input == "SI" or esta_tu_tia_input == "SI":
    puede_permitirselo = True
elif tiene_dinero_input == "NO" and esta_tu_tia_input == "NO":
    puede_permitirselo = False
else:
    print("No se lo que dices, solo puedes poner si o no, lo considerare un no")
    apetece_helado = False



if apetece_helado and puede_permitirselo:
    print("Pues a comer")
else:
    print("No hagas nada")