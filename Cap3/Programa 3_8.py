# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.8
Dada la calificación de un alumno, luego de analizarla, se imprime
un mensaje indicando si el alumno aprobó o no.
"""

calificacion = float(input('\nIngrese la calificación del alumno: '))
if calificacion >= 6:
    print('\nAprobó', end = ':)')
else:
    print('\nNo aprobó', end = ':(')
    