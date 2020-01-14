'''Ejercicio 2. Escriba un programa
que determine si un número leído
desde teclado es positivo, negativo, o cero.''' 

num=int(input("Escribe un número"))
        
if num==0:
     print("El número es cero")
elif num<0:
     print("El número es negativo")
else:
     print("El número es positivo")
