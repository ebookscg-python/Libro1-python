# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.3
Calcula e imprime el perímetro y el área de un rectángulo.
"""

base = float(input('Ingrese la base del rectángulo: '))
altura = float(input('Ingrese la altura del rectángulo: '))
perimetro = 2 * (base + altura)
area = base * altura
perim_rect = 'Perímetro del rectángulo'
area_rect = 'Área del rectángulo'
print(f'\n{perim_rect} = {perimetro:8.2f} \n{area_rect} = {area:8.2f}')
