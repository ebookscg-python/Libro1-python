# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_6

Ejemplos de tipado automático de variables.
Las 2 variables usadas tienen un tipo asociado, dependiendo del valor asignado.
"""

numero = 45  # Se asigna un valor entero.
print('\nVariable \"numero\" es de tipo: ', type(numero))   

numero = 45.16  # Se asigna un valor real.
print('¡Cambió! Ahora \"numero\" es de tipo: ', type(numero))   

nombre_mascota = "Charrúa"  # Se asigna una cadena de caracteres.
print('\nVariable \"nombre_mascota\" de tipo: ',type(nombre_mascota))   

nombre_mascota = True  # Se asigna un valor booleano.
print('¡Cambió! Ahora \"nombre_mascota\" es de tipo: ', type(nombre_mascota))   