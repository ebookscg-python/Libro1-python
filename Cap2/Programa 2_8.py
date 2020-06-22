# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.8
Calcula e imprime el total de: yardas, rods cuadrados, acres, 
homesteads y millas cuadradas que equivalen una cierta cantidad de hectáreas.
"""

ha = float(input('Ingrese total de hectáreas de la estancia: '))
yarda2 = ha * 10000 / 0.83612736
rod2 = yarda2 / 30.25
acre = rod2 / 160
homestead = acre / 160
milla2 = homestead / 4
print('\nLa estancia tiene:'.upper())
print(f'{yarda2:14.2f} yardas cuadradas')
print(f'{rod2:14.2f} rods cuadrados')
print(f'{acre:14.2f} acres')
print(f'{homestead:14.2f} homesteads')
print(f'{milla2:14.2f} millas cuadradas')
