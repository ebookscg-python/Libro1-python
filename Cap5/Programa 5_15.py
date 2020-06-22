# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.18
Determina si dos palabras son anagramas.
"""

def es_anagrama(pal1, pal2):  
    """ Determina si dos palabras son anagramas.
    Parámetros:
        pal1: de tipo str. 
        pal2: de tipo str.  
    Regresa:
        True si son anagramas, False en caso contrario.
    """
    n = len(pal1)
    if n == len(pal2):      
        indice = 0
        anagrama = True
        while indice < n and anagrama:
            try:
                pos = pal2.index(pal1[indice])
                pal2 = pal2[0: pos] + pal2[pos+1:]
            except:
                anagrama = False
            indice += 1
    else:
        anagrama = False
    return anagrama and len(pal2) == 0

# =============================================================================
# Algunas pruebas de la función es_anagrama
# =============================================================================
# CP1: se dan dos palabras que son anagramas.
if es_anagrama('frase', 'fresa'):
    print('\nCP1: "frase y fresa" son anagramas.')
else:
    print('\nCP1: "frase y fresa" no son anagramas.')
# CP2: se dan dos palabras que no son anagramas.
if es_anagrama('mar', 'arena'):
    print('CP2: "mar y arena" son anagramas.')
else:
    print('CP2: "mar y arena" no son anagramas.')
# CP3: se dan dos palabras que no son anagramas.
if es_anagrama('aparta', 'raptar'):
    print('CP3: "aparta y raptar" son anagramas.')
else:
    print('CP3: "aparta y raptar" no son anagramas.')
# CP4: se dan dos cadenas vacías.
if es_anagrama('', ''):
    print('CP4: dos cadenas vacías son anagramas.')
else:
    print('CP4: dos cadenas vacías no son anagramas.')
 