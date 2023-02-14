#!/usr/bin/python3.11


num1 = int(input("Indica el primer número: "))
num2 = int(input("Indica el segundo número: "))

opc = input("Indica la opción que quieres hacer [suma:resta:multiplica]: ")
if opc == "suma":
    print("Accediendo a la opción suma")
    res = num1 + num2
    print("El resultado es " , res)
elif opc == "resta":
    print("Accediendo a la opción resta")
    res = num1 - num2
    print("El resultado es " , res)
elif opc == "multiplica":
    print("Accediendo a la opción multiplica")
    res = num1 * num2
    print("El resultado es " , res)
else:
    print("No introdujo una opción correcta")
