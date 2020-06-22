# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.28
Encuentra e imprime el MCD (máximo común divisor) 
de dos números enteros positivos.
"""


numero1 = int(input('\nIngrese el primer número entero positivo: '))
numero2 = int(input('Ingrese el segundo número entero positivo: '))
bandera = True
mcd = 1
if numero1 >= numero2:
    divisor = numero2 // 2
else:
    divisor = numero1 // 2    
while bandera and divisor >= 1:
    if numero1 % divisor == 0 and numero2 % divisor == 0:
        mcd = divisor
        bandera = not bandera
    divisor -= 1    
print(f'\nEl MCD de {numero1} y {numero2} es: {mcd}')