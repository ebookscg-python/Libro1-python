# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.3
Calcula e imprime la suma de los números pares y el promedio 
de los números impares.
"""

n = int(input('Ingrese la cantidad de números a procesar: '))
suma_pares = 0
suma_impares = 0
cuenta_impares = 0
for i in range (1, n + 1):
    numero = int(input(f'Ingrese el número {i}: '))
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
        cuenta_impares += 1        
print('\nSuma de los números pares =', suma_pares)         
if cuenta_impares > 0:
    promedio = suma_impares / cuenta_impares   
    print(f'Promedio de los números impares = {promedio:.2f}')
else:
    print('\nNo es posible calcular el promedio de los números impares.')



