# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.27
Calcula e imprime un estimado del total a pagar en un hospital, en concepto de
internación de un paciente. Para el cálculo se considera el tipo de enfermedad,
la cantidad de días y la edad del paciente.
"""

edad = int(input('Edad del paciente: '))
tipo = int(input('Tipo de enfermedad (valor entre 1 y 4): '))
dias = int(input('Número estimado de días de internación: '))
if tipo == 1:
    costo_diario = 3150
elif tipo == 2:
    costo_diario = 3980
elif tipo == 3:
    costo_diario = 5500
elif tipo == 4:
    costo_diario = 7150
else:
    costo_diario = 0    
if costo_diario == 0:
    print('\nEl tipo de enfermedad ingresado es incorrecto'.upper())
else:
    costo_internacion = costo_diario * dias
    if edad < 16:
        costo_internacion *= 1.08
    elif edad > 70:
        costo_internacion *= 1.17
    print(f'\nCosto estimado a pagar: ${costo_internacion:.2f}')
