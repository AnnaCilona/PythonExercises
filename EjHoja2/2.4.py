'''Ejercicio 4. Escribe un programa que calcule cuál es la letra que corresponde con un determinado número de DNI.'''


listaLetras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

dni=int(input("Introduce el NIF\n"))

print("Tu letra es: " + (listaLetras[dni%23]))
