# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.7
Calcula e imprime el área de un triángulo.
"""

x1 = float(input('Ingrese la coordenada x del primer punto: '))
y1 = float(input('Ingrese la coordenada y del primer punto: '))
x2 = float(input('Ingrese la coordenada x del segundo punto: '))
y2 = float(input('Ingrese la coordenada y del segundo punto: '))
x3 = float(input('Ingrese la coordenada x del tercer punto: '))
y3 = float(input('Ingrese la coordenada y del tercer punto: '))
area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
print(f'\nÁrea del triángulo: {area:.2f}')