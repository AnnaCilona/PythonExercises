'''Ejercicio 6. Escriba un programa que calcule la cantidad total
de segundos a partir de horas, minutos y segundos pedidos al usuario.'''

from datetime import timedelta

t = input("Escribe hora, minutos y segundos, formato HH:MM:SS")

h,m,s = t.split(':')
print(int(timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()), "segundos")
