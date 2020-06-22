# -*- coding: utf-8 -*-
"""
@author: guardati
Módulo geometrico.py
Agrupa varias funciones dedicadas al cálculo de operaciones realizadas con
figuras geométricas.

Funciones:
    -area_rectangulo: calcula el área de un rectángulo.
    -perimetro_rectangulo: calcula el perímetro de un rectángulo.
    -area_circulo: calcula el área de un círculo.
    -perimetro_circulo: calcula el perímetro de un círculo.
"""

pi = 3.1415926  # Asigna valor a la variable pi.

def area_rectangulo(base, altura):
    """ Calcula y regresa el área de un rectángulo.
    
    Parámetro:
        - base: de tipo int o float > 0, es la base de un rectángulo.
        - altura: de tipo int o float > 0, es la altura de un rectángulo.
    Regresa:
        El área de un rectángulo, de tipo int o float (depende de los datos).
    """
    return base * altura

def area_circulo(radio):
    """ Calcula y regresa el área de un círculo.
    
    Parámetro:
        - radio: de tipo int o float > 0, es el radio de un círculo.
    Regresa:
        El área de un círculo, de tipo float.
    """
    return pi * radio ** 2


