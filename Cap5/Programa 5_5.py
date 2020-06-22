# -*- coding: utf-8 -*-
"""
@author: guardati
Pruebas realizadas a las funciones pedidas en los problemas 5.6,
5.7 y 5.8. 
"""

import archivos


# CP1: escritura en archivo de varios números (problema 5.6).
archivos.escribe_archivo('precios', 12.5, 8.3, 98.45, 10.45, 11, 24.30 )

# CP2: se usa el archivo creado para probar las 2 versiones de la 
# función de lectura de un archivo (problema 5.7). Se espera el mismo resultado.
leido1 = archivos.lee1_archivo('precios')
leido2 = archivos.lee2_archivo('precios')
print(f'\nDatos leídos con la solución 1\n{leido1}')
print(f'\nDatos leídos con la solución 2\n{leido2}')

# CP3: se usa un archivo que contiene solo números.  
archivos.escribe_archivo('archivo1', 12.5, 5, 4, 0, 8.7, -2)  
print('Resultado de contar y sumar:', archivos.cuenta_y_suma('archivo1'))

# CP4: se usa un archivo que contiene distintos tipos de datos (problema 5.8).
archivos.escribe_archivo('archivo2', 12.5, 5, 'hola', 0, 8.7, -2, True)  
resultado = archivos.cuenta_y_suma('archivo2')
print(f'\nHay {resultado[0]} números y su suma es {resultado[1]}')

# CP5: se proporciona el nombre de un archivo que no existe (problema 5.8).
try:  
    print(archivos.cuenta_y_suma('archivo3'))
except FileNotFoundError as error:
    print(f'\n{error}')
    








    

    
        