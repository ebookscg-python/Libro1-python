# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 2.11
Calcula e imprime el total de plántulas de lechuga que pueden 
plantarse en una huerta, considerando los espacios que debe haber 
entre cada planta y entre cada línea.
"""

metros_ancho = float(input('Ingrese total de metros de ancho de la huerta: '))
metros_largo = float(input('Ingrese total de metros de largo de la huerta: '))
total_lineas = metros_ancho / 0.3  # Se dejan 30 cm entre cada línea
total_plant_por_linea = metros_largo / 0.25 # Se dejan 25 cm entre cada plántula
total_plantulas = int(total_lineas * total_plant_por_linea)  # Se convierte a entero
print(f'\nTotal de plántulas que pueden plantarse en el huerto = {total_plantulas}')