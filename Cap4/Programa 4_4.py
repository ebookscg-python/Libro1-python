# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.4
Calcula e imprime el promedio de las calificaciones de un grupo de n alumnos.
Además, identifica la calificación más alta y la más baja del grupo y las 
imprime junto con la matrícula de los alumnos que las obtuvieron.
"""

total_alumnos = int(input('Ingrese la cantidad de alumnos: '))
suma_calif = 0
# Al mayor se lo inicializa con un valor muy pequeño.
calificacion_mayor = -1  
# Al menor se lo inicializa con un valor muy grande.
calificacion_menor = 11  
for i in range(1, total_alumnos + 1):
    print(f'\nIngrese la matrícula y la calificación del alumno {i}:')
    matricula = int(input())
    calificacion = float(input())
    suma_calif += calificacion    
    if calificacion > calificacion_mayor:
        calificacion_mayor = calificacion
        matricula_mayor = matricula        
    if calificacion < calificacion_menor:
        calificacion_menor = calificacion
        matricula_menor = matricula        
if total_alumnos > 0:
    promedio = suma_calif / total_alumnos
    print(f'\nPromedio de calificaciones = {promedio:.2f}')
    print(f'Calificación mayor = {calificacion_mayor:.2f}, obtenida por el alumno con matrícula: {matricula_mayor}')
    print(f'Calificación menor = {calificacion_menor:.2f}, obtenida por el alumno con matrícula: {matricula_menor}')    
else:
    print('\nNo hay datos que procesar.')
    