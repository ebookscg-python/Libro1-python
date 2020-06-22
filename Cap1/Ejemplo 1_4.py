# -*- coding: utf-8 -*-

"""
@author: guardati
Ejemplo 1_4
Impresiones en Python usando f-string.
"""

valor = 'edad'
edad = 83
print(f'La {valor} del abuelo es {edad} años')

valor = 'altura'
altura = 1.72   
print(f'La {valor} del abuelo es {altura:.1f} m')  # Da formato al número.

nombre = 'Alberto'
print(f'Mi abuelo se llama {nombre}.')

# El !r provoca que el valor de nombre se escriba entre ''.
print(f'Te dije que se llama {nombre!r}.')  # Se verá 'Alberto'.

# Con <10 se reservan 10 espacios para el valor de la variable.
formato1 = f'{valor:<10} = {altura:.2f}' 
print(formato1)

formato2 = f'{valor!r:<10} = {altura:.2f}'  
print(formato2)

# Ejemplo combinando f-string con formato de cadenas.
formato3 = f'{"peso".capitalize()} = {59.605:.2f}'  
print(formato3)
