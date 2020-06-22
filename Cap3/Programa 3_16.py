# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.16
Calcula e imprime el valor de la función de acuerdo a los datos ingresados.
"""

k = int(input('Ingrese el valor de k: '))
x = float(input('Ingrese el valor de x: '))
if k == 1:
    resultado = x / 5
elif k == 2 or k == 3:
    resultado = x ** 2
elif k == 4:
    resultado = x ** 3 + 5
else:
    resultado = x ** 0.5    
print(f'\nF(x) = {resultado:.2f}')           
