# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.14
Determina e imprime un mensaje indicando si el tercer dato dado
está comprendido o no entre los otros dos.
"""

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número: '))
if num3 >= num1 and num3 <= num2:
    print(f'\nEl {num3} está comprendido entre el {num1} y el {num2}.')
else:
    print(f'\nEl {num3} no está comprendido entre el {num1} y el {num2}.')