'''Ejercicio 1. Un marinero ebrio se tambalea al subir por una rampa del muelle a su barco.
La rampa tiene 5 pasos de ancho y 15 de largo. 
Comenzamos a observar al marinero cuando está en el extremo de la rampa que se apoya sobre el muelle,
comenzando a caminar hacia el barco por el centro de la rampa. 
Si da más de dos pasos a la izquierda o a la derecha, caerá al agua y se ahogará,
pero si da más de 15 pasos hacia delante estará a salvo a bordo de su barco. 
Escribe un programa para simular el irregular avance del marinero según estas instrucciones:
	a. El programa lee repetidamente un entero del teclado. 
	b. Si el entero es negativo, supondremos que el pirata se durmió sobre la rampa. 
	c. Si el entero es divisible entre 2, el pirata da un paso hacia adelante.
	d. Si el entero no es divisible entre 2, pero el entero menos 1 es divisible entre 4,
el pirata da un paso a la derecha. 
	e. En otro caso, el pirata da un paso a la izquierda. 
	f. El programa finalizará escribiendo el paradero del pirata:
cae por un costado y se ahoga, logra abordar su barco o se duerme sobre la rampa. 
Debe de ir detallando cada acción que acomete.'''

contadorLargo=0
contadorAncho=0
ancho=5
largo=15

    
while (contadorLargo<=16
       ) and (contadorAncho<=6):
    opcion=int(input("Escribe un número\n"))
    if opcion<0:
        print("El pirata se durmió sobre la rampa")
        break
    elif opcion%2==0:
        print("El pirata da un paso hacia adelante\n")
        contadorLargo=contadorLargo+1
        if contadorLargo>=15:
            print("El pirata logra abordar el barco")
            break
    elif opcion%2!=0 and ((opcion-1)%4==0):
        print("El pirata da un paso a la derecha\n")
        contadorAncho=contadorAncho+1    
        if contadorAncho>=3:
            print("El pirata cae por un costado y se ahoga")
            break
    else:
        print("El pirata da un paso a la izquierda\n")
        contadorAncho=contadorAncho+1



