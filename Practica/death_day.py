import datetime
import random
def underline(phrase):
    print(phrase)
    print("-" * len(phrase))

def yes_no_cuestion(cuestion):
    answer = None
    while answer != "S" and answer != "N" and answer != "O":
        answer = input(cuestion + "S/N/O: ")
    return answer

underline("Calcula el dia de tu muerte")

birth_date = input("Cual es tu fecha de nacimiento (formato dd/mm/yyyy)")
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

AVERAGE_LIFESPAN = 80
random_lifespan = AVERAGE_LIFESPAN - int(random.random() * AVERAGE_LIFESPAN / 2)

SMOKER_PENALIZATION = 6
DRINKER_PENALIZATION = 4
JOGGER_PENALIZATION = 4
EPILEPTIC_PENALIZATION = 10

smoker = yes_no_cuestion("Fumas? ")
if smoker == "S":
    random_lifespan -= SMOKER_PENALIZATION
elif smoker == "O":
    random_lifespan -= SMOKER_PENALIZATION / 2

drinker = yes_no_cuestion("Bebes? ")
if drinker == "S":
    random_lifespan -= DRINKER_PENALIZATION
elif drinker == "O":
    random_lifespan -= DRINKER_PENALIZATION / 2

jogger = yes_no_cuestion("Haces deporte? ")
if jogger == "N":
    random_lifespan -= JOGGER_PENALIZATION
elif jogger == "O":
    random_lifespan -= JOGGER_PENALIZATION / 2

epileptic = yes_no_cuestion("Sufres ataques de epilepsia? ")
if epileptic == "S":
    random_lifespan -= EPILEPTIC_PENALIZATION
elif epileptic == "O":
    random_lifespan -= EPILEPTIC_PENALIZATION / 2

death_date = birth_date + datetime.timedelta(days=random_lifespan*365)
days_to_die = death_date - datetime.datetime.now()
death_date_day = death_date.weekday()
if death_date_day == 0:
    death_date_day = "lunes"
elif death_date_day == 1:
    death_date_day = "martes"
elif death_date_day == 2:
    death_date_day = "miercoles"
elif death_date_day == 3:
    death_date_day = "jueves"
elif death_date_day == 4:
    death_date_day = "viernes"
elif death_date_day == 5:
    death_date_day = "sabado"
elif death_date_day == 6:
    death_date_day = "domingo"

death_age = death_date - birth_date
death_age = int(death_age.days / 365 - 1)


print("Fecha de muerte: {}, te quedan {} dias".format(death_date.strftime("%d/%m/%Y"), days_to_die.days))
print("Moriras un {}, a los {} anos".format(death_date_day, death_age))