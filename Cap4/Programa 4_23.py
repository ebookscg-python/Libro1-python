# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.23
Calcula e imprime el cuadrado y el cubo de los números naturales 
ingresados hasta que se proporcione un número negativo.
"""

num_natural = int(input('Número -para calcular su cuadrado y su cubo: '))
while num_natural >= 0:
    print(f'{num_natural}, {num_natural ** 2}, {num_natural ** 3}')
    num_natural = int(input('Siguiente número (para terminar un negativo): '))