#!/usr/bin/python3.11

for i in range(1, 101, 1):
    res = i % 2
    if res == 0:
        print(i, "es un número par")
    else:
        print(i, "es un número impar")
