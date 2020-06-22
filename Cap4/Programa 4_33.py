# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.33
Genera una secuencia de números a partir de un número dado.
"""

valor = int(input('\nIngrese un número entero positivo: '))
if valor <= 0:
    print('\nError en el dato.'.upper())
else:
    for renglon in range(1, valor + 1):        
        for numero in range(1, renglon + 1):
            print(numero, ' ', end = '')        
        print()