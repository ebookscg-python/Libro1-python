# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.3
Calcula e imprime la temperatura ambiente en función del 
número de sonidos emitidos por un grillo.
"""

numero_sonidos = int(input('¿Número de sonidos del grillo? '))
if numero_sonidos >= 0:
    temperatura = 10 + (numero_sonidos - 40) / 7
    print(f'\nLa temperatura en grados Celsius es = {temperatura:.2f}°C')
    