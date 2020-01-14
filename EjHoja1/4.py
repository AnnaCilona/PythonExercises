'''Ejercicio 4. Escriba un programa que pregunte la edad al usuario,
la fecha actual, y si ha cumplido años en el año actual o no,
y en base a esa información calcule su año de nacimiento.'''


edad=int(input("Cuántos años tienes?"))

fecha=int(input("En qué año estamos?"))

c=input("Has cumplido los años este año?")

if c==("no"):
    edad=edad+1
    
print("Has nacido en el año ",(fecha-edad))

