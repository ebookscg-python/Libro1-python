# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 4.26
Calcula el total de votos y porcentaje para cada uno de los 4 
candidatos, de acuerdo con una encuesta sobre intención de votos.
"""

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
voto = int(input('\nIngrese número del candidato (1, 2, 3, 4): '))
while voto != -1:
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    voto = int(input('Ingrese número del candidato al que votará (1, 2, 3, 4): '))    
total_votos = votos_candidato1 + votos_candidato2 + votos_candidato3 + votos_candidato4
if total_votos > 0:    
    porcentaje_cand1 = votos_candidato1 / total_votos * 100
    porcentaje_cand2 = votos_candidato2 / total_votos * 100 
    porcentaje_cand3 = votos_candidato3 / total_votos * 100
    porcentaje_cand4 = votos_candidato4 / total_votos * 100
    print(f'\nTotal de intenciones de votos para el candidato 1:'
          f' {votos_candidato1}')
    print(f'Representa un: {porcentaje_cand1:.2f}% del total.')
    print(f'\nTotal de intenciones de votos para el candidato 2:'
          f' {votos_candidato2}')
    print(f'Representa un: {porcentaje_cand2:.2f}% del total.')
    print(f'\nTotal de intenciones de votos para el candidato 3:'
          f' {votos_candidato3}')
    print(f'Representa un: {porcentaje_cand3:.2f}% del total.')
    print(f'\nTotal de intenciones de votos para el candidato 4:'
          f' {votos_candidato4}')
    print(f'Representa un: {porcentaje_cand4:.2f}% del total.')
else:
    print('\nNo hay datos que analizar.')