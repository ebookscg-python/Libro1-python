# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 3_4
Manejo de excepciones.
"""

'''
Si el valor ingresado se puede convertir a entero, entonces se 
calcula y se despliega su cuadrado. En caso contrario se despliega 
un mensaje indicando que hubo un error.
'''
try:
    numero = int(input('Ingrese un número entero: '))
    print('El cuadrado del número es:', numero ** 2)
except ValueError:
    print('\nError: el dato ingresado no se pudo convertir a entero.')
       
'''   
Si la cadena de caracteres tiene una longitud > a 0, entonces 
se muestra la inicial; es decir el carácter de la posición 0. 
En caso contrario se despliega un mensaje de error, ya que una 
cadena vacía no tiene un elemento en la posición 0.
'''
nombre = input('Ingrese el nombre de la persona: ')
try:
    print('La inicial es: ', nombre[0])
except IndexError:
    print('\nIngresó una cadena vacía. No hay inicial.')

'''
Se intenta convertir a números reales a los datos ingresados y 
posteriormente dividirlos. Sin embargo puede suceder un error al 
convertirlos (si no son números) o al dividirlos (si el segundo es 0).
En este caso las 2 excepciones que se manejan se escriben como una tupla.
''' 
numerador = input('Ingrese el numerador: ')
denominador = input('Ingrese el denominador: ')
try:
    numero1 = float(numerador)
    numero2 = float(denominador)
    resultado = numero1 / numero2
    print(f'\nEl resultado de la división es: {resultado:.2f}')
except (ValueError, ZeroDivisionError):
    print('\nDato no numérico o el denominador es un cero.')
  
'''
Otra manera de escribir el bloque except es como se muestra más abajo. 
Así se puede ser más explícito al indicar qué hacer en caso de error, 
especialmente si se requieren acciones diferentes según la excepción 
ocurrida.
'''
try:
    numero1 = float(numerador)
    numero2 = float(denominador)
    resultado = numero1 / numero2
    print(f'\nEl resultado de la división es: {resultado:.2f}')
except ValueError:
    print('\nAlguno de los datos no es un número.')
except ZeroDivisionError:
    print('\nEl denominador es un cero.')

'''
Cuando no interese precisar el tipo de excepción, el bloque del 
except se puede quedar vacío.
'''
try:
    numero1 = float(numerador)
    numero2 = float(denominador)
    resultado = numero1 / numero2
    print(f'\nEl resultado de la división es: {resultado:.2f}')
except:
    print('\nUn error ha ocurrido.'.upper())
