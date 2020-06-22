# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.1
Dada la calificación de un alumno, luego de analizarla, se imprime
un mensaje en caso de que sea aprobatoria.
"""

calificacion = float(input('\nIngrese la calificación del alumno: '))
if calificacion >= 6:
    print('\nAprobado', end = ':)')
    