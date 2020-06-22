# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.6
Calcula e imprime el área y el volumen de una esfera.
"""

import math # Módulo math para usar la constante π (pi)

radio = float(input('Ingrese el radio de la esfera: '))
area = 4 * math.pi * radio ** 2
volumen = math.pi * radio ** 3 / 3
print(f'\nÁrea de la esfera = {area:5.2f}')
print(f'Volumen de la esfera = {volumen:4.2f}')

