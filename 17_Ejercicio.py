'''
    17_Ejercicio
    Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
    El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
    Escribir un algoritmo que determine la hora de llegada a la ciudad B.
'''

from datetime import datetime, timedelta


time_start = input('Time de salida: ')
time_travel = input('Tiempo del viaje: ')

seg_start = time_start[0]*3600 + time_start[1]*60 + time_start[2] 








hora_start = '10:24:36'
time_trip = '01:54:10'

time_start = datetime.strptime(hora_start, '%H:%M:%S')
time_end = datetime.strptime(time_trip, '%H:%M:%S')

time_finish = time_start + timedelta(hours=time_end.hour, minutes=time_end.minute, seconds=time_end.second)

print('La hora de llegada es: ', time_finish)