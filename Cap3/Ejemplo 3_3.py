# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_3
Ejemplos de algunas de las excepciones que maneja Python.
Junto a cada caso se explica qué es lo que ocasiona el error
y cuál es la excepción que se lanza.
"""

# Ejemplo de excepción: ValueError.
numero = int(input('Ingrese un número entero: '))
'''
Si al ingresar el dato el usuario se equivoca e ingresa un número 
con decimales, por ejemplo 305.23, entonces se interrumpe la ejecución 
por el error ocurrido y Python lanza la excepción:
    ValueError: invalid literal for int() with base 10: '305.23'
'''   

# Ejemplo de excepción: NameError.
resultado = variable * 5.2
'''
En este caso, si se usa un IDE, se marcará una advertencia de que 
la variable está indefinida. Sin embargo, dejará ejecutar el programa 
pero, al ejecutarse, se lanzará la excepción:
    NameError: name 'variable' is not defined
'''

# Ejemplo de excepción: IndexError.
mes = 'mayo'
print(mes[4])
'''
Se intenta imprimir el carácter que está en la posición 4 de 'mayo'. 
Pero teniendo en cuenta que la indexación de los caracteres se hace 
a partir de la posición 0, la posición 4 en 'mayo' no existe, está 
fuera del rango de la cadena y, por lo tanto, lanza la excepción:
    IndexError: string index out of range
'''

# Ejemplo de excepción: TypeError.
resultado = numero // 'algo'
'''
En la operación se intenta dividir un número por una cadena de 
caracteres y, al ocurrir el error, se lanza la excepción:
    TypeError: unsupported operand type(s) for //: 'int' and 'str'
'''


