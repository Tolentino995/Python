lista = ["Pepito", "Joselito", "Gervasio"]
archivo = open("archivo_texto.txt", "a", encoding="utf-8")

for nombre in lista:
    archivo.write(nombre+"\n")
archivo.close()