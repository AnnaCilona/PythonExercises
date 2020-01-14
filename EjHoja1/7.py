'''Ejercicio 7. Escriba un programa que calcule la cantidad total
de horas, minutos y segundos a partir de segundos pedidos al usuario.'''

from datetime import timedelta

t = input("Escribe segundos")

print(str(timedelta(seconds=int(t))))
