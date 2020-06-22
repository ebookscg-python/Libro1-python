# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4.4
Calcula e imprime el promedio de las calificaciones de un grupo de n alumnos.
Además, obtiene la calificación más alta y la más baja del grupo y las 
imprime junto con la matrícula del alumno que las obtuvo.

Solución alternativa del problema 4.4. 
Compare esta solución con la desarrollada por usted y con la del Programa 4_4.
"""

total_alumnos = int(input('Ingrese la cantidad de alumnos: '))
if total_alumnos > 0:
    print(f'\nIngrese la matrícula y la calificación del primer alumno:')
    matricula = int(input())
    calificacion = float(input())
    suma_calif = calificacion
    calificacion_mayor = calificacion  # Al mayor se lo inicializa con la primer calificación.
    matricula_mayor = matricula  # Se inicializa la matrícula con la primera leída.
    calificacion_menor = calificacion  # Al menor se lo inicializa con la primer calificación.
    matricula_menor = matricula  # Se inicializa la matrícula con la primera leída.
    for i in range(2, total_alumnos + 1):  # Se leen total_alumnos - 1 en el ciclo
        print(f'\nIngrese la matrícula y la calificación del alumno {i}:')
        matricula = int(input())
        calificacion = float(input())
        suma_calif += calificacion
        if calificacion > calificacion_mayor:
            calificacion_mayor = calificacion
            matricula_mayor = matricula
        elif calificacion < calificacion_menor:
            calificacion_menor = calificacion
            matricula_menor = matricula
    promedio = suma_calif / total_alumnos
    print(f'\nPromedio de calificaciones = {promedio:.2f}')
    print(f'Calificación mayor = {calificacion_mayor:.2f}, obtenida por el alumno con matrícula: {matricula_mayor}')
    print(f'Calificación menor = {calificacion_menor:.2f}, obtenida por el alumno con matrícula: {matricula_menor}')    
else:
    print('\nNo hay datos que procesar.')
    