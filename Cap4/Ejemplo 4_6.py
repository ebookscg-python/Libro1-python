# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_6
Ciclo for con tuplas y uso del operador walrus.
"""

# Se define una tupla formada por números enteros.
numeros = (5, 12, 4, 18, 11, 3, 24, 8, 5, 20)

# Se itera sobre todos los elementos de la tupla.
# Operador := válido a partir de Python 3.8.
for num in numeros:
    if (cuadrado := num ** 2) > 100:  # A la variable cuadrado le asigna el cuadrado de num.  
        print(f'El cuadrado de {num} = {cuadrado} es mayor a 100.')  

# Equivalente a escribir:
for num in numeros:
    cuadrado = num ** 2
    if cuadrado > 100:    
        print(f'El cuadrado de {num} = {cuadrado} es mayor a 100.') 
        
