# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.11
Genera el número espejo de un número de 5 dígitos: a partir del dato dado
se obtiene otro número con sus dígitos colocados de derecha a izquierda.
"""

numero = int(input('Ingrese un número entero positivo de 5 dígitos: '))
if numero >= 10000 and numero <= 99999:    
    nuevo_numero = 0
    temporal = numero    
    for _ in range(1, 6):  
        digito = temporal % 10
        nuevo_numero = nuevo_numero * 10 + digito
        temporal = temporal // 10        
    print(f'\n{numero} --> {nuevo_numero}')
else:
    print('\nEl dato no está dentro del rango esperado.')