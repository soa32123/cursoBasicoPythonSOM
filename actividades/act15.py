#!/usr/bin/python3.11

num = int(input("Indica un número del 1 al 10: "))

if num >= 1 and num <= 10:
    for i in range(0, 11, 1):
        res = num * i
        print(num ,"*", i, "= ",res)
else:
    print("Introdujo un número equivocado")
