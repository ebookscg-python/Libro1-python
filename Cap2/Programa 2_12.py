# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.12
Codifica una frase llevando sus dos primeros caracteres 
al final y dejando la frase solo con minúsculas.
"""

frase = input('Ingrese la frase: ')
frase_minusculas = frase.lower()  # Pasa la frase a minúsculas.
# Extrae los 2 primeros caracteres.
dos_primeras_letras = frase_minusculas[0:2]  
resto = frase_minusculas[2:]  # Extrae el resto de la frase. 
# Concatena las 2 cadenas obtenidas.
codificada = resto + dos_primeras_letras  
print('\nLa frase codificada es:', codificada)
