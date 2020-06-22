# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.9
Imprime un número de 4 dígitos, dígito por dígito, de derecha a izquierda.
"""

numero = int(input('Ingrese un número entero de 4 dígitos: '))
for _ in range(1, 5):  
    digito = numero % 10
    print(digito, ' ', end = '')
    numero = numero // 10
