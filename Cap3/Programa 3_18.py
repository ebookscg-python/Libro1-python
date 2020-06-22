# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.18
Calcula e imprime el total a pagar por una llamada telefónica 
internacional, la cual se cobra de acuerdo a la región a la cual 
se llamó y a la duración de la misma.
"""

clave = int(input('Ingrese la clave del área geográfica: '))
duracion = int(input('Ingrese la duración en número de minutos: '))
if clave == 12:  
    costo = 9
elif clave == 15:
    costo = 8
elif clave == 21:
    costo = 16
elif clave == 23:
    costo = 19
elif clave == 29:
    costo = 24  
costo *= duracion
print(f'\nTotal a pagar por la llamada = ${costo:.2f}')
