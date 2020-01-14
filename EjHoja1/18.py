'''Ejercicio 18. Se definen los números triangulares como los obtenidos
de sumar los números naturales sucesivos 1, 2, 3 …
Es decir, los primeros números triangulares son 1, 3, 6, 10, etc.
Escriba un programa que nos diga si un número es o no triangular'''



n=int(input("Escribe un número\n"))
a=0
x=1
for i in range(0,n) :
    a=a+(i+1)
    i=i+1
    if(n==a):
        print("El numero ", n, " es triangular.")
        x=0    
if x==1:
    print("El numero ", n, "no es triangular.")









