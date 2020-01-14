'''Ejercicio 3. Crea una lista, pide al usuario definir cuantos elementos va a tener y haz que la rellene de números dinámicamente.
Tiene prohibido escribir cualquier cosa que no sean enteros.'''


lista=[]
tamCorrecto=False

while not tamCorrecto:
    tamanyo=input("Escribe el número de elementos que va a tener la lista: \n")
    try:
        num=int(tamanyo)
        if num>0:
            tamCorrecto=True
        else:
            print("Se aceptan sólo números mayores que cero")
    except ValueError:
        print("No has escrito un número")

print("Debes introducir " + tamanyo + " numeros.")

for i in range (0,int(tamanyo)):
    numCorrecto=False
    while not numCorrecto:
        try:
            num=int(input("Introduce el n " +str(i+1) + " de " + str(tamanyo) + ":\n"))
            lista.append(num)
            i=i+1
            numCorrecto=True
        except ValueError:
            print("No has escrito un número")

print("Tu lista es: " ,lista)
