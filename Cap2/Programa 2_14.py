# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 2.14
Modifica e imprime una cadena que contiene el nombre completo de 
una persona, dejándolo expresado de la siguiente manera: 
    primer apellido segundo apellido, nombre.
Vamos a suponer que el nombre y los apellidos no son compuestos y que se 
proporcionan separados por un solo espacio. Por ejemplo:
    Juan Pérez Pérez
"""

nombre_completo = input('Ingrese el nombre completo de la persona: ')
# Primer espacio: separa el nombre del primer apellido.
espacio = nombre_completo.find(' ')  
# Se extrae el nombre de la persona.  
nombre = nombre_completo[0:espacio]  
# Se pierde el nombre de pila.
nombre_completo = nombre_completo[espacio+1:]  
# Segundo espacio: separa el primer apellido del segundo.
espacio = nombre_completo.find(' ')    
# Se extrae el primer apellido.
primer_apellido = nombre_completo[0:espacio]  
# Se pierde el primer apellido.
segundo_apellido = nombre_completo[espacio+1:]  
nombre_completo = primer_apellido + ' ' + segundo_apellido + ', ' + nombre
print(nombre_completo)