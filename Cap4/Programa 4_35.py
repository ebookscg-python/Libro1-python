# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.35
Encuentra e imprime todos los pares de números que satisfacen 
la siguiente ecuación:
    p**4 + r**3 < 510
"""

p = 1
r = 1
while p** 4 + r ** 3 < 510:
    while p** 4 + r ** 3 < 510:
        print(f'{p} y {r} < 510')
        r += 1
    r = 1
    p += 1