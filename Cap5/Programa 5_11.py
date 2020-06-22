# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.14
Obtiene e imprime los primeros n (n > 0) números primos cuya representación 
binaria es un palíndromo. 
"""
import auxiliar

n = int(input('\n¿Cuántos primos con notación binaria palíndroma quiere calcular? '))
contador = 0
numero = 3 # Se descartan los números pares.
while contador < n:
    if auxiliar.es_primo(numero):
        binario = auxiliar.convierte_a_binario(numero)
        if auxiliar.es_palindromo(binario):
            print(numero, '-', binario)
            contador += 1
    numero += 2


