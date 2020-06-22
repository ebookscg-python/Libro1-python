# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.13
Genera e imprima la tabla de multiplicar desde 1 hasta el valor de un
número ingresado por el usuario.
"""

numero = int(input('Ingrese un número entero: '))
print(f'\nTabla de multiplicar del {numero} hasta el {numero}\n'.upper())
for valor in range(1, numero + 1):
    print(f'{valor} x {numero} = {valor * numero:5d}')