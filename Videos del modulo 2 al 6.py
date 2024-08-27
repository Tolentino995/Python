#menú de opciones
print("OPCIONES:")
print("[1] Suscribirme")
print("[2] Dejarle a like")
print("[3] Dejar comentario")

#Inicializamos las variables
opcion = 0
intentos = 0

# bucles hasta que introduzca una opcion correcta
while opcion < 1 or opcion > 3:
    opcion = input("Seleccione una opcion")
    try:
        opcion = int(opcion)
    except:
        opcion = 0
    intentos +=1
    if intentos >= 5:
        print("Has agotados el número de intentos")
        break
else:
    print(f"Has escogifo la opcion {opcion}")
