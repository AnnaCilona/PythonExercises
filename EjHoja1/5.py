'''Ejercicio 5. Escriba un programa que pregunte la edad al usuario,
la fecha actual, y en qué día y mes es su cumpleaños,
y en base a esa información calcule su año de nacimiento.'''


edad=int(input("Cuántos años tienes?"))


diaHoy=int(input("Qué día es hoy?"))



mesHoy=int(input("En qué mes estamos? (En número)"))


fecha=int(input("En qué año estamos?"))


dia=int(input("Qué día cumples los años?"))



mes=int(input("En qué mes cumples los años? (En número)"))


if mesHoy<mes:
    edad=edad+1
elif mesHoy==mes:
     if diaHoy<dia:
         edad=edad+1


    
print("Has nacido en el año ",(fecha-edad))
