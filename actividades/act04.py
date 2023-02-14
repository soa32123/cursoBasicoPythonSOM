#!/usr/bin/python3.11

# Importamos os
import os

datos = "FA:BA:DA:FA:BA:DA 192.168.5.3"
ip = datos[18:]

response = os.system("ping -c 5 " + ip + " >/dev/null")
if response == 0:
    print("Ordenador encendido")
else:
    print("Ordenador apagado")
print("Saliendo...")