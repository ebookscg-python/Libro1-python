# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.30
Determina si un número es primo o no.
"""

numero = int(input('\nIngrese un número entero positivo: '))
if numero <= 0:
    print('\nError en el dato.')
else:   
    if numero == 2:
        primo = True
    else:
        primo = False
        # Descarta el 1 y todos los pares > 2.
        if numero > 2 and numero % 2 != 0:  
            divisor = 3
            limite = numero // 2           
            while divisor < limite and numero % divisor != 0:
                divisor += 2                
            if divisor >= limite:
                primo = True                
    if primo:
        print(f'\nEl número {numero} es un número primo.')
    else:
        print(f'\nEl número {numero} no es un número primo.')