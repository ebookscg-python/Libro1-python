# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.5
Determina si nos alcanza para pagar nuestro antojo en el cine.
Si es así, imprime un mensaje adecuado.
"""

dinero_disponible = float(input('Ingrese el monto de dinero del que dispone: $'))
antojo = 135 + 45 # El precio del sándwich y del refresco.
if dinero_disponible >= antojo:
    print('\nSí nos alcanza:)')
