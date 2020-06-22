# -*- coding: utf-8 -*-

"""
@author: guardati
Ejemplo 4_1
Ciclo for usando la función range().
"""

# El valor por omisión para el tercer parámetro de range() es 1.
for numero in range(1, 10):
    print(numero)  # Imprime del 1 al 9.
    
# El valor por omisión para el primer parámetro de range() es 0.
for j in range(4):
    print(j)  # Imprime del 0 al 3.    

cadena = ''  # Cadena de caracteres vacía
# Se usa _ cuando la variable de control no se necesita en el ciclo.
for _ in range (10):  
    cadena += '*'  # Pega 10 * a la variable cadena.
print(cadena)  # Imprime **********

# En range() se especifica un incremento diferente de 1.
for numero in range(1, 10, 2):  
    print(numero)  # Imprime: 1 3 5 7 y 9.
    
'''
El tercer parámetro de range() es un incremento negativo o un decremento.
En este caso, el valor inicial debe ser mayor que el final, para 
que el for se ejecute, al menos, 1 vez.
'''
for numero in range(10, 1, -2):
    print(numero)  # Imprime: 10 8 6 4 y 2.
    
    