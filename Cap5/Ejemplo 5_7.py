# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_7
Lanzamiento de excepciones desde una función.
"""

def calcula_promedio(*numeros):
    """ Calcula el promedio de los números proporcionados.
    
    Parámetro:
        *numeros: cero o varios números, int o float.
    Regresa:
        El promedio de los números.
    Lanza:
        ZeroDivisionError: cuando no se proporcionan datos.
        ValueError: cuando alguno de los datos proporcionados no es numérico.
    """
    try:
        suma = 0
        for valor in numeros:
            suma += valor
        return suma / len(numeros)
    except ZeroDivisionError:
        raise ZeroDivisionError('No hay datos: división entre 0.')
    except TypeError:
        raise TypeError('Error en los datos: no son numéricos.')
    
#========================================================
# Pruebas de la función.
#========================================================
# CP1: no se proporcionan datos: división entre 0.
try:
    promedio = calcula_promedio()  
    print('\nCP1 --> El promedio es =', promedio)
except Exception as error:
    print('\nCP1 -->', error)

# CP2: se proporcionan datos no numéricos.
try:
    promedio = calcula_promedio(4.5, 'hola', 23, -33)  
    print('CP2 --> El promedio es =', promedio)
except Exception as error:
    print('CP2 -->', error)

# CP3: se proporcionan 2 números enteros.
print('CP3 --> El promedio es =', calcula_promedio(4, 8))  
# CP4: se proporcionan 8 números reales.
prom = calcula_promedio(3.5, 8.2, -9.6, 12.2, 25.7, 48.7, -41.55, 39.33)
print('CP4 --> El promedio es =', prom)  
