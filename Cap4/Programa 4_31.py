# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 4.31
Calcula el valor de π con una precisión menor o igual a 0.0000001, 
utilizando la serie:
    π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9-… 
"""

import math
print('\nValor de π dado por Python:', math.pi)

valor_pi = 4
termino = 4
signo = -1
denominador = 3
while termino > 0.0000001:
    termino = 4 / denominador
    valor_pi += termino * signo
    signo *= -1
    denominador += 2
print(f'\nEl valor de π calculado: {valor_pi}')