'''Ejercicio 3. Escriba un programa que lea dos números desde teclado
y si el primero es mayor que el segundo intercambie sus valores
y los muestre ordenados por pantalla
(después de haber intercambiado el valor de las variables correspondientes).'''

num1=int(input("Escribe un número"))
num2=int(input("Escribe un número"))

if num1>num2:
   num1,num2=num2,num1
   orden=[num1,num2]
   print(sorted(orden))
else:
   print(num1, "es menor que", num2)
