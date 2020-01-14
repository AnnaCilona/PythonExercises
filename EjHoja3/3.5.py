'''Ejercicio 5. Dada la matriz anterior, haz que un usuario seleccione una casilla. Ese valor se deberá convertir a cero y repintar de nuevo la matriz.'''


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


filaCorrecta=False
colCorrecta=False

while not filaCorrecta:
    fila=int(input("Escribe las coordenadas de la casilla que eliges: \n Fila: "))
    if fila<rows:
        filaCorrecta=True
    else:
        print("Error, te has salido de la matriz")

while not colCorrecta:     
    columna=int(input(" Columna: "))
    if columna<col: 
        colCorrecta=True
    else:
        print("Error, te has salido de la matriz")

print("Has elegido la casilla: ","(",fila,",",columna,")")           
matrix[fila][columna]=0
        
for i in range(rows):
    print (matrix[i])



