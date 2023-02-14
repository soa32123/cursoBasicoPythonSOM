#!/usr/bin/python3.11

edad = int(input("Indique su edad: "))

if edad < 4:
    print("Entrada gratis")
elif edad >= 4 and edad < 18:
    print("Precio 5€")
elif edad > 18:
    print("Precio 10€")
else:
    print("No ha introducido una edad correcta")
