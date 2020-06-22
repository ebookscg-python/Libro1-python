# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.3
"""

def lee_entero_positivo(mensaje):
    """ Lectura de un número entero positivo.
    
    Parámetro:
        mensaje: de tipo str. Es el mensaje que debe desplegarse en el input().
    Regresa:
        Un número entero positivo.
    """
    bandera = True
    while bandera:
        try:
            entero = int(input(mensaje))
            if entero > 0:
                bandera = False
            else:
                print('¡el número debe ser > 0!'.upper())
        except:
            print('solo se aceptan números enteros.'.upper())
    return entero

def dias_y_horas(numero):
    """ Calcula cuantos días y horas están comprendidos en el valor recibido.
    
    Parámetro:
        numero: es un número de tipo int y debe ser > 0.
    Regresa:
        Cantidad de días y horas comprendidos en el número recibido.
    """
    dias = numero // 24
    horas = numero % 24
    return dias, horas

# ========================================================
# Pruebas de las funciones.
# ========================================================   
retraso_recital = lee_entero_positivo('Total de horas de retraso del recital: ')
dias, horas = dias_y_horas(retraso_recital)
print(f'El recital se retrasó {dias} días y {horas} horas')

prox_vuelo = lee_entero_positivo('¿Cuántas horas faltan para el próximo vuelo?: ')
dias, horas = dias_y_horas(prox_vuelo)
print(f'El próximo vuelo sale en {dias} días y {horas} horas')

