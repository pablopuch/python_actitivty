'''
    03_Ejercicio
    Vamos a crear un programa en python donde vamos a declarar un diccionario 
    para guardar los precios de las distintas frutas. El programa pedirá el nombre 
    de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la 
    fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos 
    dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
'''

precio = {'manzana': 2, 'pera': 1.5, 'platano': 1.2}
while True:
    fruta = input('Dime una fruta: ')
    if fruta.lower() not in precio:
        print(f'No hemos encontrado {fruta}')
    else:
        cantidad = int(input('Numero de unidades: '))
        print('El precio es de %f' % (cantidad * precio[fruta.lower()]))
    opcion = input('¿Quieres vender atra fruta (s/n)?')
    while opcion.lower() != 's' and opcion.lower() != 'n':
        opcion = input('¿Quieres vender otra fruta (s/n)?')
    if opcion.lower() == 'n':
        break