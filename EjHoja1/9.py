'''Ejercicio 9. Unifique los ejercicios 6 y 7
en un solo programa que te deje elegir al principio
cuál de las dos operaciones hacer, o no hacer ninguna.
Después de dar el resultado te volverá a ese menú inicial.

(Ejercicio 6. Escriba un programa que calcule la cantidad
total de segundos a partir de horas, minutos y segundos pedidos al usuario. 
Ejercicio 7. Escriba un programa que haga lo contrario al ejercicio anterior.)'''


from datetime import timedelta

def menu():

    opcion= int(input("\nElige el tipo de conversión que necesita:\n 1)De HH:MM:SS a SS\n 2)De SS a HH:MM:SS\n 3)Ninguna\n "))

    if opcion==1:
        t = input("Escribe hora, minutos y segundos, formato HH:MM:SS\n")
        h,m,s = t.split(':')
        print(int(timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()), "segundos")
        menu()
         
    elif opcion==2:
        t = input("Escribe segundos\n")
        print(str(timedelta(seconds=int(t))))
        menu()

    elif opcion==3:
        print("Hasta luego")


    
menu()
