# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.26
Calcula e imprime el total a pagar a un empleado, considerando
sueldo más horas extras. Para el pago de las horas extras hay que
tener en cuenta la categoría y el total de horas extras trabajadas.
"""

sueldo = float(input('Sueldo del empleado: $'))
categoria = int(input('Categoría del empleado: '))
horas_extras = int(input('Número de horas extras: '))
if categoria == 1:
    precio_hora = 120
elif categoria == 2:
    precio_hora = 150
elif categoria == 3:
    precio_hora = 195
elif categoria == 4:
    precio_hora = 245
else:
    precio_hora = 0
if horas_extras > 30:
    horas_extras = 30    
sueldo_neto = sueldo + horas_extras * precio_hora
print(f'\nSueldo final: ${sueldo_neto:.2f}')