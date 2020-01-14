'''Ejercicio 21. Escriba un programa que muestre por pantalla todos los divisores de un número. '''

num=int(input("Escribe un número:\n"))
lista= []

for i in range (1,(num+1)):
    if (num%i==0):
        lista.append(i)
    i=i+1

print("Los divisores de ", num, " son: ", lista)
