# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 1_3
Impresiones en Python usando el método format().
"""

edad = 83
# Imprime el texto y el valor de la variable ocupando 5 espacios.
print("Edad del abuelo: {0:5d}".format(edad))  # Argumento posicional.   
print("Edad del abuelo: {edad:5d}".format(edad = 88))  # Argumento nombrado.   

'''
Al dato indicado con el 0 lo sustituye el numero1 y al indicado con el 1, 
el numero2 multiplicado por 20. Es decir, primero se multiplica y el 
resultado es el que se imprime. Se reservan 10 espacios y el resultado 
se imprime justificado a derecha.
'''
numero1 = 1258
numero2 = 8920
# Argumentos posicionales.
print('{0:1d} {1:10d}'.format(numero1, numero2 * 20))  
# Argumentos nombrados.
print('{numero1:1d} {numero2:10d}'.format(numero1 = 1234, numero2 = 987)) 
precio = 2.23
# Deja 3 decimales: completa con 0.
print("El precio del pan es: ${0:.3f}".format(precio))   
# Reserva 10 espacios para el número y justifica a derecha.
print("El precio del pan es: ${0:10.3f}".format(precio))   
print("El precio de la fruta es: ${fruta:.2f}".format(fruta = 12.5)) 

'''
En el primer ejemplo se usan argumentos nombrados, ya que entre {}
se da el nombre del argumento que se incluirá en esa posición.
En el segundo ejemplo se utilizan argumentos posicionales;
es decir, se indica con un número si se debe reemplazar con el
primer dato, el segundo, etc.
'''
print('Este {herramienta} es de color {color}.'.format(herramienta = 'martillo', color = 'gris'))
print('Este {0} es de color {1}.'.format('martillo', 'gris'))

# Al usar dos veces {0} se utiliza la palabra martillo en ambas posiciones.
print('Este {0} es de color {0}.'.format('martillo', 'gris'))

'''
Ejemplo usando variables en lugar de constantes.
En este caso solo se pueden usar argumentos posicionales.
'''
animal1 = "gatos"
animal2 = "perros"
print('Existe la creencia de que los {0} y los {1} no pueden convivir.'.format(animal1, animal2))
