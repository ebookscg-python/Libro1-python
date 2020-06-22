# -*- coding: utf-8 -*-
"""

@author: guardati
Solución del problema 2.9
Calcula e imprime el equivalente en euros, dólares americanos, 
dólares canadienses y francos suizos de una cierta cantidad 
dada en pesos mexicanos.
"""

pesos = float(input('Ingrese precio de venta del auto: $'))
euros = pesos * 0.045
dolares_ame = pesos * 0.051
dolares_can = pesos * 0.068
francos_sui = pesos * 0.050
print(f'Los ${pesos:10.2f} equivalen a: EUR{euros:10.2f}, U$S{dolares_ame:10.2f},' 
      f' C${dolares_can:10.2f} y Fr{francos_sui:10.2f}')