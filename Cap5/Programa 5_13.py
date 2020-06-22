# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.16
Encuentra e imprime todos los números primos de, al menos, 2 dígitos cuyos 
espejos también sean números primos. El usuario debe ingresar los extremos
del intervalo.
Se dice que un número es el espejo de otro cuando está formado por los mismos 
dígitos, pero en orden inverso.
"""
import auxiliar

liminf = int(input('\nIngrese límite inferior: '))
limsup = int(input('Ingrese límite superior: '))
if liminf > 9 and liminf < limsup:
    print(f'\nNúmeros primos y sus espejos primos: '.upper())
    if liminf % 2 == 0:
        liminf += 1
    for num in range(liminf, limsup + 1, 2):
        if auxiliar.es_primo(num):
            espejo = auxiliar.genera_espejo(num)
            if auxiliar.es_primo(espejo):
                print(num, '-', espejo)
else:
    print('\n¡Intervalo incorrecto!'.upper())