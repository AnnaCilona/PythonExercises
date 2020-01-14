'''Ejercicio 16. Escriba un programa que lea por teclado 20 números reales
y calcule su media.
Hacerlo sin utilizar 20 variables reales.'''

lista=[]

contador=0

print ("Escribe 20 numeros:\n")

for i in range(0,20):
    n = int(input("num :"))
    contador=contador+n
    lista.append(n)

print ("La media de los números introducidos es: ", (contador/20))
