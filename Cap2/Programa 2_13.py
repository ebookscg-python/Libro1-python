# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.13
Codifica una frase reemplazando las vocales por los números 1, 2
3, 4 o 5. Además, la primera mitad de la cadena pasará a ser la 
segunda mitad y viceversa y las letras consonantes deberán estar en mayúsculas.
"""

frase = input('Ingrese la frase a codificar: ')
# Reemplaza las vocales por números enteros.
frase_codificada = frase.replace('a', '1')
frase_codificada = frase_codificada.replace('e', '3')
frase_codificada = frase_codificada.replace('i', '5')
frase_codificada = frase_codificada.replace('o', '7')
frase_codificada = frase_codificada.replace('u', '9')
mitad = len(frase_codificada) // 2
# Extrae la primera mitad de la frase.
primera_mitad = frase_codificada[0:mitad]  
# Extrae la segunda mitad de la frase.
segunda_mitad = frase_codificada[mitad:]  
frase_codificada = segunda_mitad + primera_mitad
frase_codificada = frase_codificada.upper()  # Pasa a mayúsculas.
print('\nFrase original:', frase)
print('\nFrase codificada:', frase_codificada)