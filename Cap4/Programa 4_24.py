# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.24
Analiza un grupo de calificaciones y las clasifica de acuerdo a ciertos rangos
dados. No se conoce el total de calificaciones que se ingresarán, por lo que
al final se dará un valor negativo.
Además, calcula e imprime el promedio de las calificaciones.
"""

suma_calificaciones = 0
cuenta_calificaciones = 0
rango1 = 0
rango2 = 0
rango3 = 0
rango4 = 0
calificacion = float(input('Ingrese una calificación: '))
while calificacion >= 0:
    suma_calificaciones += calificacion
    cuenta_calificaciones += 1    
    if calificacion < 6:
        rango1 += 1
    elif calificacion < 8:
        rango2 += 1
    elif calificacion < 9:
        rango3 += 1
    else:
        rango4 += 1
    calificacion = float(input('Ingrese una calificación: '))
if cuenta_calificaciones > 0:
    promedio = suma_calificaciones / cuenta_calificaciones
    print(f'\nTotal de calificaciones entre 0 y 5.99: {rango1}')
    print(f'Total de calificaciones entre 6 y 7.99: {rango2}')
    print(f'Total de calificaciones entre 8 y 8.99: {rango3}')
    print(f'Total de calificaciones entre 9 y 10: {rango4}')
    print(f'\nPromedio de las calificaciones = {promedio:.2f}')
else:
    print(f'\nNo se ingresaron datos.'.upper())

