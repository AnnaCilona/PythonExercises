'''Ejercicio 13. Escriba un programa que convierta grados Celsius en Fahrenheit y viceversa,
a elección del usuario. La relación entre ambos es F=(9/5)*C+32.'''


def menu():

    opcion=int(input("\nElige el tipo de conversión que necesitas:\n 1)De ºC a ºF\n 2)De ºF a ºC\n 3) Salir del programa\n"))

    if opcion==1:
       conversorC()
       menu()

    if opcion==2:
       conversorF()
       menu()
        
    if opcion==3:
       print("Hasta luego")



    
def conversorC():
    userC=float(input("\nEscribe la temperatura en ºC para convertir a ºF:\n"))
    f= (userC*1.8)+32
    print(userC, "ºC", "=", f, "ºF")

def conversorF():
    userF=float(input("\nEscribe la temperatura en ºF para convertir a ºC:\n"))
    c= (userF -32)/1.8
    print(userF, "ºF", "=" , c, "ºC")



menu()



