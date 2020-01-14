'''Ejercicio 2. Construye un programa que muestre el resultado de un partido de tenis entre dos jugadores A y B. 
Para ello se introducirá inicialmente el número máximo de sets que se podrán disputar en el partido y,
sucesivamente el ganador de cada uno de los juegos del partido. 
Un partido de tenis se basa en la disputa de juegos. Cada juego es ganado por uno de los jugadores.
Si un jugador logra hacerse con un número suficiente de juegos, gana un set, y con el número suficiente de sets, gana el partido.
Cuando un jugador gana un set, se inicia la disputa del siguiente set comenzando ambos jugadores desde 0 juegos. 
Un jugador gana un set, si anota 6 juegos y el rival tiene 4 o menos, o si anota 7 juegos, dando igual los que tenga el contrincante.
Se gana el partido si se consiguen la mitad más uno de los sets en juego. Es decir, si el partido es a 3, hay que ganar 2, y si es a 5, basta con 3.
Hay que ir leyendo una secuencia de A y B que nos va indicando qué jugador va ganando cada juego,
e ir escribiendo un mensaje tras ello, indicando que el jugador ha ganado el juego y el resultado parcial del partido (sets y juegos).
Al final hay que indicar quién ha ganado y terminar el programa.'''

parcialJuegoA=0
parcialJuegoB=0
listaJuegosA=[]
listaJuegosB=[]
setA=0
setB=0
numSets=0

numSets=int(input("Introduce el número máximo de sets por partido: \n"))
while True:
    ganadorJuego=input("\nQuién gana este juego?\n a.Jugador a\n b.Jugador b\n")
    if ganadorJuego=="a" :
        parcialJuegoA=parcialJuegoA+1
        print("El jugador a ha ganado el juego\n")
        print("******Resultado parcial del partido:\n","Sets:",setA, "-", setB, "\n","Juegos:", parcialJuegoA, "-", parcialJuegoB)
    elif ganadorJuego=="b" :
        parcialJuegoB=parcialJuegoB+1
        print("El jugador b ha ganado el juego")
        print("******Resultado parcial del partido:\n","Sets:",setA, "-", setB, "\n","Juegos:", parcialJuegoA, "-", parcialJuegoB)
    if (parcialJuegoB<=4 and parcialJuegoA==6) or parcialJuegoA==7:
        print("El jugador a ha ganado el set")
        setA=setA+1
        listaJuegosA.append(parcialJuegoA)
        listaJuegosB.append(parcialJuegoB)
        parcialJuegoA=0
        parcialJuegoB=0
        print("******Resultado parcial del partido:\n","Sets:",setA, "-", setB, "\n","Juegos:", parcialJuegoA, "-", parcialJuegoB)  
    elif (parcialJuegoA<=4 and parcialJuegoB==6) or parcialJuegoB==7:
        print("El jugador b ha ganado el set")
        setB=setB+1
        listaJuegosA.append(parcialJuegoA)
        listaJuegosB.append(parcialJuegoB)
        parcialJuegoA=0
        parcialJuegoB=0
        print("******Resultado parcial del partido:\n","Sets:",setA, "-", setB, "\n","Juegos:", parcialJuegoA, "-", parcialJuegoB) 
    if  (setA>=((int)(numSets/2))+1):
        print("*-*-*-*-*-*El jugador a gana el partido: ", listaJuegosA[0],"-",listaJuegosB[0], ",", listaJuegosA[1],"-",listaJuegosB[1], ",", listaJuegosA[2],"-",listaJuegosB[2])
        break
    elif (setB>=((int)(numSets/2))+1):
        print("*-*-*-*-*-*El jugador b gana el partido: ", listaJuegosA[0],"-",listaJuegosB[0], ",", listaJuegosA[1],"-",listaJuegosB[1], ",", listaJuegosA[2],"-",listaJuegosB[2])
        break



    
