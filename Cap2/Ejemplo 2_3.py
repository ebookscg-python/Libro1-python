# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_3
Tuplas: creación y algunos ejemplos de usos.
"""

vacia = ()  # Tupla vacía.
numeros = (1, 2, 3)  # Formada por 3 números.
# Formada por 3 cadenas.
saludos = ('Buenos días', 'Buenos tardes', 'Buenas noches')  
# Formada por datos de distintos tipos.
mezcla = ('rojo', 4, True, -16.5)  
fecha = 31, 'enero', 2020  # Define una fecha. No se usaron ().

print('\nEjemplos de tuplas:'.upper())
print(vacia)
print(numeros)
print(mezcla)
print(fecha)

# Tuplas de un solo elemento: requieren una coma luego del elemento.
elem_con_coma = ('hola',)  # Para que se considere una tupla.
elem_sin_coma = ('hola')  # Al faltarle la coma, se considera una cadena.
# Imprime: <class 'tuple'>
print('\nIncluyendo la coma anónima:', type(elem_con_coma))  
# Imprime: <class 'str'>
print('No incluyendo la coma anónima:', type(elem_sin_coma))  

# Funciones de tuplas.
# Cantidad de elementos de la tupla.
print('\nLa longitud de la tupla es:', len(mezcla))  
# Cuenta cuántas veces está el 4 en la tupla.
print(f'El 4 está {mezcla.count(4)} vez (veces) en: {mezcla}')  
# Regresa la posición del valor True en la tupla.
print('El valor True está en la posición:', mezcla.index(True))  
#print(mezcla.index(17))  # Da un ValueError

# Concatena tuplas con el operador +.
conca = numeros + mezcla
print('\nResultado de la concatenación de las tuplas:', conca)

# Repite tuplas con el operador *.
repite = numeros * 3
print('\nLa tupla repetida 3 veces es:', repite)

# Acceso a elementos de la tupla por medio de un índice.
print('\nEl cuarto elemento es:', conca[3])  # Enumera a partir de 0.
print('\nEl último elemento es:', mezcla[-1])  # Inicia desde el final.
#print(vacia[1])  # Da IndexError: tuple index out of range

# Se pueden subdividir (slice) como las cadenas.
parte = mezcla[0:2]
print('\nLa tupla formada por los 2 primeros elementos es:', parte)

# Desempaquetar valores de una tupla. Exige conocer la longitud de la tupla.
dia, mes, anio = fecha
print(f'\nLuego de desempaquetar: día = {dia}, mes = {mes} y año = {anio}')
manana, tarde, noche = saludos
print(f'\nA la mañana decimos: "{manana}", a la tarde: "{tarde}" y ' 
      f'a la noche: "{noche}"')
# Da: ValueError: too many values to unpack (expected 2)
#val1, val2 = mezcla  

# Anidar tuplas: 2 cadenas y una tupla.
datos_completos = 'Silvia', 'Guardati', fecha 
print('\nAnidando 2 cadenas y 1 tupla:', datos_completos)
# Anidar tuplas: 2 tuplas.
sal_fecha = (saludos, fecha)
print('\nAnidando 2 tuplas:', sal_fecha)

# Comparación de tuplas.
# Da True: los 3 primeros elementos coinciden, pero repite tiene más.
print('\n¿Menor?', numeros < repite)    
# Da True: 'hola' es mayor que el primer elemento de saludos: 
# minúsculas > mayúsculas.
print('\n¿Mayor?', elem_con_coma > saludos)

# Genera una tupla a partir de una cadena de caracteres.
letras = tuple('lagarto')
print('\nLa tupla formada a partir de lagarto es:', letras)
