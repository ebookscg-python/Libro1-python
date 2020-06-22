# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_4
Alcance de variables.
"""

def func1(x):
    x = x + 2  # Se modifica el valor del parámetro formal.
    print(f'Desde func1, el valor de x = {x}')  
    
def func2():
    x = 'rojo'  # x es variable local a la función.
    z = x + 'blanco'
    print(f'Desde func2, el valor de x = {x}')
    print(f'Desde func2, el valor de z = {z}')
   
x = 5
print(f'Valor de x = {x}')  # Imprime 5
func1(x)
print(f'Valor de x = {x}')  # Imprime 5
func2()
print(f'Valor de x = {x}')  # Imprime 5