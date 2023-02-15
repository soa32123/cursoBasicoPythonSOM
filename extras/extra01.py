#!/usr/bin/python3.11

from dialog import Dialog

d = Dialog(dialog = "dialog")
d.set_background_title = "Pruebas..."

d.msgbox("Probando...")

d.yesno("Probando con dos opciones")

if d.yesno("Probamos") == d.OK:
    print("Seleccionaste YES")
else:
    print("Seleccionaste NO")
