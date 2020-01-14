'''Ejercicio 8. Escriba un programa que convierta euros en dólares,
y otro que convierta dólares en euros'''

def conversorMoneda():

    opcion= int(input("Elige el tipo de conversión que necesita:\n 1)De EUR a USD\n 2)De USD a EUR\n "))

    if opcion==1:
         opEUR= int(input("Escribe la cantidad de EUR para convertir\n"))
         USD= opEUR*1.11
         print (opEUR, "EUR", " = ", USD, "USD")
         
    elif opcion==2:
        opUSD= int(input("Escribe la cantidad de USD para convertir\n"))
        EUR= opUSD*0.9
        print (opUSD, "$", " = ", EUR, "EUR")



conversorMoneda()
