# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.15
Obtiene e imprime la corriente de un circuito de corriente alterna, 
con base en el voltaje y la impedancia (E = IxZ).
"""

voltaje = complex(input('Ingrese el voltaje del circuito: '))
impedancia = complex(input('Ingrese la impedancia del circuito: '))
corriente = voltaje / impedancia
print(f'\nLa corriente es: {corriente}')