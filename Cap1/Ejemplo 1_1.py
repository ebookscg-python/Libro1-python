# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_1
Impresiones en Python.
"""

edad = 83
print("Hola otoño")   
print('Edad del abuelo: ', edad)   
# Por omisión separa con espacio en blanco.
print("verde", "rojo", "azul")   
# Se establece como separador el -
print("verde", "rojo", "azul", sep = "-")  
# Se establece como separador el --> 
print("verde", "rojo, amarillo o café", "se cae", sep = " --> ")  
# Por omisión termina con un salto de línea. 
print("dulce", "amargo", "ácido")   
# Se establece que, al terminar, no baje de renglón.
print("Hola", end = "")   
# Se establece que, al terminar, no baje de renglón y escriba :)
print('otoño, estación de los colores opacos', end = ":)")   

