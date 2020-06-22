# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.2
Dado el sueldo actual de un empleado, si este es menor a $8000
se incrementa en un 12% y, además, se imprime el nuevo sueldo.
"""

sueldo = float(input('Ingrese el sueldo del trabajador: $'))
if sueldo < 8000:
    nuevo_sueldo = sueldo * 1.12
    print(f'\nEl nuevo sueldo es = ${nuevo_sueldo:.2f}')
    
