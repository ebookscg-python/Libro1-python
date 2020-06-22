# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.27
Calcula e imprime el importe de cada venta, así como el total de localidades
vendidas de cada uno de los 3 tipos y el total recaudado en un día.
En esta solución se supone que siempre se ingresa alguno de los 3 tipos
previstos de localidades.
"""

localidadesA = 0
localidadesB = 0
localidadesC = 0
total_recaudado = 0
tipo = input('\nTipo de localidad (A, B, C) o X para terminar: ').upper()
cantidad = int(input('Ingrese la cantidad de boletos o -1 para terminar: '))
while tipo != 'X' and cantidad != -1:
    if tipo == 'A':
        localidadesA += cantidad
        venta = cantidad * 980       
    elif tipo == 'B':
        localidadesB += cantidad
        venta = cantidad * 750
    else:
        localidadesC += cantidad
        venta = cantidad * 520
    print('\nTotal a pagar por los boletos: $', venta)   
    total_recaudado += venta 
    tipo = input('\nTipo de localidad (A, B, C) o X para terminar: ').upper()
    cantidad = int(input('Ingrese la cantidad de boletos o -1 para terminar: '))
total_boletos = localidadesA + localidadesB + localidadesC 
print(f'\nTotal de localidades por tipo: {localidadesA} - '
      f'{localidadesB} - {localidadesC}')
print(f'\nTotal de boletos: {total_boletos}, con una recaudación de:'
      f' ${total_recaudado:.2f}')