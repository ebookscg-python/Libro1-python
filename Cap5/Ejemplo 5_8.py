# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_8
Uso del módulo geometrico.py
"""

# Importa todo el módulo geometrico.
import geometrico  

salon_l1 = 5.2
salon_l2 = 6.5
area_salon = geometrico.area_rectangulo(salon_l1, salon_l2)
print(f'\nEl área del salón es = {area_salon:.2f} m2')

radio_mesa = 1.0
area_mesa = geometrico.area_circulo(radio_mesa)
print(f'\nEl área de la mesa es = {area_mesa:.2f} m2')