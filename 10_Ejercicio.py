'''
    03_Ejercicio
    Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
    Dicha calificación se compone de los siguientes porcentajes:

        55% del promedio de sus tres calificaciones parciales.
        30% de la calificación del examen final.
        15% de la calificación de un trabajo final.
'''

parcial_1 = float(input('Nota del 1º parcial: '))
parcial_2 = float(input('Nota del 2º parcial: '))
parcial_3 = float(input('Nota del 3º parcial: '))

nota_parciales = [parcial_1, parcial_2, parcial_3]
promedio = sum(nota_parciales) / 3

#print('Tu nota media de parciales es: ' + str(promedio))

exam_final = float(input('Nota del examen final: '))
trabajo_final = float(input('Nota del trabajo final: '))

promedio_parcial = (55 * promedio)/100
cal_examen_final = (30 * exam_final)/100
cal_trabajo_final = (15 * trabajo_final)/100

print('Nota final parciales: ' + str(promedio_parcial) + '\n' +
      'Nota final examen: ' + str(cal_examen_final) + '\n' +
      'Nota final trabajo: ' + str(cal_trabajo_final))

nota_final = promedio_parcial + cal_examen_final + cal_trabajo_final

print('Nota final de la materia: ' + str(nota_final))