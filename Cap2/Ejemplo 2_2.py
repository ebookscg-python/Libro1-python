# -*- coding: utf-8 -*-
"""
@author: guardati
Ejemplo 2_2
Operaciones con números complejos.
Cada complejo se expresa por medio de un par ordenado: a + bj, 
siendo a la parte real y b la parte imaginaria.
"""

z1 = complex(input('Ingrese un complejo: '))
z2 = z1 
print('\nEl valor de z2 es:', z2)

# Otra forma de asignar un complejo.
z3 = complex(2.5, -6.2)
print('\nEl valor de z3 es:', z3)

# Ejemplo de las operaciones de +, -, * y / entre complejos.
print(f'\nSuma: {z1 + z2}')
print(f'Resta: {z1 - z2}')
print(f'Multiplicación: {z1 * z2:.2f}')
print(f'División: {z1 / z2}')

print('\nLa parte real es:', z1.real)
print('La parte imaginaria es:', z1.imag)

# Operaciones entre complejos y entre complejos con no complejos.
z4 = z1 + 2.5  # Suma 2.5 a la parte real de z1.
z5 = z1 + 2.5 + 3.2j  # Suma a z1 el complejo (2.5 + 3.2j).
# Suma 1.8 a la parte imaginaria de z1.
z6 = z1 + 1.8j  
# Producto escalar: 4 por la parte real y 4 por la imaginaria.
z7 = 4 * z1  
print('\nComplejos obtenidos:', z4, z5, z6, z7)

# Se comparan las partes reales y las partes imaginarias entre sí.
print('\n¿Los complejos son iguales?', z1 == z2)

# Valor absoluto:  |z1| = sqrt(z1.real**2 + z1.imag**2)
print(f'\nEl valor absoluto es: {abs(z1):.3f}')  