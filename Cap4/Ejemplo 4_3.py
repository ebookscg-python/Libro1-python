# -*- coding: utf-8 -*-
"""

@author: guardati
Ejemplo 4_3
Solución del problema 4.1 sin usar ciclo.
En este caso se emplea una sola variable para leer el sueldo, 
lo cual implica que se debe leer y sumar 10 veces.
"""

nomina = 0
sueldo = float(input('Ingrese el sueldo 1: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 2: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 3: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 4: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 5: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 6: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 7: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 8: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 9: $'))
nomina += sueldo
sueldo = float(input('Ingrese el sueldo 10: $'))
nomina += sueldo
print('\nLa nómina que debe pagarse es: $', nomina)
