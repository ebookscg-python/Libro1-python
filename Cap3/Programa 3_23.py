# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.23
Dados 3 números enteros, encuentra e imprime el mayor de los 3.
Se considera que los datos pueden ser iguales entre sí.
"""

n1 = int(input('Ingrese el primer número entero: '))
n2 = int(input('Ingrese el segundo número entero: '))
n3 = int(input('Ingrese el tercer número entero: '))
if n1 > n2:
    if n1 > n3:
        print(f'\nEl mayor es: {n1} (el primer dato)')
    elif n1 == n3:
        print(f'\nLos mayores son: {n1} y {n3} (el primero y el tercero)')
    else:
        print(f'\nEl mayor es: {n3} (el tercer dato)')
elif n1 == n2:
    if n1 > n3:
        print(f'\nLos mayores son: {n1} y {n2} (el primero y el segundo)')
    elif n1 == n3:
        print(f'\nLos mayores son: {n1} - {n2} y {n3} (los 3 son iguales)')
    else:
        print(f'\nEl mayor es: {n3} (el tercer dato)')
elif n2 > n3:
    print(f'\nEl mayor es: {n2} (el segundo dato)')
elif n2 == n3:
    print(f'\nLos mayores son: {n2} y {n3} (el segundo y el tercero)')
else:
    print(f'\nEl mayor es: {n3} (el tercer dato)')
    