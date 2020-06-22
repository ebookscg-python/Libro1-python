# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.6
Calcula e imprime la productoria para un número n > 0.
"""

n = int(input('Ingrese el valor de n: '))
producto = 1
# A partir de 2: multiplicar por 1 no cambia el resultado.
for i in range(2, n + 1):  
    producto *= i
print(f'El resultado de la productoria es: {producto:.2f}')