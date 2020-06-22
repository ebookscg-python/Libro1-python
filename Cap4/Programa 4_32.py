# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.32
Encuentra e imprime todos los números perfectos comprendidos 
entre 1 y un valor dado por el usuario.
"""

valor = int(input('\nIngrese un número entero positivo: '))
if valor <= 0:
    print('\nError en el dato.'.upper())
else:
    for numero in range(1, valor + 1):
        suma_divisores = 0
        limite = numero // 2 + 1     
        for divisor in range(1, limite):
            if numero % divisor == 0:
                suma_divisores += divisor                
        if numero == suma_divisores:
            print('Número perfecto:', numero)