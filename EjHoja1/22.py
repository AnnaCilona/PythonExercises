'''Ejercicio 22. Un número entero se dice perfecto si es igual a la suma de sus divisores
(excepto él mismo, pero incluyendo el 1). El primer número perfecto es 6: 6=1+2+3.
Escriba un programa que visualice los 4 primeros números perfectos.'''




def numPerfecto(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
           suma=suma+i
    if (suma==num):
        return True
    else:
        return False
        
n=1
contador=0

while True:
    if numPerfecto(n):
        print(n)
        contador=contador+1
        if contador==4:
                break
    n=n+1
            
