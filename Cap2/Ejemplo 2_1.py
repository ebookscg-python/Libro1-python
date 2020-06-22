# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_1
Manejo de cadenas de caracteres.
"""

# Asignación de cadenas que ocupan una sola línea.
cadena1 = 'enero'
cadena2 = "febrero"

# Asignación de cadenas que ocupan más de una línea.
cadena3 = '''Esto es un ejemplo de una cadena muy larga que ocupa más 
de una línea. En estos casos se requiere usar tres comillas dobles o 
tres comillas simples. Fin del ejemplo.'''
cadena4 = """Esto es un ejemplo de una cadena muy larga que ocupa más 
de una línea. En estos casos se requiere usar tres comillas dobles o 
tres comillas simples. Fin del ejemplo."""

# Para incluir " en la cadena se deben usar las simples para encerrar la cadena.
cadena5 = '¿Por qué siempre saludas haciendo gestos "feos"?'

# Para incluir ' en la cadena se debe preceder por el caracter \.
cadena6 = 'Juan dijo: "Creo que Mc\'Gregor es un buen hombre."'

# Para concatenar o unir dos cadenas se usa el operador +.
cadena7 = cadena1 + cadena2
cadena7 = cadena1 + ' ' + cadena2  # Deja un espacio entre las dos cadenas.

# Para repetir una cadena se usa el operador *.
cadena8 = 3 * 'agua' 
print(cadena8)
cadena8 = 3 * 'agua ' 
print(cadena8)
cadena8 = 3 * 'agua' + ' '
print(cadena8)
cadena8 = 3 * ('agua' + ' ') 
print(cadena8)

# Indexación de cadenas.
print(cadena1[0])  # Imprime el primer carácter de la cadena.
print(cadena1[-1])  # Imprime el último carácter de la cadena.

# Slicing (con positivos).
print(cadena1[0:3])  # Imprime ene.
print(cadena1[:4])  # Valor inicial por omisión: 0. Imprime ener.
print(cadena1[3:])  # Valor final por omisión: la longitud. Imprime ro.
print(cadena1[:])  # Toma del 0 a la longitud -1. Imprime enero.
print(cadena1[::2])  # Igual anterior, tomando de 2 en 2. Imprime eeo.

# Slicing (con negativos).
cadena2 = 'ABCDEFGHIJKLMNOP'
# Subcadena formada por el último caracter.
print(cadena2[-1:])  # Imprime P.
# Subcadena formada por toda la cadena en orden inverso.
print(cadena2[::-1])  # Imprime PONMLKJIHGFEDCBA.
# Igual a la anterior pero excluye los últimos 9 caracteres.
print(cadena2[-10::-1])  # Imprime GFEDCBA.
# Subcadena formada por los últimos 4 caracteres, en orden inverso.
print(cadena2[:-5:-1])  # Imprime PONM.

# Ejemplo del uso de algunos de los métodos de cadenas.
cadena9 = 'hoy está lloviendo'

# Método capitalize: convierte a mayúscula la primera letra.
print(cadena9.capitalize())

''' Método para centrar, justificar a izquierda y justificar a derecha.
El entero indica la cantidad de espacios reservados para la cadena y, 
por lo tanto, se centra o justifica de acuerdo a esos espacios.'''
print(cadena9.center(30))  # Centra la cadena con respeto a 30 espacios.
print(cadena9.ljust(30))  # Justifica a izquierda la cadena con respeto a 30 espacios.
print(cadena9.rjust(30))  # Justifica a derecha la cadena con respeto a 30 espacios.

# El segundo parámetro indica el carácter con cual se completan los n espacios.
print(cadena9.center(30, '*'))
print(cadena9.ljust(30, '*'))
print(cadena9.rjust(30, '*'))

# Regresa el total de veces que una cadena está en otra cadena.
print(f'Total de veces que aparece la palabra "comillas" es = {cadena3.count("comillas")}')


''' Busca la cadena recibida en la cadena que llama al método y 
regresa la posición de esta. Si no la encuentra regresa -1. '''
print(cadena3.find('comillas'))  # Busca de izquierda a derecha.
print(cadena3.rfind('comillas'))  # Busca de derecha a izquierda.

''' Busca la cadena recibida en la cadena que llama al método y 
regresa la posición de esta.
Si no la encuentra lanza el error: ValueError: substring not found.'''
print(cadena3.index('comillas'))  # Busca de izquierda a derecha.
print(cadena3.rindex('comillas'))  # Busca de derecha a izquierda.

''' Métodos que ayudan a comprobar la naturaleza de los datos almacenados en 
la cadena. Se presentan solo algunos de los que tiene Python.'''
print(cadena1.isalpha())  # Imprime True ya que cadena1 es alfabética.
print(cadena1.isdigit())  # Imprime False ya que cadena1 no está formada por dígitos.
print('205'.isalpha())  # Imprime False ya que la cadena no es alfabética.
print('205'.isdigit())  # Imprime True ya que la cadena está formada por dígitos.

# Determina si las letras de la cadena son solo minúsculas.
print('esto es un ejemplo'.islower())  # Regresa True.

# Determina si las letras de la cadena son solo mayúsculas.
print('esto es un ejemplo'.isupper())  # Regresa False.
print('JUJUY'.isupper())  # Regresa True.

# Determina si la cadena está formada solo por espacios.
print(cadena1.isspace())  # Regresa False.
print('    '.isspace())  # Regresa True.

# Regresa el total de caracteres que forman la cadena (la longitud).
print('La longitud de la cadena es = ', len(cadena4))
print(len(''))  # Regresa 0, es una cadena vacía. 

# Convierte todas las letras de la cadena a minúsculas.
print('JUJUY'.lower())

# Convierte todas las letras de la cadena a mayúsculas.
print(cadena1.upper())

# Reemplaza a la cad1 por la cad2, si está y todas sus ocurrencias.
print(cadena1.replace('e', '*'))  # Imprime *n*ro.
print(cadena1.replace('p', '*'))  # Imprime enero.

# Determina si una cadena empieza/termina con una subcadena.
print(cadena8.startswith('agua'))  # Regresa True.
print(cadena8.endswith('agua'))  # Regresa False porque termina agua y un espacio
cadena8 = cadena8[0:len(cadena8) - 1]  # Se recorta la cadena8, suprimiendo el espacio.
print(cadena8.endswith('agua'))  # Regresa True.

# Reemplaza mayúsculas por minúsculas y viceversa.
print('Esto es UNa mezcla horrible de MayúSCulas Y minúSCULAS'.swapcase())

# Escribe la primera letra de cada palabra en mayúsculas.
print('las venas abiertas de américa latina'.title())