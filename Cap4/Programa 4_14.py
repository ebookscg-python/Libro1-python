# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.14
Obtiene e imprime el total de divisores que tiene un número entero.
"""

numero = int(input('Ingrese un número entero positivo: '))
if numero > 0:
    cuenta_divisores = 1  # El 1 divide a todos los números.
    limite = numero // 2 + 1    
    for divisor in range(2, limite):  # Se empieza a partir de 2.
        if numero % divisor == 0:
            cuenta_divisores += 1            
    if numero > 1:
        cuenta_divisores += 1  # Cuenta al mismo número como 1 de sus divisores.    
    print(f'\nTotal de divisores de {numero} es = {cuenta_divisores}')
else:
    print('\nSe espera un número positivo')