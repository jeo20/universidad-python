from random import randint

nombre = input("Ingrese su nombre: ")
nombre_mayuscula = nombre.upper().strip()[0:2]

apellido = input("Ingrese su apellido: ")
apellido_mayuscula = apellido.upper().strip()[0:2]

year = input("Ingrese su año de naciomiento: ")
year_2 = year.strip()[2:4]

valor_random = randint(0,9999)

print(f"{nombre_mayuscula}{apellido_mayuscula}{year_2}{valor_random}")