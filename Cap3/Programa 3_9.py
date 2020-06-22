# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.9
Dado el sueldo actual de un empleado, si este es menor a $8000
se incrementa un 12%. En caso contrario, el incremento
es del 8%. Una vez determinado y calculado el aumento se imprime 
junto con el nuevo sueldo.
"""

sueldo = float(input('Ingrese el sueldo del trabajador: $'))
if sueldo < 8000:
    aumento = sueldo * 0.12
else:
    aumento = sueldo * 0.08    
nuevo_sueldo = sueldo + aumento
print(f'\nAumento = ${aumento:.2f} y nuevo sueldo = ${nuevo_sueldo:.2f}')
    
