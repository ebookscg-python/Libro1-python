# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.4
"""

def lee_real(mensaje):
    """ Lectura de un número real.
    
    Parámetro:
        mensaje: tipo str. Se despliega en el input().
    Regresa:
        Un número de tipo float.
    """
    bandera = True
    while bandera:
        try:
            real = float(input(mensaje))
            bandera = False
        except:
            print('solo se aceptan números reales.'.upper())
    return real


def calcula_distancia(punto1, punto2):
    """ Calcula la distancia entre dos puntos, dadas sus coordenadas.
    
    Parámetro:
        punto1: de tipo tuple, guarda las coordenadas del primer punto.
        punto2: de tipo tuple, guarda las coordenadas del segundo punto.
    Regresa:
        La distancia entre los puntos. Es de tipo float.
    """
    distancia = ((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2) ** 0.5
    return distancia

#======================================================================
# Algunas pruebas de las funciones.
#======================================================================
x1 = lee_real('Ingrese la coordenada x del primer punto: ')
y1 = lee_real('Ingrese la coordenada y del primer punto: ')
x2 = lee_real('Ingrese la coordenada x del segundo punto: ')
y2 = lee_real('Ingrese la coordenada y del segundo punto: ')
# Se forman las tuplas que representan a los puntos.
punto1 = (x1, y1)
punto2 = (x2, y2)
distancia = calcula_distancia(punto1, punto2)
print(f'\nLa distancia entre los puntos es = {distancia:.2f}')

