# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_5
Variante de solución del problema 4.20.
Calcula e imprime la suma de los números contenidos en 
una cadena, los cuales deben estar separados por coma.
"""

cadena = input('Ingrese la cadena de caracteres: ') + ','
suma_numeros = 0
for caracter in cadena:
    if caracter == ',':
        posicion = cadena.index(',')
        numero = cadena[0:posicion]  # Se extrae el número que está antes de la coma.
        cadena = cadena[posicion + 1:]  # Evita repetir el número extraído.
        try:
            suma_numeros += float(numero)
        except ValueError:
            pass  # Si no es un número, no hay nada que hacer.
print(f'\nLa suma de los números contenidos en la cadena es = {suma_numeros:.2f}')
