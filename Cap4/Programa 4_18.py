# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.18
Calcula e imprime el factorial de un número entero positivo. 
"""

numero = int(input('Ingrese un número entero positivo: '))
if numero > 0:
    factorial = 1      
    for valor in range(numero, 1, -1):  # Uso de un for decreciente.
        factorial *= valor        
    print(f'El factorial de {numero} es = {factorial}')
else:
    print(f'\nError en el dato.'.upper())