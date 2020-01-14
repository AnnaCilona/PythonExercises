'''Ejercicio 20. Escriba un programa que calcule el factorial de un número.
Lee antes esto: https://es.wikipedia.org/wiki/Factorial
(El factorial de un entero positivo n se define como el producto
de todos los números enteros positivos desde 1 hasta n)'''

num=int(input("Escribe un número:\n"))
f=1 

for i in range (1,num):
    f=f*(i+1)
    i=i+1

print("El factorial de ", num, "es: ", f)

