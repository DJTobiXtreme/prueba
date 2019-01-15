import datetime

hoy = datetime.datetime.now()
hace_5_dias = hoy - datetime.timedelta(days=5)



print("Hace 5 dias fue: {}".format(hace_5_dias.day))
print( hace_5_dias.weekday())