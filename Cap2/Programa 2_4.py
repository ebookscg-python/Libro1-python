# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.4
Calcula e imprime el área de un triángulo por medio de la fórmula de Herón.
"""
# Módulo math necesario para calcular la raíz cuadrada (sqrt).
import math 

lado1 = float(input('Ingrese el primer lado del triángulo: '))
lado2 = float(input('Ingrese el segundo lado del triángulo: '))
lado3 = float(input('Ingrese el tercer lado del triángulo: '))
sp = (lado1 + lado2 + lado3) / 2
area = math.sqrt(sp * (sp-lado1) * (sp-lado2) * (sp-lado3))
print(f'\nEl área del triángulo es = {area:.2f}')
