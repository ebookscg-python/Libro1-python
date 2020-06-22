# -*- coding: utf-8 -*-
"""
@author: guardati
Problema 3.24
Calcula e imprime la retención del impuesto sobre la renta, así como
el ingreso neto que cobrará un contribuyente.
El impuesto sobre la renta se calcula de acuerdo a los ingresos y a la 
cantidad de dependientes económicos a cargo que tenga el contribuyente.
"""

ingreso = float(input('Proporcione el ingreso correspondiente: $'))
num_dependientes = int(input('Ingrese el número de dependientes económicos: '))
if ingreso <= 20000:
    porcentaje = 0
elif ingreso <= 40000:
    porcentaje = 0.15
elif ingreso <= 70000:
    porcentaje = 0.25
else:
    if ingreso <= 100000:
        porcentaje = 0.3
    else:
        porcentaje = 0.35
    if num_dependientes > 4:
        porcentaje -= 0.02    
retencion = ingreso * porcentaje
ingreso_neto = ingreso - retencion 
print(f'\nRetención: ${retencion:.2f} \nIngreso neto: ${ingreso_neto:.2f}')
