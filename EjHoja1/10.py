'''Ejercicio 10. Rehaga el ejercicio 8
de forma que también ofrezca un menú.
(Ejercicio 8. Escriba un programa que convierta euros en dólares, y otro que convierta dólares en euros)'''

def Menu():

    opcion= int(input("\nMENÚ: \nElige el tipo de conversión que necesitas:\n 1)De EUR a USD\n 2)De USD a EUR\n 3)Salir del menú\n "))

    if  opcion==1:
        conversorEur()
        Menu()
         
    elif opcion==2:
         conversorUsd()
         Menu()

    elif opcion==3:
         print("Hasta luego")

        

def conversorEur():
    opEUR= int(input("Escribe la cantidad de EUR para convertir:\n"))
    USD= opEUR*1.11
    print (opEUR, "EUR", " = ", USD, "USD")

    
def conversorUsd():
    opUSD= int(input("Escribe la cantidad de USD para convertir:\n"))
    EUR= opUSD*0.9
    print (opUSD, "$", " = ", EUR, "EUR")
    

    
Menu()

