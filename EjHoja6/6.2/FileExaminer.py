'''Ejercicio 2. Escribe un programa que analice el fichero de texto cuyo nombre se especifica interactivamente y muestre por pantalla la siguiente información:
	a) Para cada línea del fichero:
		• El número total de caracteres y de palabras, y la longitud media de una palabra.
		• La letra con que termina la primera palabra y el número de palabras que terminan con esa letra.
	b) Para el fichero completo:
		• El número total de caracteres, palabras y líneas del fichero, y la longitud media de una palabra.
		• El número de la línea en la que hay más palabras, junto con el número de palabras en esa línea.'''

class FileExaminer:
	
	from io import open

	def __init__(self):
			pass

	def analiza(self):
		from operator import truediv 
		import string

		myFile= open ("C:\\Users\\Anna Cilona\\Desktop\\Python\\Ejercicios\\EjHoja6\\6.2\\Odissea.txt","r", encoding="utf-8")
		listaLineas=myFile.readlines()

		almacen=0
		numLinea=0
		contaLineas=0
		contaPalabrasTotales=0
		contaCaracteresTotales=0
		longitudPalabra=0
		numPalabrasporLinea=[]
		listaLenCharporLinea=[]
		longPalporLinea=[]
		listaUltimaLetraPalabra=[]
		#listaOccurrencesUltimaLetra=[]

		for i in range(len(listaLineas)):
			longPal=0
			contaLineas=contaLineas+1
			listaPalabras=listaLineas[i].split()
			if listaPalabras[0][-1].isalpha():
				listaUltimaLetraPalabra.append(listaPalabras[0][-1].lower())
			else:
				listaUltimaLetraPalabra.append(listaPalabras[0][-2].lower())
			 
			contaPalabrasTotales=contaPalabrasTotales+len(listaPalabras)
			numPalabrasporLinea.append(len(listaPalabras))
			if almacen<len(listaPalabras):
				almacen=len(listaPalabras)
				numLinea=i+1
			listaLetras=[]
			
			
			for j in range(len(listaPalabras)):				
				longitudPalabra=longitudPalabra+len(listaPalabras[j])
				longPal=longPal+len(listaPalabras[j])
				listaLetrasConPunctuacion=list(listaPalabras[j])
				for letra in listaLetrasConPunctuacion:
					if letra not in string.punctuation:
						listaLetras.append(letra)
			listaLenCharporLinea.append(len(listaLetras))
			contaCaracteresTotales=contaCaracteresTotales+len(listaLetras) 
			longPalporLinea.append(longPal)
			

			'''for j in range(len(listaPalabras)):		
				for k in range (len(listaUltimaLetraPalabra)):
					letra=listaUltimaLetraPalabra[k]
					occurrence=listaPalabras[j].count(letra)
					listaOccurrencesUltimaLetra.append(occurrence)
					occurrence=0
			listaOccurrencesUltimaLetra.append("*")
		
		print(listaLineas[0])
		letra=listaLineas[0][-1].count(listaUltimaLetraPalabra[0])
		print(letra)'''




		print("Para el fichero completo:\n")
		print("Número total de lineas del fichero: ", contaLineas)
		print("Número total de palabras del fichero: ", contaPalabrasTotales)
		print("Número total de carácteres del fichero: ", contaCaracteresTotales)
		print("Longitud media de una palabra: " , (longitudPalabra/contaPalabrasTotales)) #habría que quitar signos de punctuación
		print("Número de la línea en la que hay más palabras: " , numLinea)
		print("Número de palabras en esa línea: " , almacen , "\n")

		print("Para cada línea del fichero:\n")
		print("Número total de palabras para cada linea:")
		for i in range(len(numPalabrasporLinea)):
			print("Linea ", i , ": " , numPalabrasporLinea[i])

		print("Número total de carácteres por cada línea:")
		for i in range(len(listaLenCharporLinea)):
			print("Linea ", i , ": " , listaLenCharporLinea[i])

		print("Longitud media de una palabra por linea:")
		res = list(map(truediv, longPalporLinea, numPalabrasporLinea)) 
		for i in range(len(res)):
			print("Linea ", i , ": " , res[i])

		
		

		
		

		myFile.close()
		





		






	
