# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.5
Calcula e imprime la distancia entre dos puntos.
"""

import math # Módulo math para usar la función raíz cuadrada (sqrt).

x1 = float(input('Ingrese la coordenada x del primer punto: '))
y1 = float(input('Ingrese la coordenada y del primer punto: '))
x2 = float(input('Ingrese la coordenada x del segundo punto: '))
y2 = float(input('Ingrese la coordenada y del segundo punto: '))
distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f'\nLa distancia entre los puntos es: {distancia:.2f}')

