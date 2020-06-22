# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.16
Calcula e imprime el resultado de la serie:
    1 + 1/2 - 1/3 + ...(+ -) 1/n
"""

numero = int(input('Ingrese un número entero positivo: '))
if numero > 0:
    suma = 1
    signo = 1    
    for valor in range(2, numero + 1):
        suma += 1 / valor * signo
        signo *= -1        
    print(f'El resultado de la serie es = {suma:.2f}')
else:
    print(f'\nError en el dato.'.upper())