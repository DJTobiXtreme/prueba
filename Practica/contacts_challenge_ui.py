import pickle
from time import sleep
from tkinter import *
from tkinter import ttk

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""
    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")
    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)

def print_contacts_tk(contacts, frame_contact_list):
    for contact in contacts:
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=row)
        ttk.Label(frame_contact_list, text=contact["email"]).grid(column=2, row=row)
        ttk.Label(frame_contact_list, text=contact["phone"]).grid(column=3, row=row)

def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=row)
    ttk.Label(frame_contact_list, text=contact["email"]).grid(column=2, row=row)
    ttk.Label(frame_contact_list, text=contact["phone"]).grid(column=3, row=row)

def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact

def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "), input("Teléfono: "), input("Email: "))

    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)

def contact_info(found_contacts, contact_index):
    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)

def search_by_name_or_email(contacts, name_or_email, nombre_o_email):
    try_dont_found = ""
    nombre_o_email2 = ""
    while try_dont_found != 2:
        if nombre_o_email == 1:
            nombre_o_email2 = "email"
        elif nombre_o_email == 0:
            nombre_o_email2 = "nombre"
        search_term = input("Introducir el {} del contacto o parte de él: ".format(nombre_o_email2))
        found_contacts = []

        print("He encontrado los siguientes contactos:")
        contact_indexes = []
        contact_counter = 0

        for contact in contacts:
            if contact[name_or_email].find(search_term) >= 0:
                found_contacts.append(contact)
                print("{} - {}".format(contact_counter, contact[name_or_email]))
                contact_indexes.append(contact_counter)
                contact_counter += 1

        contact_index = 0

        if len(contact_indexes) > 1:
            contact_index = ask_until_option_expected(contact_indexes)
            contact_info(found_contacts, contact_index)
            return
        elif len(contact_indexes) == 0:
            print("No se ha encontrado ninguno.")
            print("Quieres buscar de nuevo (1) o volver al menu (2)")
            try_dont_found = ask_until_option_expected([1, 2])
        else:
            contact_info(found_contacts, contact_index)
            return

def remove_contact(contacts):
    print("\n\nRemover contacto\n")
    contact_indexes = []
    contact_counter = 0
    for contact in contacts:
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1
    contact_to_remove = ask_until_option_expected(contact_indexes)
    removed_contact = contacts.pop(contact_to_remove)
    print("Se ha eliminado el contacto {} correctamente\n".format(removed_contact["name"]))

    return contacts

def find_contact(contacts):
    name_or_email = ""
    print("\n\nBuscar contacto\n")
    print("Quieres buscar por nombre (0) o por email (1)")
    nombre_o_email = ask_until_option_expected([0, 1])
    if nombre_o_email == 0:
        name_or_email = "name"
    elif nombre_o_email == 1:
        name_or_email = "email"
    search_by_name_or_email(contacts, name_or_email, nombre_o_email)

def export_contacts():
    pass

def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()

    root = Tk()
    frame_add_contact = ttk.Frame(root, padding="30 24 30 0")
    frame_add_contact.grid()

    frame_contact_list = ttk.Frame(root, padding="30 0 30 24")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Entry(frame_add_contact, width=15, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=phone).grid(column=3, row=2)

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_contact_list, text="Email").grid(column=2, row=1)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=3, row=1)


    ttk.Button(frame_add_contact,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3, sticky=S)

    for child in frame_add_contact.winfo_children():
        child.grid_configure(padx=5, pady=5)
    for child in frame_contact_list.winfo_children():
        child.grid_configure(padx=31, pady=31)

    counter = 0
    while counter == 0:
        print_contacts_tk(contacts, frame_contact_list)
        counter +=1

    root.mainloop()

    save_contacts(contacts)

if __name__ == "__main__":
    main()