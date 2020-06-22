# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.13
"""


def convierte_a_binario(numero):
    """ Convierte un número entero positivo a binario.
    
    Parámetro:
        numero: de tipo int, > 0.
    Regresa:
        La notación binaria del número recibido. Es de tipo int. 
    Lanza:
        ValueError: cuando el dato no es entero o > 0.
    """
    if type(numero) == int and numero > 0:
        binario = 0
        potencia = 1
        while numero >= 2:
            digito = numero % 2
            numero = numero // 2
            binario = binario + digito * potencia
            potencia = potencia * 10
        binario = binario + numero * potencia
        return binario
    raise ValueError('El dato no es un número entero o no es positivo.')

# CP1: se proporciona un número entero positivo.
print('\nCP1 --> Notación binaria de 2:', convierte_a_binario(2))
# CP2: se proporciona un número entero positivo.
print('CP2 --> Notación binaria de 254897:', convierte_a_binario(254897))
# CP3: se proporciona un número real.
try: 
    print('CP3 --> Notación binaria de 6.5:', convierte_a_binario(6.5))
except ValueError as error:
    print('CP3 -->', error)    
# CP4: se proporciona un número entero negativo.
try: 
    print('CP4 --> Notación binaria de -8:', convierte_a_binario(-8))
except ValueError as error:
    print('CP4 -->', error)
