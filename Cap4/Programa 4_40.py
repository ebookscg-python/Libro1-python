# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.40
Encuentra e imprime todas las ternas de números que 
satisfacen la siguiente ecuación:
    4 * x**4 + 2 * y**3 + z**3 < 6321
"""

x = 1
y = 1
z = 1
while  4 * x ** 4 + 2 * y ** 3 + z ** 3 < 6321:
    while 4 * x ** 4 + 2 * y ** 3 + z ** 3 < 6321:
        while 4 * x ** 4 + 2 * y ** 3 + z ** 3 < 6321:
            print(f'{x} - {y} - {z} < 6321')
            z += 1
        z = 1
        y += 1
    z = 1
    y = 1
    x += 1


