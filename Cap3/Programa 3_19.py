# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.19
Calcula e imprime el precio de venta de una obra de arte.
Este precio se calcula incrementando el precio establecido por el 
dueño en un cierto porcentaje según la técnica empleada.
"""

precio = float(input('Ingrese el precio base: $'))
tecnica = input('Ingrese la técnica usada: ')
tecnica = tecnica.lower()
if tecnica == 'óleo':
    porcentaje = 0.25
elif tecnica == 'acuarela':
    porcentaje = 0.2
elif tecnica == 'gouache':
    porcentaje = 0.18
else: 
    porcentaje = 0.1
precio_venta = precio + precio * porcentaje
print(f'\nPrecio de venta de la obra de arte = ${precio_venta:.2f}')