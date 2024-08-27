archivo = open("archivo_texto.txt", "r",  encoding="utf-8")
#contenido = archivo.read()
for linea in archivo:
    print(linea, end="")
archivo.close()
#print (contenido)
