# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.19
Calcula e imprime la suma de los dígitos contenidos en una cadena.
"""

cadena_caracteres = input('Ingrese la cadena de caracteres: ')
suma_digitos = 0
for caracter in cadena_caracteres:
    try:
        suma_digitos += int(caracter)
    except ValueError:
        pass  # Si no es un dígito, no hay nada que hacer.    
print(f'\nLa suma de los dígitos contenidos en la cadena es = {suma_digitos}')