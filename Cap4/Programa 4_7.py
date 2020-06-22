# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.7
Calcula e imprime el resultado de la serie:
    1**1 + 2**2 + 3**3 + … + n**n
"""


n = int(input('Ingrese el valor de n: '))
serie = 0
for i in range(1, n + 1):  
    serie += i ** i  
print(f'El resultado de la serie es: {serie}')