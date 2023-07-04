'''
    18_Ejercicio
    Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
'''

name = str(input('Escribe tu nombre: '))
surname_first = str(input('Escribe tu primer apellido: '))
surname_second = str(input('Escribe tu segundo apellido: '))

letter_name = name[0].upper()
letter_surname = surname_first[0].upper()
letter_surname_second = surname_second[0].upper()

print(letter_name,',',letter_surname,',',letter_surname_second)