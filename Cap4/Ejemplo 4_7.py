# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 4_7
Algunos usos de las instrucciones break y continue.
"""

'''
El ciclo permite hacer tantas lecturas como sean necesarias para 
obtener un número mayor que 0. Observe que solo cuando se cumpla 
esta condición se ejecutará el break interrumpiendo el ciclo.
'''
print('\nOpción 1: uso de break'.upper())
while True:
    numero = int(input('Ingrese un número entero positivo: '))
    if numero > 0:
        break;
        
print('\nOpción 2: sin usar break y usando una selección'.upper())
bandera = True
while bandera:
    numero = int(input('Ingrese un número entero positivo: '))
    if numero > 0:
        bandera = False
        
print('\nOpción 3: sin usar break y usando doble lectura'.upper())
numero = int(input('Ingrese un número entero positivo: '))
while numero <= 0:
    numero = int(input('Ingrese un número entero positivo: '))
      
'''
Ejemplo del uso de las instrucciones continue y break.
El continue se usa para no evaluar los números fuera de rango y los pares. 
El break se usa para interrumpir el ciclo solo cuando el usuario ya no quiera 
seguir buscando números primos mayores que 100.
'''
print('\n\nOpción 1: uso de break y continue'.upper())
while True:
    numero = int(input('Ingrese un número entero positivo > 100: '))
    # Descarta los fuera de rango y los pares.
    if numero <= 100 or numero % 2 == 0:  
        continue  # Inicia nuevamente el ciclo.
    divisor = 3
    limite = numero // 2 
    while divisor <= limite and numero % divisor != 0:
        divisor += 2            
    if divisor >= limite:
        print(f'El {numero} es un número primo')
    respuesta = input('Quiere evaluar otro número: SI/NO ').upper()
    if respuesta.upper() == 'NO': 
        break  # Interrumpe el ciclo.

print('\n\nOpción 2: sin usar el break y continue'.upper())
respuesta = input('Quiere evaluar un número: SI/NO ').upper()
while respuesta.upper() != 'NO':
    numero = int(input('Ingrese un número entero positivo > 100: '))
     # Descarta los fuera de rango y los pares.
    if numero > 100 and numero % 2 != 0: 
        divisor = 3
        limite = numero // 2 
        while divisor <= limite and numero % divisor != 0:
            divisor += 2        
        if divisor >= limite:
            print(f'El {numero} es un número primo')
        respuesta = input('Quiere evaluar otro número: SI/NO ').upper()
    
                     