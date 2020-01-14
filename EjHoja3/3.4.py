'''Ejercicio 4. Crea una matriz de 3x3, rellena sus celdas de números aleatorios e imprímela por pantalla tal que así:
	x x x
	x x x
	x x x'''

import random

col = 3
rows = 3
matrix = [[random.randrange(0,100) for j in range(col)]for i in range(rows)]

for i in range(rows):
    print (matrix[i])


