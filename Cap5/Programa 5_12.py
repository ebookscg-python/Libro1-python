# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.15
Obtiene e imprime todos los pares de números amigos comprendidos entre
dos valores dados por el usuario.
Dos números son amigos si la suma de los divisores del primero (sin incluirlo)
es igual al segundo y, a su vez, la suma de los divisores del segundo 
(sin incluirlo) es igual al primero. 
"""
import auxiliar

liminf = int(input('\nIngrese límite inferior: '))
limsup = int(input('Ingrese límite superior: '))
if liminf > 0 and liminf < limsup:
    print(f'\nNúmeros amigos en el rango: {liminf} - {limsup}'.upper())
    for num1 in range(liminf, limsup):
        for num2 in range(num1 + 1, limsup + 1): 
            suma1 = auxiliar.suma_divisores(num1)
            suma2 = auxiliar.suma_divisores(num2)
            if suma1 == num2 and suma2 == num1:
                print(num1, '-', num2)
else:
    print('\n¡Intervalo incorrecto!'.upper())
