#!/usr/bin/python3.11

# Realiza un formulario que muestre por pantalla los datos
# de manera ordenada que se pregunten a continuación:
# – Nombre
# – Apellidos
# – Edad
# – Dirección y
# – Peso

nombre = input("Dime tu nombre: ")
apellido = input("Indícame tu primer apellido: ")
edad = int(input("Dime tu edad: "))
direccion = input("Dime tu dirección: ")
peso = int(input("Indícame tu peso: "))

print("Tu nombre es: " , nombre ,  apellido , " tienes " , edad , " años y pesas ", peso , "Kg. Vives en ", direccion,".")

