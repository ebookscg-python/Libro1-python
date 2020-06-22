# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.2
Calcula e imprime la suma y el promedio de n números enteros.
"""

n = int(input('Ingrese la cantidad de números a procesar: '))
suma = 0
for i in range (1, n + 1):
    numero = int(input(f'Ingrese el número {i}: '))
    suma += numero    
try:
    promedio = suma / n
except ZeroDivisionError:
    print('\nNo es posible calcular el promedio.')
else:
    print('\nSuma =', suma)
    print(f'Promedio = {promedio:.2f}')



