'''Ejercicio 1. Desarrolla el juego del tic-tac-toe. Al entrar deberá mostrar dos opciones, jugar contra un humano o contra la máquina. En un tablero de 3x3 vacío incialmente,
cada jugador irá colocando sus fichas.
En caso de la máquina, tendremos que simular su movimiento. Puedes complicarte en su "inteligencia" todo lo que desees,
siendo el resultado óptimo que la máquina nunca pueda perder, siempre gane o empate, y siendo el resultado más básico generar movimientos aleatorios para la máquina.
Una partida consta de un número par de juegos. Cada vez empezará un jugador. En cada juego se cuenta el número de 3 en raya que ha sido capaz de hacer cada jugador.
El juego lo gana quien más 3 en raya haya hecho. La partida la gana aquel que sea el primero en superar al otro en dos victorias (es decir, dos juegos de ventaja).'''


from Juego import Juego

myJuego=Juego()

myJuego.menu()

            
