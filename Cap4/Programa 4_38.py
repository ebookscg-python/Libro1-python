# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.38
En una cadena de caracteres cambia algunas letras de 
mayúscula a minúscula e imprime el texto modificado.
"""

texto = input('\nIngrese el texto a modificar: ')
letra = input('Ingrese la letra que debe pasarse a minúsculas: ')
while letra != '':
    nuevo_texto = ''
    pos = texto.find(letra)
    while pos != -1:
        if pos > 0:          
            nuevo_texto +=  texto[0:pos] + chr((ord(letra) + 32))
        else:
            nuevo_texto += texto[0:pos + 1]
        texto = texto[pos + 1:]
        pos = texto.find(letra)
    letra = input('Ingrese la letra que debe pasarse a minúsculas: ')
    nuevo_texto += texto
    texto = nuevo_texto
print('\nTEXTO MODIFICADO:\n', texto.center(60))