valores=[  (1,'I'),
(5,'V'),
(10,'X'),
(50,'L'),
(100,'C'),
(500,'D'),
(1000,'M'),
]
def romantonumeral():
    numRom=input("Escribe el número romano para convertir: ")
    result=0
    for i in range(0,len(numRom)):
        for letra in valores:
            if numRom[i]==letra[1]:
                if letra[0]>result:
                    result=letra[0]-result
                else:
                    result=result+letra[0]
    print (result)
    return result
    


romantonumeral()
