'''Ejercicio 11. Rehaga el ejercicio 3 con 3 números'''

'''Ejercicio 3. Escriba un programa que lea dos números desde teclado
y si el primero es mayor que el segundo intercambie sus valores
y los muestre ordenados por pantalla
(después de haber intercambiado el valor de las variables correspondientes).'''


num1=int(input("Escribe un número"))
num2=int(input("Escribe un número"))
num3=int(input("Escribe un número"))

if num1>num2&num1>num3&num2<num3:
   num1,num2,num3=num3,num2,num1
   lista=[num1,num2,num3]
   print(sorted(lista))

