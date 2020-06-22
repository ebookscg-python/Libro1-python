# -*- coding: utf-8 -*-
"""
@author: guardati
Módulo lecturas.py
Solución del problema 5.5
Agrupa varias funciones dedicadas a la lectura de datos, validando estos.

Funciones:
     -lee_numero: lee y regresa un número (int o float).
     -lee_numero_positivo: lee y regresa un número (int o float) > 0.
"""

def lee_numero(tipo, mensaje):
    """ Lectura de un número entero o real, sin importar el signo.
    
    Parámetro:
        tipo: de tipo int o float. Indica qué tipo de número se debe leer.
        mensaje: de tipo str. Es el mensaje que se despliega en el input().
    Regresa:
        Un número, de tipo int o float.
    """
    bandera = True
    while bandera:
        try:
            numero = tipo(input(mensaje))
            bandera = False
        except:
            print(f'solo se aceptan números de tipo {tipo}.'.upper())
    return numero

def lee_numero_positivo(tipo, mensaje):
    """ Lectura de un número entero o real positivo.
    
    Parámetro:
        tipo: de tipo int o float. Indica qué tipo de número se debe leer.
        mensaje: de tipo str. Es el mensaje que se despliega en el input().
    Regresa:
        Un número positivo, de tipo int o float.
    """
    bandera = True
    while bandera:
        try:
            numero = tipo(input(mensaje))
            if numero > 0:
                bandera = False
            else:
                print('¡el número debe ser > 0!'.upper())
        except:
            print(f'solo se aceptan números de tipo {tipo}.'.upper())
    return numero

# ========================================================
# Algunas pruebas de las funciones.
# ========================================================
edad = lee_numero_positivo(int, 'Ingrese la edad del alumno: ')
temperatura = lee_numero(float, 'Ingrese la temperatura actual: ')
print(f'\nEl alumno tiene {edad} años')
print(f'La temperatura del día de hoy es {temperatura} °C')
