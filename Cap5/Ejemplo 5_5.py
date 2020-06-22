# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_5
Documentación de funciones, tipo "docstring".
"""

def calcula_factorial(numero):
    """Calcula el factorial de un número.
    
    Parámetro:
        numero: es un número de tipo int y debe ser > 0.
    Regresa:
        El factorial del número recibido. 
    """
    factorial = 1
    for valor in range(2, numero + 1):
        factorial *= valor
    return factorial


# Para consultar la documentación de la función.
print(calcula_factorial.__doc__)  

# Ejemplo de uso de la función.
n = int(input('Ingrese un número entero positivo: '))
print(f'El factorial de {n} es = {calcula_factorial(n)}')