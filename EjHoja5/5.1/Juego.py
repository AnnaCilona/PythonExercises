'''Ejercicio 1. Desarrolla el juego del tic-tac-toe. Al entrar deberá mostrar dos opciones, jugar contra un humano o contra la máquina. En un tablero de 3x3 vacío incialmente,
cada jugador irá colocando sus fichas.
En caso de la máquina, tendremos que simular su movimiento. Puedes complicarte en su "inteligencia" todo lo que desees,
siendo el resultado óptimo que la máquina nunca pueda perder, siempre gane o empate, y siendo el resultado más básico generar movimientos aleatorios para la máquina.
Una partida consta de un número par de juegos. Cada vez empezará un jugador. En cada juego se cuenta el número de 3 en raya que ha sido capaz de hacer cada jugador.
El juego lo gana quien más 3 en raya haya hecho. La partida la gana aquel que sea el primero en superar al otro en dos victorias (es decir, dos juegos de ventaja).'''

class Juego:
    import Variables
    tablero = Variables.tablero
    tamanyoTablero = Variables.tamanyoTablero
    
    def __init__(self):
        pass

    def menu(self):
        salir=False
        while not salir:
            opcion=int(input("Elige tu adversario:\n 1) Otro humano\n 2) Ordenador\n"))
            if opcion==1:
                print("Has elegido jugar contra otro humano")
                self.jugarJuegos()
                salir=True
            elif opcion==2:
                print("Vas a jugar contra el ordenador")
                self.jugarOrdenador()
                salir=True
            else:
                print("Elige entre opción 1 o 2")

    def setTablero(self):
        tamanyoTablero=3        
        self.tablero=[["■" for x in range(tamanyoTablero)]for y in range(tamanyoTablero)]

    def muestraTablero(self):
        for i in range (self.tamanyoTablero):
            for j in range (self.tamanyoTablero):
                print(self.tablero[i][j], end=' ')
            print()

    def jugarJuegos(self):
        juegosO=0
        juegosX=0
        numJuegos=0
        turnos=True
        tamanyoTablero = self.tamanyoTablero
        self.muestraTablero()
        while numJuegos!=4:
            if turnos:
                print("Es el turno del jugador X")
                fila=int(input("Mueve tu ficha a la casilla\nFila: "))
                col=int(input("Columna: "))
                if self.tablero[fila][col]=="■":
                    self.tablero[fila][col] ="X"
                    self.muestraTablero()
                else:
                    print("Casilla ocupada")
                if self.ganaJuego(self.tablero, jugador="X"):
                    juegosX=juegosX+1
                    numJuegos=numJuegos+1
                    self.setTablero()
                    self.muestraTablero()
                    continue
                else:
                    turnos=False
            else:                
                print("Es el turno del jugador O")
                fila=int(input("Mueve tu ficha a la casilla\nFila: "))
                col=int(input("Columna: "))
                if self.tablero[fila][col]=="■":
                    self.tablero[fila][col] ="O"
                    self.muestraTablero()
                else:
                    print("Casilla ocupada")
                if self.ganaJuego(self.tablero, jugador= "O"):
                    juegosO=juegosO+1
                    numJuegos=numJuegos+1
                    self.setTablero()
                    self.muestraTablero()
                    turnos=False
                else:
                    turnos=True
        if juegosO>juegosX:
            print("******Fin del partido: gana jugador O")
        elif juegosX>juegosO:
            print("******Fin del partido: gana jugador X")
        else:
            print("******Fin del partido\n Empate\n JugadorX: " , juegosX , "\nJugadorO: " , juegosO)
        
        
            
    def ganaJuego(self, tablero , jugador):
        if tablero[0][0]==tablero[0][1]==tablero[0][2]==jugador: 
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[1][0]==tablero[1][1]==tablero[1][2]==jugador:
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[2][0]==tablero[2][1]==tablero[2][2]==jugador:
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[0][0]==tablero[1][0]==tablero[2][0]==jugador:
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[0][1]==tablero[1][1]==tablero[2][1]==jugador:
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[0][2]==tablero[1][2]==tablero[2][2]==jugador: 
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[0][0]==tablero[1][1]==tablero[2][2]==jugador: 
            print("*********************" + jugador + " gana el juego")
            return True
        elif tablero[0][2]==tablero[1][1]==tablero[2][0]==jugador:
            print("*********************" + jugador + " gana el juego")
            return True
        else:
            return False

    def jugarOrdenador(self):
        