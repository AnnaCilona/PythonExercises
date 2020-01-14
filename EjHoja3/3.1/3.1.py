'''Ejercicio 1. Escribe un programa que traduzca un número romano menor que 4000 a un número en caracteres arábigos y viceversa.'''


def cambiaValores(rom):
    
    if rom=='M':
        return 1000
    if rom=='D':
        return 500
    if rom=='C':
        return 100
    if rom=='L':
        return 50
    if rom=='X':
        return 10
    if rom=='V':
        return 5
    if rom=='I':
        return 1
    
def convierteAarab(numRom):
    result=0
    i=0

    while i<len(numRom):
        s1=cambiaValores(numRom[i])
        print(s1)
        if i+1<len(numRom):
            s2=cambiaValores(numRom[i+1])
     
            
    if s1>=s2:
        result= result+s1
    else:
        result= result+s2-s1













def convierteAroma():
    print("Ciao")



opcion=False

while not opcion:
    eleccion=input("Elige el tipo de conversión que deseas:\n 1) De número romano a arábigo\n 2) De número arábigo a romano\n 3) Salir del programa\n")
    if eleccion=="1":
        convierteAarab(numRom=input("Escribe el número romano para convertir: "))
    elif eleccion=="2":
        convierteAroma()
    elif eleccion=="3":
        print("Hasta luego")
        opcion=True
    else:
        print("Elige entre la opción 1 , 2 o 3")
        opcion=False
        
        
