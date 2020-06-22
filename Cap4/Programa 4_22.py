# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.22
Genera e imprime los términos de la serie:
    1	5	8	12	15	19	22	26	29	…	3100 (o el menor que corresponda)
También imprime la suma de esos términos.
"""

termino = 1  # Siempre empieza en 1.
# Se va a generar a partir del segundo término.
suma_terminos = termino  
suma4 = True
while termino <= 3100:
    print(termino,' ', end = '')
    if suma4:
        termino += 4
    else:
        termino += 3
    suma_terminos += termino
    suma4 = not suma4    
print(f'\nLa suma de los términos es = {suma_terminos}')
    