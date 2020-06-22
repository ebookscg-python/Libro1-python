# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.12
"""

def es_palindromo(secuencia):
    """ Determina si la secuencia es palíndromo.
    
    Parámetro:
        secuencia: cualquier tipo iterable
    Regresa:
        True si la secuencia es palíndromo, False en caso contrario.
    """    
    # Se convierte a str para usar el método replace y quitar 
    # los posibles espacios en blanco de la secuencia.
    secuencia = str(secuencia)
    secuencia = secuencia.replace(' ', '')
    n = len(secuencia)
    izq = 0
    der = n - 1
    while izq <= der and secuencia[izq] == secuencia[der]:
        izq += 1
        der -= 1
    return izq > der
    
# CP1: se proporcionan secuencias que son palíndromos.
print('\nEvaluando palíndromos...')
print(es_palindromo('neuquen'))
print(es_palindromo('anita lava la tina'))
print(es_palindromo('amigo no gima'))
print(es_palindromo(1001001))
print(es_palindromo('yo dono rosas oro no doy'))
print(es_palindromo(3526253))

# CP2: se proporcionan secuencias que no son palíndromos.
print('\nEvaluando no palíndromos...')
print(es_palindromo('el perro ladra toda la tarde'))
print(es_palindromo('amigo no gima de esa manera'))
print(es_palindromo(1101001))
print(es_palindromo(35248))