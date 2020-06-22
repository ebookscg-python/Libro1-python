# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.17
Calcula e imprime el precio final de un automóvil.
El mismo se determina considerando su precio base y un 
posible descuento y bono, los cuales dependen del modelo.
Además del precio final, se debe imprimir el modelo y el precio base.
"""

modelo = input('Ingrese el modelo del automóvil: ')
precio = float(input('Ingrese el precio base: $'))
modelo_min = modelo.lower()  # Para evitar inconsistencias al comparar.
if modelo_min == 'serie 1':
    precio_final = precio * 0.97 - 20000
elif modelo_min == 'serie 3' or modelo == 'serie 4':
    precio_final = precio * 0.95 - 35000
elif modelo_min == 'serie 5':
    precio_final = precio * 0.95 - 60000
elif modelo == 'x1':
     precio_final = precio * 0.95 - 30000
elif modelo_min == 'x3':
     precio_final = precio * 0.93 - 50000
elif modelo_min == 'x5':
     precio_final = precio * 0.91 - 70000
else:
    precio_final = precio    
print('\nPara el modelo:', modelo.upper())
print(f'\nEl precio base es = ${precio:.2f} y '
      f'el precio final es = ${precio_final:.2f}')