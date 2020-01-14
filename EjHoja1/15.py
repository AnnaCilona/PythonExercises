'''Ejercicio 15. Escriba un programa que calcule si un año es bisiesto.
Un año es bisiesto si es múltiplo de 4 pero no de 100 aunque sí de 400.'''


a=int(input("Escribe un año, formato AAAA\n"))

if (a%4==0 and a%100!=0) or a%400==0:
    if a<=2019:
        print("El año", a, "fue bisiesto")
    else:
        print("El año", a, "será bisiesto")
else:
    if a<=2019:
        print("El año", a, "no fue bisiesto")
    else:
        print("El año", a, "no será bisiesto")
        
