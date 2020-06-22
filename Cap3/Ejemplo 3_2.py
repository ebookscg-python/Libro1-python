# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_2
Variante de solución del problema 3.18

Calcula e imprime el total a pagar por una llamada telefónica 
internacional, la cual se cobra de acuerdo a la región a la cual 
se llamó y a la duración de la misma.
"""

clave = int(input('Ingrese la clave del área geográfica: '))
duracion = int(input('Ingrese la duración en número de minutos: '))
if clave == 12:  
    costo = duracion * 9
elif clave == 15:
    costo = duracion * 8
elif clave == 21:
    costo = duracion * 16
elif clave == 23:
    costo = duracion * 19
elif clave == 29:
    costo = duracion * 24
else:
    costo = 0
    print('\n', '¡Clave incorrecta!'.center(40))
if costo > 0:
    print(f'\nTotal a pagar por la llamada = ${costo:.2f}')