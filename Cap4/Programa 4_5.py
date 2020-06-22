# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.5
Calcula e imprime el valor de la serie:
    1 + 1/1 + 1/2 + ...+ 1/n
"""

n = int(input('Ingrese el valor de n: '))
suma = 0
for i in range(1, n + 1):
    suma += 1 / i    
print(f'El resultado de la serie es: {suma:.2f}')