# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 5_1
Funciones muy simples.
"""

'''
Función que genera un saludo personalizado.
Recibe un nombre como parámetro.
No regresa ningún resultado, por eso no aparece el return.
'''
def saluda(nombre):
    print('\nHola', nombre)
     
'''
Función que regresa el mayor de 2 números.
Recibe dos números como parámetros.
Regresa el mayor de los números.
'''
def encuentra_mayor(numero1, numero2):
    if numero1 > numero2:
        mayor = numero1
    else:
        mayor = numero2
    return mayor

'''
Función que lee y regresa un entero, asegurándose que el 
dato dado es un número entero.
Recibe un mensaje como parámetro.
Regresa el número entero leído.
'''
def lee_entero(mensaje):
    bandera = True
    while bandera:
        try:
            entero = int(input(mensaje))
            bandera = False
        except:
            print('solo se aceptan números enteros.'.upper())
    return entero

# =============================================================================
# Pruebas de las funciones.
# =============================================================================
# Se llama a la función con el nombre de la persona a saludar.
saluda('Juan')
# Imprime el valor None, ya que la función no regresa un resultado.
print(saluda('Antonio'))
               
# Se proporcionan los datos que deben compararse.
# El resultado se despliega junto al mensaje que está a la izquierda.
precio1 = 25.3
precio2 = 18.6
print('\nEl mayor es:', encuentra_mayor(precio1, precio2))

# Se proporciona el mensaje que debe mostrarse cuando se pide el dato.
# El resultado obtenido por la función se guarda en las variables.
anio_construc_museo = lee_entero('¿En qué año fue construido el museo? ')
anio_construc_estadio = lee_entero('¿En qué año fue construido el estadio? ')

