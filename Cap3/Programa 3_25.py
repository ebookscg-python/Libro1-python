# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.25
Calcula e imprime el bono anual a pagar a un empleado de una empresa de
producción de lácteos.
El bono se calcula de acuerdo a la antigüedad y al sueldo del empleado.
"""

sueldo = float(input('Ingrese el sueldo del empleado: $'))
antiguedad = int(input('Ingrese la antigüedad del empleado (en años): '))
bono = sueldo * antiguedad
if antiguedad <= 10:
    bono *= 0.06
elif antiguedad <= 20:
    bono *= 0.065
else:
    bono *= 0.07
    if antiguedad > 30:
        bono += sueldo * 0.22        
print(f'\nBono anual = ${bono:.2f}')
    