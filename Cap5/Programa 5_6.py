# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.9
"""
import lecturas

def guarda_calificaciones(nom_arch, total):
    """ Guarda las calificaciones leídas por terminal en un archivo de texto. 
    En la primera línea guarda el total y cada calificación se escribe en una 
    línea diferente.
    
    Parámetro:
        nom_arch: de tipo str. Indica el nombre del archivo que se creará.
        total: de tipo int. Indica el total de calificaciones a 
        guardar en el archivo.
    """    
    arch_calif = open(nom_arch, 'w')  # Se abre para escritura.
    arch_calif.write(str(total) + '\n')  
    for i in range(1, total + 1):
        mensaje = 'Ingrese la calificación '+ str(i) + ': '
        cal = lecturas.lee_numero_positivo(float, mensaje)
        # Para que quede una calificación por línea.
        arch_calif.write(str(cal) + '\n')  
    arch_calif.close()
    
def calcula_promedio(nom_arch):
    """ Calcula y regresa el promedio de los valores  
    guardados en un archivo de texto.
    
    Parámetro:
        nom_arch: de tipo str. Indica el nombre del archivo 
        del cual se leerán los datos.
    Regresa:
        El promedio de los datos almacenados en el archivo. De tipo float.
    Lanza:
        FileNotFoundError: cuando no se pudo abrir el archivo.
        ValueError: cuando hubo algún error en los datos.        
    """ 
    try:
        archivo = open(nom_arch, 'r')
        suma = 0
        contador = int(archivo.readline())
        for _ in range(1, contador + 1):
            cal = float(archivo.readline())
            suma += cal
        archivo.close()
        return suma / contador
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())
    except (ValueError, ZeroDivisionError):
        raise ValueError('Error en los datos.'.upper())
        
#===============================================================
# Uso de las funciones para resolver el problema.
#===============================================================
archivo = input('Nombre del archivo donde guardar las calificaciones: ')
total = lecturas.lee_numero_positivo(int, '¿Cuántas calificaciones? ')
guarda_calificaciones(archivo, total)

# Importante si la creación del archivo se hizo en otro programa.
archivo = input('Nombre del archivo de calificaciones: ')
try:
    print(f"\nPromedio = {calcula_promedio(archivo):.2f}")
except Exception as error:
    print(error)