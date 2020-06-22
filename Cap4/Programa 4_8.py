# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.8
Calcula e imprime:
    - el término número doceavo de la serie de Fibonacci.
    - la suma de los primeros doce términos de la serie de Fibonacci.
"""

fibo_ant1 = 0
fibo_ant2 = 1
suma_terminos = fibo_ant2
for _ in range(3, 13):  # Llega hasta el 12.  
    fibonacci = fibo_ant1 + fibo_ant2
    suma_terminos += fibonacci
    fibo_ant1 = fibo_ant2
    fibo_ant2 = fibonacci    
print('\nTérmino 12 de la serie de Fibonacci:', fibonacci)
print('Suma de los primeros 12 términos de la serie de Fibonacci:', suma_terminos)
    
