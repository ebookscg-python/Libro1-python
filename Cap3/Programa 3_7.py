# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.7
Determina si dos números dados satisfacen la expresión:
    p3 + q3 – 2*p*q2 < 970
Si es así, se imprimen los valores de p y q.
"""

p = int(input('Ingrese el primer número: '))
q = int(input('Ingrese el segundo número: '))
resultado = p ** 3 + q ** 3 - 2 * p * q ** 2
if resultado < 970:
    print(f'\nLos números {p} y {q} sí satisfacen la ecuación.')