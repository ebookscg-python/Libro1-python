# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_6
Lista arbitraria de parámetros.
"""

def imprime(*args):
    """ Imprime los valores recibidos.
    
    Parámetro:
        *args: cero o varios valores.
    """
    print('Esto recibí:', args)
     
# ========================================================
# Pruebas de la función.
# ========================================================
# No se pasan parámetros.
imprime()   
# Se pasan 3 cadenas de caracteres.
imprime('rojo', 'verde', 'azul') 
# Se pasan 4 números reales.
imprime(12.50, 89.50, 30.20, 22.35) 
# Se pasan 4 datos de diferentes tipos.
imprime(True, 16, -45.8, 'hola') 

