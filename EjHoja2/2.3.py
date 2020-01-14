'''Ejercicio 3. Escriba un programa que sirva para examinar a un niño de las tablas de multiplicar.
Para ello se generan de forma pseudoaleatoria diez preguntas que son planteadas al niño.
Ante cada pregunta (por ejemplo “4x5=”) el niño contestará con un número.
Si la respuesta es la correcta se le felicita.
Si la respuesta es incorrecta se le informará al niño de su error
y se le volverá a plantear la misma pregunta hasta que acierte.
Después de concluir con la última pregunta se informará al niño
sobre cuántas preguntas acertó a la primera.'''

import random
def resCorrectaPrimera():
    print("Has acertado a la primera. ¡Muy bien!")


def resCorrecta():
    print("Respuesta correcta. ¡Muy bien!")

def resIncorrecta():
    print("La respuesta es incorrecta, intenta de nuevo.")

aciertos=0

                          
for i in range(0,10):
    n1=random.randrange(0,10,1)
    n2=random.randrange(0,10,1)
    respuesta=int(input("Escribe el resultado de: "+ str(n1)+ "x" + str(n2)+ "\n"))
    acertado=respuesta==(n1*n2)
    if acertado:
        resCorrectaPrimera()
        aciertos=aciertos+1
    while not acertado:
        resIncorrecta()
        respuesta=int(input("Escribe el resultado de: "+ str(n1)+ "x" + str(n2) + "\n"))
        acertado=respuesta==(n1*n2)
        if acertado:
            resCorrecta()


        
print("Has acertado a la primera", aciertos,  "preguntas.")


