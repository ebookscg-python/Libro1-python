# -*- coding: utf-8 -*-
"""
@author: guardati
Solución del problema 3.20
Cacula e imprime el total a pagar en un hotel, de acuerdo al tipo de 
habitación ocupada y a la cantidad de días de hospedaje.
"""

dias_hospedaje = int(input('Ingrese el total de días de la estadía: '))
tipo_habitacion = input('Ingrese el tipo de habitación ocupada: ')
tipo_habitacion = tipo_habitacion.upper()
if tipo_habitacion == 'S':
    precio = 1500
elif tipo_habitacion == 'D':
    precio = 2100
elif tipo_habitacion == 'T':
    precio = 2700
elif tipo_habitacion == 'F':
    precio = 3500
else:
    precio = -1  # Si se ingresó un tipo equivocado de habitación.   
''' Si precio es -1 se obtendrá un valor negativo el cual se imprimirá 
y deberá interpretarse como una alarma de que hubo un error en los datos.
En otras secciones y capítulos se verán mejores alternativas para manejar
este tipo de errores. '''
total_pagar = precio * dias_hospedaje
print(f'\nEl total a pagar en el hotel = ${total_pagar:.2f}')