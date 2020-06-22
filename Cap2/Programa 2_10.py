# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 2.10
Calcula e imprime el total a pagar por alimento, a lo largo de un mes,
en un refugio para perros en el cual viven perros de distinta edad y tamaño.
Se considera que el mes tiene 30 días.
"""

precio_alim_ad = float(input('Ingrese el precio del alimento para adulto: $')) 
precio_alim_ca = float(input('Ingrese el precio del alimento para cachorro: $')) 
''' 
Se multiplica por 30 para obtener el consumo en un mes y se divide
por 1000 para expresar el consumo en kilos. 
'''
consumo_kg_adulto = (10 * 450 + 12 * 380) * 30 / 1000
consumo_kg_cachorro = 6 * 230 * 30 / 1000
costo_alim_ad = consumo_kg_adulto * precio_alim_ad
costo_alim_ca = consumo_kg_cachorro * precio_alim_ca
print(f'\nTotal a pagar por el alimento para perros adultos = ${costo_alim_ad:.2f}')
print(f'Total a pagar por el alimento para perros cachorros = ${costo_alim_ca:.2f}')