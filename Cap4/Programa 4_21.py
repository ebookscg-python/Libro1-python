# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.21
Calcula e imprime el total gastado durante un viaje.
No se conoce el total de compras y gastos por lo que, cuando ya no haya
valores que ingresar, se dará un -1 (bandera de fin de datos).
"""

gasto = float(input('Ingrese el importe del gasto o de la compra: $'))
suma_gastos = 0
while gasto > 0:
    suma_gastos += gasto
    gasto = float(input('Ingrese el siguiente importe: $'))    
print(f'\nTotal gastado durante el viaje = ${suma_gastos:.2f}')