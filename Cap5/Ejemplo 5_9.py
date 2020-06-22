# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_9
Uso de la instrucción with.
"""

# El archivo se cierra automáticamente.
def escribe_archivo(archivo, *args):
    """ Crea un archivo y guarda en líneas diferentes cada uno 
    de los valores recibidos por medio del parámetro args.
    
    Parámetro:
        archivo: de tipo str. Nombre con el que se creará el archivo.
        *args: parámetro de longitud variable.
     """
    with open(archivo, 'w') as arch:        
        for val in args:
            arch.write(str(val))
            arch.write('\n')

# Se prueba la función que utiliza el with.
escribe_archivo('prueba_with', 'a', 'b', 'c', 'd', 'e', 'f', 'g')

