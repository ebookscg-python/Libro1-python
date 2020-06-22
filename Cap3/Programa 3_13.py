# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.13
Dados el color, el aroma y el peso de una piña o ananá, imprime un mensaje 
indicando si la fruta está o no en condiciones para consumirse.
El color y el aroma se expresan como cadenas de caracteres, mientras que
el peso como valor booleano, está o no pesada.
Los 3 datos se pudieron manejar por medio de otros tipos de datos. En este
problema se decidió hacerlo así para practicar estos en particular.
"""

color = input('Ingrese el color de la fruta: ')
aroma = input('Ingrese el aroma de la fruta: ')
pesada = bool(input('Ingrese si la fruta está pesada (True/False): '))
# Se pasan a minúsculas para evitar inconsistencias cuando se comparen.
color = color.lower()
aroma = aroma.lower()
if color == 'dorado' and aroma == 'suave' and pesada:
    print('\nLa fruta está madura. ¡Lista para comerse!')
else:
    print('\nLa fruta no está madura o ya se pasó.')
