#!/usr/bin/python3.11

from colorama import init, Fore, Back, Style

init()
print(Fore.RED + "Texto en color rojo")
print(Back.WHITE + "Texto rojo con fondo blanco")
print(Back.WHITE + Style.BRIGHT + "Texto brilla")
print(Style.RESET_ALL + "Texto con valores por defecto")
print(Fore.WHITE+Back.BLUE + "Texto blanco con fondo azul" + Back.RESET)
print("Texto blanco sobre fondo negro")

