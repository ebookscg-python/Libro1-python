# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.21
Dados 3 números enteros, los imprime en orden 
descendente (de mayor a menor).
"""

n1 = int(input('Ingrese el primer número entero: '))
n2 = int(input('Ingrese el segundo número entero: '))
n3 = int(input('Ingrese el tercer número entero: '))
print('\nNúmeros en orden decreciente: ', end = '')
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(n1, n2, n3, sep = ', ')
        else:
            print(n1, n3, n2, sep = ', ')
    else:
        print(n3, n1, n2, sep = ', ')
else:
    if n2 > n3:
        if n1 > n3:
            print(n2, n1, n3, sep = ', ')
        else:
            print(n2, n3, n1, sep = ', ')
    else:
        print(n3, n2, n1, sep = ', ')
            
