contadorPrimos = 0
contadorNumeros = 1

def siEsPrimo(n):
    if n==1:
        return True
    if n==2:
        return True
    else:
        contador=0
        for i in range(1,n+1):
            if n%i==0:
               contador=contador+1
            if contador>2:
                return False          
        return True

while contadorPrimos < 20:
    if(siEsPrimo(contadorNumeros)):
        print(contadorNumeros)
        contadorPrimos+=1
    contadorNumeros+=1



      
            
