'''Ejercicio 12. Escriba un programa que calcule el equivalente en pies
de una longitud en metros dada por el usuario, teniendo en cuenta
que un metro equivale a 39,27 pulgadas y que 12 pulgadas equivalen a un pie.'''


metros=(int(input("Escribe la longitud en metros para convertir\n")))
pies=(metros*39.27)/12
print (metros, "metros", "=", pies, "pies")

