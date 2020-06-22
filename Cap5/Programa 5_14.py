# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 5.17
Calcula, con la ayuda de la función calcula_edad(), e imprime la edad
de una persona a partir de su fecha de nacimiento.
"""

import auxiliar

fecha_nac = input('\nIngrese fecha de nacimiento (dd/mm/aaaa): ')
pos = fecha_nac.index('/')
dia = int(fecha_nac[0:pos])
fecha_nac = fecha_nac[pos + 1:]
pos = fecha_nac.index('/')
mes = int(fecha_nac[0:pos])
anio = int(fecha_nac[pos + 1:])
edad = auxiliar.calcula_edad((dia, mes, anio))
print('\nAños cumplidos al día de hoy:', edad)



