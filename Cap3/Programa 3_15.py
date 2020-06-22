# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.15
Dados el nivel y el sueldo de un trabajador, calcula el aumento
que le corresponde -de acuerdo a su nivel- e imprime el nivel, 
sueldo anterior y nuevo sueldo.
"""

nivel = int(input('Ingrese el nivel del trabajador: 1..4: '))
sueldo = float(input('Ingrese el sueldo del trabajador: $'))
if nivel == 1:
    nuevo_sueldo = sueldo * 1.12
elif nivel == 2:
    nuevo_sueldo = sueldo * 1.08
elif nivel == 3:
    nuevo_sueldo = sueldo * 1.05
elif nivel == 4:
    nuevo_sueldo = sueldo * 1.038
else: 
    nuevo_sueldo = sueldo     
print('\nNivel:', nivel)
print(f'Sueldo anterior = ${sueldo:.2f}\nNuevo sueldo = ${nuevo_sueldo:.2f}')