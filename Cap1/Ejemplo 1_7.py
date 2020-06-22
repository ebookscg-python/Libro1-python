# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_7
Lectura (ingreso) de datos por medio del teclado.
"""

print("\n¿Cómo te llamas? ")  # Se solicita el nombre por medio de un print().
nombre = input()

# Se solicita el lugar de residencia incluyendo un mensaje en el input().
ciudad = input("¿Dónde vives? ")

# Se solicita la edad. En este caso será necesario convertir a
# entero el dato ingresado. 
edad = int(input("¿Cuántos años tienes? "))

# Se solicita la altura en metros. Se convierte a real el dato ingresado.
altura = float(input("¿Cuánto mides -en metros? "))

# Se muestran todos los datos leídos.
print(f'\nLa persona de nombre {nombre} vive en {ciudad}.'
      f'\nTiene {edad} años y mide {altura} m')