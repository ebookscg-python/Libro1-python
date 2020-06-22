# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.12
Determina e imprime si un número es perfecto o no.
Se dice que un número es perfecto si la suma de todos sus divisores, 
excepto el mismo, es igual al número.
"""

numero = int(input('Ingrese un número entero positivo: '))
suma_divisores = 0  
limite = numero // 2 + 1  # El posible divisor más grande.
for divisor in range(1, limite):
    if numero % divisor == 0:
        suma_divisores += divisor        
if numero == suma_divisores:
    print('\nEl número', numero, 'es un número perfecto.')
else:
    print('\nEl número', numero, 'no es un número perfecto.')