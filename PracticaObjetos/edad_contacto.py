import datetime

class Contacto:
    def __init__(self, name, born_date):
        self.name = name
        self.born_date = born_date

    def contact_year(self):
        age = (datetime.datetime.today() - self.born_date) / 365
        return age


name = input("Nombre de contacto: ")
born_date = datetime.datetime.strptime(input("Fecha de nacimiento (formato dd/mm/aaaa)"), ("%d/%m/%Y"))
guy = Contacto(name, born_date)
age = guy.contact_year()
print(age.days)