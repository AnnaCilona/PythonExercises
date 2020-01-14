'''Ejercicio 17. Escriba un programa que pida dos números enteros
y nos muestre la tabla de multiplicar del primero
hasta el número que indique el segundo.'''


n1,n2=input("Escribe dos números enteros separados por un espacio").split()
contador=0
num1=int(n1)
num2=int(n2)

for i in range (0,num2):
    print(num1, "*", contador, "=", (num1*contador))
    contador=contador+1
