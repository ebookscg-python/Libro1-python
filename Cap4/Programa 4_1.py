# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.1
Calcula e imprime la nómina que debe pagar una empresa por sus 10 empleados.
"""

nomina = 0
for i in range (1, 11):
    sueldo = float(input(f'Ingrese el sueldo {i}: $'))
    nomina += sueldo
print('\nLa nómina que debe pagarse es: $', nomina)
