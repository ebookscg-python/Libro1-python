# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.4
Calcula e imprime el total a pagar por un cliente considerando que, si 
el monto de la compra es mayor a $3000, se le hará un descuento del 15%.
"""

compra = float(input('Ingrese el monto de la compra del cliente: $'))
descuento = 0
pago = compra
if compra > 3000:
    descuento = compra * 0.15
    pago = compra - descuento    
print(f'\nCompra = ${compra:.2f} --> descuento = ${descuento:.2f}')
print(f'Total a pagar = ${pago:.2f}')