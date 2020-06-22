# -*- coding: utf-8 -*-
"""
@author: guardati
"""

# Solución del problema 2.16 
pais = int(input('Ingrese el prefijo del país: '))
ciudad = int(input('Ingrese el prefijo de la ciudad: '))
numero = int(input('Ingrese el número: '))
numero_telefonico = (pais, ciudad, numero)
print('\nEl número telefónico es:', numero_telefonico)

# Solución del problema 2.17
dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes (1 a 12): '))
anio = int(input('Ingrese el año: '))
fecha = (anio, mes, dia)
print('\nLa fecha es:', fecha)

