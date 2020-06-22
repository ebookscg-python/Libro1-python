# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.11
"""

def estan_ordenadas(palabra):
    """ Determina si las letras de la palabra están ordenadas alfabéticamente.
    Parámetro:
        palabra: de tipo str.
    Regresa:
        True/False si las letras de la palabra tienen/o no orden alfabético.
    """
    n = len(palabra)
    i = 0
    while i < n - 1 and palabra[i] <= palabra[i + 1]:
        i += 1
    return i == n - 1

def cuenta_palabras(nombre):
    """ Cuenta y regresa el total de palabras que tienen las letras 
    ordenadas alfabéticamente. Las palabras se leen de un archivo.
    Parámetro:
        nombre: de tipo str. Nombre del archivo.
    Regresa:
        El total de palabras que cumple con la condición.
    """  
    with open(nombre, 'r') as arch:
        contador = 0 
        for pal in arch:
            pal = pal.strip()
            if estan_ordenadas(pal):
                contador += 1
        return contador
# -------------------------------------------------------------------------              
nombre = input('\nNombre del archivo que quiere analizar: ') 
try:
    print('\nTotal de palabras con letras ordenadas:', cuenta_palabras(nombre))
except Exception:
    print('Problemas con el archivo.')      
    
