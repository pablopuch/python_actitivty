'''
    05_Ejercicio
    Escribe un programa que pida un nombre de usuario y una contraseña y 
    si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
'''

name = input('Usuario: ')
password = input('Contraseña: ')


if (name == 'pepe' and password == 'asdasd'):
    print('Has entrado en el sistema')
else:
    print("Error, no tienes acceso")