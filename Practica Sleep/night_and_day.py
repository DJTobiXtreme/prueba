from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    alarm_weekday = []
    alarm_date = datetime.datetime(year=2000, month=5, day=2)
    current_time = datetime.datetime.now()
    current_time = current_time.replace(minute=0, second=0, microsecond=0)
    is_night = False
    user_input = None

    alarm_confirmation = input("Deseas utilizar una alarma: (S/N) ")
    if alarm_confirmation == "S":
        week_or_date = input("Deseas una fecha en particular (D) o que se repita durante la semana (W) ")
        if week_or_date == "D":
            alarm_date = datetime.datetime.strptime(input("Elige la fecha y hora de la alarma: (Formato dd/mm/yyyy/hh) "), "%d/%m/%Y/%H")
        elif week_or_date == "W":
            alarm_hour = datetime.datetime.strptime(input("Elige la hora de la alarma: (Formato hh) "), "%H")
            while user_input != "N":
                user_input = input("Elige el dia de la alarma (0= Lun, 6= Dom, N para finalizar) ")
                alarm_weekday.append(user_input)
    else:
            print("Esta bien, no has definido alarma")

    while True:

        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")
        if alarm_date == current_time:
            write_file_and_screen("Alarma", "horas.txt")
        elif str(current_time.weekday()) in alarm_weekday and alarm_hour.hour == current_time.hour:
            write_file_and_screen("Alarma", "horas.txt")




if __name__ == "__main__":
    main()