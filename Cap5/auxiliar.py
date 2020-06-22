# -*- coding: utf-8 -*-
"""
@author: guardati
Módulo auxuliar.py
Agrupa varias funciones desarrolladas para algunos problemas
del capítulo 5, para facilitar el reuso de estas.

Funciones:
    es_primo: determina si un número es o no primo.
    es_palindromo: determina si una secuencia es o no palíndromo.
    convierte_a_binario: obtiene la notación en binario de un 
    número entero positivo.
    suma_divisores: obtiene la suma de los divisores de un número
    entero positivo.
    genera_espejo: obtiene y regresa e número espejo del número recibido.
    calcula_edad: calcula y regresa la edad de acuerdo con la fecha de 
    nacimiento y la fecha actual.
"""

import time

def es_primo(numero):
    """ Determina si un número es primo o no.
    
    Parámetro:
        número: es de tipo int o float y > 0.
    Regresa:
        True si el número es primo, False en caso contrario.
    """
    primo = False
    if numero == 2:
        primo = True
    else:
        # Descarta el 1 y todos los pares > 2.
        if numero > 2 and numero % 2 != 0:  
            divisor = 3
            limite = numero // 2            
            while divisor < limite and numero % divisor != 0:
                divisor += 2                
            if divisor >= limite:
                primo = True                
    return primo

def es_palindromo(secuencia):
    """ Determina si la secuencia es palíndromo.
    
    Parámetro:
        secuencia: cualquier tipo iterable
    Regresa:
        True si la secuencia es palíndromo, False si no.
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


def convierte_a_binario(numero):
    """ Convierte un número entero positivo a binario.
    
    Parámetro:
        numero: de tipo int, > 0.
    Regresa:
        La representación binaria del número. Es de tipo int.
    Lanza:
        ValueError: cuando el dato no es entero o > 0.
    """
    if type(numero) == int and numero > 0:
        binario = 0
        potencia = 1
        while numero >= 2:
            digito = numero % 2
            numero = numero // 2
            binario = binario + digito * potencia
            potencia = potencia * 10
        binario = binario + numero * potencia
        return binario
    raise ValueError('El dato no es un número entero o no es positivo.')

def suma_divisores(numero):
    """ Calcula la suma de los divisores de un número, sin 
    incluir al mismo número.
    
    Parámetro:
        numero: de tipo int, > 0.
    Regresa:
        La suma de los divisores del número. Es de tipo int.
    Lanza:
        ValueError: cuando el dato no es entero o > 0.
    """
    if type(numero) == int and numero > 0:
        suma = 0
        limite = numero // 2
        for num in range(1, limite + 1):
            if numero % num == 0:
                suma += num
        return suma
    raise ValueError('El dato no es un número entero o no es positivo.')

def genera_espejo(numero):
    """ Genera el número espejo del número recibido.
    
    Parámetro:
        numero: de tipo int, > 0.
    Regresa:
        Un número de tipo int que es el espejo del número recibido.
    Lanza:
        ValueError: cuando el dato no es entero o no es > 0.
    """
    if type(numero) == int and numero > 0:
        espejo = 0
        temporal = numero
        while temporal > 0:              
            digito = temporal % 10
            espejo = espejo * 10 + digito
            temporal = temporal // 10    
        return espejo
    raise ValueError('El dato no es un número entero o no es positivo.')

def calcula_edad(fecha_nac):
    """ Calcula la edad, en años cumplidos, dada la fecha
    de nacimiento.
    
    Parámetro:
        fecha_nac: de tipo tuple, almacena la fecha de 
        nacimiento con el formato (dd, mm, aaaa).
    Regresa:
        La edad que es de tipo int.
    """
    dia_nac = fecha_nac[0]
    mes_nac = fecha_nac[1]
    anio_nac = fecha_nac[2]   
    fecha_act = time.localtime()
    dia_act = fecha_act[2]
    mes_act = fecha_act[1]
    anio_act = fecha_act[0] 
    edad = 0
    if anio_act > anio_nac:
        edad = anio_act - anio_nac - 1   
        if mes_act >= mes_nac and dia_act >= dia_nac:
            edad += 1
    return edad