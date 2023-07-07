'''
    13_Ejercicio
    Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta..
'''
from datetime import date

fecha = input('Introduce una fecha: ')

fecha_actual = date.today()

if fecha == fecha_actual:
    print("La fecha introducida coincide con la actual")
else:
    print('No es correcta')