# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.10
"""

def genera_reporte(arch_ent, arch_sal):
    """ Genera un reporte del año y sede de los últimos Juegos 
    Olímpicos, de acuerdo con las especificaciones dadas 
    (quitar datos duplicados y colocar mayúsculas).
    
    Parámetro:
        arch_ent: de tipo str. Indica el nombre del archivo que almacena 
        los datos de los Juegos Olímpicos, con errores.
        arch_sal: de tipo str. Indica el nombre del archivo donde se 
        guardará el reporte solicitado.
    Lanza:
        FileNotFoundError: si no se pudo abrir el archivo.
    """ 
    try:
        lee = open(arch_ent, 'r')
        escribe = open(arch_sal, 'w')
        escribe.write('Últimos Juegos Olímpicos\n'.upper())
        for juego in lee:
            posicion = juego.find(' ')
            anio = juego[0: posicion]
            juego = juego[posicion + 1:]
            posicion = juego.rfind(' ')
            ciudad = juego[0: posicion]
            escribe.write(anio + ' ---- ' + ciudad.title() + '\n')
        lee.close()
        escribe.close()
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el archivo.'.upper())

# ==========================================================================
# Se prueba la función. En este caso se creó un archivo con los 
# datos de las últimas 9 olimpíadas.
# ==========================================================================
genera_reporte('juegos', 'Reporte_olimpico')