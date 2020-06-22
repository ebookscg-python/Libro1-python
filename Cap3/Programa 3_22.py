# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.22
Calcula e imprime el valor de f(x), dado como dato un número entero (x).
"""

x = int(input('Ingrese el valor de x (entero): '))
if x < 0 or x > 40:
    y = 0
else:
    if x <= 10:
        y = 5 * x + 12
    elif x <= 20:
        y = x ** 2
    elif x <= 30:
        y = x ** 3 + 5
    else:
        y = x // 6 + x ** 2        
print(f'\nx = {x:d} --> f(x) = {y:d}')