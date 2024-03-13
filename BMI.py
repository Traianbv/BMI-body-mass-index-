from tkinter import *


print("Calculator Body Mass Index\n")


while True:

    try:
        a = int(input("Greutate kg : "))
        b = float(input("Inaltime (ex: 1.60 cm) : "))

        total = a / b ** 2

        if float(total) < 18.5:
            input("Slab! ")
            break
        elif float(total) <= 25:
            input("Normal!")
            break
        elif float(tota1l) <= 30:
            input("Gras!")
            break
        elif float(total) <= 35:
            input("Obez!")
            break
        else:
            input("Supraponderal")
            break
    except Exception:
        print("Error please type correct data ! ")








