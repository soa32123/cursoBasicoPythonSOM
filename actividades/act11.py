#!/usr/bin/python3.11

edad = int(input("Dime tu edad: "))
dinero = int(input("Dime cuando dinero has ganado: "))

# Podemos hacer un if dentro de un if (anidación) evaluando las dos condiciones
# Mejor usar and

if edad > 16 and dinero >= 1000:
    print("¡Debes tributar el dinero que indicas!")
else:
    print("No tributas :(")
