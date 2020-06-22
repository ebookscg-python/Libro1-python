
# -*- coding: utf-8 -*-
"""

@author: guardati
Solución del problema 4.17
Calcula e imprime la suma de los números impares comprendidos entre 39 y 181.
Note que en este problema no se ingresan datos. 
"""

suma_impares = 0
'''
En el for se usa un incremento de 2 lo cual resulta en que la variable numero 
es siempre un número impar: 39, 41, 43, etc. De esta manera evitamos evaluar si 
el número es o no impar adentro del for.
'''
for numero in range(39, 182, 2):
    suma_impares += numero        
print(f'\nLa suma de los impares entre 39 y 181 es = {suma_impares}')