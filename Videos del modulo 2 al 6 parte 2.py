# inicializamos las variables 

a = 0
b = 0

# bucle infinito while

while True:
    # solicitamos "a"
    a = input("Introduce el primer número: ")
    # solicitamos "b"
    b = input("Introduce el segundo número: ")
    # convertimos los datos introducidos a tipo "float"

    try:
        a = float(a)
        b = float(b)
        # realizamos la división
        division = a / b
    except ValueError:
        print("ERROR: Debes introducir números")
        print()
    except ZeroDivisionError:
        print("ERROR: No se puede dividir por 0")
        print()
    except:
        print("ERROR DESCONOCIDO")
        print()
        exit()
    else:
        # mostramos el resultado
        print(f"{a}/{b}={division}")
        break # salimos del bucle
