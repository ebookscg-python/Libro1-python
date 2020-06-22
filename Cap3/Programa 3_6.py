# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.6
Determina si una persona tiene problemas de bajo peso usando el 
Indice de Masa Corporal.
    IMC = al peso dividido la estatura al cuadrado. 
Si es así, imprime un mensaje adecuado.
"""

peso = float(input('Ingrese el peso de la persona en kilos: '))
estatura = float(input('Ingrese la altura de la persona en metros: '))
IMC = peso / estatura ** 2
if IMC < 18.5:
    print('\nSí tiene problemas de bajo peso. Busque ayuda.')
