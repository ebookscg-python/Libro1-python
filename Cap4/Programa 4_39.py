# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.39
Encuentra e imprime todos los números deficientes comprendidos en el 
intervalo de 1 a un valor dado por el usuario.
"""

valor = int(input('\nIngrese hasta qué valor quiere analizar: '))
if valor <= 0:
    print('¡Error en el dato!'.upper())
else:
    print('\nLista de números deficientes:')
    # Se descarta el 1, no puede ser deficiente.
    for numero in range(2, valor + 1):  
        suma_divisores = 1  # El 1 divide a todos.   
        for divisor in range(2, numero // 2 + 1):
            if numero % divisor == 0:
                suma_divisores += divisor            
        if suma_divisores < numero:
            print(f'El {numero} es un número deficiente.')