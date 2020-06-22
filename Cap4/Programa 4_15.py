# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.15
Calcula e imprime la suma y el promedio de todos los números comprendidos 
entre dos números enteros que representan el límite inferior y el 
superior del intervalo de números que deben procesarse.
"""

entero1 = int(input('Ingrese el primer número entero: '))
entero2 = int(input('Ingrese el segundo número entero: '))
if entero1 <= entero2:  # Garantizamos que, por lo menos, haya un número que sumar.
    suma = 0    
    for numero in range(entero1, entero2 + 1):
        suma += numero        
    total_numeros = entero2 - entero1 + 1
    promedio = suma / total_numeros
    print(f'\nLa suma de los números comprendidos entre {entero1} y {entero2}'
          f' es = {suma}')
    print(f'El promedio es = {promedio:.2f}')
else:
    print('\nError en los datos.')