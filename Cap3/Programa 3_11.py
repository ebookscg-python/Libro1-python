# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.11
Calcula e imprime el resultado de dos expresiones aritméticas,
siempre que el cuarto dato sea diferente de 0.
"""

print('\nIngrese cuatro números enteros: ')
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
if n4 != 0: 
    resultado1 = (n1 - n2) ** 3 / n4
    resultado2 = (n2 * n3) ** 5 / n4
    print(f'\nResultado primera expresión= {resultado1:.2f}')
    print(f'\nResultado segunda expresión= {resultado2:.2f}')
else:
    print('\n¡El cuarto número debe ser distinto de 0!'.upper())
