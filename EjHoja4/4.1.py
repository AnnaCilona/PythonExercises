'''Ejercicio 1. Desarrolla un juego de “hundir la flota” para jugar contra el ordenador. El ordenador colocará inicialmente sus barcos en su tablero sin mostrarlos por pantalla
para que el usuario no conozca su ubicación. Le pedirá al usuario que introduzca
información sobre la ubicación de sus barcos (los del usuario). Ambos jugarán con el mismo número de barcos y de las mismas dimensiones.
Y se procederá a jugar por turnos, repitiendo disparo si se acierta y perdiendo el turno si el proyectil cae en una casilla en la que haya “agua”.
Tras cada jugada, se mostrará información al usuario sobre la situación de su tablero, y sobre la situación que conoce del tablero del ordenador
(es decir, sólo los disparos que ha hecho, sobre qué posición y sus aciertos y errores). La estrategia a utilizar por el ordenador para ganar,
se deja en manos de cada desarrollador y se puede hacer tan sofisticada como se desee. No está permitido que el ordenador utilice información sobre
la situación de los barcos del adversario, se supone que el juego es limpio.
Desarrollar dos versiones del ejercicio. La primera con barcos de una sola casilla, y la segunda con barcos de más de una casilla (dos, tres... definid este campo por parámetros).'''


import random

ganar=False
tamanyoTablero=3


def muestraSitu():
    print("Tu tablero")
    for i in range (tamanyoTablero):
        print(tabUser[i])
    print("Tablero del adversario")
    for i in range (tamanyoTablero):
        print(tabUserOrd[i])
    
        
def disparar():
    barcoHundido=0
    perder=False
    while not perder:
        fila=int(input("Dispara a la casilla\nFila: "))               #   *libre  ºdisparo al agua  Xhundido    
        col=int(input("Columna:  "))
        if tabOrdenador[fila][col]=="*":
            print("---------Le has dado al agua---------\n")
            tabOrdenador[fila][col]="º"
            tabUserOrd[fila][col]="º"
            muestraSitu()
            perder=True
        else:
            print("---------¡Barco hundido! Dispara de nuevo---------")
            tabOrdenador[fila][col]="X"
            tabUserOrd[fila][col]="X"
            muestraSitu()
            barcoHundido=barcoHundido+1
        if barcoHundido==3:
            print("~~~~~~~~~~¡Has ganado el partido!~~~~~~~~~~")
            perder=True
            ganar=True
            return ganar
            break

tabOrdenador = [["*" for y in range(tamanyoTablero)]for z in range(tamanyoTablero)]
tabUser=[["*" for y in range(tamanyoTablero)]for z in range(tamanyoTablero)]
tabUserOrd=[["*" for y in range(tamanyoTablero)] for z in range(tamanyoTablero)]

for i in range(0,4):
    fila=random.randint(0,tamanyoTablero-1)
    col=random.randint(0,tamanyoTablero-1)
    tabOrdenador[fila][col]="O"
    
for i in range(0,4):
    fila=int(input("Escribe las coordenadas de la casilla donde posicionar tu barco\nFila: "))
    col=int(input("Columna:  "))
    tabUser[fila][col]="U"

print("\nTu tablero")    
for i in range (tamanyoTablero):
    print(tabUser[i])

print("\nOrdenador") 
for i in range (tamanyoTablero):
    print(tabOrdenador[i])
   

while not ganar:
    disparar()


    





