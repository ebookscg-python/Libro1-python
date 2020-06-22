# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.36
Genera e imprime una secuencia de números con la forma:
    
1												
1	2	1										
1	2	3	2	1								
1	2	3	4	3	2	1						
1	2	3	4	5	4	3	2	1				
1	2	3	4	5	6	5	4	3	2	1		
1	2	3	4	5	6	7	6	5	4	3	2	1
"""


limite = int(input('\nIngrese un número entero positivo: '))
if limite <= 0:
    print('\nError en el dato.')
else:
    for numero in range(1, limite + 1):
        for valor in range(1, numero + 1):
            print(valor, ' ', end = '')
        for valor in range(numero - 1, 0, -1):
            print(valor, ' ', end = '')
        print()  # Provoca un salto de línea.