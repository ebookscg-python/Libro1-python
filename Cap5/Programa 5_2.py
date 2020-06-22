# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.2
"""

def calcula_raiz_biseccion(numero, error):
    """ Obtiene la aproximación de la raíz cuadrada de un número 
    por medio del método de la bisección.

    Parámetros:
        numero: es un número int o float, > 0.
        error: es un número float, > 0.
    Regresa:
        La aproximación de la raíz cuadrada del número con un error < error.
    """
    inferior = 0
    superior = numero
    raiz = (inferior + superior) / 2
    while abs(raiz ** 2 - numero) >= error:
        if raiz ** 2 > numero:
            superior = raiz
        else:
            inferior = raiz
        raiz = (inferior + superior) / 2
    return raiz

# =============================================================================
# Algunos usos de la función.
# =============================================================================
raiz1 = calcula_raiz_biseccion(9, 0.1)
raiz2 = calcula_raiz_biseccion(35.5, 0.001)
print(f'\nRaíz de 9, con un error menor a 0.1, es = {raiz1:.4f}')
print(f'Raíz de 35.5, con un error menor a 0.001, es = {raiz2:.5f}')