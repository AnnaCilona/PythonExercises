'''Ejercicio 2. Escribe un programa que acepte una hora en formato militar y la transforme al formato habitual (horas, minutos y AM/PM) y viceversa'''


import datetime


def convierteAhabitual():
    horaMil=list(input("Escribe hora en formato militar (HHMM) 24horas: "))

    horaMil=[horaMil[i]+horaMil[i+1] for i in range(0,len(horaMil),2)]

    hora=str(":".join(horaMil))

    horaHabitual=datetime.datetime.strptime(hora,"%H:%M").strftime("%I:%M %p")

    print(horaHabitual)


def convierteAmil():
    hora=input("Escribe hora en formato habitual (HH:MM AM/PM) 12horas: ")
    horaHabitual=(datetime.datetime.strptime(hora,"%I:%M %p").strftime("%H%M"))

    print("".join(horaHabitual))
   




opcion=False

while not opcion:
    eleccion=input("Elige el tipo de conversión que deseas:\n 1) De hora militar a habitual\n 2) De hora habitual a militar\n 3) Salir del programa\n")
    if eleccion=="1":
        convierteAhabitual()
    elif eleccion=="2":
        convierteAmil()
    elif eleccion=="3":
        print("Hasta luego")
        opcion=True
    else:
        print("Elige entre la opción 1 , 2 o 3")
        opcion=False
        
        


    
    
