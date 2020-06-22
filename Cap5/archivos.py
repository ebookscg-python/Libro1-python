# -*- coding: utf-8 -*-
"""
@author: guardati
Módulo archivos.py
Agrupa varias funciones auxiliares en el manejo de archivos.

Funciones:
    escribe_archivo: escribe en un archivo los elementos recibidos.
    lee1_archivo: regresa el contenido de un archivo de texto.
    lee2_archivo: regresa el contenido de un archivo de texto.
    cuenta_y_suma: regresa cuantos números hay en un archivo y la suma de estos.
"""

# Solución del problema 5.6
def escribe_archivo(arch, *args):
    """ Crea un archivo y guarda en líneas diferentes cada 
    uno de los valores recibidos por medio del parámetro args.
    
    Parámetro:
        arch: de tipo str. Nombre con el que se creará el archivo.
        *args: parámetro de longitud variable.
     """
    arch = open(arch, 'w')
    for val in args:
        arch.write(str(val))
        arch.write('\n')
    arch.close()

# Solución del problema 5.7 - alternativa 1
def lee1_archivo(arch):
    """ Regresa el contenido del archivo llamado arch.
    
    Parámetro:
        arch: de tipo str. Nombre del archivo que debe leerse.
    regresa:
        El contenido del archivo con formato de str.
    Lanza: 
        FileNotFoundError: cuando no se puede abrir el archivo.
    """
    try:
        lee = open(arch, 'r')
        linea = lee.read();  # Se lee todo el contenido del archivo.
        lee.close()
        return linea
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())
    
# Solución del problema 5.7 - alternativa 2
def lee2_archivo(arch):
    try:
        lee = open(arch, 'r')
        cadena = ''
        for val in lee:  # Itera sobre el archivo.
            cadena += val
        lee.close()
        return cadena
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())
 
# Solución del problema 5.8
def cuenta_y_suma(arch):
    """ Regresa total de números guardados en un archivo y la suma de estos.
    
    Parámetro:
        arch: de tipo str. Nombre del archivo que debe leerse.
    Regresa:
        El total de números leídos y su suma. Es de tipo tuple. 
    Lanza: 
        FileNotFoundError: cuando no se pudo abrir el archivo.
    """
    try:
        lee = open(arch, 'r')
        suma = 0
        cuenta = 0
        for val in lee:  # Itera sobre el archivo.
            try:
                suma += float(val)  # El dato es un número: se +.
                cuenta += 1
            except:  # No es número: se pasa al siguiente dato.  
                continue  
        lee.close()
        return (cuenta, suma)
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())
