# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.28
Determina e imprime si un empleado es candidato o no para hacerse
cargo de un puesto dentro de la empresa. 
"""

clave = input('Ingrese clave del empleado: ')
categoria = int(input('Ingrese categoría: '))
antiguedad = int(input('Ingrese antigüedad: '))
respuesta = False
if categoria == 3 or categoria == 5:
    if antiguedad >= 5:
        respuesta = True
elif categoria == 2 and antiguedad >= 10:
    respuesta = True   
if respuesta:
     resultado = 'reúne las características para el puesto.'
else:
    resultado = 'no reúne las características para el puesto.'
print(f'\nEl empleado con clave {clave} ' + resultado)    
