#!/usr/bin/python3.11

#    Si el resto es 0, la letra es T
#    Si el resto es 1, la letra es R
#    Si el resto es 2, la letra es W
#    Si el resto es 3, la letra es A
#    Si el resto es 4, la letra es G
#    Si el resto es 5, la letra es M
#    Si el resto es 6, la letra es Y
#    Si el resto es 7, la letra es F
#    Si el resto es 8, la letra es P
#    Si el resto es 9, la letra es D
#    Si el resto es 10, la letra es X
#    Si el resto es 11, la letra es B
#    Si el resto es 12, la letra es N
#    Si el resto es 13, la letra es J
#    Si el resto es 14, la letra es Z
#    Si el resto es 15, la letra es S
#    Si el resto es 16, la letra es Q
#    Si el resto es 17, la letra es V
#    Si el resto es 18, la letra es H
#    Si el resto es 19, la letra es L
#    Si el resto es 20, la letra es C
#    Si el resto es 21, la letra es K
#    Si el resto es 22, la letra es E

dni = int(input("Indica el número de DNI sin letra: "))

resto = dni % 23
if resto == 0:
    letra = 'T'
elif resto ==  1:
    letra = 'R'
elif resto == 2:
    letra = 'W'
elif resto == 3:
    letra = 'A'
elif resto == 4:
    letra = 'G'
elif resto == 5:
    letra = 'M'
elif resto == 6:
    letra = 'Y'
elif resto == 7:
    letra = 'F'
elif resto == 8:
    letra = 'P'
elif resto == 9:
    letra = 'D'
elif resto == 10:
    letra = 'X'
elif resto == 11:
    letra = 'B'
elif resto == 12:
    letra = 'N'
elif resto == 13:
    letra = 'J'
elif resto == 14:
    letra = 'Z'
elif resto == 15:
    letra = 'S'
elif resto == 16:
    letra = 'Q'
elif resto == 17:
    letra = 'V'
elif resto == 18:
    letra = 'H'
elif resto == 19:
    letra = 'L'
elif resto == 20:
    letra = 'C'
elif resto == 21:
    letra = 'K'
elif resto == 22:
    letra = 'E'


print("La letra asignada al número " , dni , " es " ,letra)

