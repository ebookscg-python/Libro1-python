# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.34
Encuentra e imprime todos los números primos comprendidos 
en el intervalo de 1 a un valor dado por el usuario.
"""

valor = int(input('\nIngrese hasta qué valor quiere analizar: '))
if valor <= 0:
    print('\nError en el dato.')
else:
    if valor >= 2:  # Descarta el 1.
        print('\nEl número 2 es un número primo.')
        for numero in range(3, valor + 1, 2):  # Descarta los pares.       
            divisor = 3
            limite = numero // 2                
            while divisor < limite and numero % divisor != 0:
                divisor += 2                    
            if divisor >= limite:
                print(f'El número {numero} es un número primo.')
    else:
        print('\nNo hay números primos.')
       