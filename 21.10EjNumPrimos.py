#calcular si un num es primo usando funciones


def esPrimo():
    n=int(input("Escribe un número:\n"))
    if n>1:
        contador=0
        for i in range(1,n+1):
            if n%i==0:
                contador=contador+1
        if contador>2:
            print(n, "no es primo")
        else:
            print(n,"es primo")

    else:
        print(n,"no es primo")


esPrimo()
