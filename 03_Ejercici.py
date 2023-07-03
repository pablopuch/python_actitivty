'''
    03_Ejercicio
    Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''
import math

cateto_b = float(input('Introduce el cateto b: '))
cateto_c = float(input('Introduce el cateto c: '))

hipotenusa = int(math.sqrt((cateto_b ** 2) + (cateto_c ** 2)))

print('El resultado es: ' + str(hipotenusa))