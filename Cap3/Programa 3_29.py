# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.29
Calcula e imprime el costo de un paquete turístico de acuerdo 
con el destino, el nivel y la cantidad de días de duración. 
"""

destino = input('Ingrese el tipo de destino (playa/colonial/arqueológica): ')
nivel_paquete = input('Ingrese nivel de paquete (exclusivo/lujo/estándar): ')
numero_dias = int(input('Ingrese los días de duración del viaje: '))

''' Se asigna el valor del costo diario de acuerdo con el destino. Observe 
que,si el usuario se equivoca  e ingresa un destino diferente a los 3 
previstos, el programa asignará el valor de $900, y calculará e imprimirá 
un resultado inconsistente. A pesar de que existen maneras de evitar
este tipo de errores, en esta solución no se hace. '''
if destino == 'playa':
    costo_dia = 1200
elif destino == 'colonial':
    costo_dia = 1000
else:
    costo_dia = 900    
costo_paquete = costo_dia * numero_dias
# Se aplica un recargo si el nivel es exxclusivo o lujo.
if nivel_paquete == 'exclusivo':
    costo_paquete *= 1.3
elif nivel_paquete == 'lujo':
    costo_paquete *= 1.1    
if numero_dias > 10:
    costo_paquete *= 0.92  # Se aplica el descuento del 8% para estadías > 10 días.
print(f'\nEl costo del paquete elegido es ${costo_paquete:.2f}')

