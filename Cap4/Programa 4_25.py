# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.25
Calcula e imprime la serie generada a partir de la conjetura de Ulam.
"""

n = int(input('Ingrese un entero positivo: '))
if n <= 0:
    print('\nError en el dato.')
else:
    print('\nNúmeros de la serie de Ulam:')
    while n != 1:
        print(n, ' ', end = '')
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1    
    print(n)  # El 1 no se imprime en el ciclo.
     