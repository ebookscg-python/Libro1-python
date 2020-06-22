# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.20
Calcula e imprime la suma de los números contenidos en una cadena, 
los cuales deben estar separados por coma.
"""

cadena = input('Ingrese la cadena de caracteres: ')
suma_numeros = 0
for caracter in cadena:
    if caracter == ',':
        posicion = cadena.index(',')
        # Se extrae el número que está antes de la coma.
        numero = cadena[0:posicion]  
        # Evita repetir el número extraído.
        cadena = cadena[posicion + 1:]  
        try:
            suma_numeros += float(numero)
        except ValueError:
            pass  # Si no es un número, no hay nada que hacer.
# Intenta sumar el último número: no se detecta en el for 
# porque la cadena no termina con coma.
try:
    suma_numeros += float(cadena)
except ValueError:
    pass  
print(f'\nLa suma de los números contenidos en la cadena es = '
      f'{suma_numeros:.2f}')
