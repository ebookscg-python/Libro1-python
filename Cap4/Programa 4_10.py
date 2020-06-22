# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.10
Imprime, dígito por dígito, un número de 4 dígitos.
"""

numero = int(input('Ingrese un número entero de 4 dígitos: '))
if numero >= 1000 and numero <= 9999:
    denominador = 1000
    for _ in range(1, 5):  
        digito = numero // denominador
        print(digito, ' ', end = '')
        numero = numero % denominador
        denominador //= 10
else:
    print('El número ingresado no está en el rango esperado.')