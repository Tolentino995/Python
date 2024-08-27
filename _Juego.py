# importamos lo módulos necesarios 
import random
import platform
import os

# LIMPIA LA PANTALLA

def limpiar_pantalla():
    so = platform.system()
    if so == "Windows": # si es windows
        os.system("cls") # comando de Windows para limpiar pantalla
    elif os == "Linux": # si es Linux
        os.system("clear") # comando de Linux para limpiar pantalla


#### MAIN ####

if __name__ == '__main__':
    limpiar_pantalla()
    # el jugador 1 introduce una frase
    frase = input ("Jugador 1: Escribe una frase: ")
    # convertimos las palabras de la frase en una lista
    lista_frase = frase.split()
    # desordenamos las palabras de la frase
    random.shuffle(lista_frase)
    # convertimos la lista en un string 
    frase_desordenada = " ".join(lista_frase)
    # limpiamos la pantalla para que el jugador 2 no pueda ver la frase original
    limpiar_pantalla()
    # bucle infinito hasta que el jugador 2 adivina la frase
    intentos = 0
    while True: 
        #mostramos la frase con las palabras desordenadas
        print(frase_desordenada.upper())
        # el jugador 2 introduce la frase
        intentos += 1# incrementa mas 1
        frase2 = input("Jugador 2: Adivina la frase: ")
        #comprobamos si es la misma frase que la original
        if frase.lower() == frase2.lower(): # si es la misma frase (sin tener en cuenta las mayúsculas)
            print(f'¡Enhorabuena Has acertado en {intentos} intentos!')
            break # salimos del bucle
        else: # si no es la misma frase
            print(f'¡Has fallado! Intentos: {intentos}')
        print()# espacio para no amontonar los intentos
