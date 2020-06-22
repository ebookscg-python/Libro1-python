# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.10
Calcula e imprime el total a pagar por un boleto de tren, considerando
la distancia a recorrer y el número de días entre el viaje de ida y el 
de vuelta.
"""

distancia = float(input('Ingrese la distancia de punto a punto: '))
dias = int(input('Número de días entre el viaje de ida y vuelta: '))
if distancia * 2 > 500 and dias > 10:
    costo = distancia * 2 * 1.9 * 0.80
else:
    costo = distancia * 2 * 1.9    
print(f'\nCosto del boleto= ${costo:.2f}')
