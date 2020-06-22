# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_2
Parámetros de tipos inmutables.
"""

# Parámetro numérico (inmutable).
def f1(numero):
    numero = numero ** 2
    print("\nNúmero desde f1:", numero)  

# Parámetro cadena de caracteres (inmutable).
def f2(cadena):
    cadena = cadena.upper()
    print("\nFrase desde f2:", cadena)
    
# ========================================================
# Pruebas de las funciones.
# ========================================================
numero = 5    
f1(numero)
print("Número luego de llamar a f1:", numero) 
frase = 'hoy es un día soleado'    
f2(frase)
print("Frase luego de llamar a f2:", frase)
