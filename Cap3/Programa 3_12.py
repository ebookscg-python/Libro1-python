# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.12
Dado un número entero, determina e imprime un mensaje indicando
si el número es par o impar.
"""

entero = int(input('Ingrese un número entero: '))
if entero % 2 == 0:
    print('El número es par.'.center(40))
else:
    print('El número es impar.'.center(40))
