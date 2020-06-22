# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_3
Combinaciones de tipos de parámetros: posicionales, por omisión y de
palabras claves.
"""

'''
Genera una cadena con el nombre completo de una persona, 
ordenado de dos formas diferentes, según uno de los parámetros.
'''
def genera_nombre(nombre, apellido_paterno, apellido_materno, orden = False):
    if orden:
        nomb_comp = apellido_paterno + ' ' + apellido_materno + ', ' + nombre
    else:
        nomb_comp = nombre + ' ' + apellido_paterno + ' ' + apellido_materno
    return nomb_comp

# Paso de parámetros posicionales.
print('\nEjemplos de paso de parámetros posicionales:'.upper())
print(genera_nombre('Juan', 'Pérez', 'Dallia', True))
print(genera_nombre('Juan', 'Pérez', 'Dallia', False))
nombre = 'Irene'
apellido_pat = 'Leno'
apellido_mat = 'Arredondo'
print(genera_nombre(nombre, apellido_pat, apellido_mat, True))

# Paso de parámetros por nombre. No importa el orden, solo los nombres.
print('\nEjemplo de paso de parámetros por nombre:'.upper())
print(genera_nombre(nombre = 'Lucía', apellido_paterno = 'Larios', 
                    apellido_materno = 'Ruíz', orden = False))
print(genera_nombre(orden = True, apellido_paterno = 'Larios', 
                    nombre = 'Lucía', apellido_materno = 'Ruíz'))

# Uso del valor por omisión del parámetro formal orden.
print('\nParámetros por nombre y por omisión:'.upper())
print(genera_nombre(apellido_paterno = 'Pastore', nombre = 'Luis', 
                    apellido_materno = 'Genero'))

'''
Uso combinado de parámetros posicionales y por nombre. Luego de un 
parámetro por nombre no se puede escribir uno posicional.
'''
print(f'\nEjemplo de paso de parámetros posicionales seguidos de '
      f'parámetros por nombre:'.upper())
print(genera_nombre('Pedro', 'Nardoni', apellido_materno = 'Lazo', orden = False))
