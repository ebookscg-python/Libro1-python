# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.37
Encuentra e imprime todos los números primos gemelos comprendidos 
en el intervalo de 1 a un valor dado por el usuario.
"""

valor = int(input('\nIngrese hasta qué valor quiere analizar: '))
if valor <= 0:
    print('¡Error en el dato!'.upper())
else:
    print('\nLista de pares de primos gemelos:')
    primo_anterior = 0
    # Descarta los pares y el número primo 2.
    for numero in range(3, valor + 1, 2):     
        divisor = 3
        limite = numero // 2   
        while divisor < limite and numero % divisor != 0:
            divisor += 2                    
        if divisor >= limite:  # Demuestra que el número es primo.
            if numero - primo_anterior == 2:
                print(f'{primo_anterior} - {numero}'.center(30))
            primo_anterior = numero
 