# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.29
Encuentra e imprime el mínimo común múltiplo (mcm) de dos 
números enteros positivos.
"""

numero1 = int(input('\nIngrese el primer número entero positivo: '))
numero2 = int(input('Ingrese el segundo número entero positivo: '))
if numero1 > 0 and numero2 > 0:    
    if numero1 >= numero2:
        mcm = numero1 * 2
        numero = numero1
    else:
        mcm = numero2 * 2
        numero = numero2    
    while mcm % numero1 != 0 or mcm % numero2 != 0:
        mcm += numero    
    print(f'\nEl mcm de {numero1} y {numero2} es = {mcm}')
else:
    print('Los datos ingresados no son números positivos.')