import datetime

ano = int(input("Ingresa el ano: "))
mes = int(input("Ingresa el mes: "))
dia = int(input("Ingresa el dia: "))
fecha_ingresada = datetime.datetime(ano, mes, dia)
hoy = datetime.datetime.now()

horas_faltantes = (hoy - fecha_ingresada)
if horas_faltantes.total_seconds() > 0:
    print("Han pasado {} horas".format(int(horas_faltantes.total_seconds()/3600)))
else:
    print("Faltan {} horas".format(abs(int(horas_faltantes.total_seconds() / 3600))))