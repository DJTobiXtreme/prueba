import datetime

hoy = datetime.datetime.now()
cumple = datetime.datetime(year=2019, month=8, day=15,)

print(cumple - hoy)
print(datetime.datetime.now(cumple - hoy))