# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_1
Alternativa de solución del problema 3.10

Calcula e imprime el total a pagar por un boleto de tren, considerando
la distancia a recorrer y el número de días entre el viaje de ida y el 
de vuelta.
"""

distancia = float(input('Ingrese la distancia de punto a punto: '))
dias = int(input('Número de días entre el viaje de ida y vuelta: '))
costo = distancia * 2 * 1.9
if distancia * 2 > 500 and dias > 10:
    costo = costo * 0.80    
print(f'\nCosto del boleto= ${costo:.2f}')
