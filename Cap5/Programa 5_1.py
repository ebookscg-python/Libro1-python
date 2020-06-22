# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.1
"""

def es_primo(numero):
    """ Determina si un número es primo o no.
    
    Parámetro:
        número: es de tipo int o float y > 0.
    Regresa:
        True si el número es primo o False en caso contrario.
    """
    primo = False
    if numero == 2:
        primo = True
    else:
        # Descarta el 1 y todos los pares > 2.
        if numero > 2 and numero % 2 != 0:  
            divisor = 3
            limite = numero // 2            
            while divisor < limite and numero % divisor != 0:
                divisor += 2                
            if divisor >= limite:
                primo = True                
    return primo

#========================================================
# Algunos usos de la función.
#========================================================

# Determina si un número es o no primo (problema 4.30).
dato = int(input('\nIngrese un número entero positivo: '))
if dato <= 0:
    print('\nError en el dato.')
else:
    if es_primo(dato):
        print(f'El número {dato} sí es un número primo')
    else:
        print(f'El número {dato} no es un número primo')     
        
# Encuentra todos los primos hasta el valor dado (problema 4.34).
valor = int(input('\nIngrese hasta qué valor quiere analizar: '))
if valor <= 0:
    print('\nError en el dato.')
else:
    for numero in range(2, valor + 1):
        if es_primo(numero):
            print(f'El número {numero} sí es un número primo')   
        
# Encuentra todos los primos gemelos hasta el valor dado (problema 4.37).
valor = int(input('\nIngrese hasta qué valor quiere encontrar primos gemelos: '))
if valor <= 0:
    print('\nError en el dato.')
else:
    print('\nLista de pares de primos gemelos:')
    primo_anterior = 0
    for numero in range(3, valor + 1, 2):
        if es_primo(numero):
            if numero - primo_anterior == 2:
                print(f'{primo_anterior} - {numero}'.center(30))
            primo_anterior = numero
            
        
            
        
