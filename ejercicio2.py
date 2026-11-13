print("¡Bienvenido al sistema de gestion de camarotes del Crucero Atlántico!")

numero_camarotes = 90

def mostrar_menu():
    print("===MENÚ PRINCIPAL===")
    print("1.- Camarotes disponibles")
    print("2.- Reservar camarotes")
    print("3.- Cancelar camarote")
    print("4.- Historial de reservas")
    print("4.- Salir")

opcion = ""
while opcion != "5":
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print(f"Camarotes disponibles: ")

        #profe ayudeme no me quiero echar el ramo dnvo :/